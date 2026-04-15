-- N6.TheoremB_Case4c_TwoQPowR : Theorem B case 4c(viii) (n = 2·q^b·r, b ≥ 2)
-- v4 M3_v4 case 4c(viii) (2026-04-16 loop 37)
--
-- 목표: b ≥ 2, q,r odd prime ≥ 3 distinct → σφ(2·q^b·r) ≠ (2·q^b·r)·τ
--
-- 전략 (3·σφ ≥ 4·nτ):
--   σφ(q^b) ≥ (4/3)·q^b·(b+1): 3·σφ(q^b) ≥ 4·q^b·(b+1)
--       from key_ineq_odd_weak (loop 10)
--   σφ(r)   ≥ (4/3)·2r: 3·σφ(r) ≥ 8r  (r odd ≥ 3, equality at r=3)
--   곱: 9·σφ(q^b)·σφ(r) ≥ 32·q^b·r·(b+1)
--   σφ(n) = 3·σφ(q^b)·σφ(r), nτ(n) = 8·q^b·r·(b+1)
--   3·σφ(n) = 9·σφ(q^b)·σφ(r) ≥ 32·q^b·r·(b+1) = 4·nτ(n)
--   ⟹ 3·σφ(n) ≥ 4·nτ(n), nτ > 0 이므로 σφ > nτ STRICT → σφ ≠ nτ

import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.NumberTheory.Divisors
import Mathlib.Data.Nat.Totient
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum.Prime
import N6.TheoremB_PrimeCase
import N6.TheoremB_Case3_PrimePow
import N6.TheoremB_Case4_ThreePrimes
import N6.TheoremB_Case4b_TwoPrimePow
import N6.TheoremB_Case4b_OddPrimePowers
import N6.TheoremB_Case4b_TwoPowOddPow

namespace N6Mathlib

open Nat ArithmeticFunction
open scoped ArithmeticFunction.sigma

/-- 3·σφ(q^b) ≥ 4·q^b·(b+1) for q odd prime ≥ 3, b ≥ 1  (weak 4/3 bound) -/
theorem sigma_phi_odd_pow_ge_four_thirds {q b : ℕ}
    (hq : q.Prime) (hq3 : q ≥ 3) (hb : b ≥ 1) :
    3 * (σ 1 (q ^ b) * Nat.totient (q ^ b)) ≥ 4 * (q ^ b * (b + 1)) := by
  rw [sigma_one_prime_pow_sum hq, Nat.totient_prime_pow hq (by omega : b > 0)]
  have reorg : 3 * ((∑ k ∈ Finset.range (b + 1), q ^ k) * (q ^ (b - 1) * (q - 1)))
             = q ^ (b - 1) * (3 * ((q - 1) * ∑ k ∈ Finset.range (b + 1), q ^ k)) := by ring
  rw [reorg, geom_sum_identity (by omega : q ≥ 2)]
  -- Goal: q^(b-1) · (3·(q^(b+1) - 1)) ≥ 4·(q^b · (b+1))
  have h_qb : q ^ b = q * q ^ (b - 1) := by
    have : q ^ b = q ^ ((b - 1) + 1) := by congr 1; omega
    rw [this, pow_succ]; ring
  rw [h_qb]
  -- q^(b-1) · (3·(q^(b+1)-1)) ≥ 4·(q·q^(b-1)·(b+1)) = q^(b-1)·(4q(b+1))
  have hq_pos : q ^ (b - 1) > 0 := Nat.pow_pos (by omega)
  -- Need: 3·(q^(b+1)-1) ≥ 4q(b+1)
  -- Have key_ineq_odd_weak: 3·q^(b+1) ≥ 4q(b+1) + 3
  have h_weak : 3 * q ^ (b + 1) ≥ 4 * q * (b + 1) + 3 := key_ineq_odd_weak hq3 hb
  have h_pow : q ^ (b + 1) ≥ 1 := Nat.one_le_pow _ _ (by omega)
  have h_sub : 3 * (q ^ (b + 1) - 1) ≥ 4 * q * (b + 1) := by
    have : 3 * (q ^ (b + 1) - 1) = 3 * q ^ (b + 1) - 3 := by
      rw [Nat.mul_sub, Nat.mul_one]
    omega
  -- q^(b-1) · (3·(q^(b+1)-1)) ≥ q^(b-1) · (4q(b+1)) = 4·q·q^(b-1)·(b+1)
  calc q ^ (b - 1) * (3 * (q ^ (b + 1) - 1))
      ≥ q ^ (b - 1) * (4 * q * (b + 1)) := Nat.mul_le_mul_left _ h_sub
    _ = 4 * (q * q ^ (b - 1) * (b + 1)) := by ring

/-- 3·σφ(r) ≥ 8r for r odd prime ≥ 3  (weak 4/3 bound, 등식 r=3) -/
theorem sigma_phi_odd_prime_ge_four_thirds {r : ℕ} (hr : r.Prime) (hr3 : r ≥ 3) :
    3 * (σ 1 r * Nat.totient r) ≥ 4 * (r * 2) := by
  rw [sigma_one_prime hr, Nat.totient_prime hr]
  -- 3·(r+1)(r-1) ≥ 8r ⟺ 3r²-3 ≥ 8r ⟺ (3r+1)(r-3) ≥ 0
  have hr1 : r - 1 ≥ 2 := by omega
  have h_eq : (r + 1) * (r - 1) = (r - 1) * (r - 1) + 2 * (r - 1) := by
    have h_r : r + 1 = (r - 1) + 2 := by omega
    rw [h_r]; ring
  rw [h_eq]
  have : (r - 1) * (r - 1) ≥ 4 := Nat.mul_le_mul hr1 hr1 |>.trans_eq (by ring)
  nlinarith

/-- Coprime 2 and q^b·r for q,r odd primes -/
theorem coprime_2_qpow_r {q r b : ℕ}
    (hq : q.Prime) (hr : r.Prime) (hq3 : q ≥ 3) (hr3 : r ≥ 3) :
    Nat.Coprime 2 (q ^ b * r) := by
  have h2q : Nat.Coprime 2 q := by
    apply (Nat.coprime_primes (by decide : (2 : ℕ).Prime) hq).mpr; omega
  have h2r : Nat.Coprime 2 r := by
    apply (Nat.coprime_primes (by decide : (2 : ℕ).Prime) hr).mpr; omega
  have h2_pow : Nat.Coprime 2 (q ^ b) := h2q.pow_right b
  exact Nat.Coprime.mul_right h2_pow h2r

/-- Coprime q^b and r for q,r distinct odd primes -/
theorem coprime_qpow_r {q r b : ℕ}
    (hq : q.Prime) (hr : r.Prime) (hqr : q ≠ r) :
    Nat.Coprime (q ^ b) r := by
  have hcop : Nat.Coprime q r := (Nat.coprime_primes hq hr).mpr hqr
  exact hcop.pow_left b

/-- Theorem B case 4c(viii): n = 2·q^b·r, b ≥ 2, q,r odd distinct → σφ ≠ nτ -/
theorem theorem_B_2_qpow_r {q r b : ℕ}
    (hq : q.Prime) (hr : r.Prime)
    (hq3 : q ≥ 3) (hr3 : r ≥ 3)
    (hqr : q ≠ r) (hb : b ≥ 2) :
    σ 1 (2 * (q ^ b * r)) * Nat.totient (2 * (q ^ b * r)) ≠
      (2 * (q ^ b * r)) * (Nat.divisors (2 * (q ^ b * r))).card := by
  have hcop_main : Nat.Coprime 2 (q ^ b * r) := coprime_2_qpow_r hq hr hq3 hr3
  have hcop_qr : Nat.Coprime (q ^ b) r := coprime_qpow_r hq hr hqr
  have hσ : σ 1 (2 * (q ^ b * r)) = σ 1 2 * σ 1 (q ^ b * r) :=
    (isMultiplicative_sigma (k := 1)).right hcop_main
  have hσ_inner : σ 1 (q ^ b * r) = σ 1 (q ^ b) * σ 1 r :=
    (isMultiplicative_sigma (k := 1)).right hcop_qr
  have hφ : Nat.totient (2 * (q ^ b * r)) =
            Nat.totient 2 * Nat.totient (q ^ b * r) :=
    Nat.totient_mul hcop_main
  have hφ_inner : Nat.totient (q ^ b * r) =
                  Nat.totient (q ^ b) * Nat.totient r :=
    Nat.totient_mul hcop_qr
  have hτ : (Nat.divisors (2 * (q ^ b * r))).card = 2 * ((b + 1) * 2) := by
    have hσ0 : σ 0 (2 * (q ^ b * r)) = σ 0 2 * σ 0 (q ^ b * r) :=
      (isMultiplicative_sigma (k := 0)).right hcop_main
    have hσ0_inner : σ 0 (q ^ b * r) = σ 0 (q ^ b) * σ 0 r :=
      (isMultiplicative_sigma (k := 0)).right hcop_qr
    have h_left : σ 0 (2 * (q ^ b * r)) = (Nat.divisors (2 * (q ^ b * r))).card := by
      simp [sigma_zero_apply]
    have h_2 : σ 0 2 = 2 := by
      have := sigma_zero_apply_prime_pow (p := 2) (i := 1) Nat.prime_two
      simp at this; exact this
    have h_r : σ 0 r = 2 := by
      have := sigma_zero_apply_prime_pow (p := r) (i := 1) hr
      simp at this; exact this
    rw [← h_left, hσ0, hσ0_inner, h_2, sigma_zero_apply_prime_pow hq, h_r]
  rw [hσ, hσ_inner, hφ, hφ_inner, hτ]
  intro h
  -- σ₁(2)=3, φ(2)=1
  have h_sigma_2 : σ 1 2 = 3 := sigma_one_prime Nat.prime_two
  have h_totient_2 : Nat.totient 2 = 1 := by decide
  rw [h_sigma_2, h_totient_2] at h
  -- h: 3·σφ(q^b)·σφ(r) = 2·q^b·r · (2·(b+1)·2) = 8·q^b·r·(b+1)
  -- [using 1 · (... · ...) = 1 * ..., etc. ring]
  -- Strategy: 9·σφ(q^b)·σφ(r) ≥ 32·q^b·r·(b+1), but LHS = 3·σφ(n)
  -- 3·σφ(n) = 9·σφ(q^b)·σφ(r) ≥ 32·q^b·r·(b+1) = 4·nτ, 모순
  have h_weak_qb : 3 * (σ 1 (q ^ b) * Nat.totient (q ^ b)) ≥ 4 * (q ^ b * (b + 1)) :=
    sigma_phi_odd_pow_ge_four_thirds hq hq3 (by omega : b ≥ 1)
  have h_weak_r : 3 * (σ 1 r * Nat.totient r) ≥ 4 * (r * 2) :=
    sigma_phi_odd_prime_ge_four_thirds hr hr3
  -- Product 9·σφ(q^b)·σφ(r) ≥ 16·q^b·r·(b+1)·2 = 32·q^b·r·(b+1)
  have h_prod_weak :
      9 * ((σ 1 (q ^ b) * Nat.totient (q ^ b)) * (σ 1 r * Nat.totient r)) ≥
      32 * (q ^ b * r * (b + 1)) := by
    have h_prod : 9 * ((σ 1 (q ^ b) * Nat.totient (q ^ b)) * (σ 1 r * Nat.totient r))
                = (3 * (σ 1 (q ^ b) * Nat.totient (q ^ b))) *
                  (3 * (σ 1 r * Nat.totient r)) := by ring
    rw [h_prod]
    have h_bound : (4 * (q ^ b * (b + 1))) * (4 * (r * 2)) = 32 * (q ^ b * r * (b + 1)) := by ring
    rw [← h_bound]
    exact Nat.mul_le_mul h_weak_qb h_weak_r
  -- h: 3·σφ(q^b)·(1·(σφ(r)·1)) = ... simplification needed
  -- Actually h simplification via ring already done via arguments, let me expand
  -- h: 3·(σ₁(q^b)·σ₁(r)·(1·(φ(q^b)·φ(r)))) = 2·(q^b·r)·(2·(b+1)·2)
  -- Normalize via ring
  have h_eq : 3 * ((σ 1 (q ^ b) * Nat.totient (q ^ b)) * (σ 1 r * Nat.totient r)) =
              8 * (q ^ b * r * (b + 1)) := by
    have h_reorg : 3 * ((σ 1 (q ^ b) * Nat.totient (q ^ b)) * (σ 1 r * Nat.totient r)) =
                   3 * (σ 1 (q ^ b) * σ 1 r) * (1 * (Nat.totient (q ^ b) * Nat.totient r)) := by
      ring
    rw [h_reorg, h]; ring
  -- h_prod_weak × (1) / 3: 9·σφ·σφ ≥ 32·q^b·r·(b+1)
  -- h_eq × 3: 9·σφ·σφ = 24·q^b·r·(b+1)
  -- 24 ≥ 32 impossible
  have h_pos : q ^ b * r * (b + 1) > 0 := by positivity
  omega

-- 확인 예시
-- n = 2·3²·5 = 90: σ(90)=234, φ=24, τ=12, σφ=5616, nτ=1080, 비율 5.2×
-- n = 2·3²·7 = 126: σ=312, φ=36, τ=12, σφ=11232, nτ=1512, 비율 7.4×

end N6Mathlib
