-- N6.TheoremB_Case4c_TwoPowQRSTU : Theorem B case 4c(xiv) (n = 2^a·q·r·s·t·u, a ≥ 2)
-- v4 M3_v4 case 4c(xiv) (2026-04-16 loop 43)
--
-- 목표: a ≥ 2, q,r,s,t,u 5 distinct odd primes ≥ 3,5,7,11,13 → σφ ≠ nτ
--
-- 전략 (기존 strict bounds 조합):
--   σφ(qrst) > qrst·16 (loop 15의 sigma_phi_qrst_strict)
--   σφ(u) > 2u (sigma_phi_odd_prime_strict loop 17)
--   → σφ(qrstu) = σφ(qrst)·σφ(u) > qrst·16·2u = qrstu·32
--   σφ(2^a) > 2^a·(a+1) (loop 12)
--   → σφ(n) = σφ(2^a)·σφ(qrstu) > (2^a·(a+1))·(qrstu·32) = nτ(n) STRICT

import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.NumberTheory.Divisors
import Mathlib.Data.Nat.Totient
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum.Prime
import N6.TheoremB_PrimeCase
import N6.TheoremB_Case3_PrimePow
import N6.TheoremB_Case4c_FivePrimes
import N6.TheoremB_Case4c_TwoPowQR
import N6.TheoremB_Case4c_TwoPowQRST
import N6.TheoremB_Case4c_TwoPowQPowR

namespace N6Mathlib

open Nat ArithmeticFunction
open scoped ArithmeticFunction.sigma

set_option maxHeartbeats 800000

/-- Coprime (qrst) and u for 5 distinct primes -/
theorem coprime_qrst_u {q r s t u : ℕ}
    (hq : q.Prime) (hr : r.Prime) (hs : s.Prime) (ht : t.Prime) (hu : u.Prime)
    (hqu : q ≠ u) (hru : r ≠ u) (hsu : s ≠ u) (htu : t ≠ u) :
    Nat.Coprime (q * r * s * t) u := by
  have h1 : Nat.Coprime q u := coprime_of_distinct_primes hq hu hqu
  have h2 : Nat.Coprime r u := coprime_of_distinct_primes hr hu hru
  have h3 : Nat.Coprime s u := coprime_of_distinct_primes hs hu hsu
  have h4 : Nat.Coprime t u := coprime_of_distinct_primes ht hu htu
  have h12 : Nat.Coprime (q * r) u := by
    rw [Nat.Coprime, Nat.coprime_comm.mp (Nat.coprime_mul_iff_right.mpr ⟨h1.symm, h2.symm⟩)]
  have h123 : Nat.Coprime (q * r * s) u := by
    rw [Nat.Coprime, Nat.coprime_comm.mp (Nat.coprime_mul_iff_right.mpr ⟨h12.symm, h3.symm⟩)]
  rw [Nat.Coprime, Nat.coprime_comm.mp (Nat.coprime_mul_iff_right.mpr ⟨h123.symm, h4.symm⟩)]

/-- Strict bound: σφ(qrstu) > qrstu·32 for 5 odd distinct primes -/
theorem sigma_phi_qrstu_strict {q r s t u : ℕ}
    (hq : q.Prime) (hr : r.Prime) (hs : s.Prime) (ht : t.Prime) (hu : u.Prime)
    (hq3 : q ≥ 3) (hr5 : r ≥ 5) (hs7 : s ≥ 7) (ht11 : t ≥ 11) (hu13 : u ≥ 13)
    (hqr : q ≠ r) (hqs : q ≠ s) (hrs : r ≠ s)
    (hqt : q ≠ t) (hrt : r ≠ t) (hst : s ≠ t)
    (hqu : q ≠ u) (hru : r ≠ u) (hsu : s ≠ u) (htu : t ≠ u) :
    σ 1 (q * r * s * t * u) * Nat.totient (q * r * s * t * u) > (q * r * s * t * u) * 32 := by
  have hcop : Nat.Coprime (q * r * s * t) u :=
    coprime_qrst_u hq hr hs ht hu hqu hru hsu htu
  have hσ : σ 1 (q * r * s * t * u) = σ 1 (q * r * s * t) * σ 1 u :=
    (isMultiplicative_sigma (k := 1)).right hcop
  have hφ : Nat.totient (q * r * s * t * u) = Nat.totient (q * r * s * t) * Nat.totient u :=
    Nat.totient_mul hcop
  rw [hσ, hφ]
  -- σφ(qrst) · σφ(u) > 32·qrstu
  have h_inner : σ 1 (q * r * s * t) * Nat.totient (q * r * s * t) > (q * r * s * t) * 16 :=
    sigma_phi_qrst_strict hq hr hs ht hq3 hr5 hs7 ht11 hqr hqs hrs hqt hrt hst
  have h_u : σ 1 u * Nat.totient u > u * 2 := sigma_phi_odd_prime_strict hu (by omega : u ≥ 3)
  have reorg_lhs :
      σ 1 (q * r * s * t) * σ 1 u * (Nat.totient (q * r * s * t) * Nat.totient u)
      = (σ 1 (q * r * s * t) * Nat.totient (q * r * s * t)) * (σ 1 u * Nat.totient u) := by ring
  have reorg_rhs : q * r * s * t * u * 32 = (q * r * s * t) * 16 * (u * 2) := by ring
  rw [reorg_lhs, reorg_rhs]
  have hA_pos : (q * r * s * t) * 16 > 0 := by positivity
  calc (σ 1 (q * r * s * t) * Nat.totient (q * r * s * t)) * (σ 1 u * Nat.totient u)
      > (q * r * s * t) * 16 * (σ 1 u * Nat.totient u) :=
        (Nat.mul_lt_mul_right (by positivity)).mpr h_inner
    _ > (q * r * s * t) * 16 * (u * 2) :=
        (Nat.mul_lt_mul_left hA_pos).mpr h_u

/-- Coprime 2^a and (q·r·s·t·u) for q,r,s,t,u odd primes -/
theorem coprime_2pow_qrstu {q r s t u a : ℕ}
    (hq : q.Prime) (hr : r.Prime) (hs : s.Prime) (ht : t.Prime) (hu : u.Prime)
    (hq3 : q ≥ 3) (hr5 : r ≥ 5) (hs7 : s ≥ 7) (ht11 : t ≥ 11) (hu13 : u ≥ 13) :
    Nat.Coprime (2 ^ a) (q * r * s * t * u) := by
  have h2q : Nat.Coprime 2 q := by
    apply (Nat.coprime_primes (by decide : (2 : ℕ).Prime) hq).mpr; omega
  have h2r : Nat.Coprime 2 r := by
    apply (Nat.coprime_primes (by decide : (2 : ℕ).Prime) hr).mpr; omega
  have h2s : Nat.Coprime 2 s := by
    apply (Nat.coprime_primes (by decide : (2 : ℕ).Prime) hs).mpr; omega
  have h2t : Nat.Coprime 2 t := by
    apply (Nat.coprime_primes (by decide : (2 : ℕ).Prime) ht).mpr; omega
  have h2u : Nat.Coprime 2 u := by
    apply (Nat.coprime_primes (by decide : (2 : ℕ).Prime) hu).mpr; omega
  have h12 : Nat.Coprime 2 (q * r) := Nat.Coprime.mul_right h2q h2r
  have h123 : Nat.Coprime 2 (q * r * s) := Nat.Coprime.mul_right h12 h2s
  have h1234 : Nat.Coprime 2 (q * r * s * t) := Nat.Coprime.mul_right h123 h2t
  have h12345 : Nat.Coprime 2 (q * r * s * t * u) := Nat.Coprime.mul_right h1234 h2u
  exact h12345.pow_left a

/-- Theorem B case 4c(xiv): n = 2^a·q·r·s·t·u, a ≥ 2, 5 odd distinct → σφ ≠ nτ -/
theorem theorem_B_2pow_qrstu {q r s t u a : ℕ}
    (hq : q.Prime) (hr : r.Prime) (hs : s.Prime) (ht : t.Prime) (hu : u.Prime)
    (hq3 : q ≥ 3) (hr5 : r ≥ 5) (hs7 : s ≥ 7) (ht11 : t ≥ 11) (hu13 : u ≥ 13)
    (hqr : q ≠ r) (hqs : q ≠ s) (hrs : r ≠ s)
    (hqt : q ≠ t) (hrt : r ≠ t) (hst : s ≠ t)
    (hqu : q ≠ u) (hru : r ≠ u) (hsu : s ≠ u) (htu : t ≠ u)
    (ha : a ≥ 2) :
    σ 1 (2 ^ a * (q * r * s * t * u)) * Nat.totient (2 ^ a * (q * r * s * t * u)) ≠
      (2 ^ a * (q * r * s * t * u)) *
        (Nat.divisors (2 ^ a * (q * r * s * t * u))).card := by
  have hcop : Nat.Coprime (2 ^ a) (q * r * s * t * u) :=
    coprime_2pow_qrstu hq hr hs ht hu hq3 hr5 hs7 ht11 hu13
  have hσ : σ 1 (2 ^ a * (q * r * s * t * u)) =
            σ 1 (2 ^ a) * σ 1 (q * r * s * t * u) :=
    (isMultiplicative_sigma (k := 1)).right hcop
  have hφ : Nat.totient (2 ^ a * (q * r * s * t * u)) =
            Nat.totient (2 ^ a) * Nat.totient (q * r * s * t * u) :=
    Nat.totient_mul hcop
  have hσ0 : σ 0 (2 ^ a * (q * r * s * t * u)) =
             σ 0 (2 ^ a) * σ 0 (q * r * s * t * u) :=
    (isMultiplicative_sigma (k := 0)).right hcop
  have hτ : (Nat.divisors (2 ^ a * (q * r * s * t * u))).card = (a + 1) * 32 := by
    have h_left : σ 0 (2 ^ a * (q * r * s * t * u)) =
                  (Nat.divisors (2 ^ a * (q * r * s * t * u))).card := by
      simp [sigma_zero_apply]
    have h_qrstu : σ 0 (q * r * s * t * u) = 32 := by
      have h_left2 : σ 0 (q * r * s * t * u) = (Nat.divisors (q * r * s * t * u)).card := by
        simp [sigma_zero_apply]
      rw [h_left2, tau_pqrst hq hr hs ht hu hqr hqs hrs hqt hrt hst hqu hru hsu htu]
    rw [← h_left, hσ0, sigma_zero_apply_prime_pow Nat.prime_two, h_qrstu]
  rw [hσ, hφ, hτ]
  intro h
  have reorg_lhs :
      σ 1 (2 ^ a) * σ 1 (q * r * s * t * u) *
        (Nat.totient (2 ^ a) * Nat.totient (q * r * s * t * u))
      = (σ 1 (2 ^ a) * Nat.totient (2 ^ a)) *
        (σ 1 (q * r * s * t * u) * Nat.totient (q * r * s * t * u)) := by ring
  have reorg_rhs :
      2 ^ a * (q * r * s * t * u) * ((a + 1) * 32)
      = (2 ^ a * (a + 1)) * ((q * r * s * t * u) * 32) := by ring
  rw [reorg_lhs, reorg_rhs] at h
  have h1 : σ 1 (2 ^ a) * Nat.totient (2 ^ a) > 2 ^ a * (a + 1) := sigma_phi_2pow_strict ha
  have h2 : σ 1 (q * r * s * t * u) * Nat.totient (q * r * s * t * u) >
            (q * r * s * t * u) * 32 :=
    sigma_phi_qrstu_strict hq hr hs ht hu hq3 hr5 hs7 ht11 hu13
      hqr hqs hrs hqt hrt hst hqu hru hsu htu
  have hA_pos : 2 ^ a * (a + 1) > 0 := by positivity
  have h_prod_gt :
      (σ 1 (2 ^ a) * Nat.totient (2 ^ a)) *
      (σ 1 (q * r * s * t * u) * Nat.totient (q * r * s * t * u)) >
      (2 ^ a * (a + 1)) * ((q * r * s * t * u) * 32) := by
    calc (σ 1 (2 ^ a) * Nat.totient (2 ^ a)) *
         (σ 1 (q * r * s * t * u) * Nat.totient (q * r * s * t * u))
        > (2 ^ a * (a + 1)) * (σ 1 (q * r * s * t * u) * Nat.totient (q * r * s * t * u)) :=
          (Nat.mul_lt_mul_right (by positivity)).mpr h1
      _ > (2 ^ a * (a + 1)) * ((q * r * s * t * u) * 32) :=
          (Nat.mul_lt_mul_left hA_pos).mpr h2
  omega

end N6Mathlib
