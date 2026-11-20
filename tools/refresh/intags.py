"""For every merged PR with a merge sha, list the branches and tags that contain it.

Uses github.com/{o}/{r}/branch_commits/{sha} (no API quota). Tags come back in
lexicographic order, not by date; firstrel.py sorts them by version. Known
blind spots: some shas get no tags at all even though the change shipped
(Netty's 4.1 backport, Apache HttpClient #852, Swoole #6256), and newer React
PR pages expose no sha (Kiota, VueUse, Scalar) — confirm those with rawgrep.py.

usage: python -I -X utf8 tools/refresh/intags.py [states.json ...]
       output: intags.json for the default states.json, otherwise
       intags_<first input name>.json, so a second run never overwrites the first
"""
import concurrent.futures as cf
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import fetch, load, save  # noqa: E402

inputs = sys.argv[1:] or ["states.json"]
outname = "intags.json" if inputs == ["states.json"] else \
    "intags_" + os.path.splitext(os.path.basename(inputs[0]))[0] + ".json"
items = {}
for f in inputs:
    for k, v in load(f).items():
        if v.get("merge_sha"):
            items[k] = v["merge_sha"]


def one(kv):
    it, sha = kv
    o, r = it.split("/")[:2]
    code, _, s = fetch(f"https://github.com/{o}/{r}/branch_commits/{sha}")
    if not s:
        return it, {"sha": sha, "error": code}
    br = re.findall(r'<li class="branch"><a [^>]*>([^<]+)</a>', s)
    tags = re.findall(r'/releases/tag/[^"]+">([^<]+)</a>', s)
    more = re.search(r"(\d+)\s+more", s)
    return it, {"sha": sha, "branches": br, "tags": tags, "more": more.group(0) if more else None}


out = {}
with cf.ThreadPoolExecutor(6) as ex:
    for it, rec in ex.map(one, items.items()):
        out[it] = rec
save(outname, out)
print(len(out), "merged PRs;", sum(1 for v in out.values() if v.get("error") is not None), "errors ->", outname)
