"""Count a pattern in one source file at several tags: the reliable "did it ship?" check.

Use it when intags.py finds no tags for a merge (or no sha): grep the file the
PR changed at the tags before and after it, via raw.githubusercontent.com.

usage: python -I -X utf8 tools/refresh/rawgrep.py PATTERN owner/repo path/in/repo tag [tag ...]
example: rawgrep.py '"QUERY"' swoole/swoole-src src/protocol/http.cc v6.1.10 v6.1.11
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import API_UA, fetch  # noqa: E402

if len(sys.argv) < 5:
    sys.exit(__doc__)
pat, repo, path, tags = re.compile(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4:]
for tag in tags:
    code, _, s = fetch(f"https://raw.githubusercontent.com/{repo}/{tag}/{path}", tries=2, ua=API_UA, accept="*/*")
    if not s:
        print(f"{tag:<24} HTTP {code} (missing file or tag)")
        continue
    lines = [(i, ln.strip()) for i, ln in enumerate(s.splitlines(), 1) if pat.search(ln)]
    first = f"  first: {lines[0][0]}: {lines[0][1][:100]}" if lines else ""
    print(f"{tag:<24} {len(lines)} matching lines{first}")
