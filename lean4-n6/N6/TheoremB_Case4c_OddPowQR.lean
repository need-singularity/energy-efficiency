-- N6.TheoremB_Case4c_OddPowQR : Theorem B case 4c(ix) (n = p^a·q·r, p odd ≥ 3, a ≥ 2)
-- v4 M3_v4 case 4c(ix) (2026-04-16 loop 38)
--
-- 목표: p odd ≥ 3, a ≥ 2, q, r odd primes distinct (≠ p, ≠ each other) → σφ(n) ≠ nτ(n)
--
-- 전략 (case 4c(ii) 2^a → p^a 일반화):
--   σφ(p^a) > p^a·(a+1)   STRICT for prime p ≥ 2, a ≥ 2  (generic, case 3)
--   σφ(qr) > qr·4         STRICT for q,r odd distinct ≥ 3,5  (loop 12)
--   곱: σφ(n) = σφ(p^a)·σφ(qr) > p^a·(a+1)·qr·4 = nτ(n) STRICT

import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.NumberTheory.Divisors
import Mathlib.Data.Nat.Totient
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum.Prime
import N6.TheoremB_PrimeCase
import N6.TheoremB_Case3_PrimePow
import N6.TheoremB_Case2_OddOdd
import N6.TheoremB_Case4c_TwoPowQR

namespace N6Mathlib

open Nat ArithmeticFunction
open scoped ArithmeticFunction.sigma

/-- Generic strict bound: σφ(p^a) > p^a·(a+1) for prime p ≥ 2, a ≥ 2 -/
theorem sigma_phi_prime_pow_strict {p a : ℕ} (hp : p.Prime) (hp2 : p ≥ 2) (ha : a ≥ 2) :
    σ 1 (p ^ a) * Nat.totient (p ^ a) > p ^ a * (a + 1) := by
  rw [sigma_one_prime_pow_sum hp, Nat.totient_prime_pow hp (by omega : a > 0)]
  -- (Σ p^k) · (p^(a-1)·(p-1)) > p^a·(a+1)
  have reorg :
      (∑ k ∈ Finset.range (a + 1), p ^ k) * (p ^ (a - 1) * (p - 1))
      = p ^ (a - 1) * ((p - 1) * ∑ k ∈ Finset.range (a + 1), p ^ k) := by ring
  rw [reorg, geom_sum_identity hp2]
  -- p^(a-1) · (p^(a+1) - 1) > p^a · (a+1)
  have h_pa : p ^ a = p * p ^ (a - 1) := by
    have : p ^ a = p ^ ((a - 1) + 1) := by congr 1; omega
    rw [this, pow_succ]; ring
  rw [h_pa]
  have hp_pos : p ^ (a - 1) > 0 := Nat.pow_pos (by omega)
  have h_strict : p ^ (a + 1) > p * (a + 1) + 1 := prime_pow_strict_gt hp2 ha
  have h_pow_ge : p ^ (a + 1) ≥ 1 := Nat.one_le_pow _ _ (by omega)
  have h_sub : p ^ (a + 1) - 1 > p * (a + 1) := by omega
  calc p ^ (a - 1) * (p ^ (a + 1) - 1)
      > p ^ (a - 1) * (p * (a + 1)) :=
        (Nat.mul_lt_mul_left hp_pos).mpr h_sub
    _ = p * p ^ (a - 1) * (a + 1) := by ring

/-- Coprime p^a · (q · r) for p, q, r distinct primes -/
theorem coprime_ppow_qr {p q r a : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hr : r.Prime)
    (hpq : p ≠ q) (hpr : p ≠ r) :
    Nat.Coprime (p ^ a) (q * r) := by
  have hpq_cop : Nat.Coprime p q := (Nat.coprime_primes hp hq).mpr hpq
  have hpr_cop : Nat.Coprime p r := (Nat.coprime_primes hp hr).mpr hpr
  have hp_qr : Nat.Coprime p (q * r) := Nat.Coprime.mul_right hpq_cop hpr_cop
  exact hp_qr.pow_left a

/-- Theorem B case 4c(ix): p^a·q·r with p odd, a ≥ 2 → σφ ≠ nτ -/
theorem theorem_B_odd_ppow_qr {p q r a : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hr : r.Prime)
    (hp3 : p ≥ 3) (hq3 : q ≥ 3) (hr5 : r ≥ 5)
    (hpq : p ≠ q) (hpr : p ≠ r) (hqr : q ≠ r) (ha : a ≥ 2) :
    σ 1 (p ^ a * (q * r)) * Nat.totient (p ^ a * (q * r)) ≠
      (p ^ a * (q * r)) * (Nat.divisors (p ^ a * (q * r))).card := by
  have hcop : Nat.Coprime (p ^ a) (q * r) := coprime_ppow_qr hp hq hr hpq hpr
  have hcop_qr : Nat.Coprime q r := coprime_of_distinct_primes hq hr hqr
  have hσ : σ 1 (p ^ a * (q * r)) = σ 1 (p ^ a) * σ 1 (q * r) :=
    (isMultiplicative_sigma (k := 1)).right hcop
  have hφ : Nat.totient (p ^ a * (q * r)) =
            Nat.totient (p ^ a) * Nat.totient (q * r) :=
    Nat.totient_mul hcop
  have hσ0 : σ 0 (p ^ a * (q * r)) = σ 0 (p ^ a) * σ 0 (q * r) :=
    (isMultiplicative_sigma (k := 0)).right hcop
  have hτ : (Nat.divisors (p ^ a * (q * r))).card = (a + 1) * 4 := by
    have h_left : σ 0 (p ^ a * (q * r)) = (Nat.divisors (p ^ a * (q * r))).card := by
      simp [sigma_zero_apply]
    have h_qr : σ 0 (q * r) = 4 := by
      have h_left2 : σ 0 (q * r) = (Nat.divisors (q * r)).card := by
        simp [sigma_zero_apply]
      rw [h_left2, tau_pq hq hr hcop_qr]
    rw [← h_left, hσ0, sigma_zero_apply_prime_pow hp, h_qr]
  rw [hσ, hφ, hτ]
  intro h
  have reorg_lhs :
      σ 1 (p ^ a) * σ 1 (q * r) * (Nat.totient (p ^ a) * Nat.totient (q * r))
      = (σ 1 (p ^ a) * Nat.totient (p ^ a)) * (σ 1 (q * r) * Nat.totient (q * r)) := by
    ring
  have reorg_rhs :
      p ^ a * (q * r) * ((a + 1) * 4) = (p ^ a * (a + 1)) * ((q * r) * 4) := by ring
  rw [reorg_lhs, reorg_rhs] at h
  have h1 : σ 1 (p ^ a) * Nat.totient (p ^ a) > p ^ a * (a + 1) :=
    sigma_phi_prime_pow_strict hp (by omega : p ≥ 2) ha
  have h2 : σ 1 (q * r) * Nat.totient (q * r) > (q * r) * 4 :=
    sigma_phi_qr_strict hq hr hq3 hr5 hqr
  have hA_pos : p ^ a * (a + 1) > 0 := by positivity
  have h_product_gt :
      (σ 1 (p ^ a) * Nat.totient (p ^ a)) * (σ 1 (q * r) * Nat.totient (q * r))
        > (p ^ a * (a + 1)) * ((q * r) * 4) := by
    calc (σ 1 (p ^ a) * Nat.totient (p ^ a)) * (σ 1 (q * r) * Nat.totient (q * r))
        > (p ^ a * (a + 1)) * (σ 1 (q * r) * Nat.totient (q * r)) :=
          (Nat.mul_lt_mul_right (by positivity)).mpr h1
      _ > (p ^ a * (a + 1)) * ((q * r) * 4) :=
          (Nat.mul_lt_mul_left hA_pos).mpr h2
  omega

-- 확인 예시
-- n = 3²·5·7 = 315: σ=624, φ=144, τ=12. σφ=89856, nτ=3780, 비율 23.8× ✓
-- n = 5²·3·7 = 525: σ=744, φ=240, τ=12. σφ=178560, nτ=6300, 비율 28.3× ✓

end N6Mathlib
