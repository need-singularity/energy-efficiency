-- N6.TheoremB_Case4b_TwoPrimePow : Theorem B case 4b(i) (n = 2·q^b, q odd prime, b ≥ 2)
-- v4 M3_v4 case 4b(i) (2026-04-16 loop 27)
--
-- 목표: q ≥ 3 odd prime, b ≥ 2 → σ(2q^b)·φ(2q^b) ≠ (2q^b)·τ(2q^b)
-- 전략:
--   gcd(2, q^b) = 1 → σ/φ/τ multiplicative 적용
--   σ(2q^b) = 3·σ(q^b), φ(2q^b) = φ(q^b), τ(2q^b) = 2·(b+1)
--   σ(q^b)·φ(q^b) = q^(b-1)·(q^(b+1) - 1)  (case 3 geom-sum identity)
--   σφ = 3·q^(b-1)·(q^(b+1) - 1), nτ = 4·q^b·(b+1) = 4q·q^(b-1)·(b+1)
--   등식 ⟺ 3·(q^(b+1) - 1) = 4·q·(b+1) ⟺ 3·q^(b+1) = 4·q·(b+1) + 3
--   증명: 3·q^(b+1) > 4·q·(b+1) + 3  for q ≥ 3, b ≥ 2  (key_ineq_4bi)
--
-- b=1 (n=2q)은 case 2a (P2) 가 이미 q=3 에서 등식, 나머지 q≥5 에서 부등 — TheoremB_Case2_P2 참조.
-- b=2 base: 3q³ > 12q+3, q≥3 에서 자명 (q=3: 81>39).

import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.NumberTheory.Divisors
import Mathlib.Data.Nat.Totient
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.NormNum.Prime
import N6.TheoremB_PrimeCase
import N6.TheoremB_Case3_PrimePow

namespace N6Mathlib

open Nat ArithmeticFunction
open scoped ArithmeticFunction.sigma

/-- 2 와 q^b (q odd prime) 서로소 -/
theorem coprime_2_odd_prime_pow {q b : ℕ} (hq : q.Prime) (hq_odd : q ≥ 3) :
    Nat.Coprime 2 (q ^ b) := by
  have h2q : Nat.Coprime 2 q := by
    apply (Nat.coprime_primes (by decide : (2 : ℕ).Prime) hq).mpr
    omega
  exact h2q.pow_right b

/-- σ₁(2·q^b) = 3·σ₁(q^b) -/
theorem sigma_one_2_prime_pow {q b : ℕ} (hq : q.Prime) (hq_odd : q ≥ 3) :
    σ 1 (2 * q ^ b) = 3 * σ 1 (q ^ b) := by
  have hcop : Nat.Coprime 2 (q ^ b) := coprime_2_odd_prime_pow hq hq_odd
  have h_mul : σ 1 (2 * q ^ b) = σ 1 2 * σ 1 (q ^ b) :=
    (isMultiplicative_sigma (k := 1)).right hcop
  rw [h_mul, sigma_one_prime Nat.prime_two]

/-- φ(2·q^b) = φ(q^b) -/
theorem totient_2_prime_pow {q b : ℕ} (hq : q.Prime) (hq_odd : q ≥ 3) :
    Nat.totient (2 * q ^ b) = Nat.totient (q ^ b) := by
  have hcop : Nat.Coprime 2 (q ^ b) := coprime_2_odd_prime_pow hq hq_odd
  rw [Nat.totient_mul hcop, Nat.totient_prime Nat.prime_two, Nat.one_mul]

/-- τ(2·q^b) = 2·(b+1) -/
theorem tau_2_prime_pow {q b : ℕ} (hq : q.Prime) (hq_odd : q ≥ 3) :
    (Nat.divisors (2 * q ^ b)).card = 2 * (b + 1) := by
  have hcop : Nat.Coprime 2 (q ^ b) := coprime_2_odd_prime_pow hq hq_odd
  have hσ0 : σ 0 (2 * q ^ b) = σ 0 2 * σ 0 (q ^ b) :=
    (isMultiplicative_sigma (k := 0)).right hcop
  have h_left : σ 0 (2 * q ^ b) = (Nat.divisors (2 * q ^ b)).card := by
    simp [sigma_zero_apply]
  have h_qb : σ 0 (q ^ b) = b + 1 := sigma_zero_apply_prime_pow hq
  have h_2 : σ 0 2 = 2 := by
    have := sigma_zero_apply_prime_pow (p := 2) (i := 1) Nat.prime_two
    simp at this; exact this
  rw [← h_left, hσ0, h_2, h_qb]

/-- Key inequality: 3·q^(b+1) > 4·q·(b+1) + 3  for q ≥ 3, b ≥ 2 -/
theorem key_ineq_4bi {q b : ℕ} (hq : q ≥ 3) (hb : b ≥ 2) :
    3 * q ^ (b + 1) > 4 * q * (b + 1) + 3 := by
  induction b, hb using Nat.le_induction with
  | base =>
    -- b = 2: 3·q³ > 12q + 3 ⟺ q³ > 4q + 1
    -- q ≥ 3: q·(q² - 4) = q(q-2)(q+2) ≥ 3·1·5 = 15, 그리고 q³ = q(q²-4) + 4q
    -- 실제 증명: q³ ≥ 3·q² ≥ 9q, 9q ≥ 4q + 5q ≥ 4q + 15 > 4q + 1
    have h_qq : q * q ≥ 9 := by nlinarith
    have h_q3 : q ^ 3 ≥ 9 * q := by
      have : q ^ 3 = q * q * q := by ring
      rw [this]; nlinarith
    have h_pow : q ^ (2 + 1) = q ^ 3 := by norm_num
    rw [h_pow]
    nlinarith
  | succ n hn ih =>
    -- ih : 3·q^(n+1) > 4q(n+1) + 3
    -- Goal: 3·q^(n+2) > 4q(n+2) + 3
    -- q^(n+2) = q · q^(n+1), q ≥ 3 → 3·q^(n+2) = q · (3·q^(n+1)) > q · (4q(n+1)+3)
    -- = 4q²(n+1) + 3q ≥ 4q(n+2) + 3
    have hq_pos : q > 0 := by omega
    have h_pow : q ^ (n + 1 + 1) = q * q ^ (n + 1) := by ring
    have h_exp : 3 * q ^ (n + 1 + 1) = q * (3 * q ^ (n + 1)) := by
      rw [h_pow]; ring
    rw [h_exp]
    have step1 : q * (3 * q ^ (n + 1)) > q * (4 * q * (n + 1) + 3) :=
      Nat.mul_lt_mul_of_pos_left ih hq_pos
    -- 이제 q · (4q(n+1)+3) ≥ 4q(n+2) + 3 임을 보이면 충분
    have step2 : q * (4 * q * (n + 1) + 3) ≥ 4 * q * (n + 1 + 1) + 3 := by
      -- q·(4q(n+1)+3) = 4q²(n+1) + 3q
      -- 4q(n+2) + 3 = 4q(n+1) + 4q + 3
      -- diff = 4q²(n+1) - 4q(n+1) + 3q - 4q - 3 = 4q(n+1)(q-1) + (3q - 4q - 3) = 4q(n+1)(q-1) - q - 3
      -- q≥3, n≥2 → 4q(n+1)(q-1) ≥ 4·3·3·2 = 72, -q-3 ≥ -q-3 ≥ -∞... 정확히 -q-3
      -- 하지만 72 - q - 3 = 69 - q. q ≤ ??? — 문제! q가 크면 이 bound 실패?
      -- 다시 계산: q·(4q(n+1)+3) = 4q²(n+1) + 3q
      --         4q(n+1+1) + 3 = 4q(n+1) + 4q + 3
      --         diff = 4q²(n+1) + 3q - 4q(n+1) - 4q - 3
      --              = 4q(n+1)(q-1) + 3q - 4q - 3
      --              = 4q(n+1)(q-1) - q - 3
      -- q≥3, n≥2: 4q(n+1)(q-1) ≥ 4·q·3·(q-1) = 12q(q-1) = 12q² - 12q
      -- diff ≥ 12q² - 12q - q - 3 = 12q² - 13q - 3
      -- q=3: 108 - 39 - 3 = 66 > 0 ✓
      -- q=5: 300 - 65 - 3 = 232 > 0
      -- 일반: 12q² - 13q - 3 > 0 for q ≥ 3 (q² 지배)
      nlinarith [hq, hn, sq_nonneg (q - 3), Nat.mul_le_mul hq hn]
    omega

/-- Theorem B case 4b(i): q odd prime ≥ 3, b ≥ 2 → σ(2q^b)·φ(2q^b) ≠ (2q^b)·τ(2q^b) -/
theorem theorem_B_2_prime_pow {q : ℕ} (hq : q.Prime) (hq_odd : q ≥ 3) {b : ℕ} (hb : b ≥ 2) :
    σ 1 (2 * q ^ b) * Nat.totient (2 * q ^ b) ≠
      (2 * q ^ b) * (Nat.divisors (2 * q ^ b)).card := by
  rw [sigma_one_2_prime_pow hq hq_odd,
      totient_2_prime_pow hq hq_odd,
      tau_2_prime_pow hq hq_odd]
  -- Goal: 3·σ(q^b) · φ(q^b) ≠ (2q^b) · (2(b+1))
  rw [sigma_one_prime_pow_sum hq,
      Nat.totient_prime_pow hq (by omega : b > 0)]
  -- Goal: (3·Σ q^k)·(q^(b-1)·(q-1)) ≠ (2q^b)·(2(b+1))
  intro h
  have hq2 : q ≥ 2 := by omega
  have hq_pos : q ≥ 1 := by omega
  have hb1 : b ≥ 1 := by omega
  -- σφ(q^b) reduction — factor out q^(b-1)
  have reorg :
      (3 * ∑ k ∈ Finset.range (b + 1), q ^ k) * (q ^ (b - 1) * (q - 1))
        = q ^ (b - 1) * (3 * ((q - 1) * ∑ k ∈ Finset.range (b + 1), q ^ k)) := by
    ring
  rw [reorg, geom_sum_identity hq2] at h
  -- h: q^(b-1) · (3·(q^(b+1) - 1)) = (2q^b)·(2(b+1))
  -- RHS = 4·q^b·(b+1) = 4·q·q^(b-1)·(b+1) = q^(b-1)·(4q(b+1))
  have h_qb : q ^ b = q * q ^ (b - 1) := by
    have : b = (b - 1) + 1 := by omega
    conv_lhs => rw [this]
    ring
  have h_rhs : (2 * q ^ b) * (2 * (b + 1)) = q ^ (b - 1) * (4 * q * (b + 1)) := by
    rw [h_qb]; ring
  rw [h_rhs] at h
  -- h: q^(b-1) · (3·(q^(b+1) - 1)) = q^(b-1) · (4q(b+1))
  -- cancel q^(b-1) > 0
  have h_pow_pos : q ^ (b - 1) > 0 := Nat.pow_pos (by omega : q > 0)
  have h_cancel : 3 * (q ^ (b + 1) - 1) = 4 * q * (b + 1) :=
    Nat.eq_of_mul_eq_mul_left h_pow_pos h
  -- 3·(q^(b+1) - 1) = 3·q^(b+1) - 3 (as natural, since q^(b+1) ≥ 1)
  have h_pow_ge : q ^ (b + 1) ≥ 1 := Nat.one_le_pow _ _ (by omega : 0 < q)
  have h_expand : 3 * (q ^ (b + 1) - 1) = 3 * q ^ (b + 1) - 3 := by
    rw [Nat.mul_sub, Nat.mul_one]
  rw [h_expand] at h_cancel
  -- h_cancel: 3·q^(b+1) - 3 = 4q(b+1), i.e., 3·q^(b+1) = 4q(b+1) + 3
  -- Contradiction with key_ineq_4bi
  have hstrict := key_ineq_4bi hq_odd hb
  -- Need 3·q^(b+1) ≥ 3 to do subtraction properly
  have h_3pow : 3 * q ^ (b + 1) ≥ 3 := by
    have : q ^ (b + 1) ≥ 1 := h_pow_ge
    omega
  omega

/-- 확인 예시 -/
-- n = 18 = 2·3²: q=3, b=2 — 3·81 = 243 > 4·3·3+3 = 39 ✓
example : 3 * 3 ^ (2 + 1) > 4 * 3 * (2 + 1) + 3 := by decide
-- n = 50 = 2·5²: q=5, b=2
example : 3 * 5 ^ (2 + 1) > 4 * 5 * (2 + 1) + 3 := by decide

end N6Mathlib
