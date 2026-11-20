# Refresh scripts

Scripts for the weekly refresh of the tracker. They check every linked issue, PR
and discussion, find new releases and new QUERY work, refresh star counts, and
apply the README edits. None of them needs `gh` or a token. GitHub's REST API
allows 60 unauthenticated requests an hour, so everything except search uses
quota-free channels: saved github.com pages, Atom feeds, `branch_commits`,
raw.githubusercontent.com and ungh.cc.

Run them with `python -I -X utf8` (`-I` ignores `PYTHONIOENCODING`, so pass
`-X utf8` for output on Windows). Each script prints its usage when run without
the arguments it needs.

Inputs, outputs and the saved pages (about 150 MB) go to `tools/refresh/work/`,
which is git-ignored. Set `REFRESH_WORK` to use another directory. Reusing the
directory keeps the page cache, but `states.py` refetches every tracked page on
each run anyway.

## Workflow

`SINCE` is the last refresh (from the README header). Use a day earlier for
the searches, so nothing near the boundary is missed.

1. **Parse the README.** `extract.py` writes `rows.json`, `urls.json` and `repos.json`.
2. **Fetch.** These take a few minutes, so run them in the background:
   `states.py` (every item page, about 2 min), `releases.py` (both Atom feeds of
   every repo) and `stars.py`.
3. **State changes.** `compare.py SINCE` lists items whose state no longer
   matches the README, and every item with activity since `SINCE`. Read each
   one with `peek.py -q SINCE item…`. When `peek.py` shows activity but no
   event, `rawpeek.py` shows what it was (usually a mention from another repo).
   Use `disc.py` for discussions and `summ.py -n 1500` for descriptions.
4. **Releases.** `newrel.py SINCE` lists every release and tag since the last
   refresh. Check each against its row's "shipped without", "carried in" and
   "latest" claims, and read every line, including those marked
   `name-in-README`. `relgrep.py SINCE repo…` shows QUERY mentions in release
   notes.
5. **Is a merge released?** `intags.py` lists the tags that contain each merged
   PR, and `firstrel.py intags.json item…` sorts them by version, with dates.
   Use `tagdate.py owner/repo:tag…` for exact dates. When `intags.py` finds no
   tag, or no sha, `rawgrep.py PATTERN repo path tag…` greps the changed file at
   each tag.
6. **Discovery.**
   - Run `search.py SINCE created` and, a minute later, `search.py SINCE updated`,
     then `showsearch.py --cand search_created.json search_updated.json`.
   - `repo_search.py SINCE` sweeps every tracked repo plus `extra_repos.txt`.
   - Read the candidates with `summ.py`. `states.py cand.json cand_states.json`
     followed by `intags.py cand_states.json` gives their merge and tag status.
   - `stars.py owner/repo…` writes `extra_stars.json` for new rows.
   - Add any new repo worth watching to `extra_repos.txt`.
7. **Edit.** Write the edits file (format in `apply_edits.py`) and run
   `apply_edits.py EDITS.py`. Then run `stars_sort.py extra_stars.json`, which
   writes the counts, sorts each ★ table and reports any row whose cell count is
   wrong. `python tools/build_site.py --out <scratch dir>` validates the result.
8. **Commit and publish.** Commit `README.md` alone first, as "Refresh
   adoption status to day +N (YYYY-MM-DD)". The adoption curve is read from the
   README's git history, so the rebuild must come after that commit. Then run
   `python tools/build_site.py`, commit `docs/` as "Rebuild site from README
   (<short sha>)", and push. CI then finds `docs/` already up to date.

## Gotchas

- **Search finds the obvious, not everything.** Title phrases alone missed whole
  projects (Netty, Angular, Puma, Quarkus and about 30 more), which is why
  `repo_search.py` exists. Repos whose titles say "query" all the time
  (ClickHouse, Quarkus, Prometheus, Trino, Loki) fill a group's results; they
  are left out of the sweep, so search them with exact phrases instead.
- **Atom feeds hold about 10 entries.** Busy repos can push a release out of
  the feed between refreshes. Releases that were only tags, or that fell
  between refreshes, have been missed before (hapi v21.4.11, Tornado 6.6.0).
- **`branch_commits` has blind spots.** Some shas get no tags even though the
  change shipped (Netty's 4.1 backport, Apache HttpClient #852, Swoole #6256,
  which shipped in v6.1.11 and v6.2.4). Newer PR pages expose no merge sha at
  all, only `mergedTime` (Kiota, VueUse, Scalar). In both cases, use `rawgrep.py`.
- **Release dates.** The Atom `<updated>` field can be an edit time, so use
  `tagdate.py`. Some projects tag well before the real release. The .NET GA
  date is in `release-notes/<ver>/releases.json` in dotnet/core. PHP's is at
  `php.net/releases/index.php?json&version=8.6`.
- **Issue open dates.** The first `createdAt` on an issue page is not always the
  issue's own. Take `created_at` from `api.github.com/repos/{o}/{r}/issues/{n}`
  (one core API call).
- **Activity times are noisy.** The times on a page include CI runs, bot comments,
  force-pushes and mentions from other repos. A merged PR showing recent
  activity has usually just been mentioned somewhere else.
- **Who said it matters.** The README separates maintainers, collaborators,
  contributors and users. Issue comments carry `authorAssociation`, and
  discussion text shows "Collaborator" or "Member" badges.
