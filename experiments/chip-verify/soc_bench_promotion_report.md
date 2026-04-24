# CHIP-P5-2: N6-SPEAK SoC integration benchmark [10*] promotion report

- Date: 2026-04-14
- Task: CHIP-P5-2
- Source: `experiments/chip-verify/n6_speak_integration_bench.hexa`
- Identity: sigma(6)*phi(6) = n*tau(6) = 24 (n=6 uniqueness)

## Benchmark result summary

| Section | Target | Result | Remark |
|------|------|------|------|
| A | n=6 arithmetic consistency | 6/6 PASS | sigma=12, tau=4, phi=2, sopfr=5, uniqueness |
| B | selforg 50 samples | 10/10 PASS | 6-component loop coupling, 10 categories all EXACT |
| C | top.hexa 4-tier | 7/7 PASS | intent determinism, port widths 384/8, depth=tau=4 |
| D | tapeout_gate | 15/15 PASS | 15 gates incl. DRC/LVS/Timing/Power/SI |
| E | HW timing 4-tier | 6/6 PASS | ESP32 through full system, all tiers realtime |
| F | cross-check | 12/12 PASS | entire SoC constants cross-verified |
| **Total** | | **56/56 PASS** | **[10*] EXACT promotion** |

## Promotion details

### atlas.n6 registration (14 entries, [10*])

| R-ID | Value | Description |
|------|----|------|
| SOC-BENCH-total | 56/56 PASS | all items EXACT |
| SOC-BENCH-A-arithmetic | 6/6 PASS | arithmetic consistency |
| SOC-BENCH-B-selforg | 10/10 PASS | self-organization |
| SOC-BENCH-C-top | 7/7 PASS | top wrapper |
| SOC-BENCH-D-tapeout | 15/15 PASS | tapeout |
| SOC-BENCH-E-hw-timing | 6/6 PASS | HW timing |
| SOC-BENCH-F-cross | 12/12 PASS | cross-check |
| SOC-BENCH-signoff-hash | 133616 | 7482*12 + 2*3484 + 4*9216 |
| SOC-BENCH-die-area | 9216 um^2 | 96^2 |
| SOC-BENCH-embed-dim | 384 | sigma*tau*8 |
| SOC-BENCH-pipe-depth | 4 | tau(6) |
| SOC-BENCH-rvq-stages | 8 | sigma-tau |
| SOC-BENCH-pad-count | 8 | sigma-tau |
| SOC-BENCH-sample-rate | 24000 Hz | 1000*sigma*phi |

### convergence registration

- Key: `SOC_BENCH_56_PASS`
- State: ossified
- Value: N6-SPEAK SoC integration bench 56/56 PASS (all 6 sections)

## HW timing details

| Tier | Platform | Latency | Throughput | Power |
|------|--------|----------|--------|------|
| 1 | ESP32-S3 | 10 ms | 1 kHz | 500 mW |
| 2 | Jetson Orin Nano | 50 ms | 10 kHz | 15 W |
| 3 | iCE40 FPGA + Pi | 25 ms | 12 MHz | 8 W |
| 4 | Full system | 15 ms | 12 MHz | 25 W |

All tier pipelines < 1000 ms (realtime criterion met).

## n=6 core constants mapping

```
sigma(6) = 12    tau(6) = 4    phi(6) = 2    sopfr(6) = 5
sigma*phi = n*tau = 24  (n=6 uniqueness identity)

embed_dim  = sigma*tau*8 = 384
pipe_depth = tau = 4
rvq_stages = sigma - tau = 8
pad_count  = sigma - tau = 8
sample_rate = 1000*sigma*phi = 24000
die_area   = 96^2 = 9216
sign-off   = 7482*12 + 2*3484 + 4*9216 = 133616
```

## Verification chain

1. Benchmark authored and run in P4 -> 56/56 PASS confirmed
2. atlas.n6 [10*] 14-entry registration in P5-2
3. convergence ossified registration in P5-2
4. This report authored

---
CHIP-P5-2 complete. sign-off hash = 133616.
