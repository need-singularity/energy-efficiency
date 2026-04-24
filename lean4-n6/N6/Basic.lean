-- N6.Basic : σ, φ, τ 정의 + n = 6 특이성 bounded 확인
-- v3 M3 loop 18 → v4 M3 loop 33: naive σ/φ/τ 기반 bounded kernel decide.
-- 일반 (∀ n ≥ 2) 증명은 Mathlib 기반 TheoremB_Capstone + 11 sub-case 모듈에서 조립.
-- 본 파일은 독립적으로 zero-sorry.

namespace N6

/-- 약수 합 σ(n) = Σ_{d|n} d -/
def sigma (n : Nat) : Nat :=
  (List.range (n + 1)).filter (fun d => d > 0 ∧ n % d = 0) |>.foldl (· + ·) 0

/-- 오일러 토티언트 φ(n) = |{k : 1 ≤ k ≤ n, gcd(k, n) = 1}| -/
def phi (n : Nat) : Nat :=
  (List.range (n + 1)).filter (fun k => k > 0 ∧ Nat.gcd k n = 1) |>.length

/-- 약수 개수 τ(n) = |{d : d | n}| -/
def tau (n : Nat) : Nat :=
  (List.range (n + 1)).filter (fun d => d > 0 ∧ n % d = 0) |>.length

-- n = 6 특수 정체성 구체 계산 (Decidable via def computation)
example : sigma 6 = 12 := by decide
example : phi 6 = 2 := by decide
example : tau 6 = 4 := by decide
example : sigma 6 * phi 6 = 6 * tau 6 := by decide

/--
**Theorem B (Basic, bounded form)**: n = 6 만이 σ·φ = n·τ 를 만족한다 (n ∈ [2, 20]).

일반 ∀ n ≥ 2 버전은 `N6Mathlib.TheoremB_Capstone` 에 Mathlib 기반 11 sub-case
모듈의 조립으로 형식화 예정 (v5). 본 파일은 naive 정의 위에서 유한 범위를
kernel decide 로 직접 검증하는 독립 증거이다.
-/
theorem theorem_B_bounded_20 :
    ((List.range 21).filter
        (fun n => decide (n ≥ 2) ∧ decide (sigma n * phi n = n * tau n))) = [6] := by
  decide

-- 일부 작은 케이스 수동 확인 (n = 6 이 유일함을 implication 방향으로 지원)
-- n = 2: σ=3, φ=1, τ=2 → 3·1 = 3, n·τ = 4 → 불일치
example : ¬ (sigma 2 * phi 2 = 2 * tau 2) := by decide

-- n = 3: σ=4, φ=2, τ=2 → 8, n·τ = 6 → 불일치
example : ¬ (sigma 3 * phi 3 = 3 * tau 3) := by decide

-- n = 4: σ=7, φ=2, τ=3 → 14, n·τ = 12 → 불일치
example : ¬ (sigma 4 * phi 4 = 4 * tau 4) := by decide

-- n = 5: σ=6, φ=4, τ=2 → 24, n·τ = 10 → 불일치
example : ¬ (sigma 5 * phi 5 = 5 * tau 5) := by decide

-- n = 6: σ=12, φ=2, τ=4 → 24, n·τ = 24 → 일치 ✓
example : sigma 6 * phi 6 = 6 * tau 6 := by decide

-- n = 7: σ=8, φ=6, τ=2 → 48, n·τ = 14 → 불일치
example : ¬ (sigma 7 * phi 7 = 7 * tau 7) := by decide

end N6
