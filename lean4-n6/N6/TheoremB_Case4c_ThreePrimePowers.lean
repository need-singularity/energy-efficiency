-- N6.TheoremB_Case4c_ThreePrimePowers : Theorem B case 4c(x) (n = p^a·q^b·r^c, all ≥ 2)
-- v4 M3_v4 case 4c(x) (2026-04-16 loop 39)
--
-- 목표: p, q, r distinct primes, a, b, c ≥ 2 → σφ(p^a·q^b·r^c) ≠ nτ(n)
--
-- 전략 (3 generic strict 곱):
--   σφ(p^a) > p^a·(a+1)   from sigma_phi_prime_pow_strict (loop 19, generic p prime ≥ 2, a ≥ 2)
--   σφ(q^b) > q^b·(b+1)
--   σφ(r^c) > r^c·(c+1)
--   곱: σφ(n) > p^a·q^b·r^c·(a+1)(b+1)(c+1) = nτ(n)  STRICT
--
-- 이 정리는 ω=3 with **all** prime powers ≥ 2 (2, odd 섞임 포함) 영역을 한 번에 커버한다.

import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.NumberTheory.Divisors
import Mathlib.Data.Nat.Totient
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum.Prime
import N6.TheoremB_PrimeCase
import N6.TheoremB_Case3_PrimePow
import N6.TheoremB_Case4_ThreePrimes
import N6.TheoremB_Case4c_OddPowQR

namespace N6Mathlib

open Nat ArithmeticFunction
open scoped ArithmeticFunction.sigma

/-- Coprime (p^a·q^b) and r^c for distinct primes -/
theorem coprime_ppow_qpow_rpow {p q r a b c : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hr : r.Prime)
    (hpq : p ≠ q) (hpr : p ≠ r) (hqr : q ≠ r) :
    Nat.Coprime (p ^ a * q ^ b) (r ^ c) := by
  have hpr_cop : Nat.Coprime p r := (Nat.coprime_primes hp hr).mpr hpr
  have hqr_cop : Nat.Coprime q r := (Nat.coprime_primes hq hr).mpr hqr
  have h_pa_rc : Nat.Coprime (p ^ a) (r ^ c) := (hpr_cop.pow_left a).pow_right c
  have h_qb_rc : Nat.Coprime (q ^ b) (r ^ c) := (hqr_cop.pow_left b).pow_right c
  rw [Nat.Coprime, Nat.coprime_comm.mp
    (Nat.coprime_mul_iff_right.mpr ⟨h_pa_rc.symm, h_qb_rc.symm⟩)]

/-- Coprime p^a and q^b for distinct primes -/
theorem coprime_ppow_qpow_gen {p q a b : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hpq : p ≠ q) :
    Nat.Coprime (p ^ a) (q ^ b) := by
  have hpq_cop : Nat.Coprime p q := (Nat.coprime_primes hp hq).mpr hpq
  exact (hpq_cop.pow_left a).pow_right b

/-- Theorem B case 4c(x): n = p^a·q^b·r^c, all ≥ 2, 3 distinct primes → σφ ≠ nτ -/
theorem theorem_B_three_prime_powers {p q r a b c : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hr : r.Prime)
    (hp2 : p ≥ 2) (hq2 : q ≥ 2) (hr2 : r ≥ 2)
    (hpq : p ≠ q) (hpr : p ≠ r) (hqr : q ≠ r)
    (ha : a ≥ 2) (hb : b ≥ 2) (hc : c ≥ 2) :
    σ 1 (p ^ a * q ^ b * r ^ c) * Nat.totient (p ^ a * q ^ b * r ^ c) ≠
      (p ^ a * q ^ b * r ^ c) * (Nat.divisors (p ^ a * q ^ b * r ^ c)).card := by
  have hcop_main : Nat.Coprime (p ^ a * q ^ b) (r ^ c) :=
    coprime_ppow_qpow_rpow hp hq hr hpq hpr hqr
  have hcop_pq : Nat.Coprime (p ^ a) (q ^ b) :=
    coprime_ppow_qpow_gen hp hq hpq
  have hσ : σ 1 (p ^ a * q ^ b * r ^ c) = σ 1 (p ^ a * q ^ b) * σ 1 (r ^ c) :=
    (isMultiplicative_sigma (k := 1)).right hcop_main
  have hσ_inner : σ 1 (p ^ a * q ^ b) = σ 1 (p ^ a) * σ 1 (q ^ b) :=
    (isMultiplicative_sigma (k := 1)).right hcop_pq
  have hφ : Nat.totient (p ^ a * q ^ b * r ^ c) =
            Nat.totient (p ^ a * q ^ b) * Nat.totient (r ^ c) :=
    Nat.totient_mul hcop_main
  have hφ_inner : Nat.totient (p ^ a * q ^ b) =
                  Nat.totient (p ^ a) * Nat.totient (q ^ b) :=
    Nat.totient_mul hcop_pq
  have hτ : (Nat.divisors (p ^ a * q ^ b * r ^ c)).card = (a + 1) * (b + 1) * (c + 1) := by
    have hσ0 : σ 0 (p ^ a * q ^ b * r ^ c) = σ 0 (p ^ a * q ^ b) * σ 0 (r ^ c) :=
      (isMultiplicative_sigma (k := 0)).right hcop_main
    have hσ0_inner : σ 0 (p ^ a * q ^ b) = σ 0 (p ^ a) * σ 0 (q ^ b) :=
      (isMultiplicative_sigma (k := 0)).right hcop_pq
    have h_left : σ 0 (p ^ a * q ^ b * r ^ c) = (Nat.divisors (p ^ a * q ^ b * r ^ c)).card := by
      simp [sigma_zero_apply]
    rw [← h_left, hσ0, hσ0_inner,
        sigma_zero_apply_prime_pow hp,
        sigma_zero_apply_prime_pow hq,
        sigma_zero_apply_prime_pow hr]
  rw [hσ, hσ_inner, hφ, hφ_inner, hτ]
  intro h
  have reorg_lhs :
      σ 1 (p ^ a) * σ 1 (q ^ b) * σ 1 (r ^ c) *
        (Nat.totient (p ^ a) * Nat.totient (q ^ b) * Nat.totient (r ^ c))
      = (σ 1 (p ^ a) * Nat.totient (p ^ a)) *
        (σ 1 (q ^ b) * Nat.totient (q ^ b)) *
        (σ 1 (r ^ c) * Nat.totient (r ^ c)) := by ring
  have reorg_rhs :
      p ^ a * q ^ b * r ^ c * ((a + 1) * (b + 1) * (c + 1))
      = (p ^ a * (a + 1)) * (q ^ b * (b + 1)) * (r ^ c * (c + 1)) := by ring
  rw [reorg_lhs, reorg_rhs] at h
  have h1 : σ 1 (p ^ a) * Nat.totient (p ^ a) > p ^ a * (a + 1) :=
    sigma_phi_prime_pow_strict hp hp2 ha
  have h2 : σ 1 (q ^ b) * Nat.totient (q ^ b) > q ^ b * (b + 1) :=
    sigma_phi_prime_pow_strict hq hq2 hb
  have h3 : σ 1 (r ^ c) * Nat.totient (r ^ c) > r ^ c * (c + 1) :=
    sigma_phi_prime_pow_strict hr hr2 hc
  have hA_pos : p ^ a * (a + 1) > 0 := by positivity
  have hB_pos : q ^ b * (b + 1) > 0 := by positivity
  have h_prod_gt :
      (σ 1 (p ^ a) * Nat.totient (p ^ a)) *
      (σ 1 (q ^ b) * Nat.totient (q ^ b)) *
      (σ 1 (r ^ c) * Nat.totient (r ^ c)) >
      (p ^ a * (a + 1)) * (q ^ b * (b + 1)) * (r ^ c * (c + 1)) := by
    calc (σ 1 (p ^ a) * Nat.totient (p ^ a)) *
         (σ 1 (q ^ b) * Nat.totient (q ^ b)) *
         (σ 1 (r ^ c) * Nat.totient (r ^ c))
        > (p ^ a * (a + 1)) *
          (σ 1 (q ^ b) * Nat.totient (q ^ b)) *
          (σ 1 (r ^ c) * Nat.totient (r ^ c)) :=
          (Nat.mul_lt_mul_right (by positivity)).mpr
          ((Nat.mul_lt_mul_right (by positivity)).mpr h1)
      _ > (p ^ a * (a + 1)) * (q ^ b * (b + 1)) * (σ 1 (r ^ c) * Nat.totient (r ^ c)) :=
          (Nat.mul_lt_mul_right (by positivity)).mpr
          ((Nat.mul_lt_mul_left hA_pos).mpr h2)
      _ > (p ^ a * (a + 1)) * (q ^ b * (b + 1)) * (r ^ c * (c + 1)) :=
          (Nat.mul_lt_mul_left (by positivity)).mpr h3
  omega

-- 확인 예시
-- n = 4·9·25 = 900: σ=2821, φ=240, τ=27. σφ=677040, nτ=24300, 비율 27.9× ✓
-- n = 8·9·25 = 1800: σ=6045, φ=480, τ=36. σφ=2901600, nτ=64800, 비율 44.8× ✓

end N6Mathlib
