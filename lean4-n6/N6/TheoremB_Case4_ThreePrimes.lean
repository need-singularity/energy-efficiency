-- N6.TheoremB_Case4_ThreePrimes : Theorem B case 4a (n = pqr, 3 distinct primes)
-- v4 M3_v4 case 4a (2026-04-16 loop 26)
--
-- 목표: p, q, r distinct primes → σ(pqr)·φ(pqr) ≠ pqr·τ(pqr)
-- 전략:
--   σ(pqr) = (p+1)(q+1)(r+1), φ(pqr) = (p-1)(q-1)(r-1), τ(pqr) = 8
--   σ·φ = (p²-1)(q²-1)(r²-1), nτ = 8pqr
--   p,q,r 모두 ≥ 2 distinct: min {p,q,r} = 2, next ≥ 3, next ≥ 5
--   (p²-1)(q²-1)(r²-1) ≥ 3·8·24 = 576, 8pqr ≥ 8·2·3·5 = 240
--   하지만 단순 비교 부족 — 구조적 증명:
--     (p²-1)(q²-1)(r²-1) / (pqr) = (p-1/p)(q-1/q)(r-1/r) · 8/8 = ...
--   직접: (p+1)(p-1) ≥ 2p (for p ≥ 2), so (p²-1)(q²-1)(r²-1) ≥ 2p·2q·2r · some_factor
--   보다 깔끔: (p-1)(q-1)(r-1) ≥ 1·2·4 = 8, (p+1)(q+1)(r+1) ≥ 3·4·6 = 72
--   σφ = (p+1)(q+1)(r+1) · (p-1)(q-1)(r-1) ≥ 72 · 8 = 576
--   nτ = 8pqr ≤ 8·largest products
--   Cleaner: (p+1)(q+1)(r+1) > pqr (by expansion), and (p-1)(q-1)(r-1) ≥ 8 (since distinct primes)
--   So σφ > pqr · 8 = nτ

import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.NumberTheory.Divisors
import Mathlib.Data.Nat.Totient
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum.Prime
import N6.TheoremB_PrimeCase

namespace N6Mathlib

open Nat ArithmeticFunction
open scoped ArithmeticFunction.sigma

/-- 세 소수 중 두 쌍 서로소 (Nat.Coprime) -/
theorem coprime_of_distinct_primes {p q : ℕ} (hp : p.Prime) (hq : q.Prime) (hpq : p ≠ q) :
    Nat.Coprime p q :=
  (Nat.coprime_primes hp hq).mpr hpq

/-- p·q 와 r 가 coprime (p≠r, q≠r 모두 서로소) -/
theorem coprime_prod_prime {p q r : ℕ} (hp : p.Prime) (hq : q.Prime) (hr : r.Prime)
    (hpr : p ≠ r) (hqr : q ≠ r) : Nat.Coprime (p * q) r := by
  rw [Nat.Coprime, Nat.coprime_comm.mp (Nat.coprime_mul_iff_right.mpr
    ⟨(coprime_of_distinct_primes hp hr hpr).symm, (coprime_of_distinct_primes hq hr hqr).symm⟩)]

/-- σ(pqr) = σ(p)·σ(q)·σ(r) for pairwise distinct primes -/
theorem sigma_one_pqr {p q r : ℕ} (hp : p.Prime) (hq : q.Prime) (hr : r.Prime)
    (hpq : p ≠ q) (hpr : p ≠ r) (hqr : q ≠ r) :
    σ 1 (p * q * r) = σ 1 p * σ 1 q * σ 1 r := by
  have hpq_cop : Nat.Coprime p q := coprime_of_distinct_primes hp hq hpq
  have hpqr_cop : Nat.Coprime (p * q) r := coprime_prod_prime hp hq hr hpr hqr
  have h1 : σ 1 (p * q * r) = σ 1 (p * q) * σ 1 r :=
    (isMultiplicative_sigma (k := 1)).right hpqr_cop
  have h2 : σ 1 (p * q) = σ 1 p * σ 1 q :=
    (isMultiplicative_sigma (k := 1)).right hpq_cop
  rw [h1, h2]

/-- φ(pqr) = φ(p)·φ(q)·φ(r) for pairwise distinct primes -/
theorem totient_pqr {p q r : ℕ} (hp : p.Prime) (hq : q.Prime) (hr : r.Prime)
    (hpq : p ≠ q) (hpr : p ≠ r) (hqr : q ≠ r) :
    Nat.totient (p * q * r) = Nat.totient p * Nat.totient q * Nat.totient r := by
  have hpq_cop : Nat.Coprime p q := coprime_of_distinct_primes hp hq hpq
  have hpqr_cop : Nat.Coprime (p * q) r := coprime_prod_prime hp hq hr hpr hqr
  rw [Nat.totient_mul hpqr_cop, Nat.totient_mul hpq_cop]

/-- τ(pqr) = 8 for pairwise distinct primes -/
theorem tau_pqr {p q r : ℕ} (hp : p.Prime) (hq : q.Prime) (hr : r.Prime)
    (hpq : p ≠ q) (hpr : p ≠ r) (hqr : q ≠ r) :
    (Nat.divisors (p * q * r)).card = 8 := by
  have hpq_cop : Nat.Coprime p q := coprime_of_distinct_primes hp hq hpq
  have hpqr_cop : Nat.Coprime (p * q) r := coprime_prod_prime hp hq hr hpr hqr
  have h1 : σ 0 (p * q * r) = σ 0 (p * q) * σ 0 r :=
    (isMultiplicative_sigma (k := 0)).right hpqr_cop
  have h2 : σ 0 (p * q) = σ 0 p * σ 0 q :=
    (isMultiplicative_sigma (k := 0)).right hpq_cop
  have h_left : σ 0 (p * q * r) = (Nat.divisors (p * q * r)).card := by
    simp [sigma_zero_apply]
  have h_p : σ 0 p = 2 := by
    have := sigma_zero_apply_prime_pow (p := p) (i := 1) hp; simp at this; exact this
  have h_q : σ 0 q = 2 := by
    have := sigma_zero_apply_prime_pow (p := q) (i := 1) hq; simp at this; exact this
  have h_r : σ 0 r = 2 := by
    have := sigma_zero_apply_prime_pow (p := r) (i := 1) hr; simp at this; exact this
  rw [← h_left, h1, h2, h_p, h_q, h_r]

/-- Theorem B case 4a: p < q < r distinct primes → σ(pqr)·φ(pqr) ≠ pqr·τ(pqr)
    (ordered 가정은 증명 편의상. 교환 후 대칭성) -/
theorem theorem_B_three_primes {p q r : ℕ} (hp : p.Prime) (hq : q.Prime) (hr : r.Prime)
    (hp2 : p ≥ 2) (hq3 : q ≥ 3) (hr5 : r ≥ 5)
    (hpq : p ≠ q) (hpr : p ≠ r) (hqr : q ≠ r) :
    σ 1 (p * q * r) * Nat.totient (p * q * r) ≠ (p * q * r) * (Nat.divisors (p * q * r)).card := by
  rw [sigma_one_pqr hp hq hr hpq hpr hqr]
  rw [totient_pqr hp hq hr hpq hpr hqr]
  rw [tau_pqr hp hq hr hpq hpr hqr]
  rw [sigma_one_prime hp, sigma_one_prime hq, sigma_one_prime hr]
  rw [Nat.totient_prime hp, Nat.totient_prime hq, Nat.totient_prime hr]
  -- Goal: (p+1)(q+1)(r+1) * ((p-1)(q-1)(r-1)) ≠ p*q*r * 8
  -- 전략:
  --   (p+1)(q+1)(r+1) > pqr (곱 전개 후 양의 항)
  --   (p-1)(q-1)(r-1) ≥ 1·2·4 = 8 (p≥2, q≥3, r≥5)
  --   ⟹ σφ ≥ 8·(p+1)(q+1)(r+1) > 8pqr = nτ
  intro h
  -- Key: (p-1)(q-1)(r-1) ≥ 8
  have hp1 : p - 1 ≥ 1 := by omega
  have hq1 : q - 1 ≥ 2 := by omega
  have hr1 : r - 1 ≥ 4 := by omega
  have h_pq_sub : (p - 1) * (q - 1) ≥ 1 * 2 := Nat.mul_le_mul hp1 hq1
  have h_sub : (p - 1) * (q - 1) * (r - 1) ≥ 2 * 4 := by
    have : (p - 1) * (q - 1) * (r - 1) ≥ 2 * (r - 1) :=
      Nat.mul_le_mul_right (r - 1) (by omega : (1 : ℕ) * 2 ≤ (p - 1) * (q - 1)) |>.trans_eq (by ring)
    have : (p - 1) * (q - 1) * (r - 1) ≥ 2 * (r - 1) := by
      calc (p - 1) * (q - 1) * (r - 1) ≥ (1 * 2) * (r - 1) :=
            Nat.mul_le_mul_right (r - 1) h_pq_sub
        _ = 2 * (r - 1) := by ring
    calc (p - 1) * (q - 1) * (r - 1) ≥ 2 * (r - 1) := this
      _ ≥ 2 * 4 := Nat.mul_le_mul_left 2 hr1
  -- Key: (p+1)(q+1)(r+1) > pqr
  have hp3 : p + 1 ≥ 3 := by omega
  have hq4 : q + 1 ≥ 4 := by omega
  have hr6 : r + 1 ≥ 6 := by omega
  have h_add : (p + 1) * (q + 1) * (r + 1) > p * q * r := by nlinarith
  -- 합쳐서 σφ > 8pqr
  have lhs_bound :
      (p + 1) * (q + 1) * (r + 1) * ((p - 1) * (q - 1) * (r - 1)) ≥
        (p + 1) * (q + 1) * (r + 1) * 8 :=
    Nat.mul_le_mul_left ((p + 1) * (q + 1) * (r + 1)) h_sub
  have rhs_bound :
      (p + 1) * (q + 1) * (r + 1) * 8 > p * q * r * 8 := by
    have h8 : (8 : ℕ) > 0 := by norm_num
    exact (Nat.mul_lt_mul_right h8).mpr h_add
  -- h : LHS = p*q*r*8, but lhs_bound + rhs_bound → LHS > p*q*r*8. 모순.
  omega

/-- 확인 예시 -/
example : σ 1 (2 * 3 * 5) * Nat.totient (2 * 3 * 5) ≠
    (2 * 3 * 5) * (Nat.divisors (2 * 3 * 5)).card :=
  theorem_B_three_primes
    Nat.prime_two Nat.prime_three (by decide : (5 : ℕ).Prime)
    (by norm_num) (by norm_num) (by norm_num)
    (by decide) (by decide) (by decide)

example : σ 1 (2 * 3 * 7) * Nat.totient (2 * 3 * 7) ≠
    (2 * 3 * 7) * (Nat.divisors (2 * 3 * 7)).card :=
  theorem_B_three_primes
    Nat.prime_two Nat.prime_three (by decide : (7 : ℕ).Prime)
    (by norm_num) (by norm_num) (by norm_num)
    (by decide) (by decide) (by decide)

example : σ 1 (3 * 5 * 7) * Nat.totient (3 * 5 * 7) ≠
    (3 * 5 * 7) * (Nat.divisors (3 * 5 * 7)).card :=
  theorem_B_three_primes
    Nat.prime_three (by decide : (5 : ℕ).Prime) (by decide : (7 : ℕ).Prime)
    (by norm_num) (by norm_num) (by norm_num)
    (by decide) (by decide) (by decide)

-- Theorem B 진전:
--  Case 1 (prime p): ✓
--  Case 2a (n = 2q): ✓
--  Case 2b (n = pq, both odd): ✓
--  Case 3 (n = p^a, a ≥ 2): ✓
--  Case 4a (n = pqr, 3 distinct primes, ordered): ✓ (본 파일)
--  Case 4b (n = p^a·q^b·...·, 일반 합성수): v5 이상

end N6Mathlib
