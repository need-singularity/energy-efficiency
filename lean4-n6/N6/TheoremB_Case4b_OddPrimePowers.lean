-- N6.TheoremB_Case4b_OddPrimePowers : Theorem B case 4b(ii)
-- v4 M3_v4 case 4b(ii) (2026-04-16 loop 28)
--
-- 목표: p, q 모두 odd prime ≥ 3 distinct, a ≥ 1, b ≥ 1
--       → σ(p^a·q^b)·φ(p^a·q^b) ≠ (p^a·q^b)·τ(p^a·q^b)
--
-- 이 정리는 case 2b (a=b=1) 를 특수 case 로 포함한다 — odd·odd distinct prime powers 일반형.
--
-- 전략:
--   σ(p^a·q^b) = σ(p^a)·σ(q^b), φ(p^a·q^b) = φ(p^a)·φ(q^b), τ = (a+1)(b+1)  (multiplicative)
--   σ(p^a)·φ(p^a) = p^(a-1)·(p^(a+1) - 1)
--   등식 ⟺ (p^(a+1) - 1)(q^(b+1) - 1) = p·q·(a+1)(b+1)   [cancel p^(a-1)·q^(b-1)]
--   핵심: p^(a+1) - 1 > p(a+1) for p ≥ 3 odd prime, a ≥ 1  (pow_strict_gt_odd)
--         q^(b+1) - 1 > q(b+1) for q ≥ 3 odd prime, b ≥ 1
--   곱하면 STRICT 부등식, 등식 모순

import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.NumberTheory.Divisors
import Mathlib.Data.Nat.Totient
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum.Prime
import N6.TheoremB_PrimeCase
import N6.TheoremB_Case3_PrimePow

namespace N6Mathlib

open Nat ArithmeticFunction
open scoped ArithmeticFunction.sigma

/-- p^(a+1) > p(a+1) + 1  for p ≥ 3 odd prime, a ≥ 1 — case 3 확장 -/
theorem pow_strict_gt_odd {p a : ℕ} (hp : p ≥ 3) (ha : a ≥ 1) :
    p ^ (a + 1) > p * (a + 1) + 1 := by
  rcases Nat.lt_or_ge a 2 with hlt | hge
  · -- a = 1
    have ha1 : a = 1 := by omega
    subst ha1
    -- Goal: p^2 > p·2 + 1 = 2p + 1
    have hpp : p * p ≥ 9 := by nlinarith
    have hpow : p ^ (1 + 1) = p * p := by ring
    rw [hpow]
    nlinarith
  · -- a ≥ 2: 그대로 case 3 prime_pow_strict_gt
    exact prime_pow_strict_gt (by omega : p ≥ 2) hge

/-- Coprime p^a and q^b for distinct primes p, q -/
theorem coprime_pow_distinct_primes {p q : ℕ} (hp : p.Prime) (hq : q.Prime)
    (hpq : p ≠ q) (a b : ℕ) : Nat.Coprime (p ^ a) (q ^ b) := by
  have h : Nat.Coprime p q := (Nat.coprime_primes hp hq).mpr hpq
  exact (h.pow_left a).pow_right b

/-- σ₁(p^a · q^b) = σ₁(p^a) · σ₁(q^b) for distinct primes -/
theorem sigma_one_pa_qb {p q : ℕ} (hp : p.Prime) (hq : q.Prime) (hpq : p ≠ q) (a b : ℕ) :
    σ 1 (p ^ a * q ^ b) = σ 1 (p ^ a) * σ 1 (q ^ b) :=
  (isMultiplicative_sigma (k := 1)).right (coprime_pow_distinct_primes hp hq hpq a b)

/-- φ(p^a · q^b) = φ(p^a) · φ(q^b) -/
theorem totient_pa_qb {p q : ℕ} (hp : p.Prime) (hq : q.Prime) (hpq : p ≠ q) (a b : ℕ) :
    Nat.totient (p ^ a * q ^ b) = Nat.totient (p ^ a) * Nat.totient (q ^ b) :=
  Nat.totient_mul (coprime_pow_distinct_primes hp hq hpq a b)

/-- τ(p^a · q^b) = (a+1)·(b+1) for distinct primes -/
theorem tau_pa_qb {p q : ℕ} (hp : p.Prime) (hq : q.Prime) (hpq : p ≠ q) (a b : ℕ) :
    (Nat.divisors (p ^ a * q ^ b)).card = (a + 1) * (b + 1) := by
  have hcop : Nat.Coprime (p ^ a) (q ^ b) := coprime_pow_distinct_primes hp hq hpq a b
  have hσ0 : σ 0 (p ^ a * q ^ b) = σ 0 (p ^ a) * σ 0 (q ^ b) :=
    (isMultiplicative_sigma (k := 0)).right hcop
  have h_left : σ 0 (p ^ a * q ^ b) = (Nat.divisors (p ^ a * q ^ b)).card := by
    simp [sigma_zero_apply]
  rw [← h_left, hσ0, sigma_zero_apply_prime_pow hp, sigma_zero_apply_prime_pow hq]

/-- Theorem B case 4b(ii): p, q odd prime ≥ 3 distinct, a, b ≥ 1 → σφ ≠ nτ (통합: 2b+4b(ii)) -/
theorem theorem_B_odd_prime_powers {p q a b : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hpq : p ≠ q)
    (hp3 : p ≥ 3) (hq3 : q ≥ 3)
    (ha : a ≥ 1) (hb : b ≥ 1) :
    σ 1 (p ^ a * q ^ b) * Nat.totient (p ^ a * q ^ b) ≠
      (p ^ a * q ^ b) * (Nat.divisors (p ^ a * q ^ b)).card := by
  rw [sigma_one_pa_qb hp hq hpq, totient_pa_qb hp hq hpq, tau_pa_qb hp hq hpq]
  rw [sigma_one_prime_pow_sum hp, sigma_one_prime_pow_sum hq]
  rw [Nat.totient_prime_pow hp (by omega : a > 0),
      Nat.totient_prime_pow hq (by omega : b > 0)]
  intro h
  -- h: (Σ p^i)·(Σ q^j)·(p^(a-1)·(p-1)·(q^(b-1)·(q-1))) = p^a·q^b·((a+1)(b+1))
  -- Reorganize: p^(a-1)·q^(b-1) · ((p-1)·Σ p^i) · ((q-1)·Σ q^j) = ...
  -- LHS 재정렬
  have reorg_lhs :
      ((∑ i ∈ Finset.range (a + 1), p ^ i) * ∑ j ∈ Finset.range (b + 1), q ^ j) *
        (p ^ (a - 1) * (p - 1) * (q ^ (b - 1) * (q - 1)))
      = (p ^ (a - 1) * q ^ (b - 1)) *
        (((p - 1) * ∑ i ∈ Finset.range (a + 1), p ^ i) *
         ((q - 1) * ∑ j ∈ Finset.range (b + 1), q ^ j)) := by
    ring
  rw [reorg_lhs,
      geom_sum_identity (by omega : p ≥ 2),
      geom_sum_identity (by omega : q ≥ 2)] at h
  -- h: p^(a-1)·q^(b-1) · ((p^(a+1)-1)(q^(b+1)-1)) = p^a·q^b·((a+1)(b+1))
  -- RHS 변환
  have h_pa : p ^ a = p * p ^ (a - 1) := by
    have : a = (a - 1) + 1 := by omega
    conv_lhs => rw [this]; ring
  have h_qb : q ^ b = q * q ^ (b - 1) := by
    have : b = (b - 1) + 1 := by omega
    conv_lhs => rw [this]; ring
  have h_rhs :
      p ^ a * q ^ b * ((a + 1) * (b + 1))
      = (p ^ (a - 1) * q ^ (b - 1)) * (p * q * ((a + 1) * (b + 1))) := by
    rw [h_pa, h_qb]; ring
  rw [h_rhs] at h
  -- h: p^(a-1)·q^(b-1) · ((p^(a+1)-1)(q^(b+1)-1)) = p^(a-1)·q^(b-1) · (pq(a+1)(b+1))
  -- cancel p^(a-1)·q^(b-1) > 0
  have h_pow_pos : p ^ (a - 1) * q ^ (b - 1) > 0 :=
    Nat.mul_pos (Nat.pow_pos (by omega : p > 0)) (Nat.pow_pos (by omega : q > 0))
  have h_cancel :
      (p ^ (a + 1) - 1) * (q ^ (b + 1) - 1) = p * q * ((a + 1) * (b + 1)) :=
    Nat.eq_of_mul_eq_mul_left h_pow_pos h
  -- Key inequalities: p^(a+1) > p(a+1) + 1, q^(b+1) > q(b+1) + 1
  have h_pstrict : p ^ (a + 1) > p * (a + 1) + 1 := pow_strict_gt_odd hp3 ha
  have h_qstrict : q ^ (b + 1) > q * (b + 1) + 1 := pow_strict_gt_odd hq3 hb
  -- (p^(a+1) - 1) > p(a+1), (q^(b+1) - 1) > q(b+1)
  have h_psub : p ^ (a + 1) - 1 > p * (a + 1) := by omega
  have h_qsub : q ^ (b + 1) - 1 > q * (b + 1) := by omega
  have h_ppos : p * (a + 1) ≥ 1 := by
    have : p ≥ 1 := by omega
    have : (a + 1) ≥ 1 := by omega
    nlinarith
  have h_qpos : q * (b + 1) ≥ 1 := by
    have : q ≥ 1 := by omega
    have : (b + 1) ≥ 1 := by omega
    nlinarith
  -- Product: (p^(a+1)-1)(q^(b+1)-1) > p(a+1)·q(b+1) = pq(a+1)(b+1)
  have h_prod_gt :
      (p ^ (a + 1) - 1) * (q ^ (b + 1) - 1) > p * (a + 1) * (q * (b + 1)) := by
    -- A > A', B > B', A ≥ 1, B ≥ 1 → AB > A'B'
    -- Here A = p^(a+1)-1, A' = p(a+1), B = q^(b+1)-1, B' = q(b+1)
    have hA_pos : p ^ (a + 1) - 1 ≥ 1 := by omega
    have hB_pos : q ^ (b + 1) - 1 ≥ 1 := by omega
    calc (p ^ (a + 1) - 1) * (q ^ (b + 1) - 1)
        > p * (a + 1) * (q ^ (b + 1) - 1) :=
          (Nat.mul_lt_mul_right (by omega : 0 < q ^ (b + 1) - 1)).mpr h_psub
      _ ≥ p * (a + 1) * (q * (b + 1)) :=
          Nat.mul_le_mul_left _ (by omega : q * (b + 1) ≤ q ^ (b + 1) - 1)
  have h_eq_reform : p * q * ((a + 1) * (b + 1)) = p * (a + 1) * (q * (b + 1)) := by ring
  rw [h_eq_reform] at h_cancel
  omega

/-- 확인 예시 -/
-- n = 15 = 3·5 (case 2b): σφ=8·4·6·4=...
-- n = 45 = 3²·5 (case 4b(ii), a=2, b=1):
example : 3 ^ (2 + 1) > 3 * (2 + 1) + 1 := by decide
example : 5 ^ (1 + 1) > 5 * (1 + 1) + 1 := by decide

end N6Mathlib
