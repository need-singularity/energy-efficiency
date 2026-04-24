---
id: millennium-v4-design
date: 2026-04-16
roadmap_task: v4 official start (user "go v4")
grade: [10] design document
parent_roadmap: shared/roadmaps/millennium.json (v3.0)
license: CC-BY-SA-4.0
---

# Millennium v4 — design (2026-04-16, user-approved "go v4")

> **Summary**: from v3's SATURATION_ADJACENT state (14/18 done, 4 external-blocked), the user approved "go v4". v4 (1) includes the **4 v3 carry-over tasks** as explicit scope, (2) extends **depth** (theoretical derivation of α = log(2)/4, explicit Umbral VOA, Mathlib migration), (3) extends **scale** (Cremona 3M full, κ 50-bin). Inheriting v2.3's FULL_SATURATION and v3's SATURATION_ADJACENT experience, v4 **inherits the 4-principle honesty charter + v3 + honesty charter**. Assumes BT drafts complete 0/6 honestly.

---

## §0 Entry — context for the v3 → v4 transition

### 0.1 v3 final state

| Item | Value |
|------|-------|
| v3 tasks done | 14/18 (78%) |
| Blocked tasks | 4 (E2, E3, E7, M2) all external |
| v3 unique findings | α ≈ log(2)/4 CONSISTENT, (A3″) conj, Pari/Lean4 toolchain |
| BT drafts complete | 0/6 honesty preserved |
| v2.3 → v3 loops | 11 loops (loops 12-22 of 2026-04-15~16) |

### 0.2 Why v4 is needed

**v3 carry-over (required)**:
- E2: per-curve |Sel_3|, |Sel_6| (Sage-dependent)
- E3: Iwasawa μ_p
- E7: arXiv full-text + NLP
- M2: external-mathematician contact

**v3 implications (new needs)**:
1. α = log(2)/4 **lacks theoretical derivation** — requires T-track depth
2. Bootstrap σ = 0.022 → requires **bin scale-up** (E4_v4)
3. Lean4 [2, 20] decide → requires **Mathlib migration** (M3_v4 deep)
4. Umbral Moonshine heuristic → requires **explicit construction** (T2 depth)

### 0.3 Distinction between v4 and v3

| Axis | v3 | v4 |
|------|----|----|
| Scope | wide (18 tasks, 3 tracks) | deep (17 tasks, 3 tracks) |
| Focus | theoretical survey + tool bootstrap | derivation + scale + rigor |
| BT goal | honest MISS catalog | honest MISS preserved + concretized |
| External deps | carried-over + blocked | explicit handles (e.g. remote compute) |

---

## §1 v4 design principles

### 1.1 Honesty charter V4 (inherited + strengthened)

Inherits all 4 v3-charter principles + adds:

1. **BT-draft-claim ban** — inherited
2. **Expose external deps** — inherited + **strengthened**: pre-declare per-task external deps
3. **Pre-declare MISS conditions** — inherited
4. **Periodic OUROBOROS audit** — inherited
5. **v4 new**: **public progress on carry-over tasks** — periodically update their external-resolution state in atlas

### 1.2 v4 3-track split

| Track | Content | vs v3 | BT relevance |
|-------|---------|-------|--------------|
| **E (Empirical)** | 7 tasks: 3 carry-over + 4 new | scale + precision | BT-541, 546 |
| **T (Theoretical)** | 5 tasks: α derivation + Umbral + expansion | adds draft attempts | BT-545, 18 |
| **M (Meta)** | 5 tasks: 1 carry-over + Mathlib + preprint revision | Lean4 formal reinforced | all BTs |

---

## §2 v4 Phase 14 — E Empirical track (7 tasks)

### E1_v4 (carry-over v3 E2): precise |Sel_n(E)| per-curve

- **Goal**: carry over v3 E2. Per-curve over some of the 330 shards via Sage or remote compute
- **cost**: L (remote) or DEFERRED
- **external**: Sage ARM build or remote Sage server
- **Output**: `data/cremona/per_curve_sel/<shard>.json`

### E2_v4 (carry-over v3 E3): precise Iwasawa μ_p

- **Goal**: carry over v3 E3. Sage `E.iwasawa_invariants(p)` per curve
- **external**: Sage
- **Output**: precision values for atlas MILL-V3-E3

### E3_v4 (carry-over v3 E7): arXiv full-text + NLP

- **Goal**: 180-paper abstracts → PDF + NLP topic clustering
- **cost**: L (1 GB + ~1 day compute)
- **external**: arXiv PDF API
- **Output**: topic-cluster graph + deep keyword sweep for n=6

### E4_v4 (new): κ(B) 50+ bin refinement

- **Goal**: v3 E5 7 bins → 50 bins (bin width 10k, up to 500k)
- **cost**: M
- **Dependency**: requires all 330 shards (depends on E5_v4)
- **Output**: expect α uncertainty 0.022 → 0.005

### E5_v4 (new): Cremona 3M full (330 shards)

- **Goal**: v3 E4 27 shards 1.7M → full 330 shards 3M+ curves
- **cost**: M (~2 GB download + ~1 hour)
- **external**: Cremona ecdata mirror
- **Output**: complete data/cremona/allbsd/*

### E6_v4 (new): compare σφ vs nτ at other n

- **Goal**: do similar bin analyses for n = 4, 8, 12, 30 → statistical evaluation of **uniqueness** of n = 6
- **cost**: M
- **Output**: atlas MILL-V4-E6 multi-n baseline

### E7_v4 (new): per-curve η(E) distribution survey

- **Goal**: measure η(E) defined in v3 T3 (A3″) per curve — per-curve |Sel_6| / (|Sel_2| · |Sel_3|) − 1
- **cost**: L (depends on E1_v4 output)
- **Output**: η distribution histogram + direct observation of B dependence

---

## §3 v4 Phase 15 — T Theoretical track (5 tasks)

### T1_v4 (new): attempt to derive α = log(2)/4 from BKLPR theory

- **Goal**: turn v3 T3's empirical finding into a derivation inside BKLPR cokernel math
- **cost**: L (re-read Bhargava-Kane 2013 + fitting)
- **Output**: conditional draft or honest MISS
- **MISS probability**: 70% (per v3 experience)

### T2_v4 (new): explicit Umbral Moonshine A_2^12 / A_5^4 D_4

- **Goal**: explicit VOA construction from Cheng-Duncan-Harvey 2014 + DFR 2017
- **cost**: L (literature comprehension + execution)
- **Output**: explicit character tables of VOA modules

### T3_v4 (new): full-text analysis of Abelian Sixfolds

- **Goal**: fetch arXiv:2603.20268 full-text + reconfirm exact results
- **cost**: M (arXiv PDF fetch + re-read)
- **Output**: correction or confirmation of v3 T1 heuristic

### T4_v4 (new): rigorize the (A3″) formulation

- **Goal**: strengthen mathematical rigor of the v3 T3 conjecture statement
- **cost**: M
- **Output**: formal conjecture + predictions

### T5_v4 (new): 6-problem cross-BT survey

- **Goal**: extend v3 T4-T6 to the remaining BT-18, 544, 547 (Hodge non-abelian, NS Reg)
- **cost**: L
- **Output**: 5 survey .md files

---

## §4 v4 Phase 16 — M Meta track (5 tasks)

### M1_v4 (carry-over v3 M2): external-mathematician contact

- **Goal**: carry over v3 M2. Executed after user direction
- **external**: user direction
- **status**: still DEFERRED (no autonomous proposal)

### M2_v4 (new): Lean4 Mathlib integration

- **Goal**: add Mathlib dep to lean4-n6/ → switch to Nat.sigma, Nat.totient
- **cost**: L (Mathlib 3 GB download + compile ~1 hour)
- **Output**: N6/MathlibBasic.lean, faster decide execution

### M3_v4 (new): attempt Theorem-B algebraic-path 1 draft

- **Goal**: turn σφ = nτ iff n = 6 algebraic (multiplicative-function) path into Lean4
- **cost**: L (weeks of work; at v4 start, skeleton only)
- **Output**: N6/TheoremB_Algebraic.lean — partial or complete

### M4_v4 (new): preprint v0.2 revision

- **Goal**: fold v3 M1 draft + bootstrap result + T1_v4 (α-derivation attempt) into the preprint
- **cost**: M
- **Output**: theory/preprints/millennium-v4-preprint-draft-YYYY-MM-DD.md

### M5_v4 (new): OUROBOROS v3 semantic similarity

- **Goal**: extend v3 M5 namespace-aware → add semantic clustering (embed-based similarity)
- **cost**: M (local embed model or API)
- **Output**: scripts/monotone/ouroboros_detector_v3.py

---

## §5 v4 transition conditions + end conditions

### 5.1 v4 official start (in this session)

- ✓ user "go v4" explicit (2026-04-16)
- ✓ v3 SATURATION_ADJACENT declared
- ✓ 4 carry-over tasks explicitly included in scope
- ✓ millennium.json schema_version promoted to 4.0

### 5.2 v4 end condition (saturation)

v4 ends in one of:
- **FULL_SATURATION**: all 17 tasks done (including carry-overs, assuming externals resolve)
- **SATURATION_ADJACENT_V4**: all internally executable work exhausted, only external blocks remain (similar to v3)
- **user "go v5"**: conscious transition

### 5.3 Expected v4 loop count

v3 ran in 11 loops (loops 12-22). v4 is more **depth**-oriented so per-task time may be longer. Estimate 15-20 loops.

---

## §6 v4 honesty charter V4

### 6.1 4+1 principles

1. **BT-draft-claim ban** (inherited)
2. **Expose external deps** (inherited, strengthened)
3. **Pre-declare MISS conditions** (inherited)
4. **Periodic OUROBOROS audit** (inherited)
5. **Public progress on carry-over tasks** (v4 new): record external-resolution state in atlas entries

### 6.2 v4 audit checklist (end of each phase)

```
[ ] N new atlas entries, each with external source/dep cited
[ ] OUROBOROS R14 CLEAN (MILL-*, BT-*)
[ ] monotone-drift check
[ ] reconfirm BT drafts complete 0/6
[ ] update carry-over-task state (v3 E2, E3, E7, M2 = M1_v4)
[ ] v4-specific invariant: "public state of external deps on v3 carry-over tasks"
```

---

## §7 Plan for the first v4 loop

### 7.1 Loop 1 (this session)

- **T1_v4 attempt**: BKLPR theoretical derivation of α = log(2)/4
- **Method**: Bhargava-Kane 2013 cokernel theorem + try natural emergence of τ(6) = 4
- **Expected outcome**: partial analysis + MISS or conditional step

### 7.2 Loops 2~5

- M2_v4: install Mathlib + convert 1 lemma
- E5_v4: attempt full-download of Cremona 3M
- T2_v4: character table of 1 Umbral A_2^12 module

---

## §8 Related files

- **v3 design**: `theory/roadmap-v2/millennium-v3-design-2026-04-15.md`
- **v3 saturation**: `reports/breakthroughs/v3-saturation-adjacent-2026-04-16.md`
- **v3 T3 (A3″)**: `reports/breakthroughs/v3-t3-joint-distribution-modeling-2026-04-15.md`
- **v3 loop-19 bootstrap**: `reports/breakthroughs/v3-loop19-lean4-extended-kappa-bootstrap-2026-04-16.md`
- **Pari wrapper**: `scripts/empirical/pari_wrapper.py`
- **Lean4**: `lean4-n6/`
- **roadmap**: `shared/roadmaps/millennium.json` → `_v4_meta` + `_v4_phases`

---

*Written: 2026-04-16 loop 20 (v4 design doc)*
*Honesty charter: retain BT drafts complete 0/6. Expose external deps on v3's 4 carry-over tasks. v4 also targets tool + catalog + depth, not a finished product.*
