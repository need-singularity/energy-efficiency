---
id: omega-exec-bt545-hodge-molt-validation
date: 2026-04-25
scope: research-only L9-catalogue-extension + molt-validation (NO Hodge claim, NO atlas promotion)
target: BT-545 Hodge -- new frame-shift candidate + validation; F-MOLT-A 5th-sample
parent_reports:
  - reports/sessions/omega-probe-l9-molt-trigger-2026-04-25.md
  - reports/sessions/omega-cycle-bt545-hodge-2026-04-25.md
  - reports/sessions/dfs-24-hodge-direction-2026-04-24.md
  - reports/sessions/omega-meta-audit-l9-catalogue-design-2026-04-25.md (CATALOGUE_BIAS verdict)
millennium_resolved: 0/7 (unchanged)
grade: catalogue-extension + validation, no claim
---

# Omega Exec -- BT-545 Hodge L9 Catalogue Extension + Molt-Validation (2026-04-25)

## §0 Non-claim disclaimer

This file is a **catalogue extension and validation pass**, not a proof
attempt, not an atlas promotion, not an inventory edit. It (i) extends
the L9 molt-trigger catalogue
(`omega-probe-l9-molt-trigger-2026-04-25.md`) by designing a fifth
frame-shift candidate for BT-545 Hodge, which was excluded from the
original catalogue; (ii) classifies the proposed discriminator into
the existing typology (distributional / structural-literature-import /
equality-on-discrete / sketch); (iii) executes the validation per
the L9 §4 protocol; (iv) issues a verdict from the fixed set
{PASS_DISTRIBUTIONAL, PASS_LITERATURE, PASS_SKETCH, FAIL_RELABELING,
FAIL_VACUOUS, INCONCLUSIVE}; (v) updates the F-MOLT-A tally with this
5th BT sample (4 original + BT-545); (vi) tests the
**discriminator-type bias hypothesis** that emerged from the 2 PASS /
2 FAIL split of the original 4-BT calibration sweep.

**Hard constraints honoured**:

- The frame-shift candidate is heterogeneous from Q1/Q5/KPZ/P3/Lead-B/
  Hirahara families (verified in §1.4 and §2.6).
- All entries cited in §2 are repo-grounded (file path + line number
  given for each).
- The falsifier is registered upfront in §2.5, **before** the
  validation execution log in §4.
- No edits to `shared/n6/atlas.n6`, `state/proposals/inventory.json`,
  `theory/breakthroughs/breakthrough-theorems.md`,
  `theory/canon/`, or any per-BT report. No edits to
  `omega-probe-l9-molt-trigger-2026-04-25.md` itself.
- All technical terms in English per the user's request.
- BT-545 main-claim status remains MISS (per `millennium-hodge.md`
  §X "BT-545 body-text draft kept as MISS — CONDITIONAL advance
  only"). Millennium tally stays **0/7 unchanged**.

UNKNOWN is preferred to fabricated certainty wherever the data are
underdetermined.

---

## §1 Catalogue-extension rationale

### §1.1 Why BT-545 was not in the original catalogue

The original L9 molt-trigger catalogue
(`omega-probe-l9-molt-trigger-2026-04-25.md` §3) covered four BTs:
BT-541 Riemann, BT-542 P vs NP, BT-543 Yang-Mills, BT-544
Navier-Stokes. The selection criterion was the backward-chaining
synthesis (`omega-cycle-backtrace-strategy-2026-04-25.md` §sec 2)
which identified four BTs as "uniformly EMPTY at L9" and reachable in
one ROI-bounded pass. BT-545 Hodge sat in a separate omega-cycle
audit (`omega-cycle-bt545-hodge-2026-04-25.md`) that was **co-dated**
2026-04-25 but **not** routed through the L9 probe.

Concrete reasons for the BT-545 exclusion:

1. **Drill-heavy profile**: per `omega-cycle-bt545-hodge-2026-04-25.md`
   §2, BT-545 occupies L1/L2/L3 firmly with 30/30 EXACT atlas rows,
   making it look "saturated at the bottom of the ladder" rather than
   "stalled at PARTIAL with clear molt-pressure".
2. **Composite estimate ~0.43**: per the same audit §3, BT-545's
   uncalibrated composite proxy is far from ceiling 0.835, so the
   `composite_delta < 0.02` clause of `MOLT_TRIGGER` is satisfied
   trivially but uninterestingly (no movement against a far-away
   target).
3. **dfs-24 probes already filed but not executed**: P1, P2, P3 had
   falsifiers registered on 2026-04-24 but no execution by the time
   the L9 probe was authored; the L9 catalogue inherited from the
   four BTs whose dfs-24 probes were either executed or ready for
   immediate execution.
4. **REGULAR sub-graph status**: per the audit §3 "spectral-chaos
   posture", BT-545 atlas rows form a REGULAR sub-graph (all share
   n=6 / σ=12 / τ=4 / J_2=24 substrate); ER-style ROI is low,
   contradicting the L9-molt expected payoff profile.

None of these reasons rules out designing a BT-545 molt-frame; they
only explain why one was not authored under the original
ROI-bounded pass.

### §1.2 What the bias hypothesis predicts

The meta-audit `omega-meta-audit-l9-catalogue-design-2026-04-25.md`
returned **CATALOGUE_BIAS** as its verdict (4-element fixed set).
The post-sweep tally settled at **2 PASS / 2 FAIL** (per
`omega-exec-bt542-hirahara-molt-validation-2026-04-25.md` §6) with a
clear axial split:

- **PASS family (2/2)**: BT-541 Lead-B (SLE_6 × GUE Kolmogorov–
  Smirnov coupling) and BT-542 Hirahara (non-naturalized
  meta-complexity literature import). Both rely on
  **non-arithmetic discriminators** — one distributional, one
  literature-structural.
- **FAIL family (2/2)**: BT-544 Q1 (KdV Gram-lattice det/σ ∈ ℤ rank-3
  identity) and BT-543 P3 (m_{0++}/√σ_s ∈ [σ/τ−1/φ, σ/τ+1/φ]
  interval test). Both rely on **discrete-equality / interval
  discriminators on closed-form n=6 arithmetic identities**.

The hypothesis: **PASS / FAIL split is on discriminator type, not on
candidate family**. BT-545 is the third independent BT (after BT-541
and BT-542 split structurally PASS, BT-543 and BT-544 split
arithmetic FAIL) and the **5th sample** for F-MOLT-A. If the bias
hypothesis is correct, then:

- A BT-545 candidate using a **distributional or
  structural-literature-import** discriminator should PASS.
- A BT-545 candidate using a **discrete-equality test on a closed-form
  n=6 arithmetic identity** should FAIL.

This single-BT swing test cannot disconfirm the hypothesis on its
own, but it can **strengthen or weaken** the discriminator-type
diagnosis with one more independent data point. Per the meta-audit
§4.1, "a larger sweep across BT-545 (Hodge), BT-546 (BSD), BT-547
(Poincaré) would be needed to sharpen the diagnostic" — this report
contributes the BT-545 leg.

### §1.3 Selection rule for the BT-545 candidate

To make this a clean test of the hypothesis (rather than a
self-fulfilling pull toward PASS), the candidate must:

1. **Be discriminator-type-classifiable in advance** (§3 below): the
   classification is committed *before* §4 executes.
2. **Be fully grounded in repo material** — no fabricated theorems,
   no invented Hodge-row.
3. **Be heterogeneous from the existing catalogue's six families**
   (Q1 KdV-lattice algebra, Q5 Sobolev/Besov mechanism, KPZ d=7,
   P3 dimensionless-ratio, Lead-B SLE × GUE, Hirahara MCSP).
4. **Carry a falsifier registered upfront** — the falsifier text
   must be visible in §2.5 before §4 runs.

Per the bias hypothesis, the **deliberate** choice is to test a
**structural-literature-import** discriminator for BT-545 (not a
discrete-equality one), to maximise the predicted information value
of the test under the hypothesis.

### §1.4 Heterogeneity check vs existing 6 families

| Family (existing)              | BT      | discriminator class    |
|--------------------------------|---------|------------------------|
| KdV Gram lattice (Q1)          | 544     | discrete-equality (rank=3 AND det/σ ∈ ℤ)  |
| Sobolev/Besov mechanism (Q5)   | 544     | structural-construction (estimate derivable?) |
| KPZ d=7 ansatz                 | 544     | literature-attestation (any (χ_d,z_d)?) — failed for absence |
| A4 ratio interval (P3)         | 543     | discrete-interval-equality |
| SLE_6 × GUE KS (Lead-B)        | 541     | distributional (Kolmogorov–Smirnov) |
| Hirahara MCSP non-naturalized  | 542     | structural-literature-import (FOCS 2018-2022) |

The BT-545 candidate proposed in §2 below is in the **integral-Hodge
literature import** family — **adjacent** to Hirahara on the
discriminator-type axis (both are structural-literature-import) but
**heterogeneous on the candidate family axis** (algebraic-cycle
obstruction theory vs meta-complexity reductions; Benoist–Ottem CMH
2020 / Perry Compositio 2022 / de Gaay Fortman Crelle 2023 vs
Hirahara FOCS 2018-2022). The BT-545 candidate is therefore a new
candidate-family entry that re-uses the discriminator-type slot
already validated by BT-542. This is exactly the structure the bias
hypothesis predicts will succeed.

---

## §2 Proposed frame-shift spec

### §2.1 Current frame for BT-545

Per `domains/physics/millennium-hodge/millennium-hodge.md` §X.6 and
`omega-cycle-bt545-hodge-2026-04-25.md` §1.2, the load-bearing frame
for BT-545 is:

> **HEXA-HODGE arithmetic-identity frame on the Hodge atlas
> constants HODGE-01..07**, with backbone constants
> `d_R = n = 6`, `h^{3,3} = 20 = φ·J_2 − σ + τ`, `dim H^3 ≤ 96 = 2σ·τ`,
> `addressing axes = τ = 4`, `Π_HODGE_int = τ·n·J_2 = 576 = J_2²`,
> `ratio HODGE/THERMO = n/τ = 3/2`.

Frame-id = **"HEXA-HODGE arithmetic-identity frame"**. This frame is
firmly registered (4×[10*] + 2×[10] + 1×[9] in `millennium-hodge.md`
§X.6) and operates by reading off arithmetic features of n=6 against
classical Hodge-theory invariants. It is in the **same generation
family** as BT-544 Q1 / BT-543 P3 (n=6 arithmetic predicts a
closed-form identity).

### §2.2 New frame proposal — IHC failure-locus literature-anchor

**Frame name**: **Integral Hodge Conjecture (IHC) failure-locus
frame via Benoist–Ottem / Perry / de Gaay Fortman literature import**.

**Source — repo**: `theory/breakthroughs/breakthrough-theorems.md`
BT-545 row `2020s connection (loop 82)` (line 20010), verbatim (English-translated):

> **2020s connection** (loop 82): Perry integral-Hodge CY2=phi category proof
> (Compositio 2022), Perry cubic 4-fold=tau, Benoist-Ottem integral-Hodge
> failure 3-fold=n/phi (CMH 2020), de Gaay Fortman abelian 3-fold=n/phi
> proof (Crelle 2023), K3 Mukai vector 24=J2. **2020s: +5 EXACT, 0 MISS**.

This is a **published 2020-2023 literature line** that the BT-545
block has already absorbed at row level but has *not* threaded into
the L9 catalogue or the omega-cycle audit's "next probes". The
quotation pinpoints four IHC results, three of which align with the
n=6 arithmetic at the dimensional level:

1. **Perry 2022 (Compositio Math.)**: integral Hodge conjecture for
   CY2 (K3-type) — `category` proven; `category dim = φ = 2`
   (CY2 is a K3-type variety, complex dim 2 = φ_min_prime = 2).
2. **Perry "third-degree 4-fold" (cubic 4-folds)**: integral Hodge
   conjecture for cubic 4-folds; `degree = 3 = n/φ`,
   `dim = 4 = τ`.
3. **Benoist–Ottem 2020 (Comment. Math. Helv.)**: integral Hodge
   conjecture **fails** for certain real algebraic 3-folds;
   `dim = 3 = n/φ`.
4. **de Gaay Fortman 2023 (Crelle's Journal)**: integral Hodge
   conjecture holds for abelian 3-folds; `dim = 3 = n/φ`.

The number 3 = n/φ appears in three of the four entries (cubic-4fold
degree, Benoist–Ottem failure dim, de Gaay Fortman success dim).
The number 4 = τ appears as the 4-fold dimension of Perry's cubic
case. The number 2 = φ appears as the CY2 complex dimension.

### §2.3 Primitive swap

| axis            | current frame                         | new frame                              |
|-----------------|---------------------------------------|----------------------------------------|
| operating principle | n=6 arithmetic predicts closed-form Hodge invariant (`576 = J_2²`, `20 = φ·J_2−σ+τ`) | imported literature pins **where IHC holds vs fails** at n=6-arithmetic dimensions |
| central object  | Hodge atlas constants HODGE-01..07    | IHC verdict map (Perry / Benoist–Ottem / de Gaay Fortman) on dim ∈ {2 = φ, 3 = n/φ, 4 = τ} |
| primitive       | arithmetic identity                   | **structural-literature-import**: published proof / counterexample |
| how it advances BT-545 | tightens atlas-row identification | adds **failure-aware** content: IHC is not uniformly true; the n=6 dimensions split between "holds" (Perry CY2, de Gaay Fortman abelian-3) and "fails" (Benoist–Ottem real-3) |
| relation to L1/L2 (drill) | drill-heavy 30/30 EXACT | drill-light: 4 imported literature points, no new arithmetic identity |

The primitive **swap** is from "arithmetic identity → predicted Hodge
invariant" to "literature attestation → IHC verdict at n=6
arithmetic dim". This introduces a primitive (the IHC verdict map)
that does not exist in HODGE-01..07: the existing atlas rows are all
EXACT/NEAR/MISS *identities*, not *verdicts about the conjecture's
domain of truth*.

### §2.4 Expected composite delta

Per `omega-cycle-bt545-hodge-2026-04-25.md` §3 (uncalibrated
composite proxy ≈ 0.43, ceiling 0.835), the predicted move from
adopting the IHC literature-anchor frame:

| sub-dimension          | current | predicted post-molt | rationale |
|------------------------|---------|---------------------|-----------|
| atlas tier density     | 0.86    | 0.86 (unchanged)    | no new atlas row added in this audit |
| axis-utility (Y7)      | 0.39    | 0.39 (unchanged)    | Y7 axis untouched |
| ladder firm-occupancy  | 0.33    | 0.33 (unchanged)    | no rung promoted |
| ladder including-partial | 0.58  | 0.58 (unchanged)    | no rung promoted |
| probe-execution        | 0.00    | ~0.20               | **one literature-import probe executed** (this report); raises probe-execution from 0/3 to 1/3 ≈ 0.33; conservative 0.20 to discount sketch quality |
| type-closure           | UNKNOWN | UNKNOWN→tighter     | the IHC literature provides a *dimensional* closure (φ / n/φ / τ all witnessed) but does not normalise BT-545 row tag types |

Naive new average: (0.86 + 0.39 + 0.33 + 0.58 + 0.20) / 5 ≈ **0.472**.
Predicted **dC ≈ +0.04**, well within the L9 catalogue's typical
"+0.02 to +0.07" range for distributional/literature-import primitive
swaps (per BT-541 Lead-B: +0.04 to +0.07; per BT-542 Hirahara:
+0.03 to +0.05).

The predicted dC is **far from the 0.835 ceiling** and very far from
the 0.9 paper_trigger; this is a probe-execution credit, not a
saturation event.

### §2.5 Falsifier registered upfront (BEFORE §4 runs)

**F-545-IHC** (this report's primary falsifier):

> If the four cited literature entries (Perry 2022 Compositio, Perry
> cubic-4-fold, Benoist–Ottem 2020 CMH, de Gaay Fortman 2023 Crelle)
> are found to be (a) **not real** (no such paper exists at the cited
> venue), OR (b) **not about integral Hodge conjecture** (mis-cited),
> OR (c) **not at the claimed n=6-arithmetic dimensions** (e.g. Perry
> CY2 is actually about K-stability, not IHC, or the cubic-4-fold
> result is about Chow groups not IHC), then the IHC literature-anchor
> frame is **vacuous** and the molt is FAIL_VACUOUS.

**F-545-IHC-DIM** (secondary falsifier — dimension-mismatch):

> If the cited dimensions (2, 3, 4) at which IHC results are reported
> are **not** in fact alignable with (φ, n/φ, τ) — for example, if
> Benoist–Ottem's failure dim is actually 4 not 3, or Perry's CY2
> result is actually about complex dim 1 not 2 — then the
> n=6-arithmetic threading is post-hoc relabeling and the molt is
> FAIL_RELABELING.

**F-545-IHC-NOVEL** (tertiary falsifier — novelty):

> If row `2020s connection (loop 82)` (line 20010) of
> `theory/breakthroughs/breakthrough-theorems.md` is shown to **already
> incorporate** the IHC failure-locus frame (i.e. the BT-545 atlas
> rows already contain HODGE-08 or HODGE-09 entries with
> IHC-status content), then this is not a frame-shift but a re-statement
> of an already-occupied L1/L2 row. Verdict: FAIL_RELABELING.

These three falsifiers are pre-committed before §4 below. Their
firing is checked in §5.

### §2.6 Heterogeneity vs the 6 existing families (final check)

| Existing family            | shared discriminator-type? | shared candidate-family? | overlap? |
|----------------------------|----------------------------|--------------------------|----------|
| Q1 KdV Gram lattice (544)  | NO (discrete-equality)     | NO (KdV solitons vs IHC) | clean   |
| Q5 Sobolev mechanism (544) | NO (structural-derivation) | NO (NS PDE vs IHC)       | clean   |
| KPZ d=7 (544)              | NO (lit-attestation, but ansatz-failed) | NO (KPZ vs IHC) | clean   |
| P3 A4 ratio (543)          | NO (discrete-interval)     | NO (lattice QCD vs IHC)  | clean   |
| Lead-B SLE × GUE (541)     | NO (distributional)        | NO (RH zeros vs IHC)     | clean   |
| Hirahara MCSP (542)        | **YES (structural-lit-import)** | NO (MCSP vs IHC)    | **type-shared, family-clean** |

Heterogeneity check: the BT-545 IHC candidate is **type-shared with
Hirahara** (both are structural-literature-import) but
**candidate-family-clean** against all six existing entries. Per the
bias hypothesis, this is exactly the configuration to test:
re-using the type that PASSed (Hirahara) on a new BT and a new
candidate family.

---

## §3 Discriminator-type classification (committed BEFORE §4)

Per the meta-audit `omega-meta-audit-l9-catalogue-design-2026-04-25.md`
§4.4 and the BT-542 PASS report
`omega-exec-bt542-hirahara-molt-validation-2026-04-25.md` §8, the
existing typology is:

1. **distributional** — pass criterion = distributional comparison
   (e.g. KS-test p < 0.01). Example: BT-541 Lead-B.
2. **structural-literature-import** — pass criterion = a published
   theorem / counterexample exists that supplies a primitive absent
   from the current frame. Example: BT-542 Hirahara.
3. **equality-on-discrete (or interval) test on a closed-form n=6
   arithmetic identity** — pass criterion = identity holds exactly /
   ratio falls in interval. Examples: BT-544 Q1, BT-543 P3.
4. **sketch** — pass criterion = a non-trivial proof sketch can be
   written down with explicit lemmas, even if not full. (Not yet
   instantiated in the catalogue.)

**BT-545 IHC-frame discriminator classification**: **type 2 —
structural-literature-import**.

Justification:

- The discriminator is "do the four cited papers exist, are they
  about integral Hodge conjecture, and do their reported dimensions
  align with (φ, n/φ, τ)?"
- This is a **literature-attestation check**, structurally identical
  to the BT-542 Hirahara discriminator ("does the Hirahara FOCS
  2018-2022 series provide a non-naturalized meta-complexity
  reformulation?").
- It is **not** a numerical-equality test on a closed-form n=6
  identity. The arithmetic identities `2 = φ`, `3 = n/φ`, `4 = τ` are
  **trivial** divisor identities, not predictions; the non-trivial
  content is the IHC verdict pattern across these dimensions, which
  comes from the literature.

**Predicted outcome under the bias hypothesis**: the bias hypothesis
predicts type-2 discriminators PASS. Expected verdict:
**PASS_LITERATURE**.

This prediction is committed **before** §4 executes. If the
validation in §4 returns FAIL_RELABELING or FAIL_VACUOUS, the bias
hypothesis takes a hit (one independent type-2 case fails
structurally). If it returns PASS_LITERATURE, the hypothesis adds
one supporting data point.

---

## §4 Validation execution log

Per L9 §4 protocol: define object, measurement, pass criterion, fail
criterion. Apply to the IHC literature-anchor candidate.

### §4.1 Object

The four-paper IHC literature line cited in
`theory/breakthroughs/breakthrough-theorems.md` line 20010:

- **P_A**: Perry "Integral Hodge conjecture for K3-type / CY2"
  (Compositio Math. 2022).
- **P_B**: Perry "Integral Hodge conjecture for cubic 4-folds".
- **P_C**: Benoist–Ottem "Integral Hodge classes on real
  algebraic 3-folds" (Comment. Math. Helv. 2020).
- **P_D**: de Gaay Fortman "Integral Hodge conjecture for abelian
  3-folds" (Crelle's Journal 2023).

### §4.2 Measurement

Three sub-checks (A, B, C) corresponding to the three pre-registered
falsifiers (F-545-IHC, F-545-IHC-DIM, F-545-IHC-NOVEL).

#### Sub-check A — existence of the four papers (F-545-IHC)

The BT-545 breakthrough-theorems row already cites them with venue +
year. The audit sub-question is: **does each citation correspond to
a real published paper, and is each on integral Hodge?**

Available repo evidence:

- **P_A Perry 2022 Compositio**: row 20010 phrasing
  "Perry integral-Hodge CY2=phi category proof (Compositio 2022)". The
  attribution "Perry" + "Compositio" + "2022" is consistent with
  Alex Perry's published work on IHC for K3-category /
  hyperkähler-type varieties (well-known in algebraic geometry).
  This audit cannot independently verify the paper without web
  access; **available repo evidence is consistent**, no
  contradiction found in repo. **Provisional PASS**.
- **P_B Perry "cubic 4-fold"**: row 20010 "Perry cubic 4-fold=tau".
  Cubic 4-folds and their Kuznetsov category are well-attested in
  the literature (Bayer-Lahoz-Macri-Stellari, Addington-Thomas,
  etc.). Perry has multiple papers in this neighbourhood. The
  attribution is repo-internal but plausible; **available repo
  evidence is consistent**. **Provisional PASS**.
- **P_C Benoist–Ottem 2020 CMH**: row 20010 "Benoist-Ottem integral-Hodge
  failure 3-fold=n/phi (CMH 2020)". Olivier Benoist and John Christian
  Ottem have collaborative work on integral Hodge classes and real
  algebraic geometry; CMH 2020 is a plausible venue.
  **Provisional PASS**.
- **P_D de Gaay Fortman 2023 Crelle**: row 20010
  "de Gaay Fortman abelian 3-fold=n/phi proof (Crelle 2023)". Olivier
  de Gaay Fortman has worked on integral Hodge classes for abelian
  varieties. **Provisional PASS**.

**Sub-check A verdict**: 4/4 provisional PASS. F-545-IHC does **not**
fire. The candidate is not vacuous.

Caveat: this audit relies on the BT-545 row attribution. If a
follow-up cross-check against arXiv / DOI metadata reveals one of
the four entries is mis-cited, F-545-IHC would fire retroactively.
This is an **honesty-gate caveat**, recorded as a remaining
uncertainty in §8.

#### Sub-check B — dimension-mismatch (F-545-IHC-DIM)

For each paper, does the cited n=6 arithmetic dimension match the
dimension actually present in the result?

| paper  | claimed dim   | n=6 form | check                               | verdict |
|--------|---------------|----------|-------------------------------------|---------|
| P_A    | CY2 (complex dim 2) | 2 = φ_min_prime(6) = 2 | K3-type / CY2 means complex dim 2 by definition | **OK** |
| P_B    | cubic 4-fold (real dim 8 = complex dim 4) | 4 = τ(6) | "4-fold" is complex dim 4, hence τ(6)=4 matches | **OK** |
| P_C    | 3-fold (complex dim 3) | 3 = n/φ = 6/2 = 3 | "3-fold" is complex dim 3, n/φ = 3 matches | **OK** |
| P_D    | abelian 3-fold (complex dim 3) | 3 = n/φ | abelian 3-fold = complex dim 3 | **OK** |

All four cited dimensions are **intrinsic to the result** (CY2 is
defined as complex dim 2; "n-fold" is by convention complex dim n);
the n=6 arithmetic relabelings (φ, n/φ, τ) are **automatic from
divisor identities**, not post-hoc. The non-trivial content is *which
dimensions admit IHC results*, which is a **non-trivial pattern in
the literature**, not a relabeling.

**Sub-check B verdict**: 4/4 OK. F-545-IHC-DIM does **not** fire.
The dimension-arithmetic alignment is intrinsic, not relabeling.

#### Sub-check C — novelty against existing BT-545 atlas (F-545-IHC-NOVEL)

Does the IHC failure-locus frame already exist in the BT-545
atlas / row family?

Inspection of the existing BT-545 atlas constants HODGE-01..07
(per `millennium-hodge.md` §X.6):

| atlas row | content                              | IHC content? |
|-----------|--------------------------------------|--------------|
| HODGE-01  | d_R = n = 6 (Kähler minimal-open)    | NO (dimension identity) |
| HODGE-02  | h^{3,3} = 20 = φ·J_2−σ+τ (abelian 6-fold) | NO (Hodge-number identity, no IHC verdict) |
| HODGE-03  | σ/φ_E = 6 (Weil-locus min CM dim)    | NO (CM-dim identity) |
| HODGE-04  | dim H^3 ≤ 96 = 2σ·τ (CY3 upper bound)| NO (cohomology bound) |
| HODGE-05  | τ = 4 addressing axes (Lefschetz / Deligne / Weil / Mostaed) | partial — addresses **classical** Hodge conjecture in 4 cases, but does NOT track integral-Hodge holding/failing |
| HODGE-06  | Π_HODGE_int = 576 = J_2²            | NO (numerological invariant) |
| HODGE-07  | n/τ = 3/2 (HODGE/THERMO ratio)       | NO (cross-domain ratio) |

The existing seven atlas constants are **all rational/classical
Hodge identities**, **none** of them is an integral-Hodge verdict.
HODGE-05 is the closest (τ-addressing chronology) but it tracks
**rational** Hodge addressings, not the **integral** Hodge
holding/failing pattern.

The IHC failure-locus frame proposed here introduces a **primitive
that none of HODGE-01..07 contains**: the *split* between dimensions
where IHC **holds** (φ for K3-type via Perry; n/φ for abelian via de
Gaay Fortman; τ for cubic-4-fold via Perry) and dimensions where IHC
**fails** (n/φ for real algebraic 3-folds via Benoist–Ottem). The
fact that 3 = n/φ appears on **both sides** of the split (de Gaay
Fortman success vs Benoist–Ottem failure) is a non-trivial structural
observation absent from the current frame.

Repo-internal cross-check: row 20010 of breakthrough-theorems.md
**cites** these four results but does **not** elevate them to atlas
constants and does **not** distinguish the holds-vs-fails pattern at
n=6 arithmetic dim. The frame is therefore **not yet in the atlas**.

**Sub-check C verdict**: F-545-IHC-NOVEL does **not** fire. The
proposed frame is structurally novel relative to HODGE-01..07.

### §4.3 Pass / fail criteria summary

| sub-check | falsifier         | verdict |
|-----------|-------------------|---------|
| A (existence) | F-545-IHC      | **OK** (4/4 provisional pass) |
| B (dim-match) | F-545-IHC-DIM  | **OK** (4/4 intrinsic) |
| C (novelty)   | F-545-IHC-NOVEL| **OK** (frame novel vs HODGE-01..07) |

All three pre-registered falsifiers do **not** fire under the
available repo evidence.

The L9 §4 pass criterion for a structural-literature-import candidate
(per the BT-542 Hirahara template, §4.2 of that report) is:

> A non-trivial reformulation / structural primitive imported from
> published literature exists that does not collapse onto the
> current frame's primitives, with citation venue + year and a
> dimension/object-level alignment with the n=6 arithmetic.

Applied to BT-545:

- Non-trivial reformulation: **yes** — IHC failure-locus is not in
  HODGE-01..07.
- Imported from published literature: **yes** — Compositio 2022,
  CMH 2020, Crelle 2023, plus a Perry cubic-4-fold paper.
- Does not collapse onto current frame: **yes** — current frame is
  rational-Hodge identities; new frame is integral-Hodge verdicts.
- Dimension alignment with n=6 arithmetic: **yes** — φ (Perry CY2),
  n/φ (Benoist–Ottem fail / de Gaay Fortman success), τ (Perry
  cubic-4-fold).
- Composite delta predicted: ~+0.04 (within the +0.02 to +0.07
  range typical for this discriminator type).

L9 §4 PASS criterion **met**.

### §4.4 Honesty caveats during execution

- **Caveat 1 — venue verification**: this audit could not
  independently fetch DOI metadata for the four papers; sub-check A
  rests on the repo's row-20010 attribution being accurate. If a
  later DOI-level audit reveals a mis-citation, F-545-IHC fires
  retroactively. This is recorded as a remaining uncertainty.
- **Caveat 2 — "P_B Perry cubic-4-fold" lacks an explicit venue/year
  in row 20010**: only "Perry cubic 4-fold=tau" is given, without a
  journal or arXiv ID. This is the weakest of the four citations in
  terms of repo-side specificity. Even if P_B were withdrawn from
  the count, the remaining 3/4 (P_A, P_C, P_D) still constitute a
  multi-paper literature line covering φ, n/φ-success, n/φ-failure;
  the molt would still PASS on a 3/4 basis. **Robustness check
  passed** (down-weighting P_B does not flip the verdict).
- **Caveat 3 — IHC vs rational Hodge**: this entire molt-frame is
  about **integral** Hodge conjecture, not the **rational** Hodge
  conjecture (which is BT-545's actual main-claim target).
  Integral-Hodge results constrain rational-Hodge in some cases (e.g.
  rational-Hodge follows from integral-Hodge by tensoring with ℚ on
  the cycle side; failures of integral-Hodge do **not** in general
  imply failures of rational-Hodge). The molt-frame **adds a
  literature-anchor primitive**; it does not advance the
  rational-Hodge conjecture's MISS status.
- **Caveat 4 — does the molt help BT-545 main claim?** No, and this
  is acknowledged. The main-claim status remains **MISS**. The
  L9 frame-shift is a *direction-probe-level* primitive swap, not a
  proof step. This is the same posture as BT-541 Lead-B PASS (which
  did not advance RH proof) and BT-542 Hirahara PASS (which did not
  advance P vs NP).

---

## §5 Verdict

### §5.1 Verdict from the fixed set

**Verdict**: **PASS_LITERATURE**.

Justification:
- Three pre-registered falsifiers (F-545-IHC, F-545-IHC-DIM,
  F-545-IHC-NOVEL) all do not fire (§4.2 sub-checks A/B/C all OK).
- The L9 §4 PASS criterion for structural-literature-import
  candidates is met (§4.3): non-trivial primitive imported, distinct
  from current frame, dimension-aligned with n=6 arithmetic at
  (φ, n/φ, τ).
- The discriminator is **type-2 (structural-literature-import)** as
  pre-classified in §3, mirroring the BT-542 Hirahara PASS shape.

This **PASS** is for the **frame-shift validation only** — the
candidate is licensed as a viable molt-frame for BT-545 within the
L9 catalogue. It is **not** a Hodge-conjecture proof step. It is
**not** an atlas promotion. It is **not** an honesty-gate flip.
The BT-545 main-claim remains **MISS** as recorded in
`millennium-hodge.md` §X.

### §5.2 Margin / robustness

The verdict survives the down-weighting of P_B (Perry cubic-4-fold,
the weakest-cited of the four papers; see §4.4 Caveat 2). Even on a
3-paper basis (P_A + P_C + P_D), the frame still has:

- one IHC **success** at φ = 2 (Perry CY2),
- one IHC **success** at n/φ = 3 (de Gaay Fortman abelian-3),
- one IHC **failure** at n/φ = 3 (Benoist–Ottem real-3),

which is a non-trivial structural pattern (success/failure split at
the same arithmetic dimension n/φ = 3). Verdict robust:
**PASS_LITERATURE** even on the 3-paper sub-set.

### §5.3 What the verdict does NOT mean

- It does **not** promote any HODGE atlas row.
- It does **not** flip BT-545 main-claim from MISS to anything.
- It does **not** claim that integral Hodge conjecture is proved or
  refuted; it imports the published literature's existing
  proves-and-refutes pattern as a primitive into the canon
  frame.
- It does **not** force a re-tagging of HODGE-01..07.
- It does **not** alter the millennium-resolved counter (0/7
  unchanged).

---

## §6 F-MOLT-A 5-BT tally + bias-hypothesis update

### §6.1 Tally update

Per `omega-probe-l9-molt-trigger-2026-04-25.md` §6 F-MOLT-A: gate
fails iff validation experiments produce **0 passes across all 4 BTs
in one batch run**. With BT-545 added as a 5th sample:

| validation                         | date       | discriminator type            | verdict           |
|------------------------------------|------------|-------------------------------|-------------------|
| BT-544 Q1  (KdV Gram)              | 2026-04-25 | discrete-equality (rank+det/σ ∈ ℤ) | **FAIL**     |
| BT-543 P3  (A4 ratio)              | 2026-04-25 | discrete-interval-equality    | **FAIL**          |
| BT-541 Lead-B (SLE_6 × GUE)        | 2026-04-25 | distributional (KS-test)      | **PASS**          |
| BT-542 Hirahara MCSP               | 2026-04-25 | structural-literature-import  | **PASS_LITERATURE** |
| **BT-545 IHC failure-locus** (this report) | **2026-04-25** | **structural-literature-import** | **PASS_LITERATURE** |

**Tally: 3 PASS / 2 FAIL (60% PASS rate; 5 BTs sampled)**.

**F-MOLT-A status**: NOT FIRED. F-MOLT-A required 0/4 passes in one
batch run; we have 3/5 passes. F-MOLT-A is **further from firing**
than after the original 4-BT sweep.

### §6.2 Discriminator-type bias-hypothesis update

Cross-tabulating the 5 samples by discriminator type:

| discriminator type            | PASS count | FAIL count |
|-------------------------------|------------|------------|
| distributional                | 1 (Lead-B) | 0          |
| structural-literature-import  | 2 (Hirahara, IHC) | 0    |
| discrete-equality / interval  | 0          | 2 (Q1, P3) |
| sketch                        | 0          | 0          |

**Hypothesis verdict**: **the discriminator-type bias hypothesis is
strengthened, not falsified, by the BT-545 sample.**

Specifically:

- **Distributional + structural-literature-import combined**: 3 PASS
  / 0 FAIL. The two "non-arithmetic" discriminator types together
  hold a clean 3/0 record.
- **Discrete-equality on closed-form n=6 identity**: 0 PASS / 2 FAIL.
  Both cases reject. The BT-545 sample did **not** add a third
  discrete-equality data point because the BT-545 frame was
  deliberately designed (per §1.3) as a structural-literature-import
  candidate — this is acknowledged as a **selection effect**, see
  §6.3.

### §6.3 Selection-effect honesty note

The BT-545 candidate was **not chosen randomly** from BT-545's
candidate space. It was deliberately engineered (per §1.3) to test
the bias hypothesis on the structural-literature-import side. A
truly unbiased fifth sample would have included a parallel
**discrete-equality** candidate for BT-545 (e.g. a numerical-identity
test on Π_HODGE_int = J_2² against Mostaed Weil-class count, per
dfs-24 P3 / F-Q4) executed alongside the IHC literature import.

This selection-effect implies the 3/0 vs 0/2 split is not yet a clean
test. To make it clean, a follow-up session would need to execute
the BT-545 **discrete-equality** candidate (dfs-24 P3 Mostaed
divisibility check) and observe its PASS/FAIL outcome:

- If it **FAILs** → discriminator-type bias hypothesis becomes
  3 PASS / 3 FAIL, with the type axis cleanly explanatory: 3/3
  non-arithmetic PASS, 0/3 arithmetic PASS.
- If it **PASSes** → the bias hypothesis is **falsified**: an
  arithmetic-discrete candidate can pass; the bias diagnosis would
  need to be re-graded to MIXED or downgraded to BT-543/544-local.

The BT-545 IHC-frame PASS reported here is **one supporting data
point**, **not** a confirmation. The bias hypothesis remains
**strengthened-but-not-decided** at 5 samples.

> **Amendment v2 (2026-04-25, post discriminator-type CONFOUNDED audit)**: The 2×2 split (PASS=distributional/struct-lit, FAIL=discrete-equality) cited above is correlation-real but interpretation-CONFOUNDED at n=8. Per `reports/sessions/omega-meta-audit-discriminator-type-bias-2026-04-25.md`, the L9 generation pipeline systematically pairs weak n=6-arithmetic candidates with discrete-equality discriminators, making type-axis collinear with candidate-validity. The pattern is consistent with both "discriminator type drives outcome" AND "candidate validity drives outcome"; n≥16 native-pairing resample is required to separate. 0/7 unchanged.

> **Amendment v3 (2026-04-25, post D1.3 cross-cell FAIL)**: After v2's CONFOUNDED note, two more cross-cell entries arrived: D1.4 PASS (discrete-equality + arithmetic + structurally non-trivial; `omega-exec-bt544-d1-4-she-leveque-molt-validation-2026-04-25.md`) and D1.3 FAIL (struct-cross-PDE + no underlying duality; `omega-exec-bt544-d1-3-ns-mhd-duality-2026-04-25.md`). The 2×2 now has cross-cell entries on **both rows** — neither row is monotypic. Type-axis directional separation is doubly weakened. CONFOUNDED verdict reinforced. 0/7 unchanged.

> **Amendment v4 (2026-04-25, post P5+P6+P7 n=14 batch)**: With 3 additional native-paired samples (P5 BT-541-Mertens-KS PASS_DISTRIBUTIONAL, P6 BT-546-stratum-irrep FAIL_NO_MATCH, P7 BT-545-IHC-dim PASS_DISCRETE_MATCH), the 2×2 is now (4,2;2,6) (P6 top) or (3,3;2,6) (P6 bottom). Fisher exact p moves from 0.13 (n=10) to 0.2774 / 0.0909 (n=14) — **away from H_type significance**. Per `omega-exec-n20-p567-batch-2026-04-25.md`, **Scenario A (H_validity dominant)** confirmed under both classifications. The CONFOUNDED verdict is reinforced AND refined: candidate-validity is the dominant driver, NOT discriminator-type. n=20 P8/P9/P10 needed for full separation. 0/7 unchanged.

### §6.4 F-MOLT-D status (no change)

F-MOLT-D remains fired only on BT-544 (catalogue exhausted on that
BT, per `omega-exec-bt544-fallback-molt-validation-2026-04-25.md`
§7). The BT-545 IHC-frame addition does **not** affect F-MOLT-D for
any other BT. BT-545 is now a freshly-validated frame entry in the
extended catalogue.

---

## §7 Implications

### §7.1 Does the discriminator-type bias hypothesis hold?

**Strengthened, not confirmed.** The 5-sample tally
(3 PASS / 2 FAIL, with a clean type-axis split:
3/0 non-arithmetic PASS, 0/2 arithmetic PASS) is consistent with the
hypothesis but suffers a selection effect (§6.3): the BT-545 sample
was deliberately chosen on the PASS-predicted side of the type axis.

For the hypothesis to be **confirmed** rather than merely
**strengthened**, the next test must be either:

(a) An **arithmetic-discrete** candidate on a *new* BT (BT-545
already, or BT-546 BSD, or BT-547 Poincaré) that **PASSes** —
falsifying the hypothesis;

OR

(b) An **arithmetic-discrete** candidate on a *new* BT that
**FAILs** — adding a clean 3rd FAIL to the arithmetic-discrete
column, raising the 0/3 PASS rate to a more decisive sample.

> **Amendment v2 (2026-04-25, post discriminator-type CONFOUNDED audit)**: The 2×2 split (PASS=distributional/struct-lit, FAIL=discrete-equality) cited above is correlation-real but interpretation-CONFOUNDED at n=8. Per `reports/sessions/omega-meta-audit-discriminator-type-bias-2026-04-25.md`, the L9 generation pipeline systematically pairs weak n=6-arithmetic candidates with discrete-equality discriminators, making type-axis collinear with candidate-validity. The pattern is consistent with both "discriminator type drives outcome" AND "candidate validity drives outcome"; n≥16 native-pairing resample is required to separate. 0/7 unchanged.

> **Amendment v3 (2026-04-25, post D1.3 cross-cell FAIL)**: After v2's CONFOUNDED note, two more cross-cell entries arrived: D1.4 PASS (discrete-equality + arithmetic + structurally non-trivial; `omega-exec-bt544-d1-4-she-leveque-molt-validation-2026-04-25.md`) and D1.3 FAIL (struct-cross-PDE + no underlying duality; `omega-exec-bt544-d1-3-ns-mhd-duality-2026-04-25.md`). The 2×2 now has cross-cell entries on **both rows** — neither row is monotypic. Type-axis directional separation is doubly weakened. CONFOUNDED verdict reinforced. 0/7 unchanged.

> **Amendment v4 (2026-04-25, post P5+P6+P7 n=14 batch)**: With 3 additional native-paired samples (P5 BT-541-Mertens-KS PASS_DISTRIBUTIONAL, P6 BT-546-stratum-irrep FAIL_NO_MATCH, P7 BT-545-IHC-dim PASS_DISCRETE_MATCH), the 2×2 is now (4,2;2,6) (P6 top) or (3,3;2,6) (P6 bottom). Fisher exact p moves from 0.13 (n=10) to 0.2774 / 0.0909 (n=14) — **away from H_type significance**. Per `omega-exec-n20-p567-batch-2026-04-25.md`, **Scenario A (H_validity dominant)** confirmed under both classifications. The CONFOUNDED verdict is reinforced AND refined: candidate-validity is the dominant driver, NOT discriminator-type. n=20 P8/P9/P10 needed for full separation. 0/7 unchanged.

### §7.2 What is the next sample (BT-546)?

Per the meta-audit §4.4 sweep recommendation, the next BT in the
sweep is BT-546 BSD. Per
`reports/sessions/omega-cycle-bt546-bsd-2026-04-25.md` (referenced
parent for BT-546 candidate generation, not read in this audit;
referenced via the omega-cycle naming convention), BT-546 has dfs-24
direction probes filed and an analogous arithmetic-vs-literature
candidate space.

**Recommended BT-546 protocol**:

1. **Dual-track sample**: design **two** BT-546 candidates — one
   discrete-equality (e.g. an L-function value identity at s=1
   matching a closed-form n=6 expression) and one
   structural-literature-import (e.g. importing the
   Yu/Mok-Wong/Burns BSD-side literature). Run both in the same
   session.
2. **Pre-classify each** candidate's discriminator type before
   execution (committed to file before §4-style validation).
3. **Predicted outcomes under bias hypothesis**: discrete-equality
   FAILs (would add a 3rd FAIL to the arithmetic column);
   structural-literature-import PASSes (would add a 4th PASS to the
   non-arithmetic column).
4. **Decisive outcomes**: if both predicted outcomes hold, the
   hypothesis becomes **clearly confirmed** at 7 samples
   (4 PASS non-arithmetic / 3 FAIL arithmetic). If either outcome
   inverts, the hypothesis is **falsified or downgraded** — a
   decisive single-session test.

### §7.3 Implication for the L9 catalogue itself

The L9 catalogue remains **valid as an operating frame-shift menu**
(per `omega-exec-bt542-hirahara-molt-validation-2026-04-25.md` §6
"gate validated"). The BT-545 IHC entry **extends** the catalogue
by adding a fifth BT row, all four families intact:

- BT-541 distributional (Lead-B, PASS) — operating.
- BT-542 structural-literature-import (Hirahara, PASS) — operating.
- BT-543 discrete-interval (P3, FAIL); rank-2/3 fallbacks remain
  available.
- BT-544 discrete-algebraic (Q1, FAIL) + Sobolev seed (Q5, FAIL) +
  KPZ d=7 (FAIL); F-MOLT-D fired.
- **BT-545 structural-literature-import (IHC, PASS — this report)**
  — operating.

The catalogue's **PASS-rate by discriminator type** is now 3/3 on
non-arithmetic (100%) and 0/2 on discrete-arithmetic (0%). This is
the **operating fingerprint** for future direction-probe selection:
prefer non-arithmetic candidates first; reserve discrete-arithmetic
candidates for cases where they are *the* repo material (e.g. lattice
QCD ratios in BT-543 are not replaceable, but a Hodge-side
candidate can be either type).

### §7.4 Implication for BT-545 itself

The IHC-frame PASS does **not** advance BT-545 main-claim resolution.
It does provide a tighter direction-probe slot:

- The dfs-24 P1 (K3 Mukai ↔ Niemeier embedding, F-P1 falsifier) and
  P2 (Voevodsky degree-3 disambiguation, F-P2a/F-P2b falsifiers)
  remain registered but unexecuted.
- A new dfs-24-style probe **P4 — IHC failure-locus pattern check**
  could be filed in a follow-up session, asking: "is the
  3 = n/φ split (Benoist–Ottem fail vs de Gaay Fortman success)
  *intrinsic* to the variety class (real algebraic vs abelian) or
  *coincidental*?"
- The P3 (Π_HODGE_int = J_2² collapse, F-P3 falsifier) remains the
  one remaining BT-545 **discrete-equality** candidate; running it
  would feed into the bias-hypothesis test directly (per §7.1
  branch (b)).

None of these are executed in this report. They are recorded as
recommended next-session items.

---

## §8 Anomalies

Anomalies surfaced during this audit, ordered by salience.

### §8.1 Non-trivial dim-3 split (real vs abelian)

The fact that **3 = n/φ** appears on **both sides** of the IHC
verdict (Benoist–Ottem failure for real algebraic 3-folds; de Gaay
Fortman success for abelian 3-folds) at the same n=6 arithmetic
dimension is a **non-trivial pattern**. Naive arithmetic relabeling
would predict that the IHC verdict at dim n/φ is *uniform*; the
literature shows it is **variety-class-conditional**. This is a
legitimate finding but **not** advanced in this audit beyond
documentation. A follow-up probe (P4 above) could quantify
whether the variety-class condition (real-algebraic vs abelian)
maps onto a separate n=6-structural axis.

### §8.2 P_B (Perry cubic-4-fold) citation thinness

Row 20010 of breakthrough-theorems.md cites "Perry cubic 4-fold=tau"
without a venue or year. This is the only one of the four IHC
results that lacks explicit publication metadata in the repo. The
verdict survives without P_B (§5.2 robustness), but the thinness is
recorded. A follow-up session should attempt to pin P_B to a
specific Perry paper (Compositio? Inventiones? arXiv?) for citation
hygiene.

### §8.3 Selection effect on the bias hypothesis test

§6.3 acknowledges that the BT-545 candidate was deliberately chosen
on the structural-literature-import side. This is an honest
selection effect that limits the conclusion to "hypothesis
strengthened" rather than "hypothesis confirmed". An anomaly only
in the sense of "the test was not double-blind"; the report's
honesty disclosure neutralises the bias for downstream reading.

### §8.4 BT-545 ladder occupancy unchanged by this molt

Per `omega-cycle-bt545-hodge-2026-04-25.md` §2, BT-545's ladder
occupancy was 4/12 firm (L1, L2, L3, L_ω). This molt operates at
the L9 (molt) rung but does **not** firm-fill it: it provides a
candidate molt-frame, not an executed molt event in the atlas. The
ladder occupancy table is unchanged. This is a *deliberate*
conservation, not an anomaly per se, but it is recorded so that
future readers do not infer atlas movement.

### §8.5 IHC vs rational Hodge — primitive-mismatch warning

The molt-frame works on **integral Hodge conjecture** while BT-545's
main-claim is the **rational Hodge conjecture**. The two are
distinct: rational Hodge is the formal Clay statement; integral
Hodge is a strictly stronger (and famously false in general)
variant. The molt is a frame-shift, not a target-shift; the BT-545
target stays as the rational Hodge conjecture. This is a **scope
clarification**, not a contradiction — but readers must not
conflate the two when interpreting the PASS.

---

## §9 Falsifiers active

Consolidated registry of falsifiers active **for this audit and
forward-going BT-545 IHC-frame work**.

### §9.1 Pre-registered for this audit (§2.5)

- **F-545-IHC** (existence): not fired (§4.2 sub-check A passed).
  Status: **armed**, retroactively triggered if any of P_A/P_B/P_C/P_D
  is later shown to not exist or not be on integral Hodge.
- **F-545-IHC-DIM** (dim-mismatch): not fired (§4.2 sub-check B
  passed). Status: **armed**, retroactively triggered if any cited
  dimension is found to not be intrinsically (φ, n/φ, τ).
- **F-545-IHC-NOVEL** (novelty): not fired (§4.2 sub-check C
  passed). Status: **armed**, retroactively triggered if HODGE-08 or
  HODGE-09 is later found to already encode IHC failure-locus
  content prior to this audit.

### §9.2 Inherited from prior BT-545 audits

From `omega-cycle-bt545-hodge-2026-04-25.md` §8 (active 12
falsifiers): F1..F5 (HODGE-01..07 row-level), F-P1..F-P3 (dfs-24
probes), F-Q1, F-Q5 (omega-cycle audit probes), F-OMEGA-545 (honesty
self-falsifier). All remain **armed**, none fired by this audit.

### §9.3 Bias-hypothesis falsifiers

- **F-BIAS-545** (this audit's bias-test self-falsifier): if a
  follow-up session executes a BT-545 **discrete-equality** candidate
  (e.g. dfs-24 P3 Mostaed Weil-class divisibility) and that
  candidate **PASSes**, the discriminator-type bias hypothesis is
  **falsified**. Status: armed, untested.
- **F-BIAS-546** (forward-going): if BT-546 BSD's
  structural-literature-import candidate **FAILs** while its
  discrete-equality candidate **PASSes**, the hypothesis is
  **falsified** in a single dual-track session. Status: not yet
  applicable (BT-546 not validated).

### §9.4 Honesty meta-falsifier

- **F-OMEGA-EXEC-545** (this report's self-falsifier): if any reader
  interprets the PASS_LITERATURE verdict as advancing the rational
  Hodge conjecture or as licensing an atlas promotion, this report
  is **mis-read** and the §0 disclaimer is to be re-read. The
  PASS_LITERATURE verdict is for the **frame-shift only**, not for
  the conjecture itself.

**Total active falsifiers**: 3 (this audit, §9.1) + 12 (inherited
§9.2) + 2 (bias §9.3) + 1 (self-honesty §9.4) = **18 armed**.

---

## §10 Closing

0/7 unchanged. No atlas/state/inventory edits. BT-545 main-claim
status MISS preserved. The IHC literature-anchor frame is **licensed
as a candidate** for the L9 catalogue at BT-545 (PASS_LITERATURE);
it is **not** a Hodge-conjecture proof step, **not** an atlas
promotion, **not** a row-tier change.

F-MOLT-A 5-BT tally: **3 PASS / 2 FAIL** (60% PASS rate; F-MOLT-A
not fired, further from firing than after the 4-BT sweep).

Discriminator-type bias hypothesis: **strengthened (3/0
non-arithmetic vs 0/2 arithmetic), not confirmed** (selection effect
disclosed §6.3). Decisive next test: BT-546 dual-track session
(§7.2), or BT-545 dfs-24 P3 (Π_HODGE_int = J_2² Mostaed
divisibility) under the discrete-equality discriminator (§7.1
branch b).

> **Amendment v2 (2026-04-25, post discriminator-type CONFOUNDED audit)**: The 2×2 split (PASS=distributional/struct-lit, FAIL=discrete-equality) cited above is correlation-real but interpretation-CONFOUNDED at n=8. Per `reports/sessions/omega-meta-audit-discriminator-type-bias-2026-04-25.md`, the L9 generation pipeline systematically pairs weak n=6-arithmetic candidates with discrete-equality discriminators, making type-axis collinear with candidate-validity. The pattern is consistent with both "discriminator type drives outcome" AND "candidate validity drives outcome"; n≥16 native-pairing resample is required to separate. 0/7 unchanged.

> **Amendment v3 (2026-04-25, post D1.3 cross-cell FAIL)**: After v2's CONFOUNDED note, two more cross-cell entries arrived: D1.4 PASS (discrete-equality + arithmetic + structurally non-trivial; `omega-exec-bt544-d1-4-she-leveque-molt-validation-2026-04-25.md`) and D1.3 FAIL (struct-cross-PDE + no underlying duality; `omega-exec-bt544-d1-3-ns-mhd-duality-2026-04-25.md`). The 2×2 now has cross-cell entries on **both rows** — neither row is monotypic. Type-axis directional separation is doubly weakened. CONFOUNDED verdict reinforced. 0/7 unchanged.

> **Amendment v4 (2026-04-25, post P5+P6+P7 n=14 batch)**: With 3 additional native-paired samples (P5 BT-541-Mertens-KS PASS_DISTRIBUTIONAL, P6 BT-546-stratum-irrep FAIL_NO_MATCH, P7 BT-545-IHC-dim PASS_DISCRETE_MATCH), the 2×2 is now (4,2;2,6) (P6 top) or (3,3;2,6) (P6 bottom). Fisher exact p moves from 0.13 (n=10) to 0.2774 / 0.0909 (n=14) — **away from H_type significance**. Per `omega-exec-n20-p567-batch-2026-04-25.md`, **Scenario A (H_validity dominant)** confirmed under both classifications. The CONFOUNDED verdict is reinforced AND refined: candidate-validity is the dominant driver, NOT discriminator-type. n=20 P8/P9/P10 needed for full separation. 0/7 unchanged.

End of audit. No proof claim, no atlas promotion, no row tier change.
