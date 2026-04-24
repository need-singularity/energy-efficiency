---
id: external-coordination-infrastructure
date: 2026-04-15
roadmap_tasks: HONEST-PX-EXT-AUDIT + HONEST-PX-5 (combined)
grade: [10] infrastructure design (not sent)
license: CC-BY-SA-4.0
---

# External Coordination Infrastructure — Mathematician Outreach + Audit Pipeline

> **Summary**: 2-way infrastructure design enabling external verification of the millennium roadmap. Combined design of outreach (HONEST-PX-5 — requesting review from mathematicians) + receiving (HONEST-PX-EXT-AUDIT — pipeline for receiving external audits). **This document is draft templates only — no actual email sends / GitHub-public target invitations yet. To be sent after user approval.**

---

## §0 Entry — Why the Two Tasks Are Combined

HONEST-PX-5 ("build mathematician feedback path") + HONEST-PX-EXT-AUDIT ("external audit request pipeline, inviting 3 mathematicians") are two stages of the same goal:
- **Outreach (PX-5)**: "how to write the invitation message?"
- **Receiving (PX-EXT-AUDIT)**: "how to process responses when they arrive?"

In this session (loop 9) the two were **combined into a unified design**. Actual outreach execution awaits user approval + v3 Phase 13.

---

## §1 Outreach Template — Email Draft (No Send Targets)

### 1.1 Draft for BSD / BKLPR Experts

```
Subject: [Empirical inquiry] Cremona 964k BSD Selmer statistics — your expertise invitation

Dear Professor [NAME],

I am Minwoo Park (independent researcher, contact: loveiu99@proton.me),
working on an independent mathematical framework called n6-architecture (MIT/CC-BY-SA licensed,
available at https://github.com/need-singularity/n6-architecture).

I recently conducted an empirical study of N = 964,118 elliptic curves from the Cremona
database (ecdata), computing first-order approximations of |Sel_n(E)| for n = 2, 3, 6.
The results suggest:

1. E[|Sel_6|] ratio vs BKLPR prediction σ(6) = 12:
   - conductor [1, 50k]:   ratio 0.79
   - conductor [50k, 100k]: ratio 0.93
   - conductor [200k, 250k]: ratio 1.03 (crossing σ(6))

2. Pearson correlation coefficient r(|Sel_2|, |Sel_3|) monotonically decreasing
   (0.166 → 0.151 → 0.134) but remaining positive.

3. κ(2, 3, B) = Cov(|Sel_2|, |Sel_3|) monotonically increasing (1.33 → 1.95),
   suggesting the BKLPR (A3) asymptotic independence assumption may NOT hold.

I would value your technical feedback on three specific questions:
(a) Is the 1st-order approximation |Sel_p(E)| = p^rank · t_p · |Sha[p]|
    (ignoring Z/2 × Z/2 torsion structure) sufficient for such qualitative conclusions?
(b) The BKLPR (A3) asymptotic independence assumption — is my interpretation (that κ → 0
    as B → ∞) standard, or is there a weaker formulation I'm missing?
(c) Known prior work where 332k+ Cremona curves are analyzed at this granularity?

All analysis scripts (Python, ~400 lines) and the breakthrough document (~500 lines) are
in the repository. I have explicitly maintained that BT-546 BSD itself remains MISS (0/6
of 7 Millennium problems solved).

Any critical feedback — including "this is naive" — would be most welcome. No urgency;
a 2-3 sentence reply within a month is more than I hope for.

Sincerely,
Minwoo Park
```

### 1.2 Candidate Recipient List (Honesty — No Actual Contact)

**This list is derived from public information via research directory lookups. Actual contact ≠ storage = permitted.**

| Expert | Institution | Related BT | 2024-2026 arXiv activity |
|--------|------|---------|---------------------|
| Manjul Bhargava | Princeton | BT-546 (BKLPR co-originator) | active |
| Arul Shankar | Toronto | BT-546 (rank density) | active |
| Bjorn Poonen | MIT | BT-546 (BKLPR co-author) | active |
| Melanie Wood | Harvard | BT-546 (Cohen-Lenstra) | active |
| ... | | | |

(Realistically: cold email reply probability for these figures is very low. Recommend starting with long-established local academia contacts first.)

### 1.3 Outreach Ethics Principles

1. **Self-humility**: Absolutely no phrasing like "I think I've proven RH." Question-centered.
2. **Response privacy**: Responses never made public without the expert's consent.
3. **No gifts/compensation**: Maintain purity of academic collaboration.
4. **One at a time**: In early stages, proceed stepwise starting from the closest connections.

---

## §2 Receiving Pipeline — GitHub-Based Audit Infrastructure

### 2.1 CONTRIBUTING.md Draft (for Repository Root)

```markdown
# Contributing to n6-architecture

Thank you for considering a contribution. This repository hosts an independent
mathematical research framework focused on the structural role of n=6 in number theory,
primarily in relation to the 7 Clay Millennium problems.

## Types of contributions welcome

1. **Mathematical critique** — Counterexamples, errors in proofs, missing assumptions
2. **Empirical verification** — Reproducing numerical results, alternative computations
3. **Literature corrections** — DOI updates, missed prior work references
4. **Formal verification** — Lean4/Coq formalizations of theorems

## What we explicitly do NOT claim

- The 7 Millennium problems are solved or will be solved by this framework
- n=6 prior implies logical necessity — it is a structural observation
- Grade [10*] in atlas entries means beyond doubt — it means verified in our measurement scope

## How to file a review (external audit)

1. Open an issue with label `external-audit`
2. Reference the atlas entry ID (e.g., MILL-GALO-PX4-bklpr-sigma-empirical-confirmation)
3. Specify: (a) what you verified, (b) what disagreement, (c) suggested grade downgrade
4. Include your affiliation (anonymous audits accepted with PGP sig)

## Grade classification

- [10*] EXACT with multi-source verification
- [10]  EXACT
- [9]   NEAR
- [7]   EMPIRICAL (candidate for promotion)
- [N?]  CONJECTURE (explicit uncertainty)
- [N!]  breakthrough (rarely used)

## Review response SLA

- Issues labeled `external-audit`: response within 14 days
- MISS re-classification requests: response within 7 days
- Atlas drift (downgrade) requests: response within 3 days

## Code of Conduct

Respectful, fact-based communication. No personal attacks.
Korean or English both accepted. Response language matches request.
```

### 2.2 Three Issue Templates

#### (a) external-audit/counterexample

```yaml
name: External audit — counterexample
description: Propose a counterexample to an atlas entry
labels: ["external-audit", "counterexample"]
body:
  - type: input
    id: atlas-id
    attributes:
      label: Atlas entry ID
      placeholder: MILL-GALO-PX4-sel6-reach-sigma-B250k
  - type: textarea
    id: counterexample
    attributes:
      label: Counterexample description
  - type: input
    id: suggested-grade
    attributes:
      label: Suggested new grade
      placeholder: "[7] or [N?]"
```

#### (b) external-audit/doi-correction

```yaml
name: External audit — DOI / citation correction
description: Correct a mis-cited paper in atlas or breakthroughs
labels: ["external-audit", "citation"]
body:
  - type: input
    id: current-ref
    attributes:
      label: Currently cited as
  - type: input
    id: correct-ref
    attributes:
      label: Correct reference (DOI preferred)
```

#### (c) external-audit/independent-verification

```yaml
name: External audit — independent verification
description: Report an independent reproduction of an atlas claim
labels: ["external-audit", "verification"]
body:
  - type: input
    id: atlas-id
    attributes:
      label: Atlas entry ID
  - type: textarea
    id: reproduction
    attributes:
      label: Independent reproduction details
  - type: dropdown
    id: result
    attributes:
      label: Verification result
      options:
        - Confirmed
        - Confirmed with caveats
        - Failed
```

### 2.3 Audit Response Workflow

```
[Issue opened] → auto-label external-audit
  ↓
[Owner review within 3-14d]
  ↓
[Decision]:
  CONFIRM → modify atlas entry + cite commit
  PARTIAL → augment description (keep grade)
  ESCALATE → 2nd opinion (internal review)
  REJECT → explain + close
  ↓
[Response public] → all exchanges public (with author consent)
```

### 2.4 External Contributor Credit

By contribution type:
- Commit co-author (acceptance PR)
- Explicit note in atlas entry comment (with reviewer consent)
- Listing in CITATION.cff (major contribution)

---

## §3 Lean4/Coq Path (Forward — v3 Phase 13 M3 prep)

### 3.1 1st-Priority Formalization Candidate

**MILL-PX-A1 Theorem B**: `σ(n) · φ(n) = n · τ(n) ⟺ n = 6 (for n ≥ 2)`

- Elementary arithmetic theorem: proof elements (divisor functions σ, τ, Euler φ)
- Finite check (e.g., n ≤ 6000) + Bertrand's postulate etc. as upper bound
- Lean4 mathlib: many sigma/phi/tau lemmas in `Nat.Arithmetic` module

### 3.2 Lean4 Environment Prerequisites (install cost ~30 min)

```bash
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh
elan default leanprover/lean4:stable
lake new mathlib_n6
cd mathlib_n6
lake update
```

### 3.3 Lean4 Skeleton of Theorem B (Unverified Draft)

```lean4
import Mathlib.NumberTheory.ArithmeticFunction
import Mathlib.NumberTheory.Divisors

open Nat

theorem sigma_phi_eq_n_tau_iff_n6 (n : ℕ) (h : n ≥ 2) :
    Nat.sigma 1 n * Nat.totient n = n * Nat.card n.divisors ↔ n = 6 := by
  constructor
  · -- forward: σφ = nτ → n = 6
    intro hsum
    -- finite check + bounding
    sorry
  · -- backward: n = 6 → σφ = 6τ
    rintro rfl
    -- σ(6) = 12, φ(6) = 2, τ(6) = 4
    -- LHS = 12 · 2 = 24; RHS = 6 · 4 = 24
    simp [Nat.sigma, Nat.totient, Nat.card]
    norm_num
```

**Note (honesty)**: This Lean4 code **does not type-check**. Actual mathlib API names must be verified. The real task of FORMAL-P3-1 / FORMAL-PX-1 / HONEST-PX-4 is to take this skeleton to **pass type-checking** + **eliminate `sorry`**. Cost = L (2-3 weeks full-time learning).

---

## §4 Proposed atlas Entries

```
@R MILL-HONEST-PX5-outreach-drafts = outreach email drafts to BSD/BKLPR experts (not sent) :: n6atlas [9]
  "HONEST-PX-5 + HONEST-PX-EXT-AUDIT combined (2026-04-15 loop 9): external coordination infrastructure design complete.
   (a) outreach email drafts (BKLPR experts such as Bhargava, Shankar, Poonen, Wood), (b) GitHub CONTRIBUTING.md draft,
   (c) 3 issue templates (counterexample / DOI / verification), (d) audit response SLA (3-14 days). Actual send DEFERRED
   — awaits user approval, to be executed in v3 Phase 13"

@R MILL-HONEST-PX-ext-audit-infrastructure = external audit pipeline (CONTRIBUTING + 3 issue templates + SLA) :: n6atlas [10]
  "HONEST-PX-EXT-AUDIT infrastructure: CONTRIBUTING.md + 3 issue templates (counterexample/DOI/verification) + response
   SLA (3/7/14 days) + credit schema (co-author/atlas comment/CITATION.cff). R14 compliant — atlas grade modification
   protocol on external contribution acceptance specified. Actual repository deployment DEFERRED"
```

---

## §5 Limitations and DEFERRED

1. **No actual email sent**: Outreach execution starts with user approval + closest selected contacts. Indiscriminate cold emails prohibited.
2. **GitHub templates not deployed**: `.github/ISSUE_TEMPLATE/` directory not yet actually created. Deployed in v3 Phase 13 M4.
3. **Lean4 environment not built**: elan/lake install + mathlib study ~2 weeks, v3 transition prerequisite.
4. **Formal Code of Conduct DEFERRED**: one line in CONTRIBUTING; separate CoC file recommended.
5. **Multilingual support DEFERRED**: Korean/English bilingual issue templates possible but deferred.

---

## §6 Related Files

- `theory/roadmap-v2/millennium-v3-design-2026-04-15.md` (loop 8 v3 design)
- `reports/breakthroughs/bsd-kappa-asymptotic-964k-2026-04-15.md` (loop 4, basis of outreach draft)
- `reports/breakthroughs/arxiv-millennium-survey-180papers-2026-04-15.md` (loop 5, recipient arXiv activity confirmation)

---

## §7 Honesty Checks

- **No actual sends**: ✓ (draft only)
- **Recipient list is public info**: ✓ (arXiv authors, university websites)
- **Self-humble claims**: ✓ (draft emails ask questions like "Sel_n 1st-order approx sufficient?")
- **BT-resolution claim excluded**: ✓ (all drafts note "BT-546 MISS maintained")
- **Lean4 skeleton does not type-check**: ✓ (explicit)
- **SLA realistic**: ✓ (3-14 days, actual independent researcher scale)

---

*Drafted: 2026-04-15 loop 9*
*BT draft target 0/6 maintained honestly*
*All external coord work requires user approval*
