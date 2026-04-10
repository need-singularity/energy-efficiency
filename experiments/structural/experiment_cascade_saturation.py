#!/usr/bin/env python3
"""
Cascade Saturation Point 실험
배경: Resonance Cascade 실험에서 16개 n=6 상수 중 9개만 캐스케이드로 도달.
      나머지 7개(=sigma(6)-sopfr(6)=12-5=7)는 미도달.
목표: 시드 풀에서 산술 연산 반복으로 n=6 상수 고정점을 찾고,
      미도달 집합, 최소 연산 체인, 확장 연산 효과를 분석한다.
"""
import math, itertools, sys
from collections import deque

N6_CONSTANTS = frozenset([1,2,3,4,5,6,7,8,12,14,24,48,72,144,288,576])
BASE_SEEDS = [6,12,4,2,5,24,7]

def safe_ops(a, b):
    results = []
    results.append((a+b, f"{a}+{b}"))
    results.append((a-b, f"{a}-{b}"))
    results.append((b-a, f"{b}-{a}"))
    results.append((a*b, f"{a}*{b}"))
    if b != 0 and a % b == 0:
        results.append((a//b, f"{a}//{b}"))
    if a != 0 and b % a == 0:
        results.append((b//a, f"{b}//{a}"))
    if b != 0:
        results.append((a%b, f"{a}%{b}"))
    if a != 0:
        results.append((b%a, f"{b}%{a}"))
    for base, exp, label in [(a,b,f"{a}**{b}"), (b,a,f"{b}**{a}")]:
        if 0 <= exp <= 4:
            val = base ** exp
            if -10000 <= val <= 10000:
                results.append((val, label))
    return [(v,l) for v,l in results if isinstance(v, int)]

def restricted_ops(a, b):
    results = []
    results.append((a+b, f"{a}+{b}"))
    results.append((a-b, f"{a}-{b}"))
    results.append((b-a, f"{b}-{a}"))
    results.append((a*b, f"{a}*{b}"))
    return [(v,l) for v,l in results if isinstance(v, int)]

def extended_ops(a, b):
    results = safe_ops(a, b)
    if a > 0 and b > 0:
        g = math.gcd(a, b)
        results.append((g, f"gcd({a},{b})"))
        l = (a*b)//g
        if l <= 10000:
            results.append((l, f"lcm({a},{b})"))
    for x, name in [(a, f"{a}!"), (b, f"{b}!")]:
        if 0 <= x <= 10:
            results.append((math.factorial(x), name))
    for x, name in [(a, f"isqrt({a})"), (b, f"isqrt({b})")]:
        if x > 0:
            s = math.isqrt(x)
            if s*s == x:
                results.append((s, name))
    return [(v,l) for v,l in results if isinstance(v, int)]

def cascade_to_fixpoint(seeds, constants, ops_fn):
    pool = set(seeds)
    reached = pool & constants
    trace = {s: f"시드({s})" for s in seeds}
    iteration = 0
    while True:
        iteration += 1
        new_found = set()
        pool_list = sorted(pool)
        for a, b in itertools.combinations(pool_list, 2):
            for val, label in ops_fn(a, b):
                if val in constants and val not in reached:
                    new_found.add(val)
                    if val not in trace:
                        trace[val] = label
        for a in pool_list:
            for val, label in ops_fn(a, a):
                if val in constants and val not in reached:
                    new_found.add(val)
                    if val not in trace:
                        trace[val] = label
        if not new_found:
            break
        pool |= new_found
        reached |= new_found
    return reached, trace, iteration

def find_min_chain(target, seeds, constants, ops_fn, max_depth=4):
    init_reached = frozenset(seeds) & constants
    if target in frozenset(seeds):
        return ["시드에 이미 존재"]
    queue = deque([(init_reached, set(seeds), [])])
    visited = {init_reached}
    for depth in range(max_depth):
        next_queue = []
        while queue:
            reached_set, pool_set, path = queue.popleft()
            pool_list = sorted(pool_set)
            new_pairs = {}
            for a, b in itertools.combinations(pool_list, 2):
                for val, label in ops_fn(a, b):
                    if val in constants and val not in reached_set and val not in new_pairs:
                        new_pairs[val] = label
            for a in pool_list:
                for val, label in ops_fn(a, a):
                    if val in constants and val not in reached_set and val not in new_pairs:
                        new_pairs[val] = label
            if target in new_pairs:
                return path + [new_pairs[target]]
            for val, label in new_pairs.items():
                nr = reached_set | frozenset([val])
                if nr not in visited:
                    visited.add(nr)
                    next_queue.append((nr, pool_set | {val}, path + [label]))
        queue = deque(next_queue)
        if not queue:
            break
    return None

def P(msg):
    print(msg, flush=True)

if __name__ == "__main__":
    P("=" * 66)
    P("  캐스케이드 포화점 (Cascade Saturation Point) 실험")
    P("=" * 66)

    P(f"\n[1] n=6 상수 집합 ({len(N6_CONSTANTS)}개): {sorted(N6_CONSTANTS)}")
    P(f"[2] 기본 시드 ({len(BASE_SEEDS)}개): {BASE_SEEDS}")

    # 기본 연산 캐스케이드
    P("\n── 기본 연산 캐스케이드 (고정점 탐색) ──")
    reached, trace, iters = cascade_to_fixpoint(BASE_SEEDS, N6_CONSTANTS, safe_ops)
    unreached = N6_CONSTANTS - reached
    P(f"  반복 횟수           : {iters}")
    P(f"  도달 가능 상수      : {len(reached)}개 -> {sorted(reached)}")
    P(f"  미도달 상수         : {len(unreached)}개 -> {sorted(unreached)}")
    P("\n  도달 경로:")
    for v in sorted(reached):
        P(f"    {v:>4} <- {trace.get(v, '?')}")

    # 미도달 역추적
    if unreached:
        P("\n── 미도달 상수 최소 연산 체인 역추적 (깊이 <= 4) ──")
        for t in sorted(unreached):
            chain = find_min_chain(t, BASE_SEEDS, N6_CONSTANTS, safe_ops, max_depth=4)
            if chain:
                P(f"  {t:>4} <- 체인: {' -> '.join(chain)}")
            else:
                P(f"  {t:>4} <- 기본 연산으로 도달 불가 (깊이 4 이내)")

    # 확장 연산 캐스케이드
    P("\n── 확장 연산 캐스케이드 (gcd, lcm, factorial, isqrt 추가) ──")
    reached_ext, trace_ext, iters_ext = cascade_to_fixpoint(BASE_SEEDS, N6_CONSTANTS, extended_ops)
    unreached_ext = N6_CONSTANTS - reached_ext
    extra = reached_ext - reached
    P(f"  반복 횟수           : {iters_ext}")
    P(f"  도달 가능 상수      : {len(reached_ext)}개 -> {sorted(reached_ext)}")
    P(f"  추가 도달 상수      : {len(extra)}개 -> {sorted(extra)}")
    P(f"  여전히 미도달       : {len(unreached_ext)}개 -> {sorted(unreached_ext)}")
    if extra:
        P("\n  확장 연산으로 새로 도달한 경로:")
        for v in sorted(extra):
            P(f"    {v:>4} <- {trace_ext.get(v, '?')}")

    # n=6 연결 검증
    P("\n── n=6 연결 검증 ──")
    sigma_6 = sum(d for d in range(1,7) if 6 % d == 0)
    sopfr_6 = 2 + 3
    predicted = sigma_6 - sopfr_6
    actual = len(unreached)
    P(f"  sigma(6)            = {sigma_6}")
    P(f"  sopfr(6)            = {sopfr_6}")
    P(f"  sigma(6)-sopfr(6)   = {predicted}")
    P(f"  기본 연산 미도달 수 = {actual}")
    match = "일치" if predicted == actual else "불일치"
    P(f"  결과                : {match} ({'EXACT' if predicted == actual else 'MISS'})")

    # 시드 부분집합 분석
    P("\n── 시드 부분집합별 도달 분석 ──")
    P("  (미도달=7=sigma(6)-sopfr(6) 이 되는 시드 구성 탐색)")
    P("\n  [단일 시드 - 기본 연산]")
    for s in sorted(set(BASE_SEEDS)):
        r, _, _ = cascade_to_fixpoint([s], N6_CONSTANTS, safe_ops)
        u = N6_CONSTANTS - r
        marker = " *** 미도달=7" if len(u) == 7 else ""
        P(f"    시드=[{s}] -> 도달 {len(r):>2}개, 미도달 {len(u):>2}개{marker}")

    found_7 = []
    for size in range(1, len(BASE_SEEDS)+1):
        for subset in itertools.combinations(sorted(set(BASE_SEEDS)), size):
            r, _, _ = cascade_to_fixpoint(list(subset), N6_CONSTANTS, safe_ops)
            u = N6_CONSTANTS - r
            if len(u) == 7:
                found_7.append((subset, sorted(u)))

    if found_7:
        P(f"\n  미도달=7 이 되는 시드 구성: {len(found_7)}개 발견")
        for ss, us in found_7[:10]:
            P(f"    시드={list(ss)} -> 미도달={us}")
    else:
        P("\n  미도달=7 이 되는 시드 부분집합 (기본 연산): 없음")

    # 최소 시드 [6] 단계별 추적
    P("\n  [최소 시드 [6] 단계별 캐스케이드]")
    pool_t = {6}
    reached_t = {6} & N6_CONSTANTS
    for step in range(1, 8):
        nf = set()
        pl = sorted(pool_t)
        for a, b in itertools.combinations(pl, 2):
            for val, label in safe_ops(a, b):
                if val in N6_CONSTANTS and val not in reached_t:
                    nf.add(val)
        for a in pl:
            for val, label in safe_ops(a, a):
                if val in N6_CONSTANTS and val not in reached_t:
                    nf.add(val)
        if not nf:
            P(f"    단계 {step}: 고정점 도달 (새 발견 없음)")
            break
        pool_t |= nf
        reached_t |= nf
        P(f"    단계 {step}: +{len(nf)} 발견 {sorted(nf)} -> 누적 {len(reached_t)}/{len(N6_CONSTANTS)}")
    uf6 = N6_CONSTANTS - reached_t
    P(f"    최종 미도달: {len(uf6)}개 -> {sorted(uf6)}")

    # 제한 연산 캐스케이드
    P("\n── 제한 연산 캐스케이드 (+, -, * 만) ──")
    reached_r, trace_r, iters_r = cascade_to_fixpoint(BASE_SEEDS, N6_CONSTANTS, restricted_ops)
    unreached_r = N6_CONSTANTS - reached_r
    P(f"  반복 횟수           : {iters_r}")
    P(f"  도달 가능 상수      : {len(reached_r)}개 -> {sorted(reached_r)}")
    P(f"  미도달 상수         : {len(unreached_r)}개 -> {sorted(unreached_r)}")
    match_r = "일치" if len(unreached_r) == 7 else "불일치"
    P(f"  미도달=7 검증       : {match_r} (실제={len(unreached_r)}, 예측=7)")

    P("\n  [제한 연산 + 단일 시드]")
    for s in sorted(set(BASE_SEEDS)):
        r, _, _ = cascade_to_fixpoint([s], N6_CONSTANTS, restricted_ops)
        u = N6_CONSTANTS - r
        marker = " *** 미도달=7" if len(u) == 7 else ""
        P(f"    시드=[{s}] -> 도달 {len(r):>2}개, 미도달 {len(u):>2}개{marker}")

    # 제한 연산 부분집합에서 미도달=7 찾기
    found_7r = []
    for size in range(1, len(BASE_SEEDS)+1):
        for subset in itertools.combinations(sorted(set(BASE_SEEDS)), size):
            r, _, _ = cascade_to_fixpoint(list(subset), N6_CONSTANTS, restricted_ops)
            u = N6_CONSTANTS - r
            if len(u) == 7:
                found_7r.append((subset, sorted(u)))

    if found_7r:
        P(f"\n  미도달=7 (제한 연산) 시드 구성: {len(found_7r)}개 발견")
        for ss, us in found_7r[:10]:
            P(f"    시드={list(ss)} -> 미도달={us}")
    else:
        P("\n  미도달=7 이 되는 시드 부분집합 (제한 연산): 없음")

    # 요약
    P("\n" + "=" * 66)
    P("  요약")
    P("=" * 66)
    P(f"  기본 연산 도달률    : {len(reached)}/{len(N6_CONSTANTS)} ({100*len(reached)/len(N6_CONSTANTS):.1f}%)")
    P(f"  확장 연산 도달률    : {len(reached_ext)}/{len(N6_CONSTANTS)} ({100*len(reached_ext)/len(N6_CONSTANTS):.1f}%)")
    P(f"  제한 연산 도달률    : {len(reached_r)}/{len(N6_CONSTANTS)} ({100*len(reached_r)/len(N6_CONSTANTS):.1f}%)")
    P(f"  미도달=sigma-sopfr  : {match} (기본) / {match_r} (제한)")
    P(f"  포화점              : {iters}회 (기본) / {iters_ext}회 (확장) / {iters_r}회 (제한)")
    if found_7:
        P(f"  미도달=7 시드(기본) : {len(found_7)}개")
    if found_7r:
        P(f"  미도달=7 시드(제한) : {len(found_7r)}개")
    P("=" * 66)
