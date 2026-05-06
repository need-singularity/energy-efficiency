-- N6.Weave.Strategy
--
-- Free-symbol stub for the Strategy / compose / heatConsumed / LandauerPass
-- vocabulary referenced by the F-CL-FORMAL-2 axis. Definitions here are
-- placeholders (opaque types + trivial functions) so the theorem statement
-- in `LandauerMonotonic.lean` typechecks. Replace with real semantics in
-- cycle-30+ canonical work.

namespace N6
namespace Weave

/-- Opaque Strategy type. Real definition: a sub-strategy in the WEAVE
    composition algebra (see `_python_bridge/module/weave_composition.py`
    on the consumer side). -/
structure Strategy where
  heat_kT : Nat
  deriving Repr

/-- Heat consumed by a strategy, in units of kT. Stub: project from the
    Strategy record. -/
def heatConsumed (s : Strategy) : Nat := s.heat_kT

/-- Compose two strategies. Stub: heat-additive composition. Real
    composition is non-trivial; this skeleton keeps statements typecheckable. -/
def compose (s₁ s₂ : Strategy) : Strategy :=
  { heat_kT := s₁.heat_kT + s₂.heat_kT }

/-- Predicate: a strategy passes the Landauer floor (heat ≥ kT·ln2 per
    erased bit). Stub: trivially true; real predicate enforces a numeric
    floor against an erasure count. -/
def LandauerPass (_s : Strategy) : Prop := True

end Weave
end N6
