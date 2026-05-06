-- N6.Weave.LandauerMonotonic
--
-- Axis F-CL-FORMAL-2 — Landauer floor monotonicity under composition.
-- Consumer contract: hexa-bio expects theorem `landauer_monotonic`.
-- PROVEN-OVER-PLACEHOLDER 2026-05-06.
--
-- Pairs with: hexa-bio/weave/spec/lean4_mechanical_layer_v0.scaffold.md §2.2
-- Pairs with: .roadmap.weave §Falsifier preregister F-CL-FORMAL-2
--
-- raw_91 honest C3 disclosure:
--   Proof kernel-checked on lean4 4.30.0-rc1. PASS condition
--   (sorry_count = 0) MET. IMPORTANT caveat: the supporting `Strategy` /
--   `compose` / `heatConsumed` definitions in `Strategy.lean` are
--   SIMPLIFIED PLACEHOLDERS (heat-additive composition over Nat). The real
--   WEAVE composition semantics is non-additive and richer. This proof
--   verifies the STATEMENT-OVER-STUB-SEMANTICS, not the real-semantics
--   claim. Real-semantics version is a cycle-30+ work item.

import N6.Weave.Strategy

namespace N6
namespace Weave

/-- Axis F-CL-FORMAL-2: composing two Landauer-pass strategies cannot lower
    heat consumed below the max of the components. Proof: under stub
    semantics, heatConsumed (compose s₁ s₂) = s₁.heat_kT + s₂.heat_kT ≥
    max s₁.heat_kT s₂.heat_kT (Nat additivity). -/
theorem landauer_monotonic
    (s₁ s₂ : Strategy) (_h₁ : LandauerPass s₁) (_h₂ : LandauerPass s₂) :
    heatConsumed (compose s₁ s₂) ≥ max (heatConsumed s₁) (heatConsumed s₂)
  := by
    simp [heatConsumed, compose]
    omega

end Weave
end N6
