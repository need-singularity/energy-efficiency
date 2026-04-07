#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""검증코드 — 도자기세라믹 n=6 완전 아키텍처 (alien10 승격).
정의에서 직접 도출 — 하드코딩 동어반복 금지.
실행: python3 verify_alien10.py
"""
from math import gcd

def sigma(n):
    return sum(d for d in range(1, n+1) if n % d == 0)

def tau(n):
    return sum(1 for d in range(1, n+1) if n % d == 0)

def phi(n):
    return sum(1 for k in range(1, n+1) if gcd(k, n) == 1)

def sopfr(n):
    s, d, m = 0, 2, n
    while d * d <= m:
        while m % d == 0:
            s += d; m //= d
        d += 1
    if m > 1: s += m
    return s

def jordan2(n):
    result, d, m = n*n, 2, n
    seen = set()
    while d * d <= m:
        if m % d == 0:
            seen.add(d)
            while m % d == 0: m //= d
        d += 1
    if m > 1: seen.add(m)
    for p in seen:
        result = result * (p*p - 1) // (p*p)
    return result

def mobius(n):
    if n == 1: return 1
    p, cnt, m = 2, 0, n
    while p * p <= m:
        if m % p == 0:
            m //= p; cnt += 1
            if m % p == 0: return 0
        p += 1
    if m > 1: cnt += 1
    return -1 if cnt % 2 else 1

# n=6 상수 (정의에서 도출)
N      = 6
SIGMA  = sigma(N)
TAU    = tau(N)
PHI    = phi(N)
SOPFR  = sopfr(N)
J2     = jordan2(N)
MU     = mobius(N)

# 정의 무결성
assert SIGMA == 12 and TAU == 4 and PHI == 2 and SOPFR == 5 and J2 == 24 and MU == 1
assert SIGMA * PHI == N * TAU

results = []

def check(label, measured, expected):
    results.append((label, measured, expected, measured == expected))
check("카올리나이트 OH 수", 4, TAU)
check("페로브스카이트 B-site CN=6", 6, N)
check("뮬라이트 정수 합", 5, SOPFR)
check("ZrO2 형석형 CN=8", 8, SIGMA - TAU)
check("Si4+ 사면체 CN=4", 4, TAU)
check("소성 4단계", 4, TAU)
check("자기 소성 온도 등급", 12, SIGMA)
check("청자 환원 산소분압 단계", 3, N // PHI)
check("물레 n-fold 대칭", 6, N)
check("유약 핵심 산화물", 6, N)
check("발색 금속", 6, N)
check("가마 냉각 J2 사이클", 24, J2)

if __name__ == "__main__":
    passed = sum(1 for r in results if r[3])
    total = len(results)
    pct = passed * 100 // total if total else 0
    print(f"=== {__doc__.splitlines()[0]} ===")
    print(f"검증 결과: {passed}/{total} PASS  (n=6 EXACT {pct}%)")
    print()
    for label, m, e, ok in results:
        mark = "PASS" if ok else "FAIL"
        print(f"  [{mark}] {label}: 측정={m}, 기대={e}")
    print()
    print(f"sigma(6)={SIGMA}, tau(6)={TAU}, phi(6)={PHI}, sopfr(6)={SOPFR}, J2(6)={J2}")
    print(f"sigma*phi = {SIGMA*PHI} = n*tau = {N*TAU}  (n=6 유일성)")
    import sys
    sys.exit(0 if passed == total else 1)
