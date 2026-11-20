"""One paragraph per item: status, opened (+day), merged/closed (+day, by whom), body excerpt.

The issue "opened" date is the first createdAt on the page, which is not always
the issue's own; when the date matters, take created_at from
api.github.com/repos/{o}/{r}/issues/{n} (one core API call).

usage: python -I -X utf8 tools/refresh/summ.py [-n MAX] owner/repo/kind/n ...
"""
import html as H
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import day, page  # noqa: E402
from peek import jstr  # noqa: E402

args = sys.argv[1:]
mx = 400
if args[:1] == ["-n"]:
    mx, args = int(args[1]), args[2:]
if not args:
    sys.exit(__doc__)
for it in args:
    s = page(it)
    st = re.search(r'data-status="([^"]+)"', s)
    st = st.group(1) if st else "?"
    title = re.search(r"<title>(.*?)</title>", s, re.S)
    title = H.unescape(title.group(1)).split(" · ")[0] if title else ""
    if "/pull/" in it:
        m = re.search(r'data-dd-action-name="pr\.description\.copy_markdown" value="([^"]*)"', s)
        body = H.unescape(m.group(1)) if m else ""
        dts = re.findall(r'datetime="(\d{4}-[^"]+)"', s)
        opened = dts[0] if dts else None
        au = re.search(r'class="[^"]*\bauthor\b[^"]*"[^>]*>([^<]+)<', s)
        au = au.group(1) if au else "?"
        ev = ""
        m = re.search(r'merged commit.*?datetime="([^"]+)"', s, re.S) or re.search(r'"mergedTime":"([^"]+)"', s)
        if m and st == "pullMerged":
            who = (re.search(r'([A-Za-z0-9-]+)\s*</a>\s*merged commit', s)
                   or re.search(r'"mergedBy":"([^"]+)"', s))
            ev = f"merged {day(m.group(1))} ({m.group(1)[:10]})" + (f" by {who.group(1)}" if who else "")
        elif st == "pullClosed":
            m = (re.search(r'closed this\s*<a[^>]*>\s*<relative-time[^>]*datetime="([^"]+)"', s)
                 or re.search(r'closed this.{0,400}?datetime="([^"]+)"', s, re.S))
            ev = f"closed {day(m.group(1)) if m else '?'}"
        mil = re.search(r'added this to the\s*<a[^>]*>([^<]+)</a>\s*milestone', s) or \
            re.search(r'"milestone":\{[^}]*"title":"([^"]+)"', s)
        if mil:
            ev += f" milestone={mil.group(1)}"
    else:
        i = s.find('"__typename":"Issue"')
        b = s.find('"body":"', i if i >= 0 else 0)
        body = jstr(s, b + 7) if b >= 0 else ""
        ca = re.search(r'"createdAt":"([^"]+)"', s)
        opened = ca.group(1) if ca else None
        au = re.search(r'"author":\{[^{}]*?"login":"([^"]+)"', s)
        au = au.group(1) if au else "?"
        ev = ""
        cl = list(re.finditer(r'"__typename":"ClosedEvent"', s))
        if cl:
            ch = s[cl[-1].start():cl[-1].start() + 3000]
            ca2 = re.search(r'"createdAt":"([^"]+)"', ch)
            ac = re.search(r'"actor":\{[^{}]*?"login":"([^"]+)"', ch)
            sr = re.search(r'"stateReason":"([^"]+)"', ch)
            ev = (f"closed {day(ca2.group(1)) if ca2 else '?'} by {ac.group(1) if ac else '?'} "
                  f"{sr.group(1) if sr else ''}")
        ncom = len(re.findall(r'"__typename":"IssueComment"', s))
        ev += f" comments~{ncom}"
    body = re.sub(r"\s+", " ", re.sub(r"<!--.*?-->", "", body, flags=re.S)).strip()
    print(f"\n## {it} [{st}] {title}\n   opened {day(opened)} ({(opened or '')[:10]}) by {au}; {ev}\n   {body[:mx]}")
