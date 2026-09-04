# Site build

The repository root `README.md` is the **source of truth**. Nothing here ever writes to it.

`build_site.py` renders it into `docs/`, which GitHub Pages serves:

```
python tools/build_site.py          # writes docs/
```

| Output | What it is |
|---|---|
| `docs/index.html` | The README's tables, searchable and filterable by status |
| `docs/adoption-curve.html` | Weekly status counts, reconstructed from the git history of `README.md` |
| `docs/data/adoption.json` | The curve's underlying numbers |
| `docs/style.css`, `app.js`, `chart.js` | Copied verbatim from `tools/site/` |

Edit `tools/site/*` — never `docs/*`, which is overwritten on every build.

## How the curve is derived

`weekly_history()` walks `git log -- README.md`, takes the **last commit of each ISO week**, and
counts status glyphs in that revision of the table. Projects appearing in more than one table
(server *and* client rows) are de-duplicated by repository slug. Weeks with no commit are skipped,
and points are plotted at their true day offset, so a gap stays a gap.

This needs full history: CI checks out with `fetch-depth: 0`.

## Pages setup

Settings → Pages → Source: **Deploy from a branch**, branch `main`, folder `/docs`.

`.github/workflows/build-site.yml` rebuilds and commits `docs/` whenever `README.md` or `tools/`
changes, so the site follows the weekly refresh without a manual step.
