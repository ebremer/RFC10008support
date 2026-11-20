"""Star counts from ungh.cc (exact, no GitHub API quota).

usage: python -I -X utf8 tools/refresh/stars.py
           every row's stack repo (from rows.json) -> stars.json
       python -I -X utf8 tools/refresh/stars.py owner/repo [owner/repo ...]
           the named repos (e.g. candidates for new rows) -> extra_stars.json, printed
"""
import concurrent.futures as cf
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import API_UA, fetch, load, save  # noqa: E402

if len(sys.argv) > 1:
    repos, outname = sys.argv[1:], "extra_stars.json"
else:
    repos, outname = sorted({r["repo"] for r in load("rows.json") if r["repo"]}), "stars.json"


def one(repo):
    code, _, s = fetch(f"https://ungh.cc/repos/{repo}", ua=API_UA, accept="application/json", timeout=30)
    try:
        d = json.loads(s)["repo"]
        return repo, d.get("stars"), (d.get("description") or "")[:80]
    except (ValueError, KeyError, TypeError):
        return repo, None, ""


out = {}
with cf.ThreadPoolExecutor(6) as ex:
    for repo, n, desc in ex.map(one, repos):
        out[repo] = n
        if outname == "extra_stars.json":
            print(f"{repo:<50} {n}  {desc}")
save(outname, out)
print(len(out), "repos; missing:", [k for k, v in out.items() if v is None])
