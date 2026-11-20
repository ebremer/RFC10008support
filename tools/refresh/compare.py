"""Compare scraped states with the README's claims, and list recent activity.

The first list is every item whose state differs from what the README says
right after its link ("— open", "— **merged**", ...). Known false positives:
Spring #34993 ("closed, applied by maintainer") and http-kit #618 ("merged by
hand"). The second list is every item with activity since SINCE; the times
come from the page and include CI noise and cross-references, so read each
one with peek.py before writing anything.

usage: python -I -X utf8 tools/refresh/compare.py SINCE [states.json]
       SINCE = ISO time of the last refresh, e.g. 2026-11-13T14:00
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import load, readme  # noqa: E402

if len(sys.argv) < 2:
    sys.exit(__doc__)
SINCE = sys.argv[1]
states = load(sys.argv[2] if len(sys.argv) > 2 else "states.json")
urls = load("urls.json")
md = readme()

MAP = {"pullMerged": "merged", "pullOpened": "open", "draft": "open", "pullClosed": "closed",
       "issueOpened": "open", "issueClosed": "closed", "issueClosedNotPlanned": "closed"}


def claims(it):
    o, r, k, n = it.split("/")
    url = f"https://github.com/{o}/{r}/{k}/{n}"
    out = []
    for m in re.finditer(re.escape(url) + r"\)", md):
        tail = md[m.end():m.end() + 60]
        out.append(re.split(r"\[|·|\|", tail)[0].strip())
    return out


def claimed_state(cl):
    for c in cl:
        c2 = c.lower().replace("*", "")
        if not c2.startswith(("—", "-")):
            continue
        if any(w in c2 for w in ("unmerged", "not planned", "duplicate", "superseded", "replaced")):
            return "closed"
        if "merged" in c2 or "applied" in c2:
            return "merged"
        if "closed" in c2:
            return "closed"
        if "open" in c2:
            return "open"
    return None


mism, recent = [], []
for it, rec in states.items():
    st = MAP.get(rec.get("status"))
    cs = claimed_state(claims(it))
    if cs and st and cs != st:
        mism.append((it, cs, rec.get("status"), urls.get(it)))
    act = rec.get("updatedAt") if "/issues/" in it else rec.get("maxdt")
    if "/pull/" in it and rec.get("updatedAt"):
        act = max(act or "", rec["updatedAt"])
    if act and act >= SINCE:
        recent.append((act, it, rec.get("status"), urls.get(it)))

print("== state mismatches vs README ==")
for x in mism:
    print(*x)
print("\n== activity since", SINCE, "==")
for x in sorted(recent):
    print(*x)
print(len(recent), "recent")
