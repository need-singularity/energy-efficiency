#!/usr/bin/env python3
"""
dream_fusion_nightly.py — A11 Dream engine 야간 fusion wrapper

launchd/com.n6.signals-nightly.plist 에서 호출되는 야간 fusion runner.
fusion_auto_append.py --commit 실행 + gen_signals_stats.py sidecar 갱신.

사용:
  /usr/bin/python3 scripts/dream_fusion_nightly.py
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path("/Users/ghost/Dev/n6-architecture/scripts")


def run(script: str, *args: str) -> int:
    p = ROOT / script
    if not p.exists():
        print(f"SKIP {script} — 없음")
        return 0
    try:
        r = subprocess.run(
            [sys.executable, str(p), *args],
            capture_output=True, text=True, timeout=600, check=False,
        )
        if r.returncode != 0:
            print(f"FAIL {script} rc={r.returncode}")
            print(r.stderr[:1000])
            return r.returncode
        print(f"OK {script}")
        if r.stdout:
            print("  " + r.stdout.splitlines()[0][:200] if r.stdout.splitlines() else "")
    except Exception as e:
        print(f"ERR {script}: {e}")
        return 1
    return 0


def main() -> int:
    print("=== dream_fusion_nightly ===")
    rc = 0
    rc |= run("fusion_auto_append.py", "--commit")
    rc |= run("gen_signals_stats.py")
    rc |= run("cross_repo_daemon.py", "--once", "--threshold", "0.70")
    print(f"=== done rc={rc} ===")
    return rc


if __name__ == "__main__":
    sys.exit(main())
