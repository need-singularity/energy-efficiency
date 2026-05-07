---
id: lean4-formalization-plan
date: 2026-04-15
roadmap_tasks: HONEST-PX-4 + FORMAL-P3-1 + FORMAL-PX-1 (combined)
grade: [10] execution plan (not compiled)
license: CC-BY-SA-4.0
---

# Lean4 Formalization 3-Task Integrated Execution Plan — Theorem B σ(n)·φ(n) = n·τ(n) ⟺ n=6

> **Summary**: Combining 3 Lean4 tasks. (1) HONEST-PX-4 Lean4/Coq introduction — environment setup plan, (2) FORMAL-P3-1 Lean4 formalization of Clay 7 problem statements — strategy document, (3) FORMAL-PX-1 Mathlib PR — identifying concrete contribution candidates. **This session is plan + skeleton; actual compile verification comes after Lean4 environment installation in a separate session.**

---

## §0 Entry — Why the 3 Lean4 Tasks Are Integrated

The 3 deferred tasks are substantively a staged evolution of **learning + using the same toolchain (Lean4/mathlib)**:

| Task | Essence | Stage |
|------|------|------|
| HONEST-PX-4 | Lean4 environment + basic syntax mastery | **L1** (install + hello world) |
| FORMAL-P3-1 | Writing Clay 7 problem statements in Lean4 | **L2** (definition layer) |
| FORMAL-PX-1 | Submitting PR to Mathlib repository | **L3** (contribution layer) |

This document is the **plan of the L1 → L2 → L3 path**; actual compile testing happens in a **separate session after Lean4 installation**.

---

## §1 L1 — Lean4 Environment Setup (HONEST-PX-4)

### 1.1 Install Procedure (assuming Mac ARM)

```bash
# Step 1: install elan (Lean version manager)
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh

# Step 2: set Lean4 stable
elan default leanprover/lean4:stable

# Step 3: create project with mathlib dependency
cd /Users/ghost/core/canon
mkdir lean && cd lean
lake new n6arch --lang lean4
cd n6arch

# Step 4: add mathlib (edit lakefile.lean)
cat >> lakefile.lean <<'EOF'
require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "stable"
EOF

# Step 5: build (first build ~30 min)
lake update
lake build
```

**Expected blockers**:
- Mac ARM + Lean4: Apple Silicon support stable (2024~)
- First mathlib build `~8GB` disk + `~30 min` CPU
- Internet required (dependencies)

### 1.2 Verification Hello World

```lean4
-- file: N6Arch/Basic.lean
import Mathlib

-- Do mathlib's Nat.sigma / Nat.totient / Nat.card n.divisors exist?
#check @Nat.sigma   -- expected output: Nat.sigma : ℕ → ℕ → ℕ
#check @Nat.totient -- expected output: Nat.totient : ℕ → ℕ
```

If these `#check` commands pass without errors, L1 complete.

**Cannot execute in this session — no Lean4 installed**.

---

## §2 L2 — Theorem B Formalization (FORMAL-P3-1 + atlas MILL-PX-A1)

### 2.1 Clay 7 Problems Feasible in Lean4

| BT | Lean4 feasibility | Core definitions |
|----|-------------------|----------|
| BT-541 RH | partial (zeta definition OK, proof impossible) | `RiemannZeta.riemannZeta` (in mathlib) |
| BT-542 P vs NP | definable, theorem impossible | Turing machine formalization difficult |
| BT-543 YM | definition difficult (QFT) | absent in mathlib |
| BT-544 NS | partial (PDE OK, regularity theorem impossible) | `MeasureTheory` + `AnalysisODE` |
| BT-545 Hodge | definable, theorem partial | `AlgebraicGeometry.HodgeConjecture` (in progress) |
| BT-546 BSD | partial (Sel definition OK, theorem impossible) | `EllipticCurve.Selmer` (in progress) |
| **atlas MILL-PX-A1 Theorem B** | **✓ fully feasible** | `Nat.sigma`, `Nat.totient`, `Nat.card n.divisors` all in mathlib |

**Conclusion**: target of this session = **MILL-PX-A1 Theorem B** (for n ≥ 2, σ(n)·φ(n) = n·τ(n) ⟺ n = 6). **Clay 7 problem statements need mathlib API additions**; Theorem B falls within elementary arithmetic scope.

### 2.2 Skeleton for Theorem B Formalization

```lean4
-- file: N6Arch/TheoremB.lean
import Mathlib.NumberTheory.ArithmeticFunction
import Mathlib.NumberTheory.Divisors
import Mathlib.Tactic

open Nat

/-- atlas MILL-PX-A1 Theorem B: σ(n) · φ(n) = n · τ(n) ⟺ n = 6 (for n ≥ 2) -/
theorem sigma_phi_eq_n_tau_iff_six (n : ℕ) (h : n ≥ 2) :
    Nat.sigma 1 n * Nat.totient n = n * (Nat.divisors n).card ↔ n = 6 := by
  constructor
  · intro heq
    -- Forward: σφ = nτ → n = 6
    -- Strategy: exhaustive check for n ≤ 6, then bound for n > 6
    -- Key lemma: σ(n) ≥ n+1, φ(n) ≤ n-1, τ(n) ≤ 2 * sqrt(n) (Kadiri-Pomerance-like)
    -- Combined: σ(n)·φ(n)/n·τ(n) diverges from 1 for n ≠ 6
    sorry
  · rintro rfl
    -- Backward: n = 6 → σφ = 6τ
    -- σ(6) = 12, φ(6) = 2, τ(6) = 4
    -- LHS = 12 * 2 = 24
    -- RHS = 6 * 4 = 24
    -- Should be derivable by `simp` + `norm_num` + explicit computation
    unfold Nat.sigma Nat.totient
    decide  -- 6 is small enough to verify by decide
```

### 2.3 Proof Structure (forward direction detail)

**Step 1**: Finite check `n ∈ {2, 3, 4, 5, 6}`
- n=2: σ=3, φ=1, τ=2, 3·1=3 ≠ 2·2=4 ✗
- n=3: σ=4, φ=2, τ=2, 4·2=8 ≠ 3·2=6 ✗
- n=4: σ=7, φ=2, τ=3, 7·2=14 ≠ 4·3=12 ✗
- n=5: σ=6, φ=4, τ=2, 6·4=24 ≠ 5·2=10 ✗
- **n=6: σ=12, φ=2, τ=4, 12·2=24 = 6·4=24 ✓**

**Step 2**: Case of `n ≥ 7`
- Asymptotic of σ(n) · φ(n) / (n · τ(n)) ratio
- σ(n) ~ n log log n (Gronwall)
- φ(n) · σ(n) / n² does not converge to ratio 1
- Lean4 tactic: `omega` + `interval_cases` (small cases) + bound lemma

**Step 3**: full Lean4 proof strategy:

```lean4
theorem sigma_phi_eq_n_tau_iff_six (n : ℕ) (h : n ≥ 2) :
    Nat.sigma 1 n * Nat.totient n = n * (Nat.divisors n).card ↔ n = 6 := by
  constructor
  · intro heq
    -- Step 1: n ≤ 6 exhaustive
    interval_cases n
    all_goals (first | rfl | (exfalso; simp [Nat.sigma, Nat.totient] at heq; omega))
    -- Step 2: n ≥ 7 bound (actual bound lemma required)
    · sorry -- n ≥ 7 bound theorem
  · rintro rfl
    decide
```

**Reality**: `interval_cases n` works for small n, bound for large n requires **3-5 separate auxiliary lemmas**. Total workload ~500-1000 LoC Lean4, **2-3 weeks full-time**.

### 2.4 Dependency on 10 Mathlib Lemmas

```lean4
-- 1. definition of σ
Nat.sigma_one_eq_sum_divisors : Nat.sigma 1 n = ∑ d ∈ n.divisors, d

-- 2. multiplicativity of φ
Nat.totient_mul (m n : ℕ) (hmn : m.Coprime n) : (m * n).totient = m.totient * n.totient

-- 3. multiplicativity of τ
Nat.card_divisors_mul : (m * n).divisors.card = m.divisors.card * n.divisors.card  -- m ⊥ n

-- 4. Euler product of σ/n
Nat.sigma_div_n_eq_prod_primes  -- actual name to verify

-- 5. perfect number characterization
Nat.sigma_eq_two_mul_iff_perfect  -- n perfect ⟺ σ(n) = 2n

-- 6. n=6 perfect proof
Nat.sigma_one_six : Nat.sigma 1 6 = 12  -- or `decide`
Nat.totient_six : Nat.totient 6 = 2
Nat.card_divisors_six : (Nat.divisors 6).card = 4

-- 7. lower bound for σ(n)
Nat.sigma_one_ge : Nat.sigma 1 n ≥ n + 1  -- for n ≥ 2

-- 8. upper bound for φ(n)
Nat.totient_lt : Nat.totient n < n  -- for n ≥ 2

-- 9. upper bound for τ(n)
Nat.card_divisors_le : (Nat.divisors n).card ≤ 2 * Nat.sqrt n + 1  -- approx

-- 10. large n handling
interval_cases tactic  -- n ≤ 7 exhaustive
```

**Existence check needed**: 4, 7, 9 may not be directly in mathlib. Self-authoring required.

---

## §3 L3 — Mathlib PR Submission Plan (FORMAL-PX-1)

### 3.1 PR Targets — 3 Direct Contribution Candidates

**PR 1: Nat.sigma / totient / card_divisors n=6 explicit lemmas**

```lean4
-- Goal: provide building blocks for external work such as atlas MILL-PX-A1
theorem Nat.sigma_one_six : Nat.sigma 1 6 = 12 := by decide
theorem Nat.totient_six : Nat.totient 6 = 2 := by decide
theorem Nat.card_divisors_six : (Nat.divisors 6).card = 4 := by decide
```

**PR 2: perfect number perfect_of_six / perfect_of_28 lemmas**

```lean4
theorem Nat.perfect_six : Nat.Perfect 6 := by
  simp [Nat.Perfect, Nat.sigma]
  decide

theorem Nat.perfect_twenty_eight : Nat.Perfect 28 := by
  simp [Nat.Perfect, Nat.sigma]
  decide
```

**PR 3: σφ = nτ characterization (main theorem B)**

```lean4
theorem Nat.sigma_phi_eq_n_tau_iff_six (n : ℕ) (h : n ≥ 2) :
    Nat.sigma 1 n * Nat.totient n = n * (Nat.divisors n).card ↔ n = 6 := by
  ...
```

PR 1-2 take **1 day of work + 1-2 weeks Mathlib reviewer wait**. PR 3 takes **2-3 weeks of work + 4-6 weeks review**.

### 3.2 Mathlib Contribution Preparation

1. `@[simp]` attribute determination (too-strong simp can be rejected)
2. `docstring` bilingual (Korean/English)
3. First post proposal on Zulip community (https://leanprover.zulipchat.com)
4. Explain motivation via GitHub issue
5. At PR submission, verify no `#align` markers (Lean4 mathlib has separate policy)

### 3.3 Alternative Path — atlas-Based Contribution

Mathlib is the main target, alternatives:
- Own Lean4 project: `canon/lean/N6Arch/` — own theorem library
- Github Action CI: `.github/workflows/lean-ci.yml` — Lean4 compile check on each commit
- Zenodo DOI: independent release of completed Lean4 proof

---

## §4 Pre-Specified MISS Conditions for Each of 3 Tasks

| Task | MISS condition | fallback |
|------|-----------|----------|
| HONEST-PX-4 | Mac ARM + Lean4 stable build failure | Linux VM + Docker |
| FORMAL-P3-1 | Theorem B forward direction Lean4 tactic unavailable | paper-only proof + meta-note |
| FORMAL-PX-1 | Mathlib reviewer PR rejection (style / scope) | independent project release |

---

## §5 atlas Entry Proposals

```
@R MILL-HONEST-PX4-lean4-plan-published = Lean4 environment setup + Theorem B formalization plan document :: n6atlas [10]
  "HONEST-PX-4 Lean4/Coq introduction plan (2026-04-15 loop 10): L1 Mac ARM install procedure (elan/lake/mathlib,
   ~30 min + build 30 min), hello world verification example (#check on Nat.sigma, etc.). Environment setup not
   executed in this session; to be executed in a separate session after user approval"

@R MILL-FORMAL-P3-1-theorem-B-skeleton = Theorem B Lean4 skeleton (depends on 10 mathlib lemmas) :: n6atlas [9]
  "FORMAL-P3-1 Clay Lean4 formalization strategy: among the 7 Millennium problems, the only statement actually
   formalizable is atlas MILL-PX-A1 Theorem B (σφ=nτ iff n=6). Elementary arithmetic scope, easier than original Clay.
   Skeleton authored; backward direction by decide tactic + forward by interval_cases + bound lemma. 2-3 weeks
   full-time, ~500-1000 LoC expected. compile verification DEFERRED"

@R MILL-FORMAL-PX-1-mathlib-pr-candidates = Mathlib PR 3 candidates (sigma_six / perfect_six / theorem_B) :: n6atlas [9]
  "FORMAL-PX-1 Mathlib contribution plan: 3 PR candidates identified — (1) Nat.sigma_one_six + Nat.totient_six +
   Nat.card_divisors_six (PR 1-day work + 1-2 weeks review), (2) Nat.perfect_six/twenty_eight (similar), (3)
   Theorem B in full (2-3 weeks + 4-6 weeks review). Alternative path: independent release via own canon/lean/N6Arch/"
```

---

## §6 Related Files

- `theory/roadmap-v2/millennium-v3-design-2026-04-15.md` §3 T5 / §4 M3 (v3 Lean4 phase)
- `reports/breakthroughs/external-coordination-infrastructure-2026-04-15.md` §3 (outreach Lean4 parallel)
- `theory/proofs/theorem-r1-uniqueness.md` (Theorem B original proof, in Korean)

---

## §7 Honesty Checks

- **Lean4 environment not installed**: ✓ (plan only)
- **No Mathlib PR submitted**: ✓ (candidates identified only)
- **No compile verification of Theorem B**: ✓ (skeleton with `sorry`)
- **Actual workload specified**: ✓ (2-3 weeks full-time)
- **Mac ARM blockers specified**: ✓
- **Alternative paths provided**: ✓ (Linux VM, independent release)
- **BT draft target 0/6 maintained**: ✓ (Theorem B is atlas entry, not Clay problem)

---

*Drafted: 2026-04-15 loop 10*
*3-task integration (HONEST-PX-4 + FORMAL-P3-1 + FORMAL-PX-1)*
*Actual Lean4 work to be executed in v3 Phase 13 M3*
