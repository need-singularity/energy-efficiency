#!/usr/bin/env python3
"""
PreToolUse hook: Write/Edit로 .md 파일에 ```python 검증코드를 넣을 때
동어반복(하드코딩 상수 == 하드코딩 상수) 패턴을 감지하고 차단한다.

차단 조건 (하나라도 해당 시):
1. n6 상수(sigma, tau, phi 등)를 리터럴로 하드코딩한 뒤 그대로 비교
2. 수학 함수 정의 없이 상수만 나열
3. print/check만 있고 실제 계산 로직 없음
"""
import sys
import json
import re

def extract_python_blocks(text):
    """마크다운에서 ```python ... ``` 블록 추출"""
    pattern = r'```python\s*\n(.*?)```'
    return re.findall(pattern, text, re.DOTALL)

def is_hardcoded_constant(line):
    """sigma = 12 같은 하드코딩 패턴 감지"""
    n6_names = r'(sigma|tau|phi|sopfr|mu|J2|J_2|lam|P2|n)\s*='
    # "sigma = 12" 형태 (함수 정의가 아닌 리터럴 대입)
    pattern = rf'^\s*{n6_names}\s*\d+\s*(#.*)?$'
    return bool(re.match(pattern, line.strip()))

def has_real_computation(code):
    """실제 수학적 계산/도출이 있는지 확인"""
    real_patterns = [
        r'def\s+sigma\s*\(',        # σ(n) 함수 정의
        r'def\s+tau\s*\(',          # τ(n) 함수 정의
        r'def\s+phi\s*\(',          # φ(n) 함수 정의
        r'def\s+euler_totient',
        r'def\s+divisor',
        r'def\s+mobius',
        r'def\s+jordan',
        r'sum\s*\(.*range',         # sum(... for ... in range) 패턴
        r'for\s+\w+\s+in\s+range',  # 반복 계산
        r'sympy',                   # sympy 사용
        r'from\s+fractions',        # fractions 모듈
        r'math\.',                  # math 모듈 사용
        r'numpy',                   # numpy 사용
        r'%\s*\w+\s*==\s*0',        # 나눗셈 검증 (약수 판정)
        r'divisors\s*\(',           # 약수 함수
        r'gcd\s*\(',               # 최대공약수
        r'factorial',              # 팩토리얼
        r'prod\s*\(',              # 곱 연산
        r'lambda\s+\w+\s*:',       # 람다 계산식
    ]
    return any(re.search(p, code) for p in real_patterns)

def count_hardcoded_constants(code):
    """하드코딩된 n6 상수 개수"""
    return sum(1 for line in code.split('\n') if is_hardcoded_constant(line))

def analyze_verification(code):
    """검증코드 품질 분석 → (pass, message)"""
    hardcoded = count_hardcoded_constants(code)
    has_computation = has_real_computation(code)

    # 하드코딩 상수가 3개 이상이고 실제 계산 없음 = 동어반복
    if hardcoded >= 3 and not has_computation:
        return False, (
            f"❌ 동어반복 검증코드 감지 (하드코딩 상수 {hardcoded}개, 실제 수학 계산 0개)\n"
            f"\n"
            f"  문제: sigma=12 로 정의한 뒤 12==sigma 를 '검증'하는 건 동어반복입니다.\n"
            f"\n"
            f"  수정 방법:\n"
            f"  1. n6 상수를 정의에서 직접 계산하세요:\n"
            f"     def sigma(n): return sum(d for d in range(1,n+1) if n%d==0)\n"
            f"     assert sigma(6) == 12\n"
            f"\n"
            f"  2. 또는 독립 라이브러리로 교차검증하세요:\n"
            f"     from sympy import divisor_sigma\n"
            f"     assert divisor_sigma(6) == 12\n"
            f"\n"
            f"  3. 실제 데이터와 대조하세요:\n"
            f"     # 실제 UTC 시간대 수 확인\n"
            f"     assert len(pytz.common_timezones_set) > 400  # 실제값과 n6 예측 비교"
        )

    return True, ""

def main():
    tool_input = json.loads(sys.stdin.read())
    tool_name = sys.argv[1] if len(sys.argv) > 1 else ""

    # Write/Edit 만 체크
    if tool_name not in ("Write", "Edit"):
        sys.exit(0)

    file_path = tool_input.get("file_path", "")

    # .md 파일만 체크
    if not file_path.endswith(".md"):
        sys.exit(0)

    # 내용 추출
    content = tool_input.get("content", "") or tool_input.get("new_string", "")
    if not content:
        sys.exit(0)

    # python 블록 추출
    python_blocks = extract_python_blocks(content)
    if not python_blocks:
        # Edit의 경우 부분 코드일 수 있으므로 전체를 python으로 간주
        if "sigma" in content and "check(" in content and "```python" not in content:
            python_blocks = [content]
        else:
            sys.exit(0)

    # 각 블록 분석
    for block in python_blocks:
        ok, msg = analyze_verification(block)
        if not ok:
            print(msg, file=sys.stderr)
            sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()
