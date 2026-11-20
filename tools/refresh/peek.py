"""Print an item's timeline (comments and events) since SINCE, from the saved page.

Pages come from work/html/ (fetched if missing; prefix an item with refetch:
to force a fresh copy). Issue pages carry JSON nodes (IssueComment with author
and authorAssociation, ClosedEvent with stateReason, ...); PR pages are parsed
from the HTML timeline. -q drops bot comments and CI / push / label noise.
PEEK_MAX (environment) caps each line, default 700 characters.

usage: python -I -X utf8 tools/refresh/peek.py [-q] SINCE owner/repo/(issues|pull)/n ...
"""
import html as H
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import page  # noqa: E402

MAXLEN = int(os.environ.get("PEEK_MAX", "700"))
NOISE = re.compile(
    r"(?i)github-actions|codecov|vercel\[|netlify|bedevere|build-analysis|dependabot|copilot \[|\[bot\]|"
    r"azure-pipelines|codspeed|Persistent review|Gradle check|"
    r"EVENT [^ ]* \[\]: .*(force-pushed|pushed .* commit|added .* commits|All checks|deployment|"
    r"requested a review|self-assigned|added the|removed the|label)")


def jstr(s, i):
    """Decode the JSON string literal that starts at s[i] == '"'."""
    j = i + 1
    while True:
        j = s.index('"', j)
        k, bs = j - 1, 0
        while s[k] == "\\":
            bs += 1
            k -= 1
        if bs % 2 == 0:
            break
        j += 1
    return json.loads(s[i:j + 1])


def clean(t):
    t = re.sub(r"\s+", " ", t).strip()
    return t[:MAXLEN] + ("…" if len(t) > MAXLEN else "")


ISSUE_TYPES = ("IssueComment|ClosedEvent|ReopenedEvent|CrossReferencedEvent|LabeledEvent|UnlabeledEvent|"
               "AssignedEvent|UnassignedEvent|ConnectedEvent|ReferencedEvent|RenamedTitleEvent|MilestonedEvent|"
               "IssueTypeAddedEvent|ParentIssueAddedEvent|SubIssueAddedEvent|MarkedAsDuplicateEvent|"
               "ClosedByPullRequestsReferencesEvent")


def issue_events(s):
    ev = []
    for m in re.finditer(r'"__typename":"(%s)"' % ISSUE_TYPES, s):
        typ = m.group(1)
        chunk = s[m.start():m.start() + 6000]
        ca = re.search(r'"createdAt":"([^"]+)"', chunk)
        if not ca:
            continue
        if typ == "IssueComment":
            aus = re.findall(r'"author":\{[^{}]*?"login":"([^"]+)"', chunk)
            assoc = re.search(r'"authorAssociation":"([^"]+)"', chunk)
            b = chunk.find('"body":"')
            body = jstr(chunk, b + 7) if b >= 0 else ""
            who = aus[1] if len(aus) > 1 else (aus[0] if aus else "?")
            ev.append((ca.group(1), f"COMMENT {who} [{assoc.group(1) if assoc else ''}]: {clean(body)}"))
        else:
            actor = re.search(r'"actor":\{[^{}]*?"login":"([^"]+)"', chunk)
            extra = ""
            for key in ("stateReason", "name", "title", "currentTitle"):
                x = re.search(r'"%s":"([^"]+)"' % key, chunk[:800])
                if x:
                    extra += f" {key}={x.group(1)}"
            src = re.search(r'"source":\{.*?"url":"([^"]+)"', chunk[:3000])
            if src and typ in ("CrossReferencedEvent", "ConnectedEvent"):
                extra += " src=" + src.group(1)
            ev.append((ca.group(1), f"{typ} by {actor.group(1) if actor else '?'}{extra}"))
    return ev


def pr_events(s):
    ev = []
    parts = re.split(r'(?=<div[^>]*class="[^"]*(?:js-timeline-item|TimelineItem js-comment-container|'
                     r'timeline-comment-group)[^"]*")', s)
    for p in parts:
        dt = re.search(r'datetime="(\d{4}-[^"]+)"', p)
        if not dt:
            continue
        au = re.search(r'class="[^"]*\bauthor\b[^"]*"[^>]*>([^<]+)<', p)
        body = re.search(r'<td class="d-block comment-body[^"]*"[^>]*>(.*?)</td>', p, re.S)
        cc = re.search(r'data-dd-action-name="comment\.copy_markdown" value="([^"]*)"', p)
        if cc:
            txt, kind = H.unescape(cc.group(1)), "COMMENT"
        elif body:
            txt, kind = H.unescape(re.sub(r"<[^>]+>", " ", body.group(1))), "COMMENT"
        else:
            txt = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", p[:4000])))
            kind = "EVENT"
            if re.search(r"Successfully merging|All checks|This branch has", txt):
                txt = txt[:200]
        lab = re.search(r'<span[^>]*class="[^"]*tooltipped[^"]*"[^>]*aria-label="([^"]+)"[^>]*>\s*'
                        r'(Member|Owner|Collaborator|Contributor|Author)', p)
        ev.append((dt.group(1), f"{kind} {au.group(1).strip() if au else '?'} "
                                f"[{lab.group(2) if lab else ''}]: {clean(txt)}"))
    return ev


def main(argv):
    quiet = "-q" in argv
    argv = [a for a in argv if a != "-q"]
    if len(argv) < 2:
        sys.exit(__doc__)
    since = argv[0]
    for it in argv[1:]:
        force = it.startswith("refetch:")
        it = it.replace("refetch:", "")
        s = page(it, force)
        st = re.search(r'data-status="([^"]+)"', s)
        title = re.search(r"<title>(.*?)</title>", s, re.S)
        print(f"\n######## {it}  [{st.group(1) if st else '?'}]  {H.unescape(title.group(1)) if title else ''}")
        ev = issue_events(s) if "/issues/" in it else pr_events(s)
        if "/pull/" in it and not ev:
            ev = issue_events(s)
        seen = set()
        for t, e in sorted(ev):
            if t < since or (t, e[:80]) in seen or (quiet and NOISE.search(e)):
                continue
            seen.add((t, e[:80]))
            print(" ", t[:16], e)


if __name__ == "__main__":
    main(sys.argv[1:])
