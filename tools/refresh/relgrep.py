"""Print the QUERY-related context in release notes published since SINCE.

usage: python -I -X utf8 tools/refresh/relgrep.py SINCE [owner/repo ...]
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import load  # noqa: E402

if len(sys.argv) < 2:
    sys.exit(__doc__)
SINCE = sys.argv[1]
only = set(sys.argv[2:]) or None
rel = load("releases.json")
QRE = re.compile(r"\bQUERY\b|10008|query method|HttpMethod\.Query|MethodQuery|\.query\(|"
                 r"Route::query|http\.query", re.I)

for repo, d in sorted(rel.items()):
    if only and repo not in only:
        continue
    for e in d["releases"]:
        if e["updated"] < SINCE:
            continue
        b = e["body"]
        hits = [m.start() for m in QRE.finditer(b)]
        if not hits:
            continue
        print(f"## {repo} {e['link'].rsplit('/', 1)[-1]} {e['updated'][:10]}")
        last = -1000
        for h in hits:
            if h - last < 150:
                continue
            last = h
            print("   ..", b[max(0, h - 160):h + 200].replace("\n", " "))
