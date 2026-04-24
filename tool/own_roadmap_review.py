#!/usr/bin/env python3
"""own#19 — weekly roadmap review reminder.

Scans known roadmap artifacts and reports any that have had no git commit
activity within the last THRESHOLD_DAYS. Emits a JSON report to
``reports/n6_own19_roadmap_review.json`` and exits non-zero on staleness so
the scheduled workflow can surface the warning (SOFT — wrapped with
``continue-on-error`` in the cron workflow, per own#19 ``on_fail=log``).

Standard library only.
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

THRESHOLD_DAYS = 7


def _last_commit_epoch(root: Path, rel: str) -> int | None:
    """Return epoch seconds of last commit touching ``rel``, or ``None``."""
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "log", "-1", "--format=%ct", "--", rel],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return None
    if result.returncode != 0:
        return None
    raw = result.stdout.strip()
    if not raw:
        return None
    try:
        return int(raw)
    except ValueError:
        return None


def _iter_candidates(root: Path) -> list[Path]:
    """Ordered list of roadmap paths to inspect (directories and files)."""
    ordered = [
        root / "shared" / "roadmaps" / "millennium.json",
        root / "millennium.json",
        root / "ROADMAP.md",
        root / "theory" / "roadmap-v3",
        root / "theory" / "roadmap-v2",
        root / "roadmap",
    ]
    return [p for p in ordered if p.exists()]


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    candidates = _iter_candidates(root)

    now = time.time()
    inspected: list[dict] = []
    stale: list[dict] = []
    missing_history: list[str] = []

    for c in candidates:
        rel = c.relative_to(root).as_posix()
        last = _last_commit_epoch(root, rel)
        if last is None:
            missing_history.append(rel)
            continue
        age_days = (now - last) / 86400.0
        entry = {
            "path": rel,
            "last_commit_epoch": last,
            "age_days": round(age_days, 2),
        }
        inspected.append(entry)
        if age_days > THRESHOLD_DAYS:
            stale.append(entry)

    report = {
        "own_rule": 19,
        "slug": "roadmap-review-weekly",
        "threshold_days": THRESHOLD_DAYS,
        "checked_at_epoch": int(now),
        "candidates_checked": len(inspected),
        "inspected": inspected,
        "stale_roadmaps": stale,
        "missing_history": missing_history,
        "verdict": "stale" if stale else "fresh",
    }

    out_dir = root / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "n6_own19_roadmap_review.json"
    out_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    if not candidates:
        print("[own#19] no roadmap candidates found in repo")
        return 0

    if stale:
        print(f"[own#19] STALE roadmap files ({len(stale)}):")
        for s in stale:
            print(f"  - {s['path']} ({s['age_days']} days since last commit)")
        print(f"[own#19] report: {out_path.relative_to(root)}")
        return 1

    print(
        f"[own#19] all {len(inspected)} roadmap target(s) fresh "
        f"(< {THRESHOLD_DAYS} days)"
    )
    print(f"[own#19] report: {out_path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
