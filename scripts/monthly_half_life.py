#!/usr/bin/env python3
"""
monthly_half_life.py — E7 stub (monthly half-life cron)

signal_half_life.py 를 월 1회 호출하는 wrapper. launchd plist 는 com.n6.signals-monthly.plist 로 별도 필요.

상태: docstring stub. 실제 구현은 A6 signal_half_life.py 가 우선.

설계:
  1. signal_half_life.py --threshold-days 14 --commit
  2. signal_half_life.py --threshold-days 28 --archive
"""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

HALF_LIFE = Path("/Users/ghost/Dev/n6-architecture/scripts/signal_half_life.py")

if not HALF_LIFE.exists():
    print("stub: E7 monthly_half_life — signal_half_life.py 선행 필요", file=sys.stderr)
    sys.exit(0)

print("E7 monthly_half_life: signal_half_life.py 호출 예정 (stub)")
# subprocess.run([sys.executable, str(HALF_LIFE), "--threshold-days", "14"])
sys.exit(0)
