-- N6.MechVerif.AX1 : thm.AX1_n6_uniqueness — first mechanical attempt
-- W2 deliverable for proposals/hexa-weave-formal-mechanical-verification-prep.md §4 unit 1.
-- Date: 2026-04-28 (cycle 4 fan-out 4/5).
--
-- W6 cycle 8 (2026-04-28) UPDATE: `AX1Eq` definition + the named axiom
-- `axiom_robin_hardy_wright_ax1_tail` are RELOCATED to
-- `N6/MechVerif/Foundation/Axioms.lean` (single source of truth for all 7
-- W4-W6 named axioms). This file imports them; no semantic change.
-- F-W5-AX2-1 partial resolution.
--
-- Mission-text alias path: lean4-n6/HexaWeave/AX1NUniqueness.lean
-- Canonical Spec §6 path : lean4-n6/N6/MechVerif/AX1.lean  ← THIS FILE
-- Choice rationale: keep `lean_lib N6` lakefile unchanged.
--
-- Theorem statement (Spec §4 unit 1, with W1 audit corrigendum #3 applied —
-- there is NO `Nat.ArithmeticFunction.tau` symbol in mathlib4 master rev
-- `19c497800a418208f973be74c9f5c5901aac2f54`; we use `(Nat.divisors n).card`
-- which equals `σ 0 n` per `sigma_zero_apply`):
--
--   ∀ n : ℕ, n ≥ 1 →
--     ( σ 1 n * Nat.totient n = n * (Nat.divisors n).card  ↔  n = 6 )
--
-- Proof strategy per Spec §4 unit 1:
--   ⟸  (n = 6 → equality):   `decide` on Mathlib σ/φ/divisors definitions.
--   ⟹  (equality → n = 6):   bounded `decide` for n ≤ 100  (W13 cycle 20);
--                              for n > 100, asymptotic tail bound named axiom.
--
-- W13 cycle 20 (2026-04-28): bounded threshold 50 → 100 via interval_cases
-- (axiom surface n>50 → n>100; axiom count UNCHANGED at 7 — PARTIAL outcome).
-- mathlib4 has NO Robin/Hardy-Wright/Wigert asymptotic; full mechanical
-- conversion deferred. raw 91 C3 honest disclosure in Foundation/Axioms.lean
-- §3 axiom-block.

import N6.MechVerif.Foundation.Axioms
import Mathlib.Tactic.IntervalCases

namespace N6Mathlib.MechVerif

open Nat ArithmeticFunction
open scoped ArithmeticFunction.sigma

/-! ## Reverse direction (n = 6 → equality)

    Direct `decide` on Mathlib σ/φ/divisors definitions for n = 6.
    `AX1Eq` is now defined in Foundation/Axioms.lean. -/

theorem AX1_reverse_n6 : AX1Eq 6 := by
  unfold AX1Eq; decide

/-- σ(6) = 12, φ(6) = 2, τ(6) = 4 — concrete witness. -/
theorem AX1_n6_witness :
    σ 1 6 = 12 ∧ Nat.totient 6 = 2 ∧ (Nat.divisors 6).card = 4 := by
  refine ⟨?_, ?_, ?_⟩ <;> decide

/-! ## Forward direction (equality → n = 6) -/

/-- Bounded forward: for `n ∈ [2, 30]` with `AX1Eq n`, we have `n = 6`. -/
theorem AX1_forward_bounded_30 (n : ℕ) (h_lo : 2 ≤ n) (h_hi : n ≤ 30)
    (h_eq : AX1Eq n) : n = 6 := by
  unfold AX1Eq at h_eq
  interval_cases n <;> first | rfl | (exfalso; revert h_eq; decide)

/-- Extended bounded forward: for `n ∈ [2, 50]` with `AX1Eq n`, we have `n = 6`. -/
theorem AX1_forward_bounded_50 (n : ℕ) (h_lo : 2 ≤ n) (h_hi : n ≤ 50)
    (h_eq : AX1Eq n) : n = 6 := by
  unfold AX1Eq at h_eq
  interval_cases n <;> first | rfl | (exfalso; revert h_eq; decide)

/-- W13 cycle-20 bounded forward: for `n ∈ [2, 100]` with `AX1Eq n`, we have
    `n = 6`. Extends bounded threshold 50 → 100; the named axiom's quantifier
    is correspondingly hardened to `100 < n`. raw 91 C3 honest: mathlib4 has
    no Robin/Hardy-Wright/Wigert asymptotic results, so full mechanical
    conversion is infeasible at cycle 20 — this is a PARTIAL surface-area
    reduction (axiom count UNCHANGED at 7). -/
theorem AX1_forward_bounded_100 (n : ℕ) (h_lo : 2 ≤ n) (h_hi : n ≤ 100)
    (h_eq : AX1Eq n) : n = 6 := by
  unfold AX1Eq at h_eq
  interval_cases n <;> first | rfl | (exfalso; revert h_eq; decide)

/-! ## W3 cycle-7 axiomatic Robin/Hardy-Wright tail (raw 91 C3 honest disclosure)

    W13 cycle-20 UPDATE: bounded threshold extended 50 → 100; axiom hardened
    to `100 < n`. The named axiom `axiom_robin_hardy_wright_ax1_tail` is
    declared in `N6/MechVerif/Foundation/Axioms.lean` (W6 cycle 8 relocation).
    Cited literature unchanged:
      * Robin (1984), J. Math. Pures Appl. 63, 187-213.
      * Hardy & Wright, Theorems 322 (σ asymptotic), 328 (φ asymptotic).
      * Wigert (1907), Arkiv för Mat. 3, 1-9 (τ(n) = n^o(1)). -/

/-- Unbounded tail (n > 100, W13 cycle 20): discharged by
    `axiom_robin_hardy_wright_ax1_tail`. -/
theorem AX1_forward_tail (n : ℕ) (h_big : 100 < n) (h_eq : AX1Eq n) : n = 6 :=
  absurd h_eq (axiom_robin_hardy_wright_ax1_tail n h_big)

/-- **`thm.AX1_n6_uniqueness`** — main W2 statement.

    W3 UPDATE (cycle 6, 2026-04-28): premise hardened to `n ≥ 2`.
    W3 UPDATE (cycle 7, 2026-04-28): forward tail discharged by named axiom.
    W6 UPDATE (cycle 8, 2026-04-28): axiom relocated to Foundation/Axioms.lean
    (no semantic change).
    W13 UPDATE (cycle 20, 2026-04-28): bounded threshold 50 → 100; axiom
    quantifier hardened to `100 < n`. -/
theorem AX1_n6_uniqueness :
    ∀ n : ℕ, 2 ≤ n →
      (σ 1 n * Nat.totient n = n * (Nat.divisors n).card ↔ n = 6) := by
  intro n h_lo
  constructor
  · -- forward: equality → n = 6
    intro h_eq
    by_cases h_hi : n ≤ 100
    · exact AX1_forward_bounded_100 n h_lo h_hi h_eq
    · exact AX1_forward_tail n (Nat.lt_of_not_le h_hi) h_eq
  · -- reverse: n = 6 → equality
    intro h_n6
    subst h_n6
    exact AX1_reverse_n6

/-- **n=1 counter-example to the un-corrected `n ≥ 1` form**. -/
theorem AX1_n6_uniqueness_n1_counterexample :
    AX1Eq 1 ∧ (1 : ℕ) ≠ 6 := by
  refine ⟨?_, ?_⟩
  · unfold AX1Eq; decide
  · decide

/-! ## Spec §4 unit 1 corrigendum surfaced in W2 (W2 falsifier F-W2-AX1-1). -/

/-- Backwards-compat alias: `AX1_n6_uniqueness_corrected` ≡ `AX1_n6_uniqueness`. -/
theorem AX1_n6_uniqueness_corrected :
    ∀ n : ℕ, 2 ≤ n →
      (σ 1 n * Nat.totient n = n * (Nat.divisors n).card ↔ n = 6) :=
  AX1_n6_uniqueness

end N6Mathlib.MechVerif
