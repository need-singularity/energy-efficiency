# HEXA-BATTERY 7-Level Architecture Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Target ultimate battery architecture built on n=6 arithmetic, rolled out as a 7-level roadmap: goal.md + seven level documents + new BT-80~84 theorems.

**Architecture:** Mirrors the document structure used for the chip architecture (docs/chip-architecture/). Each level gets its own .md file; every section must include ASCII diagrams; every page includes an n=6 parameter map with EXACT/CLOSE/WEAK grades. Consolidates existing BT-27/43/57/60/62/68 and introduces new BT-80~84 candidates.

**Tech Stack:** Markdown docs, n=6 arithmetic constants from consciousness_laws.py, existing BT framework.

**Spec:** `docs/superpowers/specs/2026-04-01-hexa-battery-design.md`

**Reference docs (must read):**
- `docs/chip-architecture/goal.md` - chip-architecture goal.md structure to mirror
- `docs/chip-architecture/hexa-super.md` - Level 6 document-structure reference (14~16 section pattern)
- `docs/chip-architecture/hexa-wafer.md` - Level 5 document-structure reference
- `docs/battery-storage/hypotheses.md` - H-BS-1~24 existing hypotheses
- `docs/battery-storage/extreme-hypotheses.md` - H-BS-61~80 extreme hypotheses
- `docs/battery-storage/verification.md` - verification results
- `docs/breakthrough-theorems.md` - BT-27, BT-43, BT-57, BT-60, BT-62, BT-68
- `docs/energy-generation/new-hypotheses-2026-phase2.md` - H-EN-102~104

---

## Phase 1: foundation

### Task 1: goal.md - 7-Level roadmap overview

**Files:**
- Create: `docs/battery-architecture/goal.md`
- Reference: `docs/chip-architecture/goal.md` (structural template)

- [ ] **Step 1: read chip-architecture goal.md**

```bash
cat docs/chip-architecture/goal.md
```

Understand the full structure: header, Evolution Ladder table, each Level section (Status + ASCII diagram + parameters + benefits), Links.

- [ ] **Step 2: author goal.md**

Create `docs/battery-architecture/goal.md`. Must include:

```markdown
# N6 Battery Architecture - Ultimate Goal Roadmap

**Ultimate target: an energy-storage architecture that threads n=6 arithmetic from the atomic scale to the planetary scale.**

---

## Evolution Ladder

[7-Level ASCII table - see spec Section 2]
Per level: architecture name | innovation | benefit | core n=6 constants

---

## N6 Constants Reference

[n=6 constants box - follow spec Section 3 verbatim]

---

## Level 1: HEXA-CELL (design pending)
  Status: design pending -> [hexa-cell.md](hexa-cell.md)
  [ASCII diagram: CN=6 cathode/anode structure]
  [3-5 key parameters]
  [BT dependencies: BT-27, BT-43]

## Level 2: HEXA-ELECTRODE (design pending)
  ... same pattern per level ...

## Level 7: HEXA-OMEGA-E (design pending)
  ...

---

## New Breakthrough Theorems

[BT-80~84 summary table - see spec Section 11]

---

## Cross-Domain Bridge

[battery <-> chip <-> AI convergence diagram]
96 = sigma(sigma-tau): Tesla 96S = GPT-3 96L = Gaudi2 96GB
192 = phi * sigma(sigma-tau): Hyundai 192S = B100 192GB

---

## Links
- [Chip architecture](../chip-architecture/goal.md)
- [Battery-storage hypotheses](../battery-storage/hypotheses.md)
- [Breakthrough theorems](../breakthrough-theorems.md)
```

**Key rules:**
1. Match the chip-architecture goal.md section layout exactly.
2. All levels must carry ASCII diagrams (CLAUDE.md rule).
3. Each level's Status starts as "design pending" and is updated once complete.
4. Evolution Ladder uses double-border ASCII tables.
5. Target length approximately 300 lines.

- [ ] **Step 3: verify goal.md**

Checklist:
- Do all 7 levels have ASCII diagrams?
- Are BT dependencies listed for every level?
- Does the N6 Constants Reference match the spec?
- Does Links include chip-architecture + battery-storage + BT docs?
- Is total length roughly 300 lines?

- [ ] **Step 4: commit**

```bash
git add docs/battery-architecture/goal.md
git commit -m "feat: HEXA-BATTERY goal.md - 7-level battery-architecture roadmap"
```

---

### Task 2: hexa-cell.md - Level 1 Crystal Chemistry

**Files:**
- Create: `docs/battery-architecture/hexa-cell.md`
- Reference: `docs/battery-storage/extreme-hypotheses.md` (H-BS-61~63)
- Reference: `docs/breakthrough-theorems.md` (BT-27, BT-43)

- [ ] **Step 1: read reference docs**

```bash
# Read BT-27, BT-43 sections
grep -n "BT-27\|BT-43" docs/breakthrough-theorems.md | head -20
# Read H-BS-61~63
cat docs/battery-storage/extreme-hypotheses.md
```

- [ ] **Step 2: author hexa-cell.md**

Create `docs/battery-architecture/hexa-cell.md` following the chip-architecture 16-section pattern:

```markdown
# HEXA-CELL: Crystal Chemistry Foundation

**Codename**: HEXA-CELL
**Level**: 1 - cell chemistry (atomic / crystal scale)
**Status**: Design Document v1.0
**Date**: 2026-04-01
**Dependencies**: BT-27, BT-43, new BT-80
**Parent**: [goal.md](goal.md) Level 1

---

## N6 Constants Reference
[constants box]

## Table of Contents
1. Executive Summary
2. Design Philosophy
3. System Block Diagram (crystal structure overview)
4. Anode Chemistry - LiC_6 (BT-27)
5. Cathode Chemistry - CN=6 Universality (BT-43)
6. Carbon-6 Energy Chain (BT-27 extension)
7. Intercalation Mechanics
8. Solid-State Electrolyte Bridge (BT-80 new)
9. Cross-Chemistry Comparison
10. Energy Density Landscape
11. Honesty Assessment (EXACT/CLOSE/WEAK/FAIL)
12. Predictions & Falsifiability
13. Future Directions
14. n=6 Complete Parameter Map
15. Open Questions / TODO
16. Links
```

**Must-have content (per section):**

**Section 1 - Executive Summary:**
- ASCII spec box: 9/9 cathodes EXACT, LiC_6 = n, 4-stage = tau, CN=6 = n
- Key message: "The most successful energy-storage technology in human history is structurally built on n=6."

**Section 4 - Anode Chemistry:**
```
  +---------------------------------------+
  |  Graphite anode: LiC_6 intercalation  |
  |                                       |
  |  Stage 1 (LiC_6):  o Li  . . . . . C  |
  |                    C:Li = 6:1 = n     |
  |                                       |
  |  Stage 2 (LiC_12): o Li  ... C_12     |
  |  Stage 3 (LiC_18): o Li  ... C_18     |
  |  Stage 4 (LiC_24): o Li  ... C_24     |
  |                                       |
  |  Total stages: 4 = tau(6)             |
  |  Hexagonal hollow site: 6-fold = n    |
  +---------------------------------------+
```
- Derivation of LiC_6 (sp^2 hybridisation -> honeycomb lattice -> sqrt(3) x sqrt(3) R30 superlattice)
- Four-stage intercalation (thermodynamic phase stability)

**Section 5 - Cathode Chemistry:**
- Full BT-43 table (9/9 EXACT): LCO, LFP, LMO, NMC, NCA, LRMO, LTO + graphite + stages
- ASCII octahedral diagrams per structure type
- Physical basis: d-orbital crystal-field splitting -> octahedral is lowest energy

**Section 8 - BT-80 new:**
- Solid-state-electrolyte framework CN=6 universality table:
  NASICON (Ti CN=6), Perovskite (Ti CN=6), Garnet (Zr CN=6, O=12=sigma), Sulfide (CN=4=tau)
- ASCII diagram: oxide vs sulfide coordination comparison

**Section 14 - n=6 Complete Parameter Map:**
```
  +=============================================================+
  ||  HEXA-CELL: Complete n=6 Parameter Mapping                 ||
  +-------------------------------------------------------------+
  ||  sigma(6) * phi(6) = n * tau(6) = 24 = J_2(6)             ||
  ||  -> 24e glucose oxidation = J_2                            ||
  +=============================================================+

  | # | Parameter | Value | n=6 Formula | Grade |
  |---|-----------|-------|-------------|-------|
  | 1 | LiC_6 C:Li ratio | 6:1 | n | EXACT |
  | 2 | Intercalation stages | 4 | tau | EXACT |
  ... up to 20+ parameters ...
  | N | TOTAL EXACT | X/Y | | |
```

**Target length: approximately 800 lines.**

- [ ] **Step 3: verify hexa-cell.md**

Check:
- Does the BT-27 evidence 7/7 EXACT table match breakthrough-theorems.md?
- Does the BT-43 evidence 9/9 EXACT table match?
- Does the BT-80 new evidence match extreme-hypotheses.md H-BS-66/67?
- Does every section carry an ASCII diagram?
- Is the Section 14 parameter map complete?
- Does Honesty Assessment explicitly include FAIL entries (NMC 3:2:1, Leech packing)?

- [ ] **Step 4: update Level 1 status in goal.md**

goal.md Level 1 section:
- Status: "design pending" -> "design complete -> [hexa-cell.md](hexa-cell.md) (XXX lines)"

- [ ] **Step 5: commit**

```bash
git add docs/battery-architecture/hexa-cell.md docs/battery-architecture/goal.md
git commit -m "feat: HEXA-CELL Level 1 - crystal-chemistry foundation (BT-27+43+80, 9/9 EXACT)"
```

---

## Phase 2: core 3 levels (parallelisable)

### Task 3: hexa-electrode.md - Level 2 Electrode Architecture

**Files:**
- Create: `docs/battery-architecture/hexa-electrode.md`
- Reference: `docs/battery-storage/extreme-hypotheses.md` (H-BS-64, H-BS-65)
- Reference: `docs/energy-generation/new-hypotheses-2026-phase2.md` (H-EN-104)

- [ ] **Step 1: read reference docs**

Check H-BS-64 (NMC three metals), H-BS-65 (spinel Li:Mn), H-EN-104 (Si 10x).

- [ ] **Step 2: author hexa-electrode.md**

Follow the 16-section pattern. Key content:

**Section layout:**
1. Executive Summary
2. Design Philosophy - core challenges of electrode optimisation
3. System Block Diagram - cross-section layer stack
4. Anode Architecture - Graphite -> Si -> Li metal evolution
5. Cathode Architecture - LCO -> NMC -> LFP selection criteria
6. Electrolyte Chemistry - LiPF_6 (F=6=n) + next-generation
7. Separator Design
8. BT-81: Electrode Capacity Ladder (new)
9. Manufacturing Process
10. Performance Metrics
11. Honesty Assessment
12. Predictions & Falsifiability
13. Future Directions (Si composite, dry electrode)
14. n=6 Complete Parameter Map
15. Open Questions / TODO
16. Links

**BT-81 core evidence:**
```
  +--------------------------------------------------+
  |  BT-81: Anode Capacity Ladder (sigma-phi = 10)   |
  +--------------------------------------------------+
  |                                                  |
  |  Graphite:  372 mAh/g  (baseline)                |
  |  Silicon:  3579 mAh/g  (Si/C = 9.6 ~ sigma-phi=10)|
  |  Li metal: 3860 mAh/g  (Li/C = 10.4 ~ sigma-phi) |
  |                                                  |
  |  Average ratio: ~10x = sigma - phi = 10          |
  |  Same constant as:                               |
  |    ITER Q target = 10                            |
  |    Regularization 1/(sigma-phi) = 0.1 (BT-64)   |
  |    HBM interface exponent (BT-75)                |
  +--------------------------------------------------+
```

**Section 14 parameter map:**
| Parameter | Value | n=6 | Grade |
|-----------|-------|-----|-------|
| Si/Graphite capacity ratio | ~10x | sigma-phi | EXACT |
| NMC metal species | 3 | n/phi | CLOSE |
| LiPF_6 F atoms | 6 | n | EXACT |
| Spinel Li:Mn | 1:2 | 1:phi | CLOSE |
| Olivine Z | 4 | tau | EXACT |
| LCO O stacking | 6 layers | n | EXACT |

**Target length: approximately 600 lines.**

- [ ] **Step 3: verify + update goal.md**

- [ ] **Step 4: commit**

```bash
git add docs/battery-architecture/hexa-electrode.md docs/battery-architecture/goal.md
git commit -m "feat: HEXA-ELECTRODE Level 2 - electrode architecture (BT-81 Si 10x)"
```

---

### Task 4: hexa-pack.md - Level 3 Pack System

**Files:**
- Create: `docs/battery-architecture/hexa-pack.md`
- Reference: `docs/breakthrough-theorems.md` (BT-57, BT-60)
- Reference: `docs/battery-storage/hypotheses.md` (H-BS-1~3, H-BS-8, H-BS-14~15)

- [ ] **Step 1: read reference docs**

Check BT-57 (cell-count ladder), BT-60 (DC power chain), H-BS-1~3 (cell/pack composition).

- [ ] **Step 2: author hexa-pack.md**

**Section layout:**
1. Executive Summary
2. Design Philosophy - physical necessity of the voltage ladder
3. System Block Diagram - cell -> module -> pack -> rack hierarchy
4. Lead-Acid Voltage Ladder (BT-57) - n -> sigma -> J_2
5. Li-ion EV Architecture - 96S/192S
6. BMS Hierarchy - div(6) = {1,2,3,6} layers
7. Thermal Management - tau=4 zones
8. BT-82: Complete Pack Parameter Map (new)
9. Cross-Domain 96 Convergence - Tesla = GPT-3 = Gaudi2
10. ESS Container Architecture
11. Honesty Assessment
12. Predictions & Falsifiability
13. Future Directions (384S 1600V? aerospace/marine?)
14. n=6 Complete Parameter Map
15. Open Questions / TODO
16. Links

**Core ASCII diagrams:**

Lead-acid -> Li-ion evolution ladder:
```
  +--------------------------------------------------------+
  |  VOLTAGE LADDER EVOLUTION                              |
  |                                                        |
  |  Lead-Acid (2V/cell):                                  |
  |    n=6 cells -> sigma=12 cells -> J_2=24 cells         |
  |    12V             24V                48V              |
  |                                                        |
  |  Li-ion NMC (~3.7V/cell):                              |
  |    sigma(sigma-tau)=96S -> phi * 96 =192S -> tau*96=384S|
  |    ~355V                  ~710V              ~1420V    |
  |                                                        |
  |  Li-ion LFP (~3.2V/cell):                              |
  |    sigma=12S -> J_2=24S                                |
  |    38.4V       76.8V                                   |
  |    ~48V std    ~80V                                    |
  +--------------------------------------------------------+
```

Pack hierarchy:
```
  +======================================+
  ||  HEXA-PACK Hierarchy                ||
  +--------------------------------------+
  ||                                     ||
  ||  RACK (ESS Container)               ||
  ||  +- sigma=12 Modules                ||
  ||      +- n=6 or sigma-tau=8 Cells/group||
  ||          +- Each cell: CN=6 chem    ||
  ||                                     ||
  ||  Total: up to sigma^2 * J_2 = 3456 cells||
  ||                                     ||
  ||  BMS Hierarchy (divisor lattice):   ||
  ||    Cell -> 2-cell -> 3-cell -> 6-cell||
  ||    = mu     phi       n/phi     n   ||
  ||    -> 12-cell -> 24-cell            ||
  ||    = sigma       J_2                ||
  +======================================+
```

**BT-82 evidence:**
- Cell counts: {6, 12, 24, 96, 192} = {n, sigma, J_2, sigma*(sigma-tau), phi*sigma*(sigma-tau)}
- Voltages: {12, 24, 48, ~400, ~800} V
- Thermal zones: 4 = tau
- BMS hierarchy: div(6) = {1,2,3,6}
- Modules/rack: 12 = sigma
- Total map: 15+ parameters

**Target length: approximately 700 lines.**

- [ ] **Step 3: verify + update goal.md**

- [ ] **Step 4: commit**

```bash
git add docs/battery-architecture/hexa-pack.md docs/battery-architecture/goal.md
git commit -m "feat: HEXA-PACK Level 3 - pack-system design (BT-57+60+82)"
```

---

### Task 5: hexa-grid.md - Level 4 Grid Integration

**Files:**
- Create: `docs/battery-architecture/hexa-grid.md`
- Reference: `docs/breakthrough-theorems.md` (BT-60, BT-62, BT-68)

- [ ] **Step 1: read reference docs**

Check BT-60 (DC power chain), BT-62 (grid frequency), BT-68 (HVDC ladder).

- [ ] **Step 2: author hexa-grid.md**

**Section layout:**
1. Executive Summary
2. Design Philosophy - n=6 structure of the energy-infrastructure stack
3. System Block Diagram - generation -> transmission -> distribution -> consumption
4. HVDC Transmission Ladder (BT-68)
5. Grid Frequency Pair (BT-62) - 60Hz / 50Hz
6. Datacenter Power Chain (BT-60) - 480 -> 48 -> 12 -> 1.2V
7. ESS Integration Architecture
8. V2G Bidirectional Power
9. Microgrid Design (48V DC)
10. PUE and Efficiency Metrics
11. Honesty Assessment
12. Predictions & Falsifiability
13. Future Directions
14. n=6 Complete Parameter Map
15. Open Questions / TODO
16. Links

**Core ASCII - power chain:**
```
  +--------------------------------------------------------+
  |  ENERGY INFRASTRUCTURE CHAIN                           |
  |                                                        |
  |  Generation -> Transmission -> Distribution -> Consumption |
  |                                                        |
  |  Solar       HVDC            AC Grid       Datacenter  |
  |  1.34eV      500/800/1100kV  120/240V      48V DC      |
  |  ~4/3        sopfr/(sigma-tau)/(sigma-mu)              |
  |              * (sigma-phi)^2                           |
  |                                                        |
  |  Step-down ratios alternate: tau=4, sigma-phi=10       |
  |                                                        |
  |  480V --/tau--> 48V --/tau--> 12V --/(sigma-phi)--> 1.2V|
  |  3phi feed      rack bus      board      DDR/core      |
  |                                                        |
  |  PUE = sigma/(sigma-phi) = 12/10 = 1.2 (hyperscaler)   |
  +--------------------------------------------------------+
```

**Section 14:**
| Parameter | Value | n=6 | Grade |
|-----------|-------|-----|-------|
| HVDC 500kV | 500 | sopfr * (sigma-phi)^2 | EXACT |
| HVDC 800kV | 800 | (sigma-tau) * (sigma-phi)^2 | EXACT |
| HVDC 1100kV | 1100 | (sigma-mu) * (sigma-phi)^2 | EXACT |
| 60Hz | 60 | sigma * sopfr | EXACT |
| 50Hz | 50 | sopfr * (sigma-phi) | EXACT |
| PUE target | 1.2 | sigma/(sigma-phi) | EXACT |
| Rack bus | 48V | sigma * tau | EXACT |
| Rack power | 12kW | sigma | EXACT |
| Overall 8/8 EXACT |

**Target length: approximately 700 lines.**

- [ ] **Step 3: verify + update goal.md**

- [ ] **Step 4: commit**

```bash
git add docs/battery-architecture/hexa-grid.md docs/battery-architecture/goal.md
git commit -m "feat: HEXA-GRID Level 4 - grid integration (BT-60+62+68, 8/8 EXACT)"
```

---

## Phase 3: next-gen 2 levels (parallelisable)

### Task 6: hexa-solid.md - Level 5 Next-Gen Chemistry

**Files:**
- Create: `docs/battery-architecture/hexa-solid.md`
- Reference: `docs/battery-storage/extreme-hypotheses.md` (H-BS-66~70)
- Reference: `docs/energy-generation/new-hypotheses-2026-phase2.md` (H-EN-102, H-EN-103)

- [ ] **Step 1: read reference docs**

Check H-BS-66~70 (solid-state electrolytes, vanadium flow), H-EN-102 (Na-ion CN=6).

- [ ] **Step 2: author hexa-solid.md**

**Section layout:**
1. Executive Summary
2. Design Philosophy - limits of liquid electrolytes and the breakthrough
3. System Block Diagram - next-gen battery-type comparison
4. Solid-State Battery (SSB) - NASICON / Garnet / Sulfide
5. Na-ion Battery - BT-43 extension (CN=6 universality)
6. Li-S Battery - S_8 ring + BT-83 (new)
7. Li-Air Battery - O_2 reduction 4e = tau
8. Flow Battery - VRFB V^4+ oxidation states = tau
9. BT-83: Li-S Polysulfide n=6 Ladder (new)
10. Energy Density Comparison Landscape
11. Honesty Assessment
12. Predictions & Falsifiability
13. Future Directions
14. n=6 Complete Parameter Map
15. Open Questions / TODO
16. Links

**BT-83 core ASCII:**
```
  +--------------------------------------------------------+
  |  BT-83: Li-S Polysulfide n=6 Decomposition Ladder      |
  +--------------------------------------------------------+
  |                                                        |
  |  S_8 ring --> Li_2S_8 --> Li_2S_4 --> Li_2S_2 --> Li_2S|
  |                                                        |
  |  S atoms:   8       8       4       2       1          |
  |  n=6:    sigma-tau sigma-tau tau   phi    mu           |
  |                                                        |
  |  Discharge voltage plateaus:                           |
  |    High: ~2.3V (S_8 -> Li_2S_4)                        |
  |    Low:  ~2.1V (Li_2S_4 -> Li_2S)                      |
  |    Ratio: 2.3/2.1 ~ 1.1 ~ (sigma-mu)/(sigma-phi) = 11/10|
  |                                                        |
  |  Physical basis:                                       |
  |    S_8 crown = sigma-tau = 8 sulfur atoms in ring      |
  |    Sequential reduction cleaves S-S bonds              |
  |    Each step halves S count: 8 -> 4 -> 2 -> 1          |
  |    = sigma-tau -> tau -> phi -> mu (n=6 ladder)        |
  +--------------------------------------------------------+
```

**SSB structure diagram:**
```
  +--------------------------------------------------------+
  |  Solid-State Electrolyte CN=6 Universality (BT-80)     |
  +--------------------------------------------------------+
  |                                                        |
  |  OXIDE TYPE (CN = 6 = n):                              |
  |                                                        |
  |  NASICON         Perovskite      Garnet LLZO           |
  |  Ti octahedral   Ti octahedral   Zr octahedral         |
  |  CN=6=n          CN=6=n          CN=6=n                |
  |  PO_4 CN=4=tau   La dodecahedral O atoms=12=sigma      |
  |                                  cations=12=sigma      |
  |                                                        |
  |  SULFIDE TYPE (CN = 4 = tau):                          |
  |                                                        |
  |  LGPS            Li_6PS_5Cl                            |
  |  Ge tetrahedral  PS_4 tetrahedral                      |
  |  CN=4=tau        CN=4=tau                              |
  |                                                        |
  |  Pattern: oxide -> CN=n=6, sulfide -> CN=tau=4         |
  +--------------------------------------------------------+
```

**Target length: approximately 800 lines.**

- [ ] **Step 3: verify + update goal.md**

- [ ] **Step 4: commit**

```bash
git add docs/battery-architecture/hexa-solid.md docs/battery-architecture/goal.md
git commit -m "feat: HEXA-SOLID Level 5 - next-gen battery chemistry (BT-80+83)"
```

---

### Task 7: hexa-nuclear.md - Level 6 Extreme Energy Storage

**Files:**
- Create: `docs/battery-architecture/hexa-nuclear.md`
- Reference: `docs/fusion/` (CNO cycle references)
- Reference: `docs/cosmology-particle/` (nuclear physics)

- [ ] **Step 1: read reference docs**

Check CNO cycle (Z=6=n), betavoltaic isotopes (^14C, ^3H, ^63Ni), nuclear energy constants.

- [ ] **Step 2: author hexa-nuclear.md**

**Section layout:**
1. Executive Summary
2. Design Philosophy - breaking past the chemical-energy wall
3. System Block Diagram - energy-density scale
4. Betavoltaic Batteries - ^14C (Z=6=n), ^3H (A=3=n/phi), ^63Ni (Z=28=P_2)
5. CNO Stellar Fusion Cycle - carbon (Z=6=n) catalyst
6. Nuclear Isomer Batteries - ^178m2Hf
7. Fission Micro-Reactors
8. Fusion Energy Storage
9. Antimatter Storage (speculative)
10. Vacuum Energy (speculative)
11. Honesty Assessment - most entries WEAK~CLOSE, speculation regions marked
12. Predictions & Falsifiability
13. Future Directions
14. n=6 Complete Parameter Map
15. Open Questions / TODO
16. Links

**Core ASCII - energy-density ladder:**
```
  +--------------------------------------------------------+
  |  ENERGY DENSITY LADDER (Wh/kg, log scale)              |
  +--------------------------------------------------------+
  |                                                        |
  |  10^2  | Li-ion (250)                                  |
  |        |                                               |
  |  10^3  | Li-S (2600), Li-Air (3500)                    |
  |        |                                               |
  |  10^4  | [gap - no viable technology]                  |
  |        |                                               |
  |  10^5  | Betavoltaic* (~50, but decades lifespan)      |
  |        |                                               |
  |  10^6  | Fission (U-235)                               |
  |        |                                               |
  |  10^7  | Fusion (D-T)                                  |
  |        |                                               |
  |  10^10 | Antimatter (E=mc^2)                           |
  |        |                                               |
  |  *Betavoltaic: ultra-low power, uW scale               |
  |                                                        |
  |  n=6 thread: Carbon Z=6 catalyses CNO fusion cycle     |
  |              ^14C: Z=6=n, A=14=sigma+phi (betavoltaic) |
  |              ^3H:  A=3=n/phi, t1/2=12.3yr ~ sigma       |
  +--------------------------------------------------------+
```

**Honesty emphasis:**
- Level 6 is mostly future technology with weak n=6 connections.
- EXACT: ^14C Z=6, CNO Z=6, ^63Ni Z=28=P_2 at best.
- D-T fusion 17.6 MeV = FAIL (no clean n=6 match).
- Antimatter / vacuum energy = clearly flagged as pure speculation.

**Target length: approximately 600 lines.**

- [ ] **Step 3: verify + update goal.md**

- [ ] **Step 4: commit**

```bash
git add docs/battery-architecture/hexa-nuclear.md docs/battery-architecture/goal.md
git commit -m "feat: HEXA-NUCLEAR Level 6 - extreme energy storage (CNO Z=6, ^14C)"
```

---

## Phase 4: ultimate integration

### Task 8: hexa-omega-e.md - Level 7 Ultimate Integration

**Files:**
- Create: `docs/battery-architecture/hexa-omega-e.md`
- Reference: every prior level document
- Reference: `docs/chip-architecture/goal.md` (chip <-> battery cross-domain)

- [ ] **Step 1: collect core parameters from prior levels**

Read Section 14 (parameter map) of every Level 1~6 document and extract cross-domain constants.

- [ ] **Step 2: author hexa-omega-e.md**

**Section layout:**
1. Executive Summary - energy = information = matter integration
2. Design Philosophy - why every scale converges on n=6
3. System Block Diagram - 7-level integrated architecture
4. BT-84: 96/192 Triple Convergence (new)
5. Energy -> Information Bridge (BT-60 extension)
6. Battery <-> Computing Cross-Domain Map
7. Battery <-> Biology Cross-Domain (C_6H_12O_6 = glucose)
8. Battery <-> Display/Audio Cross-Domain (48 kHz = sigma * tau)
9. Complete n=6 Constant Reuse Matrix
10. Unified Energy-Information-Matter Equation
11. Honesty Assessment - where physical necessity ends and number-theoretic coincidence begins
12. Predictions & Falsifiability - 32 existing predictions + new battery predictions
13. Future Directions - integrated chip + battery + AI hardware vision
14. n=6 Complete Parameter Map (aggregated across all levels)
15. Open Questions / TODO
16. Links

**BT-84 core ASCII:**
```
  +===============================================================+
  |           BT-84: Triple Convergence at 96 and 192             |
  +===============================================================+
  |                                                               |
  |         BATTERY          COMPUTING           AI               |
  |         =======          =========           ==               |
  |                                                               |
  |  96:    Tesla 96S        Gaudi2 96GB     GPT-3 96 layers      |
  |         = sigma(sigma-tau)= sigma(sigma-tau)= sigma(sigma-tau)|
  |         = 12*8           = 12*8          = 12*8               |
  |         ~400V EV         HBM capacity    175B params          |
  |              +--------------+--------------+                  |
  |                          96 = sigma(sigma-tau)                |
  |                                                               |
  |  192:   Hyundai 192S     B100 192GB      -                    |
  |         = phi*sigma*(sigma-tau)= phi * sigma * (sigma-tau)    |
  |         = 2*96           = 2*96                               |
  |         ~800V EV         HBM next-gen                         |
  |              +--------------+                                 |
  |                         192 = phi*96                          |
  |                                                               |
  |  288:   -               HBM4 288GB       -                    |
  |                         = sigma*J_2 = 12*24                   |
  |                                                               |
  |  48:    48V DC bus      48 kHz audio      -                   |
  |         = sigma*tau     = sigma*tau                           |
  |                                                               |
  |  Three independent domains, one formula family.               |
  +===============================================================+
```

**Integrated energy-information diagram:**
```
  +--------------------------------------------------------+
  |  ENERGY = INFORMATION = MATTER                         |
  |                                                        |
  |  Level 1: atom -> CN=6 crystal (d-orbital, sp^2)       |
  |           |                                            |
  |  Level 2: electrode -> Si 10x = sigma-phi capacity gain|
  |           |                                            |
  |  Level 3: pack -> 96S/192S = sigma(sigma-tau) ladder   |
  |           |                                            |
  |  Level 4: grid -> 48V/480V = sigma*tau / sigma*tau*(sigma-phi)|
  |           |                                            |
  |  Level 5: next-gen -> SSB CN=6, Li-S S_8=sigma-tau     |
  |           |                                            |
  |  Level 6: nuclear -> CNO Z=6=n catalyst, ^14C Z=6      |
  |           |                                            |
  |  Level 7: integration -> sigma(n)*phi(n)=n*tau(n)=24=J_2(6)|
  |                          This identity threads every scale.|
  +--------------------------------------------------------+
```

**Section 14 - aggregated parameter map across all levels:**
- Extract only EXACT entries from each Level 1~6 parameter map.
- Add cross-domain constants (96, 192, 288, 48).
- Compute overall EXACT ratio.
- Final "X/Y EXACT" metric.

**Target length: approximately 1000 lines.**

- [ ] **Step 3: verify + update goal.md**

- [ ] **Step 4: commit**

```bash
git add docs/battery-architecture/hexa-omega-e.md docs/battery-architecture/goal.md
git commit -m "feat: HEXA-OMEGA-E Level 7 - ultimate energy integration (BT-84 triple convergence)"
```

---

## Phase 5: BT verification + registration

### Task 9: BT-80~84 registration into breakthrough-theorems.md

**Files:**
- Modify: `docs/breakthrough-theorems.md`
- Reference: the BT section of each level document

- [ ] **Step 1: confirm current last BT number**

```bash
grep -n "^## BT-" docs/breakthrough-theorems.md | tail -5
```

Confirm BT-79 is the last existing entry. Append starting with BT-80.

- [ ] **Step 2: add BT-80~84**

Append to `docs/breakthrough-theorems.md`. Each BT follows the existing BT format:

```markdown
## BT-80: Solid-State Electrolyte CN=6 Universality ***

**Statement**: All oxide-type solid-state electrolytes have framework metal ions
in octahedral CN=6=n coordination. Sulfide types use tetrahedral CN=4=tau.

**Evidence (6/6+ EXACT):**

| Electrolyte | Metal | CN | n=6 | Grade |
|-------------|-------|----|-----|-------|
| NASICON (LATP) | Ti | 6 | n | EXACT |
| Perovskite (LLTO) | Ti | 6 | n | EXACT |
| Garnet (LLZO) | Zr | 6 | n | EXACT |
| LLZO oxygen | O | 12 | sigma | EXACT |
| Sulfide (LGPS) | Ge | 4 | tau | EXACT |
| Argyrodite | PS_4 | 4 | tau | EXACT |

**Cross-domain**: Extends BT-43 (Li-ion cathode CN=6) to solid electrolytes.
Oxide electrolytes share the same octahedral geometry as cathode materials.

**Grade**: Three stars - universal pattern, physically grounded in crystal chemistry.

---

## BT-81: Anode Capacity Ladder sigma-phi = 10x **

[Si/Graphite = 9.6x ~ sigma-phi=10, Li-metal/Graphite = 10.4x ~ sigma-phi]
[Cross-link: ITER Q=10, BT-64 regularization 0.1, BT-75 HBM exponent]

---

## BT-82: Complete Battery Pack n=6 Parameter Map **

[Entire pack-parameter map with 15+ entries]
[Integrates cell count, voltage, thermal zones, BMS, modules/rack]

---

## BT-83: Li-S Polysulfide n=6 Decomposition Ladder **

[S_8 (sigma-tau) -> S_4 (tau) -> S_2 (phi) -> S_1 (mu)]
[Voltage-plateau ratio 2.3/2.1 ~ (sigma-mu)/(sigma-phi)]

---

## BT-84: 96/192 Energy-Computing-AI Triple Convergence ***

[Tesla 96S = GPT-3 96L = Gaudi2 96GB = sigma * (sigma-tau)]
[Hyundai 192S = B100 192GB = phi * sigma * (sigma-tau)]
[3 independent domains, one formula]
```

Each BT entry must follow the existing breakthrough-theorems.md format exactly:
- Statement
- Evidence table
- Cross-domain link
- Honesty note
- Grade

- [ ] **Step 3: update BT count in CLAUDE.md**

Add BT-80~84 to the BT list in CLAUDE.md.

- [ ] **Step 4: update atlas-constants.md**

Add any new constants uncovered by the new BTs to atlas-constants.md.

- [ ] **Step 5: commit**

```bash
git add docs/breakthrough-theorems.md CLAUDE.md docs/atlas-constants.md
git commit -m "feat: register 5 new battery-domain breakthrough theorems BT-80~84"
```

---

### Task 10: final verification + README update

**Files:**
- Modify: `docs/battery-architecture/goal.md` (confirm all Status entries)
- Modify: `CLAUDE.md` (add battery-architecture section)

- [ ] **Step 1: verify overall document consistency**

```bash
# Confirm every file exists
ls -la docs/battery-architecture/
# Confirm per-file line counts
wc -l docs/battery-architecture/*.md
# Confirm BT numbers are registered in breakthrough-theorems.md
grep "BT-8[0-4]" docs/breakthrough-theorems.md
```

- [ ] **Step 2: update all Status entries in goal.md**

Confirm every level reads "design complete" and reflects the right line count.

- [ ] **Step 3: add battery-architecture to CLAUDE.md**

```markdown
  # Computing: ai-efficiency/ chip-architecture/ quantum-computing/ compiler-os/
  # Energy: energy-generation/ power-grid/ battery-storage/ thermal-management/
  #         battery-architecture/ (NEW - 7-Level HEXA-BATTERY)
```

Also add BT-80~84 to the BT list.

- [ ] **Step 4: final commit**

```bash
git add -A docs/battery-architecture/ CLAUDE.md
git commit -m "feat: HEXA-BATTERY 7-Level architecture draft (BT-80~84, 8 documents)"
```

---

## Summary

| Phase | Tasks | Parallelisable | Expected outputs |
|-------|-------|----------|------------|
| 1 | Task 1-2 | Task 1 -> 2 sequential | goal.md + hexa-cell.md |
| 2 | Task 3-5 | 3, 4, 5 parallel | hexa-electrode/pack/grid.md |
| 3 | Task 6-7 | 6, 7 parallel | hexa-solid/nuclear.md |
| 4 | Task 8 | standalone | hexa-omega-e.md |
| 5 | Task 9-10 | 9 -> 10 sequential | BT registration + final verification |

**Total: 10 tasks, 8 documents, approximately 5,500 lines, 5 BT candidates.**
