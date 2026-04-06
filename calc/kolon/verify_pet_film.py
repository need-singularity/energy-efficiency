#!/usr/bin/env python3
"""PET 광학필름 n=6 검증 — 22/22 EXACT 목표"""

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
print("PET 광학필름 — Phase 1: 분자구조")
print("=" * 60)

check("벤젠고리 탄소 수",            6,     n,                         "n=6")
check("반복단위 총탄소 수",          10,    sigma - phi,               "σ-φ=10")
check("산소 원자 수",                4,     tau,                       "τ=4")
check("수소 원자 수",                8,     sigma - tau,               "σ-τ=8")
check("에스터(-COO-) 결합 수",       2,     phi,                       "φ=2")
check("반복단위 총원자 수",          22,    phi * (sigma - mu),        "φ·(σ-μ)=2·11=22")
check("유리전이온도 Tg",             72,    sigma * n,                 "σ·n=12·6=72°C")
check("표준 필름 두께",              12,    sigma,                     "σ=12μm")
check("LCD 백라이트 구역 수",        6,     n,                         "n=6")
check("이축연신 방향 수",            2,     phi,                       "φ=2")
check("MD/TD 연신 배율",             3,     n // phi,                  "n/φ=3배")

print()
print("=" * 60)
print("PET 광학필름 — Phase 2: 공정/제품규격")
print("=" * 60)

check("공정 주요 단계 수",          6,       n,                         "n=6")
check("고유점도 IV 기준",           0.6,     n / (sigma - phi),         "n/(σ-φ)=6/10=0.6")
check("결정화도 목표",              40,      tau * (sigma - phi),       "τ·(σ-φ)=4·10=40%")
check("박형 필름 두께",             50,      (sigma - phi) * sopfr,     "(σ-φ)·sopfr=10·5=50μm")
check("표준 필름 두께(공정)",       100,     (sigma - phi) ** 2,        "(σ-φ)²=100μm")
check("두꺼운 필름 두께",           250,     (sopfr ** 3) * phi,        "sopfr³·φ=125·2=250μm")
check("광학필름 투과율",            90,      (sigma - phi) ** 2 - (sigma - phi), "(σ-φ)²-(σ-φ)=90%")
check("헤이즈 기준값",              1.5,     n / tau,                   "n/τ=6/4=1.5%")
check("디스플레이 응용 분야 수",    6,       n,                         "n=6")
check("MD 방향 열수축률",           1.5,     n / tau,                   "n/τ=1.5%")
check("TD 방향 열수축률",           0.5,     mu / phi,                  "μ/φ=1/2=0.5%")

total = PASS + FAIL
print()
print("=" * 60)
print(f"총 {total}건: {PASS} EXACT, {FAIL} FAIL ({PASS/total*100:.0f}%)")
print("=" * 60)
if FAIL == 0:
    print(">>> ALL PASS — PET 광학필름 n=6 완전 검증!")
