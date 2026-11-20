"""Apply a refresh's README edits from an edits file, all or nothing.

The edits file is Python. It calls e(old, new) for each change and may fill
NEW with whole rows to append, keyed by section heading:

    e(r'''Last refreshed **2026-11-13** (day **+150**).''',
      r'''Last refreshed **2026-11-20** (day **+157**).''')
    e(r'''| PHP / C | ✅ Merged (8.6 RC) |''', r'''| PHP / C | ✅ Released (8.6.0) |''')
    NEW["Clients (outbound)"] = [r'''| [**Name**](https://github.com/o/r) | Lang | ⚠️ Open | 1,234 | ... |''']

Every `old` must occur exactly once in README.md, or nothing is written and
the misses are listed; keep `old` short but unique (include the row's name or
a neighbouring cell when a phrase repeats). New rows go at the end of their
section's table; stars_sort.py then puts them in star order.

usage: python -I -X utf8 tools/refresh/apply_edits.py EDITS.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import README, readme  # noqa: E402

if len(sys.argv) != 2:
    sys.exit(__doc__)
E, NEW = [], {}
with open(sys.argv[1], encoding="utf-8") as f:
    exec(compile(f.read(), sys.argv[1], "exec"), {"e": lambda old, new: E.append((old, new)), "NEW": NEW})

md = readme()
bad = []
for old, new in E:
    n = md.count(old)
    if n != 1:
        bad.append((n, old[:140]))
        continue
    md = md.replace(old, new)
if bad:
    for n, o in bad:
        print(f"MATCH {n}: {o}")
    sys.exit(1)

nrows = sum(len(v) for v in NEW.values())
out, section, in_table = [], None, False
for line in md.split("\n"):
    if line.startswith("## "):
        section = line[3:].strip()
    is_row = line.startswith("|")
    if in_table and not is_row:
        out.extend(NEW.pop(section, []))
        in_table = False
    in_table = in_table or is_row
    out.append(line)
if NEW:
    print("no table found for sections:", list(NEW))
    sys.exit(1)
with open(README, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(out))
print(f"applied {len(E)} edits; inserted {nrows} rows")
