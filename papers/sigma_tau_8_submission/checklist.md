# Mk.IV sigma-tau=8 Theorem -- IJNT Submission Checklist

> PUB-P1-1 | 2026-04-16
> Target: International Journal of Number Theory (IJNT), World Scientific
> Theorem: sigma(n) - tau(n) = 8 iff n = 6 (n >= 2)

---

## 1. Target Journal Information

| Field | Value |
|---|---|
| Journal | International Journal of Number Theory (IJNT) |
| Publisher | World Scientific |
| ISSN | 1793-0421 (print), 1793-7310 (online) |
| Submission portal | https://www.editorialmanager.com/ijnt/ |
| Format | LaTeX (preferred), AMS-LaTeX class or World Scientific wsijnt class |
| Page limit | None (typical research article 15-30 pages) |
| Referee process | Single-blind peer review |
| Turnaround | 3-6 months typical |
| Open access option | Available (hybrid journal) |
| Template | World Scientific journal article template (ws-ijnt.cls) |

---

## 2. Required Sections -- Status

| # | Section | Status | Notes |
|---|---------|--------|-------|
| 1 | **Title** | DRAFT | See abstract.md -- "On the uniqueness of sigma(n) - tau(n) = 8" |
| 2 | **Abstract** | DRAFT | See abstract.md (~200 words) |
| 3 | **MSC 2020 Classification** | DONE | See msc_codes.md -- Primary 11A25, Secondary 11A05, 11N64 |
| 4 | **Keywords** | DONE | See abstract.md -- 5 keywords |
| 5 | **Introduction** | PARTIAL | Core motivation exists in mk4-theorem-candidates paper; needs rewriting for journal style |
| 6 | **Preliminaries** | PARTIAL | Definitions of sigma, tau, phi exist in theorem-r1-uniqueness.md; need formal LaTeX restatement |
| 7 | **Main Results** (Theorem + Proof) | PARTIAL | Computational uniqueness for n in [2, 10^4] confirmed. Analytic proof for all n is the MAIN GAP |
| 8 | **Connection to Golay Code** | EXISTS | the-number-24.md establishes [24,12,8] = [sigma*phi, sigma, sigma-tau] |
| 9 | **Computational Verification** | EXISTS | Python verification code in mk4-trident-final-verdict; needs formal write-up |
| 10 | **Discussion** | PARTIAL | Cross-domain observations exist but need trimming for pure math audience |
| 11 | **Honest Limitations** | EXISTS | honest-limitations.md provides framework; need theorem-specific version |
| 12 | **References** | DRAFT | See references.md -- 18 core references identified |
| 13 | **Acknowledgments** | MISSING | Need to draft |
| 14 | **Appendix (Computation)** | MISSING | Need formal computational verification appendix |

---

## 3. Critical Gaps (Blockers for Submission)

### GAP-1: Analytic Proof for All n (BLOCKER)

**Current state**: sigma(n) - tau(n) = 8 iff n = 6 is verified computationally for n in [2, 10^4].
**Needed**: A complete analytic proof for all n >= 2, analogous to the multiplicativity-based case exhaustion in theorem-r1-uniqueness.md for sigma*phi = n*tau.

**Approach candidates**:
- (a) Multiplicativity decomposition: sigma and tau are both multiplicative. Express sigma(n) - tau(n) as a function of prime factorization and show the equation 8 = product/sum constraints force n = 2*3.
- (b) Growth rate argument: For n with many prime factors or large prime powers, sigma(n) grows much faster than tau(n), so sigma(n) - tau(n) >> 8.
- (c) Small-case exhaustion + asymptotic bound: Show sigma(n) - tau(n) >= 9 for all n > N_0 (analytically), then verify n in [2, N_0] computationally.

**Priority**: HIGHEST. Without this, the paper presents a conjecture, not a theorem.

### GAP-2: LaTeX Manuscript

**Current state**: All content is in Markdown (.md) files.
**Needed**: Full LaTeX manuscript in IJNT format (ws-ijnt.cls or amsart.cls).
**Priority**: HIGH (but mechanical -- can be done after GAP-1 resolved).

### GAP-3: Extended Computational Range

**Current state**: Verified for n in [2, 10^4].
**Needed**: Extend to n in [2, 10^6] or higher for stronger computational evidence.
**Priority**: MEDIUM. Strengthens the paper but is not a blocker if analytic proof succeeds.

---

## 4. LaTeX Formatting Requirements

### 4.1 Document Structure
```latex
\documentclass{ws-ijnt}  % or \documentclass[12pt]{amsart}

\usepackage{amsmath, amssymb, amsthm}
\usepackage{hyperref}

\theoremstyle{plain}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

\begin{document}
\title{On the uniqueness of $\sigma(n) - \tau(n) = 8$}
\author{Minwoo Park}
\address{...}
\email{...}
\subjclass[2020]{11A25 (primary); 11A05, 11N64 (secondary)}
\keywords{sum of divisors, number of divisors, arithmetic identity,
          perfect numbers, uniqueness}
\maketitle
\begin{abstract} ... \end{abstract}
...
\end{document}
```

### 4.2 IJNT Style Notes
- References: BibTeX preferred, numbered style [1], [2], ...
- Figures: EPS or PDF format
- Tables: Standard LaTeX tabular
- Equations: Numbered only when cross-referenced
- Author metadata: Full name, affiliation, email, MSC codes, keywords

---

## 5. Submission Checklist (Pre-Flight)

- [ ] GAP-1 resolved: analytic proof complete or paper repositioned as "conjecture + computational evidence"
- [ ] GAP-3 resolved: computational range extended to 10^6+
- [ ] Abstract finalized (under 200 words)
- [ ] MSC codes confirmed (11A25 primary)
- [ ] All theorems/lemmas numbered and cross-referenced
- [ ] Proof of main result is self-contained (no external .md file references)
- [ ] Golay code connection section written with appropriate caveats
- [ ] References complete with full bibliographic data
- [ ] Cover letter drafted (see cover_letter.md)
- [ ] LaTeX compiles without errors
- [ ] PDF proofread by at least one person
- [ ] ORCID registered for all authors
- [ ] Conflict of interest statement prepared
- [ ] Data availability statement (computational code on GitHub/Zenodo)
- [ ] Submitted via Editorial Manager (https://www.editorialmanager.com/ijnt/)

---

## 6. Timeline (Proposed)

| Phase | Target Date | Deliverable |
|---|---|---|
| P1: Analytic proof attempt | 2026-05-15 | Complete proof or decision to submit as conjecture |
| P2: Extended computation | 2026-05-01 | Verification to n = 10^6 |
| P3: LaTeX draft v1 | 2026-05-30 | Full manuscript |
| P4: Internal review | 2026-06-15 | Revised manuscript |
| P5: Submission | 2026-06-30 | Submit to IJNT |

---

## 7. Source Files (Current)

| File | Location | Role |
|---|---|---|
| Main proof (sigma*phi = n*tau) | theory/proofs/theorem-r1-uniqueness.md | Foundation theorem (Mk.III) |
| Mk.IV candidates analysis | theory/proofs/mk4-theorem-candidates-2026-04-14.md | 3-candidate comparison |
| Mk.IV final verdict | theory/proofs/mk4-trident-final-verdict-2026-04-15.md | sigma-tau=8 selected as Mk.IV |
| Golay code connection | theory/proofs/the-number-24.md | [24,12,8] = [sigma*phi, sigma, sigma-tau] |
| SM gauge decomposition | theory/proofs/standard-model-from-n6.md | 8+3+1=12 gauge identity |
| Honest limitations | theory/proofs/honest-limitations.md | Framework boundaries |
| Existing paper draft | papers/n6-mk4-theorem-candidates-paper.md | Internal paper (Korean, needs translation) |
| Pure math paper | papers/n6-pure-mathematics-paper.md | Broader pure math context |

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

