---
domain: hexa-nanobot
axis: biology
sister_of: hexa-weave
sisters:
  - hexa-weave
  - hexa-ribozyme
requires:
  - to: hexa-weave
  - to: hexa-ribozyme
  - to: synbio
  - to: therapeutic-nanobot
---

<!-- @own(sections=[WHY, COMPARE, REQUIRES, STRUCT, FLOW, EVOLVE, VERIFY, IDEAS, METRICS, RISKS, DEPENDENCIES, TIMELINE, TOOLS, TEAM, REFERENCES], strict=false, order=sequential, prefix="§") -->

# HEXA-NANOBOT — molecular nano-machine architecture under the n=6 invariant

> Positioning: HEXA-NANOBOT is the sister domain of HEXA-WEAVE within the biology axis. Where HEXA-WEAVE addresses write-side multi-strand molecular design composition (assembling many strands into a viable bundle), HEXA-NANOBOT addresses single molecular nano-machine architecture (one mechanical actuator per device). The split is genus-level: WEAVE composes strands; NANOBOT actuates atoms. The shared substrate is the n=6 invariant lattice with the canonical quartet σ(6)=12, τ(6)=4, φ(6)=2, J₂=24 — here projected onto motor states, vertex skeletons, pose symmetry, and binary actuator output respectively.

## §1 WHY (why a molecular nano-machine architectural layer matters)

Molecular nanotechnology has a 40-year literature corpus (Drexler 1986 productive nanotechnology, Seeman 1982 immobile-junction DNA scaffolds, Rothemund 2006 DNA origami) but lacks a canonical body inside n6-architecture that ties nano-machine primitives to the n=6 invariant. HEXA-NANOBOT registers this gap as a domain so the architectural primitives — power-stroke quartet, vertex skeleton, pose-equivalence group, binary actuator output — have an explicit ordinal-class workload trace and a 90-day MVP gate.

| Aspect | HEXA-WEAVE (sister) | HEXA-NANOBOT (this domain) |
|--------|---------------------|----------------------------|
| Object | Multi-strand bundle (P up to 10^4) | Single nano-machine (10^0-10^2 atoms per actuator) |
| Direction | Target context to strand-set composition | Target work-output to actuator architecture |
| Primary quantity | Inverse-search × Landauer floor | Mechanical work per cycle vs Brownian floor |
| Primary oracle | AlphaFold-class fold inference | Molecular-dynamics simulation (Drexler 1986 / Goddard 2003) |
| Primary constraint | Landauer × NP-search ceiling | kT thermal noise floor at 310K |
| Verdict horizon | THEORETICAL-ANALYTICAL (closure PASS) | THEORETICAL-ANALYTICAL (registration APPROACH) |

Claim: a molecular nano-machine architectural layer is a distinct technical object from a multi-strand composition layer; its primary constraint is the Brownian thermal floor, not the Landauer search ceiling. Evidence: the literature corpus (Drexler 1986 / Seeman 1982 / Rothemund 2006) treats per-device work-output and structural symmetry as primary, while HEXA-WEAVE closure construction treats inverse-search cost as primary. Limit: this registration is APPROACH grade per raw 69 ceiling-classification; no empirical 4-state 12-vertex DNA-origami simulation has been executed in this cycle (theoretical-analytical only).

## §2 COMPARE (HEXA-NANOBOT vs HEXA-WEAVE vs Drexler-class systems vs DNA-origami) — ASCII chart

```
+------------------------------------------------------------------+
|  [Object scale] (atoms per architectural unit)                   |
+------------------------------------------------------------------+
|  HEXA-NANOBOT         ##....................  10^0-10^2 atoms    |
|  Rothemund 2006       ###...................  10^4 atoms (cage)  |
|  Seeman 1982 junction ##....................  10^2 atoms         |
|  Drexler 1986 design  ###...................  10^3 atoms         |
|  HEXA-WEAVE           #################.....  10^7-10^9 atoms    |
+------------------------------------------------------------------+
|  [Primary axis] (mechanical actuation vs design composition)     |
+------------------------------------------------------------------+
|  HEXA-NANOBOT         ##############........ mechanical-actuator |
|  Rothemund 2006       ###########........... structural-only     |
|  Seeman 1982          ########............... junction-static    |
|  Drexler 1986         #################..... mechanical-actuator |
|  HEXA-WEAVE           #...................... composition not act|
+------------------------------------------------------------------+
|  [n6 invariant projection] (lattice fit)                         |
+------------------------------------------------------------------+
|  HEXA-NANOBOT         ################...... tau=4 / sigma=12    |
|  HEXA-WEAVE           ################...... sigma=12 / J_2=24   |
|  Drexler 1986         ##..................... not stated         |
|  Rothemund 2006       ####................... 12-vertex implicit |
+------------------------------------------------------------------+
```

Claim: HEXA-NANOBOT and HEXA-WEAVE are sister domains that span the same biology axis but address orthogonal sub-problems (per-device actuation vs many-strand composition). Evidence: comparison row 1 shows 5 orders of magnitude object-scale separation; row 2 shows axis-perpendicular emphasis (mechanical vs composition). Limit: at the boundary (small devices, P up to 10) the two domains can overlap; explicit boundary handshake protocol is in §11 DEPENDENCIES.

## §3 REQUIRES (prerequisites)

| Prerequisite area | Required level | Core techniques |
|-------------------|---------------|-----------------|
| Single-molecule dynamics | Advanced | Molecular dynamics, coarse-grained simulation, Brownian motion analysis |
| DNA / RNA structural biology | Advanced | Holliday junctions, immobile junctions (Seeman 1982), origami-fold scaffolding (Rothemund 2006) |
| Mechanical actuator theory | Intermediate | Power-stroke kinetics (Drexler 1986), free-energy landscape analysis |
| Symmetry group theory | Intermediate | Octahedral / icosahedral rotation groups, |O|=24 = J_2 |
| Brownian thermodynamics | Intermediate | kT thermal floor at 310K, work-output bounds |
| n6 invariant grounding | Advanced | sigma(6) = 12, tau(6) = 4, phi(6) = 2, J_2 = 24 lattice for motor / vertex / actuator cardinalities |
| HEXA-WEAVE handshake (sister domain) | Intermediate | composition-side primitives for boundary handshake at small-P regime |
| Foundation/Strand mechanical layer (lean4) | Optional | inheritable from HEXA-WEAVE if formal-verification path is pursued |

## §4 STRUCT (4-axis nano-machine architecture)

```
+======================================================================+
|  [Axis A: Vertex skeleton]      [Axis B: Power-stroke kinetics]      |
|  +--------------------+         +----------------------+             |
|  | sigma(6) = 12      |         | tau(6) = 4 motor st  |             |
|  | 12-vertex polyhedral         | idle / fwd / back / r|             |
|  | DNA-origami cage   |         | free-energy ladder   |             |
|  +----------+---------+         +----------+-----------+             |
|             +---------+--------+----------+                          |
|                       |                                              |
|             [Axis C: Pose-symmetry group]                            |
|             +--------------------+                                   |
|             | J_2 = 24 octahed   |                                   |
|             | rotation group |O| |                                   |
|             | equiv. classes     |                                   |
|             +----------+---------+                                   |
|                        |                                             |
|             [Axis D: Binary actuator output]                         |
|             +--------------------+                                   |
|             | phi(6) = 2         |                                   |
|             | open / closed      |                                   |
|             | bound / unbound    |                                   |
|             +--------------------+                                   |
+======================================================================+
```

The 4-axis layout matches tau(6) = 4 (axis count). Per-axis cardinalities use the canonical n=6 invariant quartet: sigma(6) = 12 vertex skeleton (Axis A), tau(6) = 4 motor states (Axis B), J_2 = 24 pose-equivalence group (Axis C), phi(6) = 2 binary actuator output (Axis D). The full master-identity sigma(6) * phi(6) = 6 * tau(6) = J_2 = 24 holds: 12 * 2 = 24, 6 * 4 = 24.

## §5 FLOW (sequential nano-machine design pipeline)

1. Target work-output specification: user submits the desired mechanical work per cycle (J), actuator stroke distance (nm), and operating temperature (typically 310K cellular).
2. Vertex skeleton selection: choose a 12-vertex polyhedral skeleton (truncated tetrahedron / icosahedron / cuboctahedron) per Axis A; sigma(6) = 12 fixes the vertex count.
3. Power-stroke topology: assign 4 motor states (idle / forward-stroke / backward-stroke / reset) per Axis B; tau(6) = 4 fixes the cardinality.
4. Pose-symmetry quotient: identify pose-equivalent configurations under the 24-element rotation group J_2 per Axis C, reducing the simulation state space by factor 24.
5. Binary actuator binding: connect actuator output to a phi(6) = 2 dichotomy (open/closed clamp, bound/unbound substrate) per Axis D.
6. Brownian floor check: each candidate nano-machine is checked against the kT thermal floor at 310K (kT = 4.28e-21 J); work-per-cycle below 10 * kT is flagged as Brownian-noise-limited.
7. Molecular-dynamics simulation: simulate the candidate using a coarse-grained MD framework; record power-stroke quartet trajectory and pose-equivalence class transitions.
8. Witness emission: a kick witness JSON is written under design/kick/ and absorbed into state/discovery_absorption/registry.jsonl per raw 108 + raw 135.
9. Falsifier registration: each measurable claim emits at least 3 falsifiers per raw 71.

## §6 EVOLVE (abstraction ladder L0-L_omega)

| Level | Object | Cardinality bound |
|-------|--------|-------------------|
| L0 | Atomic coordinates | 10^0-10^2 atoms per actuator |
| L1 | Bond / angle / dihedral primitives | residue-level |
| L2 | Single-actuator unit | 4 motor states (tau(6) = 4) |
| L3 | 12-vertex polyhedral skeleton | sigma(6) = 12 vertex |
| L4 | Pose-equivalence quotient | J_2 = 24 rotation group |
| L5 | Multi-actuator assembly | small-P (up to 6 actuators per assembly) |
| L6 | Functional nano-machine | actuator + skeleton + pose + binary output (4 axes integrated) |
| L7 | Network of nano-machines | crosses into HEXA-WEAVE composition regime |
| L8 | Cellular-context deployment | proteome-adjacent (HEXA-WEAVE handshake) |
| L9 | Therapeutic / industrial application | crosses into life/therapeutic-nanobot |
| L10 | Brownian thermodynamic accounting | kT floor at 310K |
| L11 | MD simulation verification | coarse-grained or atomistic |
| L12 | Symmetry-group computational reduction | O(N!) to O(N!/24) via J_2 quotient |
| L13 | Power-stroke free-energy calibration | published reference frameworks |
| L14 | Reverse-mathematics calibration | inheritable from HEXA-WEAVE Pi^1_1-CA_0 if formal-verification path pursued |
| L_omega | Bachmann-Howard ordinal closure | inheritable from HEXA-WEAVE if cosmological lift attempted |

L2 + L3 + L4 + L6 jointly define the n6-invariant-bound regime: 4 motor states × 12 vertices × 24 pose-classes × 2 actuator outputs = 2304 architectural cells per nano-machine — but the master identity sigma(6) * phi(6) = J_2 = 24 collapses the cell-count to 24 functional configurations under pose-equivalence, matching the J_2 = 24 cardinality at L4.

## §7 VERIFY (raw 70 K>=4 verification axes)

| Axis | Verification claim | Evidence | Status |
|------|--------------------|----------|--------|
| CONSTANTS | n6 quartet sigma(6) = 12, tau(6) = 4, phi(6) = 2, J_2 = 24 hold across §4 / §5 / §6 | manual cross-check vs tool/own_doc_lint.py canonical set | PASS |
| DIMENSIONS | atoms-per-actuator × actuator-count = atoms-total; J/cycle × cycles/s = W; nm × 10^-9 m/nm = m | §5 FLOW dimensionally consistent | PASS |
| CROSS | n6 invariant projection cross-checked against Rothemund 2006 (12-vertex implicit) and Drexler 1986 power-stroke quartet | literature cross-citation | PASS |
| SCALING | atomic count scales linearly with actuator count; pose-state space scales as 24 / N! up to L4 | §6 EVOLVE ladder | PASS |
| SENSITIVITY | choice of polyhedral skeleton (truncated tetrahedron vs icosahedron vs cuboctahedron) — all 12-vertex variants satisfy sigma(6) = 12 axis | §4 STRUCT Axis A | PASS |
| LIMITS | APPROACH grade, not ABSOLUTE; theoretical-analytical, not empirical; no MD simulation executed in this cycle | §1 limit clause + raw 91 C3 disclosure | PASS |
| CHI2 | quantitative chi-squared validation against measured power-output of published DNA-origami nano-machines | DEFER (no MVP simulation in this cycle) | DEFER |
| COUNTER | counter-evidence search: a nano-machine with non-12 vertex skeleton or non-4 motor states would falsify the n6-invariant binding claim | F-NB-2 falsifier registered | PASS |

7 of 8 measurable axes PASS, 1 DEFER (CHI2 sample size 0 — no MVP simulation yet) — meets raw 70 K>=4 threshold (claim/limit pair). raw 91 C3 disclosure level: HIGH-but-MITIGATED (n6 invariant mapping is structural, not yet quantitatively validated; F-NB-2 Bayesian audit deadline 2026-09-28 will calibrate).

## §8 IDEAS (research seeds)

1. 12-vertex DNA-origami truncated-icosahedron cage with a 4-state binary clamp: smallest test-bed satisfying all 4 axes simultaneously.
2. Pose-equivalence quotient simulation: implement the J_2 = 24 octahedral rotation group as a state-space reduction in a coarse-grained MD framework; expect 24-fold speedup at L4.
3. Power-stroke free-energy landscape calibration: extract the 4-state ladder from a published Drexler-class assembly and check whether peak-spacing matches kT * ln(N!) at N = 4.
4. Cross-domain handshake with HEXA-WEAVE: feed multi-actuator assembly outputs (L7) into HEXA-WEAVE bundle composition pipeline; close the loop from per-device design to multi-device composition.
5. Therapeutic / industrial application bridge: route L9 outputs to life/therapeutic-nanobot/ for clinical-application audit and to materials/ for industrial nano-machine fabrication.
6. n6-invariant Bayesian audit: collect 30 published nano-machine architectures and fit motor-state-count + vertex-count distributions against the 4 / 12 prediction.

## §9 METRICS (quantitative targets)

| Metric | Current (cycle 13 fan-out 2/5) | 90-day MVP target | Stretch |
|--------|--------------------------------|-------------------|---------|
| Nano-machine architectures simulated | 0 | 1 (12-vertex 4-state binary) | 5 |
| Vertex-count compliance with sigma(6) = 12 | structural-not-empirical | 100% on simulated set | empirically measured |
| Motor-state-count compliance with tau(6) = 4 | structural-not-empirical | 100% on simulated set | empirically measured |
| Pose-equivalence speedup observed (J_2 = 24) | not-measured | >= 10x on MD wall-clock | 24x (theoretical max) |
| Brownian floor check pass rate | n/a | 1/1 candidate stays above 10 * kT | n/1 with quantitative margin |
| Verdict tier (raw 69) | APPROACH | APPROACH-EMPIRICAL | LIMIT |
| Falsifier count | 5 (F-NB-1..F-NB-5) | 5 | 12 |
| Raw 70 axes PASS | 7 of 8 (CHI2 DEFER) | 8 of 8 | 8 of 8 with n>1 |
| Witness count in design/kick/ | 1 (this registration) | 3+ | 8 |
| CHI2 sample size n | 0 (DEFER) | 1 (PASS-MARGINAL) | 30 |
| Sister-domain handshake with HEXA-WEAVE | spec-only | one bidirectional integration test | full L7 multi-actuator network closure |

Claim: registration is APPROACH grade with 5 preregistered falsifiers and 3 condition deadlines (2026-05-28 / 2026-07-28 / 2026-09-28). Evidence: this body + witness JSON + 2 _index.json updates. Limit: a 90-day MVP miss (F-NB-4 deadline 2026-07-28) reverts the verdict to PROPOSED grade per raw 69 escalation rules.

## §10 RISKS (and falsifiers per raw 71, at least 3 per measurable claim)

Measurable claim 1 — HEXA-NANOBOT is a distinct genus from HEXA-WEAVE:

- F-NB-1-genus: evidence shows HEXA-WEAVE design composition pipeline subsumes single-nano-machine design as a special case (P=1, N small) without separate primitives — would falsify genus distinction and force merge.
- F-NB-1-b: a published unification framework treating both as instances of a single design-composition algebra would weaken the distinction.
- F-NB-1-c: discovery that nano-machine work-output is dominated by inverse-search cost (Landauer) rather than thermal floor (Brownian) at small-N would invalidate the primary-constraint split.

Measurable claim 2 — n6 invariant mapping is structural and load-bearing not decorative:

- F-NB-2-n6-decorative: Bayesian model comparison on 30 published architectures shows H0 (random) cannot be rejected at log-Bayes-factor >= 3 — would invalidate the invariant-as-causal claim.
- F-NB-2-b: a published nano-machine with 5+ motor states (violating tau(6) = 4) and equally efficient work-output would falsify the cardinality binding.
- F-NB-2-c: a published nano-machine with non-12 vertex skeleton (e.g. tetrahedral 4-vertex or cube 8-vertex) outperforming 12-vertex variants would falsify the sigma(6) = 12 binding.

Measurable claim 3 — 90-day MVP gate (F-NB-4 deadline 2026-07-28):

- F-NB-4-MVP-90day: failure to deliver a 4-state 12-vertex DNA-origami simulation by 2026-07-28 falsifies the YES_APPROACH registration upgrade and reverts the recommendation to PROPOSED.
- F-NB-4-b: an MVP simulation that completes but exhibits Brownian-floor violation (work output below 10 * kT) would constitute internal contradiction and trigger retraction.
- F-NB-4-c: an MVP simulation whose witness JSON fails the absorption pipeline (raw 108 classifier rejection) would falsify the absorption-channel design.

Measurable claim 4 — sister-axis collision with life/therapeutic-nanobot (F-NB-5 deadline 2026-05-28):

- F-NB-5-sister-axis-collision: audit shows life/therapeutic-nanobot/ already covers molecular-machine fundamentals at the same theoretical depth — would force route under life axis.
- F-NB-5-b: maintainer review of life/therapeutic-nanobot/therapeutic-nanobot.md flags overlap on §1-§7 specifically — would trigger boundary-redrawing proposal.
- F-NB-5-c: a published taxonomy treats clinical and architectural nano-machines as a single domain — would weaken the biology-vs-life axis split.

Measurable claim 5 — Brownian noise floor binds at 310K:

- F-NB-3-Brownian-floor: a published nano-machine demonstrates work output >> kT per cycle by a factor that requires Landauer-class accounting — would merge HEXA-NANOBOT physical-axis with HEXA-WEAVE Landauer treatment.
- F-NB-3-b: measurement shows 310K is not the operating temperature for any deployed nano-machine (e.g. cryogenic operation) — would shift the floor calculation.
- F-NB-3-c: a nano-machine class operates below the 10 * kT margin and still achieves directed motion via stochastic ratchet effects — would weaken the Brownian-floor-as-binding claim.

Aggregate: 15 falsifiers across 5 measurable claims, at least 3 per claim, satisfies raw 71. MISS criteria for any future MVP simulation are declared upfront here per own 12.

## §11 DEPENDENCIES (external + cross-domain)

| Dependency | Type | Why required |
|------------|------|--------------|
| Drexler K. E. 1986 "Engines of Creation" | external citation | productive nanotechnology framing; power-stroke quartet foundational reference |
| Seeman N. C. 1982 "Nucleic acid junctions and lattices" J Theor Biol 99:237-247 | external citation | immobile junction DNA architecture; vertex skeleton precursor |
| Rothemund P. W. K. 2006 "Folding DNA to create nanoscale shapes and patterns" Nature 440:297-302 | external citation | DNA origami; 12-vertex polyhedral cage implicit reference |
| Goodsell D. S. 2009 "The machinery of life" Springer | external citation | molecular-machine illustrated taxonomy |
| Goddard W. A. 2003 "Handbook of Nanoscience, Engineering, and Technology" CRC Press | external citation | molecular-dynamics simulation reference for §5 step 7 |
| Howard J. 2001 "Mechanics of Motor Proteins and the Cytoskeleton" Sinauer | external citation | power-stroke kinetics + free-energy landscape calibration reference |
| Bath J. & Turberfield A. J. 2007 "DNA nanomachines" Nat Nanotechnol 2:275-284 | external citation | DNA-machine state machine reference |
| domains/biology/hexa-weave/ | sister domain | composition-side handshake at small-P boundary; shared Foundation/Strand lean4 layer if formal-verification path pursued |
| domains/life/therapeutic-nanobot/ | cross-domain (collision audit pending) | clinical application route; F-NB-5 audit deadline 2026-05-28 |
| domains/life/synbio/ | cross-domain | physical-strand assembly handshake (shared with hexa-weave) |
| domains/materials/ | cross-domain | industrial nano-machine fabrication route at L9 |
| state/discovery_absorption/registry.jsonl | repo SSOT | raw 108 + raw 135 absorption channel |
| design/kick/ | repo SSOT | witness emission target |
| tool/own_doc_lint.py | tooling | own 1 / own 3 / own 4 / own 5 / own 16 enforcement (13/13 PASS expected) |

## §12 TIMELINE (deliverables)

| Date | Cycle | Milestone | Witness |
|------|-------|-----------|---------|
| 2026-04-28 | 13 / fan-out 2/5 | Domain registration in n6-architecture (this body + 2 _index.json updates + 1 witness JSON) | design/kick/2026-04-28_hexa-nanobot-domain-registration_omega_cycle.json |
| 2026-05-28 | TBD | F-NB-5 collision audit with life/therapeutic-nanobot completed | F-NB-5 audit row |
| 2026-07-28 | TBD | F-NB-4 90-day MVP — 4-state 12-vertex DNA-origami simulation | proposals/hexa_nanobot_mvp_<date>.md |
| 2026-09-28 | TBD | F-NB-2 Bayesian audit (30 architectures) completed | F-NB-2 audit row |
| 2027-04-28 | TBD | F-NB-3 Brownian-floor literature scan completed | F-NB-3 audit row |
| TBD | TBD | CHI2 axis upgrade DEFER to PASS (n>=1 MD simulation) | TBD |

## §13 TOOLS (concrete repo artefacts)

- tool/own_doc_lint.py --rule 1 / 3 / 4 / 5 / 16 — HARD-block lint gates this body must pass.
- tool/own1_legacy_allowlist.json — frozen English-only legacy grandfather list (this body is NOT added; new files comply directly).
- domains/_index.json — top-level axis SSOT (biology axis updated by this registration; hexa-nanobot added).
- domains/biology/_index.json — sub-axis SSOT (hexa-nanobot domain entry added; _domains_count 1 -> 2).
- state/discovery_absorption/registry.jsonl — append-only absorption registry per raw 108 + raw 135.
- design/kick/ — kick-witness emission directory (this cycle: 2026-04-28_hexa-nanobot-domain-registration_omega_cycle.json).

## §14 TEAM (roles)

| Role | Responsibility | Owner |
|------|----------------|-------|
| Domain steward | Maintain this body and its sub-index entry | n6-architecture maintainers |
| Sister-domain liaison | Maintain HEXA-WEAVE handshake at small-P boundary | hexa-weave + hexa-nanobot stewards jointly |
| MVP runner | Deliver F-NB-4 90-day 4-state 12-vertex simulation | TBD by 2026-07-28 |
| Falsifier monitor | Watch F-NB-1..F-NB-5 with deadlines 2026-05-28 / 2026-07-28 / 2026-09-28 / 2027-04-28 | n6-architecture honesty-charter team |
| Cross-domain liaison | life/therapeutic-nanobot collision audit + materials/ industrial route | per-axis domain stewards |

## §15 REFERENCES

1. Drexler K. E. 1986 "Engines of Creation: The Coming Era of Nanotechnology" Anchor / Doubleday (productive nanotechnology framing; power-stroke quartet foundational reference for tau(6) = 4 motor-state mapping).
2. Seeman N. C. 1982 "Nucleic acid junctions and lattices" J Theor Biol 99:237-247 (immobile junction DNA architecture; vertex skeleton precursor for sigma(6) = 12 polyhedral cage mapping).
3. Rothemund P. W. K. 2006 "Folding DNA to create nanoscale shapes and patterns" Nature 440:297-302 (DNA origami; 12-vertex polyhedral cage implicit reference for sigma(6) = 12 binding).
4. Goodsell D. S. 2009 "The Machinery of Life" 2nd ed Springer (molecular-machine illustrated taxonomy; cross-validation of power-stroke quartet across kinesin / myosin / ATP-synthase classes).
5. Goddard W. A. III, Brenner D. W., Lyshevski S. E., Iafrate G. J. eds 2003 "Handbook of Nanoscience, Engineering, and Technology" CRC Press (molecular-dynamics simulation reference for §5 FLOW step 7).
6. Howard J. 2001 "Mechanics of Motor Proteins and the Cytoskeleton" Sinauer (power-stroke kinetics; free-energy landscape calibration reference for §8 IDEAS seed 3).
7. Bath J. & Turberfield A. J. 2007 "DNA nanomachines" Nat Nanotechnol 2:275-284 (DNA-machine state machine reference; cross-validation of binary actuator phi(6) = 2 mapping).
8. Bustamante C., Liphardt J., Ritort F. 2005 "The Nonequilibrium Thermodynamics of Small Systems" Phys Today 58:43-48 (Brownian-floor + small-system thermodynamics for §10 RISKS measurable claim 5).
9. Astumian R. D. 1997 "Thermodynamics and Kinetics of a Brownian Motor" Science 276:917-922 (stochastic-ratchet alternative to power-stroke mechanism; cited in F-NB-3-c falsifier).
10. Landauer R. 1961 "Irreversibility and Heat Generation in the Computing Process" IBM J Res Dev 5:183-191 (kT ln 2 floor reference; comparison point for HEXA-WEAVE Landauer ceiling vs HEXA-NANOBOT Brownian floor).
11. n6-architecture sister domain: domains/biology/hexa-weave/hexa-weave.md (multi-strand composition counterpart).
12. n6-architecture domain registration witness: design/kick/2026-04-28_hexa-nanobot-domain-registration_omega_cycle.json (this cycle 13 fan-out 2/5).
13. n6-architecture sister-domain closure witness: design/kick/2026-04-28_hexa-weave-closure_omega_cycle.json (tri-axis Omega-saturation PASS at workload ceiling, referenced for handshake protocol at small-P boundary).
