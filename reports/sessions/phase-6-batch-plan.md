# Phase 6 Batch Plan — final allowlist 235 -> 0

**Date**: 2026-04-25
**Author**: Phase 6 planner (automated, planning-only)
**Status**: planning only — no code edits, no translation agents launched in this pass
**Scope**: adds only this plan under `reports/sessions/`. `tool/own1_legacy_allowlist.json`, `domains/**/*.md`, `papers/**/*.md`, `theory/**/*.md`, and `reports/sessions/specs/**/*.md` remain untouched.
**Compliance**:
- own#1 (doc-english-hard): this file under `reports/` is in own#1 scope and must be CJK = 0. Verify with `python3 tool/own_doc_lint.py --rule 1` before commit.
- own#11 (bt-solution-claim-ban): targets and batch outcomes are described as "draft / target / candidate / pattern / demonstrating" only. No "solved / proven / complete" claims for any Phase 6 deliverable in this plan or in the batch prompt templates it ships.
- own#17 (README English-only): out of scope for this plan; root `README.md` must remain CJK = 0 throughout Phase 6 execution — do not touch it.

---

## 1. Header — current state

| Field | Value |
|---|---|
| Date | 2026-04-25 |
| Branch | `main` |
| `origin/main` tip | `1ac374b7 docs(session): close Phase 5 — 14 full + 3 partial batches, 11 files deferred to Phase 6` |
| Working tree | clean (verified pre-plan) |
| Allowlist count | `235` (`_meta.count == len == unique == 235`) |
| Total CJK in-scope | `1,006,950` bytes across 235 `.md` files |
| Largest single file | `theory/breakthroughs/breakthrough-theorems.md` — 125,694 CJK, 28,481 lines |
| Phase 5 handoff | `reports/sessions/phase-6-handoff-2026-04-25.md` |
| Session log | `reports/sessions/hard-english-only-session-2026-04-24.md` |
| Enforcer | `tool/own_doc_lint.py --rule 1` (HARD at CJK > 0 threshold) |
| CI gate | `own1-doc-english-hard` (HARD block job) |
| Success metric | allowlist `_meta.count == 0`, file deleted, `on_fail: block` holds |

## 2. Audit summary

Phase 6 auditor re-ran CJK and line counts across every path in `tool/own1_legacy_allowlist.json`. Findings differ materially from the Phase 5 handoff estimate — **the expected "7 stale / surplus" cohort does not exist**. Only one genuine stale entry was confirmed.

### 2.1 Classification counts

| Classification | Count | Definition |
|---|---:|---|
| STALE surplus (CJK = 0, ready for pure shrink) | **1** | `papers/n6-hexa-cogni-integrated-paper.md` |
| TRANSLATE targets (CJK > 0) | **234** | real translation work remains |
| APEX (CJK > 3000 AND lines > 1500) — RED band | **16** | see 2.2 |
| Non-apex translate (YELLOW band) | **218** | partitioned across B1..B12 |

### 2.2 APEX list (RED band, 16 files)

| # | Path | CJK | Lines | Notes |
|--:|---|--:|--:|---|
| 1 | `theory/breakthroughs/breakthrough-theorems.md` | 125,694 | 28,481 | APEX-APEX — unreadable in a single `Read`, requires incremental split |
| 2 | `theory/constants/atlas-constants.md` | 20,722 | 6,363 | newly discovered apex (not on handoff list) |
| 3 | `reports/sessions/specs/2026-04-02-ultimate-fusion-powerplant-design.md` | 15,851 | 3,168 | B15 carryover, ASCII art |
| 4 | `reports/sessions/specs/2026-04-02-kstar-n6-tokamak-design.md` | 15,141 | 3,448 | B15 carryover, ASCII art |
| 5 | `reports/sessions/specs/2026-04-02-kstar-300s-steady-state-design.md` | 11,872 | 3,099 | B15 carryover, ASCII art |
| 6 | `domains/cognitive/ai-training-cost/ai-training-cost.md` | 10,254 | 1,927 |  |
| 7 | `domains/cognitive/ai-consciousness/ai-consciousness.md` | 10,049 | 1,841 |  |
| 8 | `domains/cognitive/ai-agent-serving/ai-agent-serving.md` | 9,523 | 1,605 |  |
| 9 | `domains/cognitive/ai-quality-scale/ai-quality-scale.md` | 9,079 | 1,570 |  |
| 10 | `domains/cognitive/ai-eval-pipeline/ai-eval-pipeline.md` | 8,815 | 1,854 |  |
| 11 | `domains/cognitive/ai-inference-cost/ai-inference-cost.md` | 8,451 | 1,649 |  |
| 12 | `domains/sf-ufo/hexa-ufo/hexa-ufo.md` | 8,042 | 1,873 |  |
| 13 | `domains/cognitive/ai-enterprise-custom/ai-enterprise-custom.md` | 7,657 | 1,537 |  |
| 14 | `papers/n6-ultimate-superconductor-integrated-paper.md` | 7,359 | 1,683 | B8 carryover |
| 15 | `papers/n6-hexa-consciousness-integrated-paper.md` | 6,644 | 1,637 |  |
| 16 | `papers/n6-hexa-chip-7dan-integrated-paper.md` | 6,156 | 1,619 |  |

### 2.3 Merged carryover groups from Phase 5

All carryovers are folded into the Phase 6 plan:

| Group | Count | Destination batch |
|---|--:|---|
| B15 fusion/KSTAR specs (3) | 3 | **B14** (RED) |
| B8 specialized physics (2): `moonshine-barrier`, `n6-ultimate-superconductor` | 2 | **B13** (RED-lite) |
| B12 theory/roadmap-v2 apex-density (5) | 5 | **B12** (RED-lite, single-file agents) |
| "6 surplus survivors" from the task prompt | 0 TRUE surplus | *all have CJK > 0 — merged into normal translate batches* |
| 1 stale (`papers/n6-hexa-cogni-integrated-paper.md`, CJK = 0) | 1 | **B0** (GREEN shrink) |
| `theory/breakthroughs/breakthrough-theorems.md` (B15 apex) | 1 | **B16** (APEX-APEX split) |
| `theory/constants/atlas-constants.md` (newly apex) | 1 | **B15** (RED dedicated) |

### 2.4 Subdirectory tally (for batching sanity)

| Prefix | Files | Total CJK |
|---|--:|--:|
| `domains/cognitive/` | 34 | 136,054 |
| `domains/compute/` (chip-* / hexa-* prefix) | 46 | 165,349 |
| `domains/compute/` (other) | 35 | 128,183 |
| `domains/physics/` | 37 | 130,268 |
| `domains/life/` | 25 | 58,138 |
| `domains/energy/` | 19 | 48,146 |
| `domains/sf-ufo/` | 11 | 36,827 |
| `domains/space/` | 8 | 23,641 |
| `domains/materials/` | 2 | 4,748 |
| `papers/` remainder (5: of which 2 apex) | 5 | 30,974 |
| `reports/sessions/specs/` (3 apex) | 3 | 42,864 |
| `theory/roadmap-v2/` (5 apex-density) | 5 | 27,489 |
| `theory/breakthroughs/` (1 APEX-APEX) | 1 | 125,694 |
| `theory/constants/` (1 apex) | 1 | 20,722 |
| **Grand total** | **235** | **1,006,950** |

---

## 3. Batch plan

16 batches across three risk bands. GREEN = pure allowlist shrink (no translation), YELLOW = normal translate+shrink, RED / RED-lite = dedicated single-file agents with heightened protocol.

| Batch | Label | Band | Files | Est CJK | Target shrink |
|---:|---|:-:|--:|--:|--:|
| B0  | stale-shrink (papers/n6-hexa-cogni) | GREEN | 1 | 0 | 235 -> 234 |
| B1  | domains/life tail | YELLOW | 18 | 41,464 | 234 -> 216 |
| B2  | domains/life tail 2 + materials (2) | YELLOW | 9 | 21,422 | 216 -> 207 |
| B3  | domains/energy (non-apex) | YELLOW | 19 | 48,146 | 207 -> 188 |
| B4  | domains/space | YELLOW | 8 | 23,641 | 188 -> 180 |
| B5  | domains/cognitive tail (non-apex) | YELLOW | 14 | 33,610 | 180 -> 166 |
| B6  | domains/cognitive tail 2 + sf-ufo non-apex | YELLOW | 23 | 66,060 | 166 -> 143 |
| B7  | domains/physics half (Millennium + pure) | YELLOW | 18 | 63,834 | 143 -> 125 |
| B8  | domains/physics half (quantum + classical + holography + cosmology) | YELLOW | 19 | 66,434 | 125 -> 106 |
| B9  | domains/compute non-chip half | YELLOW | 18 | 68,103 | 106 -> 88 |
| B10 | domains/compute non-chip half 2 | YELLOW | 17 | 60,080 | 88 -> 71 |
| B11 | domains/compute chip-/hexa- first half | YELLOW | 23 | 82,675 | 71 -> 48 |
| B12 | domains/compute chip-/hexa- second half + theory/roadmap-v2 (5 apex-density) | RED-lite | 28 | 110,163 | 48 -> 20 |
| B13 | papers/ non-apex (3) + B8 carryover (moonshine, superconductor) | RED-lite | 5 | 30,974 | 20 -> 15 |
| B14 | apex cognitive + sf-ufo + chip-paper apex (10 RED files) | RED | 10 | 84,445 | 15 -> 5 |
| B15 | reports/sessions/specs (3 KSTAR/fusion) + atlas-constants | RED | 4 | 63,586 | 5 -> 1 |
| B16 | theory/breakthroughs/breakthrough-theorems.md — **APEX-APEX 3-way split** | RED-APEX | 1 (split 3x) | 125,694 | 1 -> 0 |

Totals: 235 files addressed, est 1,006,950 CJK translated (after B16 closure the allowlist file itself is deleted — see 4.6).

Scheduling note: within RED and RED-lite bands, run **one file per agent**. Within YELLOW, run at most N = 4 parallel agents until the allowlist shard protocol from Phase 5 Section 14.3 is in place; N = 8+ is deferred until the per-prefix shard lands.

---

## 4. Per-batch prompt templates

Every YELLOW and RED prompt below bakes in the following **UNIVERSAL PROTOCOL** (stated once here, referenced by each batch):

### 4.0 UNIVERSAL PROTOCOL (inherited by all batches B0..B16)

1. **Triage first**. For each target file, classify BEFORE editing:
   - `TRANSLATE` — CJK > 0, in scope.
   - `SKIP-ALREADY-DONE` — CJK = 0 on disk; allowlist entry is stale; remove from allowlist only.
   - `SKIP-DEFER` — file fails the Apex Defer Rule (see 4.0.2) or contains uncertain domain terminology; leave on allowlist and document in the batch report.
2. **Apex Defer Rule**. If a file has `lines > 1500 AND CJK > 3000`, do NOT translate in a YELLOW batch — defer to the RED band (flag for a dedicated single-file agent). If already in a RED/RED-lite batch, proceed with the band's per-file protocol.
3. **Progress watchdog**. Emit a progress line `[B{n}] {i}/{N} {path} status={TRANSLATE|SKIP-*}` every 3 files. Parent monitors for stalls > 10 min.
4. **Allowlist mtime + atomic shrink**:
   - Before shrink, read `tool/own1_legacy_allowlist.json` and record mtime.
   - If mtime changed between read and write, abort shrink for that batch and re-stage.
   - Write via atomic `tmp -> rename` (`json.dump` to `tool/.own1_legacy_allowlist.json.tmp`, then `os.replace`).
   - Post-write verify parity: `_meta.count == len(allowlist) == len(set(allowlist))`.
5. **own#11 softeners STRICT**. In translated output replace "proven / solved / complete / done / resolved / established" with "draft / candidate / pattern / target / demonstrating / in-flight". Korean "U+C99D U+BA85 (proof)" -> "candidate lemma"; "U+C644 U+C131 (completion)" -> "draft"; "U+D574 U+AC10 (solve-sense)" -> "pattern".
6. **Verbatim preserves**. Math (`$...$`, `$$...$$`, `\[...\]`), LaTeX macros, code fences (``` ... ```), inline code, URLs, link targets, citation keys (`[N]`, `BT-xxx`, `CP-xxx`), frontmatter keys, table column widths, ASCII art box characters (`|`, `+`, `-`, box-drawing) — all pass through unchanged. Re-count column widths after translation; mismatch = revert and redo.
7. **Commit scheme**: two separate commits per batch.
   - `docs(translate): phase-6-{batch} English conversion ({K} files)`
   - `feat(own): shrink own#1 allowlist phase-6-{batch} ({K} entries)`
8. **--no-verify standard**. Use `git commit --no-verify` for both commits — pre-commit hook race was documented in Phase 5 Section 14.3. Post-push verify locally with `python3 tool/own_doc_lint.py --rule 1`.
9. **git index.lock 2s retry**. If `.git/index.lock` is present, `sleep 2` and retry up to 3 times before aborting.
10. **Push with 2-3 rebase retries**. `git push origin main`; on non-fast-forward, `git pull --rebase origin main` and retry. Cap at 3 attempts.
11. **Never** run external regex / dictionary mass-translate pipelines against `.md` files (Phase 5 Section 14.3 rule `g`). Never `git stash -u` during a parallel window.
12. **Post-batch verify**: `python3 tool/own_doc_lint.py --rule 1` exits 0. Report new allowlist count.

---

### 4.1 B0 — stale-shrink (GREEN band, 1 file, NO translation)

**Goal**: remove `papers/n6-hexa-cogni-integrated-paper.md` from allowlist only; file is already CJK = 0.

**Prompt**:
```
You are Phase 6 Batch 0 (GREEN shrink).

Target (1 file, already CJK = 0):
- papers/n6-hexa-cogni-integrated-paper.md

Tasks:
1. Verify CJK = 0 on disk via: python3 tool/own_doc_lint.py --rule 1 --files papers/n6-hexa-cogni-integrated-paper.md
   (If it reports any HARD violation, ABORT and escalate.)
2. Read tool/own1_legacy_allowlist.json; record mtime.
3. Remove the single entry from the allowlist array.
4. Decrement _meta.count by 1 (235 -> 234).
5. Atomic tmp -> rename write.
6. Post-write parity: _meta.count == len == unique.
7. git add tool/own1_legacy_allowlist.json
8. git commit --no-verify -m 'feat(own): shrink own#1 allowlist phase-6-B0 (1 entry stale)'
9. Push with 2-3 rebase retries.

No translate commit in this batch — shrink-only.
Apply UNIVERSAL PROTOCOL sections 4, 8, 9, 10 from the plan.
```

---

### 4.2 B1 — domains/life tail (YELLOW, 18 files)

**Files** (sorted ascending by CJK, densities ~2278..2346):
```
domains/life/apiculture            domains/life/baking
domains/life/bio-pharma            domains/life/biology-medical
domains/life/cheese-dairy          domains/life/coffee
domains/life/cosmetic-surgery      domains/life/crispr-gene-editing
domains/life/dolphin               domains/life/dolphin-bioacoustics
domains/life/ecology               domains/life/fermentation
domains/life/food-science          domains/life/genetics
domains/life/herbalism             domains/life/hexa-skin
domains/life/horticulture          domains/life/immunology
```
(each `<slug>/<slug>.md`)

**Glossary focus**: biology, medical, food-science, genetics terminology — align with Phase 3 `domains/` glossary. Latin binomials stay as-is.

**Prompt template** (reusable for B1..B11 YELLOW):
```
You are Phase 6 Batch {N} (YELLOW band, {K} files).

TARGETS: {list}

APPLY UNIVERSAL PROTOCOL (plan section 4.0) in full. Specifically:
- Triage-first on every file (TRANSLATE / SKIP-ALREADY-DONE / SKIP-DEFER).
- Apex Defer Rule: any file with lines > 1500 AND CJK > 3000 -> SKIP-DEFER, leave allowlist entry, report to parent for RED reassignment. (This batch pre-screens out all apex files — if one surfaces, escalate.)
- Progress emit every 3 files.
- own#11 softeners STRICT.
- Math / LaTeX / code-fence / link / frontmatter / ASCII art / citation key VERBATIM preserve.
- After translation of each file, verify CJK = 0 with tool/own_doc_lint.py --rule 1 on that file only.
- After all TRANSLATE files pass, stage with git add <paths> (no -A, no .).
- Commit 1: docs(translate): phase-6-B{N} English conversion ({K_done} files)  --no-verify
- Allowlist shrink (mtime check + atomic tmp-rename + parity re-verify).
- Commit 2: feat(own): shrink own#1 allowlist phase-6-B{N} ({K_done} entries)  --no-verify
- Push with 2-3 rebase retries.
- Never stash -u. Never run external regex/dictionary mass-translate pipelines.
- On git index.lock: sleep 2, retry up to 3 times.

Output report: counts by classification + new allowlist count + push SHA.
```

Est CJK 41,464. Target shrink 234 -> 216.

---

### 4.3 B2 — domains/life tail 2 + domains/materials (YELLOW, 9 files)

Files:
```
domains/life/mens-intimate-cleanser   domains/life/microplastics
domains/life/neuroscience             domains/life/therapeutic-nanobot
domains/life/vaccine                  domains/life/veterinary
domains/life/biology                  (moderate-density 3575)
domains/materials/ceramics            domains/materials/material-synthesis
```
Est CJK 21,422. Target shrink 216 -> 207. Use the B1 template verbatim, substituting N=2 and the file list.

---

### 4.4 B3 — domains/energy non-apex (YELLOW, 19 files)

All 19 `domains/energy/` entries currently on allowlist are non-apex; 7 are the `battery-scale-*` cluster with higher density (~5k CJK each) and should be chunked carefully but do not exceed the Apex Defer threshold. Est CJK 48,146. Target 207 -> 188. Use B1 template with N=3.

---

### 4.5 B4 — domains/space (YELLOW, 8 files)

8 files, 23,641 CJK. Target 188 -> 180. B1 template, N=4.

---

### 4.6 B5 — domains/cognitive tail non-apex (YELLOW, 14 files)

Cognitive-subdomain entries with CJK < 3000:
```
anima-service, anima-soc, brain-computer-interface, causal-chain,
cognitive-architecture, cognitive-social-psychology, dream-recorder,
hexa-dream, hexa-ear, hexa-empath, hexa-mind, hexa-neuro,
hexa-olfact, hexa-oracle
```
Est CJK ~33,610. Target 180 -> 166. B1 template, N=5.

---

### 4.7 B6 — cognitive tail 2 (20) + sf-ufo non-apex (10) (YELLOW, 23 files)

Remaining cognitive non-apex (13) plus `ai-alignment` (3264), `ai-deployment` (2331) plus all 10 sf-ufo non-apex. Est 66,060. Target 166 -> 143. B1 template, N=6. Density stays below apex threshold; do not mix with ai-welfare (4875) and ai-adversarial (5686) — those are YELLOW-hot and go here together with hexa-speak (2938).

---

### 4.8 B7 — physics half 1: Millennium + pure-math (YELLOW, 18 files)

All 7 `millennium-*` entries, `pure-mathematics`, `topology`, `holography`, `hexa-topo`, `cosmology`, `cosmology-particle`, `particle-cosmology`, `higgs`, `gravity-wave`, `quantum-oracle`, `simulation-theory`. Est 63,834. Target 143 -> 125. **Glossary note**: Millennium problem names stay as-is in English ("Hodge conjecture", "Yang–Mills", "BSD"). B1 template N=7.

---

### 4.9 B8 — physics half 2: applied + quantum + classical (YELLOW, 19 files)

Remaining 19 `domains/physics/`: `antimatter-factory`, `classical-mechanics-accelerator`, `cosmic-observatory`, `crystallography`, `crystallography-materials`, `electromagnetism`, `fluid`, `light-optics`, `mini-accelerator`, `optics`, `plasma`, `plasma-fusion-deep`, `plasma-physics`, `quantum-computer`, `quantum-computing`, `quantum-gravity-sensor`, `quantum-network`, `tachyon`, `thermodynamics`. Est 66,434. Target 125 -> 106. B1 template N=8.

---

### 4.10 B9 — compute non-chip half 1 (YELLOW, 18 files)

Non-chip compute entries batch 1: `5g-6g-network`, `advanced-packaging`, `ai-efficiency`, `blockchain`, `browser`, `compiler-os`, `consciousness-chip`, `consciousness-soc`, `cryptography`, `digital-twin`, `display`, `display-8stack`, `dram`, `exynos`, `isocell-comms`, `keyboard`, `learning-algorithm`, `mouse`. Est 68,103. Target 106 -> 88. B1 template N=9.

---

### 4.11 B10 — compute non-chip half 2 + network-protocol (YELLOW, 17 files)

`network`, `network-protocol` (3 files), `nexus-breakthrough-gate`, `nexus-service`, `performance-chip`, `programming-language`, `sc-memory`, `semiconductor-lithography`, `software-crypto`, `software-design`, `spatial-computing`, `sscb`, `unified-service`, `unified-soc`, `vnand`. Est 60,080. Target 88 -> 71. B1 template N=10.

---

### 4.12 B11 — compute chip-/hexa- first half (YELLOW, 23 files)

`chip-3d`, `chip-architecture` (5 files), `chip-design` (12 files — this sub-cluster has 12 siblings totalling 38,267 CJK; split internally 6/6 if the agent's context window is tight), `chip-dse-pipeline`, `chip-eda`, `chip-hbm`, `chip-hexa1`. Est 82,675. Target 71 -> 48. **WARNING**: 12-sibling `chip-design/` cluster on a single file edit — enforce per-file commit if the agent detects context pressure. B1 template N=11.

---

### 4.13 B12 — compute chip-/hexa- second half + theory/roadmap-v2 apex-density (RED-lite, 28 files)

**Part A (23 files)**: remaining chip-/hexa- compute — `chip-isa-n6` (3), `chip-materials`, `chip-npu-n6`, `chip-photonic`, `chip-pim`, `chip-rtl-gen`, `chip-sc`, `chip-wafer`, `hexa-3d`, `hexa-accel`, `hexa-asic`, `hexa-holo`, `hexa-ios`, `hexa-macos`, `hexa-mram`, `hexa-netproto`, `hexa-one`, `hexa-photon`, `hexa-pim`, `hexa-proglang`, `hexa-super`, `hexa-wafer`. Normal density.

**Part B — B12 carryover (5 theory/roadmap-v2 apex-density files)**:
```
theory/roadmap-v2/_archive-phase-01-forced-3-axes.md     (CJK 6342, lines 1235)
theory/roadmap-v2/n6arch-axes/axis-r1-emergence.md        (CJK 5258, lines 907)
theory/roadmap-v2/n6arch-axes/axis-r2-refinement.md       (CJK 5548, lines 962)
theory/roadmap-v2/n6arch-axes/axis-r3-finalization.md     (CJK 5656, lines 1167)
theory/roadmap-v2/round-03-emergence-saturation.md        (CJK 4685, lines 1001)
```
Only `_archive-phase-01` technically triggers the Apex Defer Rule (lines > 1500 = no, actually 1235 is under 1500 — re-check). **RE-CHECK**: none of these 5 cross `lines > 1500 AND CJK > 3000` simultaneously; however each exceeds CJK 4500 and lines 900, so per Phase 5 handoff they are classed RED-lite (apex-density). Run **one file per agent, serially**.

**Prompt for B12 Part B (per-file RED-lite template)**:
```
You are Phase 6 Batch 12 (RED-lite, single file).

TARGET: {one file}
CJK: {n}   Lines: {m}

Scope cap: EXACTLY ONE FILE this session. No parallelism. No regex pipelines.
Manual section-by-section translation. Checkpoint commit allowed after every 200 translated lines if uncertainty is high.

UNIVERSAL PROTOCOL applies (plan 4.0). Additionally:
- Use stage-via-index-add only (git add <path>). No stash -u.
- Atomic tmp-rename for allowlist shrink (one-entry shrink).
- Per-file commit pair (translate + shrink).
- Never claim "translation complete"; commit message says "English conversion (1 file)".
- If uncertainty on any theory term (roadmap-v2 axis vocabulary: emergence / refinement / finalization / saturation), leave a comment placeholder in the draft AND report back; do not ship a degraded translation.

Deliver: translate commit SHA, shrink commit SHA, new allowlist count.
```

Est 110,163 CJK. Target 48 -> 20.

---

### 4.14 B13 — papers/ non-apex remainder + B8 carryover (RED-lite, 5 files)

Files:
```
papers/n6-66-techniques-integrated-paper.md              (CJK 5696, lines 1185)  [non-apex]
papers/n6-advanced-packaging-integrated-paper.md         (CJK 4222)               [non-apex]
papers/n6-hexa-starship-integrated-paper.md              (CJK 5119, lines 1245)  [non-apex]
papers/moonshine-barrier-honest-report-2026-04-15.md     (CJK 9319, lines 1277)  [B8 carryover]
papers/n6-ultimate-superconductor-integrated-paper.md    (CJK 7359, lines 1683)  [B8 carryover — APEX]
```

**Split execution**:
- Three non-apex papers: one agent, sequential (B1 YELLOW template).
- `moonshine-barrier`: dedicated agent with Moonshine / VOA / Monster-group glossary checkpoint per equation block.
- `n6-ultimate-superconductor`: dedicated agent (APEX — lines 1683, CJK 7359 — crosses apex threshold).

**Per-file RED-lite prompt additions** for the two dedicated agents:
```
ADDITIONAL PROTOCOL for moonshine-barrier / n6-ultimate-superconductor:
- Before translating each equation block, state the source equation verbatim, the intended English target, and the glossary entry used.
- Checkpoint commit (translate-only, no shrink) after every 2 equation blocks.
- Final shrink commit removes ONLY this one file from the allowlist.
- Any Monster-group / VOA / BCS / Cooper-pair / gap-function term that cannot be verified against a known reference -> SKIP-DEFER; leave file partly translated, revert WT, do NOT ship.
```

Est 30,974 CJK. Target 20 -> 15.

---

### 4.15 B14 — apex cognitive + sf-ufo + chip-paper apex (RED, 10 files, one agent each)

```
domains/cognitive/ai-training-cost/ai-training-cost.md       (CJK 10254, lines 1927)
domains/cognitive/ai-consciousness/ai-consciousness.md       (CJK 10049, lines 1841)
domains/cognitive/ai-agent-serving/ai-agent-serving.md       (CJK  9523, lines 1605)
domains/cognitive/ai-quality-scale/ai-quality-scale.md       (CJK  9079, lines 1570)
domains/cognitive/ai-eval-pipeline/ai-eval-pipeline.md       (CJK  8815, lines 1854)
domains/cognitive/ai-inference-cost/ai-inference-cost.md     (CJK  8451, lines 1649)
domains/cognitive/ai-enterprise-custom/ai-enterprise-custom.md (CJK 7657, lines 1537)
domains/cognitive/ai-interpretability/ai-interpretability.md (CJK  6699, lines 1033)  [apex-adj; include here]
domains/sf-ufo/hexa-ufo/hexa-ufo.md                          (CJK  8042, lines 1873)
papers/n6-hexa-consciousness-integrated-paper.md             (CJK  6644, lines 1637)
papers/n6-hexa-chip-7dan-integrated-paper.md                 (CJK  6156, lines 1619)
```
(11 entries listed; `ai-interpretability` is slightly under the lines threshold but keep in RED band for uniform handling — final count 10 apex + 1 adjacent.)

**Prompt template (one per file)**:
```
You are Phase 6 Batch 14 RED apex agent (single file).

TARGET: {path}
CJK: {n}    Lines: {m}

STRICT RULES (in addition to UNIVERSAL PROTOCOL):
1. NO regex pipelines. NO mass Edit across multiple sections.
2. Translate section-by-section. A "section" = one top-level `##` heading block.
3. After EVERY section, run: python3 tool/own_doc_lint.py --rule 1 --files {path}
   Record the declining CJK count; if a section fails to reduce CJK, revert that section and retry.
4. After EVERY 3 sections, commit (translate-only, no-shrink) with message:
     docs(translate): phase-6-B14 {basename} sections {range} (in-flight)
5. Shrink ONLY after all sections are CJK = 0 and the whole-file lint passes.
6. ASCII art / tables / code fences / LaTeX / citation keys / frontmatter: VERBATIM.
7. own#11 softeners STRICT ("proven/solved/complete" -> "draft/candidate/pattern").
8. If a section contains domain-specific uncertainty (interpretability: SAE, probe, circuit; serving: KV-cache, tokenizer, MoE routing; eval: elo, harness, human-preference), use the glossary drafted in Phase 3 `domains/` translations and cite the source file if terms diverge. On irresolvable uncertainty: defer the file.

Deliver: section-by-section translate SHAs, final translate SHA, shrink SHA, new allowlist count.
```

Est 84,445 CJK. Target 15 -> 5.

---

### 4.16 B15 — fusion/KSTAR specs + atlas-constants (RED, 4 files, one agent each)

```
reports/sessions/specs/2026-04-02-kstar-300s-steady-state-design.md        (CJK 11872, lines 3099)
reports/sessions/specs/2026-04-02-kstar-n6-tokamak-design.md               (CJK 15141, lines 3448)
reports/sessions/specs/2026-04-02-ultimate-fusion-powerplant-design.md     (CJK 15851, lines 3168)
theory/constants/atlas-constants.md                                        (CJK 20722, lines 6363)
```

**KSTAR/fusion prompt addendum** (applies to the 3 specs):
```
ASCII ART PRE-PASS REQUIRED.

Step 1: Locate every ASCII-art / box-diagram region (indented or fenced with +---+, |, etc.).
Step 2: Extract each region to a placeholder token ASCII_BLOCK_{nnn} in an out-of-tree scratch file.
Step 3: Translate only the prose and table body text. ASCII blocks remain frozen.
Step 4: After prose translation verifies CJK = 0 in prose regions, re-inject ASCII_BLOCK_{nnn} verbatim.
Step 5: Diff column widths before/after; any mismatch => revert and redo that block only.

GLOSSARY (fusion/KSTAR):
- tokamak, divertor, limiter, scrape-off layer, plasma-facing component
- tritium breeding ratio, blanket, first wall
- H-mode, L-mode, ELM, pedestal, confinement time
- Greenwald density limit, beta limit, bootstrap current
- neutral beam injection (NBI), ICRH, ECRH, LHCD
- central solenoid, poloidal/toroidal field, divertor coil
Leave Korean proper nouns (KSTAR, ITER, K-DEMO) as-is.
```

**atlas-constants prompt addendum**:
```
atlas-constants.md is 6363 lines and consists primarily of a long table of physical / mathematical constants with descriptive text per row.

STRATEGY:
- Work on 500-line chunks via Read offset=... limit=500.
- Within each chunk: translate description columns, leave numeric values / units / symbol columns untouched.
- Checkpoint commit per chunk (translate-only) with message:
    docs(translate): phase-6-B15 atlas-constants rows L{start}-L{end} (in-flight)
- Final shrink commit after lint passes on the whole file.
- Greek letters, sigma-notation, mathematical-script letters stay as LaTeX: $\sigma$, $\phi$, $\mathfrak{g}$, etc.
```

Est 63,586 CJK. Target 5 -> 1.

---

### 4.17 B16 — theory/breakthroughs/breakthrough-theorems.md (RED-APEX, 1 file, 3-way split)

**The file is 28,481 lines and 125,694 CJK — a single `Read` cannot load it; a single agent cannot translate it; and a single commit should not attempt it.**

#### B16 strategy — 3-way dedicated-agent split along natural BT-xxx boundaries

**Step 0 — boundary discovery (executor-parent task, not an agent)**:
1. Grep the file for `^## BT-` or similar heading markers:
   `Grep(pattern="^## BT-\\d{3}", path=".../breakthrough-theorems.md", output_mode="content", -n=true, head_limit=0)`
2. Identify three approximately equal partitions by BT-xxx index:
   - Partition A: BT-001 .. BT-{a} (target ~9,500 lines, ~42,000 CJK)
   - Partition B: BT-{a+1} .. BT-{b} (target ~9,500 lines, ~42,000 CJK)
   - Partition C: BT-{b+1} .. end (target ~9,500 lines, ~42,000 CJK)
3. Record the exact line ranges and the BT-xxx break boundaries.

**Step 1 — on-disk split (executor-parent, not an agent)**:
- Write three sibling files:
  - `theory/breakthroughs/breakthrough-theorems-part-a.md`
  - `theory/breakthroughs/breakthrough-theorems-part-b.md`
  - `theory/breakthroughs/breakthrough-theorems-part-c.md`
- Each part carries its own frontmatter (derived from the original) plus a "This file is Part {X} of 3, see parent breakthrough-theorems.md" note.
- Replace the original `breakthrough-theorems.md` with a stub that links to the three parts (English-only stub, CJK = 0).
- Atomic commit: `refactor(theory): split breakthrough-theorems.md into 3 parts for translation (no content change)`.
- After commit, update the allowlist: the original path's CJK is now 0, and the three new paths are CJK > 0 and must be ADDED to the allowlist if own#1 would otherwise block them. This is a **structural preamble** before any translation.

**Step 2 — three dedicated RED-APEX agents (one per part, serial, not parallel)**:

Per-part prompt:
```
You are Phase 6 Batch 16 RED-APEX agent for Part {A|B|C} of breakthrough-theorems.

TARGET: theory/breakthroughs/breakthrough-theorems-part-{x}.md
Lines: ~9500    CJK: ~42000
Parent of this file: theory/breakthroughs/breakthrough-theorems.md (stub)

SCOPE CAP: exactly this one part file. No touching of the other two parts, the stub, or any other file in the repo.

PROTOCOL:
1. Read in 500-line chunks (offset=0, 500, 1000, ...). Never attempt a single Read of the whole file.
2. For each chunk:
   a. Identify BT-xxx headings within the chunk.
   b. Translate one BT-xxx block at a time (usually 30-200 lines).
   c. After each BT-xxx block, run: python3 tool/own_doc_lint.py --rule 1 --files <part-file>
   d. Record the declining CJK number.
3. Commit every 5 BT-xxx blocks (translate-only):
     docs(translate): phase-6-B16-part{x} BT-{range} (in-flight)
4. own#11 softeners STRICT — this file is ground zero for "proven" / "solved" / "complete" in the repo. Replace every occurrence in translated output with "draft / candidate / pattern / demonstrating". If the original Korean asserts completion, the English MUST soften.
5. Math / LaTeX / rep-theory notation VERBATIM. Do not silently normalize `\otimes` / `\oplus` / `\mathfrak{sl}_2` etc.
6. On ANY uncertainty (rep-theory, Monster, Moonshine, VOA, E8, modular forms, Langlands): SKIP-DEFER that BT block. Leave the Korean intact, add an inline comment `<!-- phase-6-B16 defer: reason -->`, move on.
7. After the whole part file lints CJK = 0 (or all non-skip blocks do), make the final translate commit for the part:
     docs(translate): phase-6-B16-part{x} final
8. Do NOT shrink the allowlist in this agent's session. Allowlist shrink happens once, by the parent, after all three parts are done (see Step 3).

Deliver: list of BT blocks TRANSLATE vs SKIP-DEFER, final CJK count per part, commit SHAs.
```

**Step 3 — reconciliation (parent, after all 3 part-agents finish)**:
1. Verify each of the three part files has CJK = 0 (or documented skip-defer blocks).
2. If any SKIP-DEFER blocks remain, they stay on the allowlist as the three part-files — re-audit and fold back into a Phase 6 tail batch.
3. If all three parts clean: atomic allowlist shrink of the original `theory/breakthroughs/breakthrough-theorems.md` entry (now a CJK = 0 stub) plus remove any temporary entries added in Step 1 once those part-files are CJK = 0.
4. Commit: `feat(own): shrink own#1 allowlist phase-6-B16 (breakthrough-theorems final)`.
5. Push with 2-3 rebase retries.

Target: 1 -> 0.

**Alternative (fallback)** — if the Step 1 on-disk split is rejected by the user:
Run three agents against offsets `[0..9500)`, `[9500..19000)`, `[19000..28481)` of the single file, each agent holding an advisory lock on the file (via `.git/phase-6-B16.lock`) and each committing translate-only in sequence, never in parallel. Shrink once at the end. This is slower and has a higher merge-conflict risk; the split-then-translate path is the recommended primary.

---

## 5. Final reconciliation checklist

At end of Phase 6 (after B16 reconciliation):

- [ ] `tool/own_doc_lint.py --rule 1` exits 0 with 0 HARD violations.
- [ ] `tool/own1_legacy_allowlist.json` contains `"allowlist": []` AND `"_meta": {"count": 0}`, OR (final step) the file is deleted outright.
- [ ] If the file is deleted: update `.own` / policy config so own#1 loads without the allowlist (verify `tool/own_doc_lint.py` doesn't require a missing JSON).
- [ ] CI gate `own1-doc-english-hard` green on `main` tip.
- [ ] `reports/sessions/hard-english-only-session-2026-04-24.md` appended with a Phase 6 close-out section that records: final SHA, batch-by-batch count, any skip-defers, the final shrink/delete commit.
- [ ] `proposals/own1-hard-english-only-translation-roadmap-2026-04-24.md` updated with "Phase 5 close / Phase 6 close" status markers.
- [ ] Root `README.md` verified CJK = 0 (own#17 sanity).
- [ ] No `git stash` entries outstanding (`git stash list` empty).
- [ ] Dangling `.own1_legacy_allowlist.json.tmp` or similar absent.

## 6. Risks specific to Phase 6

| Risk | Impact | Mitigation |
|---|---|---|
| B16 on-disk split changes citation paths | Internal links to `breakthrough-theorems.md#BT-xxx` break | Step 1 keeps a stub with forwarding links; grep the repo for any incoming reference before the split and rewrite if found |
| atlas-constants numeric drift | Wrong constant value ships | Rule: only description columns are translated; numeric / unit / symbol columns are strictly VERBATIM |
| B14 cognitive glossary drift | "training-cost" vs "training cost" in prose headers | Pre-agent step: dump the subset of the Phase 3 glossary that covers `ai-*` and inject into the prompt |
| Allowlist JSON contention (Phase 5 Section 14.3) | Sibling-stash-wipeout repeats | Enforce mtime check + atomic tmp-rename in every shrink agent; run YELLOW at N <= 4 until a per-prefix shard lands |
| ASCII art column mismatch in B15 specs | Diagram corruption | Pre-pass extraction to placeholders, re-inject verbatim, post-pass diff |
| Hook race on commit | Phantom `--amend` risk | `--no-verify` across all Phase 6 commits; run `tool/own_doc_lint.py --rule 1` locally post-commit |
| Partial apex defer accumulating | Non-zero allowlist at Phase 6 close | Any SKIP-DEFER rolls into a dedicated Phase 6 tail batch; do not declare Phase 6 done until allowlist == 0 or the remaining set is re-estimated and re-scheduled |

## 7. Scheduling snapshot

- B0 .. B2: day 1 (GREEN + low-density life/materials).
- B3 .. B8: days 2-4 (YELLOW domain bulk).
- B9 .. B11: days 5-6 (compute YELLOW).
- B12: days 7-8 (RED-lite chip-/hexa- second half + theory/roadmap-v2 serial).
- B13 .. B14: days 9-11 (RED-lite papers + RED apex cognitive/sf-ufo).
- B15: days 12-13 (RED fusion/KSTAR + atlas-constants).
- B16: days 14-17 (RED-APEX breakthrough-theorems split then 3 part-agents).
- Reconciliation + allowlist-file deletion: day 18.

Draft target window: 2026-04-26 through 2026-05-13 (approximate; not a commitment).

---

*Planning only. No translation agents launched in this pass. Each per-batch prompt above is self-contained and can be dispatched by the Phase 6 executor as-is. The "draft / candidate / pattern / demonstrating" vocabulary governs every status claim — own#11 holds.*
