-- N6.InvariantLattice.SigmaLatticeCard
--
-- Axis F-CL-FORMAL-1 — σ(6) = 12 invariant.
-- Consumer contract: hexa-bio expects this theorem at the exact name
-- `sigma_lattice_card` so its lean4_proof_witness emit script can grep for
-- the symbol.
--
-- Pairs with: hexa-bio/weave/spec/lean4_mechanical_layer_v0.scaffold.md §2.1
-- Pairs with: .roadmap.weave §Falsifier preregister F-CL-FORMAL-1
--
-- raw_91 honest C3 disclosure (PROVEN 2026-05-06):
--   `sigma` is a computable Nat function (List.range + filter + foldl).
--   `sigma 6` reduces to 1+2+3+6 = 12 by definitional unfolding. The proof
--   body `rfl` succeeds because both sides reduce to the same Nat literal
--   under the kernel's reduction. PASS condition (sorry_count = 0) MET.
--   F-CL-FORMAL-1 PROMOTED stub → PROVEN.

import N6.InvariantLattice.Sigma

namespace N6
namespace InvariantLattice

/-- Axis F-CL-FORMAL-1: the σ-invariant cardinality at n=6 equals 12.
    Proof: definitional reduction (sigma 6 = 1+2+3+6 = 12). -/
theorem sigma_lattice_card : sigma 6 = 12 := rfl

end InvariantLattice
end N6
