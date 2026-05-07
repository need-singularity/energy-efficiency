# stage0 live-run re-verification report — 13 .hexa files

- Date: 2026-04-14
- Binary: `/Users/ghost/core/hexa-lang/build/hexa_stage0` (arm64 Mach-O, 1.8 MB, mtime 21:52)
- Execution mode: direct invocation of `hexa_stage0 <path>` interpreter
- Timeout: perl alarm 30 s (substitute for missing macOS `timeout`)
- Purpose: take the 13 files previously logged as "runtime.c missing → parse only" in past P1~P3 sessions and actually run them through the stage0 interpreter, capturing output/verification.

## Important correction — "parse only" → "stage0 live run"

Past artifacts stated "hexa runtime.c missing → parse-only verification"; this was a misjudgment.
The cause was a bug in the old stage1 `hexa build` path; the **stage0 interpreter/run mode worked correctly from the start**.
This report captures the actual stage0 run results for those 13 files. All prior wording of "parse only" in existing docs should be replaced with "stage0 live-run result".

## Summary table

| #  | File | Status | Lines | Pass/verification | Remark |
|----|------|------|------|----------|------|
| 1  | engine/arch_quantum.hexa                                  | PASS (live) | 28 | EXACT 10/10, avg 1000 | includes main() call |
| 2  | engine/arch_selforg.hexa                                  | PASS (live) | 81 | SAMPLE 50 + END50     | includes main() call |
| 3  | engine/arch_adaptive.hexa                                 | PASS (live) | 30 | EXACT 10/10, avg 983, promotion 10/10 | includes main() call |
| 4  | engine/arch_unified.hexa                                  | RUN OK (no output) | 0 | main returns total | no println (by design) |
| 5  | bridge/ouroboros_5phase.hexa                              | PASS (live) | 55 | 5 phases, 15 promotion candidates | includes main() call |
| 6  | bridge/ecosystem_9projects.hexa                           | PASS (live) | 15 | core 7 + auxiliary 2   | includes main() call |
| 7  | domains/.../rtl/top.hexa                                  | PASS (harness) | 9  | 7/7 PASS | no main() → append-run |
| 8  | domains/.../rtl/soc_integration.hexa                      | PASS (harness) | 8  | 6/6 PASS | no main() → append-run |
| 9  | domains/.../rtl/soc_drc_lvs.hexa                          | PASS (harness) | 24 | 12/12 PASS, chksum 7482 | no main() → append-run |
| 10 | domains/.../rtl/tapeout_gate.hexa                         | PASS (harness) | 25 | 15/15 PASS, hash 133616 | no main() → append-run |
| 11 | experiments/chip-verify/verify_chip-3d.hexa               | PASS (harness) | 9  | 5/5 EXACT       | no main() → append-run |
| 12 | experiments/chip-verify/verify_anima_soc.hexa             | PASS (harness) | 20 | 12/12 EXACT     | no main() → append-run |
| 13 | experiments/chip-verify/boot_matrix_3x12.hexa             | PASS (harness) | 43 | 34/36 (94%)     | no main() → append-run |

Stats: 13/13 files executed successfully under stage0 (rc=0), zero errors. Of these, 12 files produced println output; 1 file (#4) has no main-body println by design (expected empty output).

### Execution classification

- Class A (6/13): bottom of the file already contains a `main()` call, so a single `hexa_stage0 <path>` invocation naturally emits all output (1,2,3,5,6 + 4; though #4 is intentionally silent).
- Class B (7/13): `fn main()` is defined but the bottom-of-file `main()` call is absent. Because the stage0 interpreter does not auto-invoke `main()`, running the original file yields 0 stdout lines. For the report we appended a single `\nmain()\n` line to a temporary copy and re-ran; this is marked as harness execution. The original files were not modified.

## Per-file stdout tail

### [1] engine/arch_quantum.hexa
```
  superposition=3 collapse=k0 heads=12 depth=2 dim=48 score=1000
[9] space
  superposition=3 collapse=k0 heads=12 depth=2 dim=48 score=1000

========================================
categories 10 / EXACT(>=900)=10 / avg=1000
========================================
arch_quantum OSSIFIED : EXACT=10/10 -> [7]empirical
```

### [2] engine/arch_selforg.hexa
```
SAMPLE cat=9 s=0 parts=[2,4,6,8,10,12] total=42 score=949 alien=9 closure=10
SAMPLE cat=9 s=1 parts=[2,4,6,8,10,12] total=42 score=949 alien=9 closure=10
SAMPLE cat=9 s=2 parts=[3,5,7,9,11,13] total=48 score=887 alien=8 closure=9
SAMPLE cat=9 s=3 parts=[1,3,5,7,9,11] total=36 score=887 alien=8 closure=9
SAMPLE cat=9 s=4 parts=[2,4,6,8,10,12] total=42 score=949 alien=9 closure=10
---END50---
```

### [3] engine/arch_adaptive.hexa
```
[9] space
  final fitness=966 promotion=1

========================================
categories 10 / EXACT(>=900)=10 / avg=983
promotion hook fired = 10 / 10 (atlas.n6 [7]->[10*])
========================================
arch_adaptive OSSIFIED : EXACT=10/10 -> v4 adaptive [10*] candidate
```

### [4] engine/arch_unified.hexa
```
(0 lines on stdout — main body has no println, only returns total. rc=0 normal)
```

### [5] bridge/ouroboros_5phase.hexa
```
[5/5 evolution] atlas.n6 promotion candidate logged — domain=ai-efficiency
[5/5 evolution] promotion candidates: 5, awaiting atlas.n6 append

════════════════════════════════════════════════════════════
  cycle end
════════════════════════════════════════════════════════════
total promotion candidates: 15
next step: append to atlas.n6 at [10*] grade (user approval required)
```

### [6] bridge/ecosystem_9projects.hexa
```
  canon   system-design         [ok] (core)
  papers            paper-distribution    [ok] (core)
  hexa-lang         language              [ok] (core)
  void              terminal              [ok] (core)
  airgenome         os-scanner            [ok] (core)
  contribution      paper-submission-hub  [ok] (auxiliary)
  openclaw          singularity-feed      [ok] (auxiliary)
-----------------------------------------------------------------
total 9 projects (core 7 + auxiliary 2)
```

### [7] domains/cognitive/hexa-speak/proto/rtl/top.hexa (harness)
```
=== rtl/top.hexa — N6-SPEAK v2 4-tier top wrapper ===
  [T1] σ·φ = n·τ (n=6 uniqueness) PASS
  [T2] tier-1 determinism PASS (intent_in=53312)
  [T3] top_forward(intent_in=48000) PASS (audio_out=5149)
  [T4] top_run_sequence(24) PASS (total=96446)
  [T5] port widths {intent_in[384], audio_out[8]} PASS
  [T6] pipe depth=4 = τ(6) PASS
  [T7] top_forward determinism PASS
=== rtl/top.hexa: 7/7 PASS ===
```

### [8] domains/cognitive/hexa-speak/proto/rtl/soc_integration.hexa (harness)
```
=== rtl/soc_integration.hexa — N6-SPEAK v2 SoC integration ===
  [S1] die 96×96 = 9216 μm² PASS
  [S2] block total area = 6048 μm² (occupancy 65.6%) PASS
  [S3] all blocks within die bounds PASS
  [S4] floorplan_checksum determinism PASS (c=13794)
  [S5] σ·φ = n·τ uniqueness PASS
  [S6] 6 buses (τ(6)=4 + 2 fiber) valid PASS
=== soc_integration.hexa: 6/6 PASS ===
```

### [9] domains/cognitive/hexa-speak/proto/rtl/soc_drc_lvs.hexa (harness)
```
  L4  internal bus count = 6           PASS
  L5  total port sum match             PASS
  L6  n=6 consistency (5 blocks + 1 fusion) PASS

[ summary ]
  DRC 6 rules + LVS 6 rules = 12 checks
  result: 12/12 PASS
  floorplan checksum = 7482

DRC/LVS: ALL PASS (12/12) — tapeout clean
```

### [10] domains/cognitive/hexa-speak/proto/rtl/tapeout_gate.hexa (harness)
```
  T13  DFM (manufacturability)       PASS
  T14  Final checksum σ·φ=n·τ        PASS
  T15  Sign-off hash = 133616        PASS

[ summary ]
  15/15 PASS  —  N6-SPEAK v2 tapeout GATE CLEAN
  sign-off hash = 133616
  floorplan checksum (P2-1) = 7482
  die = 96 × 96 μm²  ·  blocks = 5 + fusion = n=6
  total ports = 3484  ·  buses = 6  ·  layers = m1~m4
```

### [11] experiments/chip-verify/verify_chip-3d.hexa (harness)
```
[3D-stacked chip] n=6 alignment verification — 5 items
metal layers = 6 (n=6) -> 1
SM array     = 144 (sigma^2=144) -> 1
MAC array    = 288 (sigma*J2=288) -> 1
pipe stages  = 4 (tau=4) -> 1
power domains = 8 (sigma-tau=8) -> 1
pass = 5/5
[status] pass — 3D-stacked chip n=6 alignment OK
[feedback] dse-map [chip-3d.feedback] grade=EXACT pass=5/5 sigma=12
```

### [12] experiments/chip-verify/verify_anima_soc.hexa (harness)
```
  B4 execution units 1728 = sigma^3 -> 1
[C] HEXA-TOPO Bott-8 NoC
  C1 Bott period 8 = n+phi -> 1
  C2 NoC nodes 144 = sigma^2 -> 1
  C3 torus perimeter 16 = sigma+tau -> 1
  C4 Clifford Cl(8) dim 256 = (sigma+tau)^2 -> 1
[subtotal] A=4/4 B=4/4 C=4/4
[total] pass = 12/12
[status] pass — ANIMA-SOC + PureField + HEXA-TOPO silicon n=6 alignment EXACT
[feedback] dse-map [chip-architecture.feedback] grade=EXACT pass=12/12
```

### [13] experiments/chip-verify/boot_matrix_3x12.hexa (harness)
```
  HEXA-ASIC | PCIe | 1 | 28 | 99 | EXACT
  HEXA-ASIC | USB | 1 | 76 | 40 | NEAR
  HEXA-ASIC | NVMe | 1 | 51 | 34 | NEAR
  HEXA-ASIC | Ethernet | 1 | 132 | 48 | NEAR
  HEXA-ASIC | DisplayPort | 1 | 94 | 122 | EXACT
  HEXA-ASIC | HDMI | 1 | 79 | 50 | NEAR
[subtotal] pass = 34/36 (94%)
[average] latency = 2225 ns, bandwidth = 55 Gbps
[status] pass — matrix 34/36 ≥ 30 (5/6 threshold)
[feedback] dse-map [chip-architecture.feedback] grade=EXACT matrix=34/36 avg_lat=2225ns avg_bw=55Gbps
```

## Failed files — none

Of the 13 files, 0 produced stderr output or parse/runtime errors. Every file runs cleanly under the stage0 interpreter.

## Recommended follow-ups

1. For the 7 Class-B files (missing `main()` call), append a single `main()` line at the bottom of the originals.
2. Blanket-update docs and comments that say "parse verification only" / "runtime.c missing" to "stage0 live-run OK".
3. For file #4 arch_unified.hexa, recommend adding one println line exposing the main return `total` for verification visibility.
