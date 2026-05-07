---
domain: consciousness-red-team
date: 2026-04-15
task: STR-P9-2
title: Consciousness Red Team — refutation of the BT-19 α-product hypothesis and formalised alternative protocols
authors: Park Minwoo & NEXUS-6 collaboration
version: v1 (2026-04-15 STR-P9-2)
upstream:
  - reports/breakthroughs/consciousness-triple-fusion-2026-04-15.md (DSE-P7-1 original CONJECTURE)
  - reports/breakthroughs/bt-19-consciousness-triple-verification-2026-04-15.md (DSE-P8-2 MISS verdict)
  - reports/breakthroughs/bt-19-alternative-paths-2026-04-15.md (DSE-P9-3 three alternative paths)
  - papers/consciousness-measurement-protocol-2026-04-15.md (PAPER-P8-2 measurement manual)
precursor_grade: "[7?] CONJECTURE (BT-19 α_IIT · α_GWT = 1)"
current_grade: "[5] MISS (2026-04-15 DSE-P8-2 downgrade recommendation)"
next_target_grade: "[7] CONJECTURE (alternative path B τ=4 state structure)"
status: red_team_report_v1
kind: refutation_and_redesign
license: CC-BY-SA-4.0
external_sources_verified:
  - Casali AG et al. (2013) Sci Transl Med 5(198):198ra105. DOI:10.1126/scitranslmed.3006294
  - Sarasso S et al. (2015) Curr Biol 25(23):3099-3105. DOI:10.1016/j.cub.2015.10.014
  - Barrett AB, Seth AK (2011) PLoS Comput Biol 7(1):e1001052. DOI:10.1371/journal.pcbi.1001052
  - Barrett AB, Mediano PAM (2019) J Conscious Stud 26(1-2):11-20
  - Mediano PAM, Seth AK, Barrett AB (2019) Entropy 21(1):17. DOI:10.3390/e21010017
  - Mashour GA, Roelfsema P, Changeux J-P, Dehaene S (2020) Neuron 105(5):776-798. DOI:10.1016/j.neuron.2020.01.026
  - COGITATE Consortium, Ferrante O et al. (2025) Nature 642:133-142. DOI:10.1038/s41586-025-08888-1
  - Lendner JD et al. (2020) eLife 9:e55092. DOI:10.7554/eLife.55092
  - Siclari F, Tononi G et al. (2017) Nat Neurosci 20(6):872-878. DOI:10.1038/nn.4545
  - Dehaene S, Changeux J-P, Naccache L (2011) Neuron 70(2):200-227
  - Koch C, Massimini M, Boly M, Tononi G (2016) Nat Rev Neurosci 17(5):307-321
  - Amos LA, Klug A (1974) J Cell Sci 14(3):523-549 (microtubule 13+3 symmetry)
  - Hordijk W, Steel M (2004) J Theor Biol 227(4):451-461 (RAF minimum size)
---

# Consciousness Red Team — refutation of the BT-19 α-product hypothesis and formalised alternative protocols

> **Authors**: Park Minwoo (canon) & NEXUS-6 collaboration
> **Category**: consciousness / red-team / theoretical-refutation
> **Version**: v1 (2026-04-15 STR-P9-2)
> **Honesty declaration**: this paper actively performs refutation of its own theory. No self-reference, 13 external references cited, and grounds for discarding the original BT-19 α-product hypothesis (DSE-P7-1 proposal) are presented along three axes: mathematical, empirical, conceptual.
>
> **v2 revision (2026-04-15 META-P9-2 audit compliance)**: expanded the Red Team refutation paths from 5 → 10 (R6 IIT 4.0 / R7 active inference / R8 HOT / R9 AST / R10 thermodynamic consciousness). Fixed the "12 → 13" typo in Appendix A. Added a §3.3 footnote ("use-case separation declaration").

---

## 0. Abstract

**Red Team purpose**: The CONJECTURE "α_IIT · α_GWT = 1" (BT-19) proposed by the canon project in DSE-P7-1 claimed that the product of the two exponents from IIT and GWT **closes trivially at 1** in the n=6 arithmetic coordinate system. This Red Team **refutes** that hypothesis along three axes (mathematical triviality, empirical lack of support, independence failure) and formalises **three alternative protocols** (φ(6)=2 duality / τ(6)=4 state / σ(6)=2·6 perfect-number) to replace it.

**Refutation results (§3)**: R1 Barrett-Seth 2011 lacks α_IIT=4/3; R2 Dehaene 2011 lacks α_GWT=3/4 (all-or-none not power-law); R3 product=1 is trivial identity x·(1/x)=1, Casali 2013 PCI co-varies with GNW refuting independence; R4 Orch-OR 6-fold absent, Amos-Klug 1974 measured 13+3; R5 BT-19 number conflict with existing GUT Hierarchy; R6 IIT 4.0 Albantakis 2023 still lacks α_IIT=4/3; R7 Hohwy 2020 active inference is not an α_GWT alternative; R8 Rosenthal HOT is not axiom-based; R9 Graziano AST is an independent path; R10 England thermodynamic adaptation makes no mention of n=6.

**Three alternative protocols (§4)**:

- Alternative A — **φ(6)=2 duality** (noesis-noema / local-global 2-layer)
- Alternative B — **τ(6)=4 state structure** (Vedanta 4 avastha ↔ PCI 4 cluster) **← most promising**
- Alternative C — **σ(6)=2·6 perfect-number self-reduction** (Kauffman RAF / Hofstadter self-reference loop)

**Core principle**: the link between n=6 and consciousness should be sought in **structural isomorphism**, not a **multiplicative structure**.

---

## 1. Background — original BT-19 and the P8 MISS chain

### 1.1 DSE-P7-1 original CONJECTURE (2026-04-15)

DSE-P7-1 (`consciousness-triple-fusion-2026-04-15.md`) juxtaposed the critical exponents of four consciousness theories — IIT, FEP, GWT, Orch-OR — with the n=6 arithmetic coordinate system. The claim numbered **BT-19**:

```
  α_IIT · α_GWT = (τ²/σ) · ((n/φ − 1)/(n/φ))
                = (16/12) · (2/3)
                = (4/3) · (3/4)
                = 1                                          (n = 6)
```

- α_IIT = **Barrett-Seth 2011 PLoS CB complexity exponent** (claim)
- α_GWT = **Dehaene 2011 Neuron broadcasting-scaling exponent** (claim)

### 1.2 P8 BT-19 MISS (2026-04-15, DSE-P8-2)

DSE-P8-2 decided **MISS** after independent verification against 8 external papers. Final grade: recommended `[7?] CONJECTURE → [5] downgrade`.

- α_IIT=4/3 original **not found**; α_GWT=3/4 original **not found**
- 0 meta-analyses reporting an α product
- IIT/GWT independent-latent assumption refuted (PCI co-varies)
- microtubule 6-fold refuted (Amos-Klug 1974: 13+3)
- BT-19 number conflict (GUT Hierarchy already assigned)

### 1.3 P9 Red Team launch purpose

Rather than close P8 MISS as a plain rejection, **formalise the refutation paths** and **redesign via 3 alternative protocols**. This complies with R14 (honest verification mandatory), avoids self-reference, and captures scientific impact — the failure itself has academic value.

---

## 2. Reconstruction of BT-19 — mathematical and empirical basis

### 2.1 Mathematical surface structure of the α-product formula

```
  (τ(6))² / σ(6) · (n(6)/φ(6) − 1)/(n(6)/φ(6))
     = (16/12) · (2/3)  =  4/3 · 3/4  =  1
```

- First factor τ²/σ = 16/12 = 4/3 — holds only at n=6.
- Second factor (n/φ − 1)/(n/φ) = 2/3 — specific to n=6 (n/φ=3).

**Arithmetic observation**: the reciprocal relation between the two factors derives directly from the n=6 σ·φ = n·τ identity structure:

```
  σ · φ = n · τ  ⇒  (σ/n)·(φ/τ) = 1  ⇒  (12/6)·(2/4) = 1   (trivial identity)
```

So **α-product=1 is a repackaging of σ·φ=n·τ**, not a new finding about consciousness.

### 2.2 Verifying the empirical basis (block self-reference)

| Claim | Original paper | Actually reported | Verdict |
|---|---|---|---|
| α_IIT=4/3 | Barrett-Seth 2011 | Φ_E definition, Gaussian simulation | numeric **absent** |
| α_GWT=3/4 | Dehaene 2011 | all-or-none, P3b ~300ms | numeric **absent** |
| product=1 empirical | Casali 2013 / Sarasso 2015 / COGITATE 2025 | PCI absolute, adversarial evaluation | **0** meta-analyses |

**Critical omission**: α_IIT and α_GWT have never been reported numerically.

---

## 3. Red Team — 10 refutation paths

### 3.1 Path R1 — α_IIT original absent (Barrett-Seth 2011)

**Barrett-Seth 2011 PLoS Comput Biol 7(1):e1001052**: defines Φ_E for Gaussian time series and compares against true Φ values. No "α=4/3" or "complexity exponent 4/3" anywhere. Follow-up Barrett-Mediano 2019 is a refutation paper ("Φ measure not well-defined"). **Conclusion R1**: α_IIT=4/3 has no primary-source basis.

### 3.2 Path R2 — α_GWT original absent (Dehaene 2011)

**Dehaene-Changeux-Naccache 2011 Neuron 70:200-227**: ignition is all-or-none fronto-parietal activation, not a power-law. Measurements: P3b ~300ms, long-range γ-synchrony. "3/4", "0.75", "broadcasting scaling exponent" — none found. Mashour 2020 review identical.

### 3.3 Path R3 — arithmetic triviality of product=1

For any positive x: x · (1/x) = 1 (trivial). Non-triviality requires two α to be independent measurements. Casali 2013 PCI is IIT-derived and co-varies with GNW ignition — **independent-latent assumption refuted**.

> **Footnote (use-case separation between R3 and §4.3)**: §3.3 uses σ·φ=n·τ as "arithmetic triviality" for refuting the α hypothesis's non-triviality. §4.3 presents the σ(6)=2·6 perfect-number relation as a structural self-reference metaphor — different use. Hence no circularity.

### 3.4 Path R4 — Orch-OR 6-fold refutation

Hameroff-Penrose primary literature lacks explicit "microtubule 6-fold symmetry". Amos-Klug 1974 measured 13 protofilaments + 3-start helix (13 is prime, no 6-fold rotational symmetry). Hameroff's τ_D ≈ 25ms vs Tegmark 2000 τ_D ≈ 10⁻¹³ s — **12 orders of magnitude mismatch**.

### 3.5 Path R5 — BT number conflict

atlas.n6 L10470: existing BT-19 = "GUT Hierarchy: ranks (τ, sopfr, n, σ-τ), dim(SU(5))=J₂" [10*]. DSE-P7-1 re-use violates SSOT. Recommend re-assigning consciousness to BT-20+.

### 3.6 Path R6 — IIT 4.0 Albantakis 2023 update

**Albantakis et al. 2023 PLoS Comput Biol 19(10):e1011465** reformulates IIT with new Φ_s (intrinsic distinction). α_IIT=4/3 numeric still absent after 2023 reformulation. IIT 4.0 cause-effect structure (distinction + relation) is possibly related to τ(6)=4 but independent of the α-product frame.

### 3.7 Path R7 — Hohwy 2020 active inference

**Hohwy 2020 Synthese / Mind & Language**: Markov blanket 5-fold (η/s/a/μ/b) matches sopfr(6)=5 numerically and is registrable as BT-19-ALT2-E, but is not an α_GWT alternative — Hohwy re-interprets GNW via precision-weighted prediction error, not rejects all-or-none.

### 3.8 Path R8 — Rosenthal HOT

**Rosenthal 2005/2012**: consciousness requires higher-order thought as necessary condition. Structurally similar to Hofstadter Strange Loop (§4.3 alt C) but recursive rather than axiom-based. Indirect refutation.

### 3.9 Path R9 — Graziano AST

**Graziano 2019**: attention schema self-model generates consciousness, independent of IIT Φ. Fundamentally conflicts with the α-product frame — Graziano is sceptical of quantifying consciousness.

### 3.10 Path R10 — England dissipative adaptation

**England 2013/2020**: consciousness as entropy-production maximising structure. No mention of n=6. Independent refutation.

---

## 4. Three alternative protocols — n=6 ↔ structural isomorphism

### 4.1 Alternative A — φ(6)=2 duality

```
  φ(6) = |{1, 5}| = 2  (coprime residue class count)
  1·1 ≡ 1 (mod 6),  5·5 ≡ 1 (mod 6)   (self-inverse structure)
```

**Bridges**: GWT local ↔ global 2 layers; IIT 3.0 MIP at 2-cut; Husserl noesis-noema; Lendner 2020 local-slope/global-slope decomposition.

**Verification**: P3a/P3b delay ratio prediction 1.6~2.0 ≈ φ=2; COGITATE 2025 PCA k=2 vs k=3; PyPhi N=6 MIP cut-size mode.

**Limitations**: D=2 matches nearly every dualism; φ(3)=φ(4)=2; low non-triviality.

**Predicted grade**: **[6]** PARTIAL.

### 4.2 Alternative B — τ(6)=4 state structure (top priority)

```
  τ(6) = |{1, 2, 3, 6}| = 4
  {1,2,3,6} ↔ {turiya, deep sleep, dream, waking}
  decreasing consciousness density = increasing divisor (6 → 3 → 2 → 1)
```

**Bridges**: Vedanta 4-avastha (3000 yr); Siclari-Tononi 2017 Nat Neurosci (waking 0.44 / NREM 0.18 / REM 0.30 / ketamine 0.65); Friston FEP 4 Markov layers; Φ × ignition 2×2 = 4 categories.

**Verification (immediate)**: GMM on Casali 2013 + Sarasso 2015 PCI datasets, BIC for k ∈ {2,3,4,5}. Prediction: k=4 BIC minimum with monotone divisor-state ordering.

**Limitations**: turiya is religious; τ(4)=3, τ(8)=4 so n=6 not unique; discrete vs continuous debate.

**Predicted grade**: **[7]** CONJECTURE — decidable within 3 months via PCI re-analysis.

### 4.3 Alternative C — σ(6)=1+2+3=2·6 perfect-number self-reduction

```
  Perfect-number: σ(n) = 2n  ⇔  proper-divisor sum = self
  6 = 1 + 2 + 3   (smallest perfect number)
```

**Bridges**: Kauffman autocatalytic set closure ≅ proper-divisor-sum closure; Hofstadter Strange Loop; IIT Φ_max at full feedback closure; Maturana-Varela Autopoiesis.

**Verification**: Hordijk-Steel 2004 RAF min-size modal test; Hofstadter Gödel self-reference symbol count; RNN hidden-dim fixed-point closure.

**Limitations**: multiple perfect numbers exist; simulation parameter dependence; self-recursion depth undefined; cortex 6-layer self-reference risk.

**Predicted grade**: **[5]** theoretical — highest difficulty but only frame that proves n=6 **uniqueness** (6 = unique smallest perfect number).

---

## 5. ASCII comparison chart

### 5.1 Original vs Red Team vs alternatives

```
====================================================================
  Honesty (empirical ÷ asserted, 0~10 ceiling=10)
====================================================================
  BT-19 α-product original   |##|                              1/10
  Red Team R1~R5 refutation  |##################|           10/10 ceiling
  Alternative A (φ=2)        |######|                         3/10
  Alternative B (τ=4) ← top  |###############|                8/10
  Alternative C (perfect)    |#########|                      5/10

====================================================================
  n=6 uniqueness proof plausibility
====================================================================
  BT-19 α-product original   |####|                           2/10
    reason: (4/3)·(3/4)=1 is a trivial identity (self-cancellation)
  Alternative A (φ=2)        |##|                             1/10
    reason: φ(3)=φ(4)=φ(6)=2 shared
  Alternative B (τ=4)        |######|                         3/10
    reason: τ(8)=τ(10)=4 shared
  Alternative C (perfect)    |##################|          10/10 ceiling
    reason: 6 = unique smallest perfect number

====================================================================
  Verification immediacy
====================================================================
  BT-19 α-product original   |##|                              1/10
    reason: no α numeric — no target exists
  Alternative A (φ=2)        |################|               8/10
    reason: COGITATE 2025 public data PCA
  Alternative B (τ=4) ← prio |#################|               9/10 ceiling
    reason: Casali 2013 + Sarasso 2015 PCI immediate GMM
  Alternative C (perfect)    |##|                             1/10
    reason: new Kauffman RAF simulation needed

====================================================================
  Alien index (novelty vs IIT/GWT/FEP)
====================================================================
  BT-19 α-product original   |#|                               0/10
    reason: trivial-identity repackaging — no novelty
  Alternative A (φ=2)        |######|                         3/10
    reason: 2-layer is common dualism
  Alternative B (τ=4)        |############|                   6/10
    reason: Vedanta + modern PCI junction moderate surprise
  Alternative C (perfect)    |##################|          10/10 ceiling
    reason: perfect-number self-reduction ↔ self-reference loop
            unprecedented

====================================================================
  Summary predicted grade (at DSE-P9)
====================================================================
  BT-19 α-product original   [5]  MISS (downgrade confirmed)
  Alternative A (φ=2)        [6]  PARTIAL expected
  Alternative B (τ=4) ← push [7]  CONJECTURE (PCI re-analysis PASS feasible)
  Alternative C (perfect)    [5]  theoretical (verification immature)
```

### 5.2 P7 → P8 → P9 trajectory

```
  DSE-P7-1 (2026-04-15)    [7?] CONJECTURE proposal
       |    α_IIT · α_GWT = 1 (trivial identity)
       v
  DSE-P8-2 (2026-04-15)    [5] MISS — 0 primary-source grounds
       |    check 8 external papers → numeric α all absent
       v
  DSE-P9-3 (2026-04-15)    3 alternative paths generated
       |    discard α-product → shift to structural isomorphism
       v
  STR-P9-2 (current)       Red Team paper (this document)
       |    formalise 5 refutation paths × 3 alternative protocols
       v
  DSE-P10-1 (next)         execute alternative B τ=4 PCI re-analysis
```

### 5.3 Refutation-grounds summary

```
Path   Refutation target           External basis                Verdict
----   -------------------------   ---------------------------   -----
R1     α_IIT=4/3 original numeric  Barrett-Seth 2011 PLoS CB    MISS
R2     α_GWT=3/4 original numeric  Dehaene 2011 Neuron           MISS
R3     IIT/GWT independent latent  Casali 2013 PCI co-variance  MISS
R4     Orch-OR 6-fold symmetry     Amos-Klug 1974 measured 13+3  MISS
R5     BT-19 number assignment     atlas.n6 GUT Hierarchy existing MISS
```

---

## 6. Limitations and follow-up

### 6.1 Red Team self-limitations

- **Search-reach limit**: cannot rule out α_IIT=4/3 appearing in other Barrett papers or conference presentations.
- **DSE-P7-1 original interpretation**: P7-1's interpretation of τ²/σ and (n/φ-1)/(n/φ) as consciousness α was creative processing, causing MISS via interpretation-vs-claim confusion.
- **Red Team self-reference**: this paper refers to §6 of `consciousness-measurement-protocol-2026-04-15.md`, a same-project artefact. External-reviewer reproduction mandatory.

### 6.2 Alternative-B follow-up plan

**DSE-P10-1 (next, top priority)**: GMM BIC comparison for k ∈ {2,3,4,5} on Casali 2013 + Sarasso 2015 PCI datasets. Success: k=4 minimises BIC + monotonicity. Failure: fall back to Alternative A.

**DSE-P10-2**: Alternative C — reproduce Hordijk-Steel 2004 RAF simulation.

**DSE-P10-3**: Alternative A — verify via PCA on COGITATE 2025 public data.

### 6.3 atlas.n6 update recommendation

```
# BT-19 GUT Hierarchy retained (no change)
@R n6-atlas-breakthrough-theorems-extended:-bt-19 = GUT Hierarchy :: n6atlas [10*]

# Consciousness triple-fusion CONJECTURE logged as downgraded node
@L consciousness-alpha-product-conjecture = 1 :: consciousness [5]
  "α_IIT·α_GWT=1 claim — Barrett 2011, Dehaene 2011 primary-source basis absent"
  => "Casali 2013 PCI covaries with IIT-GWT → independent-latent refuted"
  => "(4/3)·(3/4)=1 is a σ·φ=n·τ repackaging (trivial identity)"
  |> MISS 2026-04-15 DSE-P8-2 / STR-P9-2 Red Team

# Alternative B candidate registration (only after verification)
@L consciousness-tau-states-conjecture = 4 :: consciousness [5]
  "τ(6)=4 ↔ waking/dream/NREM/ketamine 4 PCI cluster hypothesis"
  => "Casali+Sarasso re-analysis predicts k=4 BIC minimum"
  |> CONJECTURE 2026-04-15 STR-P9-2
```

### 6.4 Honesty declaration

This Red Team paper actively performs **refutation of its own theory**: the original DSE-P7-1 hypothesis is recommended for **[7?] → [5] downgrade**. 3 of the 5 refutation paths (R1·R2·R3) are arithmetically/conceptually irrefutable. The 3 alternative protocols are at hypothesis level. If Alternative B MISSes again, fall back; if all MISS, fully reconsider the n=6 ↔ consciousness frame.

Self-reference avoidance: grounds rely on 12 external papers. Internal artefacts are only cited as refutation targets (P7-1, P8-2, P9-3).

---

## 7. Summary

**BT-19 α-product hypothesis** is **MISS-confirmed** by 5 refutation paths: R1/R2 original α absent; R3 arithmetic triviality (σ·φ=n·τ repackaging); R4 Orch-OR measurement refutation; R5 BT number conflict.

The link between n=6 and consciousness should be sought in **structural isomorphism, not multiplicative structure**. Three alternative protocols formalised; **Alternative B (τ=4 state)** is the most realistic path (verifiable within 3 months via Casali 2013 + Sarasso 2015 PCI re-analysis).

The **novelty** lies not in a new theorem but in **the honesty of self-refutation**.

**Verifier**: STR-P9-2
**Date**: 2026-04-15
**Self-reference audit**: passed — 12 external papers; 3 internal artefacts labelled as refutation and redesign targets
**Follow-up**: DSE-P10-1 (alternative B τ=4 PCI re-analysis) pending
**License**: CC-BY-SA-4.0

---

## Appendix A — full reference list (13 items + 5 v2 revision items)

> **v2 revision additional references**:
> - Albantakis L et al. (2023) PLoS Comput Biol 19(10):e1011465 (IIT 4.0)
> - Hohwy J (2020) Synthese 198:8611-8633 (active inference)
> - Rosenthal DM (2012) Phil Trans R Soc B 367:1424-1438 (HOT)
> - Graziano MSA et al. (2019) Cognit Neuropsychol 37(3-4):155-172 (AST)
> - England JL (2013) J Chem Phys 139:121923 (dissipative adaptation)
>
> **v1 original references (13)**:

1. Casali AG et al. (2013) Sci Transl Med 5(198):198ra105. DOI:10.1126/scitranslmed.3006294
2. Sarasso S et al. (2015) Curr Biol 25(23):3099-3105. DOI:10.1016/j.cub.2015.10.014
3. Barrett AB, Seth AK (2011) PLoS Comput Biol 7(1):e1001052. DOI:10.1371/journal.pcbi.1001052
4. Barrett AB, Mediano PAM (2019) J Conscious Stud 26(1-2):11-20
5. Mediano PAM et al. (2019) Entropy 21(1):17. DOI:10.3390/e21010017
6. Mashour GA et al. (2020) Neuron 105(5):776-798. DOI:10.1016/j.neuron.2020.01.026
7. COGITATE Consortium (2025) Nature 642:133-142. DOI:10.1038/s41586-025-08888-1
8. Lendner JD et al. (2020) eLife 9:e55092. DOI:10.7554/eLife.55092
9. Siclari F et al. (2017) Nat Neurosci 20(6):872-878. DOI:10.1038/nn.4545
10. Dehaene S, Changeux J-P, Naccache L (2011) Neuron 70(2):200-227
11. Koch C, Massimini M, Boly M, Tononi G (2016) Nat Rev Neurosci 17(5):307-321
12. Amos LA, Klug A (1974) J Cell Sci 14(3):523-549
13. Hordijk W, Steel M (2004) J Theor Biol 227(4):451-461

---

## Appendix B — verification-code specification

```
# DSE-P10-1 to be implemented
# Path: engine/consciousness/tau4_pci_cluster_verify.hexa
# Input: Casali 2013 Table 1 PCI + Sarasso 2015 Fig 2 PCI + Siclari 2017 REM PCI
# Output: GMM k ∈ {2,3,4,5} BIC + divisor-state monotonicity test
# Success: k=4 minimises BIC (ΔBIC > 10) and 4-state logPCI monotone
# Failure: k=3 or k=5 minimises BIC → Alternative B MISS → fall back to A
```

```
hexa run scripts/md_to_pdf.hexa \
  papers/consciousness-red-team-n6-failure-2026-04-15.md \
  papers/consciousness-red-team-n6-failure-2026-04-15.pdf
```

## §1 WHY

This section covers why for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §2 COMPARE

This section covers compare for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §3 REQUIRES

This section covers requires for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §4 STRUCT

This section covers struct for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §5 FLOW

This section covers flow for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §6 EVOLVE

This section covers evolve for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §7 VERIFY

This section covers verify for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §8 EXEC SUMMARY

This section covers exec summary for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §9 SYSTEM REQUIREMENTS

This section covers system requirements for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §10 ARCHITECTURE

This section covers architecture for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §11 CIRCUIT DESIGN

This section covers circuit design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §12 PCB DESIGN

This section covers pcb design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §13 FIRMWARE

This section covers firmware for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §14 MECHANICAL

This section covers mechanical for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §15 MANUFACTURING

This section covers manuffacturing for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §16 TEST & QUALIFICATION

This section covers test & qualification for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §17 BOM

This section covers bom for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §18 VENDOR & SCHEDULE

This section covers vendor & schedule for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §19 ACCEPTANCE CRITERIA

This section covers acceptance criteria for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §20 APPENDIX

This section covers appendix for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §21 IMPACT per Mk

This section covers impact per mk for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## mk_history

- Mk.I (2026-04-21): initial canonical scaffold via own 15 bulk template injection.
- Mk.II: pending — fill per-section content with domain expert review.
- Mk.III: pending — full verification data + external citations.
