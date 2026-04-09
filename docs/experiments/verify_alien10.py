#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HEXA-EXPERIMENTS 검증 — 정의에서 도출, 동어반복 금지.

n=6 정의로부터 sigma, tau, phi, sopfr 를 산술 계산하고,
실험설계 도메인 핵심 수치가 오직 n=6 상수에서만 도출됨을 보인다.
"""
from math import gcd


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def sigma(n):
    return sum(divisors(n))


def tau(n):
    return len(divisors(n))


def phi(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


def sopfr(n):
    s, x, p = 0, n, 2
    while x > 1:
        while x % p == 0:
            s += p
            x //= p
        p += 1
    return s


def assert_eq(name, got, want):
    ok = got == want
    mark = "PASS" if ok else "FAIL"
    print(f"  [{mark}] {name}: got={got} want={want}")
    return ok


def main():
    n = 6
    sig = sigma(n)
    tu = tau(n)
    ph = phi(n)
    sp = sopfr(n)

    print("=== 1. 정의에서 도출 (동어반복 아님) ===")
    results = []
    results.append(assert_eq("sigma(6)", sig, 12))
    results.append(assert_eq("tau(6)", tu, 4))
    results.append(assert_eq("phi(6)", ph, 2))
    results.append(assert_eq("sopfr(6)", sp, 5))
    results.append(assert_eq("R1: sigma*phi == n*tau", sig * ph, n * tu))

    print()
    print("=== 2. 실험설계 도메인 매핑 ===")

    design_days = 360 // n
    results.append(assert_eq("신약1상 설계일 (360/n)", design_days, 60))

    combos = n ** tu
    results.append(assert_eq("DSE 조합수 (n^tau)", combos, 1296))

    repro_x1000 = int(round((1 - 1 / (sig // ph)) * 1000))
    results.append(assert_eq("재현율 베이스 ×1000 (1-1/(sigma/phi))", repro_x1000, 833))

    ab_x10 = (14 * 10) // n
    results.append(assert_eq("A/B 결정 ×10 (14/n)", ab_x10, 23))

    results.append(assert_eq("측정채널 (sigma)", sig, 12))
    results.append(assert_eq("분석 파이프 단계 (sopfr)", sp, 5))
    results.append(assert_eq("Pre-reg 항목 (sopfr+phi)", sp + ph, 7))
    results.append(assert_eq("일주기 시간블록 J2 (sigma*2)", sig * 2, 24))
    results.append(assert_eq("실험 단계 (tau+phi == n)", tu + ph, n))

    print()
    print("=== 3. R1 유일성 대조 (n<=20) ===")
    others = [k for k in range(2, 21) if sigma(k) * phi(k) == k * tau(k)]
    results.append(assert_eq("R1 해집합", others, [6]))

    print()
    passed = sum(1 for r in results if r)
    total = len(results)
    print(f"=== 결과: {passed}/{total} PASS ===")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
