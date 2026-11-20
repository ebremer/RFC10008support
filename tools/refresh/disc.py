"""Print the text after each comment time >= SINCE in a saved discussion page.

Discussion pages have no JSON timeline, so this prints the visible text that
follows each timestamp: the comment, then the next author's name and
"Collaborator"/"Member" badge if any. Read it as raw text.

usage: python -I -X utf8 tools/refresh/disc.py SINCE owner/repo/discussions/n ...
"""
import html as H
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import page  # noqa: E402

LEN = int(os.environ.get("PEEK_MAX", "1200"))
if len(sys.argv) < 3:
    sys.exit(__doc__)
since = sys.argv[1]
for it in sys.argv[2:]:
    s = page(it)
    print(f"\n######## {it}")
    seen = set()
    for m in re.finditer(r'datetime="(\d{4}-\d\d-\d\dT[^"]+)"', s):
        if m.group(1) < since or m.group(1) in seen:
            continue
        seen.add(m.group(1))
        seg = s[m.start():m.start() + 15000]
        t = re.sub(r"<(script|style|svg)[^>]*>.*?</\1>", " ", seg, flags=re.S)
        t = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", t)))
        t = re.sub(r"(Uh oh! )?There was an error while loading\. Please reload this page \.|"
                   r"\{\{title\}\}|Something went wrong\.|You must be logged in to vote", " ", t)
        print(" ", m.group(1)[:16], "::", re.sub(r"\s+", " ", t)[:LEN])
