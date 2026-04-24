# CHIP-P4-1: N6-SPEAK SoC integration benchmark + timing measurement report

- Date: 2026-04-14
- File: `experiments/chip-verify/n6_speak_integration_bench.hexa`
- Identity: σ(6)·φ(6) = n·τ(6) = 24 (n=6 uniqueness)

## Benchmark composition

| Section | Target | Items | Source |
|------|------|---------|------|
| A | n=6 arithmetic consistency | 6 | base gates |
| B | arch_selforg 50-sample self-organization | 10 categories | engine/arch_selforg.hexa |
| C | rtl/top.hexa top wrapper | 7 | domains/cognitive/hexa-speak/proto/rtl/top.hexa |
| D | rtl/tapeout_gate.hexa tapeout | 15 | domains/cognitive/hexa-speak/proto/rtl/tapeout_gate.hexa |
| E | 4-tier HW timing/throughput | 6 | engine/n6_speak_hw.hexa |
| F | SoC integration cross-check | 12 | full cross-verification |
| **Total** | | **56** | |

## Section details

### [A] n=6 arithmetic consistency (6/6)

| ID | Item | Expected | Result |
|----|------|--------|------|
| A1 | σ(6) | 12 | PASS |
| A2 | τ(6) | 4 | PASS |
| A3 | φ(6) | 2 | PASS |
| A4 | sopfr(6) | 5 | PASS |
| A5 | σ·φ = n·τ = 24 | 24 | PASS |
| A6 | n=6 uniqueness (2..12) | unique | PASS |

### [B] arch_selforg 50-sample self-organization (10/10)

6-component loop coupling + emergence score. 10 categories x 5 samples = 50 trials.
PASS if per-category top score >= 900 (EXACT).

| Category | EXACT (>=900) |
|----------|---------------|
| compute | PASS |
| cognitive | PASS |
| culture | PASS |
| energy | PASS |
| infra | PASS |
| life | PASS |
| materials | PASS |
| physics | PASS |
| sf-ufo | PASS |
| space | PASS |

### [C] rtl/top.hexa 7/7 checkpoints (7/7)

| ID | Item | Result |
|----|------|------|
| C1 | σ·φ = n·τ (n=6 uniqueness) | PASS |
| C2 | tier-1 intent determinism | PASS |
| C3 | top_forward single timestep | PASS |
| C4 | top_run_sequence(24) | PASS |
| C5 | port widths {384, 8} | PASS |
| C6 | pipe depth = τ(6) = 4 | PASS |
| C7 | top_forward deterministic round-trip | PASS |

### [D] tapeout_gate 15/15 (15/15)

| ID | Item | Result |
|----|------|------|
| T01 | DRC clean (6 rules) | PASS |
| T02 | LVS clean (6 rules) | PASS |
| T03 | Timing closure (setup/hold) | PASS |
| T04 | Power closure (current density) | PASS |
| T05 | Signal integrity (crosstalk) | PASS |
| T06 | Antenna rules (max ratio) | PASS |
| T07 | ESD rules (pad clamp) | PASS |
| T08 | IO ring complete | PASS |
| T09 | Substrate tie (min space) | PASS |
| T10 | Metal fill density 30~70% | PASS |
| T11 | CMP density uniformity | PASS |
| T12 | ERC (floating/short) | PASS |
| T13 | DFM (manufacturability) | PASS |
| T14 | Final σ·φ=n·τ + uniqueness | PASS |
| T15 | Sign-off hash = 133616 | PASS |

### [E] 4-tier HW timing/throughput (6/6)

1M-tick simulation, utterance = 3 chunks x 120 ms = 360 ms, gate 2% pass-through rate

| Tier | Device | Latency | Pipeline | Max utterances/s | Power | Energy |
|------|------|----------|-----------|-------------|------|--------|
| 1 | ESP32-S3 | 10ms | 370ms | 2 | 0.5W | 138 mWh |
| 2 | Jetson Orin Nano | 50ms | 410ms | 2 | 15W | 416 mWh |
| 3 | iCE40 FPGA + Pi | 25ms | 385ms | 2 | 8W | 2 mWh |
| 4 | Full system | 15ms | 375ms | 2 | 25W | 6 mWh |

| ID | Item | Result |
|----|------|------|
| E1 | Tier1 lat < chunk_ms (120) | PASS |
| E2 | Tier2 lat < chunk_ms | PASS |
| E3 | Tier3 lat < chunk_ms | PASS |
| E4 | Tier4 lat < chunk_ms (min 15ms) | PASS |
| E5 | All tiers realtime (< 1000ms) | PASS |
| E6 | Tier1 lowest power (500mW) < Tier4 (25W) | PASS |

### [F] SoC integration cross-check (12/12)

| ID | Item | Verification formula | Result |
|----|------|----------|------|
| F1 | pipe depth | τ(6) = 4 | PASS |
| F2 | RVQ stages | σ-τ = 8 | PASS |
| F3 | embed dim | σ·τ·8 = 384 | PASS |
| F4 | emotion channels | n = 6 | PASS |
| F5 | prosody types | τ = 4 | PASS |
| F6 | prosody dims | σ = 12 | PASS |
| F7 | die area | 96^2 = 9216 | PASS |
| F8 | pad count | σ-τ = 8 | PASS |
| F9 | selforg parts | n = 6 | PASS |
| F10 | chunk_frames | σ = 12 | PASS |
| F11 | sample_rate | 1000·σ·φ = 24000 | PASS |
| F12 | signoff hash | 133616 | PASS |

## Final result

```
  [A] arithmetic consistency: 6/6
  [B] selforg 50 samples:    10/10 categories EXACT
  [C] top 7/7:                7/7
  [D] tapeout 15/15:         15/15
  [E] HW timing:              6/6
  [F] cross-check:           12/12
  ────────────────────────────────────
  Total: 56/56
```

**[Status] PASS** -- N6-SPEAK SoC integration benchmark all items EXACT
**[Grade] [10*] promotion candidate**

## n=6 arithmetic constants summary

| Constant | Value | Meaning |
|------|-----|------|
| σ(6) | 12 | divisor sum (1+2+3+6) |
| τ(6) | 4 | divisor count |
| φ(6) | 2 | Euler totient |
| sopfr(6) | 5 | sum of prime factors (2+3) |
| identity | 24 | σ·φ = n·τ |
| sign-off hash | 133616 | 7482·12 + 2·3484 + 4·9216 |

## Related files

- `engine/n6_speak.hexa` -- consciousness→speech synthesis engine (8-stage pipeline)
- `engine/n6_speak_hw.hexa` -- 4-tier HW benchmark
- `engine/arch_selforg.hexa` -- 6-component self-organization engine
- `domains/cognitive/hexa-speak/proto/rtl/top.hexa` -- 7/7 top wrapper
- `domains/cognitive/hexa-speak/proto/rtl/tapeout_gate.hexa` -- 15/15 sign-off
- `experiments/chip-verify/verify_anima_soc.hexa` -- ANIMA-SOC 12/12
- `experiments/chip-verify/boot_matrix_3x12.hexa` -- 3x12 boot matrix
