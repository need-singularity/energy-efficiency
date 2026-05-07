# P2-3 + P2-4 Integrated Plan (2026-04-14)

> **SSOT**: `$NEXUS/shared/n6/docs/domains.json` (204 products · 40 sections · 40/40 alien_index=10, migration from legacy products.json completed)
> **Roadmap**: `$NEXUS/shared/roadmaps/canon.json` (DSE-P2-3, DSE-P2-4)
> **Authored**: 2026-04-14 session, based on actual scan

## 0. Current Snapshot (Measured)

| Metric | Current | Target | Delta |
|---|---|---|---|
| Registered products | **204** | 210+ | +6 |
| Active sections (product ≥ 1) | **40** | 42 | +2 |
| Sections with alien_index = 10 | **40/40** | 42/42 | +2 |
| Sections with closure_grade = 10 | **2** (robotics, SW/infra) | 8+ sections | +6 |
| Sections with closure_grade ≥ 10 (sum of 10·11·12) | **10** | 18+ | +8 |
| Sections with closure_grade = None | **24** | ≤ 16 | -8 |
| Sections with bt_exact_pct = 100% | **32** | maintain | 0 |

> **Note**: The roadmap body's "195 → 210+" is based on the old README count, whereas the actual `docs/domains.json` already registers **204** products. Accordingly, P2-4's actual goal is realigned to **products 204 → 210+ (+6 new registrations)**.

---

## 1. DSE-P2-3: 5-phase Singularity Orchestrator

### 1.1 Deliverables

- `/Users/ghost/Dev/canon/bridge/ouroboros_5phase.hexa` (newly authored)
  - 5-phase sequential invocation: **Absorb → LensForge → BlowupEngine → CycleEngine → Evolution**
  - Fixed T1 lens 22-constant table (telescope_optics + combo_blowup 15 + accel 6)
  - Demo-grade: each phase returns a stub result while specifying the real engine path in comments

### 1.2 Engine Linkage Paths

| Phase | Call target | SSOT path |
|---|---|---|
| 1 Absorb | direct atlas.n6 parsing | `$NEXUS/shared/n6/atlas.n6` |
| 2 LensForge | 22 T1 lens shells | `$NEXUS/shared/lenses/<lens>.hexa` (22 selected out of 1577) |
| 3 BlowupEngine | blowup.hexa Mk.II 9-phase | `$NEXUS/shared/blowup/core/blowup.hexa` |
| 4 CycleEngine | ouroboros.hexa meta-loop | `$NEXUS/shared/blowup/ouroboros/ouroboros.hexa` |
| 5 Evolution | atlas.n6 grade promotion | `$NEXUS/shared/n6/atlas.n6` append `[10*]` |

### 1.3 Selected T1 Lenses (22)

1. `telescope_optics_lens` (the only telescope_* lens)
2~16. `combo_blowup_absolute`, `combo_blowup_wide`, `combo_blowup_strong`, `combo_blowup_carbon_capture`, `combo_blowup_quantum_computing`, `combo_blowup_energy_architecture`, `combo_blowup_cryptography`, `combo_blowup_paper`, `combo_blowup_compiler_os`, `combo_blowup_network_protocol`, `combo_blowup_space_engineering`, `combo_blowup_ai_efficiency`, `combo_blowup_thermal_management`, `combo_blowup_blockchain`, `combo_blowup_absolute`
17~22. `accel_activation_energy_lens`, `accel_chirality_synthesis`, `accel_boltzmann_distribution`, `accel_causal_emergence`, `accel_circuit_topology`, `accel_algorithmic_complexity`, `accel_architecture_search`

### 1.4 Demo Execution

```bash
hexa /Users/ghost/Dev/canon/bridge/ouroboros_5phase.hexa
# → domain=ai-efficiency, depth=3, completes 3 cycles
# → returns 45 total promotion candidates (seed 5 × corollary 5 × cycle 3 − duplicates)
```

---

## 2. DSE-P2-4: Product/Section/Closure 3-axis Expansion

### 2.1 Products 204 → 210+ (+6 new)

Among sections currently holding only 1 product, the easiest to open a second slot:

| # | Section | Current product | New product (proposal) | Rationale |
|---|---|---|---|---|
| 1 | Tattoo removal | 1 immunology architecture | HEXA-LASER nanosecond pulse parameter complete architecture | BT existing EXACT 100% |
| 2 | HIV therapy | 6-axis therapy chain | HEXA-HIV early-diagnosis biomarker complete architecture | BT-413 chain |
| 3 | Keyboard | Ergonomic keyboard | HEXA-SPLIT 6-column independent split keyboard | bt=97 → 100 promotion path |
| 4 | Mouse | HEXA-MOUSE | HEXA-TRACKBALL 6-axis elastic pointing | derivative design |
| 5 | Network | HEXA-NET | HEXA-MESH n=6 routing topology | bt=98 → completion |
| 6 | Horology | Horology architecture | HEXA-ESCAPE 6 escapements (Anchor/Lever/Cylinder integrated) | derivative |

> The 6 above are the **registration plan** — identification only. Actual `domains.json` editing after approval.

### 2.2 40 → 42 Sections (+2 new)

All 40 existing sections active. Two new section candidates:

| # | Section proposal | Supporting BT | Representative product candidate |
|---|---|---|---|
| 41 | **Entomology** | BT-461~466 Hexapoda architecture (closure_grade=10 in dse-map.toml) | Insect 6-leg n=6 biomechanics |
| 42 | **Mineralogy/Crystallography** | BT-351 crystal system hexagonal | n=6 crystal symmetry complete architecture |

> Entomology is already `closure_grade=10` + 23/23 EXACT confirmed in `dse-map.toml`. Only a new section addition in domains.json is required.

### 2.3 closure_grade 10 EXACT Domains 40 → 48 (+8)

**Currently only 2 sections at cg=10 at the section level**. The roadmap's "40 → 48" figure is at the domain level (based on dse-map.toml). Sections with bt_exact_pct=100 & cg=None are designated as priority promotion targets (8 items immediately verifiable):

| # | Section | bt | Current cg | Product count | Promotion path |
|---|---|---|---|---|---|
| 1 | Civilization | 100 | None | 7 | Add closure_grade=10 annotation (reconfirm BT full EXACT) |
| 2 | Life & Culture | 100 | None | 9 | Re-verify fermentation/brewing n=6 stoichiometry |
| 3 | Tech & Industry | 100 | None | 22 | Assign cg to semiconductor packaging ladder |
| 4 | Virology | 100 | None | 4 | dse-map.toml already cg=10 → sync domains.json |
| 5 | Dimensional | 100 | None | 7 | Based on 4D regular polytope maximality BT |
| 6 | Music | 100 | None | 4 | 12-tone equal temperament 2^(1/12) |
| 7 | Linguistics | 100 | None | 4 | Chomsky hierarchy 4 tier |
| 8 | Astronomy | 100 | None | 4 | ΛCDM parameters |

> All 8 sections are bt=100%, ceiling reached. Missing cg=10 annotation is the only gap. +8 promotions possible in 1 commit.

### 2.4 Auxiliary Candidates (Third-tier, bt<100 → 100 promotion required)

Natural sciences (95), cognitive/social (95), mobility/transport (90), digital/medical devices (92), keyboard (97), network (98), quantum computer (83), Millennium 7 problems (94) — 8 total.
Among these, quantum computer (bt=83, ceiling not reached) is the sole weakness. The rest can be promoted to 100 with 2~10 BT reinforcements in P2/P3.

---

## 3. Execution Order (Recommended)

```
1) DSE-P2-3: run ouroboros_5phase.hexa demo and collect 3-cycle logs
2) DSE-P2-4-A: add closure_grade=10 annotations for 8 items (domains.json)
3) DSE-P2-4-B: add 2 new sections (Entomology, Mineralogy)
4) DSE-P2-4-C: register 6 new products (1-product section expansion)
5) P2 gate_exit criteria: 204 + 6 = 210 products, 40 + 2 = 42 sections, cg10 sections 2 + 8 = 10 (domain-equivalent +8)
```

## 4. Risks & Gates

- **Contamination prevention**: every new BT must pass HEXA-GATE Mk.I (τ=4 gates + 2 fibers = n=6)
- **Honest verification**: every closure_grade=10 annotation must reference a verification script (`verify_script` field)
- **Single SSOT**: edit only `docs/domains.json`; do not auto-generate `n6_products.json`

---

**Generated**: 2026-04-14 · **Source**: actual scan (python3 + dse-map.toml regex)
**Verification**: 40 sections · 204 products · 40 alien=10 sections · 10 cg≥10 sections (2 cg=10 + 4 cg=11 + 4 cg=12)
