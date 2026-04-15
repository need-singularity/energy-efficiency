-- N6.TheoremB_Case3_PrimePow : Theorem B case 3 (n = p^a, a ≥ 2)
-- v4 M3_v4 case 3 (2026-04-16 loop 25)
--
-- 목표: p prime, a ≥ 2 → σ(p^a)·φ(p^a) ≠ p^a·τ(p^a)
-- 전략:
--   σ(p^a) = Σ p^k (k=0..a) = (p^(a+1) - 1)/(p-1)
--   φ(p^a) = p^(a-1)·(p-1)
--   τ(p^a) = a + 1
--   σ·φ = p^(a-1)·(p^(a+1) - 1)
--   n·τ = p^a·(a+1)
--   등식 ⟺ p^(a+1) - 1 = p·(a+1) ⟺ p^(a+1) = p(a+1) + 1
--   증명: p^(a+1) > p(a+1) + 1 for p ≥ 2, a ≥ 2

import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.NumberTheory.Divisors
import Mathlib.Data.Nat.Totient
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum.Prime

namespace N6Mathlib

open Nat ArithmeticFunction
open scoped ArithmeticFunction.sigma

/-- 2^a ≥ a + 2 for a ≥ 2 — induction from base a=2 -/
theorem two_pow_ge_lin {a : ℕ} (ha : a ≥ 2) : 2 ^ a ≥ a + 2 := by
  induction a, ha using Nat.le_induction with
  | base => decide
  | succ n hn ih =>
    -- n ≥ 2, ih : 2^n ≥ n+2. Goal: 2^(n+1) ≥ (n+1)+2
    have expand : 2 ^ (n + 1) = 2 * 2 ^ n := by ring
    omega

/-- p^(a+1) ≥ p · (a + 2) for p ≥ 2, a ≥ 2 -/
theorem prime_pow_ge_linear {p a : ℕ} (hp : p ≥ 2) (ha : a ≥ 2) :
    p ^ (a + 1) ≥ p * (a + 2) := by
  have h2a : 2 ^ a ≥ a + 2 := two_pow_ge_lin ha
  have hpa : p ^ a ≥ 2 ^ a := Nat.pow_le_pow_left hp a
  have : p ^ a ≥ a + 2 := le_trans h2a hpa
  have : p ^ (a + 1) = p * p ^ a := by ring
  nlinarith

/-- Key: p^(a+1) > p·(a+1) + 1 for p ≥ 2, a ≥ 2 -/
theorem prime_pow_strict_gt {p a : ℕ} (hp : p ≥ 2) (ha : a ≥ 2) :
    p ^ (a + 1) > p * (a + 1) + 1 := by
  have h := prime_pow_ge_linear hp ha
  -- h : p ^ (a + 1) ≥ p * (a + 2)
  -- p * (a + 2) = p * (a + 1) + p
  -- p ≥ 2, so p * (a + 1) + p ≥ p * (a + 1) + 2 > p * (a + 1) + 1
  have expand : p * (a + 2) = p * (a + 1) + p := by ring
  omega

/-- τ(p^a) = a + 1 for prime p -/
theorem tau_prime_pow {p a : ℕ} (hp : p.Prime) : (Nat.divisors (p ^ a)).card = a + 1 := by
  have h : σ 0 (p ^ a) = a + 1 := sigma_zero_apply_prime_pow hp
  have : σ 0 (p ^ a) = (Nat.divisors (p ^ a)).card := by simp [sigma_zero_apply]
  omega

/-- σ(p^a) 의 sum form -/
theorem sigma_one_prime_pow_sum {p a : ℕ} (hp : p.Prime) :
    σ 1 (p ^ a) = ∑ k ∈ Finset.range (a + 1), p ^ k :=
  sigma_one_apply_prime_pow hp

/-- (p - 1) · Σ p^k (k=0..a) = p^(a+1) - 1  (geometric sum) -/
theorem geom_sum_identity {p a : ℕ} (hp : p ≥ 2) :
    (p - 1) * ∑ k ∈ Finset.range (a + 1), p ^ k = p ^ (a + 1) - 1 := by
  induction a with
  | zero =>
    -- (p-1) * Σ_{k∈range 1} p^k = (p-1) * p^0 = p - 1 = p^1 - 1
    simp
  | succ n ih =>
    -- Σ_{k∈range(n+2)} p^k = Σ_{k∈range(n+1)} p^k + p^(n+1)
    rw [Finset.sum_range_succ, Nat.mul_add, ih]
    -- Goal: (p^(n+1) - 1) + (p - 1) * p^(n+1) = p^(n+2) - 1
    have h_pow : p ^ (n + 1) ≥ 1 := Nat.one_le_pow _ _ (by omega)
    have expand : (p - 1) * p ^ (n + 1) = p * p ^ (n + 1) - p ^ (n + 1) := by
      rw [Nat.sub_mul, Nat.one_mul]
    rw [expand]
    have hpow2 : p ^ (n + 2) = p * p ^ (n + 1) := by ring
    rw [hpow2]
    -- (p * p^(n+1) - 1) + (p * p^(n+1) - p^(n+1))  no this is wrong rearrangement
    -- Actually: (p^(n+1) - 1) + (p * p^(n+1) - p^(n+1)) = p^(n+1) - 1 + p*p^(n+1) - p^(n+1)
    --         = p * p^(n+1) - 1
    -- Need h_pp : p * p^(n+1) ≥ p^(n+1)
    have h_pp : p * p ^ (n + 1) ≥ p ^ (n + 1) := by
      have : p * p ^ (n + 1) ≥ 1 * p ^ (n + 1) := Nat.mul_le_mul_right _ (by omega : 1 ≤ p)
      linarith
    omega

/-- Theorem B case 3: p prime, a ≥ 2 → σ(p^a)·φ(p^a) ≠ p^a·τ(p^a) -/
theorem theorem_B_prime_power {p : ℕ} (hp : p.Prime) {a : ℕ} (ha : a ≥ 2) :
    σ 1 (p ^ a) * Nat.totient (p ^ a) ≠ (p ^ a) * (Nat.divisors (p ^ a)).card := by
  have hp2 : p ≥ 2 := hp.two_le
  have hp_pos : p ≥ 1 := by omega
  rw [sigma_one_prime_pow_sum hp, tau_prime_pow hp]
  rw [Nat.totient_prime_pow hp (by omega : a > 0)]
  -- Goal: (Σ p^k) * (p^(a-1) * (p-1)) = p^a * (a+1)
  intro h
  -- Reorganize: p^(a-1) * ((p-1) * Σ p^k) = p^a * (a+1)
  have reorg : (∑ k ∈ Finset.range (a + 1), p ^ k) * (p ^ (a - 1) * (p - 1))
             = p ^ (a - 1) * ((p - 1) * ∑ k ∈ Finset.range (a + 1), p ^ k) := by
    ring
  rw [reorg, geom_sum_identity hp2] at h
  -- h: p^(a-1) * (p^(a+1) - 1) = p^a * (a+1)
  -- Note p^a = p * p^(a-1) (for a ≥ 1)
  have h_pa : p ^ a = p * p ^ (a - 1) := by
    have h' : a = (a - 1) + 1 := by omega
    conv_lhs => rw [h']
    ring
  rw [h_pa] at h
  -- h: p^(a-1) * (p^(a+1) - 1) = p * p^(a-1) * (a+1)
  -- Cancel p^(a-1) > 0 to get p^(a+1) - 1 = p * (a+1), contradicts strict_gt
  have hstrict : p ^ (a + 1) > p * (a + 1) + 1 := prime_pow_strict_gt hp2 ha
  have h_reorg_rhs : p * p ^ (a - 1) * (a + 1) = p ^ (a - 1) * (p * (a + 1)) := by ring
  rw [h_reorg_rhs] at h
  -- h: p^(a-1) * (p^(a+1) - 1) = p^(a-1) * (p*(a+1))
  have h_cancel : p ^ (a + 1) - 1 = p * (a + 1) :=
    Nat.eq_of_mul_eq_mul_left (Nat.pos_of_ne_zero (by positivity)) h
  omega

/-- 확인: 작은 케이스들 -/
example : σ 1 (2^2) * Nat.totient (2^2) ≠ (2^2) * (Nat.divisors (2^2)).card :=
  theorem_B_prime_power Nat.prime_two (by norm_num)

example : σ 1 (3^2) * Nat.totient (3^2) ≠ (3^2) * (Nat.divisors (3^2)).card :=
  theorem_B_prime_power Nat.prime_three (by norm_num)

example : σ 1 (2^3) * Nat.totient (2^3) ≠ (2^3) * (Nat.divisors (2^3)).card :=
  theorem_B_prime_power Nat.prime_two (by norm_num)

example : σ 1 (5^4) * Nat.totient (5^4) ≠ (5^4) * (Nat.divisors (5^4)).card :=
  theorem_B_prime_power (by decide : (5 : ℕ).Prime) (by norm_num)

-- Theorem B 진전:
--  Case 1 (prime p): ✓ theorem_B_prime_case
--  Case 2a (n = 2q, q odd prime): ✓ theorem_B_2q
--  Case 2b (n = pq, p, q odd distinct): ✓ theorem_B_odd_pq
--  Case 3 (n = p^a, a ≥ 2): ✓ theorem_B_prime_power (본 파일)
--  Case 4 (n = 일반 합성수): v5 이상

end N6Mathlib
