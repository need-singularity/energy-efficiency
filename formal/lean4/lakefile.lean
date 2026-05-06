-- formal/lean4/lakefile.lean
--
-- Stub-layer build for the consumer-contract theorems consumed by hexa-bio
-- (lean4_mechanical_layer_v0.scaffold.md). Separate from the older
-- `lean4-n6/` package so the n=6 number-theory work and the formal-axis
-- consumer stubs evolve independently.

import Lake
open Lake DSL

package «n6-formal-stub» where
  -- Stub layer for axes F-CL-FORMAL-1..4. All four theorems carry `sorry`
  -- as proof body. raw_91 honest C3 disclosure: structural skeleton only.

lean_lib «N6» where
  roots := #[`N6.InvariantLattice.Sigma,
             `N6.InvariantLattice.SigmaLatticeCard,
             `N6.Weave.Strategy,
             `N6.Weave.LandauerMonotonic,
             `N6.Weave.PiP2Verifier,
             `N6.Weave.PiP2Termination,
             `N6.Weave.ClosureCert]

-- Mathlib pin (commit hash to attempt; may be replaced with a known-good
-- SHA in cycle-30+ once a proof body actually needs Mathlib lemmas). The
-- stub-layer theorems do not currently require Mathlib because all proof
-- bodies are `sorry`; the require below is included for future-proofing.
require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "master"
