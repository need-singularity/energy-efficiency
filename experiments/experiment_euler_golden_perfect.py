#!/usr/bin/env python3
"""
실험: Euler-Golden-Perfect Trinity
===================================
BT-1113 배경: gamma + 1/(2*12) ≈ 1/phi (오차 0.04%), 12 = sigma(6)
질문: gamma + 1/(2*sigma(n)) ≈ 1/phi 를 만족하는 완전수가 n=6뿐인가?

알고리즘:
  1) 완전수 목록에서 sigma(n)=2n 이용, gamma+1/(4n) 계산
  2) m=1..1000 전수 스캔으로 최적 m 탐색
  3) 베르누이 보정으로 고차항 효과 분석
  4) 잔차 ≈ 1/tau(6) 관계 검증
"""

import math
from fractions import Fraction

# ── 상수 ──
GAMMA = 0.5772156649015328606065120900824024310421  # 오일러-마스케로니 상수
PHI = (1 + math.sqrt(5)) / 2                        # 황금비
INV_PHI = 1.0 / PHI                                  # 1/phi ≈ 0.6180339887...

print("=" * 72)
print("  실험: 오일러-황금비-완전수 삼위일체 (Euler-Golden-Perfect Trinity)")
print("=" * 72)
print()
print(f"  오일러-마스케로니 상수 gamma = {GAMMA:.16f}")
print(f"  황금비 phi                   = {PHI:.16f}")
print(f"  1/phi                        = {INV_PHI:.16f}")
print()

# ═══════════════════════════════════════════════════════════════════════
# 1단계: 완전수에 대해 gamma + 1/(4n) vs 1/phi
# ═══════════════════════════════════════════════════════════════════════
print("─" * 72)
print("  [1단계] 완전수별 gamma + 1/(4n) vs 1/phi")
print("─" * 72)

perfect_numbers = [6, 28, 496, 8128, 33550336]

print(f"  {'완전수 n':>12s}  {'sigma(n)=2n':>12s}  {'gamma+1/(4n)':>18s}  "
      f"{'|오차|':>14s}  {'오차(%)':>10s}")
print(f"  {'─'*12}  {'─'*12}  {'─'*18}  {'─'*14}  {'─'*10}")

for n in perfect_numbers:
    sigma_n = 2 * n  # 완전수 성질
    val = GAMMA + 1.0 / (4.0 * n)
    err = abs(val - INV_PHI)
    pct = err / INV_PHI * 100
    print(f"  {n:>12d}  {sigma_n:>12d}  {val:>18.16f}  {err:>14.2e}  {pct:>10.6f}")

print()
print(f"  >>> n=6 일 때 gamma + 1/24 = {GAMMA + 1/24:.16f}")
print(f"  >>> 1/phi                  = {INV_PHI:.16f}")
print(f"  >>> 절대오차               = {abs(GAMMA + 1/24 - INV_PHI):.2e}")
print(f"  >>> 상대오차               = {abs(GAMMA + 1/24 - INV_PHI)/INV_PHI*100:.4f}%")
print()

# ═══════════════════════════════════════════════════════════════════════
# 2단계: sigma(m), m=1..1000 전수 스캔
# ═══════════════════════════════════════════════════════════════════════
print("─" * 72)
print("  [2단계] m=1..1000 전수 스캔 — gamma + 1/(2*sigma(m)) ≈ 1/phi 최적값")
print("─" * 72)


def sigma(m):
    """약수의 합 sigma(m)"""
    s = 0
    for d in range(1, int(math.isqrt(m)) + 1):
        if m % d == 0:
            s += d
            if d != m // d:
                s += m // d
    return s


results = []
for m in range(1, 1001):
    s = sigma(m)
    val = GAMMA + 1.0 / (2.0 * s)
    err = abs(val - INV_PHI)
    results.append((m, s, val, err))

# 오차 기준 상위 10개
results.sort(key=lambda x: x[3])
top10 = results[:10]

print(f"  {'순위':>4s}  {'m':>6s}  {'sigma(m)':>10s}  {'gamma+1/(2*sigma)':>20s}  "
      f"{'|오차|':>14s}  {'완전수?':>7s}")
print(f"  {'─'*4}  {'─'*6}  {'─'*10}  {'─'*20}  {'─'*14}  {'─'*7}")

for rank, (m, s, val, err) in enumerate(top10, 1):
    is_perfect = "예" if s == 2 * m else "아니오"
    print(f"  {rank:>4d}  {m:>6d}  {s:>10d}  {val:>20.16f}  {err:>14.2e}  {is_perfect:>7s}")

# 완전수가 1위인지 확인
best_m, best_s, best_val, best_err = results[0]
print()
if best_s == 2 * best_m:
    print(f"  >>> 최적 m = {best_m} (완전수) — sigma({best_m}) = {best_s}")
else:
    print(f"  >>> 최적 m = {best_m} (비완전수) — sigma({best_m}) = {best_s}")
print(f"  >>> 최소 오차 = {best_err:.2e}")
print()

# m=6이 몇 위인지 찾기
rank_of_6 = next(i+1 for i, (m,_,_,_) in enumerate(results) if m == 6)
err_of_6 = next(err for m,_,_,err in results if m == 6)
print(f"  >>> m=6 순위: {rank_of_6}위 (오차 {err_of_6:.2e})")
print()

# ═══════════════════════════════════════════════════════════════════════
# 3단계: 비완전수 포함 — sigma(m)=12 인 m 전수 조사
# ═══════════════════════════════════════════════════════════════════════
print("─" * 72)
print("  [3단계] sigma(m)=12 인 모든 m (1~1000)")
print("─" * 72)

sigma12_list = [m for m in range(1, 1001) if sigma(m) == 12]
print(f"  sigma(m) = 12 인 m: {sigma12_list}")
for m in sigma12_list:
    is_p = "(완전수)" if sigma(m) == 2*m else "(비완전수)"
    print(f"    m={m}: sigma({m})={sigma(m)} {is_p}")
print()

# ═══════════════════════════════════════════════════════════════════════
# 4단계: 일반화 — sigma(m)=12가 핵심인지, m=6이 핵심인지 분리
# ═══════════════════════════════════════════════════════════════════════
print("─" * 72)
print("  [4단계] 핵심 분석: sigma(m)=12 vs m=6 분리")
print("─" * 72)

# gamma + 1/(2*12) 에서 12가 핵심
target_sigma = 2.0 * (INV_PHI - GAMMA)  # sigma 역산
target_sigma_inv = 1.0 / target_sigma
print(f"  gamma + 1/(2*S) = 1/phi  →  S = 1/(2*(1/phi - gamma))")
print(f"  이론적 최적 S* = {target_sigma_inv:.10f}")
print(f"  S* = {target_sigma_inv:.4f}  ≈  12 + {target_sigma_inv - 12:.4f}")
print()

# sigma(m)이 12에 가장 가까운 m 목록
sigma_near_12 = [(m, sigma(m), abs(sigma(m) - target_sigma_inv))
                 for m in range(1, 1001)]
sigma_near_12.sort(key=lambda x: x[2])
print(f"  sigma(m) ≈ S*={target_sigma_inv:.4f} 에 가장 가까운 상위 5개:")
for rank, (m, s, d) in enumerate(sigma_near_12[:5], 1):
    is_p = "(완전수)" if s == 2*m else ""
    print(f"    {rank}위: m={m}, sigma={s}, |sigma-S*|={d:.4f} {is_p}")
print()

# ═══════════════════════════════════════════════════════════════════════
# 5단계: 베르누이 보정 — H(n) = ln(n) + gamma + 1/(2n) - B₂/(2·n²) + ...
# ═══════════════════════════════════════════════════════════════════════
print("─" * 72)
print("  [5단계] 베르누이 보정 — 고차항 포함 시 n* 변화")
print("─" * 72)

# 베르누이 수 (짝수 인덱스)
bernoulli = {
    2:  Fraction(1, 6),
    4:  Fraction(-1, 30),
    6:  Fraction(1, 42),
    8:  Fraction(-1, 30),
    10: Fraction(5, 66),
    12: Fraction(-691, 2730),
}

print("  H(n) ≈ ln(n) + gamma + 1/(2n) - sum_{k=1}^{K} B_{2k}/(2k·n^{2k})")
print()
print("  n=12에서 보정항 크기:")

n_test = 12
total_correction = 0.0
for k in range(1, 7):
    b2k = float(bernoulli[2*k])
    term = -b2k / (2*k * n_test**(2*k))
    total_correction += term
    print(f"    k={k}: B_{2*k}={str(bernoulli[2*k]):>10s}  항 = {term:>+.2e}  누적 = {total_correction:>+.2e}")

print()
print(f"  1/(2*12) = {1/24:.16f}")
print(f"  보정 총합 = {total_correction:.16f}")
print(f"  1/24 + 보정 = {1/24 + total_correction:.16f}")
print()

# 보정 포함 시 최적 n* 탐색 (연속 변수)
# gamma + 1/(2n) - B2/(2*n^2) + B4/(4*n^4) - ... = 1/phi - ln(n)... 은 복잡
# 대신 이산 검색: n=1..100에서 |H(n) - ln(n) - 1/phi| 최소화
print("  n=1..100 이산 검색: |[H(n) - ln(n)] - 1/phi| 최소")
print()


def harmonic(n):
    """조화수 H(n) 정확 계산"""
    return sum(1.0/k for k in range(1, n+1))


h_results = []
for n in range(1, 101):
    h_n = harmonic(n)
    diff = h_n - math.log(n)  # H(n) - ln(n) ≈ gamma + 1/(2n) - ...
    err = abs(diff - INV_PHI)
    h_results.append((n, h_n, diff, err))

h_results.sort(key=lambda x: x[3])
print(f"  {'순위':>4s}  {'n':>4s}  {'H(n)-ln(n)':>16s}  {'|오차|':>14s}")
print(f"  {'─'*4}  {'─'*4}  {'─'*16}  {'─'*14}")
for rank, (n, h, d, e) in enumerate(h_results[:8], 1):
    mark = " ◀ n=6 완전수" if n == 6 else ""
    print(f"  {rank:>4d}  {n:>4d}  {d:>16.12f}  {e:>14.2e}{mark}")

print()
best_h_n = h_results[0][0]
print(f"  >>> H(n)-ln(n) ≈ 1/phi 최적: n = {best_h_n}")
rank6_h = next(i+1 for i,(n,_,_,_) in enumerate(h_results) if n == 6)
print(f"  >>> n=6 순위: {rank6_h}위")
print()

# ═══════════════════════════════════════════════════════════════════════
# 6단계: n* = 12 + 잔차, 잔차 ≈ 1/tau(6) 검증
# ═══════════════════════════════════════════════════════════════════════
print("─" * 72)
print("  [6단계] n* = S* 잔차 분석 — 1/tau(6) = 0.25 관계")
print("─" * 72)

# tau(6) = 약수 개수 = 4
tau_6 = 4
inv_tau_6 = 1.0 / tau_6

residual = target_sigma_inv - 12.0

print(f"  S* (이론적 최적 sigma) = {target_sigma_inv:.16f}")
print(f"  S* - 12                = {residual:.16f}")
print(f"  1/tau(6) = 1/4         = {inv_tau_6:.16f}")
print(f"  |잔차 - 1/tau(6)|      = {abs(residual - inv_tau_6):.2e}")
print(f"  잔차/inv_tau(6)         = {residual/inv_tau_6:.6f}")
print()

# 좀 더 정밀하게
delta = residual - inv_tau_6
print(f"  잔차 = 1/tau(6) + {delta:.10f}")
print(f"  delta/gamma            = {delta/GAMMA:.10f}")
print(f"  delta * phi            = {delta * PHI:.10f}")
print(f"  delta * 24             = {delta * 24:.10f}")
print()

# ═══════════════════════════════════════════════════════════════════════
# 7단계: 최종 판정
# ═══════════════════════════════════════════════════════════════════════
print("=" * 72)
print("  [최종 판정]")
print("=" * 72)
print()

# 판정 1: 완전수 중 n=6 유일성
print("  판정 1: 완전수 중 gamma+1/(4n) ≈ 1/phi 최적은 n=6인가?")
pn_errors = [(n, abs(GAMMA + 1/(4*n) - INV_PHI)) for n in perfect_numbers]
pn_errors.sort(key=lambda x: x[1])
best_pn = pn_errors[0]
print(f"    → 예. n={best_pn[0]} 이 최적 (오차 {best_pn[1]:.2e})")
ratio_2nd = pn_errors[1][1] / pn_errors[0][1]
print(f"    → 2위 n={pn_errors[1][0]} 대비 오차 {ratio_2nd:.1f}배 큼")
print()

# 판정 2: 전체 m=1..1000 중 m=6 특수성
print("  판정 2: m=1..1000 중 sigma(m) 기반 최적은?")
print(f"    → 최적 m={top10[0][0]} (sigma={top10[0][1]})")
if top10[0][0] == 6:
    print(f"    → m=6(완전수)이 전체 1000개 자연수 중 1위!")
else:
    # sigma=12인 다른 수가 1위일 수 있음
    if top10[0][1] == 12:
        print(f"    → sigma({top10[0][0]})=12 = sigma(6). 핵심은 sigma=12.")
        six_in_top = [r for r in top10 if r[0] == 6]
        if six_in_top:
            print(f"    → m=6도 동일 sigma=12으로 공동 1위")
    print(f"    → m=6 순위: {rank_of_6}위")
print()

# 판정 3: 잔차 관계
print("  판정 3: S* - 12 ≈ 1/tau(6)?")
if abs(residual - inv_tau_6) < 0.01:
    print(f"    → 예. |S*-12 - 1/4| = {abs(residual-inv_tau_6):.6f} < 0.01")
    print(f"    → S* ≈ 12 + 1/tau(6) = sigma(6) + 1/tau(6)")
else:
    print(f"    → 아니오. |S*-12 - 1/4| = {abs(residual-inv_tau_6):.6f}")
print()

# 종합
print("  종합:")
print(f"    gamma + 1/(2·sigma(6)) = gamma + 1/24 ≈ 1/phi")
print(f"    오차 = {abs(GAMMA + 1/24 - INV_PHI)/INV_PHI*100:.4f}%")
print(f"    완전수 중 유일한 최적: n = 6")
print(f"    자연수 1~1000 중 sigma 기반 순위: m=6은 {rank_of_6}위")
print()
print("=" * 72)
print("  실험 완료")
print("=" * 72)
