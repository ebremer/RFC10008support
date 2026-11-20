"""Grouped per-repo title sweep for QUERY (search API; about 16 groups of ~35 repos).

Searches `QUERY in:title created:>=SINCE repo:a repo:b ...` over every tracked
repo (work/repos.json) plus tools/refresh/extra_repos.txt, up to 3 pages a
group, then keeps titles matching \\bQUERY\\b case-sensitively. Repos whose
issue titles say "query" all the time (SWAMP) would fill a group's results, so
they are left out here; search them with exact phrases instead.

usage: python -I -X utf8 tools/refresh/repo_search.py SINCE [repos.txt]
       SINCE = date a day before the last refresh, e.g. 2026-11-12
"""
import json
import os
import re
import sys
import time
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import API_UA, HERE, fetch, load  # noqa: E402

SWAMP = {"clickhouse/clickhouse", "quarkusio/quarkus", "prometheus/prometheus", "trinodb/trino", "grafana/loki"}

if len(sys.argv) < 2:
    sys.exit(__doc__)
since = sys.argv[1]
if len(sys.argv) > 2:
    names = [ln.strip() for ln in open(sys.argv[2]) if ln.strip() and not ln.startswith("#")]
else:
    names = load("repos.json")
    names += [ln.strip() for ln in open(os.path.join(HERE, "extra_repos.txt"))
              if ln.strip() and not ln.startswith("#")]
seen, repos = set(), []
for r in names:
    if r.lower() not in seen and r.lower() not in SWAMP:
        seen.add(r.lower())
        repos.append(r)
known = set(load("urls.json"))

groups, cur = [], []
for r in repos:
    cur.append(r)
    if len(" ".join("repo:" + x for x in cur)) > 800:
        groups.append(cur)
        cur = []
if cur:
    groups.append(cur)

hits = {}
for gi, g in enumerate(groups):
    q = f"QUERY in:title created:>={since} " + " ".join("repo:" + x for x in g)
    items = []
    for pg in (1, 2, 3):
        url = "https://api.github.com/search/issues?" + urllib.parse.urlencode(
            {"q": q, "per_page": 100, "sort": "created", "page": pg})
        code, _, s = fetch(url, tries=2, ua=API_UA, accept="application/vnd.github+json")
        try:
            d = json.loads(s)
        except ValueError:
            print("ERR", g[:3], code, file=sys.stderr)
            d = {}
        items += d.get("items", [])
        print(f"group {gi} p{pg}: {len(g)} repos, total {d.get('total_count')}", file=sys.stderr)
        time.sleep(7)
        if len(items) >= (d.get("total_count") or 0):
            break
    for it in items:
        t = it["title"]
        if re.search(r"\bQUERY\b", t) or re.search(r"(?i)rfc ?10008|safe.method.w.body|QUERY (http )?(method|verb)", t):
            u = it["html_url"].replace("https://github.com/", "")
            hits[u] = (it["created_at"][:10], it["state"], "PR" if "pull_request" in it else "IS", t[:110], u in known)

for u, v in sorted(hits.items(), key=lambda kv: kv[1][0]):
    print(("   " if v[4] else "NEW"), v[0], v[1], v[2], u, "|", v[3])
