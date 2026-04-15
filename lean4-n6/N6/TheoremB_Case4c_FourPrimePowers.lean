-- N6.TheoremB_Case4c_FourPrimePowers : Theorem B case 4c(xvii) (n = p^a·q^b·r^c·s^d, all ≥ 2)
-- v4 M3_v4 case 4c(xvii) (2026-04-16 loop 47)
--
-- 목표: p,q,r,s distinct primes ≥ 2, a,b,c,d ≥ 2 → σφ(p^a·q^b·r^c·s^d) ≠ nτ
--
-- 전략 (4 generic strict 곱, sigma_phi_prime_pow_strict 4번):
--   σφ(p^a) > p^a(a+1), σφ(q^b) > q^b(b+1), σφ(r^c) > r^c(c+1), σφ(s^d) > s^d(d+1)
--   곱: σφ(n) > p^a·q^b·r^c·s^d · (a+1)(b+1)(c+1)(d+1) = nτ(n) STRICT

import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.NumberTheory.Divisors
import Mathlib.Data.Nat.Totient
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum.Prime
import N6.TheoremB_PrimeCase
import N6.TheoremB_Case3_PrimePow
import N6.TheoremB_Case4c_ThreePrimePowers
import N6.TheoremB_Case4c_OddPowQR

namespace N6Mathlib

open Nat ArithmeticFunction
open scoped ArithmeticFunction.sigma

set_option maxHeartbeats 800000

/-- Coprime (p^a·q^b·r^c) and s^d for 4 distinct primes -/
theorem coprime_three_prime_pows_s {p q r s a b c d : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hr : r.Prime) (hs : s.Prime)
    (hps : p ≠ s) (hqs : q ≠ s) (hrs : r ≠ s) :
    Nat.Coprime (p ^ a * q ^ b * r ^ c) (s ^ d) := by
  have hps_cop : Nat.Coprime p s := (Nat.coprime_primes hp hs).mpr hps
  have hqs_cop : Nat.Coprime q s := (Nat.coprime_primes hq hs).mpr hqs
  have hrs_cop : Nat.Coprime r s := (Nat.coprime_primes hr hs).mpr hrs
  have h_pa_sd : Nat.Coprime (p ^ a) (s ^ d) := (hps_cop.pow_left a).pow_right d
  have h_qb_sd : Nat.Coprime (q ^ b) (s ^ d) := (hqs_cop.pow_left b).pow_right d
  have h_rc_sd : Nat.Coprime (r ^ c) (s ^ d) := (hrs_cop.pow_left c).pow_right d
  have h_pq_sd : Nat.Coprime (p ^ a * q ^ b) (s ^ d) := by
    rw [Nat.Coprime, Nat.coprime_comm.mp
      (Nat.coprime_mul_iff_right.mpr ⟨h_pa_sd.symm, h_qb_sd.symm⟩)]
  rw [Nat.Coprime, Nat.coprime_comm.mp
    (Nat.coprime_mul_iff_right.mpr ⟨h_pq_sd.symm, h_rc_sd.symm⟩)]

/-- Theorem B case 4c(xvii): 4 distinct primes, all powers ≥ 2 → σφ ≠ nτ -/
theorem theorem_B_four_prime_powers {p q r s a b c d : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hr : r.Prime) (hs : s.Prime)
    (hp2 : p ≥ 2) (hq2 : q ≥ 2) (hr2 : r ≥ 2) (hs2 : s ≥ 2)
    (hpq : p ≠ q) (hpr : p ≠ r) (hps : p ≠ s)
    (hqr : q ≠ r) (hqs : q ≠ s) (hrs : r ≠ s)
    (ha : a ≥ 2) (hb : b ≥ 2) (hc : c ≥ 2) (hd : d ≥ 2) :
    σ 1 (p ^ a * q ^ b * r ^ c * s ^ d) *
      Nat.totient (p ^ a * q ^ b * r ^ c * s ^ d) ≠
    (p ^ a * q ^ b * r ^ c * s ^ d) *
      (Nat.divisors (p ^ a * q ^ b * r ^ c * s ^ d)).card := by
  have hcop_main : Nat.Coprime (p ^ a * q ^ b * r ^ c) (s ^ d) :=
    coprime_three_prime_pows_s hp hq hr hs hps hqs hrs
  have hcop_3 : Nat.Coprime (p ^ a * q ^ b) (r ^ c) :=
    coprime_ppow_qpow_rpow hp hq hr hpq hpr hqr
  have hcop_pq : Nat.Coprime (p ^ a) (q ^ b) :=
    coprime_ppow_qpow_gen hp hq hpq
  have hσ : σ 1 (p ^ a * q ^ b * r ^ c * s ^ d) =
            σ 1 (p ^ a * q ^ b * r ^ c) * σ 1 (s ^ d) :=
    (isMultiplicative_sigma (k := 1)).right hcop_main
  have hσ_3 : σ 1 (p ^ a * q ^ b * r ^ c) =
              σ 1 (p ^ a * q ^ b) * σ 1 (r ^ c) :=
    (isMultiplicative_sigma (k := 1)).right hcop_3
  have hσ_pq : σ 1 (p ^ a * q ^ b) = σ 1 (p ^ a) * σ 1 (q ^ b) :=
    (isMultiplicative_sigma (k := 1)).right hcop_pq
  have hφ : Nat.totient (p ^ a * q ^ b * r ^ c * s ^ d) =
            Nat.totient (p ^ a * q ^ b * r ^ c) * Nat.totient (s ^ d) :=
    Nat.totient_mul hcop_main
  have hφ_3 : Nat.totient (p ^ a * q ^ b * r ^ c) =
              Nat.totient (p ^ a * q ^ b) * Nat.totient (r ^ c) :=
    Nat.totient_mul hcop_3
  have hφ_pq : Nat.totient (p ^ a * q ^ b) =
               Nat.totient (p ^ a) * Nat.totient (q ^ b) :=
    Nat.totient_mul hcop_pq
  have hτ : (Nat.divisors (p ^ a * q ^ b * r ^ c * s ^ d)).card =
            (a + 1) * (b + 1) * (c + 1) * (d + 1) := by
    have hσ0 : σ 0 (p ^ a * q ^ b * r ^ c * s ^ d) =
               σ 0 (p ^ a * q ^ b * r ^ c) * σ 0 (s ^ d) :=
      (isMultiplicative_sigma (k := 0)).right hcop_main
    have hσ0_3 : σ 0 (p ^ a * q ^ b * r ^ c) =
                 σ 0 (p ^ a * q ^ b) * σ 0 (r ^ c) :=
      (isMultiplicative_sigma (k := 0)).right hcop_3
    have hσ0_pq : σ 0 (p ^ a * q ^ b) = σ 0 (p ^ a) * σ 0 (q ^ b) :=
      (isMultiplicative_sigma (k := 0)).right hcop_pq
    have h_left : σ 0 (p ^ a * q ^ b * r ^ c * s ^ d) =
                  (Nat.divisors (p ^ a * q ^ b * r ^ c * s ^ d)).card := by
      simp [sigma_zero_apply]
    rw [← h_left, hσ0, hσ0_3, hσ0_pq,
        sigma_zero_apply_prime_pow hp,
        sigma_zero_apply_prime_pow hq,
        sigma_zero_apply_prime_pow hr,
        sigma_zero_apply_prime_pow hs]
  rw [hσ, hσ_3, hσ_pq, hφ, hφ_3, hφ_pq, hτ]
  intro h
  have reorg_lhs :
      σ 1 (p ^ a) * σ 1 (q ^ b) * σ 1 (r ^ c) * σ 1 (s ^ d) *
        (Nat.totient (p ^ a) * Nat.totient (q ^ b) * Nat.totient (r ^ c) *
         Nat.totient (s ^ d))
      = (σ 1 (p ^ a) * Nat.totient (p ^ a)) *
        (σ 1 (q ^ b) * Nat.totient (q ^ b)) *
        (σ 1 (r ^ c) * Nat.totient (r ^ c)) *
        (σ 1 (s ^ d) * Nat.totient (s ^ d)) := by ring
  have reorg_rhs :
      p ^ a * q ^ b * r ^ c * s ^ d * ((a + 1) * (b + 1) * (c + 1) * (d + 1))
      = (p ^ a * (a + 1)) * (q ^ b * (b + 1)) * (r ^ c * (c + 1)) *
        (s ^ d * (d + 1)) := by ring
  rw [reorg_lhs, reorg_rhs] at h
  have h1 : σ 1 (p ^ a) * Nat.totient (p ^ a) > p ^ a * (a + 1) :=
    sigma_phi_prime_pow_strict hp hp2 ha
  have h2 : σ 1 (q ^ b) * Nat.totient (q ^ b) > q ^ b * (b + 1) :=
    sigma_phi_prime_pow_strict hq hq2 hb
  have h3 : σ 1 (r ^ c) * Nat.totient (r ^ c) > r ^ c * (c + 1) :=
    sigma_phi_prime_pow_strict hr hr2 hc
  have h4 : σ 1 (s ^ d) * Nat.totient (s ^ d) > s ^ d * (d + 1) :=
    sigma_phi_prime_pow_strict hs hs2 hd
  have hA_pos : p ^ a * (a + 1) > 0 := by positivity
  have hB_pos : q ^ b * (b + 1) > 0 := by positivity
  have hC_pos : r ^ c * (c + 1) > 0 := by positivity
  -- Chain 4 strict bounds
  have h_prod_gt :
      (σ 1 (p ^ a) * Nat.totient (p ^ a)) *
      (σ 1 (q ^ b) * Nat.totient (q ^ b)) *
      (σ 1 (r ^ c) * Nat.totient (r ^ c)) *
      (σ 1 (s ^ d) * Nat.totient (s ^ d)) >
      (p ^ a * (a + 1)) * (q ^ b * (b + 1)) *
      (r ^ c * (c + 1)) * (s ^ d * (d + 1)) := by
    calc (σ 1 (p ^ a) * Nat.totient (p ^ a)) *
         (σ 1 (q ^ b) * Nat.totient (q ^ b)) *
         (σ 1 (r ^ c) * Nat.totient (r ^ c)) *
         (σ 1 (s ^ d) * Nat.totient (s ^ d))
        > (p ^ a * (a + 1)) *
          (σ 1 (q ^ b) * Nat.totient (q ^ b)) *
          (σ 1 (r ^ c) * Nat.totient (r ^ c)) *
          (σ 1 (s ^ d) * Nat.totient (s ^ d)) :=
          (Nat.mul_lt_mul_right (by positivity)).mpr
          ((Nat.mul_lt_mul_right (by positivity)).mpr
          ((Nat.mul_lt_mul_right (by positivity)).mpr h1))
      _ > (p ^ a * (a + 1)) * (q ^ b * (b + 1)) *
          (σ 1 (r ^ c) * Nat.totient (r ^ c)) *
          (σ 1 (s ^ d) * Nat.totient (s ^ d)) :=
          (Nat.mul_lt_mul_right (by positivity)).mpr
          ((Nat.mul_lt_mul_right (by positivity)).mpr
          ((Nat.mul_lt_mul_left hA_pos).mpr h2))
      _ > (p ^ a * (a + 1)) * (q ^ b * (b + 1)) * (r ^ c * (c + 1)) *
          (σ 1 (s ^ d) * Nat.totient (s ^ d)) :=
          (Nat.mul_lt_mul_right (by positivity)).mpr
          ((Nat.mul_lt_mul_left (by positivity)).mpr h3)
      _ > (p ^ a * (a + 1)) * (q ^ b * (b + 1)) * (r ^ c * (c + 1)) *
          (s ^ d * (d + 1)) :=
          (Nat.mul_lt_mul_left (by positivity)).mpr h4
  omega

end N6Mathlib
