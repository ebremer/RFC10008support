"""List every release and tag since SINCE for the tracked repos.

Check each one against its row's "shipped without" / "carried in" / "latest"
claims. Lines are marked:
  name-in-README  the tag name appears somewhere in the README. This does NOT
                  mean the row already covers it (v2.2.0 or 7.1.0 can match an
                  unrelated row), so never filter these lines out.
  QUERY:n         the release notes match a QUERY pattern n times; mostly
                  query-string noise, read them with relgrep.py.

usage: python -I -X utf8 tools/refresh/newrel.py SINCE [releases.json]
       SINCE = date of the last refresh, e.g. 2026-11-13
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import load, readme  # noqa: E402

if len(sys.argv) < 2:
    sys.exit(__doc__)
SINCE = sys.argv[1]
rel = load(sys.argv[2] if len(sys.argv) > 2 else "releases.json")
md = readme()
QRE = re.compile(r"\bQUERY\b|10008|query method|HttpMethod\.Query|MethodQuery", re.I)

for repo, d in sorted(rel.items()):
    seen, lines = set(), []
    for kind in ("releases", "tags"):
        for e in d[kind]:
            if e["updated"] < SINCE:
                continue
            name = e["link"].rsplit("/", 1)[-1]
            if name in seen:
                continue
            seen.add(name)
            q = QRE.findall(e["body"]) if kind == "releases" else []
            inmd = "name-in-README" if (e["title"] in md or name in md) else ""
            lines.append(f"   {kind[0]} {e['updated'][:10]} {name} | {e['title'][:60]} {inmd} "
                         f"{'QUERY:' + str(len(q)) if q else ''}")
    if lines:
        print(repo)
        print("\n".join(lines))
