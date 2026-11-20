"""Shared paths and helpers for the tracker refresh scripts.

Every script reads README.md from the repository root and keeps its inputs,
outputs and the saved GitHub pages in a work directory: tools/refresh/work/
(git-ignored) unless the REFRESH_WORK environment variable names another one.
"""
import datetime as dt
import json
import os
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
README = os.path.join(ROOT, "README.md")
WORK = os.environ.get("REFRESH_WORK") or os.path.join(HERE, "work")
HTML = os.path.join(WORK, "html")
os.makedirs(HTML, exist_ok=True)

DAY0 = dt.date(2026, 6, 16)  # RFC 10008 publication; must match tools/build_site.py
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")
API_UA = "tracker-refresh"  # for api.github.com and ungh.cc


def work(name):
    """Path of a file in the work directory (absolute paths pass through)."""
    return name if os.path.isabs(name) else os.path.join(WORK, name)


def load(name):
    with open(work(name), encoding="utf-8") as f:
        return json.load(f)


def save(name, obj):
    with open(work(name), "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=1, ensure_ascii=False)


def readme():
    with open(README, encoding="utf-8") as f:
        return f.read()


def day(iso):
    """'2026-11-20…' -> '+157' (days after RFC publication)."""
    try:
        return f"{(dt.date.fromisoformat(iso[:10]) - DAY0).days:+d}"
    except (TypeError, ValueError):
        return "?"


def fetch(url, tries=4, ua=UA, accept="text/html", timeout=40):
    """GET url -> (status, final_url, text). 404/410/451 return ('', status) at once;
    other failures are retried with backoff and end as status 0."""
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept": accept})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.geturl(), r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code in (404, 410, 451):
                return e.code, url, ""
            time.sleep(3 * (i + 1))
        except Exception:
            time.sleep(3 * (i + 1))
    return 0, url, ""


def html_path(item):
    """Saved page for owner/repo/kind/n."""
    return os.path.join(HTML, item.replace("/", "__") + ".html")


def page(item, force=False):
    """Saved GitHub page for owner/repo/(issues|pull|discussions)/n, fetched if missing."""
    fn = html_path(item)
    if os.path.exists(fn) and not force:
        with open(fn, encoding="utf-8") as f:
            return f.read()
    o, r, k, n = item.split("/")
    code, _, s = fetch(f"https://github.com/{o}/{r}/{k}/{n}")
    if s:
        with open(fn, "w", encoding="utf-8") as f:
            f.write(s)
    return s
