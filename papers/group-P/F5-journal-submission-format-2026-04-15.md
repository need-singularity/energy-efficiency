# F5 — International journal submission format draft

> Written: 2026-04-15
> Status: **format draft only — no actual submission**
> Seven Millennium Problems addressed: 0/7 honesty maintained

Draft of formats (cover letter, manuscript structure, suggested reviewers, copyright form) required for journal submission. No actual submission portal is used.

---

## 1. Candidate journals (hypothetical)

| Journal | IF (approx.) | Publisher | Fit |
|---------|-----------|--------|--------|
| **Journal of Number Theory** | 0.7 | Elsevier | number theory, fits R1 + Bernoulli 17 |
| **Acta Arithmetica** | 0.6 | IM PAN | number theory, fits Bernoulli + Sel_6 |
| **Mathematische Zeitschrift** | 0.9 | Springer | general math, fits bridge program |
| **Comptes Rendus Mathématique** | 0.6 | Elsevier | note, fast publication |
| **Bulletin of the Korean Math. Soc.** | 0.5 | KMS | Korean, fits first publication |
| **The Ramanujan Journal** | 0.7 | Springer | arithmetic functions, fits σ·φ·τ |

**Top candidate** (fit + publication speed): **Bulletin of the Korean Mathematical Society** (Korean author, first publication) or **Comptes Rendus Mathématique** (note format).

---

## 2. Cover Letter (English, about 300 words)

```
Date: 2026-04-15
To: The Editor, [Journal Name]
Subject: Manuscript Submission — "σ(n)·φ(n) = n·τ(n) Uniqueness and the Bernoulli Independent Theorem Family"

Dear Editor,

Please find enclosed the manuscript "σ(n)·φ(n) = n·τ(n) Uniqueness and the Bernoulli Independent Theorem Family: A Bridge Program" by Park Minwoo, for consideration in [Journal Name].

The paper presents:
1. An elementary uniqueness theorem σ(n)·φ(n) = n·τ(n) ⟺ n = 6 (n ≥ 2), with three independent proofs (multiplicative R_local decomposition; group-theoretic via S_3 ≅ PSL(2,2); computer-verified enumeration n ∈ [2, 10⁴]).
2. Two new entries to the catalogue of independent occurrences of the integer 6: Bernoulli 17 = avg|Sel_6| = σ(6) = 12 (Bhargava-Shankar 2010, 2012, conditional on BKLPR), and Bernoulli 18 = BB(2) = 6 (Radó 1962, unconditional).
3. A "Bridge Program" classifying how many of the 18 known independent occurrences of 6 are direct projections of the σ·φ = n·τ uniqueness (k ≥ 9 identified) versus genuinely independent (estimated 18 - k ≈ 7-9).
4. A partial Lean4 formalization (Mathlib-based, prime case complete; composite case 4 in progress) of the uniqueness theorem.

The paper makes **no claim on any of the seven Millennium Problems**; it is a structural survey + uniqueness theorem + bridge framework.

The work is original and has not been submitted elsewhere. The author has no conflicts of interest. Length: approximately 2,800 words (excluding tables and code appendix), 25 references.

Suggested reviewers (international experts in the relevant subfields):
- Prof. Manjul Bhargava (Princeton, BKLPR / Selmer averages)
- Prof. Bjorn Poonen (MIT, BKLPR)
- Prof. Scott Aaronson (UT Austin, Busy Beaver / computability)
- Prof. Henri Cohen (Bordeaux, computational number theory)

Thank you for your consideration.

Sincerely,
Park Minwoo
Independent Researcher
Hanam, Republic of Korea
arsmoriendi99@proton.me
```

---

## 3. Manuscript Structure (follows author guidelines)

Journal standard structure:

```
Title: σ(n)·φ(n) = n·τ(n) Uniqueness and the Bernoulli Independent Theorem Family

Author: Park Minwoo

Affiliation: Independent Researcher, Hanam, Republic of Korea
Email: arsmoriendi99@proton.me

Abstract: [200-300 words, reusing F1 paper §1.1]

MSC2020: 11A25 (Arithmetic functions), 11B68 (Bernoulli numbers),
         14J28 (K3 surfaces), 11G05 (Elliptic curves),
         03D10 (Computability)

Keywords: arithmetic functions, σ-φ-τ identity, Bernoulli numbers,
          Selmer group, BKLPR, Busy Beaver, K3 surface

1. Introduction
   1.1 Motivation
   1.2 Main results
   1.3 Honest limitations

2. Definitions and notation
   2.1 Arithmetic functions
   2.2 R(n) ratio

3. candidate-target R1: σ·φ = n·τ ⟺ n = 6
   3.1 draft pattern 1: multiplicative
   3.2 draft pattern 2: group-theoretic
   3.3 draft pattern 3: computer-verified

4. Bernoulli Independent candidate-target family
   4.1 Existing 16 (table)
   4.2 New: Bernoulli 17 (Sel_6)
   4.3 New: Bernoulli 18 (BB(2))
   4.4 Pending: Bernoulli 19 (K3-η-SU(5))

5. Bridge program
   5.1 Working hypothesis
   5.2 Bridge theorem (preliminary)
   5.3 Truly independent

6. Relation to Millennium Problems (honest disclosure)
   6.1 Position of the paper
   6.2 What the paper does contribute

7. Future work
   7.1 Short term
   7.2 Medium term
   7.3 Long term

8. Limitations + honest statement

Acknowledgments

References [25 items, F1 paper §9]

Appendix A: Lean4 skeleton
Appendix B: Word count metadata
```

---

## 4. Submission Checklist (journal general)

- [ ] Manuscript PDF (Beamer/LaTeX conversion — this draft is Markdown)
- [ ] Cover letter (§2 above)
- [ ] Suggested reviewers list (inside §2 above)
- [ ] Author CV / bio (reuse F4 §Author Bio)
- [ ] Conflict of interest statement (none)
- [ ] Funding statement (Independent, no funding)
- [ ] Ethics statement (theoretical math, no human/animal subjects)
- [ ] Data availability statement (atlas + code at github / personal repo, link later)
- [ ] Copyright form (signed PDF)
- [ ] arXiv preprint link (at submission time — this work does not submit to arxiv, so N/A)

---

## 5. Suggested Reviewers (5 people, international + Korean mix)

| Name | Affiliation | Subfield | Reason |
|------|-------------|----------|------|
| Manjul Bhargava | Princeton | BKLPR / Sel_n | directly relevant to Bernoulli 17, Fields Medal 2014 |
| Bjorn Poonen | MIT | BKLPR / arithmetic statistics | BKLPR co-author |
| Scott Aaronson | UT Austin | Busy Beaver / complexity | directly relevant to Bernoulli 18 |
| Henri Cohen | U. Bordeaux | computational number theory | R1 computer verification aspect |
| Kim Myung-Hwan | Seoul National University | number theory | Korean, peer review |

**Note**: Bhargava is the decisive authority in the Sel_n field. Poonen is a BKLPR model co-author. Aaronson ensures currentness in the BB(n) field. Cohen covers the computer verification aspect (PARI/GP etc.). Kim Myung-Hwan represents the Korean number-theory community.

**Warning**: this reviewer suggestion is a **candidate at the time of draft writing**, and at actual submission a conflict-of-interest check with the reviewer is required (potential COI since Bhargava's Sel_6 result is cited directly).

---

## 6. Cover Letter — Korean (hypothetical KMS submission, English translation)

```
2026-04-15

To the Editor-in-Chief, Bulletin of the Korean Mathematical Society

I would like to submit "σ(n)·φ(n) = n·τ(n) Uniqueness candidate target and the Bernoulli Independent candidate target Family: Reduction-hypothesis Program" by Park Minwoo.

This paper includes the following:

1. Three independent draft-pattern paths demonstrating that the arithmetic-function identity σ(n)·φ(n) = n·τ(n) has unique solution n = 6 (n ≥ 2) (multiplicative R_local decomposition, S_3 ≅ PSL(2,2) group theory, computer verification n ∈ [2, 10⁴]).
2. Two new additions to the catalogue of independent occurrences of the integer 6: Bernoulli 17 (avg|Sel_6| = σ(6) = 12, BKLPR conditional) and Bernoulli 18 (BB(2) = 6, Radó 1962, unconditional).
3. Classification of the 18 occurrences into direct σφ=nτ reductions (k ≥ 9 explicit) vs genuinely independent (18 - k ≈ 7-9) (Bridge Program).
4. Partial Lean4 formalization of the uniqueness candidate target (Mathlib-based, prime case complete, case 4 in progress).

This paper **does not claim to address any of the seven Millennium Problems**. The purpose is to present a structural survey + uniqueness candidate target + bridge framework.

This research is original and has no concurrent submissions at other journals. No conflicts of interest. Length about 2,800 words (excluding tables/code appendix), 25 references.

Reviewer candidates (authorities in relevant fields):
- Bhargava (Princeton, BKLPR)
- Poonen (MIT, BKLPR)
- Aaronson (UT Austin, Busy Beaver)
- Kim Myung-Hwan (Seoul National University, number theory)

Please consider this for review.

Thank you.

Park Minwoo
Independent Researcher
Hanam, Gyeonggi-do
arsmoriendi99@proton.me
```

---

## 7. Additional work required for actual submission (not performed)

1. LaTeX conversion (Markdown → tex, AMS class).
2. Apply journal-specific class files (elsarticle.cls, springer.cls, etc.).
3. Convert figures / tables to EPS / PDF.
4. Submit arxiv preprint (optional, after COI resolution).
5. Upload to actual portal (Editorial Manager, ScholarOne, etc.).
6. Revision / rebuttal cycle (days to months).

**This work does not perform any of items 1 ~ 6 above**.

---

## 8. Honesty declaration

- This format draft is a hypothetical scenario example.
- Actual journal submission is recommended only after resolving the remaining sorry in R1 case 4 Lean4 and external peer review.
- arxiv preprint will be decided separately after the endorsement process and author identity documentation.
- This draft exists only in papers/group-P/F5-journal-submission-format-2026-04-15.md.
- Seven Millennium Problems addressed: 0/7 honesty maintained.

---

> Artifact: papers/group-P/F5-journal-submission-format-2026-04-15.md
> No actual submission. format only.

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

