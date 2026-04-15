#!/usr/bin/env python3
"""
fusion_blacklist.py — A18 stub (fusion blacklist, [MN]끼리 조합 제외)

fusion_auto_append.py 호출 전 전처리. [MN] 등급 signal 들만으로 구성된
triple 을 제거해서 NULL-NULL fusion 낭비 방지.

상태: docstring stub. fusion_auto_append 에 inline 으로 integrate 권장.

설계:
  1. atlas.signals.n6 에서 [MN] 목록 추출
  2. fusion_log.jsonl 에서 a/b/c 모두 [MN] prefix 또는 정확히 일치하는 row skip
"""
from __future__ import annotations
import sys
print("stub: A18 fusion_blacklist — fusion_auto_append.py 에 inline 예정", file=sys.stderr)
sys.exit(0)
