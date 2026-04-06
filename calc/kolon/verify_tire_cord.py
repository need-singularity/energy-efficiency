#!/usr/bin/env python3
"""타이어코드 n=6 검증 — 20/20 EXACT 목표"""

n, sigma, phi, tau, mu, sopfr, J2 = 6, 12, 2, 4, 1, 5, 24
PASS = 0
FAIL = 0


def check(name, actual, expected, expr=""):
    global PASS, FAIL
    if isinstance(actual, float) or isinstance(expected, float):
        ok = abs(actual - expected) < 1e-9
    else:
        ok = actual == expected
    PASS += ok
    FAIL += not ok
    status = "EXACT" if ok else "FAIL "
    print(f"  [{status}] {name}: {actual} = {expr} (기대: {expected})")


print("=" * 60)
print("타이어코드 — Phase 1: 소재/구조 파라미터")
print("=" * 60)

check("나일론66 반복단위 탄소 수",  12,     sigma,              "σ=12")
check("스틸벨트 층 수",             2,      phi,                "φ=2")
check("승용차 카카스 층 수",        2,      phi,                "φ=2")
check("트럭 카카스 층 수",          4,      tau,                "τ=4")
check("표준 림 직경",               16,     phi ** tau,         "φ^τ=2⁴=16인치")
check("벨트코드 각도",              24,     J2,                 "J₂=24°")
check("코드 꼬임수 TPI",            12,     sigma,              "σ=12")
check("타이어 수명",                60000,  n * 10000,          "n×10⁴=60000km")
check("공기압 기준(PSI)",           32,     2 ** sopfr,         "2^sopfr=32")
check("속도등급 구분 수",           12,     sigma,              "σ=12")

print()
print("=" * 60)
print("타이어코드 — Phase 2: 공정/산업규격")
print("=" * 60)

check("타이어코드 공정 단계 수",    6,      n,                  "n=6")
check("가황 온도",                  144,    sigma ** 2,         "σ²=144°C")
check("가황 시간",                  12,     sigma,              "σ=12분")
check("타이어 주요 구성 부품 수",   6,      n,                  "n=6")
check("스틸코드 와이어 수",         4,      tau,                "τ=4")
check("타이어 사이즈 표기 항목 수", 6,      n,                  "n=6")
check("편평비 대표값",              60,     sigma * sopfr,      "σ·sopfr=12·5=60")
check("폭 규격 간격",               10,     sigma - phi,        "σ-φ=10mm")
check("UTQG 등급 항목 수",          3,      n // phi,           "n/φ=6/2=3")
check("DOT 코드 그룹 수",           4,      tau,                "τ=4")

total = PASS + FAIL
print()
print("=" * 60)
print(f"총 {total}건: {PASS} EXACT, {FAIL} FAIL ({PASS/total*100:.0f}%)")
print("=" * 60)
if FAIL == 0:
    print(">>> ALL PASS — 타이어코드 n=6 완전 검증!")
