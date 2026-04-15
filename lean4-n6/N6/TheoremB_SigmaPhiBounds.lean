-- N6.TheoremB_SigmaPhiBounds : Strict σφ bounds for squarefree n with ω ≥ 3
-- v4 M3_v4 helpers (2026-04-16 loop 49)
--
-- Loop 23 의 theorem_B_six_primes 내 strict > 논증을 public lemma 로 추출.
-- 다음 단계 (ω=7 via split) 에 사용.

import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.NumberTheory.Divisors
import Mathlib.Data.Nat.Totient
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum.Prime
import N6.TheoremB_PrimeCase
import N6.TheoremB_Case4_ThreePrimes
import N6.TheoremB_Case4c_FourPrimes
import N6.TheoremB_Case4c_FivePrimes
import N6.TheoremB_Case4c_SixPrimes

namespace N6Mathlib

open Nat ArithmeticFunction
open scoped ArithmeticFunction.sigma

set_option maxHeartbeats 800000

/-- σφ(pqrstu) > pqrstu·64 STRICT for 6 distinct primes ≥ 2,3,5,7,11,13.
    loop 23 의 proof 내부 bound 추출. -/
theorem sigma_phi_pqrstu_strict {p q r s t u : ℕ}
    (hp : p.Prime) (hq : q.Prime) (hr : r.Prime) (hs : s.Prime)
    (ht : t.Prime) (hu : u.Prime)
    (hp2 : p ≥ 2) (hq3 : q ≥ 3) (hr5 : r ≥ 5) (hs7 : s ≥ 7)
    (ht11 : t ≥ 11) (hu13 : u ≥ 13)
    (hpq : p ≠ q) (hpr : p ≠ r) (hqr : q ≠ r)
    (hps : p ≠ s) (hqs : q ≠ s) (hrs : r ≠ s)
    (hpt : p ≠ t) (hqt : q ≠ t) (hrt : r ≠ t) (hst : s ≠ t)
    (hpu : p ≠ u) (hqu : q ≠ u) (hru : r ≠ u) (hsu : s ≠ u) (htu : t ≠ u) :
    σ 1 (p * q * r * s * t * u) * Nat.totient (p * q * r * s * t * u) >
      (p * q * r * s * t * u) * 64 := by
  rw [sigma_one_pqrstu hp hq hr hs ht hu hpq hpr hqr hps hqs hrs hpt hqt hrt hst hpu hqu hru hsu htu]
  rw [totient_pqrstu hp hq hr hs ht hu hpq hpr hqr hps hqs hrs hpt hqt hrt hst hpu hqu hru hsu htu]
  rw [sigma_one_prime hp, sigma_one_prime hq, sigma_one_prime hr,
      sigma_one_prime hs, sigma_one_prime ht, sigma_one_prime hu]
  rw [Nat.totient_prime hp, Nat.totient_prime hq, Nat.totient_prime hr,
      Nat.totient_prime hs, Nat.totient_prime ht, Nat.totient_prime hu]
  -- Want: (p+1)(q+1)(r+1)(s+1)(t+1)(u+1)·(p-1)(q-1)(r-1)(s-1)(t-1)(u-1) > pqrstu · 64
  have hp1 : p - 1 ≥ 1 := by omega
  have hq1 : q - 1 ≥ 2 := by omega
  have hr1 : r - 1 ≥ 4 := by omega
  have hs1 : s - 1 ≥ 6 := by omega
  have ht1 : t - 1 ≥ 10 := by omega
  have hu1 : u - 1 ≥ 12 := by omega
  have h_sub6 : (p - 1) * (q - 1) * (r - 1) * (s - 1) * (t - 1) * (u - 1) ≥ 5760 := by
    have h2 : (p - 1) * (q - 1) ≥ 2 :=
      (Nat.mul_le_mul hp1 hq1).trans_eq (by ring)
    have h3 : (p - 1) * (q - 1) * (r - 1) ≥ 8 :=
      (Nat.mul_le_mul h2 hr1).trans_eq (by ring)
    have h4 : (p - 1) * (q - 1) * (r - 1) * (s - 1) ≥ 48 :=
      (Nat.mul_le_mul h3 hs1).trans_eq (by ring)
    have h5 : (p - 1) * (q - 1) * (r - 1) * (s - 1) * (t - 1) ≥ 480 :=
      (Nat.mul_le_mul h4 ht1).trans_eq (by ring)
    calc (p - 1) * (q - 1) * (r - 1) * (s - 1) * (t - 1) * (u - 1) ≥ 480 * 12 :=
        Nat.mul_le_mul h5 hu1
      _ = 5760 := by ring
  -- (p+1)(q+1)(r+1)(s+1)(t+1)(u+1) > pqrstu via pairwise bounds
  have h_pq_pos : p * q > 0 := by positivity
  have h_pqrs_rs_pos : (p * q) * (r * s) > 0 := by positivity
  have h_pq_gt : (p + 1) * (q + 1) > p * q := by nlinarith
  have h_rs_gt : (r + 1) * (s + 1) > r * s := by nlinarith
  have h_tu_gt : (t + 1) * (u + 1) > t * u := by nlinarith
  have h_add :
      (p + 1) * (q + 1) * (r + 1) * (s + 1) * (t + 1) * (u + 1) >
      p * q * r * s * t * u := by
    calc (p + 1) * (q + 1) * (r + 1) * (s + 1) * (t + 1) * (u + 1)
        = ((p + 1) * (q + 1)) * ((r + 1) * (s + 1)) * ((t + 1) * (u + 1)) := by ring
      _ > (p * q) * ((r + 1) * (s + 1)) * ((t + 1) * (u + 1)) :=
          (Nat.mul_lt_mul_right (by positivity)).mpr
            ((Nat.mul_lt_mul_right (by positivity)).mpr h_pq_gt)
      _ > (p * q) * (r * s) * ((t + 1) * (u + 1)) :=
          (Nat.mul_lt_mul_right (by positivity)).mpr
            ((Nat.mul_lt_mul_left h_pq_pos).mpr h_rs_gt)
      _ > (p * q) * (r * s) * (t * u) :=
          (Nat.mul_lt_mul_left h_pqrs_rs_pos).mpr h_tu_gt
      _ = p * q * r * s * t * u := by ring
  -- σφ ≥ 5760·(p+1)…(u+1) > 5760·pqrstu > 64·pqrstu
  have lhs_bound :
      (p + 1) * (q + 1) * (r + 1) * (s + 1) * (t + 1) * (u + 1) *
        ((p - 1) * (q - 1) * (r - 1) * (s - 1) * (t - 1) * (u - 1)) ≥
      (p + 1) * (q + 1) * (r + 1) * (s + 1) * (t + 1) * (u + 1) * 5760 :=
    Nat.mul_le_mul_left _ h_sub6
  have mid_gt :
      (p + 1) * (q + 1) * (r + 1) * (s + 1) * (t + 1) * (u + 1) * 5760 >
      p * q * r * s * t * u * 5760 :=
    (Nat.mul_lt_mul_right (by norm_num)).mpr h_add
  have final_gt : p * q * r * s * t * u * 5760 > p * q * r * s * t * u * 64 := by
    have h_pos : p * q * r * s * t * u > 0 := by positivity
    nlinarith
  omega

end N6Mathlib
