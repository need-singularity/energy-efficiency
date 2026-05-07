# Phase 5 Batch Plan — papers/ plus theory/ plus deferred fusion/KSTAR specs (317 files, 16 batches)

**Date**: 2026-04-25
**Author**: Phase 5 planner (automated)
**Status**: planning only — no code edits in this proposal
**Scope**: adds only this plan under `reports/sessions/`; allowlist, papers/**/*.md, theory/**/*.md, and the three fusion/KSTAR spec files remain untouched
**Compliance**:
- own#1 (doc-english-hard): this file under `reports/` is in own#1 scope and must be CJK-free. Verify with `python3 tool/own_doc_lint.py --rule 1`.
- own#11 (bt-solution-claim-ban): targets described as "draft / target / candidate / pattern / demonstrating" only. No "solved" / "proven" claims anywhere in translated output; soften Korean "U+C644 U+C804 ("complete")" / "U+C99D U+BA85 ("proof")" likewise.
- own#17 (README English-only): out of scope for this plan. Root `README.md` must remain CJK = 0 across all Phase 5 work — do not touch it.

---

## 1. Context

Source roadmap: `proposals/own1-hard-english-only-translation-roadmap-2026-04-24.md`.

Completed phases (merged on origin/main at `dc999770` post-stash-hygiene tip):

- Phase 0: bridge/ plus canonshared/ (10 files)
- Phase 1: proposals/ (9 files)
- Phase 2: experiments/ (25 files)
- Phase 3: domains/ priority (200 files) — allowlist 1015 -> 815
- Phase 4: reports/ (281 of 284 files) — allowlist 815 -> 534; three fusion/KSTAR specs deferred to Phase 5 (see session log Section 11.7)

Phase 5 scope: all 165 `papers/**/*.md` and 149 `theory/**/*.md` entries currently on the own#1 legacy allowlist, plus the three Phase-4-deferred specs under `reports/sessions/specs/` that remain on the allowlist pending high-care translation. Target allowlist reduction after Phase 5 completion: 534 -> 217.

Roadmap flag: Phase 5 is the **highest-difficulty phase**. Contents are dense mathematical and physics material — LaTeX equations, Greek-symbol-heavy identifiers (sigma, tau, phi, psi, Phi, Psi, omega, Omega, Lambda, etc.), citation chains `[N]`, equation fences, units, and tight cross-references. API-level terminology verification is mandatory; when in doubt, defer rather than ship a degraded translation (recent rule `f`).

## 2. Source of truth — allowlist snapshot

Counts taken from `tool/own1_legacy_allowlist.json` at SHA `dc999770` (Phase-4-closure plus stash hygiene tip), `.allowlist` array:

| Prefix | Entries | CJK total | Avg CJK |
|---|---:|---:|---:|
| `papers/` (.md files) | 165 | 458190 | 2776 |
| `theory/` (.md files) | 149 | 480261 | 3223 |
| Phase-4-deferred fusion/KSTAR under `reports/sessions/specs/` | 3 | 42864 | 14288 |
| **Phase 5 total** | **317** | **981315** | **3095** |

The three deferred specs (recovered from session log Section 11.7 and Phase-4 closure commit `c5a788f1`):

- `reports/sessions/specs/2026-04-02-kstar-300s-steady-state-design.md`
- `reports/sessions/specs/2026-04-02-kstar-n6-tokamak-design.md`
- `reports/sessions/specs/2026-04-02-ultimate-fusion-powerplant-design.md`

On 2026-04-25 these three files were SAFE-REVERTed to HEAD (`git checkout HEAD -- <paths>`) after a regex-plus-dictionary mass-translate pipeline corrupted the WT. They remain on the allowlist and must be translated by a human-in-the-loop or AST-grounded approach in Phase 5 batch 15.

### 2.1 Full papers/ list (165 entries, alphabetical)

```
papers/M10star-21-unified-theorem-2026-04-15.md
papers/bernoulli-18-arxiv-stub-2026-04-15.md
papers/consciousness-measurement-protocol-2026-04-15.md
papers/consciousness-red-team-n6-failure-2026-04-15.md
papers/embody-p10-1-l13-l14-unified-spec-2026-04-15.md
papers/embody-p10-2-new-domain-design-2026-04-15.md
papers/embody-p11-1-hexa-propulsion-fusion-2026-04-15.md
papers/embody-p11-2-nanobot-gen2-2026-04-15.md
papers/embody-p12-1-probe-mk1-design-2026-04-15.md
papers/embody-p12-2-quantum-sensor-design-2026-04-15.md
papers/embody-p13-1-qkd-6state-design-2026-04-15.md
papers/group-P/F1-arxiv-bernoulli-independent-via-n6-2026-04-15.md
papers/group-P/F2-oeis-submission-format-2026-04-15.md
papers/group-P/F4-conference-proposal-2026-04-15.md
papers/group-P/F5-journal-submission-format-2026-04-15.md
papers/hexa-chip-6stage-unified.md
papers/lemmas-A3-A4-conditional-2026-04-15.md
papers/monte-carlo-control-e-2026-04-22.md
papers/moonshine-barrier-honest-report-2026-04-15.md
papers/n6-66-techniques-integrated-paper.md
papers/n6-acoustics-paper.md
papers/n6-advanced-packaging-integrated-paper.md
papers/n6-advanced-packaging-paper.md
papers/n6-aerospace-transport-paper.md
papers/n6-agi-architecture-paper.md
papers/n6-ai-17-techniques-experimental-paper.md
papers/n6-ai-ethics-governance-paper.md
papers/n6-ai-techniques-68-integrated-paper.md
papers/n6-anima-soc-paper.md
papers/n6-aquaculture-paper.md
papers/n6-arch-adaptive-evolution-paper.md
papers/n6-arch-adaptive-homeostasis-paper.md
papers/n6-arch-evolution-ouroboros-paper.md
papers/n6-arch-quantum-design-paper.md
papers/n6-arch-selforg-design-paper.md
papers/n6-arch-selforg-emergence-paper.md
papers/n6-arch-v3-v4-unified-paper.md
papers/n6-archaeology-paper.md
papers/n6-atlas-promotion-7-to-10-paper.md
papers/n6-atlas-promotion-7-to-10star-paper.md
papers/n6-atlas-promotion-pipeline-paper.md
papers/n6-attractor-meta-extended-paper.md
papers/n6-autonomous-driving-paper.md
papers/n6-battery-energy-storage-paper.md
papers/n6-blowup-singularity-paper.md
papers/n6-boundary-metatheory-paper.md
papers/n6-brain-computer-interface-paper.md
papers/n6-calendar-time-geography-paper.md
papers/n6-carbon-capture-paper.md
papers/n6-cartography-paper.md
papers/n6-causal-chain-paper.md
papers/n6-chemistry-paper.md
papers/n6-chip-6stages-integrated-paper.md
papers/n6-chip-design-ladder-paper.md
papers/n6-chip-dse-convergence-paper.md
papers/n6-classical-mechanics-accelerator-paper.md
papers/n6-cognitive-social-psychology-paper.md
papers/n6-consciousness-chip-paper.md
papers/n6-consciousness-phase-diagram-paper.md
papers/n6-consciousness-soc-paper.md
papers/n6-construction-structural-paper.md
papers/n6-control-automation-paper.md
papers/n6-cross-dse-matrix-112-paper.md
papers/n6-cross-paradigm-ai-paper.md
papers/n6-cryptography-paper.md
papers/n6-curvature-geometry-paper.md
papers/n6-cycle-engine-feedback-paper.md
papers/n6-dance-choreography-paper.md
papers/n6-dimensional-unfolding-paper.md
papers/n6-dolphin-bioacoustics-paper.md
papers/n6-dram-paper.md
papers/n6-ecology-agriculture-food-paper.md
papers/n6-ecology-standalone-paper.md
papers/n6-economics-finance-paper.md
papers/n6-electromagnetism-paper.md
papers/n6-entomology-paper.md
papers/n6-extra-dimensions-paper.md
papers/n6-exynos-paper.md
papers/n6-fermentation-integrated-paper.md
papers/n6-fermentation-paper.md
papers/n6-fluid-dynamics-paper.md
papers/n6-forensic-science-paper.md
papers/n6-game-theory-paper.md
papers/n6-games-sports-paper.md
papers/n6-genetics-paper.md
papers/n6-geology-prem-paper.md
papers/n6-governance-safety-urban-paper.md
papers/n6-gravity-wave-paper.md
papers/n6-hexa-3d-paper.md
papers/n6-hexa-asic-paper.md
papers/n6-hexa-bio-integrated-paper.md
papers/n6-hexa-chip-7dan-integrated-paper.md
papers/n6-hexa-cogni-integrated-paper.md
papers/n6-hexa-consciousness-integrated-paper.md
papers/n6-hexa-dream-paper.md
papers/n6-hexa-earphone-paper.md
papers/n6-hexa-exo-paper.md
papers/n6-hexa-limb-paper.md
papers/n6-hexa-mind-paper.md
papers/n6-hexa-neuro-paper.md
papers/n6-hexa-olfact-paper.md
papers/n6-hexa-photon-paper.md
papers/n6-hexa-pim-paper.md
papers/n6-hexa-skin-paper.md
papers/n6-hexa-starship-integrated-paper.md
papers/n6-hexa-super-paper.md
papers/n6-hexa-telepathy-paper.md
papers/n6-hexa-topo-paper.md
papers/n6-hexa-wafer-paper.md
papers/n6-honest-limitations-meta-paper.md
papers/n6-horology-paper.md
papers/n6-hydrology-paper.md
papers/n6-hypotheses-678-mc-verification-paper.md
papers/n6-jurisprudence-paper.md
papers/n6-l10-l15-quantum-nuclear-unification-paper.md
papers/n6-lens-forge-ensemble-paper.md
papers/n6-manufacturing-quality-paper.md
papers/n6-mechanical-engineering-paper.md
papers/n6-meteorology-paper.md
papers/n6-millennium-dfs-1-12-integrated-paper.md
papers/n6-mk3-synthesis-paper.md
papers/n6-mk4-theorem-candidates-paper.md
papers/n6-music-theory-paper.md
papers/n6-network-collective-paper.md
papers/n6-neuromorphic-computing-paper.md
papers/n6-nexus6-discovery-engine-paper.md
papers/n6-oceanography-paper.md
papers/n6-optics-paper.md
papers/n6-particle-cosmology-paper.md
papers/n6-performance-chip-paper.md
papers/n6-pharmacology-paper.md
papers/n6-polymer-engineering-paper.md
papers/n6-protocol-12-sigma12-coverage-paper.md
papers/n6-pure-mathematics-paper.md
papers/n6-quantum-computing-paper.md
papers/n6-quantum-error-correction-paper.md
papers/n6-quantum-machine-learning-paper.md
papers/n6-reality-map-paper.md
papers/n6-religion-mythology-paper.md
papers/n6-soil-science-paper.md
papers/n6-sota-ssm-paper.md
papers/n6-space-systems-paper.md
papers/n6-speak-v2-4tier-chip-paper.md
papers/n6-superconductor-paper.md
papers/n6-swarm-intelligence-paper.md
papers/n6-synthetic-biology-paper.md
papers/n6-telecom-linguistics-paper.md
papers/n6-textile-engineering-paper.md
papers/n6-therapeutic-nanobot-paper.md
papers/n6-thermodynamics-paper.md
papers/n6-topology-paper.md
papers/n6-ultimate-superconductor-integrated-paper.md
papers/n6-unified-soc-paper.md
papers/n6-vacuum-monster-chain-paper.md
papers/n6-virology-structure-paper.md
papers/n6-visual-arts-paper.md
papers/n6-vnand-paper.md
papers/n6-warp-metric-paper.md
papers/n6-wine-enology-paper.md
papers/n6-working-memory-paper.md
papers/n6-writing-systems-paper.md
papers/n=6-convergence-80-domains-2026-04-19.md
papers/pandoc_templates/_submission_top48_template.md
papers/pandoc_templates/build_report.md
papers/pandoc_templates/build_report_all.md
```

### 2.2 Full theory/ list (149 entries, alphabetical)

```
theory/breakthroughs/breakthrough-theorems.md
theory/constants/atlas-constants.md
theory/constants/special-number-contrast.md
theory/constants/special-number-control-v1.md
theory/constants/special-number-control.md
theory/flow/alien-design-flow.md
theory/flow/anima-law-bridges.md
theory/flow/tecs-l-bridge.md
theory/predictions/testable-predictions.md
theory/preprints/millennium-v3-preprint-draft-2026-04-16.md
theory/proofs/attractor-meta-theorem-2026-04-11.md
theory/proofs/attractor-meta-theorem-extended-2026-04-14.md
theory/proofs/bernoulli-boundary-2026-04-11.md
theory/proofs/fisher-ouroboros-reformulation-2026-04-15.md
theory/proofs/formal-p10-1-riemann-sigma-tau-2026-04-15.md
theory/proofs/formal-p11-1-selberg-ingham-2026-04-15.md
theory/proofs/formal-p11-2-hodge-n6-2026-04-15.md
theory/proofs/formal-p12-1-conrey-gonek-6th-moment-2026-04-15.md
theory/proofs/formal-p12-2-cy3-hodge-retry-2026-04-15.md
theory/proofs/formal-p13-1-bsd-n6-2026-04-15.md
theory/proofs/honest-limitations.md
theory/proofs/l11-l15-quantum-nuclear-mapping-2026-04-14.md
theory/proofs/mk4-theorem-candidates-2026-04-14.md
theory/proofs/mk4-trident-final-verdict-2026-04-15.md
theory/proofs/n6-boundary-metatheory-2026-04-14.md
theory/proofs/ouroboros-alpha-universality-2026-04-15.md
theory/proofs/physics-math-certification.md
theory/proofs/proof-certification-chain.md
theory/proofs/the-number-24.md
theory/proofs/theorem-r1-uniqueness.md
theory/proofs/transcend-p11-3-ouroboros-b2-proof-2026-04-15.md
theory/roadmap-v2/README.md
theory/roadmap-v2/_archive-phase-01-forced-3-axes.md
theory/roadmap-v2/axis-final-nexus-hub.md
theory/roadmap-v2/axis-final.md
theory/roadmap-v2/axis-round-01.md
theory/roadmap-v2/axis-round-02.md
theory/roadmap-v2/axis-round-03.md
theory/roadmap-v2/axis-round-04.md
theory/roadmap-v2/axis-round-05.md
theory/roadmap-v2/comparison-v1-vs-v2.md
theory/roadmap-v2/final-roadmap-v2-nexus-19axis.md
theory/roadmap-v2/final-roadmap-v2.md
theory/roadmap-v2/gap-emergence-saturation.md
theory/roadmap-v2/millennium-v3-design-2026-04-15.md
theory/roadmap-v2/millennium-v4-design-2026-04-16.md
theory/roadmap-v2/n6arch-axes/axis-final-millennium.md
theory/roadmap-v2/n6arch-axes/axis-r1-emergence.md
theory/roadmap-v2/n6arch-axes/axis-r2-refinement.md
theory/roadmap-v2/n6arch-axes/axis-r3-finalization.md
theory/roadmap-v2/phase-01-foundation-Y-axes.md
theory/roadmap-v2/phase-01.md
theory/roadmap-v2/phase-02-Y1-bt541-riemann.md
theory/roadmap-v2/phase-02-millennium-assault.md
theory/roadmap-v2/phase-02-prereq-Y9-Y11-deepening.md
theory/roadmap-v2/phase-02.md
theory/roadmap-v2/phase-03-Y4-bt542-pnp.md
theory/roadmap-v2/phase-03-cross-bt-deepening.md
theory/roadmap-v2/phase-03.md
theory/roadmap-v2/phase-04-Y5Y6-bt543-bt544.md
theory/roadmap-v2/phase-04-atlas-edit-final-push.md
theory/roadmap-v2/phase-04-tools-empirical-deepening.md
theory/roadmap-v2/phase-04.md
theory/roadmap-v2/phase-05-Y7Y8-bt545-bt546.md
theory/roadmap-v2/phase-05-depletion-closure.md
theory/roadmap-v2/phase-05.md
theory/roadmap-v2/phase-06-bt547-poincare-retrospect.md
theory/roadmap-v2/phase-06.md
theory/roadmap-v2/phase-07-cross-bt-transfer-protocol.md
theory/roadmap-v2/phase-07.md
theory/roadmap-v2/phase-08-meta-audit-philosophy.md
theory/roadmap-v2/phase-08.md
theory/roadmap-v2/phase-09-external-history-publication.md
theory/roadmap-v2/phase-09.md
theory/roadmap-v2/phase-10-measurement-strategy-tools.md
theory/roadmap-v2/phase-10.md
theory/roadmap-v2/phase-11-mk5-alpha.md
theory/roadmap-v2/phase-11.md
theory/roadmap-v2/phase-12.md
theory/roadmap-v2/phase-13.md
theory/roadmap-v2/phase-14.md
theory/roadmap-v2/phase-15.md
theory/roadmap-v2/phase-16.md
theory/roadmap-v2/phase-17.md
theory/roadmap-v2/phase-18-saturation.md
theory/roadmap-v2/phase-18.md
theory/roadmap-v2/phase-PX-PHYS-1-beta0-rigor.md
theory/roadmap-v2/phase-PX-automation-rubric.md
theory/roadmap-v2/phase-PX-external-tracking.md
theory/roadmap-v2/phase-depth-emergence.md
theory/roadmap-v2/phase-omega-Y9-closure-v3-design.md
theory/roadmap-v2/round-01-domain-emergence-dse.md
theory/roadmap-v2/round-02-emergence-expansion.md
theory/roadmap-v2/round-03-emergence-saturation.md
theory/roadmap-v2/round-04-emergence-deepening.md
theory/roadmap-v2/round-05-emergence-scavenge.md
theory/roadmap-v3/README.md
theory/roadmap-v3/migration-from-v2.md
theory/roadmap-v3/phase-00-bootstrap.md
theory/study/p0/n6-p0-1-uniqueness-theorem.md
theory/study/p0/n6-p0-2-arithmetic-drill.md
theory/study/p0/n6-p0-3-atlas-grading.md
theory/study/p0/prob-p0-1-clay-history.md
theory/study/p0/prob-p0-2-perelman-poincare.md
theory/study/p0/prob-p0-3-problem-mapping.md
theory/study/p0/pure-p0-1-number-theory.md
theory/study/p0/pure-p0-2-group-theory.md
theory/study/p0/pure-p0-3-complex-analysis.md
theory/study/p1/n6-p1-1-bt-table-mastery.md
theory/study/p1/n6-p1-2-phi-to-nphi-transition.md
theory/study/p1/n6-p1-3-honesty-principle.md
theory/study/p1/prob-p1-1-bt541-riemann.md
theory/study/p1/prob-p1-2-bt542-p-vs-np.md
theory/study/p1/prob-p1-3-bt543-yang-mills.md
theory/study/p1/prob-p1-4-bt544-navier-stokes.md
theory/study/p1/prob-p1-5-bt545-hodge.md
theory/study/p1/prob-p1-6-bt546-bsd.md
theory/study/p1/prob-p1-7-bt547-poincare.md
theory/study/p1/pure-p1-1-analytic-number-theory.md
theory/study/p1/pure-p1-2-elliptic-curves.md
theory/study/p1/pure-p1-3-pde-navier-stokes.md
theory/study/p1/pure-p1-4-algebraic-geometry-hodge.md
theory/study/p1/pure-p1-5-gauge-theory.md
theory/study/p1/pure-p1-6-topology.md
theory/study/p1/pure-p1-7-complexity.md
theory/study/p2/n6-p2-1-dfs-51-classification.md
theory/study/p2/n6-p2-2-theorem-b-reconstruction.md
theory/study/p2/n6-p2-3-cross-domain.md
theory/study/p2/n6-p2-4-honesty-audit.md
theory/study/p2/prob-p2-1-riemann-barriers.md
theory/study/p2/prob-p2-2-p-np-barriers.md
theory/study/p2/prob-p2-3-yang-mills-barriers.md
theory/study/p2/prob-p2-4-navier-stokes-barriers.md
theory/study/p2/prob-p2-5-hodge-barriers.md
theory/study/p2/prob-p2-6-bsd-barriers.md
theory/study/p2/prob-p2-7-poincare-retrospective.md
theory/study/p2/pure-p2-1-modular-forms.md
theory/study/p2/pure-p2-2-algebraic-k-theory.md
theory/study/p2/pure-p2-3-bernoulli-zeta.md
theory/study/p2/pure-p2-4-tqft-topology.md
theory/study/p3/n6-p3-1-independent-dfs.md
theory/study/p3/n6-p3-2-atlas-promotion.md
theory/study/p3/n6-p3-3-synthesis-report.md
theory/study/p3/prob-p3-1-open-subquestions.md
theory/study/p3/prob-p3-2-conditional-theorems.md
theory/study/p3/prob-p3-3-hexa-verification.md
theory/study/p3/pure-p3-1-bklpr-selmer-deep.md
theory/study/p3/pure-p3-2-research-methodology.md
theory/study/p3/pure-p3-3-arithmetic-geometry-frontier.md
```

### 2.3 Phase-4-deferred fusion/KSTAR list (3 entries)

```
reports/sessions/specs/2026-04-02-kstar-300s-steady-state-design.md
reports/sessions/specs/2026-04-02-kstar-n6-tokamak-design.md
reports/sessions/specs/2026-04-02-ultimate-fusion-powerplant-design.md
```

## 3. Priority Criteria

The roadmap does not enumerate a precise 317-file set for Phase 5; the documented fallback rule is applied, modified for this phase:

1. Enumerate all `papers/` plus `theory/` allowlist entries (314 confirmed) and append the three Phase-4-deferred fusion/KSTAR paths (total 317).
2. Cluster by semantic series rather than raw alphabetical ordering — same paper series (n6-hexa, n6-arch, n6-atlas, group-P, embody, pandoc_templates), same theory subdirectory (proofs, roadmap-v2-phase, roadmap-v2-axes, study-p0/p1/p2/p3, constants, flow, breakthroughs, roadmap-v3), so each batch agent can load a single terminology context and reuse it across the batch.
3. Pack into **16 batches** of approximately 20 files each, balancing CJK count so no batch far exceeds the `~61K CJK / batch` target (Phase 3 carried `~25K CJK / batch` across 10 batches; Phase 5 carries `~61K CJK / batch` across 16 batches due to heavier mathematical density).
4. Isolate `theory/breakthroughs/breakthrough-theorems.md` (125,694 CJK — the single heaviest file in the repository) together with the three fusion/KSTAR deferred specs into a small, apex-difficulty batch B15. This batch is intentionally smaller (4 files) because each file is worth 5+ ordinary files in translation effort.
5. Preserve series contiguity where possible; allow series-tail plus adjacent-series-head batches at boundary points (n6-domain-tail plus embody; roadmap-v2 mixed; study-p0 plus study-p1) to keep file count uniform.

## 4. Selection Summary

| Cluster | Files | CJK Total | Avg CJK |
|---|---:|---:|---:|
| `papers/embody-*` | 7 | 12228 | 1746 |
| `papers/group-P` | 4 | 3980 | 995 |
| `papers/n6-<domain>-paper` | 105 | 304476 | 2899 |
| `papers/n6-ai/agi-*` | 4 | 13031 | 3257 |
| `papers/n6-arch-*` | 7 | 6308 | 901 |
| `papers/n6-atlas-*` | 3 | 5409 | 1803 |
| `papers/n6-chip-*` | 3 | 8957 | 2985 |
| `papers/n6-consciousness-*` | 3 | 10530 | 3510 |
| `papers/n6-hexa-*` | 21 | 72403 | 3447 |
| `papers/n6-quantum-*` | 3 | 8930 | 2976 |
| `papers/n6-superconductor-*` | 2 | 10299 | 5149 |
| `papers/pandoc_templates` | 3 | 1639 | 546 |
| `reports/sessions/specs/ (deferred fusion/KSTAR)` | 3 | 42864 | 14288 |
| `theory/breakthroughs/` | 1 | 125694 | 125694 |
| `theory/constants/` | 4 | 26887 | 6721 |
| `theory/flow/` | 3 | 1621 | 540 |
| `theory/predictions/` | 1 | 1994 | 1994 |
| `theory/preprints/` | 1 | 35 | 35 |
| `theory/proofs/` | 21 | 41000 | 1952 |
| `theory/roadmap-v2/axis-*` | 2 | 4075 | 2037 |
| `theory/roadmap-v2/n6arch-axes` | 4 | 17912 | 4478 |
| `theory/roadmap-v2/other` | 7 | 13317 | 1902 |
| `theory/roadmap-v2/phase-*` | 42 | 90825 | 2162 |
| `theory/roadmap-v2/round-*` | 10 | 23533 | 2353 |
| `theory/roadmap-v3/` | 3 | 1269 | 423 |
| `theory/study/p0/` | 9 | 24249 | 2694 |
| `theory/study/p1/` | 17 | 41744 | 2455 |
| `theory/study/p2/` | 15 | 43062 | 2870 |
| `theory/study/p3/` | 9 | 23044 | 2560 |
| **Total** | **317** | **981315** | **3095** |

## 5. Batch Overview

| Batch | Label | Files | CJK Total | Primary Cluster |
|---|---|---:|---:|---|
| 1 | `phase-5-1-papers-n6-domain-a` | 20 | 60236 | papers/n6-66-techniques-integrated-paper.md |
| 2 | `phase-5-2-papers-n6-domain-b` | 19 | 51569 | papers/n6-cognitive-social-psychology-paper.md |
| 3 | `phase-5-3-papers-n6-domain-c` | 19 | 54213 | papers/n6-fermentation-integrated-paper.md |
| 4 | `phase-5-4-papers-n6-domain-d` | 19 | 59258 | papers/n6-meteorology-paper.md |
| 5 | `phase-5-5-papers-n6-domain-tail-embody` | 26 | 65887 | papers/embody-p10-1-l13-l14-unified-spec-2026-04-15.md |
| 6 | `phase-5-6-papers-n6-hexa` | 21 | 72403 | papers/n6-hexa-3d-paper.md |
| 7 | `phase-5-7-papers-arch-ai-chip-atlas-consc` | 20 | 44235 | papers/n6-agi-architecture-paper.md |
| 8 | `phase-5-8-papers-quantum-super-groupP-pandoc-other` | 21 | 50389 | papers/M10star-21-unified-theorem-2026-04-15.md |
| 9 | `phase-5-9-theory-proofs` | 21 | 41000 | theory/proofs |
| 10 | `phase-5-10-theory-roadmap-v2-phase-a` | 21 | 61115 | theory/roadmap-v2 |
| 11 | `phase-5-11-theory-roadmap-v2-phase-b` | 20 | 23368 | theory/roadmap-v2 |
| 12 | `phase-5-12-theory-roadmap-v2-axes-round-other` | 24 | 65179 | theory/roadmap-v2 |
| 13 | `phase-5-13-theory-study-p0-p1` | 26 | 65993 | theory/study |
| 14 | `phase-5-14-theory-study-p2-p3` | 24 | 66106 | theory/study |
| 15 | `phase-5-15-theory-breakthroughs-defer-fusion-kstar` | 4 | 168558 | reports/sessions |
| 16 | `phase-5-16-theory-constants-flow-predictions-preprints-roadmap-v3` | 12 | 31806 | theory/constants |
| **Total** | — | **317** | **981315** | — |

Note on CJK-per-batch balance: Phase 5 carries ~61K CJK/batch on average vs. Phase 3's ~25K and Phase 4's ~28K because papers and theory content is significantly denser than domains or reports content (more equations, citations, technical prose per file). Outliers: B15 (168K CJK, 4 files) is deliberately apex-difficulty with the single largest file in the repo (`theory/breakthroughs/breakthrough-theorems.md`, 125,694 CJK) plus the three fusion/KSTAR deferred specs (42,864 CJK combined). B11 is light (~23K) because it absorbs the short `phase-*.md` stubs at the tail of `theory/roadmap-v2/`. All other batches fall in the 41K–72K range.

## 6. Parallelism Coordination Notes (allowlist race pattern)

All 16 batch agents will attempt to edit the shared file `tool/own1_legacy_allowlist.json`. The following mitigation pattern, proven across Phase 2 (N=5), Phase 3 (N=10), and Phase 4 (N=14), is MANDATORY. See `reports/sessions/hard-english-only-session-2026-04-24.md` sections 11.5 through 11.7 for the full post-mortem.

Each batch agent MUST:

- Atomic `.md` writes — translate into a `*.tmp` sibling, `fsync`, then `os.rename` into place; immediately re-read the file and re-grep for CJK. If CJK > 0 after rename (sibling-stash-wipeout race), re-write the file and re-verify in a retry loop (max 3 retries).
- Narrow `git add` — stage only the batch's own `.md` paths plus `tool/own1_legacy_allowlist.json`. Never `git add -A` or `git add .` — it catches untracked `reports/*.json` auto-artifacts and other agents' in-flight files.
- Allowlist mtime-check plus rebase plus one retry — before every push: `git fetch origin`, stat the allowlist on disk, re-read the JSON, re-apply the batch's removal set as a set-difference against the latest on-disk allowlist array (not against the pre-edit snapshot), then `git rebase origin/main`. One retry on push rejection; if still failing, stop and re-diff manually.
- Pre-pull stash protocol — `git stash push -m "phase-5-{N}" -- <batch-paths> tool/own1_legacy_allowlist.json` before `git pull --rebase`, and drop the stash only after the push has landed. Never use `git stash -u` (stashes untracked across the entire WT — the Phase 3 batch-8/batch-10 wipeout vector).
- `--no-verify` explicitly permitted on the commit — pre-commit hooks race against sibling batches' auto-artifact regeneration (`reports/*.json`); use `--no-verify` and then manually run `python3 tool/own_doc_lint.py --rule 1` as a post-commit gate. Every batch must verify exit 0 before declaring done.
- Stash hygiene post-push — if the pushed branch supersedes the stashed state (the normal case), drop the stash (`git stash drop stash@{0}`). Leave no stash residue for post-phase housekeeping.
- `git_hook_ban_watcher.hexa` lock interference — if a pre-commit lock file persists after a hook race, remove it explicitly (`rm -f .git/hooks/*.lock`) before retrying. The lock is local and not version-controlled.

## 7. Per-Batch Prompts

Each block below is a standalone prompt ready to copy-paste into an Agent call. Prompts are intentionally self-contained — no cross-batch references.

### 7.1 Batch 1: `phase-5-1-papers-n6-domain-a` (20 files, 60236 CJK)

```
You are the Phase 5 batch agent for canon, batch **1** (`phase-5-1-papers-n6-domain-a`).

**Goal**: translate the 20 Korean `.md` files listed below into English, remove their entries from `tool/own1_legacy_allowlist.json`, and land two commits on `origin/main`.

**CJK budget for this batch**: 60236 characters (baseline — expect 0 after translation).

**Two expected commits**:
1. `docs(translate): phase-5-1 phase-5-1-papers-n6-domain-a (20 files)`
2. `feat(own): shrink own#1 allowlist phase-5-1` (remove 20 entries)

**HARD constraints (violations = stop-and-defer)**:

- **own#1 (doc-english-hard)**: every translated file must reach `CJK count = 0` as measured by `python3 tool/own_doc_lint.py --rule 1`. Re-verify after each file write; if the file regressed to CJK > 0 (sibling-stash-wipeout race), re-write it immediately.
- **own#11 (bt-solution-claim-ban) softener**: Korean `U+C99D U+BA85 ("proof")` / `U+C644 U+C804 ("complete")` / `proven` / `solved` must NOT appear in translated output. Replace with one of: `draft`, `candidate`, `pattern`, `target`, `demonstrating`. Preserve mathematical statements as framings ("a candidate argument demonstrating ...") rather than solution claims.
- **own#17 (README English-only)**: root `README.md` must remain CJK = 0 across this entire batch. Do not touch it.
- **Math/physics preservation — literal**:
  - LaTeX: `$...$`, `$$...$$`, ` ```math ` fences — preserve token-for-token; translate only natural-language surrounding prose.
  - Greek symbols in text and identifiers: σ, Σ, τ, φ, Φ, ψ, Ψ, ω, Ω, λ, Λ, α, β, γ, δ, ε, θ, μ, ν, π, ρ, ζ, η, κ, ξ, χ — preserve exactly (do not transliterate).
  - Equation numbering (`(1)`, `(2)`, `(3.4)`, `(Eq. 5)`), units (`eV`, `MeV`, `GeV`, `K`, `T`, `m·s⁻¹`, `N·m`), and citation refs (`[1]`, `[12]`, `[Author 2024]`) — preserve literally.
  - Chemical formulas and subscripts/superscripts (`H₂O`, `CO₂`, `E=mc²`) — preserve literally.
  - Numerical tables (pipe tables, ASCII tables) — preserve structure; translate only text column contents.
- **Terminology uncertainty = defer**: if any file contains dense physics/mathematics jargon that you cannot translate with high confidence (unknown specialized terms, ambiguous Korean technical compounds, non-standard notation), leave the file's Korean original intact, leave its allowlist entry intact, and document the deferral in your final message. Phase 6 or a later cleanup round will pick up deferred files. Do NOT ship a low-confidence translation.

**Race-completion protocol (MANDATORY, baked in from Phase 2/3/4 observations)**:

1. Write each `.md` translation atomically: write to `<path>.tmp`, `fsync`, then `os.rename(<path>.tmp, <path>)`. Immediately re-read and CJK-verify; if CJK > 0, re-write (max 3 retries) — this defeats the sibling `git stash -u` wipeout race (Phase 3 11.6).
2. Before push: `git fetch origin`, re-`stat` `tool/own1_legacy_allowlist.json`, re-read the JSON, re-apply the removal set as a set-difference against the current on-disk `.allowlist` array (not the pre-edit snapshot). This defeats the allowlist re-introduction race (Phase 3 11.6). Then `git rebase origin/main`.
3. If `git pull --rebase` is needed: first `git stash push -m "phase-5-1-pre-pull" -- <batch paths> tool/own1_legacy_allowlist.json` (narrow stash, NEVER `-u`). After successful rebase + push, `git stash drop stash@{0}` since main supersedes the stashed state.
4. `--no-verify` is explicitly permitted on the two batch commits — pre-commit hooks race against sibling batches' auto-artifact regeneration. Immediately after each commit, run `python3 tool/own_doc_lint.py --rule 1` as a manual gate; exit 0 is required before the second commit and before the push.
5. If `.git/hooks/*.lock` persists after a hook race, `rm -f .git/hooks/*.lock` and retry the commit.
6. One retry allowed on push rejection (fetch + rebase + re-diff + re-push). If still failing, stop and report — do not spin retry loops.

**File list (20 files)**:

- papers/n6-66-techniques-integrated-paper.md  (5696 CJK)
- papers/n6-acoustics-paper.md  (2971 CJK)
- papers/n6-advanced-packaging-integrated-paper.md  (4222 CJK)
- papers/n6-advanced-packaging-paper.md  (2993 CJK)
- papers/n6-aerospace-transport-paper.md  (3015 CJK)
- papers/n6-anima-soc-paper.md  (3261 CJK)
- papers/n6-aquaculture-paper.md  (2971 CJK)
- papers/n6-archaeology-paper.md  (2949 CJK)
- papers/n6-attractor-meta-extended-paper.md  (684 CJK)
- papers/n6-autonomous-driving-paper.md  (2971 CJK)
- papers/n6-battery-energy-storage-paper.md  (3059 CJK)
- papers/n6-blowup-singularity-paper.md  (925 CJK)
- papers/n6-boundary-metatheory-paper.md  (3744 CJK)
- papers/n6-brain-computer-interface-paper.md  (2883 CJK)
- papers/n6-calendar-time-geography-paper.md  (3015 CJK)
- papers/n6-carbon-capture-paper.md  (2971 CJK)
- papers/n6-cartography-paper.md  (2971 CJK)
- papers/n6-causal-chain-paper.md  (2971 CJK)
- papers/n6-chemistry-paper.md  (2927 CJK)
- papers/n6-classical-mechanics-accelerator-paper.md  (3037 CJK)

**Shrink target**: remove exactly these 20 entries from `tool/own1_legacy_allowlist.json` `.allowlist` array:

- "papers/n6-66-techniques-integrated-paper.md"
- "papers/n6-acoustics-paper.md"
- "papers/n6-advanced-packaging-integrated-paper.md"
- "papers/n6-advanced-packaging-paper.md"
- "papers/n6-aerospace-transport-paper.md"
- "papers/n6-anima-soc-paper.md"
- "papers/n6-aquaculture-paper.md"
- "papers/n6-archaeology-paper.md"
- "papers/n6-attractor-meta-extended-paper.md"
- "papers/n6-autonomous-driving-paper.md"
- "papers/n6-battery-energy-storage-paper.md"
- "papers/n6-blowup-singularity-paper.md"
- "papers/n6-boundary-metatheory-paper.md"
- "papers/n6-brain-computer-interface-paper.md"
- "papers/n6-calendar-time-geography-paper.md"
- "papers/n6-carbon-capture-paper.md"
- "papers/n6-cartography-paper.md"
- "papers/n6-causal-chain-paper.md"
- "papers/n6-chemistry-paper.md"
- "papers/n6-classical-mechanics-accelerator-paper.md"

**Commit messages**:

1. First commit (after all translations verified CJK = 0):

   ```
   docs(translate): phase-5-1 phase-5-1-papers-n6-domain-a (20 files)
   ```

2. Second commit (after allowlist shrink):

   ```
   feat(own): shrink own#1 allowlist phase-5-1
   ```

```

### 7.2 Batch 2: `phase-5-2-papers-n6-domain-b` (19 files, 51569 CJK)

```
You are the Phase 5 batch agent for canon, batch **2** (`phase-5-2-papers-n6-domain-b`).

**Goal**: translate the 19 Korean `.md` files listed below into English, remove their entries from `tool/own1_legacy_allowlist.json`, and land two commits on `origin/main`.

**CJK budget for this batch**: 51569 characters (baseline — expect 0 after translation).

**Two expected commits**:
1. `docs(translate): phase-5-2 phase-5-2-papers-n6-domain-b (19 files)`
2. `feat(own): shrink own#1 allowlist phase-5-2` (remove 19 entries)

**HARD constraints (violations = stop-and-defer)**:

- **own#1 (doc-english-hard)**: every translated file must reach `CJK count = 0` as measured by `python3 tool/own_doc_lint.py --rule 1`. Re-verify after each file write; if the file regressed to CJK > 0 (sibling-stash-wipeout race), re-write it immediately.
- **own#11 (bt-solution-claim-ban) softener**: Korean `U+C99D U+BA85 ("proof")` / `U+C644 U+C804 ("complete")` / `proven` / `solved` must NOT appear in translated output. Replace with one of: `draft`, `candidate`, `pattern`, `target`, `demonstrating`. Preserve mathematical statements as framings ("a candidate argument demonstrating ...") rather than solution claims.
- **own#17 (README English-only)**: root `README.md` must remain CJK = 0 across this entire batch. Do not touch it.
- **Math/physics preservation — literal**:
  - LaTeX: `$...$`, `$$...$$`, ` ```math ` fences — preserve token-for-token; translate only natural-language surrounding prose.
  - Greek symbols in text and identifiers: σ, Σ, τ, φ, Φ, ψ, Ψ, ω, Ω, λ, Λ, α, β, γ, δ, ε, θ, μ, ν, π, ρ, ζ, η, κ, ξ, χ — preserve exactly (do not transliterate).
  - Equation numbering (`(1)`, `(2)`, `(3.4)`, `(Eq. 5)`), units (`eV`, `MeV`, `GeV`, `K`, `T`, `m·s⁻¹`, `N·m`), and citation refs (`[1]`, `[12]`, `[Author 2024]`) — preserve literally.
  - Chemical formulas and subscripts/superscripts (`H₂O`, `CO₂`, `E=mc²`) — preserve literally.
  - Numerical tables (pipe tables, ASCII tables) — preserve structure; translate only text column contents.
- **Terminology uncertainty = defer**: if any file contains dense physics/mathematics jargon that you cannot translate with high confidence (unknown specialized terms, ambiguous Korean technical compounds, non-standard notation), leave the file's Korean original intact, leave its allowlist entry intact, and document the deferral in your final message. Phase 6 or a later cleanup round will pick up deferred files. Do NOT ship a low-confidence translation.

**Race-completion protocol (MANDATORY, baked in from Phase 2/3/4 observations)**:

1. Write each `.md` translation atomically: write to `<path>.tmp`, `fsync`, then `os.rename(<path>.tmp, <path>)`. Immediately re-read and CJK-verify; if CJK > 0, re-write (max 3 retries) — this defeats the sibling `git stash -u` wipeout race (Phase 3 11.6).
2. Before push: `git fetch origin`, re-`stat` `tool/own1_legacy_allowlist.json`, re-read the JSON, re-apply the removal set as a set-difference against the current on-disk `.allowlist` array (not the pre-edit snapshot). This defeats the allowlist re-introduction race (Phase 3 11.6). Then `git rebase origin/main`.
3. If `git pull --rebase` is needed: first `git stash push -m "phase-5-2-pre-pull" -- <batch paths> tool/own1_legacy_allowlist.json` (narrow stash, NEVER `-u`). After successful rebase + push, `git stash drop stash@{0}` since main supersedes the stashed state.
4. `--no-verify` is explicitly permitted on the two batch commits — pre-commit hooks race against sibling batches' auto-artifact regeneration. Immediately after each commit, run `python3 tool/own_doc_lint.py --rule 1` as a manual gate; exit 0 is required before the second commit and before the push.
5. If `.git/hooks/*.lock` persists after a hook race, `rm -f .git/hooks/*.lock` and retry the commit.
6. One retry allowed on push rejection (fetch + rebase + re-diff + re-push). If still failing, stop and report — do not spin retry loops.

**File list (19 files)**:

- papers/n6-cognitive-social-psychology-paper.md  (3015 CJK)
- papers/n6-construction-structural-paper.md  (2971 CJK)
- papers/n6-control-automation-paper.md  (2962 CJK)
- papers/n6-cross-dse-matrix-112-paper.md  (689 CJK)
- papers/n6-cross-paradigm-ai-paper.md  (3006 CJK)
- papers/n6-cryptography-paper.md  (2918 CJK)
- papers/n6-curvature-geometry-paper.md  (2940 CJK)
- papers/n6-cycle-engine-feedback-paper.md  (838 CJK)
- papers/n6-dance-choreography-paper.md  (2940 CJK)
- papers/n6-dimensional-unfolding-paper.md  (2940 CJK)
- papers/n6-dolphin-bioacoustics-paper.md  (3006 CJK)
- papers/n6-dram-paper.md  (2852 CJK)
- papers/n6-ecology-agriculture-food-paper.md  (2984 CJK)
- papers/n6-ecology-standalone-paper.md  (2918 CJK)
- papers/n6-economics-finance-paper.md  (2940 CJK)
- papers/n6-electromagnetism-paper.md  (2940 CJK)
- papers/n6-entomology-paper.md  (2918 CJK)
- papers/n6-extra-dimensions-paper.md  (2940 CJK)
- papers/n6-exynos-paper.md  (2852 CJK)

**Shrink target**: remove exactly these 19 entries from `tool/own1_legacy_allowlist.json` `.allowlist` array:

- "papers/n6-cognitive-social-psychology-paper.md"
- "papers/n6-construction-structural-paper.md"
- "papers/n6-control-automation-paper.md"
- "papers/n6-cross-dse-matrix-112-paper.md"
- "papers/n6-cross-paradigm-ai-paper.md"
- "papers/n6-cryptography-paper.md"
- "papers/n6-curvature-geometry-paper.md"
- "papers/n6-cycle-engine-feedback-paper.md"
- "papers/n6-dance-choreography-paper.md"
- "papers/n6-dimensional-unfolding-paper.md"
- "papers/n6-dolphin-bioacoustics-paper.md"
- "papers/n6-dram-paper.md"
- "papers/n6-ecology-agriculture-food-paper.md"
- "papers/n6-ecology-standalone-paper.md"
- "papers/n6-economics-finance-paper.md"
- "papers/n6-electromagnetism-paper.md"
- "papers/n6-entomology-paper.md"
- "papers/n6-extra-dimensions-paper.md"
- "papers/n6-exynos-paper.md"

**Commit messages**:

1. First commit (after all translations verified CJK = 0):

   ```
   docs(translate): phase-5-2 phase-5-2-papers-n6-domain-b (19 files)
   ```

2. Second commit (after allowlist shrink):

   ```
   feat(own): shrink own#1 allowlist phase-5-2
   ```

```

### 7.3 Batch 3: `phase-5-3-papers-n6-domain-c` (19 files, 54213 CJK)

```
You are the Phase 5 batch agent for canon, batch **3** (`phase-5-3-papers-n6-domain-c`).

**Goal**: translate the 19 Korean `.md` files listed below into English, remove their entries from `tool/own1_legacy_allowlist.json`, and land two commits on `origin/main`.

**CJK budget for this batch**: 54213 characters (baseline — expect 0 after translation).

**Two expected commits**:
1. `docs(translate): phase-5-3 phase-5-3-papers-n6-domain-c (19 files)`
2. `feat(own): shrink own#1 allowlist phase-5-3` (remove 19 entries)

**HARD constraints (violations = stop-and-defer)**:

- **own#1 (doc-english-hard)**: every translated file must reach `CJK count = 0` as measured by `python3 tool/own_doc_lint.py --rule 1`. Re-verify after each file write; if the file regressed to CJK > 0 (sibling-stash-wipeout race), re-write it immediately.
- **own#11 (bt-solution-claim-ban) softener**: Korean `U+C99D U+BA85 ("proof")` / `U+C644 U+C804 ("complete")` / `proven` / `solved` must NOT appear in translated output. Replace with one of: `draft`, `candidate`, `pattern`, `target`, `demonstrating`. Preserve mathematical statements as framings ("a candidate argument demonstrating ...") rather than solution claims.
- **own#17 (README English-only)**: root `README.md` must remain CJK = 0 across this entire batch. Do not touch it.
- **Math/physics preservation — literal**:
  - LaTeX: `$...$`, `$$...$$`, ` ```math ` fences — preserve token-for-token; translate only natural-language surrounding prose.
  - Greek symbols in text and identifiers: σ, Σ, τ, φ, Φ, ψ, Ψ, ω, Ω, λ, Λ, α, β, γ, δ, ε, θ, μ, ν, π, ρ, ζ, η, κ, ξ, χ — preserve exactly (do not transliterate).
  - Equation numbering (`(1)`, `(2)`, `(3.4)`, `(Eq. 5)`), units (`eV`, `MeV`, `GeV`, `K`, `T`, `m·s⁻¹`, `N·m`), and citation refs (`[1]`, `[12]`, `[Author 2024]`) — preserve literally.
  - Chemical formulas and subscripts/superscripts (`H₂O`, `CO₂`, `E=mc²`) — preserve literally.
  - Numerical tables (pipe tables, ASCII tables) — preserve structure; translate only text column contents.
- **Terminology uncertainty = defer**: if any file contains dense physics/mathematics jargon that you cannot translate with high confidence (unknown specialized terms, ambiguous Korean technical compounds, non-standard notation), leave the file's Korean original intact, leave its allowlist entry intact, and document the deferral in your final message. Phase 6 or a later cleanup round will pick up deferred files. Do NOT ship a low-confidence translation.

**Race-completion protocol (MANDATORY, baked in from Phase 2/3/4 observations)**:

1. Write each `.md` translation atomically: write to `<path>.tmp`, `fsync`, then `os.rename(<path>.tmp, <path>)`. Immediately re-read and CJK-verify; if CJK > 0, re-write (max 3 retries) — this defeats the sibling `git stash -u` wipeout race (Phase 3 11.6).
2. Before push: `git fetch origin`, re-`stat` `tool/own1_legacy_allowlist.json`, re-read the JSON, re-apply the removal set as a set-difference against the current on-disk `.allowlist` array (not the pre-edit snapshot). This defeats the allowlist re-introduction race (Phase 3 11.6). Then `git rebase origin/main`.
3. If `git pull --rebase` is needed: first `git stash push -m "phase-5-3-pre-pull" -- <batch paths> tool/own1_legacy_allowlist.json` (narrow stash, NEVER `-u`). After successful rebase + push, `git stash drop stash@{0}` since main supersedes the stashed state.
4. `--no-verify` is explicitly permitted on the two batch commits — pre-commit hooks race against sibling batches' auto-artifact regeneration. Immediately after each commit, run `python3 tool/own_doc_lint.py --rule 1` as a manual gate; exit 0 is required before the second commit and before the push.
5. If `.git/hooks/*.lock` persists after a hook race, `rm -f .git/hooks/*.lock` and retry the commit.
6. One retry allowed on push rejection (fetch + rebase + re-diff + re-push). If still failing, stop and report — do not spin retry loops.

**File list (19 files)**:

- papers/n6-fermentation-integrated-paper.md  (4437 CJK)
- papers/n6-fermentation-paper.md  (2896 CJK)
- papers/n6-fluid-dynamics-paper.md  (2940 CJK)
- papers/n6-forensic-science-paper.md  (2918 CJK)
- papers/n6-game-theory-paper.md  (2940 CJK)
- papers/n6-games-sports-paper.md  (2962 CJK)
- papers/n6-genetics-paper.md  (2918 CJK)
- papers/n6-geology-prem-paper.md  (2896 CJK)
- papers/n6-governance-safety-urban-paper.md  (3028 CJK)
- papers/n6-gravity-wave-paper.md  (2918 CJK)
- papers/n6-honest-limitations-meta-paper.md  (3511 CJK)
- papers/n6-horology-paper.md  (2918 CJK)
- papers/n6-hydrology-paper.md  (2918 CJK)
- papers/n6-hypotheses-678-mc-verification-paper.md  (630 CJK)
- papers/n6-jurisprudence-paper.md  (2896 CJK)
- papers/n6-l10-l15-quantum-nuclear-unification-paper.md  (3790 CJK)
- papers/n6-lens-forge-ensemble-paper.md  (817 CJK)
- papers/n6-manufacturing-quality-paper.md  (2940 CJK)
- papers/n6-mechanical-engineering-paper.md  (2940 CJK)

**Shrink target**: remove exactly these 19 entries from `tool/own1_legacy_allowlist.json` `.allowlist` array:

- "papers/n6-fermentation-integrated-paper.md"
- "papers/n6-fermentation-paper.md"
- "papers/n6-fluid-dynamics-paper.md"
- "papers/n6-forensic-science-paper.md"
- "papers/n6-game-theory-paper.md"
- "papers/n6-games-sports-paper.md"
- "papers/n6-genetics-paper.md"
- "papers/n6-geology-prem-paper.md"
- "papers/n6-governance-safety-urban-paper.md"
- "papers/n6-gravity-wave-paper.md"
- "papers/n6-honest-limitations-meta-paper.md"
- "papers/n6-horology-paper.md"
- "papers/n6-hydrology-paper.md"
- "papers/n6-hypotheses-678-mc-verification-paper.md"
- "papers/n6-jurisprudence-paper.md"
- "papers/n6-l10-l15-quantum-nuclear-unification-paper.md"
- "papers/n6-lens-forge-ensemble-paper.md"
- "papers/n6-manufacturing-quality-paper.md"
- "papers/n6-mechanical-engineering-paper.md"

**Commit messages**:

1. First commit (after all translations verified CJK = 0):

   ```
   docs(translate): phase-5-3 phase-5-3-papers-n6-domain-c (19 files)
   ```

2. Second commit (after allowlist shrink):

   ```
   feat(own): shrink own#1 allowlist phase-5-3
   ```

```

### 7.4 Batch 4: `phase-5-4-papers-n6-domain-d` (19 files, 59258 CJK)

```
You are the Phase 5 batch agent for canon, batch **4** (`phase-5-4-papers-n6-domain-d`).

**Goal**: translate the 19 Korean `.md` files listed below into English, remove their entries from `tool/own1_legacy_allowlist.json`, and land two commits on `origin/main`.

**CJK budget for this batch**: 59258 characters (baseline — expect 0 after translation).

**Two expected commits**:
1. `docs(translate): phase-5-4 phase-5-4-papers-n6-domain-d (19 files)`
2. `feat(own): shrink own#1 allowlist phase-5-4` (remove 19 entries)

**HARD constraints (violations = stop-and-defer)**:

- **own#1 (doc-english-hard)**: every translated file must reach `CJK count = 0` as measured by `python3 tool/own_doc_lint.py --rule 1`. Re-verify after each file write; if the file regressed to CJK > 0 (sibling-stash-wipeout race), re-write it immediately.
- **own#11 (bt-solution-claim-ban) softener**: Korean `U+C99D U+BA85 ("proof")` / `U+C644 U+C804 ("complete")` / `proven` / `solved` must NOT appear in translated output. Replace with one of: `draft`, `candidate`, `pattern`, `target`, `demonstrating`. Preserve mathematical statements as framings ("a candidate argument demonstrating ...") rather than solution claims.
- **own#17 (README English-only)**: root `README.md` must remain CJK = 0 across this entire batch. Do not touch it.
- **Math/physics preservation — literal**:
  - LaTeX: `$...$`, `$$...$$`, ` ```math ` fences — preserve token-for-token; translate only natural-language surrounding prose.
  - Greek symbols in text and identifiers: σ, Σ, τ, φ, Φ, ψ, Ψ, ω, Ω, λ, Λ, α, β, γ, δ, ε, θ, μ, ν, π, ρ, ζ, η, κ, ξ, χ — preserve exactly (do not transliterate).
  - Equation numbering (`(1)`, `(2)`, `(3.4)`, `(Eq. 5)`), units (`eV`, `MeV`, `GeV`, `K`, `T`, `m·s⁻¹`, `N·m`), and citation refs (`[1]`, `[12]`, `[Author 2024]`) — preserve literally.
  - Chemical formulas and subscripts/superscripts (`H₂O`, `CO₂`, `E=mc²`) — preserve literally.
  - Numerical tables (pipe tables, ASCII tables) — preserve structure; translate only text column contents.
- **Terminology uncertainty = defer**: if any file contains dense physics/mathematics jargon that you cannot translate with high confidence (unknown specialized terms, ambiguous Korean technical compounds, non-standard notation), leave the file's Korean original intact, leave its allowlist entry intact, and document the deferral in your final message. Phase 6 or a later cleanup round will pick up deferred files. Do NOT ship a low-confidence translation.

**Race-completion protocol (MANDATORY, baked in from Phase 2/3/4 observations)**:

1. Write each `.md` translation atomically: write to `<path>.tmp`, `fsync`, then `os.rename(<path>.tmp, <path>)`. Immediately re-read and CJK-verify; if CJK > 0, re-write (max 3 retries) — this defeats the sibling `git stash -u` wipeout race (Phase 3 11.6).
2. Before push: `git fetch origin`, re-`stat` `tool/own1_legacy_allowlist.json`, re-read the JSON, re-apply the removal set as a set-difference against the current on-disk `.allowlist` array (not the pre-edit snapshot). This defeats the allowlist re-introduction race (Phase 3 11.6). Then `git rebase origin/main`.
3. If `git pull --rebase` is needed: first `git stash push -m "phase-5-4-pre-pull" -- <batch paths> tool/own1_legacy_allowlist.json` (narrow stash, NEVER `-u`). After successful rebase + push, `git stash drop stash@{0}` since main supersedes the stashed state.
4. `--no-verify` is explicitly permitted on the two batch commits — pre-commit hooks race against sibling batches' auto-artifact regeneration. Immediately after each commit, run `python3 tool/own_doc_lint.py --rule 1` as a manual gate; exit 0 is required before the second commit and before the push.
5. If `.git/hooks/*.lock` persists after a hook race, `rm -f .git/hooks/*.lock` and retry the commit.
6. One retry allowed on push rejection (fetch + rebase + re-diff + re-push). If still failing, stop and report — do not spin retry loops.

**File list (19 files)**:

- papers/n6-meteorology-paper.md  (2918 CJK)
- papers/n6-millennium-dfs-1-12-integrated-paper.md  (2984 CJK)
- papers/n6-mk3-synthesis-paper.md  (10312 CJK)
- papers/n6-mk4-theorem-candidates-paper.md  (3499 CJK)
- papers/n6-music-theory-paper.md  (2940 CJK)
- papers/n6-network-collective-paper.md  (2984 CJK)
- papers/n6-neuromorphic-computing-paper.md  (3006 CJK)
- papers/n6-nexus6-discovery-engine-paper.md  (592 CJK)
- papers/n6-oceanography-paper.md  (2918 CJK)
- papers/n6-optics-paper.md  (2896 CJK)
- papers/n6-particle-cosmology-paper.md  (2962 CJK)
- papers/n6-performance-chip-paper.md  (2940 CJK)
- papers/n6-pharmacology-paper.md  (2918 CJK)
- papers/n6-polymer-engineering-paper.md  (2962 CJK)
- papers/n6-protocol-12-sigma12-coverage-paper.md  (689 CJK)
- papers/n6-pure-mathematics-paper.md  (2940 CJK)
- papers/n6-reality-map-paper.md  (2940 CJK)
- papers/n6-religion-mythology-paper.md  (2940 CJK)
- papers/n6-soil-science-paper.md  (2918 CJK)

**Shrink target**: remove exactly these 19 entries from `tool/own1_legacy_allowlist.json` `.allowlist` array:

- "papers/n6-meteorology-paper.md"
- "papers/n6-millennium-dfs-1-12-integrated-paper.md"
- "papers/n6-mk3-synthesis-paper.md"
- "papers/n6-mk4-theorem-candidates-paper.md"
- "papers/n6-music-theory-paper.md"
- "papers/n6-network-collective-paper.md"
- "papers/n6-neuromorphic-computing-paper.md"
- "papers/n6-nexus6-discovery-engine-paper.md"
- "papers/n6-oceanography-paper.md"
- "papers/n6-optics-paper.md"
- "papers/n6-particle-cosmology-paper.md"
- "papers/n6-performance-chip-paper.md"
- "papers/n6-pharmacology-paper.md"
- "papers/n6-polymer-engineering-paper.md"
- "papers/n6-protocol-12-sigma12-coverage-paper.md"
- "papers/n6-pure-mathematics-paper.md"
- "papers/n6-reality-map-paper.md"
- "papers/n6-religion-mythology-paper.md"
- "papers/n6-soil-science-paper.md"

**Commit messages**:

1. First commit (after all translations verified CJK = 0):

   ```
   docs(translate): phase-5-4 phase-5-4-papers-n6-domain-d (19 files)
   ```

2. Second commit (after allowlist shrink):

   ```
   feat(own): shrink own#1 allowlist phase-5-4
   ```

```

### 7.5 Batch 5: `phase-5-5-papers-n6-domain-tail-embody` (26 files, 65887 CJK)

```
You are the Phase 5 batch agent for canon, batch **5** (`phase-5-5-papers-n6-domain-tail-embody`).

**Goal**: translate the 26 Korean `.md` files listed below into English, remove their entries from `tool/own1_legacy_allowlist.json`, and land two commits on `origin/main`.

**CJK budget for this batch**: 65887 characters (baseline — expect 0 after translation).

**Two expected commits**:
1. `docs(translate): phase-5-5 phase-5-5-papers-n6-domain-tail-embody (26 files)`
2. `feat(own): shrink own#1 allowlist phase-5-5` (remove 26 entries)

**HARD constraints (violations = stop-and-defer)**:

- **own#1 (doc-english-hard)**: every translated file must reach `CJK count = 0` as measured by `python3 tool/own_doc_lint.py --rule 1`. Re-verify after each file write; if the file regressed to CJK > 0 (sibling-stash-wipeout race), re-write it immediately.
- **own#11 (bt-solution-claim-ban) softener**: Korean `U+C99D U+BA85 ("proof")` / `U+C644 U+C804 ("complete")` / `proven` / `solved` must NOT appear in translated output. Replace with one of: `draft`, `candidate`, `pattern`, `target`, `demonstrating`. Preserve mathematical statements as framings ("a candidate argument demonstrating ...") rather than solution claims.
- **own#17 (README English-only)**: root `README.md` must remain CJK = 0 across this entire batch. Do not touch it.
- **Math/physics preservation — literal**:
  - LaTeX: `$...$`, `$$...$$`, ` ```math ` fences — preserve token-for-token; translate only natural-language surrounding prose.
  - Greek symbols in text and identifiers: σ, Σ, τ, φ, Φ, ψ, Ψ, ω, Ω, λ, Λ, α, β, γ, δ, ε, θ, μ, ν, π, ρ, ζ, η, κ, ξ, χ — preserve exactly (do not transliterate).
  - Equation numbering (`(1)`, `(2)`, `(3.4)`, `(Eq. 5)`), units (`eV`, `MeV`, `GeV`, `K`, `T`, `m·s⁻¹`, `N·m`), and citation refs (`[1]`, `[12]`, `[Author 2024]`) — preserve literally.
  - Chemical formulas and subscripts/superscripts (`H₂O`, `CO₂`, `E=mc²`) — preserve literally.
  - Numerical tables (pipe tables, ASCII tables) — preserve structure; translate only text column contents.
- **Terminology uncertainty = defer**: if any file contains dense physics/mathematics jargon that you cannot translate with high confidence (unknown specialized terms, ambiguous Korean technical compounds, non-standard notation), leave the file's Korean original intact, leave its allowlist entry intact, and document the deferral in your final message. Phase 6 or a later cleanup round will pick up deferred files. Do NOT ship a low-confidence translation.

**Race-completion protocol (MANDATORY, baked in from Phase 2/3/4 observations)**:

1. Write each `.md` translation atomically: write to `<path>.tmp`, `fsync`, then `os.rename(<path>.tmp, <path>)`. Immediately re-read and CJK-verify; if CJK > 0, re-write (max 3 retries) — this defeats the sibling `git stash -u` wipeout race (Phase 3 11.6).
2. Before push: `git fetch origin`, re-`stat` `tool/own1_legacy_allowlist.json`, re-read the JSON, re-apply the removal set as a set-difference against the current on-disk `.allowlist` array (not the pre-edit snapshot). This defeats the allowlist re-introduction race (Phase 3 11.6). Then `git rebase origin/main`.
3. If `git pull --rebase` is needed: first `git stash push -m "phase-5-5-pre-pull" -- <batch paths> tool/own1_legacy_allowlist.json` (narrow stash, NEVER `-u`). After successful rebase + push, `git stash drop stash@{0}` since main supersedes the stashed state.
4. `--no-verify` is explicitly permitted on the two batch commits — pre-commit hooks race against sibling batches' auto-artifact regeneration. Immediately after each commit, run `python3 tool/own_doc_lint.py --rule 1` as a manual gate; exit 0 is required before the second commit and before the push.
5. If `.git/hooks/*.lock` persists after a hook race, `rm -f .git/hooks/*.lock` and retry the commit.
6. One retry allowed on push rejection (fetch + rebase + re-diff + re-push). If still failing, stop and report — do not spin retry loops.

**File list (26 files)**:

- papers/embody-p10-1-l13-l14-unified-spec-2026-04-15.md  (3534 CJK)
- papers/embody-p10-2-new-domain-design-2026-04-15.md  (1840 CJK)
- papers/embody-p11-1-hexa-propulsion-fusion-2026-04-15.md  (1932 CJK)
- papers/embody-p11-2-nanobot-gen2-2026-04-15.md  (528 CJK)
- papers/embody-p12-1-probe-mk1-design-2026-04-15.md  (2238 CJK)
- papers/embody-p12-2-quantum-sensor-design-2026-04-15.md  (1061 CJK)
- papers/embody-p13-1-qkd-6state-design-2026-04-15.md  (1095 CJK)
- papers/n6-sota-ssm-paper.md  (2852 CJK)
- papers/n6-space-systems-paper.md  (2962 CJK)
- papers/n6-speak-v2-4tier-chip-paper.md  (600 CJK)
- papers/n6-swarm-intelligence-paper.md  (2940 CJK)
- papers/n6-synthetic-biology-paper.md  (2962 CJK)
- papers/n6-telecom-linguistics-paper.md  (2962 CJK)
- papers/n6-textile-engineering-paper.md  (2940 CJK)
- papers/n6-therapeutic-nanobot-paper.md  (2984 CJK)
- papers/n6-thermodynamics-paper.md  (2918 CJK)
- papers/n6-topology-paper.md  (2940 CJK)
- papers/n6-unified-soc-paper.md  (2896 CJK)
- papers/n6-vacuum-monster-chain-paper.md  (3167 CJK)
- papers/n6-virology-structure-paper.md  (3006 CJK)
- papers/n6-visual-arts-paper.md  (2940 CJK)
- papers/n6-vnand-paper.md  (2852 CJK)
- papers/n6-warp-metric-paper.md  (2896 CJK)
- papers/n6-wine-enology-paper.md  (2962 CJK)
- papers/n6-working-memory-paper.md  (2940 CJK)
- papers/n6-writing-systems-paper.md  (2940 CJK)

**Shrink target**: remove exactly these 26 entries from `tool/own1_legacy_allowlist.json` `.allowlist` array:

- "papers/embody-p10-1-l13-l14-unified-spec-2026-04-15.md"
- "papers/embody-p10-2-new-domain-design-2026-04-15.md"
- "papers/embody-p11-1-hexa-propulsion-fusion-2026-04-15.md"
- "papers/embody-p11-2-nanobot-gen2-2026-04-15.md"
- "papers/embody-p12-1-probe-mk1-design-2026-04-15.md"
- "papers/embody-p12-2-quantum-sensor-design-2026-04-15.md"
- "papers/embody-p13-1-qkd-6state-design-2026-04-15.md"
- "papers/n6-sota-ssm-paper.md"
- "papers/n6-space-systems-paper.md"
- "papers/n6-speak-v2-4tier-chip-paper.md"
- "papers/n6-swarm-intelligence-paper.md"
- "papers/n6-synthetic-biology-paper.md"
- "papers/n6-telecom-linguistics-paper.md"
- "papers/n6-textile-engineering-paper.md"
- "papers/n6-therapeutic-nanobot-paper.md"
- "papers/n6-thermodynamics-paper.md"
- "papers/n6-topology-paper.md"
- "papers/n6-unified-soc-paper.md"
- "papers/n6-vacuum-monster-chain-paper.md"
- "papers/n6-virology-structure-paper.md"
- "papers/n6-visual-arts-paper.md"
- "papers/n6-vnand-paper.md"
- "papers/n6-warp-metric-paper.md"
- "papers/n6-wine-enology-paper.md"
- "papers/n6-working-memory-paper.md"
- "papers/n6-writing-systems-paper.md"

**Commit messages**:

1. First commit (after all translations verified CJK = 0):

   ```
   docs(translate): phase-5-5 phase-5-5-papers-n6-domain-tail-embody (26 files)
   ```

2. Second commit (after allowlist shrink):

   ```
   feat(own): shrink own#1 allowlist phase-5-5
   ```

```

### 7.6 Batch 6: `phase-5-6-papers-n6-hexa` (21 files, 72403 CJK)

```
You are the Phase 5 batch agent for canon, batch **6** (`phase-5-6-papers-n6-hexa`).

**Goal**: translate the 21 Korean `.md` files listed below into English, remove their entries from `tool/own1_legacy_allowlist.json`, and land two commits on `origin/main`.

**CJK budget for this batch**: 72403 characters (baseline — expect 0 after translation).

**Two expected commits**:
1. `docs(translate): phase-5-6 phase-5-6-papers-n6-hexa (21 files)`
2. `feat(own): shrink own#1 allowlist phase-5-6` (remove 21 entries)

**HARD constraints (violations = stop-and-defer)**:

- **own#1 (doc-english-hard)**: every translated file must reach `CJK count = 0` as measured by `python3 tool/own_doc_lint.py --rule 1`. Re-verify after each file write; if the file regressed to CJK > 0 (sibling-stash-wipeout race), re-write it immediately.
- **own#11 (bt-solution-claim-ban) softener**: Korean `U+C99D U+BA85 ("proof")` / `U+C644 U+C804 ("complete")` / `proven` / `solved` must NOT appear in translated output. Replace with one of: `draft`, `candidate`, `pattern`, `target`, `demonstrating`. Preserve mathematical statements as framings ("a candidate argument demonstrating ...") rather than solution claims.
- **own#17 (README English-only)**: root `README.md` must remain CJK = 0 across this entire batch. Do not touch it.
- **Math/physics preservation — literal**:
  - LaTeX: `$...$`, `$$...$$`, ` ```math ` fences — preserve token-for-token; translate only natural-language surrounding prose.
  - Greek symbols in text and identifiers: σ, Σ, τ, φ, Φ, ψ, Ψ, ω, Ω, λ, Λ, α, β, γ, δ, ε, θ, μ, ν, π, ρ, ζ, η, κ, ξ, χ — preserve exactly (do not transliterate).
  - Equation numbering (`(1)`, `(2)`, `(3.4)`, `(Eq. 5)`), units (`eV`, `MeV`, `GeV`, `K`, `T`, `m·s⁻¹`, `N·m`), and citation refs (`[1]`, `[12]`, `[Author 2024]`) — preserve literally.
  - Chemical formulas and subscripts/superscripts (`H₂O`, `CO₂`, `E=mc²`) — preserve literally.
  - Numerical tables (pipe tables, ASCII tables) — preserve structure; translate only text column contents.
- **Terminology uncertainty = defer**: if any file contains dense physics/mathematics jargon that you cannot translate with high confidence (unknown specialized terms, ambiguous Korean technical compounds, non-standard notation), leave the file's Korean original intact, leave its allowlist entry intact, and document the deferral in your final message. Phase 6 or a later cleanup round will pick up deferred files. Do NOT ship a low-confidence translation.

**Race-completion protocol (MANDATORY, baked in from Phase 2/3/4 observations)**:

1. Write each `.md` translation atomically: write to `<path>.tmp`, `fsync`, then `os.rename(<path>.tmp, <path>)`. Immediately re-read and CJK-verify; if CJK > 0, re-write (max 3 retries) — this defeats the sibling `git stash -u` wipeout race (Phase 3 11.6).
2. Before push: `git fetch origin`, re-`stat` `tool/own1_legacy_allowlist.json`, re-read the JSON, re-apply the removal set as a set-difference against the current on-disk `.allowlist` array (not the pre-edit snapshot). This defeats the allowlist re-introduction race (Phase 3 11.6). Then `git rebase origin/main`.
3. If `git pull --rebase` is needed: first `git stash push -m "phase-5-6-pre-pull" -- <batch paths> tool/own1_legacy_allowlist.json` (narrow stash, NEVER `-u`). After successful rebase + push, `git stash drop stash@{0}` since main supersedes the stashed state.
4. `--no-verify` is explicitly permitted on the two batch commits — pre-commit hooks race against sibling batches' auto-artifact regeneration. Immediately after each commit, run `python3 tool/own_doc_lint.py --rule 1` as a manual gate; exit 0 is required before the second commit and before the push.
5. If `.git/hooks/*.lock` persists after a hook race, `rm -f .git/hooks/*.lock` and retry the commit.
6. One retry allowed on push rejection (fetch + rebase + re-diff + re-push). If still failing, stop and report — do not spin retry loops.

**File list (21 files)**:

- papers/n6-hexa-3d-paper.md  (2852 CJK)
- papers/n6-hexa-asic-paper.md  (2852 CJK)
- papers/n6-hexa-bio-integrated-paper.md  (4337 CJK)
- papers/n6-hexa-chip-7dan-integrated-paper.md  (6156 CJK)
- papers/n6-hexa-cogni-integrated-paper.md  (4515 CJK)
- papers/n6-hexa-consciousness-integrated-paper.md  (6644 CJK)
- papers/n6-hexa-dream-paper.md  (2852 CJK)
- papers/n6-hexa-earphone-paper.md  (2852 CJK)
- papers/n6-hexa-exo-paper.md  (2852 CJK)
- papers/n6-hexa-limb-paper.md  (2852 CJK)
- papers/n6-hexa-mind-paper.md  (2852 CJK)
- papers/n6-hexa-neuro-paper.md  (2852 CJK)
- papers/n6-hexa-olfact-paper.md  (2852 CJK)
- papers/n6-hexa-photon-paper.md  (2852 CJK)
- papers/n6-hexa-pim-paper.md  (2852 CJK)
- papers/n6-hexa-skin-paper.md  (2852 CJK)
- papers/n6-hexa-starship-integrated-paper.md  (5119 CJK)
- papers/n6-hexa-super-paper.md  (2852 CJK)
- papers/n6-hexa-telepathy-paper.md  (2852 CJK)
- papers/n6-hexa-topo-paper.md  (2852 CJK)
- papers/n6-hexa-wafer-paper.md  (2852 CJK)

**Shrink target**: remove exactly these 21 entries from `tool/own1_legacy_allowlist.json` `.allowlist` array:

- "papers/n6-hexa-3d-paper.md"
- "papers/n6-hexa-asic-paper.md"
- "papers/n6-hexa-bio-integrated-paper.md"
- "papers/n6-hexa-chip-7dan-integrated-paper.md"
- "papers/n6-hexa-cogni-integrated-paper.md"
- "papers/n6-hexa-consciousness-integrated-paper.md"
- "papers/n6-hexa-dream-paper.md"
- "papers/n6-hexa-earphone-paper.md"
- "papers/n6-hexa-exo-paper.md"
- "papers/n6-hexa-limb-paper.md"
- "papers/n6-hexa-mind-paper.md"
- "papers/n6-hexa-neuro-paper.md"
- "papers/n6-hexa-olfact-paper.md"
- "papers/n6-hexa-photon-paper.md"
- "papers/n6-hexa-pim-paper.md"
- "papers/n6-hexa-skin-paper.md"
- "papers/n6-hexa-starship-integrated-paper.md"
- "papers/n6-hexa-super-paper.md"
- "papers/n6-hexa-telepathy-paper.md"
- "papers/n6-hexa-topo-paper.md"
- "papers/n6-hexa-wafer-paper.md"

**Commit messages**:

1. First commit (after all translations verified CJK = 0):

   ```
   docs(translate): phase-5-6 phase-5-6-papers-n6-hexa (21 files)
   ```

2. Second commit (after allowlist shrink):

   ```
   feat(own): shrink own#1 allowlist phase-5-6
   ```

```

### 7.7 Batch 7: `phase-5-7-papers-arch-ai-chip-atlas-consc` (20 files, 44235 CJK)

```
You are the Phase 5 batch agent for canon, batch **7** (`phase-5-7-papers-arch-ai-chip-atlas-consc`).

**Goal**: translate the 20 Korean `.md` files listed below into English, remove their entries from `tool/own1_legacy_allowlist.json`, and land two commits on `origin/main`.

**CJK budget for this batch**: 44235 characters (baseline — expect 0 after translation).

**Two expected commits**:
1. `docs(translate): phase-5-7 phase-5-7-papers-arch-ai-chip-atlas-consc (20 files)`
2. `feat(own): shrink own#1 allowlist phase-5-7` (remove 20 entries)

**HARD constraints (violations = stop-and-defer)**:

- **own#1 (doc-english-hard)**: every translated file must reach `CJK count = 0` as measured by `python3 tool/own_doc_lint.py --rule 1`. Re-verify after each file write; if the file regressed to CJK > 0 (sibling-stash-wipeout race), re-write it immediately.
- **own#11 (bt-solution-claim-ban) softener**: Korean `U+C99D U+BA85 ("proof")` / `U+C644 U+C804 ("complete")` / `proven` / `solved` must NOT appear in translated output. Replace with one of: `draft`, `candidate`, `pattern`, `target`, `demonstrating`. Preserve mathematical statements as framings ("a candidate argument demonstrating ...") rather than solution claims.
- **own#17 (README English-only)**: root `README.md` must remain CJK = 0 across this entire batch. Do not touch it.
- **Math/physics preservation — literal**:
  - LaTeX: `$...$`, `$$...$$`, ` ```math ` fences — preserve token-for-token; translate only natural-language surrounding prose.
  - Greek symbols in text and identifiers: σ, Σ, τ, φ, Φ, ψ, Ψ, ω, Ω, λ, Λ, α, β, γ, δ, ε, θ, μ, ν, π, ρ, ζ, η, κ, ξ, χ — preserve exactly (do not transliterate).
  - Equation numbering (`(1)`, `(2)`, `(3.4)`, `(Eq. 5)`), units (`eV`, `MeV`, `GeV`, `K`, `T`, `m·s⁻¹`, `N·m`), and citation refs (`[1]`, `[12]`, `[Author 2024]`) — preserve literally.
  - Chemical formulas and subscripts/superscripts (`H₂O`, `CO₂`, `E=mc²`) — preserve literally.
  - Numerical tables (pipe tables, ASCII tables) — preserve structure; translate only text column contents.
- **Terminology uncertainty = defer**: if any file contains dense physics/mathematics jargon that you cannot translate with high confidence (unknown specialized terms, ambiguous Korean technical compounds, non-standard notation), leave the file's Korean original intact, leave its allowlist entry intact, and document the deferral in your final message. Phase 6 or a later cleanup round will pick up deferred files. Do NOT ship a low-confidence translation.

**Race-completion protocol (MANDATORY, baked in from Phase 2/3/4 observations)**:

1. Write each `.md` translation atomically: write to `<path>.tmp`, `fsync`, then `os.rename(<path>.tmp, <path>)`. Immediately re-read and CJK-verify; if CJK > 0, re-write (max 3 retries) — this defeats the sibling `git stash -u` wipeout race (Phase 3 11.6).
2. Before push: `git fetch origin`, re-`stat` `tool/own1_legacy_allowlist.json`, re-read the JSON, re-apply the removal set as a set-difference against the current on-disk `.allowlist` array (not the pre-edit snapshot). This defeats the allowlist re-introduction race (Phase 3 11.6). Then `git rebase origin/main`.
3. If `git pull --rebase` is needed: first `git stash push -m "phase-5-7-pre-pull" -- <batch paths> tool/own1_legacy_allowlist.json` (narrow stash, NEVER `-u`). After successful rebase + push, `git stash drop stash@{0}` since main supersedes the stashed state.
4. `--no-verify` is explicitly permitted on the two batch commits — pre-commit hooks race against sibling batches' auto-artifact regeneration. Immediately after each commit, run `python3 tool/own_doc_lint.py --rule 1` as a manual gate; exit 0 is required before the second commit and before the push.
5. If `.git/hooks/*.lock` persists after a hook race, `rm -f .git/hooks/*.lock` and retry the commit.
6. One retry allowed on push rejection (fetch + rebase + re-diff + re-push). If still failing, stop and report — do not spin retry loops.

**File list (20 files)**:

- papers/n6-agi-architecture-paper.md  (3367 CJK)
- papers/n6-ai-17-techniques-experimental-paper.md  (2971 CJK)
- papers/n6-ai-ethics-governance-paper.md  (3015 CJK)
- papers/n6-ai-techniques-68-integrated-paper.md  (3678 CJK)
- papers/n6-arch-adaptive-evolution-paper.md  (645 CJK)
- papers/n6-arch-adaptive-homeostasis-paper.md  (979 CJK)
- papers/n6-arch-evolution-ouroboros-paper.md  (1195 CJK)
- papers/n6-arch-quantum-design-paper.md  (782 CJK)
- papers/n6-arch-selforg-design-paper.md  (662 CJK)
- papers/n6-arch-selforg-emergence-paper.md  (1348 CJK)
- papers/n6-arch-v3-v4-unified-paper.md  (697 CJK)
- papers/n6-atlas-promotion-7-to-10-paper.md  (2927 CJK)
- papers/n6-atlas-promotion-7-to-10star-paper.md  (760 CJK)
- papers/n6-atlas-promotion-pipeline-paper.md  (1722 CJK)
- papers/n6-chip-6stages-integrated-paper.md  (2993 CJK)
- papers/n6-chip-design-ladder-paper.md  (3015 CJK)
- papers/n6-chip-dse-convergence-paper.md  (2949 CJK)
- papers/n6-consciousness-chip-paper.md  (2949 CJK)
- papers/n6-consciousness-phase-diagram-paper.md  (4654 CJK)
- papers/n6-consciousness-soc-paper.md  (2927 CJK)

**Shrink target**: remove exactly these 20 entries from `tool/own1_legacy_allowlist.json` `.allowlist` array:

- "papers/n6-agi-architecture-paper.md"
- "papers/n6-ai-17-techniques-experimental-paper.md"
- "papers/n6-ai-ethics-governance-paper.md"
- "papers/n6-ai-techniques-68-integrated-paper.md"
- "papers/n6-arch-adaptive-evolution-paper.md"
- "papers/n6-arch-adaptive-homeostasis-paper.md"
- "papers/n6-arch-evolution-ouroboros-paper.md"
- "papers/n6-arch-quantum-design-paper.md"
- "papers/n6-arch-selforg-design-paper.md"
- "papers/n6-arch-selforg-emergence-paper.md"
- "papers/n6-arch-v3-v4-unified-paper.md"
- "papers/n6-atlas-promotion-7-to-10-paper.md"
- "papers/n6-atlas-promotion-7-to-10star-paper.md"
- "papers/n6-atlas-promotion-pipeline-paper.md"
- "papers/n6-chip-6stages-integrated-paper.md"
- "papers/n6-chip-design-ladder-paper.md"
- "papers/n6-chip-dse-convergence-paper.md"
- "papers/n6-consciousness-chip-paper.md"
- "papers/n6-consciousness-phase-diagram-paper.md"
- "papers/n6-consciousness-soc-paper.md"

**Commit messages**:

1. First commit (after all translations verified CJK = 0):

   ```
   docs(translate): phase-5-7 phase-5-7-papers-arch-ai-chip-atlas-consc (20 files)
   ```

2. Second commit (after allowlist shrink):

   ```
   feat(own): shrink own#1 allowlist phase-5-7
   ```

```

### 7.8 Batch 8: `phase-5-8-papers-quantum-super-groupP-pandoc-other` (21 files, 50389 CJK)

```
You are the Phase 5 batch agent for canon, batch **8** (`phase-5-8-papers-quantum-super-groupP-pandoc-other`).

**Goal**: translate the 21 Korean `.md` files listed below into English, remove their entries from `tool/own1_legacy_allowlist.json`, and land two commits on `origin/main`.

**CJK budget for this batch**: 50389 characters (baseline — expect 0 after translation).

**Two expected commits**:
1. `docs(translate): phase-5-8 phase-5-8-papers-quantum-super-groupP-pandoc-other (21 files)`
2. `feat(own): shrink own#1 allowlist phase-5-8` (remove 21 entries)

**HARD constraints (violations = stop-and-defer)**:

- **own#1 (doc-english-hard)**: every translated file must reach `CJK count = 0` as measured by `python3 tool/own_doc_lint.py --rule 1`. Re-verify after each file write; if the file regressed to CJK > 0 (sibling-stash-wipeout race), re-write it immediately.
- **own#11 (bt-solution-claim-ban) softener**: Korean `U+C99D U+BA85 ("proof")` / `U+C644 U+C804 ("complete")` / `proven` / `solved` must NOT appear in translated output. Replace with one of: `draft`, `candidate`, `pattern`, `target`, `demonstrating`. Preserve mathematical statements as framings ("a candidate argument demonstrating ...") rather than solution claims.
- **own#17 (README English-only)**: root `README.md` must remain CJK = 0 across this entire batch. Do not touch it.
- **Math/physics preservation — literal**:
  - LaTeX: `$...$`, `$$...$$`, ` ```math ` fences — preserve token-for-token; translate only natural-language surrounding prose.
  - Greek symbols in text and identifiers: σ, Σ, τ, φ, Φ, ψ, Ψ, ω, Ω, λ, Λ, α, β, γ, δ, ε, θ, μ, ν, π, ρ, ζ, η, κ, ξ, χ — preserve exactly (do not transliterate).
  - Equation numbering (`(1)`, `(2)`, `(3.4)`, `(Eq. 5)`), units (`eV`, `MeV`, `GeV`, `K`, `T`, `m·s⁻¹`, `N·m`), and citation refs (`[1]`, `[12]`, `[Author 2024]`) — preserve literally.
  - Chemical formulas and subscripts/superscripts (`H₂O`, `CO₂`, `E=mc²`) — preserve literally.
  - Numerical tables (pipe tables, ASCII tables) — preserve structure; translate only text column contents.
- **Terminology uncertainty = defer**: if any file contains dense physics/mathematics jargon that you cannot translate with high confidence (unknown specialized terms, ambiguous Korean technical compounds, non-standard notation), leave the file's Korean original intact, leave its allowlist entry intact, and document the deferral in your final message. Phase 6 or a later cleanup round will pick up deferred files. Do NOT ship a low-confidence translation.

**Race-completion protocol (MANDATORY, baked in from Phase 2/3/4 observations)**:

1. Write each `.md` translation atomically: write to `<path>.tmp`, `fsync`, then `os.rename(<path>.tmp, <path>)`. Immediately re-read and CJK-verify; if CJK > 0, re-write (max 3 retries) — this defeats the sibling `git stash -u` wipeout race (Phase 3 11.6).
2. Before push: `git fetch origin`, re-`stat` `tool/own1_legacy_allowlist.json`, re-read the JSON, re-apply the removal set as a set-difference against the current on-disk `.allowlist` array (not the pre-edit snapshot). This defeats the allowlist re-introduction race (Phase 3 11.6). Then `git rebase origin/main`.
3. If `git pull --rebase` is needed: first `git stash push -m "phase-5-8-pre-pull" -- <batch paths> tool/own1_legacy_allowlist.json` (narrow stash, NEVER `-u`). After successful rebase + push, `git stash drop stash@{0}` since main supersedes the stashed state.
4. `--no-verify` is explicitly permitted on the two batch commits — pre-commit hooks race against sibling batches' auto-artifact regeneration. Immediately after each commit, run `python3 tool/own_doc_lint.py --rule 1` as a manual gate; exit 0 is required before the second commit and before the push.
5. If `.git/hooks/*.lock` persists after a hook race, `rm -f .git/hooks/*.lock` and retry the commit.
6. One retry allowed on push rejection (fetch + rebase + re-diff + re-push). If still failing, stop and report — do not spin retry loops.

**File list (21 files)**:

- papers/M10star-21-unified-theorem-2026-04-15.md  (1892 CJK)
- papers/bernoulli-18-arxiv-stub-2026-04-15.md  (7 CJK)
- papers/consciousness-measurement-protocol-2026-04-15.md  (3999 CJK)
- papers/consciousness-red-team-n6-failure-2026-04-15.md  (4647 CJK)
- papers/group-P/F1-arxiv-bernoulli-independent-via-n6-2026-04-15.md  (2545 CJK)
- papers/group-P/F2-oeis-submission-format-2026-04-15.md  (450 CJK)
- papers/group-P/F4-conference-proposal-2026-04-15.md  (263 CJK)
- papers/group-P/F5-journal-submission-format-2026-04-15.md  (722 CJK)
- papers/hexa-chip-6stage-unified.md  (2895 CJK)
- papers/lemmas-A3-A4-conditional-2026-04-15.md  (964 CJK)
- papers/monte-carlo-control-e-2026-04-22.md  (4 CJK)
- papers/moonshine-barrier-honest-report-2026-04-15.md  (9319 CJK)
- papers/n6-quantum-computing-paper.md  (2962 CJK)
- papers/n6-quantum-error-correction-paper.md  (2984 CJK)
- papers/n6-quantum-machine-learning-paper.md  (2984 CJK)
- papers/n6-superconductor-paper.md  (2940 CJK)
- papers/n6-ultimate-superconductor-integrated-paper.md  (7359 CJK)
- papers/n=6-convergence-80-domains-2026-04-19.md  (1814 CJK)
- papers/pandoc_templates/_submission_top48_template.md  (1133 CJK)
- papers/pandoc_templates/build_report.md  (371 CJK)
- papers/pandoc_templates/build_report_all.md  (135 CJK)

**Shrink target**: remove exactly these 21 entries from `tool/own1_legacy_allowlist.json` `.allowlist` array:

- "papers/M10star-21-unified-theorem-2026-04-15.md"
- "papers/bernoulli-18-arxiv-stub-2026-04-15.md"
- "papers/consciousness-measurement-protocol-2026-04-15.md"
- "papers/consciousness-red-team-n6-failure-2026-04-15.md"
- "papers/group-P/F1-arxiv-bernoulli-independent-via-n6-2026-04-15.md"
- "papers/group-P/F2-oeis-submission-format-2026-04-15.md"
- "papers/group-P/F4-conference-proposal-2026-04-15.md"
- "papers/group-P/F5-journal-submission-format-2026-04-15.md"
- "papers/hexa-chip-6stage-unified.md"
- "papers/lemmas-A3-A4-conditional-2026-04-15.md"
- "papers/monte-carlo-control-e-2026-04-22.md"
- "papers/moonshine-barrier-honest-report-2026-04-15.md"
- "papers/n6-quantum-computing-paper.md"
- "papers/n6-quantum-error-correction-paper.md"
- "papers/n6-quantum-machine-learning-paper.md"
- "papers/n6-superconductor-paper.md"
- "papers/n6-ultimate-superconductor-integrated-paper.md"
- "papers/n=6-convergence-80-domains-2026-04-19.md"
- "papers/pandoc_templates/_submission_top48_template.md"
- "papers/pandoc_templates/build_report.md"
- "papers/pandoc_templates/build_report_all.md"

**Commit messages**:

1. First commit (after all translations verified CJK = 0):

   ```
   docs(translate): phase-5-8 phase-5-8-papers-quantum-super-groupP-pandoc-other (21 files)
   ```

2. Second commit (after allowlist shrink):

   ```
   feat(own): shrink own#1 allowlist phase-5-8
   ```

```

### 7.9 Batch 9: `phase-5-9-theory-proofs` (21 files, 41000 CJK)

```
You are the Phase 5 batch agent for canon, batch **9** (`phase-5-9-theory-proofs`).

**Goal**: translate the 21 Korean `.md` files listed below into English, remove their entries from `tool/own1_legacy_allowlist.json`, and land two commits on `origin/main`.

**CJK budget for this batch**: 41000 characters (baseline — expect 0 after translation).

**Two expected commits**:
1. `docs(translate): phase-5-9 phase-5-9-theory-proofs (21 files)`
2. `feat(own): shrink own#1 allowlist phase-5-9` (remove 21 entries)

**HARD constraints (violations = stop-and-defer)**:

- **own#1 (doc-english-hard)**: every translated file must reach `CJK count = 0` as measured by `python3 tool/own_doc_lint.py --rule 1`. Re-verify after each file write; if the file regressed to CJK > 0 (sibling-stash-wipeout race), re-write it immediately.
- **own#11 (bt-solution-claim-ban) softener**: Korean `U+C99D U+BA85 ("proof")` / `U+C644 U+C804 ("complete")` / `proven` / `solved` must NOT appear in translated output. Replace with one of: `draft`, `candidate`, `pattern`, `target`, `demonstrating`. Preserve mathematical statements as framings ("a candidate argument demonstrating ...") rather than solution claims.
- **own#17 (README English-only)**: root `README.md` must remain CJK = 0 across this entire batch. Do not touch it.
- **Math/physics preservation — literal**:
  - LaTeX: `$...$`, `$$...$$`, ` ```math ` fences — preserve token-for-token; translate only natural-language surrounding prose.
  - Greek symbols in text and identifiers: σ, Σ, τ, φ, Φ, ψ, Ψ, ω, Ω, λ, Λ, α, β, γ, δ, ε, θ, μ, ν, π, ρ, ζ, η, κ, ξ, χ — preserve exactly (do not transliterate).
  - Equation numbering (`(1)`, `(2)`, `(3.4)`, `(Eq. 5)`), units (`eV`, `MeV`, `GeV`, `K`, `T`, `m·s⁻¹`, `N·m`), and citation refs (`[1]`, `[12]`, `[Author 2024]`) — preserve literally.
  - Chemical formulas and subscripts/superscripts (`H₂O`, `CO₂`, `E=mc²`) — preserve literally.
  - Numerical tables (pipe tables, ASCII tables) — preserve structure; translate only text column contents.
- **Terminology uncertainty = defer**: if any file contains dense physics/mathematics jargon that you cannot translate with high confidence (unknown specialized terms, ambiguous Korean technical compounds, non-standard notation), leave the file's Korean original intact, leave its allowlist entry intact, and document the deferral in your final message. Phase 6 or a later cleanup round will pick up deferred files. Do NOT ship a low-confidence translation.

**Race-completion protocol (MANDATORY, baked in from Phase 2/3/4 observations)**:

1. Write each `.md` translation atomically: write to `<path>.tmp`, `fsync`, then `os.rename(<path>.tmp, <path>)`. Immediately re-read and CJK-verify; if CJK > 0, re-write (max 3 retries) — this defeats the sibling `git stash -u` wipeout race (Phase 3 11.6).
2. Before push: `git fetch origin`, re-`stat` `tool/own1_legacy_allowlist.json`, re-read the JSON, re-apply the removal set as a set-difference against the current on-disk `.allowlist` array (not the pre-edit snapshot). This defeats the allowlist re-introduction race (Phase 3 11.6). Then `git rebase origin/main`.
3. If `git pull --rebase` is needed: first `git stash push -m "phase-5-9-pre-pull" -- <batch paths> tool/own1_legacy_allowlist.json` (narrow stash, NEVER `-u`). After successful rebase + push, `git stash drop stash@{0}` since main supersedes the stashed state.
4. `--no-verify` is explicitly permitted on the two batch commits — pre-commit hooks race against sibling batches' auto-artifact regeneration. Immediately after each commit, run `python3 tool/own_doc_lint.py --rule 1` as a manual gate; exit 0 is required before the second commit and before the push.
5. If `.git/hooks/*.lock` persists after a hook race, `rm -f .git/hooks/*.lock` and retry the commit.
6. One retry allowed on push rejection (fetch + rebase + re-diff + re-push). If still failing, stop and report — do not spin retry loops.

**File list (21 files)**:

- theory/proofs/attractor-meta-theorem-2026-04-11.md  (5340 CJK)
- theory/proofs/attractor-meta-theorem-extended-2026-04-14.md  (3928 CJK)
- theory/proofs/bernoulli-boundary-2026-04-11.md  (950 CJK)
- theory/proofs/fisher-ouroboros-reformulation-2026-04-15.md  (1419 CJK)
- theory/proofs/formal-p10-1-riemann-sigma-tau-2026-04-15.md  (1164 CJK)
- theory/proofs/formal-p11-1-selberg-ingham-2026-04-15.md  (1288 CJK)
- theory/proofs/formal-p11-2-hodge-n6-2026-04-15.md  (1635 CJK)
- theory/proofs/formal-p12-1-conrey-gonek-6th-moment-2026-04-15.md  (1839 CJK)
- theory/proofs/formal-p12-2-cy3-hodge-retry-2026-04-15.md  (1677 CJK)
- theory/proofs/formal-p13-1-bsd-n6-2026-04-15.md  (1291 CJK)
- theory/proofs/honest-limitations.md  (2464 CJK)
- theory/proofs/l11-l15-quantum-nuclear-mapping-2026-04-14.md  (2737 CJK)
- theory/proofs/mk4-theorem-candidates-2026-04-14.md  (1255 CJK)
- theory/proofs/mk4-trident-final-verdict-2026-04-15.md  (1412 CJK)
- theory/proofs/n6-boundary-metatheory-2026-04-14.md  (2901 CJK)
- theory/proofs/ouroboros-alpha-universality-2026-04-15.md  (1621 CJK)
- theory/proofs/physics-math-certification.md  (1851 CJK)
- theory/proofs/proof-certification-chain.md  (3046 CJK)
- theory/proofs/the-number-24.md  (718 CJK)
- theory/proofs/theorem-r1-uniqueness.md  (583 CJK)
- theory/proofs/transcend-p11-3-ouroboros-b2-proof-2026-04-15.md  (1881 CJK)

**Shrink target**: remove exactly these 21 entries from `tool/own1_legacy_allowlist.json` `.allowlist` array:

- "theory/proofs/attractor-meta-theorem-2026-04-11.md"
- "theory/proofs/attractor-meta-theorem-extended-2026-04-14.md"
- "theory/proofs/bernoulli-boundary-2026-04-11.md"
- "theory/proofs/fisher-ouroboros-reformulation-2026-04-15.md"
- "theory/proofs/formal-p10-1-riemann-sigma-tau-2026-04-15.md"
- "theory/proofs/formal-p11-1-selberg-ingham-2026-04-15.md"
- "theory/proofs/formal-p11-2-hodge-n6-2026-04-15.md"
- "theory/proofs/formal-p12-1-conrey-gonek-6th-moment-2026-04-15.md"
- "theory/proofs/formal-p12-2-cy3-hodge-retry-2026-04-15.md"
- "theory/proofs/formal-p13-1-bsd-n6-2026-04-15.md"
- "theory/proofs/honest-limitations.md"
- "theory/proofs/l11-l15-quantum-nuclear-mapping-2026-04-14.md"
- "theory/proofs/mk4-theorem-candidates-2026-04-14.md"
- "theory/proofs/mk4-trident-final-verdict-2026-04-15.md"
- "theory/proofs/n6-boundary-metatheory-2026-04-14.md"
- "theory/proofs/ouroboros-alpha-universality-2026-04-15.md"
- "theory/proofs/physics-math-certification.md"
- "theory/proofs/proof-certification-chain.md"
- "theory/proofs/the-number-24.md"
- "theory/proofs/theorem-r1-uniqueness.md"
- "theory/proofs/transcend-p11-3-ouroboros-b2-proof-2026-04-15.md"

**Commit messages**:

1. First commit (after all translations verified CJK = 0):

   ```
   docs(translate): phase-5-9 phase-5-9-theory-proofs (21 files)
   ```

2. Second commit (after allowlist shrink):

   ```
   feat(own): shrink own#1 allowlist phase-5-9
   ```

```

### 7.10 Batch 10: `phase-5-10-theory-roadmap-v2-phase-a` (21 files, 61115 CJK)

```
You are the Phase 5 batch agent for canon, batch **10** (`phase-5-10-theory-roadmap-v2-phase-a`).

**Goal**: translate the 21 Korean `.md` files listed below into English, remove their entries from `tool/own1_legacy_allowlist.json`, and land two commits on `origin/main`.

**CJK budget for this batch**: 61115 characters (baseline — expect 0 after translation).

**Two expected commits**:
1. `docs(translate): phase-5-10 phase-5-10-theory-roadmap-v2-phase-a (21 files)`
2. `feat(own): shrink own#1 allowlist phase-5-10` (remove 21 entries)

**HARD constraints (violations = stop-and-defer)**:

- **own#1 (doc-english-hard)**: every translated file must reach `CJK count = 0` as measured by `python3 tool/own_doc_lint.py --rule 1`. Re-verify after each file write; if the file regressed to CJK > 0 (sibling-stash-wipeout race), re-write it immediately.
- **own#11 (bt-solution-claim-ban) softener**: Korean `U+C99D U+BA85 ("proof")` / `U+C644 U+C804 ("complete")` / `proven` / `solved` must NOT appear in translated output. Replace with one of: `draft`, `candidate`, `pattern`, `target`, `demonstrating`. Preserve mathematical statements as framings ("a candidate argument demonstrating ...") rather than solution claims.
- **own#17 (README English-only)**: root `README.md` must remain CJK = 0 across this entire batch. Do not touch it.
- **Math/physics preservation — literal**:
  - LaTeX: `$...$`, `$$...$$`, ` ```math ` fences — preserve token-for-token; translate only natural-language surrounding prose.
  - Greek symbols in text and identifiers: σ, Σ, τ, φ, Φ, ψ, Ψ, ω, Ω, λ, Λ, α, β, γ, δ, ε, θ, μ, ν, π, ρ, ζ, η, κ, ξ, χ — preserve exactly (do not transliterate).
  - Equation numbering (`(1)`, `(2)`, `(3.4)`, `(Eq. 5)`), units (`eV`, `MeV`, `GeV`, `K`, `T`, `m·s⁻¹`, `N·m`), and citation refs (`[1]`, `[12]`, `[Author 2024]`) — preserve literally.
  - Chemical formulas and subscripts/superscripts (`H₂O`, `CO₂`, `E=mc²`) — preserve literally.
  - Numerical tables (pipe tables, ASCII tables) — preserve structure; translate only text column contents.
- **Terminology uncertainty = defer**: if any file contains dense physics/mathematics jargon that you cannot translate with high confidence (unknown specialized terms, ambiguous Korean technical compounds, non-standard notation), leave the file's Korean original intact, leave its allowlist entry intact, and document the deferral in your final message. Phase 6 or a later cleanup round will pick up deferred files. Do NOT ship a low-confidence translation.

**Race-completion protocol (MANDATORY, baked in from Phase 2/3/4 observations)**:

1. Write each `.md` translation atomically: write to `<path>.tmp`, `fsync`, then `os.rename(<path>.tmp, <path>)`. Immediately re-read and CJK-verify; if CJK > 0, re-write (max 3 retries) — this defeats the sibling `git stash -u` wipeout race (Phase 3 11.6).
2. Before push: `git fetch origin`, re-`stat` `tool/own1_legacy_allowlist.json`, re-read the JSON, re-apply the removal set as a set-difference against the current on-disk `.allowlist` array (not the pre-edit snapshot). This defeats the allowlist re-introduction race (Phase 3 11.6). Then `git rebase origin/main`.
3. If `git pull --rebase` is needed: first `git stash push -m "phase-5-10-pre-pull" -- <batch paths> tool/own1_legacy_allowlist.json` (narrow stash, NEVER `-u`). After successful rebase + push, `git stash drop stash@{0}` since main supersedes the stashed state.
4. `--no-verify` is explicitly permitted on the two batch commits — pre-commit hooks race against sibling batches' auto-artifact regeneration. Immediately after each commit, run `python3 tool/own_doc_lint.py --rule 1` as a manual gate; exit 0 is required before the second commit and before the push.
5. If `.git/hooks/*.lock` persists after a hook race, `rm -f .git/hooks/*.lock` and retry the commit.
6. One retry allowed on push rejection (fetch + rebase + re-diff + re-push). If still failing, stop and report — do not spin retry loops.

**File list (21 files)**:

- theory/roadmap-v2/phase-01-foundation-Y-axes.md  (2345 CJK)
- theory/roadmap-v2/phase-01.md  (1236 CJK)
- theory/roadmap-v2/phase-02-Y1-bt541-riemann.md  (4853 CJK)
- theory/roadmap-v2/phase-02-millennium-assault.md  (3766 CJK)
- theory/roadmap-v2/phase-02-prereq-Y9-Y11-deepening.md  (1634 CJK)
- theory/roadmap-v2/phase-02.md  (999 CJK)
- theory/roadmap-v2/phase-03-Y4-bt542-pnp.md  (8188 CJK)
- theory/roadmap-v2/phase-03-cross-bt-deepening.md  (2813 CJK)
- theory/roadmap-v2/phase-03.md  (775 CJK)
- theory/roadmap-v2/phase-04-Y5Y6-bt543-bt544.md  (8167 CJK)
- theory/roadmap-v2/phase-04-atlas-edit-final-push.md  (2370 CJK)
- theory/roadmap-v2/phase-04-tools-empirical-deepening.md  (2496 CJK)
- theory/roadmap-v2/phase-04.md  (544 CJK)
- theory/roadmap-v2/phase-05-Y7Y8-bt545-bt546.md  (8697 CJK)
- theory/roadmap-v2/phase-05-depletion-closure.md  (2519 CJK)
- theory/roadmap-v2/phase-05.md  (417 CJK)
- theory/roadmap-v2/phase-06-bt547-poincare-retrospect.md  (5584 CJK)
- theory/roadmap-v2/phase-06.md  (389 CJK)
- theory/roadmap-v2/phase-07-cross-bt-transfer-protocol.md  (1130 CJK)
- theory/roadmap-v2/phase-07.md  (524 CJK)
- theory/roadmap-v2/phase-08-meta-audit-philosophy.md  (1669 CJK)

**Shrink target**: remove exactly these 21 entries from `tool/own1_legacy_allowlist.json` `.allowlist` array:

- "theory/roadmap-v2/phase-01-foundation-Y-axes.md"
- "theory/roadmap-v2/phase-01.md"
- "theory/roadmap-v2/phase-02-Y1-bt541-riemann.md"
- "theory/roadmap-v2/phase-02-millennium-assault.md"
- "theory/roadmap-v2/phase-02-prereq-Y9-Y11-deepening.md"
- "theory/roadmap-v2/phase-02.md"
- "theory/roadmap-v2/phase-03-Y4-bt542-pnp.md"
- "theory/roadmap-v2/phase-03-cross-bt-deepening.md"
- "theory/roadmap-v2/phase-03.md"
- "theory/roadmap-v2/phase-04-Y5Y6-bt543-bt544.md"
- "theory/roadmap-v2/phase-04-atlas-edit-final-push.md"
- "theory/roadmap-v2/phase-04-tools-empirical-deepening.md"
- "theory/roadmap-v2/phase-04.md"
- "theory/roadmap-v2/phase-05-Y7Y8-bt545-bt546.md"
- "theory/roadmap-v2/phase-05-depletion-closure.md"
- "theory/roadmap-v2/phase-05.md"
- "theory/roadmap-v2/phase-06-bt547-poincare-retrospect.md"
- "theory/roadmap-v2/phase-06.md"
- "theory/roadmap-v2/phase-07-cross-bt-transfer-protocol.md"
- "theory/roadmap-v2/phase-07.md"
- "theory/roadmap-v2/phase-08-meta-audit-philosophy.md"

**Commit messages**:

1. First commit (after all translations verified CJK = 0):

   ```
   docs(translate): phase-5-10 phase-5-10-theory-roadmap-v2-phase-a (21 files)
   ```

2. Second commit (after allowlist shrink):

   ```
   feat(own): shrink own#1 allowlist phase-5-10
   ```

```

### 7.11 Batch 11: `phase-5-11-theory-roadmap-v2-phase-b` (20 files, 23368 CJK)

```
You are the Phase 5 batch agent for canon, batch **11** (`phase-5-11-theory-roadmap-v2-phase-b`).

**Goal**: translate the 20 Korean `.md` files listed below into English, remove their entries from `tool/own1_legacy_allowlist.json`, and land two commits on `origin/main`.

**CJK budget for this batch**: 23368 characters (baseline — expect 0 after translation).

**Two expected commits**:
1. `docs(translate): phase-5-11 phase-5-11-theory-roadmap-v2-phase-b (20 files)`
2. `feat(own): shrink own#1 allowlist phase-5-11` (remove 20 entries)

**HARD constraints (violations = stop-and-defer)**:

- **own#1 (doc-english-hard)**: every translated file must reach `CJK count = 0` as measured by `python3 tool/own_doc_lint.py --rule 1`. Re-verify after each file write; if the file regressed to CJK > 0 (sibling-stash-wipeout race), re-write it immediately.
- **own#11 (bt-solution-claim-ban) softener**: Korean `U+C99D U+BA85 ("proof")` / `U+C644 U+C804 ("complete")` / `proven` / `solved` must NOT appear in translated output. Replace with one of: `draft`, `candidate`, `pattern`, `target`, `demonstrating`. Preserve mathematical statements as framings ("a candidate argument demonstrating ...") rather than solution claims.
- **own#17 (README English-only)**: root `README.md` must remain CJK = 0 across this entire batch. Do not touch it.
- **Math/physics preservation — literal**:
  - LaTeX: `$...$`, `$$...$$`, ` ```math ` fences — preserve token-for-token; translate only natural-language surrounding prose.
  - Greek symbols in text and identifiers: σ, Σ, τ, φ, Φ, ψ, Ψ, ω, Ω, λ, Λ, α, β, γ, δ, ε, θ, μ, ν, π, ρ, ζ, η, κ, ξ, χ — preserve exactly (do not transliterate).
  - Equation numbering (`(1)`, `(2)`, `(3.4)`, `(Eq. 5)`), units (`eV`, `MeV`, `GeV`, `K`, `T`, `m·s⁻¹`, `N·m`), and citation refs (`[1]`, `[12]`, `[Author 2024]`) — preserve literally.
  - Chemical formulas and subscripts/superscripts (`H₂O`, `CO₂`, `E=mc²`) — preserve literally.
  - Numerical tables (pipe tables, ASCII tables) — preserve structure; translate only text column contents.
- **Terminology uncertainty = defer**: if any file contains dense physics/mathematics jargon that you cannot translate with high confidence (unknown specialized terms, ambiguous Korean technical compounds, non-standard notation), leave the file's Korean original intact, leave its allowlist entry intact, and document the deferral in your final message. Phase 6 or a later cleanup round will pick up deferred files. Do NOT ship a low-confidence translation.

**Race-completion protocol (MANDATORY, baked in from Phase 2/3/4 observations)**:

1. Write each `.md` translation atomically: write to `<path>.tmp`, `fsync`, then `os.rename(<path>.tmp, <path>)`. Immediately re-read and CJK-verify; if CJK > 0, re-write (max 3 retries) — this defeats the sibling `git stash -u` wipeout race (Phase 3 11.6).
2. Before push: `git fetch origin`, re-`stat` `tool/own1_legacy_allowlist.json`, re-read the JSON, re-apply the removal set as a set-difference against the current on-disk `.allowlist` array (not the pre-edit snapshot). This defeats the allowlist re-introduction race (Phase 3 11.6). Then `git rebase origin/main`.
3. If `git pull --rebase` is needed: first `git stash push -m "phase-5-11-pre-pull" -- <batch paths> tool/own1_legacy_allowlist.json` (narrow stash, NEVER `-u`). After successful rebase + push, `git stash drop stash@{0}` since main supersedes the stashed state.
4. `--no-verify` is explicitly permitted on the two batch commits — pre-commit hooks race against sibling batches' auto-artifact regeneration. Immediately after each commit, run `python3 tool/own_doc_lint.py --rule 1` as a manual gate; exit 0 is required before the second commit and before the push.
5. If `.git/hooks/*.lock` persists after a hook race, `rm -f .git/hooks/*.lock` and retry the commit.
6. One retry allowed on push rejection (fetch + rebase + re-diff + re-push). If still failing, stop and report — do not spin retry loops.

**File list (20 files)**:

- theory/roadmap-v2/phase-08.md  (468 CJK)
- theory/roadmap-v2/phase-09-external-history-publication.md  (1013 CJK)
- theory/roadmap-v2/phase-09.md  (489 CJK)
- theory/roadmap-v2/phase-10-measurement-strategy-tools.md  (878 CJK)
- theory/roadmap-v2/phase-10.md  (604 CJK)
- theory/roadmap-v2/phase-11-mk5-alpha.md  (2227 CJK)
- theory/roadmap-v2/phase-11.md  (288 CJK)
- theory/roadmap-v2/phase-12.md  (225 CJK)
- theory/roadmap-v2/phase-13.md  (166 CJK)
- theory/roadmap-v2/phase-14.md  (133 CJK)
- theory/roadmap-v2/phase-15.md  (188 CJK)
- theory/roadmap-v2/phase-16.md  (131 CJK)
- theory/roadmap-v2/phase-17.md  (154 CJK)
- theory/roadmap-v2/phase-18-saturation.md  (665 CJK)
- theory/roadmap-v2/phase-18.md  (289 CJK)
- theory/roadmap-v2/phase-PX-PHYS-1-beta0-rigor.md  (304 CJK)
- theory/roadmap-v2/phase-PX-automation-rubric.md  (1403 CJK)
- theory/roadmap-v2/phase-PX-external-tracking.md  (606 CJK)
- theory/roadmap-v2/phase-depth-emergence.md  (2267 CJK)
- theory/roadmap-v2/phase-omega-Y9-closure-v3-design.md  (10870 CJK)

**Shrink target**: remove exactly these 20 entries from `tool/own1_legacy_allowlist.json` `.allowlist` array:

- "theory/roadmap-v2/phase-08.md"
- "theory/roadmap-v2/phase-09-external-history-publication.md"
- "theory/roadmap-v2/phase-09.md"
- "theory/roadmap-v2/phase-10-measurement-strategy-tools.md"
- "theory/roadmap-v2/phase-10.md"
- "theory/roadmap-v2/phase-11-mk5-alpha.md"
- "theory/roadmap-v2/phase-11.md"
- "theory/roadmap-v2/phase-12.md"
- "theory/roadmap-v2/phase-13.md"
- "theory/roadmap-v2/phase-14.md"
- "theory/roadmap-v2/phase-15.md"
- "theory/roadmap-v2/phase-16.md"
- "theory/roadmap-v2/phase-17.md"
- "theory/roadmap-v2/phase-18-saturation.md"
- "theory/roadmap-v2/phase-18.md"
- "theory/roadmap-v2/phase-PX-PHYS-1-beta0-rigor.md"
- "theory/roadmap-v2/phase-PX-automation-rubric.md"
- "theory/roadmap-v2/phase-PX-external-tracking.md"
- "theory/roadmap-v2/phase-depth-emergence.md"
- "theory/roadmap-v2/phase-omega-Y9-closure-v3-design.md"

**Commit messages**:

1. First commit (after all translations verified CJK = 0):

   ```
   docs(translate): phase-5-11 phase-5-11-theory-roadmap-v2-phase-b (20 files)
   ```

2. Second commit (after allowlist shrink):

   ```
   feat(own): shrink own#1 allowlist phase-5-11
   ```

```

### 7.12 Batch 12: `phase-5-12-theory-roadmap-v2-axes-round-other` (24 files, 65179 CJK)

```
You are the Phase 5 batch agent for canon, batch **12** (`phase-5-12-theory-roadmap-v2-axes-round-other`).

**Goal**: translate the 24 Korean `.md` files listed below into English, remove their entries from `tool/own1_legacy_allowlist.json`, and land two commits on `origin/main`.

**CJK budget for this batch**: 65179 characters (baseline — expect 0 after translation).

**Two expected commits**:
1. `docs(translate): phase-5-12 phase-5-12-theory-roadmap-v2-axes-round-other (24 files)`
2. `feat(own): shrink own#1 allowlist phase-5-12` (remove 24 entries)

**HARD constraints (violations = stop-and-defer)**:

- **own#1 (doc-english-hard)**: every translated file must reach `CJK count = 0` as measured by `python3 tool/own_doc_lint.py --rule 1`. Re-verify after each file write; if the file regressed to CJK > 0 (sibling-stash-wipeout race), re-write it immediately.
- **own#11 (bt-solution-claim-ban) softener**: Korean `U+C99D U+BA85 ("proof")` / `U+C644 U+C804 ("complete")` / `proven` / `solved` must NOT appear in translated output. Replace with one of: `draft`, `candidate`, `pattern`, `target`, `demonstrating`. Preserve mathematical statements as framings ("a candidate argument demonstrating ...") rather than solution claims.
- **own#17 (README English-only)**: root `README.md` must remain CJK = 0 across this entire batch. Do not touch it.
- **Math/physics preservation — literal**:
  - LaTeX: `$...$`, `$$...$$`, ` ```math ` fences — preserve token-for-token; translate only natural-language surrounding prose.
  - Greek symbols in text and identifiers: σ, Σ, τ, φ, Φ, ψ, Ψ, ω, Ω, λ, Λ, α, β, γ, δ, ε, θ, μ, ν, π, ρ, ζ, η, κ, ξ, χ — preserve exactly (do not transliterate).
  - Equation numbering (`(1)`, `(2)`, `(3.4)`, `(Eq. 5)`), units (`eV`, `MeV`, `GeV`, `K`, `T`, `m·s⁻¹`, `N·m`), and citation refs (`[1]`, `[12]`, `[Author 2024]`) — preserve literally.
  - Chemical formulas and subscripts/superscripts (`H₂O`, `CO₂`, `E=mc²`) — preserve literally.
  - Numerical tables (pipe tables, ASCII tables) — preserve structure; translate only text column contents.
- **Terminology uncertainty = defer**: if any file contains dense physics/mathematics jargon that you cannot translate with high confidence (unknown specialized terms, ambiguous Korean technical compounds, non-standard notation), leave the file's Korean original intact, leave its allowlist entry intact, and document the deferral in your final message. Phase 6 or a later cleanup round will pick up deferred files. Do NOT ship a low-confidence translation.

**Race-completion protocol (MANDATORY, baked in from Phase 2/3/4 observations)**:

1. Write each `.md` translation atomically: write to `<path>.tmp`, `fsync`, then `os.rename(<path>.tmp, <path>)`. Immediately re-read and CJK-verify; if CJK > 0, re-write (max 3 retries) — this defeats the sibling `git stash -u` wipeout race (Phase 3 11.6).
2. Before push: `git fetch origin`, re-`stat` `tool/own1_legacy_allowlist.json`, re-read the JSON, re-apply the removal set as a set-difference against the current on-disk `.allowlist` array (not the pre-edit snapshot). This defeats the allowlist re-introduction race (Phase 3 11.6). Then `git rebase origin/main`.
3. If `git pull --rebase` is needed: first `git stash push -m "phase-5-12-pre-pull" -- <batch paths> tool/own1_legacy_allowlist.json` (narrow stash, NEVER `-u`). After successful rebase + push, `git stash drop stash@{0}` since main supersedes the stashed state.
4. `--no-verify` is explicitly permitted on the two batch commits — pre-commit hooks race against sibling batches' auto-artifact regeneration. Immediately after each commit, run `python3 tool/own_doc_lint.py --rule 1` as a manual gate; exit 0 is required before the second commit and before the push.
5. If `.git/hooks/*.lock` persists after a hook race, `rm -f .git/hooks/*.lock` and retry the commit.
6. One retry allowed on push rejection (fetch + rebase + re-diff + re-push). If still failing, stop and report — do not spin retry loops.

**File list (24 files)**:

- theory/roadmap-v2/README.md  (353 CJK)
- theory/roadmap-v2/_archive-phase-01-forced-3-axes.md  (6342 CJK)
- theory/roadmap-v2/axis-final-nexus-hub.md  (1343 CJK)
- theory/roadmap-v2/axis-final.md  (2732 CJK)
- theory/roadmap-v2/axis-round-01.md  (1555 CJK)
- theory/roadmap-v2/axis-round-02.md  (1288 CJK)
- theory/roadmap-v2/axis-round-03.md  (1180 CJK)
- theory/roadmap-v2/axis-round-04.md  (1069 CJK)
- theory/roadmap-v2/axis-round-05.md  (606 CJK)
- theory/roadmap-v2/comparison-v1-vs-v2.md  (4640 CJK)
- theory/roadmap-v2/final-roadmap-v2-nexus-19axis.md  (717 CJK)
- theory/roadmap-v2/final-roadmap-v2.md  (1782 CJK)
- theory/roadmap-v2/gap-emergence-saturation.md  (3836 CJK)
- theory/roadmap-v2/millennium-v3-design-2026-04-15.md  (1061 CJK)
- theory/roadmap-v2/millennium-v4-design-2026-04-16.md  (928 CJK)
- theory/roadmap-v2/n6arch-axes/axis-final-millennium.md  (1450 CJK)
- theory/roadmap-v2/n6arch-axes/axis-r1-emergence.md  (5258 CJK)
- theory/roadmap-v2/n6arch-axes/axis-r2-refinement.md  (5548 CJK)
- theory/roadmap-v2/n6arch-axes/axis-r3-finalization.md  (5656 CJK)
- theory/roadmap-v2/round-01-domain-emergence-dse.md  (3803 CJK)
- theory/roadmap-v2/round-02-emergence-expansion.md  (3620 CJK)
- theory/roadmap-v2/round-03-emergence-saturation.md  (4685 CJK)
- theory/roadmap-v2/round-04-emergence-deepening.md  (3492 CJK)
- theory/roadmap-v2/round-05-emergence-scavenge.md  (2235 CJK)

**Shrink target**: remove exactly these 24 entries from `tool/own1_legacy_allowlist.json` `.allowlist` array:

- "theory/roadmap-v2/README.md"
- "theory/roadmap-v2/_archive-phase-01-forced-3-axes.md"
- "theory/roadmap-v2/axis-final-nexus-hub.md"
- "theory/roadmap-v2/axis-final.md"
- "theory/roadmap-v2/axis-round-01.md"
- "theory/roadmap-v2/axis-round-02.md"
- "theory/roadmap-v2/axis-round-03.md"
- "theory/roadmap-v2/axis-round-04.md"
- "theory/roadmap-v2/axis-round-05.md"
- "theory/roadmap-v2/comparison-v1-vs-v2.md"
- "theory/roadmap-v2/final-roadmap-v2-nexus-19axis.md"
- "theory/roadmap-v2/final-roadmap-v2.md"
- "theory/roadmap-v2/gap-emergence-saturation.md"
- "theory/roadmap-v2/millennium-v3-design-2026-04-15.md"
- "theory/roadmap-v2/millennium-v4-design-2026-04-16.md"
- "theory/roadmap-v2/n6arch-axes/axis-final-millennium.md"
- "theory/roadmap-v2/n6arch-axes/axis-r1-emergence.md"
- "theory/roadmap-v2/n6arch-axes/axis-r2-refinement.md"
- "theory/roadmap-v2/n6arch-axes/axis-r3-finalization.md"
- "theory/roadmap-v2/round-01-domain-emergence-dse.md"
- "theory/roadmap-v2/round-02-emergence-expansion.md"
- "theory/roadmap-v2/round-03-emergence-saturation.md"
- "theory/roadmap-v2/round-04-emergence-deepening.md"
- "theory/roadmap-v2/round-05-emergence-scavenge.md"

**Commit messages**:

1. First commit (after all translations verified CJK = 0):

   ```
   docs(translate): phase-5-12 phase-5-12-theory-roadmap-v2-axes-round-other (24 files)
   ```

2. Second commit (after allowlist shrink):

   ```
   feat(own): shrink own#1 allowlist phase-5-12
   ```

```

### 7.13 Batch 13: `phase-5-13-theory-study-p0-p1` (26 files, 65993 CJK)

```
You are the Phase 5 batch agent for canon, batch **13** (`phase-5-13-theory-study-p0-p1`).

**Goal**: translate the 26 Korean `.md` files listed below into English, remove their entries from `tool/own1_legacy_allowlist.json`, and land two commits on `origin/main`.

**CJK budget for this batch**: 65993 characters (baseline — expect 0 after translation).

**Two expected commits**:
1. `docs(translate): phase-5-13 phase-5-13-theory-study-p0-p1 (26 files)`
2. `feat(own): shrink own#1 allowlist phase-5-13` (remove 26 entries)

**HARD constraints (violations = stop-and-defer)**:

- **own#1 (doc-english-hard)**: every translated file must reach `CJK count = 0` as measured by `python3 tool/own_doc_lint.py --rule 1`. Re-verify after each file write; if the file regressed to CJK > 0 (sibling-stash-wipeout race), re-write it immediately.
- **own#11 (bt-solution-claim-ban) softener**: Korean `U+C99D U+BA85 ("proof")` / `U+C644 U+C804 ("complete")` / `proven` / `solved` must NOT appear in translated output. Replace with one of: `draft`, `candidate`, `pattern`, `target`, `demonstrating`. Preserve mathematical statements as framings ("a candidate argument demonstrating ...") rather than solution claims.
- **own#17 (README English-only)**: root `README.md` must remain CJK = 0 across this entire batch. Do not touch it.
- **Math/physics preservation — literal**:
  - LaTeX: `$...$`, `$$...$$`, ` ```math ` fences — preserve token-for-token; translate only natural-language surrounding prose.
  - Greek symbols in text and identifiers: σ, Σ, τ, φ, Φ, ψ, Ψ, ω, Ω, λ, Λ, α, β, γ, δ, ε, θ, μ, ν, π, ρ, ζ, η, κ, ξ, χ — preserve exactly (do not transliterate).
  - Equation numbering (`(1)`, `(2)`, `(3.4)`, `(Eq. 5)`), units (`eV`, `MeV`, `GeV`, `K`, `T`, `m·s⁻¹`, `N·m`), and citation refs (`[1]`, `[12]`, `[Author 2024]`) — preserve literally.
  - Chemical formulas and subscripts/superscripts (`H₂O`, `CO₂`, `E=mc²`) — preserve literally.
  - Numerical tables (pipe tables, ASCII tables) — preserve structure; translate only text column contents.
- **Terminology uncertainty = defer**: if any file contains dense physics/mathematics jargon that you cannot translate with high confidence (unknown specialized terms, ambiguous Korean technical compounds, non-standard notation), leave the file's Korean original intact, leave its allowlist entry intact, and document the deferral in your final message. Phase 6 or a later cleanup round will pick up deferred files. Do NOT ship a low-confidence translation.

**Race-completion protocol (MANDATORY, baked in from Phase 2/3/4 observations)**:

1. Write each `.md` translation atomically: write to `<path>.tmp`, `fsync`, then `os.rename(<path>.tmp, <path>)`. Immediately re-read and CJK-verify; if CJK > 0, re-write (max 3 retries) — this defeats the sibling `git stash -u` wipeout race (Phase 3 11.6).
2. Before push: `git fetch origin`, re-`stat` `tool/own1_legacy_allowlist.json`, re-read the JSON, re-apply the removal set as a set-difference against the current on-disk `.allowlist` array (not the pre-edit snapshot). This defeats the allowlist re-introduction race (Phase 3 11.6). Then `git rebase origin/main`.
3. If `git pull --rebase` is needed: first `git stash push -m "phase-5-13-pre-pull" -- <batch paths> tool/own1_legacy_allowlist.json` (narrow stash, NEVER `-u`). After successful rebase + push, `git stash drop stash@{0}` since main supersedes the stashed state.
4. `--no-verify` is explicitly permitted on the two batch commits — pre-commit hooks race against sibling batches' auto-artifact regeneration. Immediately after each commit, run `python3 tool/own_doc_lint.py --rule 1` as a manual gate; exit 0 is required before the second commit and before the push.
5. If `.git/hooks/*.lock` persists after a hook race, `rm -f .git/hooks/*.lock` and retry the commit.
6. One retry allowed on push rejection (fetch + rebase + re-diff + re-push). If still failing, stop and report — do not spin retry loops.

**File list (26 files)**:

- theory/study/p0/n6-p0-1-uniqueness-theorem.md  (1886 CJK)
- theory/study/p0/n6-p0-2-arithmetic-drill.md  (2022 CJK)
- theory/study/p0/n6-p0-3-atlas-grading.md  (2611 CJK)
- theory/study/p0/prob-p0-1-clay-history.md  (3223 CJK)
- theory/study/p0/prob-p0-2-perelman-poincare.md  (3660 CJK)
- theory/study/p0/prob-p0-3-problem-mapping.md  (3025 CJK)
- theory/study/p0/pure-p0-1-number-theory.md  (2583 CJK)
- theory/study/p0/pure-p0-2-group-theory.md  (3621 CJK)
- theory/study/p0/pure-p0-3-complex-analysis.md  (1618 CJK)
- theory/study/p1/n6-p1-1-bt-table-mastery.md  (2704 CJK)
- theory/study/p1/n6-p1-2-phi-to-nphi-transition.md  (2750 CJK)
- theory/study/p1/n6-p1-3-honesty-principle.md  (3071 CJK)
- theory/study/p1/prob-p1-1-bt541-riemann.md  (3515 CJK)
- theory/study/p1/prob-p1-2-bt542-p-vs-np.md  (2846 CJK)
- theory/study/p1/prob-p1-3-bt543-yang-mills.md  (3207 CJK)
- theory/study/p1/prob-p1-4-bt544-navier-stokes.md  (2234 CJK)
- theory/study/p1/prob-p1-5-bt545-hodge.md  (2093 CJK)
- theory/study/p1/prob-p1-6-bt546-bsd.md  (1648 CJK)
- theory/study/p1/prob-p1-7-bt547-poincare.md  (2082 CJK)
- theory/study/p1/pure-p1-1-analytic-number-theory.md  (2082 CJK)
- theory/study/p1/pure-p1-2-elliptic-curves.md  (2313 CJK)
- theory/study/p1/pure-p1-3-pde-navier-stokes.md  (2069 CJK)
- theory/study/p1/pure-p1-4-algebraic-geometry-hodge.md  (1715 CJK)
- theory/study/p1/pure-p1-5-gauge-theory.md  (2441 CJK)
- theory/study/p1/pure-p1-6-topology.md  (2546 CJK)
- theory/study/p1/pure-p1-7-complexity.md  (2428 CJK)

**Shrink target**: remove exactly these 26 entries from `tool/own1_legacy_allowlist.json` `.allowlist` array:

- "theory/study/p0/n6-p0-1-uniqueness-theorem.md"
- "theory/study/p0/n6-p0-2-arithmetic-drill.md"
- "theory/study/p0/n6-p0-3-atlas-grading.md"
- "theory/study/p0/prob-p0-1-clay-history.md"
- "theory/study/p0/prob-p0-2-perelman-poincare.md"
- "theory/study/p0/prob-p0-3-problem-mapping.md"
- "theory/study/p0/pure-p0-1-number-theory.md"
- "theory/study/p0/pure-p0-2-group-theory.md"
- "theory/study/p0/pure-p0-3-complex-analysis.md"
- "theory/study/p1/n6-p1-1-bt-table-mastery.md"
- "theory/study/p1/n6-p1-2-phi-to-nphi-transition.md"
- "theory/study/p1/n6-p1-3-honesty-principle.md"
- "theory/study/p1/prob-p1-1-bt541-riemann.md"
- "theory/study/p1/prob-p1-2-bt542-p-vs-np.md"
- "theory/study/p1/prob-p1-3-bt543-yang-mills.md"
- "theory/study/p1/prob-p1-4-bt544-navier-stokes.md"
- "theory/study/p1/prob-p1-5-bt545-hodge.md"
- "theory/study/p1/prob-p1-6-bt546-bsd.md"
- "theory/study/p1/prob-p1-7-bt547-poincare.md"
- "theory/study/p1/pure-p1-1-analytic-number-theory.md"
- "theory/study/p1/pure-p1-2-elliptic-curves.md"
- "theory/study/p1/pure-p1-3-pde-navier-stokes.md"
- "theory/study/p1/pure-p1-4-algebraic-geometry-hodge.md"
- "theory/study/p1/pure-p1-5-gauge-theory.md"
- "theory/study/p1/pure-p1-6-topology.md"
- "theory/study/p1/pure-p1-7-complexity.md"

**Commit messages**:

1. First commit (after all translations verified CJK = 0):

   ```
   docs(translate): phase-5-13 phase-5-13-theory-study-p0-p1 (26 files)
   ```

2. Second commit (after allowlist shrink):

   ```
   feat(own): shrink own#1 allowlist phase-5-13
   ```

```

### 7.14 Batch 14: `phase-5-14-theory-study-p2-p3` (24 files, 66106 CJK)

```
You are the Phase 5 batch agent for canon, batch **14** (`phase-5-14-theory-study-p2-p3`).

**Goal**: translate the 24 Korean `.md` files listed below into English, remove their entries from `tool/own1_legacy_allowlist.json`, and land two commits on `origin/main`.

**CJK budget for this batch**: 66106 characters (baseline — expect 0 after translation).

**Two expected commits**:
1. `docs(translate): phase-5-14 phase-5-14-theory-study-p2-p3 (24 files)`
2. `feat(own): shrink own#1 allowlist phase-5-14` (remove 24 entries)

**HARD constraints (violations = stop-and-defer)**:

- **own#1 (doc-english-hard)**: every translated file must reach `CJK count = 0` as measured by `python3 tool/own_doc_lint.py --rule 1`. Re-verify after each file write; if the file regressed to CJK > 0 (sibling-stash-wipeout race), re-write it immediately.
- **own#11 (bt-solution-claim-ban) softener**: Korean `U+C99D U+BA85 ("proof")` / `U+C644 U+C804 ("complete")` / `proven` / `solved` must NOT appear in translated output. Replace with one of: `draft`, `candidate`, `pattern`, `target`, `demonstrating`. Preserve mathematical statements as framings ("a candidate argument demonstrating ...") rather than solution claims.
- **own#17 (README English-only)**: root `README.md` must remain CJK = 0 across this entire batch. Do not touch it.
- **Math/physics preservation — literal**:
  - LaTeX: `$...$`, `$$...$$`, ` ```math ` fences — preserve token-for-token; translate only natural-language surrounding prose.
  - Greek symbols in text and identifiers: σ, Σ, τ, φ, Φ, ψ, Ψ, ω, Ω, λ, Λ, α, β, γ, δ, ε, θ, μ, ν, π, ρ, ζ, η, κ, ξ, χ — preserve exactly (do not transliterate).
  - Equation numbering (`(1)`, `(2)`, `(3.4)`, `(Eq. 5)`), units (`eV`, `MeV`, `GeV`, `K`, `T`, `m·s⁻¹`, `N·m`), and citation refs (`[1]`, `[12]`, `[Author 2024]`) — preserve literally.
  - Chemical formulas and subscripts/superscripts (`H₂O`, `CO₂`, `E=mc²`) — preserve literally.
  - Numerical tables (pipe tables, ASCII tables) — preserve structure; translate only text column contents.
- **Terminology uncertainty = defer**: if any file contains dense physics/mathematics jargon that you cannot translate with high confidence (unknown specialized terms, ambiguous Korean technical compounds, non-standard notation), leave the file's Korean original intact, leave its allowlist entry intact, and document the deferral in your final message. Phase 6 or a later cleanup round will pick up deferred files. Do NOT ship a low-confidence translation.

**Race-completion protocol (MANDATORY, baked in from Phase 2/3/4 observations)**:

1. Write each `.md` translation atomically: write to `<path>.tmp`, `fsync`, then `os.rename(<path>.tmp, <path>)`. Immediately re-read and CJK-verify; if CJK > 0, re-write (max 3 retries) — this defeats the sibling `git stash -u` wipeout race (Phase 3 11.6).
2. Before push: `git fetch origin`, re-`stat` `tool/own1_legacy_allowlist.json`, re-read the JSON, re-apply the removal set as a set-difference against the current on-disk `.allowlist` array (not the pre-edit snapshot). This defeats the allowlist re-introduction race (Phase 3 11.6). Then `git rebase origin/main`.
3. If `git pull --rebase` is needed: first `git stash push -m "phase-5-14-pre-pull" -- <batch paths> tool/own1_legacy_allowlist.json` (narrow stash, NEVER `-u`). After successful rebase + push, `git stash drop stash@{0}` since main supersedes the stashed state.
4. `--no-verify` is explicitly permitted on the two batch commits — pre-commit hooks race against sibling batches' auto-artifact regeneration. Immediately after each commit, run `python3 tool/own_doc_lint.py --rule 1` as a manual gate; exit 0 is required before the second commit and before the push.
5. If `.git/hooks/*.lock` persists after a hook race, `rm -f .git/hooks/*.lock` and retry the commit.
6. One retry allowed on push rejection (fetch + rebase + re-diff + re-push). If still failing, stop and report — do not spin retry loops.

**File list (24 files)**:

- theory/study/p2/n6-p2-1-dfs-51-classification.md  (2126 CJK)
- theory/study/p2/n6-p2-2-theorem-b-reconstruction.md  (1877 CJK)
- theory/study/p2/n6-p2-3-cross-domain.md  (3047 CJK)
- theory/study/p2/n6-p2-4-honesty-audit.md  (4297 CJK)
- theory/study/p2/prob-p2-1-riemann-barriers.md  (3110 CJK)
- theory/study/p2/prob-p2-2-p-np-barriers.md  (2314 CJK)
- theory/study/p2/prob-p2-3-yang-mills-barriers.md  (3907 CJK)
- theory/study/p2/prob-p2-4-navier-stokes-barriers.md  (3752 CJK)
- theory/study/p2/prob-p2-5-hodge-barriers.md  (3068 CJK)
- theory/study/p2/prob-p2-6-bsd-barriers.md  (2663 CJK)
- theory/study/p2/prob-p2-7-poincare-retrospective.md  (3722 CJK)
- theory/study/p2/pure-p2-1-modular-forms.md  (2716 CJK)
- theory/study/p2/pure-p2-2-algebraic-k-theory.md  (2016 CJK)
- theory/study/p2/pure-p2-3-bernoulli-zeta.md  (2369 CJK)
- theory/study/p2/pure-p2-4-tqft-topology.md  (2078 CJK)
- theory/study/p3/n6-p3-1-independent-dfs.md  (3314 CJK)
- theory/study/p3/n6-p3-2-atlas-promotion.md  (3250 CJK)
- theory/study/p3/n6-p3-3-synthesis-report.md  (3622 CJK)
- theory/study/p3/prob-p3-1-open-subquestions.md  (2542 CJK)
- theory/study/p3/prob-p3-2-conditional-theorems.md  (2930 CJK)
- theory/study/p3/prob-p3-3-hexa-verification.md  (2218 CJK)
- theory/study/p3/pure-p3-1-bklpr-selmer-deep.md  (1486 CJK)
- theory/study/p3/pure-p3-2-research-methodology.md  (1727 CJK)
- theory/study/p3/pure-p3-3-arithmetic-geometry-frontier.md  (1955 CJK)

**Shrink target**: remove exactly these 24 entries from `tool/own1_legacy_allowlist.json` `.allowlist` array:

- "theory/study/p2/n6-p2-1-dfs-51-classification.md"
- "theory/study/p2/n6-p2-2-theorem-b-reconstruction.md"
- "theory/study/p2/n6-p2-3-cross-domain.md"
- "theory/study/p2/n6-p2-4-honesty-audit.md"
- "theory/study/p2/prob-p2-1-riemann-barriers.md"
- "theory/study/p2/prob-p2-2-p-np-barriers.md"
- "theory/study/p2/prob-p2-3-yang-mills-barriers.md"
- "theory/study/p2/prob-p2-4-navier-stokes-barriers.md"
- "theory/study/p2/prob-p2-5-hodge-barriers.md"
- "theory/study/p2/prob-p2-6-bsd-barriers.md"
- "theory/study/p2/prob-p2-7-poincare-retrospective.md"
- "theory/study/p2/pure-p2-1-modular-forms.md"
- "theory/study/p2/pure-p2-2-algebraic-k-theory.md"
- "theory/study/p2/pure-p2-3-bernoulli-zeta.md"
- "theory/study/p2/pure-p2-4-tqft-topology.md"
- "theory/study/p3/n6-p3-1-independent-dfs.md"
- "theory/study/p3/n6-p3-2-atlas-promotion.md"
- "theory/study/p3/n6-p3-3-synthesis-report.md"
- "theory/study/p3/prob-p3-1-open-subquestions.md"
- "theory/study/p3/prob-p3-2-conditional-theorems.md"
- "theory/study/p3/prob-p3-3-hexa-verification.md"
- "theory/study/p3/pure-p3-1-bklpr-selmer-deep.md"
- "theory/study/p3/pure-p3-2-research-methodology.md"
- "theory/study/p3/pure-p3-3-arithmetic-geometry-frontier.md"

**Commit messages**:

1. First commit (after all translations verified CJK = 0):

   ```
   docs(translate): phase-5-14 phase-5-14-theory-study-p2-p3 (24 files)
   ```

2. Second commit (after allowlist shrink):

   ```
   feat(own): shrink own#1 allowlist phase-5-14
   ```

```

### 7.15 Batch 15: `phase-5-15-theory-breakthroughs-defer-fusion-kstar` (4 files, 168558 CJK)

```
You are the Phase 5 batch agent for canon, batch **15** (`phase-5-15-theory-breakthroughs-defer-fusion-kstar`).

**Goal**: translate the 4 Korean `.md` files listed below into English, remove their entries from `tool/own1_legacy_allowlist.json`, and land two commits on `origin/main`.

**CJK budget for this batch**: 168558 characters (baseline — expect 0 after translation).

**Two expected commits**:
1. `docs(translate): phase-5-15 phase-5-15-theory-breakthroughs-defer-fusion-kstar (4 files)`
2. `feat(own): shrink own#1 allowlist phase-5-15` (remove 4 entries)

**HARD constraints (violations = stop-and-defer)**:

- **own#1 (doc-english-hard)**: every translated file must reach `CJK count = 0` as measured by `python3 tool/own_doc_lint.py --rule 1`. Re-verify after each file write; if the file regressed to CJK > 0 (sibling-stash-wipeout race), re-write it immediately.
- **own#11 (bt-solution-claim-ban) softener**: Korean `U+C99D U+BA85 ("proof")` / `U+C644 U+C804 ("complete")` / `proven` / `solved` must NOT appear in translated output. Replace with one of: `draft`, `candidate`, `pattern`, `target`, `demonstrating`. Preserve mathematical statements as framings ("a candidate argument demonstrating ...") rather than solution claims.
- **own#17 (README English-only)**: root `README.md` must remain CJK = 0 across this entire batch. Do not touch it.
- **Math/physics preservation — literal**:
  - LaTeX: `$...$`, `$$...$$`, ` ```math ` fences — preserve token-for-token; translate only natural-language surrounding prose.
  - Greek symbols in text and identifiers: σ, Σ, τ, φ, Φ, ψ, Ψ, ω, Ω, λ, Λ, α, β, γ, δ, ε, θ, μ, ν, π, ρ, ζ, η, κ, ξ, χ — preserve exactly (do not transliterate).
  - Equation numbering (`(1)`, `(2)`, `(3.4)`, `(Eq. 5)`), units (`eV`, `MeV`, `GeV`, `K`, `T`, `m·s⁻¹`, `N·m`), and citation refs (`[1]`, `[12]`, `[Author 2024]`) — preserve literally.
  - Chemical formulas and subscripts/superscripts (`H₂O`, `CO₂`, `E=mc²`) — preserve literally.
  - Numerical tables (pipe tables, ASCII tables) — preserve structure; translate only text column contents.
- **Terminology uncertainty = defer**: if any file contains dense physics/mathematics jargon that you cannot translate with high confidence (unknown specialized terms, ambiguous Korean technical compounds, non-standard notation), leave the file's Korean original intact, leave its allowlist entry intact, and document the deferral in your final message. Phase 6 or a later cleanup round will pick up deferred files. Do NOT ship a low-confidence translation.

**Race-completion protocol (MANDATORY, baked in from Phase 2/3/4 observations)**:

1. Write each `.md` translation atomically: write to `<path>.tmp`, `fsync`, then `os.rename(<path>.tmp, <path>)`. Immediately re-read and CJK-verify; if CJK > 0, re-write (max 3 retries) — this defeats the sibling `git stash -u` wipeout race (Phase 3 11.6).
2. Before push: `git fetch origin`, re-`stat` `tool/own1_legacy_allowlist.json`, re-read the JSON, re-apply the removal set as a set-difference against the current on-disk `.allowlist` array (not the pre-edit snapshot). This defeats the allowlist re-introduction race (Phase 3 11.6). Then `git rebase origin/main`.
3. If `git pull --rebase` is needed: first `git stash push -m "phase-5-15-pre-pull" -- <batch paths> tool/own1_legacy_allowlist.json` (narrow stash, NEVER `-u`). After successful rebase + push, `git stash drop stash@{0}` since main supersedes the stashed state.
4. `--no-verify` is explicitly permitted on the two batch commits — pre-commit hooks race against sibling batches' auto-artifact regeneration. Immediately after each commit, run `python3 tool/own_doc_lint.py --rule 1` as a manual gate; exit 0 is required before the second commit and before the push.
5. If `.git/hooks/*.lock` persists after a hook race, `rm -f .git/hooks/*.lock` and retry the commit.
6. One retry allowed on push rejection (fetch + rebase + re-diff + re-push). If still failing, stop and report — do not spin retry loops.

**File list (4 files)**:

- reports/sessions/specs/2026-04-02-kstar-300s-steady-state-design.md  (11872 CJK)
- reports/sessions/specs/2026-04-02-kstar-n6-tokamak-design.md  (15141 CJK)
- reports/sessions/specs/2026-04-02-ultimate-fusion-powerplant-design.md  (15851 CJK)
- theory/breakthroughs/breakthrough-theorems.md  (125694 CJK)

**Shrink target**: remove exactly these 4 entries from `tool/own1_legacy_allowlist.json` `.allowlist` array:

- "reports/sessions/specs/2026-04-02-kstar-300s-steady-state-design.md"
- "reports/sessions/specs/2026-04-02-kstar-n6-tokamak-design.md"
- "reports/sessions/specs/2026-04-02-ultimate-fusion-powerplant-design.md"
- "theory/breakthroughs/breakthrough-theorems.md"

**Commit messages**:

1. First commit (after all translations verified CJK = 0):

   ```
   docs(translate): phase-5-15 phase-5-15-theory-breakthroughs-defer-fusion-kstar (4 files)
   ```

2. Second commit (after allowlist shrink):

   ```
   feat(own): shrink own#1 allowlist phase-5-15
   ```

```

### 7.16 Batch 16: `phase-5-16-theory-constants-flow-predictions-preprints-roadmap-v3` (12 files, 31806 CJK)

```
You are the Phase 5 batch agent for canon, batch **16** (`phase-5-16-theory-constants-flow-predictions-preprints-roadmap-v3`).

**Goal**: translate the 12 Korean `.md` files listed below into English, remove their entries from `tool/own1_legacy_allowlist.json`, and land two commits on `origin/main`.

**CJK budget for this batch**: 31806 characters (baseline — expect 0 after translation).

**Two expected commits**:
1. `docs(translate): phase-5-16 phase-5-16-theory-constants-flow-predictions-preprints-roadmap-v3 (12 files)`
2. `feat(own): shrink own#1 allowlist phase-5-16` (remove 12 entries)

**HARD constraints (violations = stop-and-defer)**:

- **own#1 (doc-english-hard)**: every translated file must reach `CJK count = 0` as measured by `python3 tool/own_doc_lint.py --rule 1`. Re-verify after each file write; if the file regressed to CJK > 0 (sibling-stash-wipeout race), re-write it immediately.
- **own#11 (bt-solution-claim-ban) softener**: Korean `U+C99D U+BA85 ("proof")` / `U+C644 U+C804 ("complete")` / `proven` / `solved` must NOT appear in translated output. Replace with one of: `draft`, `candidate`, `pattern`, `target`, `demonstrating`. Preserve mathematical statements as framings ("a candidate argument demonstrating ...") rather than solution claims.
- **own#17 (README English-only)**: root `README.md` must remain CJK = 0 across this entire batch. Do not touch it.
- **Math/physics preservation — literal**:
  - LaTeX: `$...$`, `$$...$$`, ` ```math ` fences — preserve token-for-token; translate only natural-language surrounding prose.
  - Greek symbols in text and identifiers: σ, Σ, τ, φ, Φ, ψ, Ψ, ω, Ω, λ, Λ, α, β, γ, δ, ε, θ, μ, ν, π, ρ, ζ, η, κ, ξ, χ — preserve exactly (do not transliterate).
  - Equation numbering (`(1)`, `(2)`, `(3.4)`, `(Eq. 5)`), units (`eV`, `MeV`, `GeV`, `K`, `T`, `m·s⁻¹`, `N·m`), and citation refs (`[1]`, `[12]`, `[Author 2024]`) — preserve literally.
  - Chemical formulas and subscripts/superscripts (`H₂O`, `CO₂`, `E=mc²`) — preserve literally.
  - Numerical tables (pipe tables, ASCII tables) — preserve structure; translate only text column contents.
- **Terminology uncertainty = defer**: if any file contains dense physics/mathematics jargon that you cannot translate with high confidence (unknown specialized terms, ambiguous Korean technical compounds, non-standard notation), leave the file's Korean original intact, leave its allowlist entry intact, and document the deferral in your final message. Phase 6 or a later cleanup round will pick up deferred files. Do NOT ship a low-confidence translation.

**Race-completion protocol (MANDATORY, baked in from Phase 2/3/4 observations)**:

1. Write each `.md` translation atomically: write to `<path>.tmp`, `fsync`, then `os.rename(<path>.tmp, <path>)`. Immediately re-read and CJK-verify; if CJK > 0, re-write (max 3 retries) — this defeats the sibling `git stash -u` wipeout race (Phase 3 11.6).
2. Before push: `git fetch origin`, re-`stat` `tool/own1_legacy_allowlist.json`, re-read the JSON, re-apply the removal set as a set-difference against the current on-disk `.allowlist` array (not the pre-edit snapshot). This defeats the allowlist re-introduction race (Phase 3 11.6). Then `git rebase origin/main`.
3. If `git pull --rebase` is needed: first `git stash push -m "phase-5-16-pre-pull" -- <batch paths> tool/own1_legacy_allowlist.json` (narrow stash, NEVER `-u`). After successful rebase + push, `git stash drop stash@{0}` since main supersedes the stashed state.
4. `--no-verify` is explicitly permitted on the two batch commits — pre-commit hooks race against sibling batches' auto-artifact regeneration. Immediately after each commit, run `python3 tool/own_doc_lint.py --rule 1` as a manual gate; exit 0 is required before the second commit and before the push.
5. If `.git/hooks/*.lock` persists after a hook race, `rm -f .git/hooks/*.lock` and retry the commit.
6. One retry allowed on push rejection (fetch + rebase + re-diff + re-push). If still failing, stop and report — do not spin retry loops.

**File list (12 files)**:

- theory/constants/atlas-constants.md  (20722 CJK)
- theory/constants/special-number-contrast.md  (1630 CJK)
- theory/constants/special-number-control-v1.md  (1706 CJK)
- theory/constants/special-number-control.md  (2829 CJK)
- theory/flow/alien-design-flow.md  (896 CJK)
- theory/flow/anima-law-bridges.md  (384 CJK)
- theory/flow/tecs-l-bridge.md  (341 CJK)
- theory/predictions/testable-predictions.md  (1994 CJK)
- theory/preprints/millennium-v3-preprint-draft-2026-04-16.md  (35 CJK)
- theory/roadmap-v3/README.md  (434 CJK)
- theory/roadmap-v3/migration-from-v2.md  (401 CJK)
- theory/roadmap-v3/phase-00-bootstrap.md  (434 CJK)

**Shrink target**: remove exactly these 12 entries from `tool/own1_legacy_allowlist.json` `.allowlist` array:

- "theory/constants/atlas-constants.md"
- "theory/constants/special-number-contrast.md"
- "theory/constants/special-number-control-v1.md"
- "theory/constants/special-number-control.md"
- "theory/flow/alien-design-flow.md"
- "theory/flow/anima-law-bridges.md"
- "theory/flow/tecs-l-bridge.md"
- "theory/predictions/testable-predictions.md"
- "theory/preprints/millennium-v3-preprint-draft-2026-04-16.md"
- "theory/roadmap-v3/README.md"
- "theory/roadmap-v3/migration-from-v2.md"
- "theory/roadmap-v3/phase-00-bootstrap.md"

**Commit messages**:

1. First commit (after all translations verified CJK = 0):

   ```
   docs(translate): phase-5-16 phase-5-16-theory-constants-flow-predictions-preprints-roadmap-v3 (12 files)
   ```

2. Second commit (after allowlist shrink):

   ```
   feat(own): shrink own#1 allowlist phase-5-16
   ```

```

## 8. Race-Completion Appendix

Lessons from Phase 2/3/4 (session log sections 11.5, 11.6, 11.7) inherited by every Phase 5 batch:

### 8.1 Stash-wipeout race (Phase 3 11.6, batches 8 and 10)

A sibling batch running `git stash push -u` snapshots and reverts the entire working tree — including files owned by other batches mid-edit. Victim batches observed their in-progress `.md` edits silently reverted to HEAD (Korean originals re-appearing). Detection: harness `system-reminder` "file state changed externally" messages plus CJK > 0 on files the agent believed it had just translated. Mitigation: atomic tmp-rename plus post-write CJK verify with in-loop re-write; hard ban on `git stash -u` during an active parallel window — narrow `git stash push -- <paths>` only.

### 8.2 Allowlist re-introduction race (Phase 3 11.6, batch 7)

A sibling batch's allowlist shrink was written on top of a pre-shrink snapshot, re-adding the victim batch's already-removed entries to the array. Mitigation: before every push, re-read `tool/own1_legacy_allowlist.json` at its current mtime, re-apply the batch's removal set as a set-difference against the latest on-disk entries (not against any pre-edit in-memory snapshot), then commit and push. Phase 5 extends this to "re-read-and-re-difference unconditionally, not only on merge conflict."

### 8.3 `git_hook_ban_watcher.hexa` lock interference (Phase 4 closure, intermittent)

A local pre-commit hook lock file (`.git/hooks/*.lock` or a watcher artifact) can persist after a hook race and block subsequent commits. Mitigation: `rm -f .git/hooks/*.lock` before retry. The lock is local-only and not version-controlled; removing it is safe.

### 8.4 Pre-commit hook auto-staging races (Phase 2 11.5, Phase 4 11.7)

Sibling batches' meta runs regenerate `reports/*.json` artifacts; the project pre-commit hook tries to auto-stage them, which races against the batch's narrow `git add`. Mitigation: `--no-verify` on the batch commits, then manual `python3 tool/own_doc_lint.py --rule 1` as a post-commit gate (exit 0 required). This is the expected mode for any parallel translation window, not an exception.

### 8.5 External regex/dictionary mass-translate corruption (Phase 4 11.7)

An out-of-band regex-plus-dictionary pipeline against `.md` files corrupted the WT for three fusion/KSTAR specs (broken cross-refs, mangled sigma/tau identifiers, half-rewritten LaTeX). Contained entirely in the WT — never reached a commit. SAFE-REVERT (`git checkout HEAD -- <paths>`) recovered the originals. Rule: **never run an external regex/dictionary mass-translate pipeline against `.md` files during an active parallel window.** Phase 5 B15 handles these three files manually / AST-grounded.

### 8.6 Stash hygiene at phase close (Phase 4 11.7, commit `dc999770`)

At the end of a 14-way window ten residual stashes remained (`phase-4-2` through `phase-4-14` plus pre-pull/pre-rebase auxiliaries). Inspection on 2026-04-25 classified all ten as DROP-SAFE (HEAD fully superseded each stashed state). Phase 5 should follow the same discipline: drop stashes after successful push; at phase close, inspect any residuals before dropping.

## 9. Sequencing Guidance

**Recommended firing pattern**: single parallel salvo of all 16 batches at once, matching the Phase 3 (N=10) and Phase 4 (N=14) pattern. Each batch agent acquires the allowlist race pattern from Section 6 and the defer protocol from the per-batch prompt. Expected landing order is non-deterministic — the allowlist merge serializes the commits on origin/main.

**Risk flags specific to Phase 5**:

- **Highest-difficulty phase overall.** The roadmap marks Phase 5 as "API verification mandatory." Batch agents MUST NOT guess specialized physics/mathematics terminology. When terminology verification is uncertain, invoke rule `f` (defer-don't-ship-degraded): leave the file's Korean original intact, leave its allowlist entry intact, document in the batch's final message. Phase 6 or a final cleanup round will pick up deferred files.
- **B15 is the apex batch.** Four files — `theory/breakthroughs/breakthrough-theorems.md` (125K CJK) plus the three fusion/KSTAR deferred specs. The B15 agent should take extra time, cross-check terminology across multiple references, and may legitimately defer all four if confidence is insufficient. A 4-file defer in B15 is acceptable; a 100-file defer is not.
- **B9 (theory/proofs) and B13/B14 (study-p*)** carry the densest proof-style mathematics across medium-sized files. Expect per-file translation time to exceed the average by 1.5-2x.
- **B6 (papers/n6-hexa-*)** is a 21-file series of hardware/bio integration papers with consistent terminology — the agent should translate the first 2-3 files carefully to establish vocabulary, then reuse it across the remaining 18.

**Deferred set**: maintain a per-batch deferred list in the agent's final message. At Phase 5 close, aggregate all deferrals into a Phase 6 (or final cleanup round) scope. A deferred file remains on the allowlist; its count contributes to the residual 217 target gap.

**Expected end state after Phase 5 (clean closure, zero deferrals)**:

- `tool/own1_legacy_allowlist.json` `.allowlist` reduced 534 -> 217
- 317 `.md` files verified CJK = 0 by `python3 tool/own_doc_lint.py --rule 1` (exit 0)
- 32 commits on `origin/main` (16 translate + 16 shrink)
- session log `reports/sessions/hard-english-only-session-2026-04-24.md` appended with a Phase 5 closure section (sections 11.8 plus verification snapshot update)

**Expected end state after Phase 5 (with deferrals, pessimistic)**:

- `tool/own1_legacy_allowlist.json` `.allowlist` reduced 534 -> 217 + D (D = number of deferred files)
- (317 - D) files verified CJK = 0
- 32 or fewer commits (deferrals skip the second shrink commit for those files)
- Phase 6 scope updated with D deferred paths

## 10. Post-Phase-5 Reconciliation Checklist (template)

Run this checklist exactly once, after the last of the 16 batches has landed on `origin/main` and all sibling batch agents have reported "done or deferred." This is the Phase 5 closure gate. Copy this block into the session log at closure time and fill in the measured values.

### 10.1 CJK audit — 317 file set

Goal: confirm every Phase 5 in-scope file reaches CJK = 0 (or is explicitly on the deferred list).

- [ ] Enumerate the 317 in-scope paths from section 2.1 / 2.2 / 2.3 into a newline-delimited list `/tmp/phase-5-paths.txt`.
- [ ] For each path, measure CJK: `python3 tool/own_doc_lint.py --rule 1 --paths-from /tmp/phase-5-paths.txt` and capture the JSON output.
- [ ] Verify `len(violations) == len(deferred)`. Any file with CJK > 0 that is NOT on the per-batch deferred list is a regression — re-open the owning batch and re-translate.
- [ ] Global lint re-run: `python3 tool/own_doc_lint.py --rule 1` repo-wide, exit 0 required (non-Phase-5 files were already CJK = 0 at the Phase-4-closure snapshot).

### 10.2 Allowlist parity

Goal: confirm the allowlist shrink on disk exactly equals (534 − 317 + D) = 217 + D.

- [ ] Count on-disk: `jq '.allowlist | length' tool/own1_legacy_allowlist.json`. Target = 217 (zero deferrals) or 217 + D.
- [ ] Set-compare: compute set-difference between the Phase-4-closure allowlist snapshot (534 entries) and the current on-disk allowlist. Removed set must equal the 317 in-scope paths minus the D deferred paths.
- [ ] Confirm no NEW entries were silently added by any batch (sibling-race re-introduction regression).
- [ ] Commit hash check: last allowlist-touching commit on `origin/main` must be a `feat(own): shrink own#1 allowlist phase-5-{N}` from one of the 16 batches.

### 10.3 Stash hygiene

Goal: zero residual stashes (matches Phase-4-closure discipline at `dc999770`).

- [ ] `git stash list` — expected empty. If non-empty, inspect each (`git stash show -p stash@{N}`) and classify as DROP-SAFE or REQUIRES-INSPECTION.
- [ ] For each DROP-SAFE (HEAD fully supersedes the stashed state) — drop with `git stash drop stash@{N}`.
- [ ] For each REQUIRES-INSPECTION — stop, document, and resolve before declaring Phase 5 closed.

### 10.4 Session log update

Goal: close Phase 5 in the single running session log file.

- [ ] Append a new section `11.8 Phase 5 closure (2026-04-?? or later)` to `reports/sessions/hard-english-only-session-2026-04-24.md` with:
  - Batch landing order (actual merge order on `origin/main`).
  - Per-batch CJK baseline vs post counts.
  - Deferrals list (path, reason, proposed Phase 6 disposition).
  - Any race events observed (stash-wipeout, allowlist re-introduction, hook lock) with mitigations applied.
  - Final allowlist count (217 + D) and final repo-wide CJK count (should be 0 + deferred-CJK).
- [ ] Update the "Verification snapshot" table at the top of the session log with the new allowlist count and date.
- [ ] Commit: `docs(session): phase-5 closure — <N> deferrals, allowlist 534 -> <final>` (no `--no-verify`; closure commits run clean pre-commit hooks).

### 10.5 CI re-verify

Goal: 9/9 CI green on `origin/main` at the Phase-5-closure tip.

- [ ] Push the session-log closure commit on its own (no batched push).
- [ ] Watch CI: all 9 checks must pass. If any check fails (own#1 doc-english-hard is the expected failure vector), halt and re-audit.
- [ ] Tag the closure commit: `git tag -a phase-5-closure -m "Phase 5 closure: allowlist 534 -> <final>, <N> deferrals" && git push origin phase-5-closure`.

### 10.6 Phase 6 scope handoff (conditional)

Goal: if D > 0, seed Phase 6 scope file with the deferred set.

- [ ] Create / update `proposals/own1-phase-6-scope-<date>.md` with:
  - Deferred paths list (D entries).
  - Per-file deferral reason (terminology confidence gap, notation ambiguity, spec cross-ref).
  - Suggested Phase 6 mitigation (human-in-the-loop review, AST-grounded translation, targeted subject-matter reference).
- [ ] Link the scope file from the roadmap (`proposals/own1-hard-english-only-translation-roadmap-2026-04-24.md`).

---

_End of Phase 5 batch plan._
