-- N6.TheoremB_Case4c_FivePrimes : Theorem B case 4c(iv) (n = pqrst, 5 distinct primes)
-- v4 M3_v4 case 4c(iv) (2026-04-16 loop 34)
--
-- 목표: p ≥ 2, q ≥ 3, r ≥ 5, s ≥ 7, t ≥ 11 distinct primes → σφ(pqrst) ≠ pqrst·τ(pqrst)
--
-- 전략 (case 4c(i) pqrs 확장):
--   σ(pqrst) = (p+1)(q+1)(r+1)(s+1)(t+1), φ = ∏(pᵢ-1), τ = 32
--   (p-1)(q-1)(r-1)(s-1)(t-1) ≥ 1·2·4·6·10 = 480
--   (p+1)(q+1)(r+1)(s+1)(t+1) > pqrst (전개)
--   σφ ≥ 480·(p+1)…(t+1) > 480·pqrst > 32·pqrst = nτ  [480 > 32]

import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.NumberTheory.Divisors
import Mathlib.Data.Nat.Totient
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum.Prime
import N6.TheoremB_PrimeCase
import N6.TheoremB_Case4_ThreePrimes
import N6.TheoremB_Case4c_FourPrimes

namespace N6Mathlib

open Nat ArithmeticFunction
open scoped ArithmeticFunction.sigma

/-- (pqrs) coprime with t for 5 distinct primes -/
theorem coprime_quad_prod_prime {p q r s t : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hr : r.Prime) (hs : s.Prime) (ht : t.Prime)
    (hpt : p ≠ t) (hqt : q ≠ t) (hrt : r ≠ t) (hst : s ≠ t) :
    Nat.Coprime (p * q * r * s) t := by
  have h1 : Nat.Coprime p t := coprime_of_distinct_primes hp ht hpt
  have h2 : Nat.Coprime q t := coprime_of_distinct_primes hq ht hqt
  have h3 : Nat.Coprime r t := coprime_of_distinct_primes hr ht hrt
  have h4 : Nat.Coprime s t := coprime_of_distinct_primes hs ht hst
  have h12 : Nat.Coprime (p * q) t := by
    rw [Nat.Coprime, Nat.coprime_comm.mp (Nat.coprime_mul_iff_right.mpr ⟨h1.symm, h2.symm⟩)]
  have h123 : Nat.Coprime (p * q * r) t := by
    rw [Nat.Coprime, Nat.coprime_comm.mp (Nat.coprime_mul_iff_right.mpr ⟨h12.symm, h3.symm⟩)]
  rw [Nat.Coprime, Nat.coprime_comm.mp (Nat.coprime_mul_iff_right.mpr ⟨h123.symm, h4.symm⟩)]

/-- σ(pqrst) = σ(p)·σ(q)·σ(r)·σ(s)·σ(t) -/
theorem sigma_one_pqrst {p q r s t : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hr : r.Prime) (hs : s.Prime) (ht : t.Prime)
    (hpq : p ≠ q) (hpr : p ≠ r) (hqr : q ≠ r)
    (hps : p ≠ s) (hqs : q ≠ s) (hrs : r ≠ s)
    (hpt : p ≠ t) (hqt : q ≠ t) (hrt : r ≠ t) (hst : s ≠ t) :
    σ 1 (p * q * r * s * t) = σ 1 p * σ 1 q * σ 1 r * σ 1 s * σ 1 t := by
  have hcop : Nat.Coprime (p * q * r * s) t :=
    coprime_quad_prod_prime hp hq hr hs ht hpt hqt hrt hst
  have h1 : σ 1 (p * q * r * s * t) = σ 1 (p * q * r * s) * σ 1 t :=
    (isMultiplicative_sigma (k := 1)).right hcop
  rw [h1, sigma_one_pqrs hp hq hr hs hpq hpr hqr hps hqs hrs]

/-- φ(pqrst) = ∏ φ(pᵢ) -/
theorem totient_pqrst {p q r s t : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hr : r.Prime) (hs : s.Prime) (ht : t.Prime)
    (hpq : p ≠ q) (hpr : p ≠ r) (hqr : q ≠ r)
    (hps : p ≠ s) (hqs : q ≠ s) (hrs : r ≠ s)
    (hpt : p ≠ t) (hqt : q ≠ t) (hrt : r ≠ t) (hst : s ≠ t) :
    Nat.totient (p * q * r * s * t) =
      Nat.totient p * Nat.totient q * Nat.totient r * Nat.totient s * Nat.totient t := by
  have hcop : Nat.Coprime (p * q * r * s) t :=
    coprime_quad_prod_prime hp hq hr hs ht hpt hqt hrt hst
  rw [Nat.totient_mul hcop, totient_pqrs hp hq hr hs hpq hpr hqr hps hqs hrs]

/-- τ(pqrst) = 32 -/
theorem tau_pqrst {p q r s t : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hr : r.Prime) (hs : s.Prime) (ht : t.Prime)
    (hpq : p ≠ q) (hpr : p ≠ r) (hqr : q ≠ r)
    (hps : p ≠ s) (hqs : q ≠ s) (hrs : r ≠ s)
    (hpt : p ≠ t) (hqt : q ≠ t) (hrt : r ≠ t) (hst : s ≠ t) :
    (Nat.divisors (p * q * r * s * t)).card = 32 := by
  have hcop : Nat.Coprime (p * q * r * s) t :=
    coprime_quad_prod_prime hp hq hr hs ht hpt hqt hrt hst
  have hσ0 : σ 0 (p * q * r * s * t) = σ 0 (p * q * r * s) * σ 0 t :=
    (isMultiplicative_sigma (k := 0)).right hcop
  have h_left : σ 0 (p * q * r * s * t) = (Nat.divisors (p * q * r * s * t)).card := by
    simp [sigma_zero_apply]
  have h_pqrs_tau : σ 0 (p * q * r * s) = 16 := by
    have h_left' : σ 0 (p * q * r * s) = (Nat.divisors (p * q * r * s)).card := by
      simp [sigma_zero_apply]
    rw [h_left', tau_pqrs hp hq hr hs hpq hpr hqr hps hqs hrs]
  have h_t : σ 0 t = 2 := by
    have := sigma_zero_apply_prime_pow (p := t) (i := 1) ht
    simp at this; exact this
  rw [← h_left, hσ0, h_pqrs_tau, h_t]

/-- Theorem B case 4c(iv): 5 distinct primes → σφ ≠ nτ -/
theorem theorem_B_five_primes {p q r s t : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hr : r.Prime) (hs : s.Prime) (ht : t.Prime)
    (hp2 : p ≥ 2) (hq3 : q ≥ 3) (hr5 : r ≥ 5) (hs7 : s ≥ 7) (ht11 : t ≥ 11)
    (hpq : p ≠ q) (hpr : p ≠ r) (hqr : q ≠ r)
    (hps : p ≠ s) (hqs : q ≠ s) (hrs : r ≠ s)
    (hpt : p ≠ t) (hqt : q ≠ t) (hrt : r ≠ t) (hst : s ≠ t) :
    σ 1 (p * q * r * s * t) * Nat.totient (p * q * r * s * t) ≠
      (p * q * r * s * t) * (Nat.divisors (p * q * r * s * t)).card := by
  rw [sigma_one_pqrst hp hq hr hs ht hpq hpr hqr hps hqs hrs hpt hqt hrt hst]
  rw [totient_pqrst hp hq hr hs ht hpq hpr hqr hps hqs hrs hpt hqt hrt hst]
  rw [tau_pqrst hp hq hr hs ht hpq hpr hqr hps hqs hrs hpt hqt hrt hst]
  rw [sigma_one_prime hp, sigma_one_prime hq, sigma_one_prime hr,
      sigma_one_prime hs, sigma_one_prime ht]
  rw [Nat.totient_prime hp, Nat.totient_prime hq, Nat.totient_prime hr,
      Nat.totient_prime hs, Nat.totient_prime ht]
  intro h
  -- (p-1)(q-1)(r-1)(s-1)(t-1) ≥ 1·2·4·6·10 = 480
  have hp1 : p - 1 ≥ 1 := by omega
  have hq1 : q - 1 ≥ 2 := by omega
  have hr1 : r - 1 ≥ 4 := by omega
  have hs1 : s - 1 ≥ 6 := by omega
  have ht1 : t - 1 ≥ 10 := by omega
  have h_sub5 : (p - 1) * (q - 1) * (r - 1) * (s - 1) * (t - 1) ≥ 480 := by
    have h_pq : (p - 1) * (q - 1) ≥ 2 := by
      calc (p - 1) * (q - 1) ≥ 1 * 2 := Nat.mul_le_mul hp1 hq1
        _ = 2 := by ring
    have h_pqr : (p - 1) * (q - 1) * (r - 1) ≥ 8 := by
      calc (p - 1) * (q - 1) * (r - 1) ≥ 2 * 4 := Nat.mul_le_mul h_pq hr1
        _ = 8 := by ring
    have h_pqrs : (p - 1) * (q - 1) * (r - 1) * (s - 1) ≥ 48 := by
      calc (p - 1) * (q - 1) * (r - 1) * (s - 1) ≥ 8 * 6 := Nat.mul_le_mul h_pqr hs1
        _ = 48 := by ring
    calc (p - 1) * (q - 1) * (r - 1) * (s - 1) * (t - 1) ≥ 48 * 10 :=
        Nat.mul_le_mul h_pqrs ht1
      _ = 480 := by ring
  -- (p+1)(q+1)(r+1)(s+1)(t+1) > pqrst
  have h_add : (p + 1) * (q + 1) * (r + 1) * (s + 1) * (t + 1) > p * q * r * s * t := by
    have h_pq_pos : p * q > 0 := by positivity
    have h_rs_pos : r * s > 0 := by positivity
    have h_pqrs_pos : p * q * r * s > 0 := by positivity
    have h_pq_gt : (p + 1) * (q + 1) > p * q := by nlinarith
    have h_rs_gt : (r + 1) * (s + 1) > r * s := by nlinarith
    have h_t_gt : (t + 1) > t := by omega
    -- (p+1)(q+1) > pq, (r+1)(s+1) > rs, (t+1) > t 곱
    -- ((p+1)(q+1))·((r+1)(s+1))·(t+1) > (pq)·(rs)·t = pqrst
    calc (p + 1) * (q + 1) * (r + 1) * (s + 1) * (t + 1)
        = ((p + 1) * (q + 1)) * ((r + 1) * (s + 1)) * (t + 1) := by ring
      _ > (p * q) * ((r + 1) * (s + 1)) * (t + 1) :=
          (Nat.mul_lt_mul_right (by positivity)).mpr
          ((Nat.mul_lt_mul_right (by nlinarith : (r + 1) * (s + 1) > 0)).mpr h_pq_gt)
      _ > (p * q) * (r * s) * (t + 1) :=
          (Nat.mul_lt_mul_right (by omega : t + 1 > 0)).mpr
          ((Nat.mul_lt_mul_left h_pq_pos).mpr h_rs_gt)
      _ > (p * q) * (r * s) * t :=
          (Nat.mul_lt_mul_left (by positivity)).mpr h_t_gt
      _ = p * q * r * s * t := by ring
  -- σφ ≥ 480·(p+1)(q+1)(r+1)(s+1)(t+1) > 480·pqrst > 32·pqrst = nτ
  have lhs_bound :
      (p + 1) * (q + 1) * (r + 1) * (s + 1) * (t + 1) *
        ((p - 1) * (q - 1) * (r - 1) * (s - 1) * (t - 1)) ≥
        (p + 1) * (q + 1) * (r + 1) * (s + 1) * (t + 1) * 480 :=
    Nat.mul_le_mul_left _ h_sub5
  have rhs_bound :
      (p + 1) * (q + 1) * (r + 1) * (s + 1) * (t + 1) * 480 > p * q * r * s * t * 480 :=
    (Nat.mul_lt_mul_right (by norm_num : (480 : ℕ) > 0)).mpr h_add
  have h_480_32 : p * q * r * s * t * 480 > p * q * r * s * t * 32 := by
    have h_pos : p * q * r * s * t > 0 := by positivity
    nlinarith
  omega

-- 확인 예시
-- n = 2310 = 2·3·5·7·11: σ=6912, φ=480, τ=32
-- σφ = 6912·480 = 3317760, nτ = 2310·32 = 73920, 비율 44.9× ✓

end N6Mathlib
