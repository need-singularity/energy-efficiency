---
id: millennium-v3-design
date: 2026-04-15
roadmap_task: HONEST-PX-3 (v3 roadmap realization)
grade: [10] design document
parent_roadmap: shared/roadmaps/millennium.json (v2.3)
license: CC-BY-SA-4.0
---

# Millennium 7-problem roadmap v3 — design (based on 7-loop v2.3 experience)

> **Summary**: after the v2.3 FULL_SATURATION declaration (saturation_round 14), the session-level 7 loops added empirical BSD (Cremona 964k) + arXiv 180 papers + BT-542 4 barriers + OUROBOROS R14 CLI. v3 absorbs this progress into formal phases + decomposes the DEFERRED scope still beyond the horizon (Sage / Lean4 / external coord) into executable stages.

---

## §0 Entry — motive for the v2.3 → v3 transition

### 0.1 Final state of v2.3 (2026-04-15 13:10 UTC)

| Item | v2.3 value |
|------|------------|
| total_tasks | 155 |
| done | 143 |
| partial | 5 |
| deferred | 7 |
| planned | 0 |
| phases_done | 4 (P0, P1, P3, P7) |
| phases_partial | 0 |
| saturation_index | 1.0 |
| saturation_round | R14 (0 new gaps) |
| BT drafts complete | 0/6 (honesty preserved) |

### 0.2 **New progress** from loops 1~7 of v2.3 (outside v2 scope)

| loop | task | output | atlas entries |
|------|------|--------|---------------|
| 1 | GALO-PX-2 | Cremona 332k Sel_6 empirical | 4 |
| 1 | GALO-PX-3 | Iwasawa mod 6 surrogate | 2 |
| 1 | HONEST-PX-AUTO-EMPIRICAL | LMFDB/Cremona pipeline | 0 |
| 2 | GALO-PX-1 | (A3) Modified Conjecture (A3') | 2 |
| 2 | MONOTONE-PX-1 | atlas drift monitor CLI | 0 |
| 3 | BARRIER-PX-1 | BT-542 4-barrier catalog | 2 |
| 4 | GALO-PX-4 | κ(B) asymptotic + σ(6)=12 empirical reached | 3 |
| 5 | NUM-PX-3 | arXiv 180-paper survey | 3 |
| 6 | HONEST-PX-2 | OUROBOROS R14 audit CLI | 2 |
| 7 | — | (this document HONEST-PX-3) | — |

**Cumulative**: 18 atlas entries, 11 breakthrough .md, 4 CLI tools, 964k Cremona measurements + 180 arXiv collected.

### 0.3 Why v3 is needed

Scope **missing** from v2.3 schema:
- (P) actual tool precision (Sage, Pari-GP, Lean4) — cost L, infrastructure
- (Q) external-mathematician collaboration (peer review, preprint submission) — cost M, multi-session
- (R) scale extension (Cremona 3M full DB, arXiv full-text, Cremona conductor 10⁷) — cost L, time
- (S) meta-verification depth (namespace-aware OUROBOROS, monotone-drift extension) — cost M

Rather than leaving these as deferred items in v2.3 PX, v3 **decomposes them into executable stages**.

---

## §1 v3 design principles

### 1.1 Honesty first

- **BT draft-claim ban**: v3 may end 0/6. Progression means catalog / empirical / tool improvement.
- **Explicit external dependencies**: Sage, Pari, Lean4, mathematician peers — all declared as **prerequisites** to enter v3.
- **Asymptotic claims banned**: forbid statements like "RH will be drafted by end of v3". Instead use operational goals such as "after v3 Phase N we can measure x".

### 1.2 3-track split

| Track | Content | cost sum | BT relevance |
|-------|---------|----------|--------------|
| **E (Empirical)** | measurement extension, precision tooling, scale-up | L+L+M | BT-541, 546 |
| **T (Theoretical)** | draft stages, 4-barrier bypass, Moonshine L5 | L+L+L | BT-542, 545 |
| **M (Meta)** | peer review, preprint, formal verification | M+L+M | all BTs |

### 1.3 Phase structure (v3 P0~PX)

v3 **preserves** v2.3's 16-axis × 13-phase structure and **adds new P-tier only**:

| v3 phase | Content | inherited from v2.3 | New |
|----------|---------|---------------------|-----|
| P0~P10 | v2.3 unchanged | done/partial kept | no change |
| PΩ | v2.3 unchanged | — | — |
| PX | v2.3 + loops 1-7 entries | 15 done | 18 done (loops 1-7) |
| **P11 (new)** | E track: Sage precision + scale-up | — | 7 tasks |
| **P12 (new)** | T track: theoretical deepening | — | 6 tasks |
| **P13 (new)** | M track: peer coord + preprint | — | 5 tasks |

---

## §2 v3 Phase 11 — E Empirical track (7 tasks)

### E1: Sage/Pari-GP install + integration

- **Goal**: enable the Python runner to call Sage/Pari locally
- **cost**: L (install ~2h + API learning ~1h)
- **Output**: `scripts/empirical/sage_wrapper.py` + usage doc
- **MISS condition**: Sage dep fails to build on Mac ARM
- **DEFERRED rationale**: cannot run within a v2.3 loop (session-isolated)

### E2: Precise Cremona |Sel_n(E)| recomputation

- **Goal**: replace v2.3 GALO-PX-2 first-order approximation with precise |Sel_2|, |Sel_3|
- **cost**: L (Sage `E.selmer_group(2)`, ...)
- **Output**: precise values for 332k curves → re-measured mean |Sel_6|
- **MISS condition**: Sage-computation timeout (expected 10 s+ per curve)

### E3: Precise Iwasawa μ_p

- **Goal**: GALO-PX-3 surrogate → precise Sage `E.iwasawa_invariants(p)`
- **cost**: L (Iwasawa takes a few seconds per curve)
- **Output**: precision-version atlas entry for MILL-GALO-PX3

### E4: Cremona 3M full-dataset collection

- **Goal**: bulk download all ecdata (~330 shards, 3M curves)
- **cost**: M (~2 GB, 1 hour)
- **Output**: complete data/cremona/allbsd/*

### E5: κ(B) 10+ bin asymptotic verification

- **Goal**: extend GALO-PX-4 3-bin → 10+ bins (conductor 1M, 2M, 5M, 10M, ...)
- **cost**: M (analysis after E4, ~30 min)
- **Output**: estimated asymptotic functional form of κ(B)

### E6: arXiv periodic-survey pipeline

- **Goal**: turn the NUM-PX-3 one-shot into a monthly auto-collection cron
- **cost**: M (GitHub Actions setup + script)
- **Output**: `.github/workflows/arxiv-quarterly.yml`

### E7: arXiv full-text download + topic clustering

- **Goal**: 180-paper abstracts → PDF fetch + NLP topic modeling
- **cost**: L (~1 GB PDF, ~1 day compute)
- **Output**: topic graph + deep keyword search for n=6

---

## §3 v3 Phase 12 — T Theoretical track (6 tasks)

### T1: BT-545 "Abelian Sixfolds" deep dive

- **Goal**: full-text analysis of arxiv:2603.20268 → connect with atlas MILL-PX-A11 (Enriques)
- **cost**: L (~1 week reading + writing)
- **Output**: `theory/breakthroughs/bt-545-abelian-sixfolds-connection-v3.md`

### T2: LATT-PX-1 Moonshine L5 retry

- **Goal**: v2.3 deferred. Explore a new approach to L5 (Monster action) in the 5-step V♮ construction
- **cost**: L (re-read Conway-Norton, Borcherds literature)
- **Output**: promote BT-18 to PARTIAL or retain honest MISS

### T3: Joint-distribution modeling for GALO-PX-4 (A3')

- **Goal**: estimate the mathematical form of κ(B) (power law? log?)
- **cost**: L (re-read BKLPR + fitting)
- **Output**: propose a new conjecture

### T4: BT-541 Guth-Maynard 2024 revisit

- **Goal**: implications of zeta-zero large-value improvement
- **cost**: L (preprint re-read)
- **Output**: atlas MILL-GUTH-MAYNARD-2024 entry

### T5: BT-542 meta-complexity deep dive

- **Goal**: reconfirm non-applicability of Hirahara 2022 MCSP to n=6
- **cost**: L
- **Output**: augment BARRIER-PX-1 document

### T6: BT-543 Balaban 2D reorganization

- **Goal**: modern re-organization of the Balaban 1980s continuum construction
- **cost**: L (substantial volume)
- **Output**: survey, MISS possible

---

## §4 v3 Phase 13 — M Meta track (5 tasks)

### M1: preprint submission (1+ item)

- **Goal**: of the loop 1~7 breakthrough .md files, submit the strongest to arXiv as a preprint
- **cost**: M (formatting + submit + 3-day review)
- **Candidates**:
  - `bsd-kappa-asymptotic-964k-2026-04-15.md` (loop 4)
  - `arxiv-millennium-survey-180papers-2026-04-15.md` (loop 6, meta-survey)
- **MISS condition**: arXiv moderation rejects

### M2: invite 3 mathematicians to review

- **Goal**: HONEST-PX-5 = peer-review pipeline. Email template + target list
- **cost**: M (selection + sending)
- **Targets**: BSD/BKLPR experts (Bhargava, Bhargava-Shankar, ...)
- **MISS condition**: no replies (expected as normal)

### M3: Lean4/Coq formalization exploration

- **Goal**: integrate HONEST-PX-4 + FORMAL-P3-1 + FORMAL-PX-1 (3 tasks)
- **cost**: L (2~3 weeks Lean4 study)
- **Output**: attempt Lean4 draft of MILL-PX-A1 Theorem B (σφ = nτ iff n=6)

### M4: HONEST-PX-EXT-AUDIT

- **Goal**: external-audit pipeline — accept external contributions via GitHub PR
- **cost**: M (draft CONTRIBUTING.md + issue templates)
- **Output**: repository infrastructure

### M5: OUROBOROS 2.0 — namespace-aware severity

- **Goal**: improvement based on loop 7
- **cost**: M (extend existing CLI)
- **Output**: scripts/monotone/ouroboros_detector_v2.py

---

## §5 v3 transition conditions (v2.3 → v3)

### 5.1 **MANDATORY** (must be met before official v3 start)

- [ ] at least 3 of v2.3's 7 deferred items have their "v3 Phase placement" complete → see §2-4
- [ ] re-verify the 18 atlas entries from v2.3 loops 1~7 (R14 CLEAN fixed 2026-04-15)
- [ ] monotone-drift check (register baseline via MONOTONE-PX-1 CLI)
- [ ] reconfirm BT drafts complete 0/6 (honesty declaration before v3 start)

### 5.2 **RECOMMENDED** (suggested before v3 start)

- [ ] attempt Sage environment setup (E1)
- [ ] prototype arXiv monthly pipeline (E6)
- [ ] start Lean4 learning (M3 prep)
- [ ] draft 1 preprint (M1 prep)

### 5.3 v3 official-start declaration

All 4 items in §5.1 complete + explicit user "go v3" → promote millennium.json schema_version to "3.0".

---

## §6 v3 honesty charter

### 6.1 4 principles

1. **BT draft-claim ban**: at no point in v3 may one claim e.g. "RH drafted".
2. **Expose external dependencies**: v3 work depends on Sage / Lean4 / arXiv API / external mathematicians. These dependencies will not be hidden but explicitly stated.
3. **Declare MISS conditions in advance**: every task specifies exact MISS criteria (v2.3 principle continues).
4. **Periodic OUROBOROS audit**: run OUROBOROS CLI at the end of every v3 phase and confirm R14 CLEAN.

### 6.2 v3 audit checklist (end of each phase)

```
[ ] N new atlas entries, each with external source cited
[ ] OUROBOROS R14 CLEAN (MILL-*, BT-*)
[ ] drift-monotone check (0 downgrades)
[ ] reconfirm BT drafts complete 0/6
[ ] peer-review request status updated
```

---

## §7 Related files

- `shared/roadmaps/millennium.json` (v2.3, parent)
- `reports/breakthroughs/bsd-cremona-sel6-empirical-2026-04-15.md` (loop 1)
- `reports/breakthroughs/bsd-A3-modified-with-joint-covariance-2026-04-15.md` (loop 2)
- `reports/breakthroughs/bsd-kappa-asymptotic-964k-2026-04-15.md` (loop 4)
- `reports/breakthroughs/bt-542-p-vs-np-4-barriers-survey-2026-04-15.md` (loop 3)
- `reports/breakthroughs/arxiv-millennium-survey-180papers-2026-04-15.md` (loop 5)
- `reports/breakthroughs/ouroboros-atlas-audit-2026-04-15.md` (loop 6)
- `scripts/empirical/*.py` (5 files)
- `scripts/monotone/*.py` (2 files)

---

## §8 atlas entry proposal

```
@R MILL-HONEST-PX3-v3-design-published = v3 roadmap design doc (based on 7-loop experience, 3-track 18 tasks) :: n6atlas [10]
  "HONEST-PX-3 v3 roadmap realization (2026-04-15 loop 8): absorbs session loop 1~7 progress after v2.3 FULL_SATURATION.
   3-track (E Empirical 7 / T Theoretical 6 / M Meta 5) = 18 new tasks. v2.3 → v3 transition has 4 MANDATORY
   + 4 RECOMMENDED conditions. Honesty charter states 4 principles (BT-draft-claim ban, expose external deps, MISS pre-declare, periodic OUROBOROS).
   BT drafts complete 0/6 retained honestly — v3 targets tool + catalog improvement, not a product"
```

---

*Written: 2026-04-15 loop 8*
*Path: theory/roadmap-v2/millennium-v3-design-2026-04-15.md*
*Next step: on user approval, officially start v3 + promote millennium.json schema_version to 3.0*
