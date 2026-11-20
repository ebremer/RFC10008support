"""Write star counts into README.md, sort each ★ table by stars, and check cell counts.

Every table row whose first cell links a GitHub repo gets that repo's count from
stars.json (plus any extra files named, e.g. extra_stars.json for new rows).
A row whose repo has no count keeps its old value. Each table with a ★ Stars
column is then stable-sorted, highest first, non-numeric last. Rows whose cell
count differs from the header are reported (a literal " | " in a cell breaks
the table) — fix those before committing.

usage: python -I -X utf8 tools/refresh/stars_sort.py [extra_stars.json ...]
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import README, load, readme  # noqa: E402

stars = {}
for f in ["stars.json"] + sys.argv[1:]:
    stars.update({k.lower(): v for k, v in load(f).items() if v is not None})

LINK = re.compile(r"^\[[^\]]*\]\(https://github\.com/([^/]+)/([^/#?)]+)/?\)")
lines = readme().split("\n")
out, i, changed, problems = [], 0, 0, []
while i < len(lines):
    if not lines[i].startswith("|"):
        out.append(lines[i])
        i += 1
        continue
    j = i
    while j < len(lines) and lines[j].startswith("|"):
        j += 1
    block = lines[i:j]
    header = [c.strip() for c in block[0].strip().strip("|").split(" | ")]
    body = block[2:]
    for r in body:
        n = len(r.strip().strip("|").split(" | "))
        if n != len(header):
            problems.append((n, len(header), r[:100]))
    if "★ Stars" in header:
        si = header.index("★ Stars")
        rows = []
        for r in body:
            cells = [c.strip() for c in r.strip().strip("|").split(" | ")]
            m = LINK.match(cells[0])
            if m:
                key = f"{m.group(1)}/{m.group(2)}".lower()
                if key in stars and cells[si] != f"{stars[key]:,}":
                    cells[si] = f"{stars[key]:,}"
                    changed += 1
            rows.append(cells)

        def k(c):
            v = c[si].replace(",", "")
            return (0, -int(v)) if v.isdigit() else (1, 0)
        body = ["| " + " | ".join(c) + " |" for c in sorted(rows, key=k)]
    out.extend(block[:2] + body)
    i = j

with open(README, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(out))
print("star cells changed:", changed)
for p in problems:
    print("CELLCOUNT", p)
