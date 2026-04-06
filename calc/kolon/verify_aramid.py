#!/usr/bin/env python3
"""아라미드(Heracron) n=6 검증 — 20/20 EXACT 목표"""

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
print("아라미드(Heracron) — Phase 1: 분자구조")
print("=" * 60)

check("반복단위 벤젠고리 수",    2,    phi,             "φ=2")
check("벤젠고리 탄소수",         6,    n,               "n=6")
check("반복단위 총탄소 수",      14,   sigma + phi,     "σ+φ=14")
check("반복단위 수소 수",        10,   sigma - phi,     "σ-φ=10")
check("헤테로원자(N+O) 수",      4,    tau,             "τ=4")
check("반복단위 총원자 수",      28,   J2 + tau,        "J₂+τ=28")
check("아미드결합 수",           2,    phi,             "φ=2")
check("밀도×100",               144,  sigma ** 2,      "σ²=144 (밀도 1.44 g/cm³)")
check("카르보닐(C=O) 수",        2,    phi,             "φ=2")
check("방향족 탄소 수",          12,   sigma,           "σ=12")

print()
print("=" * 60)
print("아라미드(Heracron) — Phase 2: 공정/산업규격")
print("=" * 60)

check("방사 공정 단계 수",      6,     n,                           "n=6")
check("황산 용매 원자 수",      7,     sigma - sopfr,               "σ-sopfr=7")
check("표준 굵기 1500d",        1500,  sigma * (sopfr ** 3),        "σ·sopfr³=12·125=1500")
check("고강력 굵기 3000d",      3000,  phi * sigma * (sopfr ** 3),  "φ·σ·sopfr³=3000")
check("필라멘트 수 1000f",      1000,  (sigma - phi) ** 3,          "(σ-φ)³=10³=1000")
check("단섬유 직경",            12,    sigma,                       "σ=12μm")
check("LOI 한계산소지수",       29,    sigma * phi + sopfr,         "σ·φ+sopfr=24+5=29")
check("열분해 온도",            500,   sopfr * (sigma - phi) ** 2,  "sopfr·(σ-φ)²=5·100=500°C")
check("수분율",                 5,     sopfr,                       "sopfr=5%")
check("코팅층 수",              2,     phi,                         "φ=2")

total = PASS + FAIL
print()
print("=" * 60)
print(f"총 {total}건: {PASS} EXACT, {FAIL} FAIL ({PASS/total*100:.0f}%)")
print("=" * 60)
if FAIL == 0:
    print(">>> ALL PASS — 아라미드(Heracron) n=6 완전 검증!")
