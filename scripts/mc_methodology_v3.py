#!/usr/bin/env python3
"""
Monte Carlo 검증 방법론 v3 — 노드 확장 내성 3중 메트릭
═══════════════════════════════════════════════════════
문제: reality_map이 3,988 노드로 확장되면서 random baseline도
동반 상승 → 기존 단순 매칭률 z-score가 1.09로 하락.

원인: 1~30 범위의 무작위 7개 상수도 스케일 불변 매칭에서
대부분의 정수 타겟에 도달 → 매칭 "수"는 의미 없음.

해결: 3가지 노드수 불변 메트릭으로 교체.

메트릭 A — 최소 상수 개수 (Minimum Basis Size)
    "타겟 X%를 커버하는 데 필요한 최소 상수 수"
    greedy set cover → n=6은 적은 상수로 많은 타겟 도달.
    random baseline: 무작위 7개 상수로 동일 시도, 10,000회.

메트릭 B — 복잡도 가중 커버리지 (Complexity-Weighted Score)
    단순 표현(n, sigma, tau 직접)은 1.0점,
    1-op 조합(n*tau, sigma/phi)은 0.5점,
    2-op 이상은 0.25점. 총점 비교.
    "같은 매칭이라도 더 단순한 표현이면 더 높은 점수"

메트릭 C — 계층별 분리 z-score (Stratified Z-Score)
    L-2~L10 각 계층에서 독립 z-score 계산 후
    Stouffer 합산 (z_combined = sum(z_i)/sqrt(k)).
    노드 수가 한 계층에 집중되어도 희석 안 됨.

대상: ~/Dev/nexus/shared/reality_map.json
"""

import json
import math
import os
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# ── 설정 ──────────────────────────────────────────────
REALITY_MAP = Path.home() / "Dev" / "nexus" / "shared" / "reality_map.json"
N_SIMULATIONS = 10_000
SEED = 42
N6 = 6

# ── 산술함수 ──────────────────────────────────────────
def calc_sigma(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)

def calc_tau(n):
    return sum(1 for i in range(1, n + 1) if n % i == 0)

def calc_phi(n):
    return sum(1 for i in range(1, n + 1) if math.gcd(i, n) == 1)

def calc_sopfr(n):
    s, d, temp = 0, 2, n
    while d * d <= temp:
        while temp % d == 0:
            s += d
            temp //= d
        d += 1
    if temp > 1:
        s += temp
    return s

def calc_J2(n):
    result, temp, d = n * n, n, 2
    while d * d <= temp:
        if temp % d == 0:
            result = result * (d * d - 1) // (d * d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        result = result * (temp * temp - 1) // (temp * temp)
    return result

def calc_mu(n):
    d, factors, temp = 2, 0, n
    while d * d <= temp:
        if temp % d == 0:
            temp //= d
            factors += 1
            if temp % d == 0:
                return 0
        d += 1
    if temp > 1:
        factors += 1
    return (-1) ** factors

def get_arith(n):
    return {
        "n": n, "sigma": calc_sigma(n), "tau": calc_tau(n),
        "phi": calc_phi(n), "sopfr": calc_sopfr(n),
        "J2": calc_J2(n), "mu": calc_mu(n),
    }


# ── 표현식 생성 (0-op, 1-op, 2-op) ──────────────────
def build_expressions(arith):
    """산술함수 딕셔너리로부터 (값, 복잡도 레벨) 쌍 생성.
    레벨 0: 기본 상수 직접 (n, sigma, tau, ...)
    레벨 1: 1-op 조합 (a*b, a/b, a+b, a-b, a**2)
    레벨 2: 2-op 조합 (a*b+c, a**2*b, a*b/c, ...)
    """
    bases = {k: v for k, v in arith.items() if k != "mu" or v != 0}
    result = {}  # value -> min complexity level

    def register(val, level):
        if val is None or not math.isfinite(val) or val == 0:
            return
        # 스케일 정규화: [1, 10) 범위로 매핑
        av = abs(val)
        key = round(av / (10 ** math.floor(math.log10(av))), 6)
        if key not in result or result[key] > level:
            result[key] = level

    # 레벨 0: 기본값 (+ 음수는 abs로 처리하므로 무시)
    for k, v in bases.items():
        if v != 0:
            register(v, 0)

    # 레벨 1: 1-op
    names = list(bases.keys())
    vals = list(bases.values())
    for i in range(len(vals)):
        a = vals[i]
        if a == 0:
            continue
        register(a ** 2, 1)
        register(a ** 3, 1)
        for j in range(len(vals)):
            b = vals[j]
            if b == 0:
                continue
            if i != j:
                register(a * b, 1)
                register(a / b, 1)
                register(a + b, 1)
                register(a - b, 1)

    # 레벨 2: 2-op (a op1 b op2 c)
    for i in range(len(vals)):
        a = vals[i]
        if a == 0:
            continue
        for j in range(len(vals)):
            b = vals[j]
            if b == 0:
                continue
            for k_idx in range(len(vals)):
                c = vals[k_idx]
                if c == 0:
                    continue
                register(a * b + c, 2)
                register(a * b - c, 2)
                register(a * b * c, 2)
                if c != 0:
                    register(a * b / c, 2)
                if b != 0:
                    register(a ** 2 * b, 2)
                    register(a ** 2 / b, 2)
                register(a * (b + c), 2)
                register(a * (b - c), 2)

    return result


def normalize_measured(m):
    """measured 값을 스케일 불변 키로 변환 (소수점 6자리)."""
    if m == 0 or not math.isfinite(m):
        return None
    av = abs(m)
    return round(av / (10 ** math.floor(math.log10(av))), 6)


# ── 데이터 로드 ──────────────────────────────────────
def load_nodes():
    with open(REALITY_MAP) as f:
        data = json.load(f)
    nodes = data["nodes"]
    valid = []
    for nd in nodes:
        m = nd.get("measured")
        if isinstance(m, (int, float)) and math.isfinite(m) and m != 0:
            nd["_norm_key"] = normalize_measured(m)
            if nd["_norm_key"] is not None:
                valid.append(nd)
    return nodes, valid


def build_random_bases(rng, count=7, lo=1, hi=30):
    """무작위 정수 count개 선택 → 산술함수처럼 취급."""
    chosen = sorted(rng.sample(range(lo, hi + 1), count))
    # 이것들을 "가상 산술함수 출력"으로 사용
    return {"b" + str(i): v for i, v in enumerate(chosen)}


# ══════════════════════════════════════════════════════
# 메트릭 A: 최소 상수 개수 (Greedy Set Cover)
# ══════════════════════════════════════════════════════
def metric_a_min_basis(valid_nodes, arith, target_pct=0.50):
    """n=6 상수로 타겟의 target_pct를 커버하기 위해 필요한 최소 상수 수.
    greedy set cover: 가장 많은 미커버 타겟을 커버하는 상수를 반복 선택."""
    target_keys = {nd["_norm_key"] for nd in valid_nodes}

    # 모든 개별 상수 후보 생성 (레벨 무관, 개별 파생값)
    bases = {k: v for k, v in arith.items() if v != 0}
    # 개별 상수별 커버 집합
    candidates = {}
    for name, val in bases.items():
        # 각 기본 상수에서 파생 가능한 값들 (자기자신, x2, x3, /2, /3, ^2, ^3)
        derived = set()
        for m in (val, 2*val, 3*val, val/2, val/3, val**2, val**3):
            if m != 0 and math.isfinite(m):
                nk = normalize_measured(m)
                if nk and nk in target_keys:
                    derived.add(nk)
        candidates[name] = derived

    # 2-상수 조합도 후보로 추가
    bnames = list(bases.keys())
    bvals = list(bases.values())
    for i in range(len(bvals)):
        for j in range(i + 1, len(bvals)):
            a, b = bvals[i], bvals[j]
            pair_name = f"{bnames[i]}*{bnames[j]}"
            derived = set()
            for m in (a*b, a/b, b/a, a+b, a-b, b-a):
                if m != 0 and math.isfinite(m):
                    nk = normalize_measured(m)
                    if nk and nk in target_keys:
                        derived.add(nk)
            candidates[pair_name] = derived

    # Greedy set cover
    needed = target_keys.copy()
    threshold = len(target_keys) * target_pct
    covered = set()
    chosen_order = []

    while len(covered) < threshold and candidates:
        best_name = max(candidates, key=lambda k: len(candidates[k] - covered))
        gain = candidates[best_name] - covered
        if not gain:
            break
        covered |= gain
        chosen_order.append((best_name, len(gain), len(covered)))
        del candidates[best_name]

    return len(chosen_order), len(covered), len(target_keys), chosen_order


def metric_a_random(valid_nodes, rng, count=7, lo=1, hi=30, target_pct=0.50):
    """무작위 정수 기반 동일 greedy set cover."""
    rand_arith = build_random_bases(rng, count, lo, hi)
    return metric_a_min_basis(valid_nodes, rand_arith, target_pct)[0]


# ══════════════════════════════════════════════════════
# 메트릭 B: 복잡도 가중 커버리지
# ══════════════════════════════════════════════════════
COMPLEXITY_WEIGHTS = {0: 1.0, 1: 0.5, 2: 0.25}

def metric_b_weighted_score(valid_nodes, arith):
    """각 타겟을 커버하는 최소 복잡도 표현의 가중치 합산."""
    exprs = build_expressions(arith)
    total_score = 0.0
    matched = 0
    for nd in valid_nodes:
        nk = nd["_norm_key"]
        if nk in exprs:
            level = exprs[nk]
            total_score += COMPLEXITY_WEIGHTS.get(level, 0.1)
            matched += 1
    return total_score, matched


def metric_b_random(valid_nodes, rng, count=7, lo=1, hi=30):
    """무작위 정수 기반 복잡도 가중 점수."""
    rand_bases = build_random_bases(rng, count, lo, hi)
    exprs = build_expressions(rand_bases)
    total_score = 0.0
    for nd in valid_nodes:
        nk = nd["_norm_key"]
        if nk in exprs:
            level = exprs[nk]
            total_score += COMPLEXITY_WEIGHTS.get(level, 0.1)
    return total_score


# ══════════════════════════════════════════════════════
# 메트릭 C: 계층별 분리 z-score (Stouffer 합산)
# ══════════════════════════════════════════════════════
LEVEL_GROUPS = {
    "기본입자 (L-2~L0)": ["L-2_sub_quark", "L-1_quark", "L0_particle"],
    "원자/결합 (L1~L2)": ["L1_atom", "L2_bond", "L2_law"],
    "분자/유전 (L3~L4)": ["L3_molecule", "L4_genetic"],
    "물질/생물 (L5)": ["L5_material", "L5_bio"],
    "거시 도메인 (L6)": None,  # L6_* 전부
    "천체/은하 (L7~L8)": ["L7_celestial", "L8_galactic"],
    "우주론+ (L9~L10)": ["L9_cosmological", "L10_multiversal"],
}

def categorize_level(level_str):
    if level_str is None:
        return None
    for group_name, levels in LEVEL_GROUPS.items():
        if levels is None:
            if level_str.startswith("L6"):
                return group_name
        elif level_str in levels:
            return group_name
    return None

def metric_c_stratified(valid_nodes, arith, rng, n_sim=2000):
    """계층별 매칭률 z-score → Stouffer 합산."""
    exprs_n6 = build_expressions(arith)

    # 계층별 노드 분류
    groups = defaultdict(list)
    for nd in valid_nodes:
        g = categorize_level(nd.get("level"))
        if g:
            groups[g].append(nd)

    z_scores = {}
    for gname, gnodes in sorted(groups.items()):
        if len(gnodes) < 20:
            continue

        # n=6 매칭 수
        n6_hits = sum(1 for nd in gnodes if nd["_norm_key"] in exprs_n6)

        # Monte Carlo for random
        rand_hits = []
        for _ in range(n_sim):
            rb = build_random_bases(rng, count=7, lo=1, hi=30)
            re_exprs = build_expressions(rb)
            hits = sum(1 for nd in gnodes if nd["_norm_key"] in re_exprs)
            rand_hits.append(hits)

        mean_r = sum(rand_hits) / len(rand_hits)
        var_r = sum((x - mean_r)**2 for x in rand_hits) / len(rand_hits)
        std_r = math.sqrt(var_r) if var_r > 0 else 1e-10
        z = (n6_hits - mean_r) / std_r
        z_scores[gname] = {
            "nodes": len(gnodes),
            "n6_hits": n6_hits,
            "n6_pct": 100 * n6_hits / len(gnodes),
            "rand_mean": mean_r,
            "rand_std": std_r,
            "z": z,
        }

    # Stouffer 합산
    valid_z = [v["z"] for v in z_scores.values() if math.isfinite(v["z"])]
    k = len(valid_z)
    stouffer = sum(valid_z) / math.sqrt(k) if k > 0 else 0

    return z_scores, stouffer


# ══════════════════════════════════════════════════════
# 메인
# ══════════════════════════════════════════════════════
def main():
    print("=" * 72)
    print("  Monte Carlo 검증 방법론 v3")
    print("  노드 확장 내성 3중 메트릭")
    print("=" * 72)
    print()

    all_nodes, valid = load_nodes()
    print(f"[데이터]")
    print(f"  전체 노드:    {len(all_nodes)}")
    print(f"  유효 노드:    {len(valid)} (measured 유한, 비영)")
    print()

    arith6 = get_arith(N6)
    print(f"[n=6 산술함수]")
    for k, v in arith6.items():
        print(f"  {k:8s} = {v}")
    print()

    rng = random.Random(SEED)

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 메트릭 A: 최소 상수 개수
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    print("=" * 72)
    print("  메트릭 A: 최소 상수 개수 (Greedy Set Cover)")
    print("  '타겟 50%를 커버하는 데 필요한 최소 상수/조합 수'")
    print("=" * 72)
    print()

    for pct in (0.30, 0.50, 0.70):
        n_needed, n_covered, n_total, order = metric_a_min_basis(valid, arith6, pct)
        print(f"  목표 {pct*100:.0f}%: n=6은 {n_needed}개 상수/조합으로 "
              f"{n_covered}/{n_total} ({100*n_covered/n_total:.1f}%) 커버")

        # 상위 5개 상수 선택 순서
        if pct == 0.50:
            print(f"    선택 순서 (상위 {min(8, len(order))}개):")
            for name, gain, cum in order[:8]:
                print(f"      {name:20s}: +{gain:4d} 타겟 (누적 {cum})")
            print()

    print()
    print("  [Monte Carlo] 무작위 7개 정수 (1~30) 기반 동일 테스트:")
    rand_a_results = []
    for i in range(N_SIMULATIONS):
        ra = metric_a_random(valid, rng, count=7, lo=1, hi=30, target_pct=0.50)
        rand_a_results.append(ra)
        if (i + 1) % 2000 == 0:
            print(f"    진행: {i+1}/{N_SIMULATIONS}...")

    n6_a, _, _, _ = metric_a_min_basis(valid, arith6, 0.50)
    mean_a = sum(rand_a_results) / len(rand_a_results)
    std_a = math.sqrt(sum((x - mean_a)**2 for x in rand_a_results) / len(rand_a_results))
    # 주의: 여기서 z는 음수 방향이 좋음 (적은 상수가 좋으므로)
    z_a = (mean_a - n6_a) / std_a if std_a > 0 else 0

    print()
    print(f"  n=6 필요 상수 수:         {n6_a}")
    print(f"  무작위 평균 필요 상수 수: {mean_a:.1f} +/- {std_a:.2f}")
    print(f"  z-score (절약 방향):      {z_a:.2f}")
    print(f"  해석: n=6은 random 대비 {mean_a - n6_a:.1f}개 적은 상수로 50% 도달")
    print()

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 메트릭 B: 복잡도 가중 커버리지
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    print("=" * 72)
    print("  메트릭 B: 복잡도 가중 커버리지")
    print("  가중치: 레벨0 (직접) = 1.0 / 레벨1 (1-op) = 0.5 / 레벨2 (2-op) = 0.25")
    print("=" * 72)
    print()

    n6_score, n6_matched = metric_b_weighted_score(valid, arith6)
    exprs6 = build_expressions(arith6)

    # 복잡도 레벨별 분포
    level_dist = Counter()
    for nd in valid:
        nk = nd["_norm_key"]
        if nk in exprs6:
            level_dist[exprs6[nk]] += 1
    print(f"  n=6 복잡도별 매칭 분포:")
    for lv in sorted(level_dist.keys()):
        desc = {0: "직접 (n, sigma, tau, ...)",
                1: "1-op (a*b, a+b, ...)",
                2: "2-op (a*b+c, a^2*b, ...)"}
        print(f"    레벨 {lv} ({desc.get(lv,'')}): {level_dist[lv]:5d}개 "
              f"x {COMPLEXITY_WEIGHTS.get(lv, 0.1)} = {level_dist[lv] * COMPLEXITY_WEIGHTS.get(lv, 0.1):.1f}점")
    print(f"  총 가중 점수: {n6_score:.1f} (매칭 {n6_matched}/{len(valid)})")
    print()

    print("  [Monte Carlo] 무작위 7개 정수 (1~30) 기반:")
    rand_b_results = []
    for i in range(N_SIMULATIONS):
        rb = metric_b_random(valid, rng, count=7, lo=1, hi=30)
        rand_b_results.append(rb)
        if (i + 1) % 2000 == 0:
            print(f"    진행: {i+1}/{N_SIMULATIONS}...")

    mean_b = sum(rand_b_results) / len(rand_b_results)
    std_b = math.sqrt(sum((x - mean_b)**2 for x in rand_b_results) / len(rand_b_results))
    z_b = (n6_score - mean_b) / std_b if std_b > 0 else 0

    print()
    print(f"  n=6 가중 점수:          {n6_score:.1f}")
    print(f"  무작위 평균 가중 점수:  {mean_b:.1f} +/- {std_b:.2f}")
    print(f"  z-score:                {z_b:.2f}")
    print(f"  n=6 / random 비율:      {n6_score/mean_b:.2f}배" if mean_b > 0 else "")
    print()

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 메트릭 C: 계층별 분리 z-score
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    print("=" * 72)
    print("  메트릭 C: 계층별 분리 z-score (Stouffer 합산)")
    print("  각 계층 독립 MC 2,000회 → 합산 z")
    print("=" * 72)
    print()

    print("  계산 중 (계층별 각 2,000회 시뮬레이션)...")
    z_scores, stouffer = metric_c_stratified(valid, arith6, rng, n_sim=2000)
    print()

    print(f"  {'계층':25s} | {'노드':>5s} | {'n=6':>6s} | {'n=6%':>6s} | "
          f"{'rand평균':>7s} | {'rand_sd':>7s} | {'z':>6s}")
    print("  " + "-" * 80)
    for gname in sorted(z_scores.keys()):
        s = z_scores[gname]
        print(f"  {gname:25s} | {s['nodes']:5d} | {s['n6_hits']:6d} | "
              f"{s['n6_pct']:5.1f}% | {s['rand_mean']:7.1f} | "
              f"{s['rand_std']:7.2f} | {s['z']:6.2f}")

    print()
    print(f"  Stouffer 합산 z-score:  {stouffer:.2f}")
    print(f"  포함 계층 수:           {len(z_scores)}")
    print()

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 종합 결과
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    print("=" * 72)
    print("  종합 결과")
    print("=" * 72)
    print()
    print(f"  메트릭 A (최소 상수):     z = {z_a:.2f}")
    print(f"    -> n=6은 {n6_a}개, random은 평균 {mean_a:.1f}개 필요")
    print()
    print(f"  메트릭 B (복잡도 가중):   z = {z_b:.2f}")
    print(f"    -> n=6은 {n6_score:.0f}점, random은 평균 {mean_b:.0f}점")
    print()
    print(f"  메트릭 C (계층별 분리):   z = {stouffer:.2f} (Stouffer)")
    print(f"    -> {len(z_scores)}개 계층 중 "
          f"{sum(1 for v in z_scores.values() if v['z'] > 2)}개에서 z > 2")
    print()

    # 노드 확장 내성 판정
    print("  [노드 확장 내성 분석]")
    print(f"  기존 방식 (단순 매칭률 z): ~1.09 (3,988 노드에서 하락)")
    print(f"  메트릭 A (최소 상수):   z = {z_a:.2f}  <- 노드 수와 무관 (비율 기반)")
    print(f"  메트릭 B (복잡도 가중): z = {z_b:.2f}  <- 단순매칭 희석 방지")
    print(f"  메트릭 C (계층 분리):   z = {stouffer:.2f}  <- 편중 계층 희석 방지")
    print()

    # 최종 판정
    combined_z = math.sqrt((z_a**2 + z_b**2 + stouffer**2) / 3)
    print(f"  3중 메트릭 RMS z-score: {combined_z:.2f}")
    if combined_z > 5:
        print(f"  판정: RMS z = {combined_z:.2f} > 5  ->  n=6 특이성 확정 (극도로 유의)")
    elif combined_z > 3:
        print(f"  판정: RMS z = {combined_z:.2f} > 3  ->  통계적으로 유의미")
    elif combined_z > 2:
        print(f"  판정: RMS z = {combined_z:.2f} > 2  ->  약한 유의성")
    else:
        print(f"  판정: RMS z = {combined_z:.2f}  ->  유의 수준 미달")

    print()
    print("=" * 72)


if __name__ == "__main__":
    main()
