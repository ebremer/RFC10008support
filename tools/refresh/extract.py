"""Parse the README tables into the work directory.

Writes rows.json (one entry per table row: section, name, stack repo, linked
GitHub items, cells), urls.json (every linked issue/PR/discussion -> row names)
and repos.json (every repo involved).

usage: python -I -X utf8 tools/refresh/extract.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import readme, save  # noqa: E402

LINK = re.compile(r"\[([^\]]*)\]\((https?://[^)\s]+)\)")
GH_ITEM = re.compile(r"https://github\.com/([^/]+)/([^/]+)/(issues|pull|discussions)/(\d+)")
GH_REPO = re.compile(r"^https://github\.com/([^/]+)/([^/#?]+)/?$")

md = readme()
rows, section, header = [], None, None
for ln, line in enumerate(md.splitlines(), 1):
    if line.startswith("## "):
        section, header = line[3:].strip(), None
        continue
    if not line.startswith("|"):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
    if header is None:
        header = cells
        continue
    if set("".join(cells)) <= set("-:| "):
        continue
    m = LINK.search(cells[0])
    name = re.sub(r"[*\[\]]", "", m.group(1)) if m else re.sub(r"[*]", "", cells[0])
    repo = None
    if m:
        rm = GH_REPO.match(m.group(2))
        if rm:
            repo = f"{rm.group(1)}/{rm.group(2)}"
    items = []
    for c in cells[1:]:
        for gm in GH_ITEM.finditer(c):
            items.append("/".join(gm.groups()))
    rows.append({"line": ln, "section": section, "name": name, "repo": repo,
                 "items": list(dict.fromkeys(items)), "cells": cells, "header": header})

urls = {}
for r in rows:
    for it in r["items"]:
        urls.setdefault(it, []).append(r["name"])
for gm in GH_ITEM.finditer(md):  # items outside tables too (related trackers etc.)
    urls.setdefault("/".join(gm.groups()), [])

repos = sorted({r["repo"] for r in rows if r["repo"]} | {"/".join(u.split("/")[:2]) for u in urls})
save("rows.json", rows)
save("urls.json", urls)
save("repos.json", repos)
print(len(rows), "rows;", len(urls), "items;", len(repos), "repos")
