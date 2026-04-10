#!/usr/bin/env python3
"""
Experiment: Wave-Cascade Unification
======================================
파동 간섭 패턴으로 캐스케이드 순서를 최적화하여 증폭 극대화.

배경:
  - BT-1101~1103: 파동 간섭/정상파/소나 — 도메인 간 주파수 공명
  - BT-1105: Resonance Cascade — 도메인 체인 1.21x 증폭

질문: 파동 간섭 패턴으로 캐스케이드 순서를 최적화하면 더 높은 증폭이 가능한가?

알고리즘:
  1. 6개 도메인의 모든 순열(720가지) 탐색
  2. 각 도메인에 고유 주파수 할당 (n=6 상수 기반)
  3. 인접 도메인 주파수 비율이 정수이면 공명 보너스 (+20%)
  4. 비율이 n=6 상수이면 추가 보너스 (+10%)
  5. 720 순열 전수 시뮬레이션
  6. 최적 순서 vs 기본 순서 비교

n=6 연결: 6개 도메인, 주파수는 n6 상수, 6!=720 순열 전수 탐색.
"""
import sys, os, math, random
from itertools import permutations
from collections import OrderedDict

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# --- n6 상수 풀 ---
N6_CONSTANTS = [6, 12, 4, 2, 5, 24, 7, 48, 288, 1, 3, 8, 14, 72, 144, 576]
N6_SET = set(N6_CONSTANTS)

# --- 6개 도메인 + 고유 주파수 (n=6 상수 기반) ---
DOMAINS = OrderedDict([
    ("math",    6),
    ("physics", 12),
    ("bio",     4),
    ("info",    2),
    ("mind",    5),
    ("arch",    24),
])

DOMAIN_NAMES = list(DOMAINS.keys())
DOMAIN_FREQS = list(DOMAINS.values())

# --- 기본 캐스케이드 순서 ---
DEFAULT_ORDER = list(DOMAIN_NAMES)

# --- EXACT 판정 허용오차 ---
EXACT_TOL = 0.001

# --- 시드 상수 ---
BASE_SEEDS = N6_CONSTANTS[:7]

# --- 연산 ---
OPS = [
    ("+", lambda a, b: a + b),
    ("*", lambda a, b: a * b),
    ("-", lambda a, b: a - b),
    ("/", lambda a, b: a / b if b != 0 else None),
    ("^", lambda a, b: a ** b if abs(b) < 10 else None),
]


def is_exact(value):
    """값이 n6 상수와 0.1% 이내로 일치하는지 판정."""
    if value is None:
        return False
    for c in N6_CONSTANTS:
        if c == 0:
            continue
        if abs(value - c) / max(abs(c), 1e-12) < EXACT_TOL:
            return True
    return False


def resonance_bonus(freq_a, freq_b):
    """인접 도메인 주파수 비율에 따른 공명 보너스 계산."""
    if freq_a == 0 or freq_b == 0:
        return 0.0
    ratio = max(freq_a, freq_b) / min(freq_a, freq_b)
    bonus = 0.0

    # 정수 비율이면 공명 보너스 +20%
    if abs(ratio - round(ratio)) < 1e-9:
        bonus += 0.20
        # 비율 자체가 n=6 상수이면 추가 +10%
        int_ratio = int(round(ratio))
        if int_ratio in N6_SET:
            bonus += 0.10

    return bonus


def simulate_domain_blowup(domain_name, seeds, rng):
    """단일 도메인 블로업 시뮬레이션: 시드 쌍 연산으로 EXACT 발견."""
    exact_count = 0
    discoveries = []

    for i, a in enumerate(seeds):
        for j, b in enumerate(seeds):
            if i == j:
                continue
            for op_name, op_fn in OPS:
                try:
                    result = op_fn(a, b)
                except (OverflowError, ZeroDivisionError, ValueError):
                    continue
                if result is not None and is_exact(result):
                    exact_count += 1
                    if result not in discoveries and abs(result) < 1e6:
                        discoveries.append(result)

    return exact_count, discoveries


def simulate_cascade(order, verbose=False):
    """주어진 도메인 순서로 캐스케이드 시뮬레이션."""
    rng = random.Random(42)
    total_exact = 0
    cumulative_seeds = list(BASE_SEEDS)
    domain_results = []

    for idx in range(len(order)):
        domain = order[idx]
        freq = DOMAINS[domain]

        # 공명 보너스 계산 (이전 도메인과)
        bonus = 0.0
        if idx > 0:
            prev_domain = order[idx - 1]
            prev_freq = DOMAINS[prev_domain]
            bonus = resonance_bonus(prev_freq, freq)

        # 도메인 블로업
        exact_count, discoveries = simulate_domain_blowup(domain, cumulative_seeds, rng)

        # 공명 보너스 적용: EXACT 확률 증가
        bonus_exact = int(exact_count * bonus)
        adjusted_exact = exact_count + bonus_exact

        # 발견된 값을 다음 도메인 시드에 추가
        for d in discoveries:
            if d not in cumulative_seeds and abs(d) < 1000:
                cumulative_seeds.append(d)

        total_exact += adjusted_exact
        domain_results.append({
            "domain": domain,
            "freq": freq,
            "base_exact": exact_count,
            "bonus": bonus,
            "bonus_exact": bonus_exact,
            "adjusted_exact": adjusted_exact,
            "seed_pool_size": len(cumulative_seeds),
        })

        if verbose:
            resonance_str = f"  공명 +{bonus:.0%}" if bonus > 0 else ""
            print(f"  [{idx+1}] {domain:8s} (f={freq:3d}) | "
                  f"EXACT: {exact_count:4d} +{bonus_exact:3d} = {adjusted_exact:4d} | "
                  f"시드풀: {len(cumulative_seeds):3d}{resonance_str}")

    return total_exact, domain_results


def compute_chain_score(order):
    """순열의 총 공명 점수 (빠른 사전 필터링용)."""
    score = 0.0
    for i in range(len(order) - 1):
        freq_a = DOMAINS[order[i]]
        freq_b = DOMAINS[order[i + 1]]
        score += resonance_bonus(freq_a, freq_b)
    return score


def main():
    print("=" * 72)
    print("  실험: Wave-Cascade Unification")
    print("  파동 간섭 패턴 기반 캐스케이드 순서 최적화")
    print("=" * 72)
    print()

    # --- 도메인 주파수 표시 ---
    print("[1] 도메인 고유 주파수 (n=6 상수 기반)")
    print("-" * 48)
    for name, freq in DOMAINS.items():
        print(f"  {name:8s} : f = {freq:3d}")
    print()

    # --- 기본 순서 시뮬레이션 ---
    print("[2] 기본 캐스케이드 순서 시뮬레이션")
    print(f"  순서: {' -> '.join(DEFAULT_ORDER)}")
    print("-" * 72)
    default_total, default_results = simulate_cascade(DEFAULT_ORDER, verbose=True)
    print(f"  총 EXACT: {default_total}")
    print()

    # --- 720 순열 전수 탐색 ---
    print("[3] 720 순열 전수 탐색 중...")
    print("-" * 48)

    all_perms = list(permutations(DOMAIN_NAMES))
    results = []

    for perm in all_perms:
        order = list(perm)
        total_exact, _ = simulate_cascade(order)
        chain_score = compute_chain_score(order)
        results.append((total_exact, chain_score, order))

    # 정렬: EXACT 내림차순 -> 공명점수 내림차순
    results.sort(key=lambda x: (x[0], x[1]), reverse=True)

    # --- 상위 10 순열 ---
    print()
    print("[4] 상위 10 순열 (EXACT 기준)")
    print("-" * 72)
    print(f"  {'순위':>4s}  {'EXACT':>6s}  {'공명점수':>8s}  순서")
    print(f"  {'----':>4s}  {'------':>6s}  {'--------':>8s}  " + "-" * 40)

    for rank, (total, score, order) in enumerate(results[:10], 1):
        arrow_order = " -> ".join(order)
        marker = " <-- 최적" if rank == 1 else ""
        print(f"  {rank:4d}  {total:6d}  {score:8.2f}  {arrow_order}{marker}")

    # --- 하위 5 순열 ---
    print()
    print("[5] 하위 5 순열 (최악)")
    print("-" * 72)
    for rank, (total, score, order) in enumerate(results[-5:], len(results) - 4):
        arrow_order = " -> ".join(order)
        print(f"  {rank:4d}  {total:6d}  {score:8.2f}  {arrow_order}")

    # --- 최적 순서 상세 ---
    best_total, best_score, best_order = results[0]
    worst_total, _, worst_order = results[-1]

    print()
    print("[6] 최적 순서 상세 시뮬레이션")
    print(f"  순서: {' -> '.join(best_order)}")
    print("-" * 72)
    best_total_v, best_details = simulate_cascade(best_order, verbose=True)
    print(f"  총 EXACT: {best_total_v}")
    print()

    # --- 비교 분석 ---
    print("[7] 비교 분석")
    print("=" * 72)

    amplification = best_total / max(default_total, 1)
    range_ratio = best_total / max(worst_total, 1)

    print(f"  기본 순서 EXACT:  {default_total:6d}  ({' -> '.join(DEFAULT_ORDER)})")
    print(f"  최적 순서 EXACT:  {best_total:6d}  ({' -> '.join(best_order)})")
    print(f"  최악 순서 EXACT:  {worst_total:6d}  ({' -> '.join(worst_order)})")
    print()
    print(f"  최적/기본 증폭 계수:  {amplification:.4f}x")
    print(f"  최적/최악 범위 비율:  {range_ratio:.4f}x")
    print()

    # --- 공명 패턴 분석 ---
    print("[8] 최적 순서 공명 패턴")
    print("-" * 72)
    for i in range(len(best_order) - 1):
        d1, d2 = best_order[i], best_order[i + 1]
        f1, f2 = DOMAINS[d1], DOMAINS[d2]
        ratio = max(f1, f2) / min(f1, f2)
        bonus = resonance_bonus(f1, f2)
        ratio_str = f"{ratio:.2f}"
        n6_tag = " (n6 상수)" if int(round(ratio)) in N6_SET and abs(ratio - round(ratio)) < 1e-9 else ""
        res_tag = " [공명]" if bonus > 0 else ""
        print(f"  {d1:8s}(f={f1:3d}) -> {d2:8s}(f={f2:3d}) | "
              f"비율={ratio_str:>6s}{n6_tag}{res_tag} | 보너스=+{bonus:.0%}")
    print()

    # --- 통계 ---
    all_totals = [r[0] for r in results]
    avg_total = sum(all_totals) / len(all_totals)
    std_total = (sum((x - avg_total) ** 2 for x in all_totals) / len(all_totals)) ** 0.5

    print("[9] 720 순열 통계")
    print("-" * 48)
    print(f"  평균 EXACT: {avg_total:.1f}")
    print(f"  표준편차:   {std_total:.1f}")
    print(f"  최소:       {min(all_totals)}")
    print(f"  최대:       {max(all_totals)}")
    print(f"  고유 EXACT 값 수: {len(set(all_totals))}")
    print()

    # --- 결론 ---
    print("[결론]")
    print("=" * 72)
    if amplification > 1.0:
        print(f"  파동 공명 기반 순서 최적화로 기본 대비 {amplification:.4f}x 증폭 달성.")
        print(f"  BT-1105의 1.21x 대비 {'초과' if amplification > 1.21 else '미달'} "
              f"({amplification/1.21:.2f}x 비율).")
    else:
        print(f"  기본 순서가 이미 최적이거나 근접 ({amplification:.4f}x).")

    print(f"  720 순열 중 최적-최악 격차: {range_ratio:.4f}x")
    print(f"  공명 패턴이 캐스케이드 증폭에 기여하는 정도: "
          f"{best_score:.2f} (공명 점수 합)")
    print()
    print("  [실험 완료]")
    print("=" * 72)


if __name__ == "__main__":
    main()
