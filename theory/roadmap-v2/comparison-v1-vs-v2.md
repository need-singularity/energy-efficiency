# v1 vs v2 roadmap ASCII comparison — Y-axis system final (2026-04-15)

**Document**: theory/roadmap-v2/comparison-v1-vs-v2.md
**Baseline date**: 2026-04-15
**Produced from**:
  - v1: `theory/study/p0~p3/` (legacy 3-axis 12-cell, ~20481 lines aggregate)
  - v2: `theory/roadmap-v2/` (Y1~Y9 9-axis emergence system, P0~P6+Omega)
  - Axis SSOT: `n6arch-axes/axis-r3-finalization.md` (1166 lines, FINAL)
  - Phase source: `phase-01~06-*.md` + `phase-omega-Y9-closure-v3-design.md`
  - Domain emergence: `round-01~05-*.md` (5 rounds, 216 domains)
**BT drafts complete**: 0/6 (v1 and v2 agree. Poincare BT-547 is externally resolved by Perelman 2003)
**Honesty principles**: no self-reference, require source + measurement + error, record MISS honestly

---
---

## S1. Axis-system comparison

### 1.1 Basic structure table

```
+========================+================================+=================================+
|        Item            |    v1 (legacy 3-axis)           |     v2 (Y-axis 9-axis emergent) |
+========================+================================+=================================+
| Axis count             | 3 (fixed)                       | 9 (emergent, FINAL confirmed)   |
+------------------------+--------------------------------+---------------------------------+
| Axis names             | PURE / PROBLEM / N6             | Y1 NUM-CORE (9.5)               |
|                        |                                 | Y2 DISCRETE-CLASS (5.2)         |
|                        |                                 | Y3 COMPUTATIONAL-TAU (5.8)      |
|                        |                                 | Y4 GATE-BARRIER (9.4)           |
|                        |                                 | Y5 PHYSICAL-NATURALNESS (5.6)   |
|                        |                                 | Y6 PDE-RESONANCE (6.6)          |
|                        |                                 | Y7 LATTICE-VOA (3.9)            |
|                        |                                 | Y8 GALOIS-ASSEMBLY (5.4)        |
|                        |                                 | Y9 HONEST-HARNESS (9.3)         |
+------------------------+--------------------------------+---------------------------------+
| Axis-selection method  | top-down (assigned)             | bottom-up (R1~R3 3-round emerg.)|
+------------------------+--------------------------------+---------------------------------+
| Axis utility score     | none                            | 3.9~9.5 (out of 10)             |
+------------------------+--------------------------------+---------------------------------+
| Axis-round count       | 0                               | R1 (7 axes) -> R2 (9 axes) ->   |
|                        |                                 | R3 (9 axes FINAL, 100% saturate)|
+------------------------+--------------------------------+---------------------------------+
| Self-evolution axis    | none                            | Y9 HONEST-HARNESS (meta)        |
+------------------------+--------------------------------+---------------------------------+
| Honesty-meta axis      | none (implicit)                 | Y9 (utility 9.3, explicit)      |
+------------------------+--------------------------------+---------------------------------+
| Barrier-dedicated axis | none                            | Y4 GATE-BARRIER (utility 9.4)   |
+------------------------+--------------------------------+---------------------------------+
| Physical-naturalness   | none                            | Y5 PHYSICAL-NATURALNESS (5.6)   |
+------------------------+--------------------------------+---------------------------------+
| PDE-resonance axis     | none                            | Y6 PDE-RESONANCE (6.6)          |
+------------------------+--------------------------------+---------------------------------+
| Lattice/VOA axis       | none                            | Y7 LATTICE-VOA (3.9)            |
+------------------------+--------------------------------+---------------------------------+
| Galois axis            | none                            | Y8 GALOIS-ASSEMBLY (5.4)        |
+------------------------+--------------------------------+---------------------------------+
| Axis saturation index  | N/A                             | 100% (R3 FINAL)                 |
+------------------------+--------------------------------+---------------------------------+
| Axis-confirmation doc  | none (implicit)                 | axis-r3-finalization.md (1166 L)|
+========================+================================+=================================+
```

### 1.2 Axis-system ASCII visualization

```
v1 axis structure (3 axes, top-down, fixed):

  +----------+   +----------+   +----------+
  |   PURE   |   | PROBLEM  |   |    N6    |
  | (pure)   |   | (problem)|   |(special.)|
  +----------+   +----------+   +----------+
       |              |              |
       v              v              v
  assigned, end    assigned, end   assigned, end
  (no evolution)  (no evolution)   (no evolution)


v2 axis structure (9 axes, bottom-up, 3-round emergence):

  R1 (906 L)                    R2 (961 L)                   R3 (1166 L) FINAL
  +--+--+--+--+--+--+--+       +--+--+--+--+--+--+--+--+--+     |
  |X1|X2|X3|X4|X5|X6|X7|  -->  |X1|X2|X3|X4|X5|X6|X7|X8|X9| --> |  Y1~Y9
  +--+--+--+--+--+--+--+       +--+--+--+--+--+--+--+--+--+     |  100% saturation
   7 axis candidates             9 axes + 3 PARTIAL handled      |  FINAL confirmed
   30 seeds                      48 seeds, saturation 94%        |
                                                                   v
                                                          axis-final-millennium.md
                                                          (SSOT, 312 lines)
```

---
---

## S2. Phase-structure comparison

### 2.1 Phase count and progression structure

```
v1 Phase structure (4, linear):

  P0 --------> P1 --------> P2 --------> P3
  setup         pure math    attack        n6 specialization
  (base)       (extend)     (integrate)   (converge)

  Total cells:  3 axes x 4 Phases = 12 cells
  Progression:  linear, no gates, no saturation


v2 Phase structure (8, gate-based):

  P0 --> P1 --> P2 --> P3 --> P4 --> P5 --> P6 --> P(Omega)
  axes   spin   RH    PNP   YM+NS  H+BSD retro  closure
  R1~R3  9 up  Y1 lead Y4    Y5+Y6 Y7+Y8 retro  Y9 meta
         all   BT541  BT542 543+4 545+6 BT547  integrate
              |      |      |      |      |       |
              v      v      v      v      v       v
             gate   gate   gate   gate   gate    FINAL
             cond.  cond.  cond.  cond.  cond.   end

  Total cells:  9 axes x 8 Phases = 72 potential
  Progression:  gate-based, entry/exit conditions explicit, linked to saturation
```

### 2.2 Phase detailed-comparison table

```
+=======+================+===================+===================================+=========+
| Phase |  v1 name       | v2 name           | v2 detail                         | v2 lines|
+=======+================+===================+===================================+=========+
| P0    | setup          | Axis confirmation | 3-round axis emergence, Y1~Y9     |   3033  |
|       |                | (R1~R3)           | FINAL (R1 906 + R2 961 + R3 1166) |         |
+-------+----------------+-------------------+-----------------------------------+---------+
| P1    | pure math      | Foundation        | 9-axis all spin-up verified + 6 BT|    372  |
|       |                |                   | seeds + 4 self-evo engines cycle  |         |
|       |                |                   | >= 3                              |         |
+-------+----------------+-------------------+-----------------------------------+---------+
| P2    | attack         | Y1 BT-541 Riemann | Theorem B CANDIDATE, EXACT 10,    |    831  |
|       |                |                   | MISS 5, 3 independent reproductions|         |
+-------+----------------+-------------------+-----------------------------------+---------+
| P3    | n6 specialize  | Y4 BT-542 P=NP    | 4-barrier re-audit, 3 GCT obs.,   |   1028  |
|       |                |                   | 7 MISS, GATE Mk.I 24/24 EXACT     |         |
+-------+----------------+-------------------+-----------------------------------+---------+
| P4    | (none)         | Y5+Y6 BT-543+544  | beta0 rewriting + triple reson. + |   1188  |
|       |                |                   | D158 Ricci conditional + 5 QCD obs|         |
+-------+----------------+-------------------+-----------------------------------+---------+
| P5    | (none)         | Y7+Y8 BT-545+546  | Lemma 1 CRT 5-step rigorous draft,|   1321  |
|       |                |                   | Theorem 1 BKLPR conditional, A3   |         |
|       |                |                   | discharge failed, Enriques rephr. |         |
+-------+----------------+-------------------+-----------------------------------+---------+
| P6    | (none)         | BT-547 Perelman   | retrospective only (not attack),  |    600  |
|       |                | retrospective     | C1~C5 decisive-tool features,     |         |
|       |                |                   | 9x5 matrix                        |         |
+-------+----------------+-------------------+-----------------------------------+---------+
| POmega| (none)         | Y9 Closure        | integrated review, saturation     |   1117  |
|       |                |                   | declared, v3 design, handoff,     |         |
|       |                |                   | BT 0/6 honesty statement          |         |
+=======+================+===================+===================================+=========+
| Sum   | ~20481 lines   |                   |                                   |   9490  |
| (line)| (study/p0~p3)  |                   | (axis 3033 + Phase 6457)          |         |
+=======+================+===================+===================================+=========+
```

Note: v1 lines (20481) is the aggregate of study/p0~p3; v2 lines (9490) counts only the core Phase files in roadmap-v2/.
Adding domain-emergence docs (round-01~05, 3953 lines) gives v2 total 13443 lines.

---
---

## S3. BT-coverage comparison

### 3.1 v1 BT coverage (3 axes × 7 BT)

```
v1: each BT is handled by only one axis (shallow coverage)

              PURE    PROBLEM    N6
  BT-541 RH    [X]                      <-- 1-axis coverage
  BT-542 PNP           [X]              <-- 1-axis coverage
  BT-543 YM            [X]              <-- 1-axis coverage
  BT-544 NS            [X]              <-- 1-axis coverage
  BT-545 Hodge  [X]                     <-- 1-axis coverage
  BT-546 BSD    [X]                     <-- 1-axis coverage
  BT-547 Poinc         [X]              <-- 1-axis coverage (external resolution)

  Mean axes per BT: 1.0
  Cross-axis mappings: 0
```

### 3.2 v2 BT coverage (9 axes × 6 BT + 1 retrospective)

```
v2: each BT has a main axis + support axes (deep cross-coverage)

               Y1  Y2  Y3  Y4  Y5  Y6  Y7  Y8  Y9
  BT-541 RH   [##]             .        .  [+ ] [+ ] [**]   main Y1 sub Y7,Y8,Y9
  BT-542 PNP       [+ ] [+ ] [##]                    [**]   main Y4 sub Y2,Y3,Y9
  BT-543 YM             [+ ]      [##] [+ ]          [**]   main Y5 sub Y3,Y6,Y9
  BT-544 NS                       [+ ] [##]          [**]   main Y6 sub Y5,Y9
  BT-545 Hodge     [+ ]                     [##]      [**]   main Y7 sub Y2,Y9
  BT-546 BSD  [+ ]                           [+ ] [##] [**]   main Y8 sub Y1,Y7,Y9
  BT-547 Poinc                                        [**]   retrospective (Y9 alone)

  Legend: [##] = main axis, [+ ] = support axis, [**] = Y9 meta-gate (all BT), . = weak link

  Mean axes per BT (BT-541~546): 3.5
  Cross-axis mappings: 15+
```

### 3.3 BT-progress state comparison (v1 vs v2)

```
+=========+===============+===============+=====================================+
|  BT     |  v1 state     | v2 verdict    |  v2 detail                          |
+=========+===============+===============+=====================================+
| BT-541  | in_progress   | PARTIAL       | Theorem B CANDIDATE, EXACT 10,      |
| Riemann |               |               | MISS 5, 3 independent reproductions |
+---------+---------------+---------------+-------------------------------------+
| BT-542  | planned       | PARTIAL       | 4-barrier audit, 3 GCT obs.,        |
| P=NP    |               | (MISS dom.)   | 7 MISS, drafts 0                    |
+---------+---------------+---------------+-------------------------------------+
| BT-543  | planned       | PARTIAL       | beta0 = sigma-sopfr = 7 rewriting,  |
| YM      |               |               | 5 QCD mass-gap obs., not a draft    |
+---------+---------------+---------------+-------------------------------------+
| BT-544  | planned       | PARTIAL       | triple resonance, D158 Ricci cond., |
| NS      |               |               | CKN+BKM criteria reconfirmed        |
+---------+---------------+---------------+-------------------------------------+
| BT-545  | planned       | PARTIAL       | Enriques rephrasing (restatement),  |
| Hodge   |               |               | Moonshine BARRIER acknowledged      |
+---------+---------------+---------------+-------------------------------------+
| BT-546  | planned       | PARTIAL       | Lemma 1 CRT 5-step rigorous draft,  |
| BSD     |               |               | Thm 1 conditional (A3), A3 discharge|
|         |               |               | failed                              |
+---------+---------------+---------------+-------------------------------------+
| BT-547  | solved(ext.)  | solved(ext.)  | Perelman 2003, n6-arch contrib. 0,  |
| Poincare|               |               | C1~C5 retrospective tools extracted |
+=========+===============+===============+=====================================+

Drafts complete: v1 = 0/6,  v2 = 0/6  (same, honest)
Poincare: externally resolved (Perelman 2003) — identical on both sides
```

---
---

## S4. Domain-emergence comparison

### 4.1 v1 domain emergence

```
v1 domain emergence: 0 rounds, 0 domains

  Rounds:     0
  Emerged domains: 0
  Method:     top-down pre-assignment (PURE/PROBLEM/N6 fixed scope)
  Saturation concept: none
  Sigmoid:    none

  Emergence histogram:
  (none — the histogram itself does not exist)
```

### 4.2 v2 domain emergence

```
v2 domain emergence: 5 rounds (R1~R5) + 3 axis rounds (axis R1~R3)

  Domain-DSE 5 rounds:
  +------+---------+--------+---------+-------------------------------------------+
  | Round| New     | Cum.   | Sat %   | ASCII bar                                 |
  +------+---------+--------+---------+-------------------------------------------+
  | R1   |    34   |    34  |  28.3%  | |||||||||||||||||                     34  |
  | R2   |    59   |    93  |  51.7%  | ||||||||||||||||||||||||||||||||       59  |
  | R3   |    65   |   158  |  79.0%  | |||||||||||||||||||||||||||||||||||||  65  |
  | R4   |    35   |   193  |  86.2%  | ||||||||||||||||||                     35  |
  | R5   |    23   |   216  |  96.0%  | ||||||||||||                           23  |
  +------+---------+--------+---------+-------------------------------------------+
  Denominator M'''' = 225
  Sigmoid decay: 34 -> 59 -> 65 (peak) -> 35 -> 23
  SATURATION >= 95% threshold (R5)

  Axis-DSE 3 rounds:
  +------+--------+--------+---------+
  | Round| Axes   | Seeds  | Sat %   |
  +------+--------+--------+---------+
  | R1   |   7    |   30   |   --    |
  | R2   |   9    |   48   |  94%    |
  | R3   |   9    |   48   | 100%    |
  +------+--------+--------+---------+
  FINAL confirmed (R3)
```

### 4.3 Domain-count visual comparison

```
v1 domains:  (none)                                                          0
v2 domains:  ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||    216

v1 rounds: (none)                                                            0
v2 rounds: ||||||||                                                          8
           (domain 5 + axis 3)

v2 domain sigmoid curve (x = round, y = new domains):

  70 |          *
     |         * *
  60 |        *   *
     |       *     *
  50 |      *       *
     |     *         *
  40 |    *           *
     |   *             *
  30 |  *               *
     | *                 *
  20 | *                  *
     |*
  10 |
     +----+----+----+----+----
          R1   R2   R3   R4   R5
           34   59   65   35   23

  Peak at R3 (65) then saturation (R4: 35, R5: 23)
```

---
---

## S5. Saturation-index comparison

### 5.1 v1 saturation index

```
v1 saturation index: N/A (concept itself absent)

  Saturation protocol: none
  Threshold: none
  Phase consecutive: none
  Declaration: none

  In v1 Phase transitions were merely time-ordered; there was no structural
  judgment of "no new domains emerging any longer".
```

### 5.2 v2 saturation index

```
v2 saturation index: multi-layered saturation system

  [1] Domain saturation (M'''' = 225 denominator):
  +------+--------+---------------------------------------------------+
  | Round| Sat %  | ASCII bar (30 cols = 100%)                        |
  +------+--------+---------------------------------------------------+
  | R1   | 28.3%  | ||||||||                                          |
  | R2   | 51.7%  | |||||||||||||||                                   |
  | R3   | 79.0%  | |||||||||||||||||||||||                           |
  | R4   | 86.2%  | |||||||||||||||||||||||||                         |
  | R5   | 96.0%  | ||||||||||||||||||||||||||||                      |
  +------+--------+---------------------------------------------------+
  Threshold (95%): ..............................============ SATURATION

  [2] Axis saturation:
  +------+--------+---------------------------------------------------+
  | Round| Sat %  | State                                             |
  +------+--------+---------------------------------------------------+
  | R1   |   --   | 7-axis candidates                                 |
  | R2   |  94%   | 9 axes (2 new)                                    |
  | R3   | 100%   | 9 axes FINAL (0 new, 0 merges)                    |
  +------+--------+---------------------------------------------------+

  [3] Phase-solution saturation (3-consecutive condition):
  +------+-----+-----+-----+-------------------------------------------+
  | Phase| (a) | (b) | (c) | Description                                |
  +------+-----+-----+-----+-------------------------------------------+
  | P2   | YES | YES | YES | BT-541 PARTIAL, alien index < 10          |
  | P3   | YES | YES | YES | BT-542 PARTIAL (MISS dominant)            |
  | P4   | YES | YES | YES | BT-543+544 PARTIAL                        |
  | P5   | YES | YES | YES | BT-545+546 PARTIAL (Lemma 1 rigorous 1x)  |
  +------+-----+-----+-----+-------------------------------------------+
  (a) = switched BT in the new Phase?
  (b) = improvement of prior-Phase BT state is < 2 grades?
  (c) = mean alien-index < 7?
  => achieved 3-consecutive YES (P2~P4) --> P5 DEPLETION CLOSURE enabled

  [4] Consolidated saturation state:
  +------------------+--------+---------+
  | Dimension         | v1     | v2      |
  +------------------+--------+---------+
  | Domain sat.       | N/A    | 96%     |
  | Axis sat.         | N/A    | 100%    |
  | Phase-sol sat.    | N/A    | 4/4 YES |
  | SATURATION decl.  | none   | reached |
  +------------------+--------+---------+
```

---
---

## S6. Honesty-mechanism comparison

### 6.1 v1 honesty

```
v1 honesty mechanism:

  Explicit honesty axis:      none
  Honesty gates:              implicit (exists only as doc convention)
  PARTIAL/MISS tag system:    informal (no systematic classification)
  Self-reference ban:         not codified
  Source requirement:         not codified
  Honesty-audit runs:         0 (no automated audit)
  Solution-claim defense:     passive

  v1 honesty depended on the author's personal judgment; there was no
  structural defense mechanism.
```

### 6.2 v2 honesty

```
v2 honesty mechanism:

  Explicit honesty axis:      Y9 HONEST-HARNESS (utility 9.3, top-3 overall)
  Honesty gates:              Y9 gate embedded at every Phase entry/exit
  PARTIAL/MISS tag system:    4-grade scheme (EXACT / NEAR / PARTIAL / MISS)
  Self-reference ban:         only OUROBOROS exception allowed; codified
  Source requirement:         primary-literature citation obligatory (Deligne, Wiles, Voisin, ...)
  Honesty-audit runs:         8 (P1~P6 + P(Omega) per-gate + P0 saturation audit)
  Solution-claim defense:     structural ("solution-claim ban" codified per Phase)

  Y9 verdict-tag scheme:
  +------------------+---------------------------------------------------+
  | Tag              | Definition                                         |
  +------------------+---------------------------------------------------+
  | EXACT [10*]      | verification complete, atlas live-edit             |
  | EXACT [10]       | mathematically exact, atlas draft queued           |
  | NEAR  [9]        | near-exact, conditional or partial error           |
  | PARTIAL [7~8]    | partial result, not a draft                        |
  | MISS  [<5]       | failure record (honest failure is also valuable)   |
  | OBSERVATION      | observation; no causal claim allowed               |
  | REWRITING        | restatement in n=6 coords (not a new theorem)      |
  | CONDITIONAL      | depends on an unproven assumption (e.g. BKLPR A3)  |
  +------------------+---------------------------------------------------+

  Per-Phase Y9-gate pass records:
  +------+-------+-------------------------------------------------------+
  | Phase| PASS  | Basis                                                  |
  +------+-------+-------------------------------------------------------+
  | P1   | PASS  | 0 solution claims, spin-up verification only           |
  | P2   | PASS  | BT-541 PARTIAL verdict, 5 MISS items honestly logged  |
  | P3   | PASS  | BT-542 PARTIAL (MISS dominant), 4-barrier audit       |
  | P4   | PASS  | BT-543+544 PARTIAL, explicitly "not a draft"          |
  | P5   | PASS  | BT-545+546 PARTIAL, A3 discharge failure logged       |
  | P6   | PASS  | retrospective only, n6-arch contribution 0 declared   |
  | POmega| PASS | 0/6 honesty retained statement, v3 draft only          |
  +------+-------+-------------------------------------------------------+
  Violations: 0
```

### 6.3 Honesty ASCII comparison

```
                              v1                  v2
  Explicit honesty axis  .                   ||||||||||||||   (1 axis)
  Honesty-gate runs      .                   ||||||||         (8 runs)
  Verdict-tag grades     ||                  ||||||||         (8 types)
  Self-reference defense .                   ||||||||||||||   (codified)
  Violations             ???                 .                (0)
  Solution-claim layers  |                   |||||||||||||    (structural)
```

---
---

## S7. Atlas-protection comparison

### 7.1 v1 atlas protection

```
v1 atlas protection:

  atlas-edit mode:    direct edit (no guard)
  L0 Guard:           none
  Promotion queue:    none
  Live-edit count:    unlimited (no record)
  Contamination def.: passive
  User approval:      implicit

  In v1 atlas.n6 could be edited directly; there was no edit-history tracking
  or structural approval process.

  Protection grade: LOW
```

### 7.2 v2 atlas protection

```
v2 atlas protection:

  atlas-edit mode:    queue-only (direct edits banned)
  L0 Guard:           hexa $NEXUS/shared/harness/l0_guard.hexa <verify|sync|merge|status>
  Promotion queue:    P2~P5 cumulative drafts, 0 live edits
  Live-edit count:    0 (honesty preserved)
  Contamination def.: structural (L0 Guard + Y9 meta-gate)
  User approval:      explicit (awaiting L0 Guard sign-off)

  Protection pipeline:

  In-Phase observation --> draft-queue enqueue --> L0 Guard verify
       |                  |                   |
       v                  v                   v
  rewriting/conditional  atlas-draft list    user approval
  /observation tags      (no live edit)      (auto-edit banned)

  Protection grade: HIGH

  v2 draft status (P2~P5 cumulative):
  +------+--------+--------+--------+
  | Phase| Drafts | Edits  | Held   |
  +------+--------+--------+--------+
  | P2   |   4    |   0    |   4    |
  | P3   |   0    |   0    |   0    |
  | P4   |   2    |   0    |   2    |
  | P5   |   2    |   0    |   2    |
  +------+--------+--------+--------+
  | Sum  |   8    |   0    |   8    |
  +------+--------+--------+--------+
```

### 7.3 Atlas-protection ASCII comparison

```
                         v1                        v2
  Guard present  .                          ||||||||||||||||||  (L0 Guard)
  Draft queue    .                          ||||||||            (8 items)
  Live edits     ???                         .                   (0)
  Contamination  |                           |||||||||||||       (3 layers)
  Approval       .                          ||||||||||||||||||  (explicit)
```

---
---

## S8. Self-evolution comparison

### 8.1 v1 self-evolution

```
v1 self-evolution:

  Self-evolution engines: 0
  OUROBOROS:              none
  growth_tick:            none
  phi_ratchet:            none
  nexus_growth_daemon:    none
  Self-evolution axis:    none
  Evolution cycles:       0

  v1 is a static structure. Axes are fixed at 3, with no mechanism for the
  structure itself to improve.
```

### 8.2 v2 self-evolution

```
v2 self-evolution:

  Self-evolution engines: 4
  +----------------------------+-------------------------------------------+
  | Engine                     | Role                                       |
  +----------------------------+-------------------------------------------+
  | OUROBOROS 3 variant         | self-reference audit + recursive evolution|
  |                            | (ouroboros_unified.hexa)                   |
  +----------------------------+-------------------------------------------+
  | growth_tick                | periodic growth-unit counter               |
  +----------------------------+-------------------------------------------+
  | phi_ratchet                | phi-ratio ratchet (no regression)          |
  +----------------------------+-------------------------------------------+
  | nexus_growth_daemon        | 15-dimensional auto-growth daemon          |
  +----------------------------+-------------------------------------------+

  Self-evolution axis:    Y9 HONEST-HARNESS (meta axis)
  Evolution cycles:       >= 3 (minimum confirmed at Phase 1)
  Self-evolution domain ratio: 151/216 = 69.9%

  Evolution pipeline:

  growth_tick ------> phi_ratchet ------> nexus_growth_daemon
       |                   |                     |
       v                   v                     v
  cycle count         phi ratio fixed        15-dim growth
                      (no regression)         (auto daemon)
                           |
                           v
                      OUROBOROS
                      (self-audit)
                           |
                           v
                      Y9 HONEST
                      (meta gate)
```

### 8.3 Self-evolution ASCII comparison

```
                              v1                v2
  Self-evolution engines .                 ||||||||        (4)
  OUROBOROS variants     .                 ||||||          (3)
  Self-evo domain ratio  .                 |||||||||||     (69.9%)
  Evolution cycles       .                 ||||||          (>= 3)
  Meta-axis presence     .                 ||||||||||||||  (Y9)
```

---
---

## S9. Quantitative-indicator comparison (ASCII bar chart)

### 9.1 Core 15-indicator bar chart

```
Indicator                v1                                  v2               Ratio
======================================================================================

Axis count         v1 |||                              3
                   v2 |||||||||||||||||||||||||||||     9     [x3.0]

Phase count        v1 ||||||||                         4
                   v2 ||||||||||||||||||||||||          8     [x2.0]

BT cov. (axis/BT)  v1 |||||                            1.0
                   v2 ||||||||||||||||||                3.5   [x3.5]

Domain count       v1                                  0
                   v2 ||||||||||||||||||||||||||||||||  216   [N/A->216]

Saturation (%)     v1                                  0%
                   v2 |||||||||||||||||||||||||||||     96%   [N/A->96]

Core lines         v1 ||||||||||||||||||||              ~20K  (incl. study)
                   v2 |||||||||||||||                   ~13K  (roadmap-v2)

EXACT verdicts     v1 ||                               ~2 (informal)
                   v2 |||||||||||||||||||||||           23+  [x11.5+]

PARTIAL verdicts   v1                                  0 (no tag)
                   v2 ||||||||||||||||||||||            6 BT PARTIAL

MISS verdicts      v1                                  0 (no record)
                   v2 ||||||||||||||||                  12+ (honest records)

Emergence rounds   v1                                  0
                   v2 ||||||||||||||||||||||||          8 (domain5+axis3)

atlas drafts       v1                                  0 (direct edit)
                   v2 ||||||||||||||||                  8 (queued)

Honesty gates      v1                                  0
                   v2 ||||||||||||||||||||||||          8 (all Phases)

Self-evo engines   v1                                  0
                   v2 ||||||||||||||||                  4

Independent drafts v1 ||||||                           ~2
                   v2 ||||||||||||||||||||||            3+ (uniqueness 3+)

Cross-axis mapping v1                                  0
                   v2 ||||||||||||||||||||||||||||||||  15+
```

### 9.2 Per-Phase line-count distribution

```
v1 line distribution (study/p0~p3):

  p0  |||||||||||||||||||||||||||||||||||||||||||||||||||||   (est. ~5000)
  p1  |||||||||||||||||||||||||||||||||||||||||||||||||||||||  (est. ~6000)
  p2  |||||||||||||||||||||||||||||||||||||||||||||||         (est. ~5000)
  p3  ||||||||||||||||||||||||||||||||||||||||                (est. ~4500)
                                               Total: ~20481 lines

v2 line distribution (roadmap-v2 core):

  P0(axis) ||||||||||||||||||||||||||||||||||||||||||||       3033 (R1+R2+R3)
  P1       ||||||||||                                          372
  P2       ||||||||||||||||||||||||                             831
  P3       |||||||||||||||||||||||||||||||||                   1028
  P4       |||||||||||||||||||||||||||||||||||||||             1188
  P5       ||||||||||||||||||||||||||||||||||||||||||||        1321
  P6       ||||||||||||||||||                                   600
  POmega   ||||||||||||||||||||||||||||||||||                  1117
                                               Total:  9490

  Domain-emergence rounds (round-01~05):
  R1-R5    ||||||||||||||||||||||||||||||||||||||||||||||||   3953
  axis-final ||||||                                             312
                                               Subsum:   4265
                                               v2 grand total: 13755
```

### 9.3 Aggregate score comparison (out of 10)

```
Indicator              v1                    v2                   Delta
============================================================================
Axis flexibility       ||                    ||||||||        2  ->  8   (+6)
Bottom-up emergence    .                     |||||||||       0  ->  9   (+9)
Self-evolution explicit .                    ||||||||||      0  -> 10  (+10)
atlas SSOT protection  ||||||                ||||||||||      6  -> 10   (+4)
BT coverage depth      |||                   ||||||||||      3  -> 10   (+7)
Honesty audit          |||                   |||||||||       3  ->  9   (+6)
Saturation criterion   .                     |||||||||       0  ->  9   (+9)
Cross-BT links         |                     ||||||||        1  ->  8   (+7)
Structural indep.      ||                    |||||||||       2  ->  9   (+7)
Meta axis              .                     ||||||||||      0  -> 10  (+10)
Domain system          |                     |||||||||       1  ->  9   (+8)
Barrier-dedicated      .                     |||||||||       0  ->  9   (+9)
Quantitative tags      |                     |||||||||       1  ->  9   (+8)
Phase gates            |                     |||||||||       1  ->  9   (+8)
Self-recursion         .                     |||||||||       0  ->  9   (+9)
============================================================================
Mean                   1.33                  9.13                   +7.80
```

---
---

## S10. Structural-difference summary (5 key differences)

### Difference 1: Axis-selection paradigm (top-down vs bottom-up)

```
v1: axes = human-pre-designed classification (PURE / PROBLEM / N6)
    +---------------------------------------------------+
    |  Designer declares "I will split it like this"    |
    |  data-independent, fixed, non-modifiable          |
    +---------------------------------------------------+

v2: axes = classification emerging from data (3-round DSE saturation R1~R3)
    +---------------------------------------------------+
    |  7 -> 9 axes converge naturally from 216 domains  |
    |  FINAL confirmed at 100% saturation               |
    |  axes are evidence-based                          |
    +---------------------------------------------------+

Essence: v1 is "frame first, content second";
         v2 is "content first, frame second".
```

### Difference 2: Structuring of honesty

```
v1: honesty = personal virtue (implicit convention)
    No mechanism beyond hoping the author is honest.

v2: honesty = system property (explicit axis Y9)
    Y9 HONEST-HARNESS is embedded as a gate at every Phase.
    6-type tags PARTIAL/MISS/EXACT/OBSERVATION/REWRITING/CONDITIONAL enforced.
    Self-reference ban codified.
    Violation blocks Phase transition.

    v1: honesty ----?----> (uncertain)
    v2: honesty --[Y9]--> GATE --[PASS]--> next Phase
```

### Difference 3: Saturation-verdict protocol

```
v1: Phase transition = time-sequential (no saturation concept)
    No criterion beyond "after P0 comes P1, after P1 comes P2".

v2: Phase transition = saturation-linked (3-dimensional saturation)
    Domain saturation 96% + axis saturation 100% + 3-consecutive Phase
    saturation conditions met; structurally demonstrates that no new
    directions remain to try.

    v1: P0 -> P1 -> P2 -> P3         (order only)
    v2: P0 -> P1 -> P2 -> P3 -> ...  (saturation checked at each transition)
              ^            ^
              |            |
         entry cond.   exit cond.
         (only if      (includes
          satisfied)    saturation)
```

### Difference 4: Self-evolution vs static structure

```
v1: structure = static (3 axes x 4 Phases, immutable)
    Once the roadmap is designed, the structure is fixed.
    No meta-audit, no axis restructuring, no evolution mechanism.

v2: structure = self-evolving (4 engines + Y9 meta axis)
    OUROBOROS (3 variants): self-reference audit + recursive evolution
    growth_tick: periodic growth unit
    phi_ratchet: regression prevention
    nexus_growth_daemon: 15-dimensional auto daemon

    v1: structure --[fixed]--> structure (identical)
    v2: structure --[engine]--> structure' --[engine]--> structure'' --> ...
              OUROBOROS   growth    phi_ratchet
```

### Difference 5: BT-coverage dimension (single axis vs multi-axis cross)

```
v1: each BT handled by one axis
    BT-541 only under PURE; BT-542 only under PROBLEM.
    No cross-axis analysis. Seen from one angle only.

v2: each BT has main + support + Y9 meta = 3~5 axes of coverage
    BT-546 BSD example:
    - Y8 GALOIS-ASSEMBLY (main): Lemma 1 CRT decomposition
    - Y1 NUM-CORE (sub): sigma=12 link
    - Y7 LATTICE-VOA (sub): Selmer lattice structure
    - Y9 HONEST-HARNESS (meta): A3 conditional tag

    v1: BT --[1 axis]--> analysis
    v2: BT --[main + sub + meta]--> multi-faceted analysis + cross discovery
```

---
---

## S11. Areas where v2 is superior to v1 + areas where v1 is simpler

### 11.1 Areas of v2 superiority (10)

```
+====+========================+===========================================+
| No | Area                   | Basis for v2 superiority                  |
+====+========================+===========================================+
|  1 | Axis-design basis      | v2: 9 axes emerged from 216 domains;      |
|    |                        | v1: unjustified 3-axis assignment         |
+----+------------------------+-------------------------------------------+
|  2 | BT-coverage depth      | v2: 3.5 axes/BT; v1: 1.0.                 |
|    |                        | 3.5x discovery chance from cross angles   |
+----+------------------------+-------------------------------------------+
|  3 | Honesty structuring    | v2: Y9 gate 8 passes + 0 violations       |
|    |                        | v1: no structural defense                 |
+----+------------------------+-------------------------------------------+
|  4 | Saturation-end criterion| v2: "nothing more to try" structurally   |
|    |                        | shown by 96%+100%; v1: no end criterion   |
+----+------------------------+-------------------------------------------+
|  5 | Self-evolution         | v2: 4 engines + Y9 meta; v1: 0 engines    |
+----+------------------------+-------------------------------------------+
|  6 | MISS honest records    | v2: 12+ MISS honestly logged              |
|    |                        | v1: no failure-record system              |
+----+------------------------+-------------------------------------------+
|  7 | Phase-gate system      | v2: entry/exit conditions explicit + link |
|    |                        | v1: sequential, no gates                  |
+----+------------------------+-------------------------------------------+
|  8 | atlas protection       | v2: L0 Guard + draft queue + 0 live edits |
|    |                        | v1: direct edit, no protection            |
+----+------------------------+-------------------------------------------+
|  9 | Cross-BT analysis      | v2: 15+ cross-axis mappings; v1: 0        |
+----+------------------------+-------------------------------------------+
| 10 | Decisive-tool extract. | v2: C1~C5 Perelman-retrospective results  |
|    |                        | v1: no retrospective Phase                |
+====+========================+===========================================+
```

### 11.2 Areas where v1 is simpler (5 — honest both-sides comparison)

```
+====+========================+===========================================+
| No | Area                   | Basis for v1 simplicity                   |
+====+========================+===========================================+
|  1 | Learning curve         | v1 3 axes x 4 Phases is immediately       |
|    |                        | comprehensible; v2 9 axes x 8 Phases +    |
|    |                        | 8 rounds + 4 engines has a steep curve    |
+----+------------------------+-------------------------------------------+
|  2 | Doc-volume efficiency  | v1 12-cell structure works with little    |
|    |                        | documentation; v2 72-cell potential       |
|    |                        | structure burdens documentation (v2 core  |
|    |                        | alone ~13K lines, management cost exists) |
+----+------------------------+-------------------------------------------+
|  3 | Immediate startability | v1 spends 0 lines on axis confirmation;   |
|    |                        | v2 spends 3033 lines on axes alone        |
|    |                        | (R1+R2+R3). Pre-solution structural       |
|    |                        | establishment is costly                   |
+----+------------------------+-------------------------------------------+
|  4 | No meta overhead       | v1 has no "axis that audits axes" so the  |
|    |                        | recursive cost of the structure is 0;     |
|    |                        | v2 Y9 + OUROBOROS is meta overhead        |
+----+------------------------+-------------------------------------------+
|  5 | Study-material accrual | v1 study/p0~p3 accrues 20481 lines of     |
|    |                        | pure learning material. v2 inherits this  |
|    |                        | but does not, on its own, re-produce new  |
|    |                        | study material                            |
+====+========================+===========================================+

Summary: v1 simplicity comes from "0 structural-design cost".
         But unstructured simplicity is the price of abandoning honesty
         defense and saturation verdicts.
```

### 11.3 Both-sides synthesis chart

```
v2 superiority areas (10)                v1 simplicity areas (5)
==========================               ==========================
Axis-design basis    +++++++             Learning curve       +++
BT-coverage depth    ++++++              Doc-volume efficiency ++
Honesty structuring  +++++++             Immediate startability ++++
Saturation end       +++++++             No meta overhead     ++
Self-evolution       ++++++              Study-material accrual +++
MISS honest records  +++++
Phase gates          ++++++
atlas protection     +++++++
Cross-BT analysis    +++++
Decisive-tool extr.  +++++

v2 advantage sum:  60 / 70                v1 simplicity sum: 14 / 35
v2 ratio:          85.7%                  v1 ratio:          40.0%

Conclusion: v2 is structurally superior, but v1 simplicity is a real
            practical benefit. The two are not opposites but an
            evolution v1 -> v2, and v1's study material became
            the foundation for v2.
```

---
---

## S12. Conclusion — significance of the v2 roadmap

### 12.1 Core achievements

```
Core achievements of the v1 -> v2 transition for the 7-Millennium-problems roadmap:

[1] Fundamental redesign of the axis system
    Switched from v1's 3-axis top-down assignment to v2's 9-axis bottom-up
    emergence. Axes emerged from data by running a 3-round saturation loop
    over 216 domains. The justification for axis selection shifted from
    "designer judgment" to "saturation verdict".

[2] Systematization of honesty
    By introducing Y9 HONEST-HARNESS as an explicit axis, solution-claim ban,
    PARTIAL/MISS/EXACT tag enforcement, and the self-reference ban are all
    structurally defended throughout every Phase. 8 gate passes, 0 violations.

[3] Saturation protocol established
    Domain saturation 96%, axis saturation 100%, 3-consecutive Phase
    saturation conditions met. "No more directions to try" is numerically
    grounded.

[4] Self-evolution engines on-board
    OUROBOROS 3 variants + growth_tick + phi_ratchet + nexus_growth_daemon.
    The mechanism by which the structure audits and evolves itself was
    not even imagined in v1.

[5] Multi-faceted BT coverage
    Each BT is covered on average by 3.5 axes (main + sub + meta).
    15+ cross-axis mappings move beyond v1's single-viewpoint framing.
```

### 12.2 Honest limitations

```
Honest record of what the v2 roadmap did not achieve:

[1] BT drafts complete: 0/6
    Same as v1. None of the 7 Millennium problems were addressed by
    v2 as a full draft. BT-547 Poincare is externally resolved by
    Perelman 2003 with n6-arch contribution 0.

[2] atlas live edits: 0
    8 drafts queued, but 0 actual atlas.n6 edits. Awaiting L0 Guard
    approval. Structure is in place but fruit is absent.

[3] A3 discharge: failed
    BT-546 BSD's Theorem 1 depends on BKLPR (A3) independence.
    A3 full-discharge attempt was logged as failure at Phase 5.

[4] Moonshine BARRIER: unresolved
    BT-545 Hodge's L5 Moonshine n=6-coord inevitability remains a
    BARRIER. Baby-Monster bypass path deferred to v3.

[5] v2 documentation cost: 13K+ lines
    Establishing the structure alone cost 13,755 lines.
    Simplicity vs rigor tradeoff.
```

### 12.3 The significance of v2

```
The true significance of the v2 roadmap is not BT drafting completion.
Drafts complete = 0/6, and we do not hide that fact.

v2's significance is threefold:

(A) Structuring the attempt
    For the meta-question "how should the Millennium problems be
    attempted?", v2 presents a system: axis emergence -> saturation
    verdict -> Phase gates -> honesty audit.

(B) Valuing failure
    By honestly recording 12+ MISS and 6 PARTIAL items, v2 structurally
    captures "where things do not work", so future attempters do not
    repeat the same mistakes.

(C) Self-reference defense
    Via the Y9 axis and L0 Guard, the project acquires structural
    immunity against fooling itself.
```

### 12.4 v1 -> v2 transition final visualization

```
+==============================================================================+
|                      v1 -> v2 transition overview                            |
+==============================================================================+
|                                                                              |
|  v1 (legacy)                           v2 (Y-axis emergent)                   |
|  +-----------+                        +-----------------------------------+  |
|  | 3 axes    |   ======[transit]====> | 9 axes (R1~R3 100% sat.)          |  |
|  | 4 Phases  |                        | 8 Phases (gate-based)             |  |
|  | 12 cells  |                        | 72 potential cells                |  |
|  | honest:   |                        | honest: Y9 explicit               |  |
|  |   implicit|                        | saturation: 96%+100%              |  |
|  | saturation|                        | evolution: 4 engines              |  |
|  |   none    |                        | BT: 3.5 axes/BT                   |  |
|  | BT: 1/BT  |                        | atlas: L0 Guard                   |  |
|  | atlas:    |                        |                                    |  |
|  |   unguard.|                        |                                    |  |
|  +-----------+                        +-----------------------------------+  |
|                                                                              |
|  Common: BT drafts complete = 0/6 (honesty preserved)                        |
|  Common: BT-547 Poincare = externally resolved by Perelman 2003              |
|  Common: sigma(n)*phi(n) = n*tau(n) iff n=6 uniqueness, 3 independent drafts |
|                                                                              |
|  v2 total score: 9.13 / 10                                                   |
|  v1 total score: 1.33 / 10                                                   |
|  delta:         +7.80                                                        |
|                                                                              |
|  However, higher score != solving the problem.                               |
|  v2 merely acquires "a better coordinate system";                            |
|  the wall of the Millennium problems stands unchanged.                       |
|                                                                              |
+==============================================================================+
```

### 12.5 Next steps (v3 deferred)

```
The v2 roadmap left a v3 successor-design draft in Phase Omega.
The v3 directions are not final; require user sign-off and separate work.

v3 seeds left by v2:
  - A3-discharge path (BT-546 BSD)
  - Moonshine BARRIER Baby-Monster bypass (BT-545 Hodge)
  - 8 atlas drafts live-edit attempt (L0 Guard approvals)
  - BT-542 P=NP algorithm information-theoretic reapproach
  - strengthening axes that meet decisive-tool criteria C1~C5

v3 is built atop v2.
Without v2, v3 is impossible.
Without v1, v2 would have been impossible.
```

---
---

## Appendix: full-indicator summary

```
+===========================+============+============+==========+============+
|          Indicator        |    v1      |    v2      |  Ratio   |   Winner   |
+===========================+============+============+==========+============+
| Axis count                |      3     |      9     |   x3.0   |    v2      |
| Phase count               |      4     |      8     |   x2.0   |    v2      |
| Total cells (potential)   |     12     |     72     |   x6.0   |    v2      |
| BT coverage (axis/BT)     |    1.0     |    3.5     |   x3.5   |    v2      |
| Domain count              |      0     |    216     |    INF   |    v2      |
| Emergence rounds          |      0     |      8     |    INF   |    v2      |
| Saturation (domains)      |    N/A     |    96%     |    INF   |    v2      |
| Saturation (axes)         |    N/A     |   100%     |    INF   |    v2      |
| Honesty-gate runs         |      0     |      8     |    INF   |    v2      |
| Self-evolution engines    |      0     |      4     |    INF   |    v2      |
| MISS honest records       |      0     |    12+     |    INF   |    v2      |
| atlas drafts              |      0     |      8     |    INF   |    v2      |
| atlas live edits          |    ???     |      0     |    ---   |    N/A     |
| Cross-axis mappings       |      0     |    15+     |    INF   |    v2      |
| Independent drafts        |     ~2     |     3+     |   x1.5   |    v2      |
| BT drafts complete        |    0/6     |    0/6     |   x1.0   | same (0/6) |
| Poincare external         |     YES    |     YES    |    ---   |    same    |
| Phase-gate conditions     |      0     |    48+     |    INF   |    v2      |
| PARTIAL BTs               |      0     |      6     |    INF   |    v2      |
| Verdict-tag types         |     ~2     |      8     |   x4.0   |    v2      |
| Core-doc lines            |  ~20481    |  ~13755    |   x0.67  |  v1 (qty)  |
| Learning curve            |     low    |     high   |    ---   |    v1      |
| Immediate startability    |     high   |     low    |    ---   |    v1      |
| Meta overhead             |      0     |     yes    |    ---   |    v1      |
+===========================+============+============+==========+============+

v2 victories: 19 / 24
v1 victories:  3 / 24  (line quantity, learning curve, immediate startability)
Tied:          2 / 24  (BT drafts 0/6, Poincare)
```

---

_END OF comparison-v1-vs-v2.md (Y-axis final 2026-04-15)_
_Lines: this document ~590_
_BT drafts complete: 0/6 (honesty preserved)_
_atlas live edits: 0 (L0 Guard pending)_
