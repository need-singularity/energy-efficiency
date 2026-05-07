---
id: btAI2-honesty-bit-scheduler-2026-04-26
date: 2026-04-26
type: anomaly-experiment
parent_session: reports/sessions/omega-cycle-ai-native-arch-beyond-gpu-2026-04-26.md
parent_cycle: BT-AI2
falsifiers_registered: [F-AI2-A, F-AI2-B]
verdict: PASS (both falsifiers cleared at simulation tier)
scope: cycle-level functional simulation — no RTL, no fab, no measured silicon
---

# BT-AI2 — Honesty-bit Scheduler Simulator Results

## §0 Non-claim disclaimer

This report records a **cycle-level functional simulation** of the
6-tile honesty-bit scheduler proposed in
`reports/sessions/omega-cycle-ai-native-arch-beyond-gpu-2026-04-26.md`
§4. Wall-clock timing, wire delay, area, power, and process-node effects
are **not modeled**. A PASS verdict here clears the design-stage
falsifier contract at the simulator tier only; it does not establish
silicon viability. RTL synthesis and EDA validation remain open
follow-on cycles (BT-AI3 candidate).

---

## §1 Falsifier verdict

| Falsifier | Threshold | Measured | Verdict |
|-----------|-----------|----------|---------|
| F-AI2-A — provenance-bit propagation throughput drop | drop ≤ 5% | **4.00%** drop | **PASS** |
| F-AI2-B — write-barrier rejection of legitimate (grade ≥ threshold) promotions | rate ≤ 1% | **0.0%** (0 of 49) | **PASS** |
| Composite | both PASS | both PASS | **PASS** |

Numbers are the canonical entries of `reports/anomaly/btAI2_results.json`
under `.falsifiers` (machine-readable companion to this document).

---

## §2 Run configuration

| Parameter        | Value                |
|------------------|----------------------|
| Seed             | 42                   |
| Cycle budget     | 10000                |
| Threshold        | 8 (atlas grade gate) |
| Workload         | `full` (~200 tensors, GPT-style attention + FFN) |
| Tiles            | n = 6 (atlas: foundation [11*]) |
| Stages           | tau = 4 (atlas: foundation [11*]) |
| Sparsity floor   | phi/n = 1/3 (atlas: meta [10*!]) |
| Provenance overhead constant | phi/sigma_n = 1/36 ≈ 2.78% (atlas: architecture [10*]) |
| Implementation   | SimPy event loop (cycle-driven), numpy RNG |
| Wall time (paired runs) | < 0.01 s on a single CPU core |

---

## §3 Throughput comparison (F-AI2-A)

| Mode                    | Throughput (tensors / cycle) | Cycles used | Completed tensors |
|-------------------------|-----------------------------:|------------:|------------------:|
| Baseline (provenance OFF, barrier OFF) | 2.0833 | 96  | 200 |
| Provenance ON + barrier ON              | 2.0000 | 100 | 200 |
| **Drop**                                 | **4.00%** | +4 cycles | identical |

Drop sits below the F-AI2-A 5% ceiling and is consistent with the
arithmetic prediction `phi/sigma_n ≈ 2.78%` once the additional
hypothesis-write blocking is included (the simulator additionally
stalls hypothesis writes whose grade is below threshold, which the
arithmetic ratio alone does not capture).

---

## §4 Write-barrier behaviour (F-AI2-B)

| Counter | Value |
|---------|------:|
| Legitimate promotions attempted (grade ≥ threshold) | 49 |
| Legitimate promotions refused                       | 0  |
| Legitimate-rejection rate                           | 0.0% |
| Hypothesis writes blocked (grade < threshold)       | 45 |

The barrier exhibits zero false positives at this seed and workload.
Hypothesis blocks are not false positives by definition — they are the
intended `principle:write-barrier` behaviour realized by
`silicon:promotion-counter-mmu`.

---

## §5 Per-tile distribution (provenance + barrier ON)

| Tile | Productive cycles | Stall cycles | Fact writes | Hyp writes blocked | Propagation events |
|-----:|------------------:|-------------:|------------:|-------------------:|-------------------:|
| 0    | 89 | 5 | 21 | 6 | 34 |
| 1    | 91 | 2 | 19 | 7 | 34 |
| 2    | 88 | 4 | 20 | 8 | 33 |
| 3    | 91 | 0 | 18 | 9 | 33 |
| 4    | 83 | 8 | 17 | 9 | 33 |
| 5    | 86 | 8 | 17 | 6 | 33 |
| **Σ** | **528** | **27** | **112** | **45** | **200** |

Tiles are reasonably balanced; no tile starves and no tile dominates.
The 27-cycle global stall budget is small relative to the 600-cycle
productive budget (4.5%), which matches the observed throughput drop.

---

## §6 Atlas / KG / domain references (read-only from this experiment)

- atlas
  - `n = 6 :: foundation [11*]`
  - `tau = 4 :: foundation [11*]`
  - `meta_fp = phi/n = 1/3 :: meta [10*!]`
  - `provenance_bit_overhead = phi/sigma_n = 1/36 :: architecture [10*]`
    (`atlas/atlas.append.canon-historical-absorption-2026-04-26.n6:526`)
- KG nodes (`canonshared/discovery_graph.json`)
  - `silicon:provenance-bit`
  - `silicon:promotion-counter-mmu`
  - `silicon:bt-id-isa`
  - `principle:honesty-triad` — realized by `silicon:provenance-bit`
  - `principle:write-barrier` — realized by `silicon:promotion-counter-mmu`
  - `principle:constraint-honesty` — realized by `silicon:bt-id-isa`
  - `arch:n6-native-accelerator` — requires the three silicon primitives
- domain (`canonshared/n6/docs/domains.json`)
  - `ai-native-architecture` (axis: compute, mk0 → mk_infinity)

This experiment **does not write** to atlas, KG, or domains.json.

---

## §7 Limitations (no-fabrication)

1. Cycle-level only — no wire delay, no area, no power, no process-node
   effects.
2. Workload is a synthetic ~200-tensor DAG, not a measured Llama-3 or
   GPT trace.
3. Promotion-counter MMU is modelled as a pure boolean gate; real MMUs
   pay TLB pressure and coherency cost not captured here.
4. Single seed reported. A robustness sweep (seed 0..99) is a sensible
   extension but not required by the registered falsifier contract.
5. The 4.00% measured drop sits inside the 5% F-AI2-A budget, but only
   by 1 percentage point. Tighter workloads or a different threshold
   schedule could push the drop above 5%; this is a known sensitivity.

---

## §8 Follow-on cycles

- **BT-AI1** (already registered in parent session §6):
  enforce `phi/n = 1/3` N:M sparsity on Llama-3 7B and measure
  MMLU / GSM8K. Independent of BT-AI2; can run in parallel.
- **BT-AI3 candidate** (newly proposed): RTL prototype of the three
  silicon primitives at a small process node (e.g. SkyWater 130nm via
  OpenROAD), to convert the simulator-tier PASS into a silicon-tier
  measurement. Required before any "silicon viability" claim.
- **BT-AI2 robustness extension** (optional): seed sweep 0..99 to
  bound the throughput drop distribution rather than the single-seed
  point estimate reported here.

---

## §9 Audit close

The BT-AI2 falsifier contract registered in
`reports/sessions/omega-cycle-ai-native-arch-beyond-gpu-2026-04-26.md` §6
is hereby **cleared at the simulator tier** with verdict **PASS** on
both F-AI2-A (4.00% drop ≤ 5%) and F-AI2-B (0.0% ≤ 1%). The parent
session's MEDIUM verdict (design-HIGH / silicon-LOW) is unchanged; this
report advances the design-stage evidence but does not promote the
silicon-stage grade. Atlas writes 0. KG writes 0. domains.json writes 0.
