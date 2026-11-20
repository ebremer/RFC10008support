"""Fetch releases.atom and tags.atom for every tracked repo.

Each feed holds only the newest ~10 entries, so run this every refresh.
Atom <updated> can be an edit time; get exact dates with tagdate.py.

usage: python -I -X utf8 tools/refresh/releases.py [repos.json] [out.json]
       defaults: repos.json -> releases.json
"""
import concurrent.futures as cf
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import fetch, load, save  # noqa: E402

repos = load(sys.argv[1] if len(sys.argv) > 1 else "repos.json")
outname = sys.argv[2] if len(sys.argv) > 2 else "releases.json"


def parse(s):
    out = []
    for e in re.findall(r"<entry>(.*?)</entry>", s, re.S):
        t = re.search(r"<title>(.*?)</title>", e, re.S)
        u = re.search(r"<updated>(.*?)</updated>", e)
        lk = re.search(r'<link[^>]*href="([^"]+)"', e)
        c = re.search(r"<content[^>]*>(.*?)</content>", e, re.S)
        body = re.sub(r"<[^>]+>", " ", html.unescape(html.unescape(c.group(1)))) if c else ""
        out.append({"title": html.unescape(t.group(1).strip()) if t else "",
                    "updated": u.group(1) if u else "",
                    "link": lk.group(1) if lk else "",
                    "body": re.sub(r"\s+", " ", body)[:20000]})
    return out


def one(repo):
    rel = parse(fetch(f"https://github.com/{repo}/releases.atom", tries=3, accept="*/*")[2])
    tags = parse(fetch(f"https://github.com/{repo}/tags.atom", tries=3, accept="*/*")[2])
    for t in tags:
        t["body"] = ""
    return repo, {"releases": rel, "tags": tags}


out = {}
with cf.ThreadPoolExecutor(6) as ex:
    for repo, rec in ex.map(one, repos):
        out[repo] = rec
save(outname, out)
print(len(out), "repos;", sum(1 for v in out.values() if not v["releases"] and not v["tags"]), "with nothing")
