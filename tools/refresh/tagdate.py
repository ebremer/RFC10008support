"""Exact date of a release or tag, from its github.com/{repo}/releases/tag/{tag} page.

Prefer this over the Atom <updated> time, which can be an edit time. Some
projects tag days before the real release (.NET: see releases.json in
dotnet/core; PHP: php.net/releases/index.php?json&version=8.6).
Tag names cannot contain ':', so it separates repo and tag.

usage: python -I -X utf8 tools/refresh/tagdate.py owner/repo:tag [owner/repo:tag ...]
"""
import concurrent.futures as cf
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import day, fetch  # noqa: E402


def tagdate(repo, tag):
    """ISO datetime string, '404', or '?'."""
    code, _, s = fetch(f"https://github.com/{repo}/releases/tag/{urllib.parse.quote(tag, safe='')}", tries=3)
    if code == 404:
        return "404"
    m = re.search(r'<relative-time[^>]*datetime="([^"]+)"', s) or re.search(r'datetime="(\d{4}-[^"]+)"', s)
    return m.group(1) if m else "?"


if __name__ == "__main__":
    pairs = [a.split(":", 1) for a in sys.argv[1:] if ":" in a]
    if not pairs:
        sys.exit(__doc__)
    with cf.ThreadPoolExecutor(6) as ex:
        for (repo, tag), d in zip(pairs, ex.map(lambda p: tagdate(*p), pairs)):
            print(f"{repo:<42} {tag:<26} {d[:16]:<17} {day(d)}")
