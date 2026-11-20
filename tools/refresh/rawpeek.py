"""Show the page text just before each datetime >= SINCE in a saved page.

The fallback when peek.py shows activity but no readable event: it reveals
mentions from other repos ("X mentioned this pull request"), force-pushes,
release bots and the like.

usage: python -I -X utf8 tools/refresh/rawpeek.py SINCE owner/repo/kind/n ...
"""
import html as H
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import page  # noqa: E402

if len(sys.argv) < 3:
    sys.exit(__doc__)
since = sys.argv[1]
for it in sys.argv[2:]:
    s = page(it)
    print(f"\n######## {it}")
    last = None
    for m in re.finditer(r'datetime="(\d{4}-\d\d-\d\dT[^"]+)"', s):
        if m.group(1) < since or (last and m.start() - last < 1500):
            continue
        last = m.start()
        chunk = s[max(0, m.start() - 2500):m.start() + 300]
        t = re.sub(r"<(script|style|svg)[^>]*>.*?</\1>", " ", chunk, flags=re.S)
        t = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", t))).strip()
        print(" ", m.group(1)[:16], "…", t[-330:])
