"""Show search.py hits whose title really names the method, marking untracked ones NEW.

Keeps titles matching \\bQUERY\\b (case-sensitive) or RFC 10008. With --cand,
also writes the NEW items to cand.json, ready for states.py / summ.py.

usage: python -I -X utf8 tools/refresh/showsearch.py [--cand] search_created.json [search_updated.json ...]
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import load, save  # noqa: E402

args = sys.argv[1:]
cand = "--cand" in args
args = [a for a in args if a != "--cand"]
if not args:
    sys.exit(__doc__)
known = set(load("urls.json"))
hits = {}
for f in args:
    hits.update(load(f))
new = {}
for u, v in sorted(hits.items(), key=lambda kv: kv[1]["created"]):
    t = v["title"]
    if not (re.search(r"\bQUERY\b", t) or re.search(r"(?i)rfc[ -]?10008", t)):
        continue
    mark = "   " if u in known else "NEW"
    if mark == "NEW":
        new[u] = []
    print(mark, v["created"], v["updated"], v["state"], "PR" if v["pr"] else "IS", u, "|", t[:110])
if cand:
    save("cand.json", new)
    print(len(new), "new items -> cand.json")
