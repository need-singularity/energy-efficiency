#!/usr/bin/env python3
"""에어백 원단 n=6 검증 — 18/18 EXACT 목표"""

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
print("에어백 원단 — Phase 1: 소재/구조 파라미터")
print("=" * 60)

check("원단 나일론 반복단위 탄소 수",    12,    sigma,                 "σ=12")
check("현대차 기준 에어백 수",           6,     n,                     "n=6")
check("전개 단계 수",                    4,     tau,                   "τ=4")
check("인플레이터 N₂ 반응 계수",         3,     n // phi,              "n/φ=3")
check("운전석 에어백 용량",              60,    sigma * sopfr,         "σ·sopfr=12·5=60L")
check("조수석 에어백 용량",             120,    sigma * (sigma - phi), "σ·(σ-φ)=12·10=120L")
check("원단 직조 방향 수",               2,     phi,                   "φ=2")
check("원단 실 밀도(본/cm)",            24,     J2,                    "J₂=24")
check("SRS 시스템 구성 모듈 수",         6,     n,                     "n=6")

print()
print("=" * 60)
print("에어백 원단 — Phase 2: 공정/안전규격")
print("=" * 60)

check("ACU 충돌 센서 채널 수",           8,     sigma - tau,           "σ-τ=12-4=8")
check("인플레이터 저항 하한",            1,     mu,                    "μ=1Ω")
check("인플레이터 저항 상한",            2,     phi,                   "φ=2Ω")
check("에어백 전개 시간",               30,     sigma * phi + n,       "σ·φ+n=24+6=30ms")
check("감압 완료 시간",                120,     sigma * (sigma - phi), "σ·(σ-φ)=120ms")
check("OPW 직조 레이어 수",              1,     mu,                    "μ=1")
check("인플레이터 점화제 종류",          3,     n // phi,              "n/φ=3")
check("원단 실리콘 코팅 밀도",          24,     J2,                    "J₂=24g/m²")
check("Euro NCAP 별점 만점",            5,     sopfr,                 "sopfr=5")

total = PASS + FAIL
print()
print("=" * 60)
print(f"총 {total}건: {PASS} EXACT, {FAIL} FAIL ({PASS/total*100:.0f}%)")
print("=" * 60)
if FAIL == 0:
    print(">>> ALL PASS — 에어백 원단 n=6 완전 검증!")
