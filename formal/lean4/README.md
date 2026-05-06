# formal/lean4 — consumer-contract stub layer

**Status (2026-05-06, cycle 25 closure):** STUB LANDED. All four axis
theorems carry `sorry` as proof body. **sorry-count = 4.**

## Purpose

This subtree is the canonical-side landing pad for the lean4 mechanical
layer consumed by `~/core/hexa-bio/`. The consumer's contract is recorded
upstream of this directory at:

- `~/core/hexa-bio/weave/spec/lean4_mechanical_layer_v0.scaffold.md`
- `~/core/hexa-bio/weave/spec/lean4_proof_witness_v0.schema.json`

Hexa-bio expects exactly the theorem names and module paths used here.
Renaming any declaration is a **breaking change** to the cross-repo
contract; coordinate via the consumer's scaffold spec promotion (v0 → v1).

## File map (axis → file)

| Axis           | Theorem                       | Module path                                | File                                                |
|:--             |:--                            |:--                                         |:--                                                  |
| F-CL-FORMAL-1  | `sigma_lattice_card`          | `N6.InvariantLattice.SigmaLatticeCard`     | `N6/InvariantLattice/SigmaLatticeCard.lean`         |
| F-CL-FORMAL-2  | `landauer_monotonic`          | `N6.Weave.LandauerMonotonic`               | `N6/Weave/LandauerMonotonic.lean`                   |
| F-CL-FORMAL-3  | `pi_p2_verifier_terminates`   | `N6.Weave.PiP2Termination`                 | `N6/Weave/PiP2Termination.lean`                     |
| F-CL-FORMAL-4  | `closure_cert_idempotent`     | `N6.Weave.ClosureCert`                     | `N6/Weave/ClosureCert.lean`                         |

Free-symbol stubs (`Sigma.lean`, `Strategy.lean`, `PiP2Verifier.lean`)
exist solely so the four theorem statements typecheck. Their definitions
are placeholders; replacing them is part of the cycle-30+ proof work.

## raw_91 honest C3 disclosure

This stub layer is a **structurally-correct skeleton**, not a verification.
Concretely:

- No proof body has been constructed. Every axis theorem ends in `sorry`.
- The supporting type definitions (`Strategy`, `StrandCatalogue`,
  `ClosureCert`) are placeholders, not the real WEAVE semantics. They keep
  the theorem statements typecheckable so the consumer-side witness emit
  script (`hexa-bio/_python_bridge/module/lean4_proof_witness_emit.py`) can
  grep for the declaration names without dangling references.
- `lakefile.lean` requires Mathlib at `master` but the stub theorems do not
  yet exercise it; the require is forward-looking. A reproducible Mathlib
  commit pin is not yet recorded — substitute one in cycle-30+ when the
  first real proof body lands.
- The PASS condition for any axis is `sorry_count == 0` on its theorem.
  Currently every axis is at `sorry_count == 1`. **No axis is PASS.**

This file (the README) is the formal raw_91 disclosure for the stub layer.

## Consumer (hexa-bio) integration points

- Witness emission: `_python_bridge/module/lean4_proof_witness_emit.py`
  (stdlib-only; reads each `.lean` file, counts `sorry` occurrences,
  emits one `raw_77_lean4_proof_witness_v0` row per axis into
  `state/discovery_absorption/registry.jsonl`).
- Roadmap entries:
  - `.roadmap.weave` §Falsifier preregister F-CL-FORMAL-1/2/3/4 — flipped
    from `DEFERRED — canonical work pending` to `STUB LANDED 2026-05-06
    (n6-architecture canonical, sorry-count=4)`.
  - `.roadmap.hexa_bio` §G GATE-26-2 — flipped from `SCAFFOLD LANDED` to
    `STUB LANDED (cross-repo, 4-sorry placeholder; actual proof bodies
    cycle 30+)`.

## Non-goals

- This README does **not** claim any formal correctness. It claims only
  that the file tree exists and that consumer-contract theorem names lock
  in for downstream witness emission.
- This stub layer does not replace or modify the existing `~/core/n6-architecture/lean4-n6/`
  number-theory package. The two coexist; this one (`formal/lean4/`) is
  scoped to the hexa-bio consumer contract.
