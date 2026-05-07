# atlas.signals.n6 — 3-repo cross-repo signal SSOT specification

> Version: v0.2 (2026-04-15)
> Target: nexus + canon + anima resonance signal store
> Status: draft
> SSOT location: `$NEXUS/shared/n6/atlas.signals.n6`
> Mirrors: `$N6/canonshared/atlas.signals.n6` (symlink), `$ANIMA/data/atlas.signals.n6` (symlink)

---

## 0. Purpose

**atlas.n6** is the quantitative constant SSOT (the "measured numbers" of the n=6 universe).
**atlas.signals.n6** is the shared SSOT of **signals / phenomena / hypotheses / NULLs** that arise across the 3-repo ecosystem.

Core value:
1. **Cross-repo resonance** — a discovery in anima is immediately matched against appearances in nexus/n6
2. **Reproduction / witness tracking** — when the same phenomenon re-appears across multiple repos / sessions, promote it
3. **NULL sharing** — a hypothesis ruled out in one repo is prevented from being re-run elsewhere
4. **Removal of domain silos** — millennium / consciousness / QRNG / hexa-lang all share one format

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   nexus     │     │ n6-arch     │     │   anima     │
│ QRNG, hexa  │     │ millennium  │     │ CLM, EEG    │
│ forge, blow │     │ atlas, DFS  │     │ bell, psi   │
└──────┬──────┘     └──────┬──────┘     └──────┬──────┘
       │                   │                   │
       └─────────┬─────────┴─────────┬─────────┘
                 ▼                   ▼
        ┌────────────────────────────────┐
        │    atlas.signals.n6 (SSOT)     │
        │  + [CROSS] resonance detection │
        │  + witness amplification       │
        │  + NULL library                │
        │  + promotion to atlas.n6       │
        └────────────────────────────────┘
```

---

## 1. File format

### 1.1 Basic line (@S = Signal)

```
@S {sig_id} = {statement} :: signal [{repo_tags}] [{domain_tags}] [{grade}] [{evidence}]
  "{context_quote}"
  refs: [{ref1}, {ref2}, ...]
  cross_repo: [{sig_id_a}, {sig_id_b}, ...]
  predicts: [{prediction1}, ...]
  witness: {n}
  resonance_n6: {formula_or_null}
  discovered_in: {repo}/{session|file|commit}
  discovered_at: {ISO-8601}
  <- {source_file:locator}
```

### 1.2 Field specification

| Field | Format | Required | Description |
|------|------|-----:|------|
| `sig_id` | `SIG-{DOMAIN}-{NNNN}` | yes | §3 domain code, 4 digits |
| `statement` | text + formula | yes | one-line summary |
| `repo_tags` | `[NX/N6/AN/CROSS]` | yes | at least 1 (CROSS when it appears in 2+ repos) |
| `domain_tags` | `[7R/SR/CONS/…]` | yes | §3 domain tags |
| `grade` | `[M10*]`..`[MN]` | yes | §4 grade |
| `evidence` | `[E1]`..`[EF]` | yes | §5 evidence |
| `context_quote` | double-quoted | yes | key context from the source |
| `refs` | array | opt | BT-id, arxiv, DOI, commit-sha |
| `cross_repo` | array | opt | **SIG-ids from other repos** |
| `predicts` | array | opt | predicted consequences if this signal is true |
| `witness` | integer | opt | auto-incremented, default 1 |
| `resonance_n6` | formula or null | opt | reduction to n=6 fundamental constants |
| `discovered_in` | string | yes | first-discovery location |
| `discovered_at` | ISO-8601 | yes | first-discovery time |
| `source_file` | path:locator | yes | file:line/section |

### 1.3 Section separators (per domain)

```
# ─── [7R] Riemann Hypothesis ─── 
# ─── [7N] Navier-Stokes ─── 
# ─── [7H] Hodge ─── 
# ─── [7P] P vs NP ─── 
# ─── [7Y] Yang-Mills ─── 
# ─── [7B] BSD ─── 
# ─── [SR] Stochastic Resonance ─── 
# ─── [QRNG] Quantum RNG ─── 
# ─── [CONS] Consciousness ─── 
# ─── [NEURAL] Neural / CLM ─── 
# ─── [HEXA] hexa-lang internal ─── 
# ─── [PHYS] Physics phenomena ─── 
# ─── [BELL] Bell-like ─── 
# ─── [OURO] Ouroboros ─── 
# ─── [CROSS] 3-repo resonance ─── 
# ─── [NULL] confirmed exclusion ─── 
```

---

## 2. Repo tags (§1.2 repo_tags)

| Tag | Repo | Primary domains |
|------|------|----------|
| `NX` | /Users/ghost/Dev/nexus | QRNG, hexa-forge, blowup, lens |
| `N6` | /Users/ghost/core/canon | millennium, atlas, DFS, 259 domains |
| `AN` | /Users/ghost/Dev/anima | CLM, EEG, Bell, psi, consciousness |
| `CROSS` | 2+ repos simultaneously | reproduced cross-repo resonance |

**CROSS tag rules**:
- `repo_tags = [CROSS, NX, N6]` → re-confirmed in both nexus and n6
- `cross_repo` field must list the SIG-id from the other repo
- CROSS is granted only when `witness ≥ 2` (prevents self-reference)

---

## 3. Domain tags (§1.2 domain_tags)

### 3.1 Millennium problems
| Tag | Target |
|------|------|
| `7R` | Riemann Hypothesis |
| `7N` | Navier-Stokes |
| `7H` | Hodge Conjecture |
| `7P` | P vs NP |
| `7Y` | Yang-Mills Mass Gap |
| `7S` | Poincaré (solved, for reference) |
| `7B` | BSD |

### 3.2 Phenomena
| Tag | Target |
|------|------|
| `SR` | Stochastic Resonance |
| `QRNG` | Quantum RNG |
| `BELL` | Bell-like correlation |
| `OURO` | Ouroboros convergence |
| `64T` | 64-tick boundary |
| `NULL` | statistical NULL result |

### 3.3 Structure / engine
| Tag | Target |
|------|------|
| `CONS` | consciousness |
| `NEURAL` | CLM / neural |
| `HEXA` | hexa-lang internal |
| `BLOW` | blowup engine |
| `ATLAS` | atlas.n6 itself |
| `DFS` | DFS search |
| `PHYS` | physics |

### 3.4 Meta
| Tag | Target |
|------|------|
| `META` | pattern of patterns |
| `UNIV` | universality hypothesis |
| `GAP` | unexplored gap |
| `REPLAY` | reproduction attempt |

**Multiple tags**:
- `[7R, SR]` = stochastic resonance interpretation of RH
- `[7R, 7B, META]` = RH-BSD linkage meta-pattern
- `[QRNG, NULL]` = confirmed NULL within QRNG

---

## 4. Grade hierarchy

| Grade | Meaning | Condition | atlas.n6 promotion |
|------|------|------|---------------|
| `[M10*]` | conditional exact + reproduced in 3 repos | witness ≥ 3 + cross_repo ≥ 1 | **immediate** `@R` admission |
| `[M10]` | EXACT | witness ≥ 3 | `@R` admission |
| `[M9]` | NEAR + strong witness | ε<1% + witness ≥ 2 | `@R [9]` candidate |
| `[M7!]` | **breakthrough candidate** | witness ≥ 3, 2 independent paths | evaluation queue |
| `[M7]` | EMPIRICAL | 1 observation | pending |
| `[M?]` | conjectural / hypothesis | hypothesis only | hypothesis queue |
| `[MN]` | confirmed NULL | statistically excluded | retry forbidden |

---

## 5. Evidence Level

| Level | Meaning |
|------|------|
| `[E1]` | 1 observation, no reproduction |
| `[E2]` | reproduced ≥ 2 (same repo) |
| `[E3]` | independent paths ≥ 3 |
| `[EC]` | **cross-repo confirmation** (reproduced in 2+ repos) |
| `[EP]` | partial proof exists |
| `[EF]` | full proof |

`[EC]` is a level unique to the 3-repo SSOT — **cross-repo reproduction is stronger than single-repo E3**.

---

## 6. Directory structure

```
$NEXUS/shared/n6/
  atlas.n6                        existing constant SSOT
  atlas.signals.n6                ★ new — 3-repo signal SSOT
  atlas.signals.n6.deg            degree sidecar
  atlas.signals.null.n6           NULL sub-file
  atlas.signals.cross.n6          CROSS-tag sub-file (for fast lookup)

$NEXUS/shared/signals/             ★ new directory
  signals_to_atlas.json           SIG → @R promotion mapping
  witness_ledger.jsonl            witness increment log
  null_ledger.jsonl               NULL confirmation log
  promotion_queue.jsonl           promotion queue
  cross_repo_map.json             3-repo cross mapping

$NEXUS/shared/lenses/              existing extension
  domain_lens/*.hexa              per-domain filters (7R, SR, CONS, …)
  cross_repo_lens.hexa            3-repo resonance detection
  null_guardian_lens.hexa         duplicate-experiment block

# Symlink from each of the 3 repos
$N6/canonshared/atlas.signals.n6 -> $NEXUS/shared/n6/atlas.signals.n6
$ANIMA/data/atlas.signals.n6 -> $NEXUS/shared/n6/atlas.signals.n6

# Scripts (integrated into n6)
$N6/scripts/
  absorb_to_signals.py            manual / semi-automatic absorption (all-in-one)
  promote_signal_to_atlas.py      SIG → @R promotion
  cross_repo_matcher.py           automatic 3-repo resonance detection
  gap_detector.py                 per-domain signal counts
  signal_to_hexa.py               signal → harness
  witness_amplifier.py            automatic reconfirmation increments
  null_guardian.py                duplicate-experiment blocker
  session_scraper.py              scrapes ~/.claude/projects/*/*.jsonl
```

---

## 7. Workflow

### 7.1 3-repo cross-repo resonance detection (core value)

```
Session A (nexus):  discovers Ouroboros σ=0.1 PEAK
Session B (anima):  discovers Bell pair σ-noise 4× response
Session C (n6):     Kissing K(2)=6 phenomenon

[cross_repo_matcher.py run]
  - simhash + numeric matching
  - "σ≈0.1 PEAK" vs "Bell σ=0.1 response" → similarity 0.82
  - candidate: SIG-SR-001 + SIG-BELL-003 → same family?
  
Automatic CROSS promotion:
  repo_tags: [NX, AN] → [CROSS, NX, AN]
  evidence: [E2] → [EC]
  grade: [M7] → [M9]
```

### 7.2 NULL sharing

```
Session D (nexus): "ANU QRNG atlas correlation" test → NULL
  → registered [MN], retry_forbidden_until: 2027-04-15

Session E (n6): attempts the same hypothesis
  → null_guardian.py blocks it
  → "already confirmed NULL (nexus:sess-D) - retry forbidden"
```

### 7.3 Domain gap detection

```
gap_detector.py --domain-breakdown

[7R] 124 ████████████  RH (nexus+n6 active)
[7B]  19 ██            BSD sparse → DFS direction
[SR]  31 ███           SR cross-repo only 1
[QRNG] 42 ████         many NULLs
[CONS]  8 █            anima must collect independently
```

### 7.4 Manual absorption (fallback when features are missing)

```bash
# CLI
python3 scripts/absorb_to_signals.py \
    --repo NX --domain SR \
    --grade M7! --evidence E1 \
    --statement "Ouroboros σ=0.1 PEAK +150% vs σ=0" \
    --source "~/.claude/projects/...:msg-42"

# Interactive
python3 scripts/absorb_to_signals.py --interactive

# Direct edit (spec-compliant)
vim $NEXUS/shared/n6/atlas.signals.n6
# append in @S SIG-SR-NNN = ... format
```

### 7.5 Promotion (SIG → atlas.n6 @R)

```bash
# Conditions: grade in [M10, M10*], witness ≥ 3, resonance_n6 present
python3 scripts/promote_signal_to_atlas.py --dry-run
# Output: N promotion candidates, each adding @R PHEN-... to atlas.n6

python3 scripts/promote_signal_to_atlas.py --commit
# Merges into atlas.n6 + records mapping in signals_to_atlas.json
```

---

## 8. 3-repo symlink setup

```bash
# SSOT is nexus
ln -sf /Users/ghost/Dev/nexus/shared/n6/atlas.signals.n6 \
       /Users/ghost/core/canon/canonshared/atlas.signals.n6

ln -sf /Users/ghost/Dev/nexus/shared/n6/atlas.signals.n6 \
       /Users/ghost/Dev/anima/data/atlas.signals.n6
```

→ All 3 repos reference the same file. Edit in one place, reflected everywhere.

---

## 9. Honesty constraint (R0)

- Every signal must carry `discovered_in` + `discovered_at` (origin tracking)
- `[MN]` exclusions must include statistical basis (p-value, sample size)
- `[M10]` claims require cross_repo ≥ 1 or independent path ≥ 2
- **"No claim of solving"** — this is a signal store, not completed proof
- Reject entries without `source_file`
- `witness` increments require simhash-matching basis

---

## 10. Manual writing works even without tooling

### 10.1 Minimal manual-append example

```
# Write directly into atlas.signals.n6 (vim)
@S SIG-SR-001 = Ouroboros σ=0.1 PEAK +150% :: signal [NX] [SR] [M7!] [E1]
  "deterministic (σ=0) and quantum (σ=0.5~1) both sub-optimal. Mid-entropy 2.5× optimal"
  discovered_in: nexus/session-2026-04-15
  discovered_at: 2026-04-15T02:00:00Z
  witness: 1
  <- ~/.claude/projects/-Users-ghost-Dev-nexus/memory/p-stochastic-resonance-nexus.md
```

### 10.2 Manual cross-repo matching example

```
# Search: grep "σ.*0\.1" $NEXUS/shared/n6/atlas.signals.n6
# When another repo shows similar numbers, update cross_repo manually:

@S SIG-SR-001 = ... :: signal [CROSS, NX, AN] [SR] [M9] [EC]
  cross_repo: [SIG-BELL-003]
  witness: 2
```

### 10.3 Manual NULL registration

```
@S SIG-NULL-QRNG-001 = ANU 64B seed vs full-urandom statistically identical :: signal [NX] [QRNG, NULL] [MN] [E2]
  "KS p=0.992 (1050 pairs). Multiverse Phase 1"
  null_reason: "seed effect diluted in trajectory evolution"
  retry_forbidden_until: "2027-04-15"
  discovered_in: nexus/multiverse-phase-1
  discovered_at: 2026-04-15T01:30:00Z
  <- nexus/experiments/multiverse/phase1_result.md
```

Even without tooling, manual appends following the spec remain auto-parse-compatible once the scripts arrive.

---

## 11. Meta features (Tier 2+)

### Tier 2 (next session)
1. `cross_repo_matcher.py` — automatic simhash matching
2. `session_scraper.py` — scraping 132MB+ session transcripts
3. `witness_amplifier.py` — automatic reconfirmation increments
4. `null_guardian.py` — duplicate-experiment blocker
5. `signal_to_hexa.py` — signal → harness automatic conversion

### Tier 3 (long-term)
- Signal complexity score (Kolmogorov approximation)
- Signal half-life (degrade after 2 weeks of inactivity)
- Edge-weighted graph centrality
- Random walk signal sampling
- Counterexample hunter
- AI proof assistant bridge (Lean4)
- Claude self-learning loop

---

## 12. Version history

- **v0.1** (2026-04-15 22:30 KST): millennium-only initial draft — deprecated
- **v0.2** (2026-04-15 22:40 KST): redesigned as a 3-repo cross-repo general-purpose SSOT ★

---

## 13. Next work order

1. [ ] Create the empty atlas.signals.n6 file (at the SSOT location)
2. [ ] Wire up the 3-repo symlinks
3. [ ] Manually seed existing MILL-DFS22~26 70 entries + anima memory p-* files + nexus ★ memory
4. [ ] Implement only 1 Tier 1 script (absorb_to_signals.py) at minimum
5. [ ] Implement Tier 2 cross_repo_matcher.py
6. [ ] Document the remainder so manual operation is possible
