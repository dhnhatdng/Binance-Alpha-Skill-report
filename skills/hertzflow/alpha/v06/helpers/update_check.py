#!/usr/bin/env python3
"""update_check.py — Self-check for newer skill versions on GitHub.

v0.6.5. On pipeline startup, optionally checks GitHub for newer commits
on main. If installed commit SHA differs from latest, prints a single
i18n-localized line to stderr suggesting `npx skills update`.

Design constraints:
  - **Non-blocking**: 3-second curl timeout, silent failure
  - **24h cache**: writes ~/.binance-alpha-data/last_update_check to
    avoid hitting GitHub more than once per day
  - **No GitHub token required** (public API)
  - **i18n-localized**: respects current lang via i18n.t()
  - **Off-switch**: BINANCE_ALPHA_NO_UPDATE_CHECK=1 disables entirely
  - **Privacy**: only 1 HTTP GET to GitHub commits API, no user data
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

# Module constants
DEFAULT_DATA_DIR = Path.home() / ".binance-alpha-data"
DEFAULT_CHECK_CACHE = DEFAULT_DATA_DIR / "last_update_check.json"
DEFAULT_INSTALLED_FILE = DEFAULT_DATA_DIR / "installed_commit"
CHECK_TTL_SECS = 86400   # 24h
HTTP_TIMEOUT_SECS = 3
GITHUB_REPO = "HertzFlow/hertzflow-skills"
GITHUB_COMMITS_URL = f"https://api.github.com/repos/{GITHUB_REPO}/commits/main"


def check_for_update(
    *,
    cache_path: Path = DEFAULT_CHECK_CACHE,
    installed_file: Path = DEFAULT_INSTALLED_FILE,
    ttl_secs: int = CHECK_TTL_SECS,
    quiet: bool = False,
) -> dict | None:
    """Run the self-update check. Returns:
        - None if check skipped (env opt-out, recent cache hit) or failed
        - {"installed": str, "latest": str, "is_newer": bool} otherwise

    Side effect: writes warning to stderr if is_newer is True.
    Idempotent: 24h cache prevents repeated GitHub API hits.
    """
    if os.environ.get("BINANCE_ALPHA_NO_UPDATE_CHECK", "").strip() in ("1", "true", "yes"):
        return None

    # Cache check — skip if we hit GitHub in the last 24h
    cache = _load_cache(cache_path)
    if cache:
        age = int(time.time()) - cache.get("checked_ts", 0)
        if age < ttl_secs:
            # Within TTL — still print warning if last check found newer.
            if cache.get("is_newer") and not quiet:
                _print_warning(cache.get("installed", ""), cache.get("latest", ""))
            return cache

    # Fetch latest from GitHub (3s timeout, silent failure)
    latest_sha = _fetch_latest_sha()
    if not latest_sha:
        return None   # network failure → silently skip

    installed_sha = _read_installed(installed_file)

    is_newer = bool(installed_sha and latest_sha != installed_sha)
    result = {
        "installed": installed_sha or "",
        "latest": latest_sha,
        "is_newer": is_newer,
        "checked_ts": int(time.time()),
    }
    _save_cache(cache_path, result)

    if is_newer and not quiet:
        _print_warning(installed_sha, latest_sha)

    return result


def record_install(commit_sha: str, *, installed_file: Path = DEFAULT_INSTALLED_FILE) -> None:
    """Write installed commit SHA to disk. Called by skill installer hook.

    If the installer cannot reliably get the commit SHA, this can be a no-op;
    the update check will simply not have a baseline to compare against, and
    will silently print nothing.
    """
    installed_file.parent.mkdir(parents=True, exist_ok=True)
    installed_file.write_text(commit_sha.strip(), encoding="utf-8")


def _fetch_latest_sha() -> str | None:
    """Hit GitHub commits API. Returns short SHA or None on failure."""
    try:
        result = subprocess.run(
            ["curl", "-sS", "--max-time", str(HTTP_TIMEOUT_SECS),
             "-H", "User-Agent: binance-alpha-skill",
             GITHUB_COMMITS_URL],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=HTTP_TIMEOUT_SECS + 2, check=False,
        )
    except (subprocess.TimeoutExpired, OSError):
        return None
    if result.returncode != 0:
        return None
    try:
        doc = json.loads(result.stdout)
    except json.JSONDecodeError:
        return None
    sha = (doc.get("sha") or "")[:7]
    return sha if sha else None


def _read_installed(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8").strip()[:7]
    except (OSError, UnicodeDecodeError):
        return None


def _load_cache(path: Path) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _save_cache(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        path.write_text(json.dumps(data), encoding="utf-8")
    except OSError:
        pass


def _print_warning(old: str, new: str) -> None:
    """Print i18n-localized warning to stderr. Lazy import to avoid
    circular dependency if i18n calls back into us."""
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from i18n import t
        title = t("section.update_check.title", old=old or "?", new=new)
        action = t("section.update_check.action")
        print(f"\n{title}", file=sys.stderr)
        print(f"   {action}\n", file=sys.stderr)
    except Exception:
        # Fall back to English if i18n itself fails
        print(f"\n🆕 New version available ({old or '?'} → {new})", file=sys.stderr)
        print(f"   Run `npx skills update hertzflow` to update\n", file=sys.stderr)


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check", help="Run update check (default)")
    p_record = sub.add_parser("record-install", help="Record installed commit SHA")
    p_record.add_argument("sha")
    args = ap.parse_args()

    if args.cmd == "record-install":
        record_install(args.sha)
        print(f"Recorded installed commit: {args.sha[:7]}")
    else:
        result = check_for_update()
        if result:
            print(json.dumps(result, indent=2))
        else:
            print("(no result)")
