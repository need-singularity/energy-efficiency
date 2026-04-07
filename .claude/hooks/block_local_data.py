#!/usr/bin/env python3
"""
PreToolUse hook: 데이터 파일(.jsonl, constants, discovery 등)을
n6-architecture 안에 생성/수정하려는 시도를 차단.
→ 모든 데이터는 ~/Dev/nexus/shared/ 에 저장해야 함.
"""
import sys
import json
import os
import re

# nexus/shared 경로 (데이터의 유일한 보관 장소)
NEXUS_SHARED = os.path.expanduser("~/Dev/nexus/shared")

# 차단 대상 패턴
BLOCKED_PATTERNS = [
    r'\.jsonl$',                    # 모든 JSONL 파일
    r'discovered_constants',        # 발견 상수
    r'discovery_log',               # 디스커버리 로그
    r'growth_bus',                  # 성장 버스
    r'verified_constants',          # 검증 상수
    r'n6_constants',                # n6 상수
    r'alien_index_records',         # 외계인 지수
    r'growth_strategies',           # 성장 전략
    r'scan_priority',               # 스캔 우선순위
]

# 예외: 이 경로는 허용 (nexus/shared 자체, 또는 프로젝트 설정용)
ALLOWED_PATTERNS = [
    r'/nexus/shared/',              # nexus 중앙 저장소는 OK
    r'hexa_grammar\.jsonl',         # 문법 참조용은 OK (읽기 전용 복사)
    r'package\.json',               # 패키지 설정
]

def main():
    tool_input = json.loads(sys.stdin.read())
    tool_name = sys.argv[1] if len(sys.argv) > 1 else ""

    if tool_name not in ("Write", "Edit"):
        sys.exit(0)

    file_path = tool_input.get("file_path", "")
    if not file_path:
        sys.exit(0)

    # nexus/shared 안이면 허용
    if NEXUS_SHARED in file_path:
        sys.exit(0)

    # 기타 허용 패턴
    for pattern in ALLOWED_PATTERNS:
        if re.search(pattern, file_path):
            sys.exit(0)

    # 차단 패턴 검사
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, file_path):
            print(
                f"❌ 데이터 파일을 프로젝트 안에 저장하지 마세요!\n"
                f"\n"
                f"  시도한 경로: {file_path}\n"
                f"  차단 이유: 상수/수식/발견 데이터는 nexus 중앙 저장소에만 보관\n"
                f"\n"
                f"  올바른 경로: ~/Dev/nexus/shared/ 아래에 저장하세요\n"
                f"  예시:\n"
                f"    ~/Dev/nexus/shared/discovered_constants.jsonl\n"
                f"    ~/Dev/nexus/shared/discovery_log.jsonl\n"
                f"    ~/Dev/nexus/shared/growth_bus.jsonl\n"
                f"\n"
                f"  규칙: 모든 프로젝트 데이터 → nexus/shared/ (유일한 진실의 원천)",
                file=sys.stderr
            )
            sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()
