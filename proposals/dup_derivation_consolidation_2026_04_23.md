# Dup-Derivation Consolidation Strategy — 2026-04-23

**source**: `reports/n6_roi.json` `findings.dup_derivation_candidates`
**roi-item**: `n6-roi-006` (priority 50, ROI 1.25)
**scanner refinement**: `tool/_n6_lib scan_roi` now scopes the
`sigma.*phi.*tau` regex to code extensions only (`.hexa|.py|.rs|.ts|.js|.go`).
Count dropped 30 (mixed markdown + code) → **18 real code duplicates**.

## Inventory — the 18 files that re-inline the n=6 constants

All 18 are per-domain `verify_*.hexa` (or equivalent RTL driver) that
hardcode `let sigma = 12`, `let tau = 4`, `let phi = 2` and assert the
n=6 identity. They do this because the current hexa stage does not
support stable cross-unit `import` / `include` of typed constants
(language gap forwarded as `hxa-20260422-00?`).

| Domain                                    | File                                                                      |
| ------------------------------------------ | ------------------------------------------------------------------------- |
| cognitive/brain-computer-interface         | `verify_brain-computer-interface.hexa`                                    |
| cognitive/hexa-speak (RTL)                 | `proto/rtl/soc_integration.hexa`                                          |
| cognitive/hexa-speak (RTL)                 | `proto/rtl/tapeout_gate.hexa`                                             |
| cognitive/hexa-speak (RTL)                 | `proto/rtl/intent_encoder.hexa`                                           |
| cognitive/hexa-speak (RTL)                 | `proto/rtl/top.hexa`                                                      |
| energy/room-temp-sc                        | `tabletop-fusion-verify.hexa`                                             |
| compute/chip-hexa1                         | `verify_chip-hexa1.hexa`                                                  |
| compute/chip-pim                           | `verify_chip-pim.hexa`                                                    |
| compute/mouse                              | `hexa_mouse.hexa`                                                         |
| compute/chip-design/hexa-quantum-hybrid    | `verify_chip-quantum-hybrid.hexa`                                         |
| compute/chip-design/hexa-1-digital         | `verify_chip-hexa1-digital.hexa`                                          |
| compute/chip-design/hexa-2-pim             | `verify_chip-hexa2-pim.hexa`                                              |
| compute/chip-design/hexa-photon-topo       | `verify_chip-photon-topo.hexa`                                            |
| compute/chip-design/hexa-neuromorphic      | `verify_chip-neuromorphic.hexa`                                           |
| compute/chip-design/hexa-dna-molecular     | `verify_chip-dna-molecular.hexa`                                          |
| compute/chip-design/hexa-topo-anyon        | `verify_chip-topo-anyon.hexa`                                             |
| compute/chip-design/hexa-superconducting   | `verify_chip-superconducting.hexa`                                        |
| physics/millennium-riemann                 | `verify_millennium-riemann.hexa`                                          |

## Decision — preserve the inlining, promote a SSOT

We intentionally **do not** refactor the 18 files today. The rationale:

1. **Self-containment** is a design property: each `verify_<domain>.hexa`
   must be runnable in isolation (`hexa run path/to/verify.hexa`) as the
   per-domain audit trail. Breaking it would couple auditability to the
   import graph.
2. **Hexa import is not stable yet** — forwarded to hexa-lang as a
   `lang_gap` (n6a-20260422-003 convention).
3. **Divergence risk is low** — the six constants (n, sigma, tau, phi,
   sopfr, j2) are deliberately tiny and self-falsifying: if any single
   file drifts, its `assert(sigma * phi == n * tau)` fails on run.

What we ship instead:

- **Canonical SSOT file**: `atlas/n6_core_constants.hexa`. Treat this
  as the reviewer's diff target when any of the 18 files changes.
- **Scanner refinement**: `dup_derivation_candidates` already filtered
  to code extensions; markdown references no longer inflate the count.

## Follow-up when hexa import lands

When hexa stage supports `import`/`use`, the 18 files become:

```hexa
use atlas::n6_core_constants::{n, sigma, tau, phi};

fn main() {
    // domain-specific assertions only; constants pulled from SSOT
    ...
}
```

That refactor is gated on the hexa-lang side and should be proposed as
`n6-roi-006b` once unblocked.

## Verification

```
bash bin/n6_meta roi
jq '.findings.dup_derivation_candidates | length' reports/n6_roi.json
# Post-refinement: 18 (real code files, not markdown)
```

The count of 18 is now stable and documents a design choice, not a bug.
