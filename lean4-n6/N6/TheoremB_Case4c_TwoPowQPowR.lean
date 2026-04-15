-- N6.TheoremB_Case4c_TwoPowQPowR : Theorem B case 4c(vi) (n = 2^a·q^b·r, a,b ≥ 2)
-- v4 M3_v4 case 4c(vi) (2026-04-16 loop 36)
--
-- 목표: a ≥ 2, b ≥ 2, q,r odd prime ≥ 3 distinct → σφ(n) ≠ nτ(n)
--
-- 전략 (3 STRICT bound 곱):
--   σφ(2^a) > 2^a·(a+1)    [loop 12]
--   σφ(q^b) > q^b·(b+1)    [loop 9/10 pattern — case 3 for odd primes]
--   σφ(r) > r·2            [case 1 for r ≥ 3 odd prime]
--   곱: σφ(n) > 2^a(a+1)·q^b(b+1)·2r = nτ(n) STRICT

import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.NumberTheory.Divisors
import Mathlib.Data.Nat.Totient
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum.Prime
import N6.TheoremB_PrimeCase
import N6.TheoremB_Case3_PrimePow
import N6.TheoremB_Case4b_OddPrimePowers
import N6.TheoremB_Case4c_TwoPowQR

namespace N6Mathlib

open Nat ArithmeticFunction
open scoped ArithmeticFunction.sigma

/-- Strict bound: σφ(q^b) > q^b·(b+1) for q odd prime ≥ 3, b ≥ 1 -/
theorem sigma_phi_odd_prime_pow_strict {q b : ℕ}
    (hq : q.Prime) (hq3 : q ≥ 3) (hb : b ≥ 1) :
    σ 1 (q ^ b) * Nat.totient (q ^ b) > q ^ b * (b + 1) := by
  rw [sigma_one_prime_pow_sum hq, Nat.totient_prime_pow hq (by omega : b > 0)]
  -- (Σ q^k)·(q^(b-1)·(q-1)) > q^b·(b+1)
  have reorg :
      (∑ k ∈ Finset.range (b + 1), q ^ k) * (q ^ (b - 1) * (q - 1)) =
      q ^ (b - 1) * ((q - 1) * ∑ k ∈ Finset.range (b + 1), q ^ k) := by ring
  rw [reorg]
  rw [geom_sum_identity (by omega : q ≥ 2)]
  -- Goal: q^(b-1) · (q^(b+1) - 1) > q^b · (b+1)
  -- q^b = q·q^(b-1), so RHS = q·q^(b-1)·(b+1)
  -- Divide by q^(b-1) > 0: q^(b+1) - 1 > q·(b+1)
  -- For q odd ≥ 3, b ≥ 1: pow_strict_gt_odd gives q^(b+1) > q(b+1)+1
  -- So q^(b+1) - 1 > q(b+1), hence q^(b-1)·(q^(b+1) - 1) > q^(b-1)·q·(b+1) = q^b·(b+1)
  have h_qb : q ^ b = q * q ^ (b - 1) := by
    have : q ^ b = q ^ ((b - 1) + 1) := by congr 1; omega
    rw [this, pow_succ]; ring
  rw [h_qb]
  have hq_pos : q ^ (b - 1) > 0 := Nat.pow_pos (by omega)
  have h_pow_strict : q ^ (b + 1) > q * (b + 1) + 1 := pow_strict_gt_odd hq3 hb
  have h_sub_gt : q ^ (b + 1) - 1 > q * (b + 1) := by omega
  -- q^(b-1) · (q^(b+1) - 1) > q^(b-1) · q·(b+1) = q·q^(b-1)·(b+1)
  calc q ^ (b - 1) * (q ^ (b + 1) - 1)
      > q ^ (b - 1) * (q * (b + 1)) :=
        (Nat.mul_lt_mul_left hq_pos).mpr h_sub_gt
    _ = q * q ^ (b - 1) * (b + 1) := by ring

/-- Strict bound: σφ(r) > 2r for r odd prime ≥ 3 -/
theorem sigma_phi_odd_prime_strict {r : ℕ} (hr : r.Prime) (hr3 : r ≥ 3) :
    σ 1 r * Nat.totient r > r * 2 := by
  rw [sigma_one_prime hr, Nat.totient_prime hr]
  -- (r+1)(r-1) > 2r ⟺ r²-1 > 2r ⟺ (r-1)² > 2
  -- For r ≥ 3: (r-1)² ≥ 4 > 2
  have hr1 : r - 1 ≥ 2 := by omega
  have h_eq : (r + 1) * (r - 1) = (r - 1) * (r - 1) + 2 * (r - 1) := by
    have h_r : r + 1 = (r - 1) + 2 := by omega
    rw [h_r]; ring
  rw [h_eq]
  have : (r - 1) * (r - 1) ≥ 4 := Nat.mul_le_mul hr1 hr1 |>.trans_eq (by ring)
  omega

/-- Coprime (2^a · q^b) and r for q, r distinct odd primes -/
theorem coprime_2pow_qpow_r {q r a b : ℕ}
    (hq : q.Prime) (hr : r.Prime) (hq3 : q ≥ 3) (hr3 : r ≥ 3) (hqr : q ≠ r) :
    Nat.Coprime (2 ^ a * q ^ b) r := by
  have h2r : Nat.Coprime 2 r := by
    apply (Nat.coprime_primes (by decide : (2 : ℕ).Prime) hr).mpr; omega
  have hqr_cop : Nat.Coprime q r := (Nat.coprime_primes hq hr).mpr hqr
  have h2_pow : Nat.Coprime (2 ^ a) r := h2r.pow_left a
  have hq_pow : Nat.Coprime (q ^ b) r := hqr_cop.pow_left b
  -- (2^a · q^b).Coprime r
  rw [Nat.Coprime, Nat.coprime_comm.mp
    (Nat.coprime_mul_iff_right.mpr ⟨h2_pow.symm, hq_pow.symm⟩)]

/-- Coprime 2^a and q^b for q odd prime -/
theorem coprime_2pow_qpow {q a b : ℕ}
    (hq : q.Prime) (hq3 : q ≥ 3) :
    Nat.Coprime (2 ^ a) (q ^ b) := by
  have h2q : Nat.Coprime 2 q := by
    apply (Nat.coprime_primes (by decide : (2 : ℕ).Prime) hq).mpr; omega
  exact (h2q.pow_left a).pow_right b

/-- Theorem B case 4c(vi): n = 2^a·q^b·r, a,b ≥ 2, q,r odd distinct → σφ ≠ nτ -/
theorem theorem_B_2pow_qpow_r {q r a b : ℕ}
    (hq : q.Prime) (hr : r.Prime)
    (hq3 : q ≥ 3) (hr3 : r ≥ 3)
    (hqr : q ≠ r) (ha : a ≥ 2) (hb : b ≥ 2) :
    σ 1 (2 ^ a * q ^ b * r) * Nat.totient (2 ^ a * q ^ b * r) ≠
      (2 ^ a * q ^ b * r) * (Nat.divisors (2 ^ a * q ^ b * r)).card := by
  have hcop_main : Nat.Coprime (2 ^ a * q ^ b) r := coprime_2pow_qpow_r hq hr hq3 hr3 hqr
  have hcop_2q : Nat.Coprime (2 ^ a) (q ^ b) := coprime_2pow_qpow hq hq3
  -- σ, φ, τ multiplicative
  have hσ : σ 1 (2 ^ a * q ^ b * r) = σ 1 (2 ^ a * q ^ b) * σ 1 r :=
    (isMultiplicative_sigma (k := 1)).right hcop_main
  have hσ_inner : σ 1 (2 ^ a * q ^ b) = σ 1 (2 ^ a) * σ 1 (q ^ b) :=
    (isMultiplicative_sigma (k := 1)).right hcop_2q
  have hφ : Nat.totient (2 ^ a * q ^ b * r) =
            Nat.totient (2 ^ a * q ^ b) * Nat.totient r :=
    Nat.totient_mul hcop_main
  have hφ_inner : Nat.totient (2 ^ a * q ^ b) = Nat.totient (2 ^ a) * Nat.totient (q ^ b) :=
    Nat.totient_mul hcop_2q
  have hτ : (Nat.divisors (2 ^ a * q ^ b * r)).card = (a + 1) * (b + 1) * 2 := by
    have hσ0 : σ 0 (2 ^ a * q ^ b * r) = σ 0 (2 ^ a * q ^ b) * σ 0 r :=
      (isMultiplicative_sigma (k := 0)).right hcop_main
    have hσ0_inner : σ 0 (2 ^ a * q ^ b) = σ 0 (2 ^ a) * σ 0 (q ^ b) :=
      (isMultiplicative_sigma (k := 0)).right hcop_2q
    have h_left : σ 0 (2 ^ a * q ^ b * r) = (Nat.divisors (2 ^ a * q ^ b * r)).card := by
      simp [sigma_zero_apply]
    have h_r : σ 0 r = 2 := by
      have := sigma_zero_apply_prime_pow (p := r) (i := 1) hr
      simp at this; exact this
    rw [← h_left, hσ0, hσ0_inner,
        sigma_zero_apply_prime_pow Nat.prime_two,
        sigma_zero_apply_prime_pow hq, h_r]
  rw [hσ, hσ_inner, hφ, hφ_inner, hτ]
  intro h
  -- Reorganize LHS/RHS
  have reorg_lhs :
      σ 1 (2 ^ a) * σ 1 (q ^ b) * σ 1 r *
      (Nat.totient (2 ^ a) * Nat.totient (q ^ b) * Nat.totient r)
      = (σ 1 (2 ^ a) * Nat.totient (2 ^ a)) *
        (σ 1 (q ^ b) * Nat.totient (q ^ b)) *
        (σ 1 r * Nat.totient r) := by ring
  have reorg_rhs :
      2 ^ a * q ^ b * r * ((a + 1) * (b + 1) * 2)
      = (2 ^ a * (a + 1)) * (q ^ b * (b + 1)) * (r * 2) := by ring
  rw [reorg_lhs, reorg_rhs] at h
  -- Strict bounds
  have h1 : σ 1 (2 ^ a) * Nat.totient (2 ^ a) > 2 ^ a * (a + 1) :=
    sigma_phi_2pow_strict ha
  have h2 : σ 1 (q ^ b) * Nat.totient (q ^ b) > q ^ b * (b + 1) :=
    sigma_phi_odd_prime_pow_strict hq hq3 (by omega : b ≥ 1)
  have h3 : σ 1 r * Nat.totient r > r * 2 :=
    sigma_phi_odd_prime_strict hr hr3
  have hA_pos : 2 ^ a * (a + 1) > 0 := by positivity
  have hB_pos : q ^ b * (b + 1) > 0 := by positivity
  have hC_pos : r * 2 > 0 := by positivity
  have h_prod_gt :
      (σ 1 (2 ^ a) * Nat.totient (2 ^ a)) *
      (σ 1 (q ^ b) * Nat.totient (q ^ b)) *
      (σ 1 r * Nat.totient r) >
      (2 ^ a * (a + 1)) * (q ^ b * (b + 1)) * (r * 2) := by
    calc (σ 1 (2 ^ a) * Nat.totient (2 ^ a)) *
         (σ 1 (q ^ b) * Nat.totient (q ^ b)) *
         (σ 1 r * Nat.totient r)
        > (2 ^ a * (a + 1)) *
          (σ 1 (q ^ b) * Nat.totient (q ^ b)) *
          (σ 1 r * Nat.totient r) :=
          (Nat.mul_lt_mul_right (by positivity)).mpr
          ((Nat.mul_lt_mul_right (by positivity)).mpr h1)
      _ > (2 ^ a * (a + 1)) * (q ^ b * (b + 1)) * (σ 1 r * Nat.totient r) :=
          (Nat.mul_lt_mul_right (by positivity)).mpr
          ((Nat.mul_lt_mul_left hA_pos).mpr h2)
      _ > (2 ^ a * (a + 1)) * (q ^ b * (b + 1)) * (r * 2) :=
          (Nat.mul_lt_mul_left (by positivity)).mpr h3
  omega

-- 확인 예시
-- n = 180 = 4·9·5: σ(180)=546, φ=48, τ=18, σφ=26208, nτ=3240, 비율 8.09× ✓

end N6Mathlib
