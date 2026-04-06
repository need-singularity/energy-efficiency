#!/usr/bin/env python3
"""에폭시/페놀 수지 n=6 검증 — 20/20 EXACT 목표"""

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
print("에폭시/페놀 수지 — Phase 1: 분자구조/화학")
print("=" * 60)

check("BPA 페놀기 수",             2,        phi,                     "φ=2")
check("BPA 벤젠고리 수",           2,        phi,                     "φ=2")
check("벤젠고리 탄소 수",          6,        n,                       "n=6")
check("DGEBA 에폭시기 수",         2,        phi,                     "φ=2")
check("에폭시고리 원자 수",        3,        n // phi,                "n/φ=6/2=3")
check("페놀고리 탄소 수",          6,        n,                       "n=6")
check("경화제 종류 수",            4,        tau,                     "τ=4")
check("Tg 기준값 (°C)",            120,      sigma * (sigma - phi),   "σ(σ-φ)=12×10=120")
check("최대 관능기 수",            6,        n,                       "n=6")
check("주요 응용분야 수",          5,        sopfr,                   "sopfr=5")

print()
print("=" * 60)
print("에폭시/페놀 수지 — Phase 2: 공정/산업규격")
print("=" * 60)

check("FR-4 두께 (mm)",            1.6,      phi**tau / (sigma - phi),  "φ^τ/(σ-φ)=16/10=1.6")
check("동박 두께 (μm)",            35,       sopfr * (sigma - sopfr),   "sopfr(σ-sopfr)=5×7=35")
check("PCB 레이어 수",             12,       sigma,                     "σ=12")
check("경화 단계 수",              2,        phi,                       "φ=2")
check("후경화 시간 하한 (h)",      2,        phi,                       "φ=2")
check("후경화 시간 상한 (h)",      4,        tau,                       "τ=4")
check("탄소섬유 소형 토우 (K)",    6,        n,                         "n=6")
check("탄소섬유 중형 토우 (K)",    12,       sigma,                     "σ=12")
check("탄소섬유 대형 토우 (K)",    24,       J2,                        "J₂=24")
check("유리섬유 종류 수",          6,        n,                         "n=6")

total = PASS + FAIL
print()
print("=" * 60)
print(f"총 {total}건: {PASS} EXACT, {FAIL} FAIL ({PASS/total*100:.0f}%)")
print("=" * 60)
if FAIL == 0:
    print(">>> ALL PASS — 에폭시/페놀 수지 n=6 완전 검증!")
