-- N6.TheoremB_Case4c_TwoPowQRS : Theorem B case 4c(iii) (n = 2^a·q·r·s, a ≥ 2)
-- v4 M3_v4 case 4c(iii) (2026-04-16 loop 32)
--
-- 목표: a ≥ 2, q ≥ 3, r ≥ 5, s ≥ 7 odd distinct primes → σ(n)·φ(n) ≠ n·τ(n)
--
-- 전략 (STRICT bounds 곱):
--   σφ(2^a) > 2^a·(a+1)  [loop 12 sigma_phi_2pow_strict]
--   σφ(qrs) > qrs·8       [새 lemma: sigma_phi_qrs_strict, case 4a 확장]
--   곱: σφ(2^a·qrs) > (2^a·(a+1))·(qrs·8) = nτ(2^a·qrs) STRICT

import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.NumberTheory.Divisors
import Mathlib.Data.Nat.Totient
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum.Prime
import N6.TheoremB_PrimeCase
import N6.TheoremB_Case3_PrimePow
import N6.TheoremB_Case4_ThreePrimes
import N6.TheoremB_Case4c_TwoPowQR

namespace N6Mathlib

open Nat ArithmeticFunction
open scoped ArithmeticFunction.sigma

/-- Strict bound: σφ(qrs) > qrs·8 for q,r,s odd distinct primes ≥ 3,5,7 -/
theorem sigma_phi_qrs_strict {q r s : ℕ}
    (hq : q.Prime) (hr : r.Prime) (hs : s.Prime)
    (hq3 : q ≥ 3) (hr5 : r ≥ 5) (hs7 : s ≥ 7)
    (hqr : q ≠ r) (hqs : q ≠ s) (hrs : r ≠ s) :
    σ 1 (q * r * s) * Nat.totient (q * r * s) > (q * r * s) * 8 := by
  have hcop_qr : Nat.Coprime q r := coprime_of_distinct_primes hq hr hqr
  have hcop_qrs : Nat.Coprime (q * r) s := coprime_prod_prime hq hr hs hqs hrs
  rw [sigma_one_pqr hq hr hs hqr hqs hrs]
  rw [totient_pqr hq hr hs hqr hqs hrs]
  rw [sigma_one_prime hq, sigma_one_prime hr, sigma_one_prime hs]
  rw [Nat.totient_prime hq, Nat.totient_prime hr, Nat.totient_prime hs]
  -- Goal: (q+1)(r+1)(s+1)·(q-1)(r-1)(s-1) > qrs·8
  -- Bounds:
  -- (q+1)(q-1) ≥ 2q + 2 (q≥3, from loop 12 pattern)
  -- (r+1)(r-1) ≥ 2r + 8 (r≥5)
  -- (s+1)(s-1) ≥ 2s + 12 (s≥7, from (s-1)² ≥ 36)
  -- 곱: ≥ (2q+2)(2r+8)(2s+12) = 8(q+1)(r+4)(s+6) ≥ 8·4·9·13 = 3744 at min
  -- nτ = 8qrs = 8·q·r·s. q=3, r=5, s=7 → 8·105 = 840
  -- 3744 > 840 ✓
  have hq_lb : (q + 1) * (q - 1) ≥ 2 * q + 2 := by
    have hq1 : q - 1 ≥ 2 := by omega
    have h_eq : (q + 1) * (q - 1) = (q - 1) * (q - 1) + 2 * (q - 1) := by
      have h_q : q + 1 = (q - 1) + 2 := by omega
      rw [h_q]; ring
    rw [h_eq]
    have : (q - 1) * (q - 1) ≥ 4 := Nat.mul_le_mul hq1 hq1 |>.trans_eq (by ring)
    omega
  have hr_lb : (r + 1) * (r - 1) ≥ 2 * r + 8 := by
    have hr1 : r - 1 ≥ 4 := by omega
    have h_eq : (r + 1) * (r - 1) = (r - 1) * (r - 1) + 2 * (r - 1) := by
      have h_r : r + 1 = (r - 1) + 2 := by omega
      rw [h_r]; ring
    rw [h_eq]
    have : (r - 1) * (r - 1) ≥ 16 := Nat.mul_le_mul hr1 hr1 |>.trans_eq (by ring)
    omega
  have hs_lb : (s + 1) * (s - 1) ≥ 2 * s + 12 := by
    have hs1 : s - 1 ≥ 6 := by omega
    have h_eq : (s + 1) * (s - 1) = (s - 1) * (s - 1) + 2 * (s - 1) := by
      have h_s : s + 1 = (s - 1) + 2 := by omega
      rw [h_s]; ring
    rw [h_eq]
    have : (s - 1) * (s - 1) ≥ 36 := Nat.mul_le_mul hs1 hs1 |>.trans_eq (by ring)
    omega
  -- Reorganize: (q+1)(r+1)(s+1)·(q-1)(r-1)(s-1) = (q+1)(q-1) · (r+1)(r-1) · (s+1)(s-1)
  have reorg :
      (q + 1) * (r + 1) * (s + 1) * ((q - 1) * (r - 1) * (s - 1))
      = ((q + 1) * (q - 1)) * ((r + 1) * (r - 1)) * ((s + 1) * (s - 1)) := by
    ring
  rw [reorg]
  -- Product ≥ (2q+2)(2r+8)(2s+12)
  have h_prod : ((q + 1) * (q - 1)) * ((r + 1) * (r - 1)) * ((s + 1) * (s - 1))
                  ≥ (2 * q + 2) * (2 * r + 8) * (2 * s + 12) :=
    Nat.mul_le_mul (Nat.mul_le_mul hq_lb hr_lb) hs_lb
  -- (2q+2)(2r+8)(2s+12) > 8qrs — expansion 계산
  -- = 8(q+1)(r+4)(s+6). Expand: (q+1)(r+4)(s+6) = qrs + ... > qrs (all terms positive)
  -- 구체적: (q+1)(r+4) = qr + 4q + r + 4
  -- × (s+6) = qrs + 6qr + 4qs + 24q + rs + 6r + 4s + 24
  -- So (q+1)(r+4)(s+6) = qrs + 6qr + 4qs + rs + 24q + 6r + 4s + 24
  -- (2q+2)(2r+8)(2s+12) = 8·[qrs + 6qr + 4qs + rs + 24q + 6r + 4s + 24]
  -- > 8qrs (all other terms positive)
  nlinarith

/-- Coprime 2^a and qrs for q,r,s odd primes -/
theorem coprime_2pow_qrs {q r s a : ℕ}
    (hq : q.Prime) (hr : r.Prime) (hs : s.Prime)
    (hq3 : q ≥ 3) (hr5 : r ≥ 5) (hs7 : s ≥ 7) :
    Nat.Coprime (2 ^ a) (q * r * s) := by
  have h2q : Nat.Coprime 2 q := by
    apply (Nat.coprime_primes (by decide : (2 : ℕ).Prime) hq).mpr; omega
  have h2r : Nat.Coprime 2 r := by
    apply (Nat.coprime_primes (by decide : (2 : ℕ).Prime) hr).mpr; omega
  have h2s : Nat.Coprime 2 s := by
    apply (Nat.coprime_primes (by decide : (2 : ℕ).Prime) hs).mpr; omega
  have h2qr : Nat.Coprime 2 (q * r) := Nat.Coprime.mul_right h2q h2r
  have h2qrs : Nat.Coprime 2 (q * r * s) := Nat.Coprime.mul_right h2qr h2s
  exact h2qrs.pow_left a

/-- Theorem B case 4c(iii): n = 2^a·q·r·s, a ≥ 2, q,r,s odd distinct → σφ ≠ nτ -/
theorem theorem_B_2pow_qrs {q r s a : ℕ}
    (hq : q.Prime) (hr : r.Prime) (hs : s.Prime)
    (hq3 : q ≥ 3) (hr5 : r ≥ 5) (hs7 : s ≥ 7)
    (hqr : q ≠ r) (hqs : q ≠ s) (hrs : r ≠ s) (ha : a ≥ 2) :
    σ 1 (2 ^ a * (q * r * s)) * Nat.totient (2 ^ a * (q * r * s)) ≠
      (2 ^ a * (q * r * s)) * (Nat.divisors (2 ^ a * (q * r * s))).card := by
  have hcop : Nat.Coprime (2 ^ a) (q * r * s) := coprime_2pow_qrs hq hr hs hq3 hr5 hs7
  have hσ : σ 1 (2 ^ a * (q * r * s)) = σ 1 (2 ^ a) * σ 1 (q * r * s) :=
    (isMultiplicative_sigma (k := 1)).right hcop
  have hφ : Nat.totient (2 ^ a * (q * r * s)) =
            Nat.totient (2 ^ a) * Nat.totient (q * r * s) :=
    Nat.totient_mul hcop
  have hσ0 : σ 0 (2 ^ a * (q * r * s)) = σ 0 (2 ^ a) * σ 0 (q * r * s) :=
    (isMultiplicative_sigma (k := 0)).right hcop
  have hτ : (Nat.divisors (2 ^ a * (q * r * s))).card = (a + 1) * 8 := by
    have h_left : σ 0 (2 ^ a * (q * r * s)) = (Nat.divisors (2 ^ a * (q * r * s))).card := by
      simp [sigma_zero_apply]
    have h_qrs : σ 0 (q * r * s) = 8 := by
      have h_left2 : σ 0 (q * r * s) = (Nat.divisors (q * r * s)).card := by
        simp [sigma_zero_apply]
      rw [h_left2, tau_pqr hq hr hs hqr hqs hrs]
    rw [← h_left, hσ0, sigma_zero_apply_prime_pow Nat.prime_two, h_qrs]
  rw [hσ, hφ, hτ]
  intro h
  -- h: σ₁(2^a)·σ₁(qrs)·(φ(2^a)·φ(qrs)) = 2^a·qrs·((a+1)·8)
  have reorg_lhs :
      σ 1 (2 ^ a) * σ 1 (q * r * s) * (Nat.totient (2 ^ a) * Nat.totient (q * r * s))
      = (σ 1 (2 ^ a) * Nat.totient (2 ^ a)) * (σ 1 (q * r * s) * Nat.totient (q * r * s)) := by
    ring
  have reorg_rhs :
      2 ^ a * (q * r * s) * ((a + 1) * 8) = (2 ^ a * (a + 1)) * ((q * r * s) * 8) := by
    ring
  rw [reorg_lhs, reorg_rhs] at h
  -- Strict bounds
  have h1 : σ 1 (2 ^ a) * Nat.totient (2 ^ a) > 2 ^ a * (a + 1) := sigma_phi_2pow_strict ha
  have h2 : σ 1 (q * r * s) * Nat.totient (q * r * s) > (q * r * s) * 8 :=
    sigma_phi_qrs_strict hq hr hs hq3 hr5 hs7 hqr hqs hrs
  have hA_pos : 2 ^ a * (a + 1) > 0 := by positivity
  have h_product_gt :
      (σ 1 (2 ^ a) * Nat.totient (2 ^ a)) * (σ 1 (q * r * s) * Nat.totient (q * r * s))
        > (2 ^ a * (a + 1)) * ((q * r * s) * 8) := by
    calc (σ 1 (2 ^ a) * Nat.totient (2 ^ a)) * (σ 1 (q * r * s) * Nat.totient (q * r * s))
        > (2 ^ a * (a + 1)) * (σ 1 (q * r * s) * Nat.totient (q * r * s)) :=
          (Nat.mul_lt_mul_right (by positivity)).mpr h1
      _ > (2 ^ a * (a + 1)) * ((q * r * s) * 8) :=
          (Nat.mul_lt_mul_left hA_pos).mpr h2
  omega

-- 확인 예시
-- n = 420 = 4·3·5·7: σ=672, φ=96, τ=24. σφ=64512, nτ=10080, 비율 6.4 ✓
-- n = 840 = 8·3·5·7: σ=2880, φ=192, τ=32. σφ=552960, nτ=26880, 비율 20.6 ✓

end N6Mathlib
