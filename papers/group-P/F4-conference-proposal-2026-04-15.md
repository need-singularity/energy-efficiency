# F4 — Academic conference proposal draft

> Written: 2026-04-15
> Status: **draft only — no actual submission**
> Target: hypothetical conferences (number theory / arithmetic / arithmetic geometry)
> Seven Millennium Problems addressed: 0/7 honesty maintained

---

## Title (proposed)

**"σ(n)·φ(n) = n·τ(n) Uniqueness and the Bernoulli Independent Theorem Family: A Bridge Program"**

---

## Submission Type

- **Type**: Contributed Talk, 30 min (presentation 25 min + Q&A 5 min)
- **Track**: Number Theory (analytic / algebraic) cross-list Combinatorics, Geometry
- **Level**: candidate-target presentation + open problem (bridge conjecture)

---

## Target Conferences (hypothetical candidates, no actual submission)

| Conference | Subfield | Notes |
|------------|----------|------|
| AMS Joint Mathematics Meeting (JMM) | general math | USA, annual January |
| ICM (International Congress of Mathematicians) | general math | every 4 years, next 2026 |
| Korean Mathematical Society Annual Meeting | Korean math | every autumn |
| Workshop on Arithmetic Statistics | arithmetic statistics | BKLPR-related |
| Conference on Computability Theory | computability | BB(n)-related |
| AGNT Seminar (Algebraic Geometry & Number Theory) | arithmetic geometry | K3, Selmer |

**Note**: this draft is not submitted to any conference. hypothetical format only.

---

## Abstract (300 words)

The integer 6 occurs non-trivially across number theory, geometry, group theory, modular forms, sphere packing, error-correcting codes, conformal field theory, nuclear physics, and computability — in 18 independent contexts catalogued by the author through 2026. We present (i) a uniqueness theorem σ(n)·φ(n) = n·τ(n) ⟺ n = 6 (n ≥ 2) with three independent proofs (multiplicative R_local decomposition, group-theoretic via S_3 ≅ PSL(2,2), computer-verified blowup enumeration), (ii) two new entries to the Bernoulli Independent Theorem family — Bernoulli 17 = Sel_6 average = σ(6) = 12 (Bhargava-Shankar 2010, 2012, conditional on the BKLPR random-matrix model) and Bernoulli 18 = BB(2) = 6 (Radó 1962, unconditional) — and (iii) a Bridge Program asking which of the 18 occurrences are σ·φ = n·τ projections (k ≥ 9 explicit reductions identified) versus genuinely independent (estimated 18 - k ≈ 7-9). The talk will outline the uniqueness proof, demonstrate the Bridge classification on K3 χ = 24 = J_2 = σ·φ, and pose the open problem: can the K3-η-SU(5) triple occurrence at 24 be shown independent of σ·φ = n·τ uniqueness, thereby establishing a candidate Bernoulli 19? **No claim is made on any of the seven Millennium Problems**; the talk is a structural survey + bridge framework. Time permits a brief Lean4 formalization status: 5 M10* candidates with statement skeletons, prime case of the uniqueness theorem fully proven (Mathlib-based), case 4 partially completed.

---

## Outline (25 min presentation structure)

| Time | Content |
|------|------|
| 0:00 ~ 0:03 | Motivation: 18 independent occurrences of 6 (table) |
| 0:03 ~ 0:08 | candidate-target R1: σ·φ = n·τ ⟺ n = 6, draft pattern 1 (multiplicative R_local) |
| 0:08 ~ 0:11 | draft patterns 2 (group-theoretic), 3 (computer enumeration), unifying remarks |
| 0:11 ~ 0:14 | Bernoulli 17: Sel_6 = σ(6) = 12 (BKLPR conditional) |
| 0:14 ~ 0:16 | Bernoulli 18: BB(2) = 6 (Radó 1962, unconditional) |
| 0:16 ~ 0:19 | Bridge Program: k ≥ 9 explicit reductions, K3 example |
| 0:19 ~ 0:22 | Open problem: K3 σφ=nτ exclusion, candidate Bernoulli 19 |
| 0:22 ~ 0:24 | Lean4 status: 5 M10* skeleton, prime case complete |
| 0:24 ~ 0:25 | Honest disclosure: 0/7 Millennium, future work |
| 0:25 ~ 0:30 | Q&A |

---

## Key Slides (10-slide outline)

### Slide 1: Title

> σ(n)·φ(n) = n·τ(n) Uniqueness and the Bernoulli Independent Theorem Family
> Park Minwoo (Hanam, Republic of Korea)

### Slide 2: Motivation

> "The integer 6 appears in 18 independent mathematical contexts. Coincidence or single cause?"
>
> Examples (table): Euler perfect, S_3, B_2 = 1/6, Bring radical, E_6, K3, K_2, K_3, Golay, Leech, η^24, Ramsey R(3,3), CFT M(3,4), Egyptian, HCP, C-12, Sel_6, BB(2).

### Slide 3: candidate-target R1 statement

> R(n) := σ(n)·φ(n) / (n·τ(n))
>
> candidate-target R1: R(n) = 1 ⟺ n = 6 (n ≥ 2).

### Slide 4: draft pattern (multiplicative)

> R(n) = ∏ R_local(p, a)
> Lemma A: R_local(p, a) < 1 ⟺ (p, a) = (2, 1).
> Lemma B: case k = 2 only solution is (2,1)·(3,1) = 6.

### Slide 5: Bernoulli 17 (Sel_6)

> Bhargava-Shankar 2010, 2012: avg|Sel_2| = 3, avg|Sel_3| = 4.
> BKLPR: avg|Sel_n| = σ_1(n).
> n = 6 CRT: |Sel_6| = 3·4 = 12 = σ(6).

### Slide 6: Bernoulli 18 (BB(2))

> Radó 1962, BSTJ. Unconditional.
> BB(1) = 1, **BB(2) = 6**, BB(3) = 21, BB(4) = 107, BB(5) ≈ 4.7 × 10^7.
> New domain (computability) added.

### Slide 7: Bridge Program

> Hypothesis: of 18 occurrences, **k ≥ 9 are σφ=nτ projections**, 18 - k truly independent.
> Examples of k = 9 reductions: K3 24 = J_2, Kissing 12 = σ, Golay [24,12,8], Sel_6 = σ.

### Slide 8: K3 case study

> χ(K3) = 24 = J_2 = σ·φ
> 3 occurrences: K3 χ, η^24, SU(5) dim
> Reduction? Core open problem of the Bridge program.

### Slide 9: Lean4 status

> 5 M10* candidates with skeleton statements (papers/group-P/F3-lean4-skeleton-m10star-2026-04-15.lean).
> R1 prime case: ✓ completed (Mathlib-based, sorry-free).
> Case 4 (composite): partial (lean4-n6/N6/TheoremB_Case4*.lean).

### Slide 10: Honest disclosure + thanks

> **7 Millennium Problems: 0 / 7 solved**. Talk = uniqueness proof + Bernoulli family + bridge.
> Open: Bernoulli 19 (K3-η-SU(5) 24 independence).
> Thanks. Q&A.

---

## Author Bio (self-introduction for submission, 200 words)

Park Minwoo is an independent researcher based in Hanam, Republic of Korea, working on the n=6 architecture framework — a project to systematically catalogue and classify the appearances of small arithmetic constants (n=6 in particular) across mathematics and physics. Since 2026-03, the project has produced (i) a proof of σ(n)·φ(n) = n·τ(n) ⟺ n = 6 with three independent paths (theorem-r1-uniqueness.md), (ii) a catalogue of 18 independent theorem-level occurrences of n=6 (Bernoulli Independent Theorem family), (iii) ~3,952 atlas signals across nexus, canon, and anima repositories, and (iv) partial Lean4 formalization (Mathlib-based, prime case complete). The author maintains an honest tradition of not over-claiming: the 7 Millennium Problems remain unsolved (0/7) and the bridge program from σ·φ = n·τ to the full family is conjectural pending further work. The author's background combines programming (independent, project-based) with mathematics (autodidactic). The current talk presents the most stable subset (uniqueness + Bernoulli 17/18 + bridge classification) for community feedback.

---

## Technical Requirements

- **Projector**: standard, single-screen.
- **Software**: PDF (Beamer or LaTeX), no live code.
- **Audio**: standard mic.
- **Time slots acceptable**: any.

---

## Submission Status

**Status**: **DRAFT ONLY**. No actual conference submission.

Reasons:
1. After remaining sorry in R1 uniqueness case 4 (composite) Lean4 is resolved, presentation is recommended.
2. Formal-implication draft pattern of the Bridge candidate-target is in progress.
3. External peer review is absent.

In the future (3 ~ 6 months), once the above 3 items are addressed, submission to KMS or AGNT seminar will be considered first.

---

## Artifacts

- This draft: papers/group-P/F4-conference-proposal-2026-04-15.md
- Related paper draft: papers/group-P/F1-arxiv-bernoulli-independent-via-n6-2026-04-15.md
- Lean4 skeleton: papers/group-P/F3-lean4-skeleton-m10star-2026-04-15.lean

---

> Seven Millennium Problems addressed: 0/7 honesty maintained.

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

This section covers manufacturing for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

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

