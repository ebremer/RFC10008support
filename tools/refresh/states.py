"""Fetch every tracked issue/PR/discussion page and record its state.

Saves each page under work/html/ (the other scripts read the narrative from
there) and writes, per item: HTTP code, status (data-status: pullMerged,
pullOpened, pullClosed, draft, issueOpened, issueClosed, issueClosedNotPlanned),
latest updatedAt / datetime seen, merge sha (old-style pages only) and title.

usage: python -I -X utf8 tools/refresh/states.py [items.json] [out.json]
       defaults: urls.json -> states.json (about 2 minutes for ~460 items)
"""
import concurrent.futures as cf
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import fetch, html_path, load, save  # noqa: E402

src = sys.argv[1] if len(sys.argv) > 1 else "urls.json"
outname = sys.argv[2] if len(sys.argv) > 2 else "states.json"
items = list(load(src))


def one(it):
    o, r, kind, n = it.split("/")
    code, final, s = fetch(f"https://github.com/{o}/{r}/{kind}/{n}")
    if s:
        with open(html_path(it), "w", encoding="utf-8") as f:
            f.write(s)
    rec = {"code": code, "final": final}
    m = re.search(r'data-status="([^"]+)"', s)
    rec["status"] = m.group(1) if m else None
    ups = re.findall(r'"updatedAt":"([^"]+)"', s)
    rec["updatedAt"] = max(ups) if ups else None
    dts = re.findall(r'datetime="(\d{4}-\d\d-\d\dT[^"]+)"', s)
    rec["maxdt"] = max(dts) if dts else None
    m = (re.search(r'merged commit <a[^>]*href="[^"]*/commit/([0-9a-f]{40})', s)
         or re.search(r'merged commit\s*<a[^>]*>\s*<code[^>]*>([0-9a-f]{7,40})', s))
    rec["merge_sha"] = m.group(1) if m else None
    m = re.search(r'"mergedTime":"([^"]+)"', s)  # newer React PR pages: no sha, but a time
    rec["merged_time"] = m.group(1) if m else None
    m = re.search(r"<title>(.*?)</title>", s, re.S)
    rec["title"] = m.group(1).strip() if m else None
    if kind == "discussions":
        m = re.search(r"(\d+)\s+comments?", s)
        rec["comments"] = m.group(0) if m else None
        rec["closed"] = ("State--closed" in s) or ('"closed":true' in s)
    return it, rec


out = {}
with cf.ThreadPoolExecutor(6) as ex:
    for it, rec in ex.map(one, items):
        out[it] = rec
save(outname, out)
bad = [k for k, v in out.items() if not v["status"] and "discussions" not in k]
print(len(out), "fetched;", len(bad), "without status:", bad[:20])
