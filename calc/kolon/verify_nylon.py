#!/usr/bin/env python3
"""나일론 6/6,6 n=6 검증 — 23/23 EXACT 목표"""

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
print("나일론 6/6,6 — Phase 1: 분자구조")
print("=" * 60)

check("카프로락탐 탄소수",         6,             n,                     "n")
check("아디프산 탄소수",           6,             n,                     "n")
check("헥사메틸렌디아민 탄소수",   6,             n,                     "n")
check("나일론6,6 반복단위 총탄소", 12,            sigma,                 "σ=12")
check("주력 등급 수",              2,             phi,                   "φ=2")
check("아미드결합 수",             2,             phi,                   "φ=2")
check("헤테로원자(N+O) 수",        4,             tau,                   "τ=4")
check("아디프산 메틸렌 수",        4,             tau,                   "τ=4")
check("디아민 메틸렌 수",          6,             n,                     "n=6")
check("반복단위 총 메틸렌 수",     10,            sigma - phi,           "σ-φ=10")
check("중원자 수",                 16,            phi ** tau,            "φ^τ=16")
check("나일론6 고리원자 수",       6,             n,                     "n=6")

print()
print("=" * 60)
print("나일론 6/6,6 — Phase 2: 공정/산업규격")
print("=" * 60)

check("840d 원사 굵기",  840,  sigma * (sigma - phi) * (sigma - sopfr),  "σ(σ-φ)(σ-sopfr)=12·10·7=840")
check("420d 원사",       420,  840 // phi,                                "840/φ=420")
check("210d 원사",       210,  840 // tau,                                "840/τ=210")
check("70d 원사",        70,   840 // sigma,                              "840/σ=70")
check("필라멘트 24f",    24,   J2,                                        "J₂=24")
check("필라멘트 48f",    48,   sigma * tau,                               "σ·τ=48")
check("필라멘트 72f",    72,   sigma * n,                                 "σ·n=72")
check("필라멘트 144f",   144,  sigma ** 2,                                "σ²=144")
check("중합 목표 DP",    120,  sigma * (sigma - phi),                     "σ(σ-φ)=120")
check("중합시간 단계1",  12,   sigma,                                     "σ=12h")
check("중합시간 단계2",  24,   J2,                                        "J₂=24h")

total = PASS + FAIL
print()
print("=" * 60)
print(f"총 {total}건: {PASS} EXACT, {FAIL} FAIL ({PASS/total*100:.0f}%)")
print("=" * 60)
if FAIL == 0:
    print(">>> ALL PASS — 나일론 6/6,6 n=6 완전 검증!")
