"""Discovery by title phrase through the search API (unauthenticated: 10 requests/min).

Runs each phrase with created:>=SINCE or updated:>=SINCE and saves the hits to
search_<field>.json; show the new ones with showsearch.py. Run "created" and
"updated" a minute apart. Title phrases alone miss whole projects, so also run
repo_search.py.

usage: python -I -X utf8 tools/refresh/search.py SINCE created|updated
       SINCE = date a day before the last refresh, e.g. 2026-11-12
"""
import json
import os
import sys
import time
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import API_UA, fetch, save  # noqa: E402

if len(sys.argv) < 3 or sys.argv[2] not in ("created", "updated"):
    sys.exit(__doc__)
since, field = sys.argv[1], sys.argv[2]
TERMS = ['"RFC 10008"', '"RFC10008"', '"QUERY method"', '"HTTP QUERY"', '"QUERY verb"', '"QUERY HTTP"',
         '"method QUERY"', '"QUERY request"', '"QUERY requests"', '"rfc-10008"']
found = {}
for i, t in enumerate(TERMS):
    q = f"{t} in:title {field}:>={since}"
    url = "https://api.github.com/search/issues?" + urllib.parse.urlencode(
        {"q": q, "sort": "updated", "order": "desc", "per_page": 100})
    code, _, s = fetch(url, tries=2, ua=API_UA, accept="application/vnd.github+json")
    try:
        d = json.loads(s)
    except ValueError:
        print("ERR", t, code, file=sys.stderr)
        time.sleep(8)
        continue
    for it in d.get("items", []):
        u = it["html_url"].replace("https://github.com/", "")
        found[u] = {"title": it["title"], "state": it["state"], "created": it["created_at"][:10],
                    "updated": it["updated_at"][:10], "comments": it["comments"],
                    "pr": "pull_request" in it, "term": t,
                    "repo_url": it["repository_url"].replace("https://api.github.com/repos/", "")}
    print(t, d.get("total_count"), file=sys.stderr)
    if i < len(TERMS) - 1:
        time.sleep(7)
save(f"search_{field}.json", found)
print(len(found), "hits saved to", f"search_{field}.json")
