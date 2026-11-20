"""For merged PRs: the earliest and latest containing tag, version-sorted, with dates.

TAGRE (environment) keeps only tags matching that regex, e.g. TAGRE='^v4\\.' to
ignore another release line or sub-package tags in a monorepo.

usage: python -I -X utf8 tools/refresh/firstrel.py intags.json [owner/repo/pull/n ...]
"""
import concurrent.futures as cf
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import day, load  # noqa: E402
from tagdate import tagdate  # noqa: E402

if len(sys.argv) < 2:
    sys.exit(__doc__)
tags = load(sys.argv[1])
items = sys.argv[2:] or list(tags)
FILTER = os.environ.get("TAGRE")


def vkey(t):
    nums = [int(x) for x in re.findall(r"\d+", t)]
    pre = 0 if re.search(r"(?i)alpha|beta|rc|preview|-m\d|canary|next|dev|snapshot", t) else 1
    return (nums[:4] + [0] * (4 - len(nums[:4])), pre, nums[4:])


def one(it):
    rec = tags.get(it, {})
    tl = rec.get("tags", [])
    if FILTER:
        tl = [t for t in tl if re.search(FILTER, t)]
    if not tl:
        return it, rec.get("branches"), None, None
    s = sorted(tl, key=vkey)
    repo = "/".join(it.split("/")[:2])
    first, last = s[0], s[-1]
    fd = tagdate(repo, first)
    ld = tagdate(repo, last) if last != first else fd
    return it, rec.get("branches"), (first, fd), (last, ld)


with cf.ThreadPoolExecutor(6) as ex:
    for it, br, f, last in ex.map(one, items):
        if not f:
            print(f"{it:<58} branches={br} NO TAG")
            continue
        n = len(tags[it]["tags"])
        more = " +more" if tags[it].get("more") else ""
        print(f"{it:<58} first={f[0]} ({f[1][:10]} {day(f[1])})  "
              f"latest={last[0]} ({last[1][:10]} {day(last[1])})  n={n}{more}")
