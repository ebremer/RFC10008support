#!/usr/bin/env python3
"""Build the GitHub Pages site from README.md.

README.md is the source of truth. This script never writes to it; it renders it
into docs/ as a filterable site, and reconstructs the weekly adoption curve from
the git history of README.md itself.

Usage:  python tools/build_site.py [--out docs]
"""

import argparse
import collections
import datetime
import html
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "tools", "site")
README = os.path.join(ROOT, "README.md")
DAY0 = datetime.date(2026, 6, 16)

REPO_URL = "https://github.com/ebremer/RFC10008support"
RAW_README = REPO_URL + "/blob/main/README.md"

# status glyph -> (slug, human label)
STATUS = collections.OrderedDict([
    ("✅", ("yes", "Supporting")),
    ("⚠", ("wip", "Working on it")),
    ("❌", ("no", "Declined")),
    ("❓", ("none", "No signal")),
])


# --------------------------------------------------------------------------
# inline markdown
# --------------------------------------------------------------------------

def inline(text):
    """Render inline markdown. Input is raw markdown; output is escaped HTML."""
    codes = []

    def stash(m):
        codes.append(m.group(1))
        return "\x00%d\x00" % (len(codes) - 1)

    text = re.sub(r"`([^`]+)`", stash, text)
    text = html.escape(text, quote=False)

    def link(m):
        label, href = m.group(1), m.group(2)
        ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
        return '<a href="%s"%s>%s</a>' % (html.escape(href, quote=True), ext, label)

    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![*\w])\*([^*\n]+)\*(?![*\w])", r"<em>\1</em>", text)

    def unstash(m):
        return "<code>%s</code>" % html.escape(codes[int(m.group(1))], quote=False)

    return re.sub(r"\x00(\d+)\x00", unstash, text)


def strip_md(text):
    """Plain text of an inline markdown fragment (for titles and aria labels)."""
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\*+", "", text)
    return text.strip()


# --------------------------------------------------------------------------
# block parsing
# --------------------------------------------------------------------------

def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def is_divider(cells):
    return all(set(c) <= set("-: ") and c for c in cells)


def classify(cells):
    """Return (status_slug, status_label) for a table row, or (None, None)."""
    for cell in cells:
        for glyph, (slug, label) in STATUS.items():
            if glyph in cell:
                return slug, label
    return None, None


def col_class(header):
    h = header.lower()
    if h.startswith("stack") or h.startswith("project"):
        return "col-stack"
    if "star" in h:
        return "col-num"
    if h.startswith("status") or h.startswith("kind"):
        return "col-status"
    if "days" in h:
        return "col-days"
    if h.startswith("lang"):
        return "col-lang"
    if "pr /" in h or h.startswith("source") or h.startswith("tracking"):
        return "col-links"
    if h.startswith("note"):
        return "col-notes"
    return ""


def render_table(header, body):
    cols = [col_class(h) for h in header]
    out = ['<div class="table-scroll"><table>', "<thead><tr>"]
    for h, c in zip(header, cols):
        cls = ' class="%s"' % c if c else ""
        out.append("<th%s scope=\"col\">%s</th>" % (cls, inline(h)))
    out.append("</tr></thead><tbody>")

    counted = []
    for cells in body:
        slug, label = classify(cells)
        attr = ' data-status="%s"' % slug if slug else ""
        out.append("<tr%s>" % attr)
        for idx, cell in enumerate(cells):
            c = cols[idx] if idx < len(cols) else ""
            cls = ' class="%s"' % c if c else ""
            if c == "col-stack":
                out.append('<th scope="row" class="col-stack">%s</th>' % inline(cell))
            elif c == "col-status" and slug:
                text = cell
                for glyph in STATUS:
                    text = text.replace(glyph, "")
                text = strip_md(text).replace("️", "").strip()
                out.append(
                    '<td class="col-status"><span class="chip st-%s">'
                    '<span class="dot"></span>%s</span></td>'
                    % (slug, html.escape(text or label, quote=False))
                )
            else:
                out.append("<td%s>%s</td>" % (cls, inline(cell)))
        out.append("</tr>")
        counted.append(cells)

    out.append("</tbody></table></div>")
    return "".join(out), counted


SKIP_INTRO = re.compile(r"Last refreshed|ebremer\.github\.io")


def parse(md):
    """README markdown -> (list of section dicts, intro html).

    Intro blocks are the prose above the first `##`. The refresh line becomes the
    eyebrow and the site link would point at this page, so both are dropped.
    """
    lines = md.split("\n")
    sections = []
    intro = []
    cur = None
    i = 0

    def target():
        return cur["html"] if cur else intro

    while i < len(lines):
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        if line.startswith("# "):
            i += 1
            continue                                     # h1 is the masthead

        if line.startswith("## "):
            cur = {"title": line[3:].strip(), "html": [], "rows": 0,
                   "id": re.sub(r"[^a-z0-9]+", "-", line[3:].strip().lower()).strip("-")}
            sections.append(cur)
            i += 1
            continue

        if line.strip() == "---":
            i += 1
            continue

        if line.startswith("|"):
            block = []
            while i < len(lines) and lines[i].startswith("|"):
                block.append(split_row(lines[i]))
                i += 1
            header = block[0]
            body = [r for r in block[1:] if not is_divider(r)]
            markup, counted = render_table(header, body)
            target().append(markup)
            if cur:
                cur["rows"] += len(counted)
            continue

        if line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                item = lines[i][2:]
                i += 1
                while i < len(lines) and lines[i].strip() and not lines[i].startswith(("- ", "|", "#")):
                    item += " " + lines[i].strip()
                    i += 1
                items.append(item)
            target().append("<ul>%s</ul>" % "".join("<li>%s</li>" % inline(x) for x in items))
            continue

        para = [line.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith(("|", "#", "- ")) \
                and lines[i].strip() != "---":
            para.append(lines[i].strip())
            i += 1
        text = " ".join(para)
        if cur is None and SKIP_INTRO.search(text):
            continue
        target().append("<p>%s</p>" % inline(text))

    return sections, "".join(intro)


# --------------------------------------------------------------------------
# counts + weekly history
# --------------------------------------------------------------------------

def count_projects(md):
    """De-duplicated project counts by status, keyed on the repo slug."""
    rank = {"yes": 0, "wip": 1, "no": 2, "none": 3}
    best = {}
    for line in md.split("\n"):
        if not line.startswith("|"):
            continue
        cells = split_row(line)
        if len(cells) < 3 or is_divider(cells):
            continue
        slug, _ = classify(cells)
        if not slug:
            continue
        m = re.search(r"github\.com/([\w.\-]+)/([\w.\-]+)", cells[0])
        key = ("%s/%s" % m.groups()).lower() if m else strip_md(cells[0]).lower()
        if key not in best or rank[slug] < rank[best[key]]:
            best[key] = slug
    tally = collections.Counter(best.values())
    return {
        "total": len(best),
        "yes": tally.get("yes", 0),
        "wip": tally.get("wip", 0),
        "no": tally.get("no", 0),
        "none": tally.get("none", 0),
    }


def count_rows(md):
    """Status counts per table row (a project counts once per role it appears in)."""
    tally = collections.Counter()
    for line in md.split("\n"):
        if not line.startswith("|"):
            continue
        cells = split_row(line)
        if len(cells) < 3 or is_divider(cells):
            continue
        slug, _ = classify(cells)
        if slug:
            tally[slug] += 1
    tally["total"] = sum(tally.values())
    return tally


def git(*args):
    return subprocess.run(["git"] + list(args), cwd=ROOT,
                          capture_output=True, check=True).stdout.decode("utf-8", "replace")


def weekly_history():
    """One snapshot per ISO week: the last commit that touched README.md."""
    try:
        log = git("log", "--format=%H|%ad|%G-W%V", "--date=format:%Y-%m-%d|%G-W%V", "--", "README.md")
    except Exception as exc:                                   # no git, or shallow clone
        print("  ! git history unavailable (%s); skipping the curve" % exc, file=sys.stderr)
        return []

    seen = collections.OrderedDict()
    for line in log.strip().split("\n"):
        if not line:
            continue
        parts = line.split("|")
        sha, date, week = parts[0], parts[1], parts[2]
        if week not in seen:                                   # log is newest-first
            seen[week] = (sha, date)

    points = []
    for week, (sha, date) in seen.items():
        try:
            snap = git("show", "%s:README.md" % sha)
        except Exception:
            continue
        c = count_projects(snap)
        d = datetime.date.fromisoformat(date)
        points.append({
            "sha": sha[:7], "date": date, "week": week, "day": (d - DAY0).days,
            "total": c["total"], "supporting": c["yes"], "working": c["wip"],
            "dont": c["no"] + c["none"], "declined": c["no"], "none": c["none"],
        })
    points.sort(key=lambda p: p["day"])
    return points


# --------------------------------------------------------------------------
# page templates
# --------------------------------------------------------------------------

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 16 16%22><text y=%2213%22 font-size=%2213%22>{emoji}</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="style.css">
{extra_head}</head>
<body>
<header class="topbar"><div class="topbar-inner">
  <a class="brand" href="index.html">RFC&nbsp;10008 <span>/ adoption</span></a>
  <nav class="topnav">
    <a href="index.html"{nav_index}>Tracker</a>
    <a href="adoption-curve.html"{nav_curve}>Adoption curve</a>
    <a href="{repo}" target="_blank" rel="noopener">Repo</a>
  </nav>
</div></header>
"""

FOOT = """<script src="{script}"></script>
</body>
</html>
"""

SEARCH_SVG = ('<svg width="14" height="14" viewBox="0 0 16 16" fill="none" '
              'stroke="currentColor" stroke-width="1.6" aria-hidden="true">'
              '<circle cx="7" cy="7" r="4.5"/><path d="M10.5 10.5 14 14"/></svg>')


def build_index(intro, sections, counts, rows, latest):
    head = HEAD.format(
        title="RFC 10008 Adoption Tracker",
        desc=("Which HTTP stacks support the QUERY method (RFC 10008) — %d projects tracked "
              "across servers, clients, edge and tooling." % counts["total"]),
        emoji="%F0%9F%94%8D",
        extra_head="",
        nav_index=' aria-current="page"',
        nav_curve="",
        repo=REPO_URL,
    )

    refreshed = latest or "—"
    tiles = [
        ("all", "is-total", rows["total"], "Tracked entries",
         "%d projects · some in two roles" % counts["total"]),
        ("yes", "is-yes", rows["yes"], "Supporting", "shipped, released or merged"),
        ("wip", "is-wip", rows["wip"], "Working on it", "PR, issue or discussion open"),
        ("no none", "is-no", rows["no"] + rows["none"], "Not yet",
         "%d declined · %d no signal" % (rows["no"], rows["none"])),
    ]
    tile_html = []
    for slug, cls, n, label, sub in tiles:
        tile_html.append(
            '<button class="tile {cls}" type="button" data-status="{slug}" aria-pressed="false">'
            '<span class="n">{n}</span>'
            '<span class="k"><span class="dot"></span>{label}</span>'
            '<span class="sub">{sub}</span></button>'.format(
                cls=cls, slug=slug, n=n, label=label, sub=sub)
        )

    body = [head, '<main class="wrap">']
    body.append("""
<div class="masthead">
  <div class="eyebrow">
    <span>The HTTP QUERY Method</span><span>Published 2026-06-16</span><span>Refreshed {refreshed}</span>
  </div>
  <h1>Who supports HTTP QUERY?</h1>
  <p class="standfirst">A census of <strong>{total} projects</strong> — servers, clients, proxies,
  caches and tooling — tracked against <a href="https://datatracker.ietf.org/doc/rfc10008/"
  target="_blank" rel="noopener">RFC&nbsp;10008</a> since publication. Search for your stack, or
  filter by status.</p>
  {intro}
</div>
<div class="summary">{tiles}</div>
<div class="callout">
  <p>Six weekly snapshots, reconstructed from this repository's own history: the total has tripled
  while the &ldquo;not yet&rdquo; count has barely moved.</p>
  <a class="go" href="adoption-curve.html">See the adoption curve &rarr;</a>
</div>
<div class="controls">
  <label class="search">{svg}
    <input id="q" type="search" placeholder="Search stacks, languages, notes…  (press /)"
           autocomplete="off" aria-label="Search the tracker">
    <button id="q-clear" type="button" hidden aria-label="Clear search">&times;</button>
  </label>
  <button class="reset" id="reset" type="button" hidden>Clear filters</button>
  <span class="result-count" id="result-count"></span>
</div>
<div id="empty" class="empty">No rows match. Try a different search, or clear the filters.</div>
<div class="content">
""".format(refreshed=refreshed, total=counts["total"], tiles="".join(tile_html),
           svg=SEARCH_SVG, intro=intro))

    for s in sections:
        count = ('<span class="count">%d rows</span>' % s["rows"]) if s["rows"] else ""
        body.append('<section class="section" id="%s"><h2>%s%s</h2>%s</section>'
                    % (s["id"], inline(s["title"]), count, "".join(s["html"])))

    body.append("""</div>
<footer>
  <span><strong>README.md is the source of truth.</strong> This page is generated from it by
  <code>tools/build_site.py</code>; every table, status and note here is the README's own.</span>
  <span>Read the <a href="{raw}" target="_blank" rel="noopener">raw README</a> ·
  file a correction on the <a href="{repo}/issues" target="_blank" rel="noopener">issue tracker</a>.</span>
</footer>
</main>
""".format(raw=RAW_README, repo=REPO_URL))
    body.append(FOOT.format(script="app.js"))
    return "".join(body)


CHART_CSS = """<style>
  .chart-card { background: var(--surface); border: 1px solid var(--hair); border-radius: 10px;
                padding: 22px 22px 14px; display: flex; flex-direction: column; gap: 16px;
                --s-total: #2a78d6; --s-working: #eb6834; --s-supporting: #1baf7a; --s-dont: #eda100; }
  @media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) .chart-card {
    --s-total: #3987e5; --s-working: #d95926; --s-supporting: #199e70; --s-dont: #c98500; } }
  :root[data-theme="dark"] .chart-card {
    --s-total: #3987e5; --s-working: #d95926; --s-supporting: #199e70; --s-dont: #c98500; }
  .legend { display: flex; flex-wrap: wrap; gap: 8px 22px; align-items: center; }
  .legend-item { display: inline-flex; align-items: center; gap: 8px; font-size: 13.5px; color: var(--ink-2); }
  .legend-key { width: 18px; height: 2px; border-radius: 1px; flex: none; }
  .plot-shell { position: relative; overflow-x: auto; }
  svg.plot { display: block; width: 100%; height: auto; min-width: 620px; }
  .grid-line { stroke: var(--grid); stroke-width: 1; }
  .axis-line { stroke: var(--grid); stroke-width: 1; }
  .tick { font-family: var(--mono); font-size: 11.5px; fill: var(--muted); }
  .tick-date { font-family: var(--sans); font-size: 10.5px; fill: var(--muted); }
  .axis-title { font-size: 11px; font-weight: 500; letter-spacing: .08em; text-transform: uppercase; fill: var(--muted); }
  .series-line { fill: none; stroke-width: 2; stroke-linejoin: round; stroke-linecap: round; }
  .marker { stroke: var(--surface); stroke-width: 2; }
  .end-label { font-size: 12.5px; font-weight: 600; fill: var(--ink); }
  .end-label-sub { font-family: var(--mono); font-size: 11px; fill: var(--ink-2); }
  .crosshair { stroke: var(--muted); stroke-width: 1; opacity: 0; }
  .hit { fill: transparent; cursor: crosshair; }
  .tip { position: absolute; pointer-events: none; opacity: 0; transition: opacity .12s ease;
         background: var(--raised); border: 1px solid var(--hair); box-shadow: 0 6px 20px rgba(0,0,0,.13);
         border-radius: 8px; padding: 10px 12px; min-width: 176px; z-index: 4; }
  .tip.on { opacity: 1; }
  .tip-head { font-family: var(--mono); font-size: 11.5px; letter-spacing: .06em; color: var(--muted);
              text-transform: uppercase; margin-bottom: 8px; }
  .tip-row { display: grid; grid-template-columns: 16px 1fr auto; align-items: center; gap: 9px; padding: 2px 0; }
  .tip-key { height: 2px; border-radius: 1px; }
  .tip-name { font-size: 12.5px; color: var(--ink-2); }
  .tip-val { font-family: var(--mono); font-size: 13.5px; font-weight: 600; color: var(--ink);
             font-variant-numeric: tabular-nums; }
  .tip-foot { margin-top: 8px; padding-top: 7px; border-top: 1px solid var(--hair); font-size: 11.5px; color: var(--muted); }
  .chart-table table { min-width: 620px; }
  .chart-table thead th { top: var(--bar-h); }
  .chart-table td { font-family: var(--mono); font-size: 13.5px; color: var(--ink); text-align: right; }
  .chart-table td:first-child, .chart-table th:first-child { text-align: left; }
  .chart-table th { text-align: right; }
  .chart-table td.day { color: var(--ink-2); }
  .chart-table tbody tr:last-child td { font-weight: 600; }
  .th-key { display: inline-block; width: 14px; height: 2px; border-radius: 1px;
            vertical-align: middle; margin-right: 6px; }
  .notes { display: grid; grid-template-columns: repeat(auto-fit, minmax(272px, 1fr)); gap: 22px; }
  .note h3 { margin: 0 0 5px; font-size: 13.5px; font-weight: 600; color: var(--ink); }
  .note p { margin: 0; font-size: 13.5px; color: var(--ink-2); max-width: 58ch; }
</style>
"""


def build_chart(points, counts):
    first, last = points[0], points[-1]
    head = HEAD.format(
        title="RFC 10008 Adoption Curve",
        desc="Weekly counts of projects supporting, working on, or not tracking RFC 10008.",
        emoji="%F0%9F%93%88",
        extra_head=CHART_CSS,
        nav_index="",
        nav_curve=' aria-current="page"',
        repo=REPO_URL,
    )

    aria = ("Line chart of tracked projects by status from day +%d to day +%d after RFC 10008 "
            "publication. Total rises from %d to %d; supporting from %d to %d; working on it from "
            "%d to %d; not-yet stays between %d and %d."
            % (first["day"], last["day"], first["total"], last["total"],
               first["supporting"], last["supporting"], first["working"], last["working"],
               min(p["dont"] for p in points), max(p["dont"] for p in points)))

    declines = last["declined"]
    silent = last["none"]

    return "".join([
        head,
        '<main class="wrap">',
        """
<div class="masthead">
  <div class="eyebrow"><span>Day 0 = 2026-06-16</span><span>{n} weekly snapshots</span>
  <span>+{d0} &rarr; +{d1}</span></div>
  <h1>RFC 10008 Adoption Curve</h1>
  <p class="standfirst">Every project in the tracker, counted by status at the end of each week.
  The x-axis is the tracker's own unit: days after RFC publication.</p>
</div>
<section class="chart-card">
  <div class="legend" id="legend"></div>
  <div class="plot-shell" id="shell">
    <svg class="plot" id="plot" viewBox="0 0 960 452" role="img" aria-label="{aria}"></svg>
    <div class="tip" id="tip" role="status" aria-live="polite"></div>
  </div>
</section>
<section class="section chart-table">
  <h2>Table view</h2>
  <div class="table-scroll"><table>
    <thead><tr>
      <th scope="col">Snapshot</th><th scope="col">Day</th>
      <th scope="col"><span class="th-key" style="background:#2a78d6"></span>Total tracked</th>
      <th scope="col"><span class="th-key" style="background:#eb6834"></span>Working on it</th>
      <th scope="col"><span class="th-key" style="background:#1baf7a"></span>Supporting</th>
      <th scope="col"><span class="th-key" style="background:#eda100"></span>Don&rsquo;t</th>
      <th scope="col">&mdash; declined</th><th scope="col">&mdash; no signal</th>
    </tr></thead>
    <tbody id="chart-tbody"></tbody>
  </table></div>
</section>
<section class="notes">
  <div class="note"><h3>What each line counts</h3>
  <p>One row per project, de-duplicated where a project appears in more than one table (Go, Spring and
  aiohttp each carry a server and a client row). <strong>Supporting</strong> is &#9989;;
  <strong>working on it</strong> is &#9888;&#65039;; <strong>don&rsquo;t</strong> is &#10060; declined
  plus &#10067; no tracking found.</p></div>
  <div class="note"><h3>The flat line is the finding</h3>
  <p>Total tracked triples, but &ldquo;don&rsquo;t&rdquo; never moves. Almost every project discovered
  since has arrived already supporting or already in progress &mdash; and that line is mostly
  <em>silence</em>, not refusal: only {declines} of the {dont} are actual declines. The other {silent}
  are stacks where no QUERY issue exists at all.</p></div>
  <div class="note"><h3>Coverage grows too</h3>
  <p>Each refresh runs discovery searches, so the total rises from both real adoption and wider
  tracking. Read the ratio between the lines rather than the absolute total.</p></div>
</section>
<footer>
  <span>Reconstructed at build time from the git history of <code>README.md</code> &mdash; the last
  commit of each ISO week, {first_sha} through {last_sha}. Points sit at their true day offset, so
  a skipped week leaves a gap rather than a false straight line.</span>
</footer>
""".format(n=len(points), d0=first["day"], d1=last["day"], aria=html.escape(aria, quote=True),
           declines=declines, dont=last["dont"], silent=silent,
           first_sha=first["sha"], last_sha=last["sha"]),
        "</main>\n",
        '<script>window.ADOPTION = %s;</script>\n' % json.dumps(points, separators=(",", ":")),
        FOOT.format(script="chart.js"),
    ])


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(ROOT, "docs"))
    args = ap.parse_args()
    out = os.path.abspath(args.out)

    md = open(README, encoding="utf-8").read()
    sections, intro = parse(md)
    counts = count_projects(md)
    rows = count_rows(md)

    m = re.search(r"Last refreshed \*\*([\d-]+)\*\* \(day \*\*([+\-\d]+)\*\*\)", md)
    latest = "%s (day %s)" % (m.group(1), m.group(2)) if m else None

    os.makedirs(os.path.join(out, "data"), exist_ok=True)
    for name in ("style.css", "app.js", "chart.js"):
        shutil.copyfile(os.path.join(SITE, name), os.path.join(out, name))
    open(os.path.join(out, ".nojekyll"), "w").close()

    with open(os.path.join(out, "index.html"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(build_index(intro, sections, counts, rows, latest))
    print("  index.html    %d sections, %d rows, %d projects"
          % (len(sections), sum(s["rows"] for s in sections), counts["total"]))

    points = weekly_history()
    if points:
        with open(os.path.join(out, "adoption-curve.html"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(build_chart(points, counts))
        with open(os.path.join(out, "data", "adoption.json"), "w", encoding="utf-8", newline="\n") as fh:
            json.dump(points, fh, indent=1)
        print("  adoption-curve.html  %d weekly snapshots (+%d → +%d)"
              % (len(points), points[0]["day"], points[-1]["day"]))

    print("  -> %s" % out)


if __name__ == "__main__":
    main()
