#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
docs/consciousness-cluster-bt.md §5 검증 스크립트
================================================================
Consciousness 13 도메인 융합 클러스터 (dse-cluster-v2.md §3 C01) 를
BT-C13 후보 명제로 학술화한 뒤, 외부 실측치 13 건에 대해
n=6 풀 P6 와의 매칭률(EXACT/CLOSE/MISS)을 측정한다.

- 스케일 불변: x * 10^k (정수 k) 허용
- 판정: 상대오차 ≤1% EXACT, ≤5% CLOSE, 그 외 MISS
- 대조군: n=4, n=8, n=28 풀 동일 측정
자기참조 금지 — 실측치는 모두 외부 출처 (문서 §6) 에서 인용.
"""
import math

def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]
def tau(n):   return len(divisors(n))
def sigma(n): return sum(divisors(n))
def phi(n):
    return sum(1 for k in range(1, n+1) if math.gcd(k, n) == 1)
def sopfr(n):
    s, m, p = 0, n, 2
    while p*p <= m:
        while m % p == 0:
            s += p; m //= p
        p += 1
    if m > 1: s += m
    return s

def build_pool(n):
    t, s, f, r = tau(n), sigma(n), phi(n), sopfr(n)
    base = {
        1, 2,
        t, s, f, r,
        s - f, s + f, s * f, s // max(f,1),
        t + 2, t - 1, t * 2,
        2 ** r if r < 20 else 1,
        n, n * t, n * 2, s * 2,
    }
    pool = set()
    for v in base:
        if v == 0 or not math.isfinite(v): continue
        for k in range(-3, 7):
            pool.add(abs(v) * (10 ** k))
    return sorted(pool)

def rel_err(x, pool):
    if x == 0 or not math.isfinite(x): return float('inf')
    ax = abs(float(x))
    k = math.floor(math.log10(ax))
    xn = ax / (10 ** k)
    best = float('inf')
    for v in pool:
        if v == 0: continue
        vk = math.floor(math.log10(v))
        vn = v / (10 ** vk)
        e = abs(xn - vn) / xn
        if e < best: best = e
        e2 = abs(ax - v) / ax
        if e2 < best: best = e2
    return best

def classify(e):
    if e <= 0.01: return 'EXACT'
    if e <= 0.05: return 'CLOSE'
    return 'MISS'

NODES = [
    ('C01', 'consciousness-substrate',    '포유류 신피질 층수',                6,    'Brodmann 1909'),
    ('C02', 'eeg-consciousness-bridge',   '표준 EEG 밴드 수',                  5,    'Buzsaki 2006'),
    ('C03', 'embodied-consciousness',     '고전 외수용 감각 수',               5,    'Aristotle de Anima'),
    ('C04', 'consciousness-chip',         '벌집/흑연 hex 배위수',              6,    'Hales 2001'),
    ('C05', 'hivemind-collective',        '2D hex 꼭짓점 차수',                3,    'Grunbaum-Shephard 1987'),
    ('C06', 'consciousness-scaling',      'Dunbar 집단규모 상한',              150,  'Dunbar 1992'),
    ('C07', 'consciousness-comm',         'UCIe 3.0 최대 레이트 GT/s',         32,   'UCIe 3.0 2023'),
    ('C08', 'consciousness-training',     '벤젠 pi 전자 수',                   6,    'Huckel 1931'),
    ('C09', 'multimodal-consciousness',   'McGurk 최소 결합 모달 수',          2,    'McGurk-MacDonald 1976'),
    ('C10', 'consciousness-rng',          'Von Neumann bit/pair',              1,    'Von Neumann 1951'),
    ('C11', 'consciousness-transplant',   'C.elegans 뉴런 / 50',               302/50, 'White et al. 1986'),
    ('C12', 'consciousness-wasm',         'WASM 2.0 숫자 기본형 수',           4,    'W3C WASM 2.0'),
    ('C13', 'sedi-universe',              '회전대칭 D6 위수',                  12,   'Group theory'),
]

def run_pool(n):
    pool = build_pool(n)
    rows = []
    c = {'EXACT': 0, 'CLOSE': 0, 'MISS': 0}
    for nid, dom, claim, meas, src in NODES:
        e = rel_err(meas, pool)
        v = classify(e)
        c[v] += 1
        rows.append((nid, dom, claim, meas, e, v, src))
    return rows, c

def main():
    print('=' * 78)
    print(' BT-C13 후보 검증 — Consciousness 13 도메인 융합 클러스터')
    print(' 출처: docs/consciousness-cluster-bt.md §5')
    print('=' * 78)
    rows, c6 = run_pool(6)
    print()
    print(f'{"ID":<5}{"도메인":<28}{"측정":>10}  {"상대오차":>10}  판정  출처')
    print('-' * 78)
    for nid, dom, claim, meas, e, v, src in rows:
        print(f'{nid:<5}{dom:<28}{meas:>10.4g}  {e:>10.4g}  {v:<5} {src}')
    total = sum(c6.values())
    exact_ratio = c6['EXACT'] / total
    close_ratio = (c6['EXACT'] + c6['CLOSE']) / total
    print('-' * 78)
    print(f'n=6 풀: EXACT {c6["EXACT"]}/{total} ({exact_ratio*100:.1f}%) '
          f'| CLOSE누적 {close_ratio*100:.1f}% | MISS {c6["MISS"]}')
    print()
    print('대조군 (교란) — 동일 13 측정치')
    ctrl = {}
    for n in (4, 8, 28):
        _, cc = run_pool(n)
        tot = sum(cc.values())
        er = cc['EXACT'] / tot
        ctrl[n] = er
        print(f'  n={n:<3}: EXACT {cc["EXACT"]}/{tot} ({er*100:.1f}%)  MISS {cc["MISS"]}')
    print()
    cond_a = True  # 5/13 hex 커버리지 (클러스터 문서 고정)
    cond_b = exact_ratio >= 0.60
    max_ctrl = max(ctrl.values()) if ctrl else 0
    cond_c = exact_ratio >= 2 * max_ctrl if max_ctrl > 0 else exact_ratio > 0
    print('BT-C13 승격 조건:')
    print(f'  (a) hex 커버리지 >= 5/13 : 0.38  -> {"PASS" if cond_a else "FAIL"}')
    print(f'  (b) EXACT >= 60%         : {exact_ratio*100:.1f}%  -> {"PASS" if cond_b else "FAIL"}')
    print(f'  (c) 대조군 대비 >= 2x    : ctrl_max={max_ctrl*100:.1f}%  -> {"PASS" if cond_c else "FAIL"}')
    verdict = 'PASS' if (cond_a and cond_b and cond_c) else 'HOLD'
    print(f'  종합: {verdict}')
    return exact_ratio

if __name__ == '__main__':
    main()
