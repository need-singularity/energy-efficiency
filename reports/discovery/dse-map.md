# N6 DSE map - Design Space Exploration status across all domains

> Before starting ultimate-architecture work, always consult this map.
> Fixing an ultimate architecture without DSE is forbidden (CLAUDE.md rule).

---

## DSE status

```
  +-----------------------------------------------------------------------+
  |  Per-domain DSE completion status                                     |
  |                                                                       |
  |  [done] chip architecture  3,000 combos   -> Si+TSMC_N2+HEXA-P (100%, 86.38)  |
  |  [done] fusion            39,191,040 combos -> Tokamak+Nb3Sn+D_T (100%, 96.32) |
  |  [wip]  battery           goal.md drafted  -> DSE sweep not run yet  |
  |  [  ]   solar cell        not started                                 |
  |  [  ]   energy integration  not started (needs Cross-DSE)             |
  +-----------------------------------------------------------------------+
```

| # | Domain | Chain | Theoretical combos | Explored combos | Best n6% | Best Pareto | Best path | Status |
|---|--------|------|----------|----------|---------|------------|----------|------|
| 1 | Chip architecture | material x process x core x chip x system | 3,000 | 3,000 | 100% | 86.38 | Si+TSMC_N2+HEXA-P+HEXA-1_Half+DGX_Style | done |
| 2 | **Fusion** | **method x material x core x device x system** | **67,184,640** | **39,191,040** | **100%** | **96.32** | **Tokamak+Nb3Sn+Li_ceramic+RAFM+D_T+TF6+A3.0+B12+Q10+Rankine+DCLL+AC_50Hz** | **done** |
| 3 | Battery | material x process x core x chip x system | TBD | - | - | - | - | wip (goal.md drafted) |
| 4 | Solar cell | TBD | - | - | - | - | - | not started |

---

## Fusion DSE detail

```
  +---------------------------------------------------------------------+
  |  Ultimate fusion target path (Pareto #1, n6 EXACT = 14/14 = 100%)   |
  |                                                                     |
  |  Level 1        Level 2              Level 3                        |
  |  +----------+  +----------------+   +----------------+              |
  |  | Tokamak  |->| SC:  Nb3Sn     |-> | Heat: ICRH     |              |
  |  | PF=6=n   |  | Bl:  Li_ceramic|   | Conf: SC_coil  |              |
  |  | CS=6=n   |  | St:  RAFM     |   | Fuel: D_T      |              |
  |  +----------+  +----------------+   +-------+--------+              |
  |                                             |                       |
  |  Level 5              Level 4               v                       |
  |  +----------------+  +----------------+                             |
  |  | Pwr: Rankine   |<-| TF:  6=n       |                             |
  |  | TBR: DCLL 1.20 |  | A:   3.0=n/phi |                             |
  |  | Grid: 50Hz     |  | B:   12T=sigma |                             |
  |  +----------------+  | Q:   10=sopfr*phi |                          |
  |                      +----------------+                             |
  |                                                                     |
  |  n6 match detail:                                                   |
  |    PF=6=n v  CS=6=n v  B_max=24=J2 v  Coolant v                     |
  |    MW=6=n v  D+T=5=sopfr v  80%=tau/sopfr v                         |
  |    TF=6=n v  A=3=n/phi v  B=12=sigma v  Q=10=sopfr*phi v            |
  |    Eff=33%=1/3 v  TBR=1.20=sigma/(sigma-phi) v  50Hz=sopfr*(sigma-phi) v  |
  +---------------------------------------------------------------------+
```

### Per-method optimum comparison

| Method | Pareto | n6% | Q_gain | TRL | LCOE | Key combo |
|------|--------|-----|--------|-----|------|----------|
| **Tokamak** | **96.32** | **100%** | 100 | 90 | 86 | Nb3Sn+D_T+TF6+A3.0+B12+Q10 |
| Stellarator | 72.34 | 86% | 50 | 70 | 82 | Nb3Sn+D_T+TF6+A3.0+B12+Q10 |
| FRC | 59.56 | 86% | 20 | 50 | 78 | Nb3Sn+D_T+TF6+A3.0+B12+Q10 |
| ICF_Laser | 57.96 | 86% | 20 | 60 | 58 | Nb3Sn+D_T+TF6+A3.0+B12+Q10 |
| Mirror | 54.66 | 86% | 10 | 50 | 68 | Nb3Sn+D_T+TF6+A3.0+B12+Q10 |
| Z_Pinch | 47.06 | 86% | 10 | 40 | 38 | Nb3Sn+D_T+TF6+A3.0+B12+Q10 |

### Statistics

```
  Total theoretical combos:     67,184,640
  Incompatibles excluded:       27,993,600 (41.7%)
  Actually explored:            39,191,040
  Max n6 EXACT:                 100.0%
  Avg n6 EXACT:                 45.9%
  >=80% EXACT:                  60,096 (0.15%)
  >=60% EXACT:                  4,056,336 (10.35%)
```

---

## Cross-DSE candidates

> Trigger Cross-DSE once two or more domains are DSE-complete (CLAUDE.md rule).
> Current: chip + fusion = 2 complete -> **Cross-DSE is enabled**.

| Combo | Domain A | Domain B | Intersections | Status |
|------|---------|---------|--------|------|
| chip x fusion | chip-arch (3K) | fusion (39M) | Power-conversion / control IC, BMS, sensors | not started |
| battery x fusion | battery (TBD) | fusion (39M) | Storage + generation integration | waiting on battery DSE |
| chip x battery | chip-arch (3K) | battery (TBD) | BMS chip design | waiting on battery DSE |
| **Triple integration** | chip x battery x fusion | | Energy-compute-AI triple convergence (BT-84) | after all domains complete |

---

## DSE tools

| Tool | Path | Combos | Runtime |
|------|------|---------|----------|
| Chip DSE | `tools/dse-calc/dse-calc` | 3,000 | <1s |
| Fusion DSE | `tools/fusion-dse/fusion-dse` | 39M | a few seconds |
| Battery DSE | TBD | TBD | TBD |
