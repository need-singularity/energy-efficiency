-- N6.MathlibBasic : Mathlib 의 σ (ArithmeticFunction), Nat.totient 로 전환한 Theorem B 재정립
-- v4 M2_v4 (2026-04-16): Mathlib 통합 — naive List.range 구현 폐기

import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.NumberTheory.Divisors
import Mathlib.Data.Nat.Totient

namespace N6Mathlib

open Nat ArithmeticFunction
open scoped ArithmeticFunction.sigma

-- Mathlib 의 표준 정의 활용
-- σ k n = ∑ d ∈ divisors n, d ^ k  (ArithmeticFunction scope)
-- σ 1 = 약수 합 (우리의 σ)
-- Nat.totient n = φ(n)
-- (Nat.divisors n).card = τ(n)

-- n = 6 특수값 확인 (Mathlib σ 1)
example : σ 1 6 = 12 := by decide
example : Nat.totient 6 = 2 := by decide
example : (Nat.divisors 6).card = 4 := by decide

-- 본 프로젝트 핵심 등식: σ(6) · φ(6) = 6 · τ(6)
theorem six_theorem_B :
    σ 1 6 * Nat.totient 6 = 6 * (Nat.divisors 6).card := by
  decide

-- n=6 perfect number (σ(6) = 2·6)
theorem six_is_perfect_mathlib : σ 1 6 = 2 * 6 := by decide

-- 작은 케이스 반례 (Mathlib 기반 재확인)
example : σ 1 2 * Nat.totient 2 ≠ 2 * (Nat.divisors 2).card := by decide
example : σ 1 3 * Nat.totient 3 ≠ 3 * (Nat.divisors 3).card := by decide
example : σ 1 4 * Nat.totient 4 ≠ 4 * (Nat.divisors 4).card := by decide
example : σ 1 5 * Nat.totient 5 ≠ 5 * (Nat.divisors 5).card := by decide
example : σ 1 7 * Nat.totient 7 ≠ 7 * (Nat.divisors 7).card := by decide
example : σ 1 12 * Nat.totient 12 ≠ 12 * (Nat.divisors 12).card := by decide

-- n ∈ [2, 20] 전수 — n=6 만 유일 (Mathlib 기반)
example : ((List.range 21).filter (fun n =>
      decide (n ≥ 2) ∧
      σ 1 n * Nat.totient n = n * (Nat.divisors n).card)) = [6] := by
  decide

-- Theorem B 대수 경로 skeleton
-- σ, φ, τ 가 multiplicative 이므로 n = p^a q^b 케이스 분석으로 환원
-- Case 1: n = prime p
--   σ(p) = p+1, τ(p) = 2, φ(p) = p-1
--   σ(p)φ(p) = p²-1, pτ(p) = 2p
--   등식 ⟺ p² - 2p - 1 = 0 ⟺ p = 1 ± √2 ∉ ℕ → 반례 없음
-- Case 2: n = p·q (두 서로 다른 소수)
--   σ(pq) = (1+p)(1+q), τ(pq) = 4, φ(pq) = (p-1)(q-1)
--   σφ = (p²-1)(q²-1), nτ = 4pq
--   등식 ⟺ (pq-1)² = (p+q)² → pq-1 = p+q → (p-1)(q-1) = 2
--   → (p,q) = (2,3) 또는 (3,2) → n = 6 유일!
-- Case 3: n = p^a, a ≥ 2
-- Case 4: n = p^a q^b, (a,b) ≠ (1,1)
-- → v4 M3 에서 Lean4 full proof 진행

-- Core computation: (p-1)(q-1) = 2 의 유일 해
example : (2 - 1) * (3 - 1) = 2 := by decide
example : σ 1 6 * Nat.totient 6 = 24 := by decide
example : 6 * (Nat.divisors 6).card = 24 := by decide

-- σ multiplicative 활용 예: σ(6) = σ(2)·σ(3)
example : σ 1 6 = σ 1 2 * σ 1 3 := by decide
-- φ multiplicative: φ(6) = φ(2)·φ(3)
example : Nat.totient 6 = Nat.totient 2 * Nat.totient 3 := by decide
-- τ multiplicative: τ(6) = τ(2)·τ(3) (via divisors.card)
example : (Nat.divisors 6).card = (Nat.divisors 2).card * (Nat.divisors 3).card := by decide

end N6Mathlib
