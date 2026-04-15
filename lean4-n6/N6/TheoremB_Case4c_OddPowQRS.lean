-- N6.TheoremB_Case4c_OddPowQRS : Theorem B case 4c(xii) (n = p^a·q·r·s, all odd)
-- v4 M3_v4 case 4c(xii) (2026-04-16 loop 41)
--
-- 목표: p, q, r, s odd prime distinct, p ≥ 3, q ≥ 3, r ≥ 5, s ≥ 7, a ≥ 2
--       → σφ(p^a·q·r·s) ≠ nτ
--
-- 전략 (case 4c(iii) 2^a·qrs 의 odd prime power 버전):
--   σφ(p^a) > p^a·(a+1)  generic (sigma_phi_prime_pow_strict, loop 19)
--   σφ(qrs) > qrs·8      (sigma_phi_qrs_strict, loop 13 — for q,r,s odd ≥ 3,5,7)
--   곱: σφ(n) > p^a(a+1)·qrs·8 = nτ(n) STRICT

import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.NumberTheory.Divisors
import Mathlib.Data.Nat.Totient
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum.Prime
import N6.TheoremB_PrimeCase
import N6.TheoremB_Case3_PrimePow
import N6.TheoremB_Case4_ThreePrimes
import N6.TheoremB_Case4c_TwoPowQRS
import N6.TheoremB_Case4c_OddPowQR

namespace N6Mathlib

open Nat ArithmeticFunction
open scoped ArithmeticFunction.sigma

/-- Coprime p^a and (q·r·s) for p distinct from q, r, s -/
theorem coprime_ppow_qrs {p q r s a : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hr : r.Prime) (hs : s.Prime)
    (hpq : p ≠ q) (hpr : p ≠ r) (hps : p ≠ s) :
    Nat.Coprime (p ^ a) (q * r * s) := by
  have hpq_cop : Nat.Coprime p q := (Nat.coprime_primes hp hq).mpr hpq
  have hpr_cop : Nat.Coprime p r := (Nat.coprime_primes hp hr).mpr hpr
  have hps_cop : Nat.Coprime p s := (Nat.coprime_primes hp hs).mpr hps
  have hp_qr : Nat.Coprime p (q * r) := Nat.Coprime.mul_right hpq_cop hpr_cop
  have hp_qrs : Nat.Coprime p (q * r * s) := Nat.Coprime.mul_right hp_qr hps_cop
  exact hp_qrs.pow_left a

/-- Theorem B case 4c(xii): n = p^a·q·r·s, 4 odd distinct, a ≥ 2 → σφ ≠ nτ -/
theorem theorem_B_odd_ppow_qrs {p q r s a : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hr : r.Prime) (hs : s.Prime)
    (hp3 : p ≥ 3) (hq3 : q ≥ 3) (hr5 : r ≥ 5) (hs7 : s ≥ 7)
    (hpq : p ≠ q) (hpr : p ≠ r) (hps : p ≠ s)
    (hqr : q ≠ r) (hqs : q ≠ s) (hrs : r ≠ s)
    (ha : a ≥ 2) :
    σ 1 (p ^ a * (q * r * s)) * Nat.totient (p ^ a * (q * r * s)) ≠
      (p ^ a * (q * r * s)) * (Nat.divisors (p ^ a * (q * r * s))).card := by
  have hcop : Nat.Coprime (p ^ a) (q * r * s) := coprime_ppow_qrs hp hq hr hs hpq hpr hps
  have hσ : σ 1 (p ^ a * (q * r * s)) = σ 1 (p ^ a) * σ 1 (q * r * s) :=
    (isMultiplicative_sigma (k := 1)).right hcop
  have hφ : Nat.totient (p ^ a * (q * r * s)) =
            Nat.totient (p ^ a) * Nat.totient (q * r * s) :=
    Nat.totient_mul hcop
  have hσ0 : σ 0 (p ^ a * (q * r * s)) = σ 0 (p ^ a) * σ 0 (q * r * s) :=
    (isMultiplicative_sigma (k := 0)).right hcop
  have hτ : (Nat.divisors (p ^ a * (q * r * s))).card = (a + 1) * 8 := by
    have h_left : σ 0 (p ^ a * (q * r * s)) = (Nat.divisors (p ^ a * (q * r * s))).card := by
      simp [sigma_zero_apply]
    have h_qrs : σ 0 (q * r * s) = 8 := by
      have h_left' : σ 0 (q * r * s) = (Nat.divisors (q * r * s)).card := by
        simp [sigma_zero_apply]
      rw [h_left', tau_pqr hq hr hs hqr hqs hrs]
    rw [← h_left, hσ0, sigma_zero_apply_prime_pow hp, h_qrs]
  rw [hσ, hφ, hτ]
  intro h
  have reorg_lhs :
      σ 1 (p ^ a) * σ 1 (q * r * s) *
        (Nat.totient (p ^ a) * Nat.totient (q * r * s))
      = (σ 1 (p ^ a) * Nat.totient (p ^ a)) *
        (σ 1 (q * r * s) * Nat.totient (q * r * s)) := by ring
  have reorg_rhs :
      p ^ a * (q * r * s) * ((a + 1) * 8) = (p ^ a * (a + 1)) * ((q * r * s) * 8) := by ring
  rw [reorg_lhs, reorg_rhs] at h
  have h1 : σ 1 (p ^ a) * Nat.totient (p ^ a) > p ^ a * (a + 1) :=
    sigma_phi_prime_pow_strict hp (by omega : p ≥ 2) ha
  have h2 : σ 1 (q * r * s) * Nat.totient (q * r * s) > (q * r * s) * 8 :=
    sigma_phi_qrs_strict hq hr hs hq3 hr5 hs7 hqr hqs hrs
  have hA_pos : p ^ a * (a + 1) > 0 := by positivity
  have h_prod_gt :
      (σ 1 (p ^ a) * Nat.totient (p ^ a)) * (σ 1 (q * r * s) * Nat.totient (q * r * s)) >
      (p ^ a * (a + 1)) * ((q * r * s) * 8) := by
    calc (σ 1 (p ^ a) * Nat.totient (p ^ a)) * (σ 1 (q * r * s) * Nat.totient (q * r * s))
        > (p ^ a * (a + 1)) * (σ 1 (q * r * s) * Nat.totient (q * r * s)) :=
          (Nat.mul_lt_mul_right (by positivity)).mpr h1
      _ > (p ^ a * (a + 1)) * ((q * r * s) * 8) :=
          (Nat.mul_lt_mul_left hA_pos).mpr h2
  omega

-- 확인 예시
-- n = 9·5·7·11 = 3465: σ=13·6·8·12=7488, φ=6·4·6·10=1440, τ=3·2·2·2=24
-- σφ=10,782,720, nτ=83160, 비율 130× ✓

end N6Mathlib
