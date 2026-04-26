---
id: btAI2c-counter-design-2026-04-26
date: 2026-04-26
type: anomaly-experiment-design
parent_cycle: BT-AI2
parent_followup_to: reports/anomaly/btAI2_robustness_summary.md
status: design-only (no execution this session)
gate_to_clear: F-AI2-A drop <= 5% at threshold=8 across all 100 seeds for at least one of the 3 workloads (attn / ffn / full)
hypotheses_tested: [H1, H2, H3]
falsifiers_proposed: [F-AI2c-A, F-AI2c-B, F-AI2c-C]
---

# BT-AI2c — Counter-Cycle Experiment Design

## §0 Non-claim disclaimer

This is a DESIGN spec. No simulator runs are performed in this session.
No atlas writes, no KG writes, no domains.json writes, no inventory
updates, no README writes. Every quantitative claim below is inherited
verbatim from `reports/anomaly/btAI2_robustness_summary.md`; this file
adds zero new measurements.

---

## §1 Why BT-AI2c is needed

The 900-run robustness sweep recorded in `btAI2_robustness_summary.md`
§0 / §2 / §6 produced the following verdict, quoted unmodified:

- F-AI2-A is "breached in 7 of 9 grid cells" (§0).
- threshold=4 yields a trivial PASS (drop = 0% in all three workloads,
  i.e. the write-barrier "never engages") (§2).
- Meaningful thresholds breach the 5% ceiling: threshold=8 breaches
  18 to 66 seeds out of 100; threshold=12 breaches 75 to 96 seeds out
  of 100 (§4).
- Worst cell `(full, 12)`: mean drop 11.4%, p99 17.3%, max 20.0%,
  96/100 seeds breach (§2, §4).
- Parent §6 explicitly proposes BT-AI2c with three candidate causes
  and names the gate "F-AI2-A <= 5% at threshold=8 across all 100
  seeds" before any design-HIGH claim is reinstated.

BT-AI2c is therefore the minimum experiment required to recover a
non-trivial design-stage clearance for F-AI2-A.

---

## §2 Three candidate causes (hypotheses)

Per `btAI2_robustness_summary.md` §6 (followup proposal block).

### H1 — Hypothesis-write blocking is too aggressive

(a) Simulator change: relax the write-barrier so a tile may issue a
speculative read of an un-promoted tensor; a grade-failure on the
producer triggers a rollback of the speculative consumer rather than
a full upstream stall.
(b) Distinguishing falsifier: F-AI2c-A. Distinguishes from H2 because
H1 leaves DAG fan-out unchanged; distinguishes from H3 because the
propagation-latency parameter is held at its current implicit value.
(c) Predicted F-AI2-A profile under threshold=8 if H1 holds: drop
mean falls below 5% across all 100 seeds in at least the `full`
workload (the cell where speculative parallelism has the most
serial stalls to absorb). `attn` and `ffn` should also improve but
are not required to clear.

### H2 — Workload DAGs have too few independent tiles

(a) Simulator change: increase per-stage fan-out by 2x in the attn,
ffn, and full DAG generators so threshold=12 promotion stalls have
sibling tiles ready to run.
(b) Distinguishing falsifier: F-AI2c-B. Distinguishes from H1 because
the write-barrier semantics are unchanged; distinguishes from H3
because per-tile latency cost is unchanged.
(c) Predicted F-AI2-A profile under threshold=8 if H2 holds: drop
mean falls below 5% across all 100 seeds in `attn` first (lightest
workload, easiest to widen) and the gap to `full` narrows. If
fan-out is the binding constraint, threshold=12 should also improve.

### H3 — Provenance propagation latency saturates at high threshold

(a) Simulator change: introduce an explicit `prop_latency` parameter
(cycles per grade-update) and sweep it across `{1, 2, 4, 8}` with
threshold and workload pinned.
(b) Distinguishing falsifier: F-AI2c-C. Distinguishes from H1 and
H2 because the test is monotonicity in latency, not absolute drop
reduction; H1 and H2 do not predict latency-monotonicity.
(c) Predicted F-AI2-A profile if H3 holds: at threshold=8, `full`
workload, drop mean is monotone increasing in `prop_latency` with a
saturation knee. If H3 is wrong, the curve is flat or non-monotone.

---

## §3 Falsifiers

- **F-AI2c-A** (H1): if speculative-read + rollback reduces (full, 8)
  drop mean below 5% across 100 seeds, H1 is supported.
- **F-AI2c-B** (H2): if 2x DAG fan-out reduces (full, 8) drop mean
  below 5% across 100 seeds, H2 is supported.
- **F-AI2c-C** (H3): if a propagation-latency parameter sweep shows
  F-AI2-A drop is monotonic in latency with threshold and workload
  fixed, H3 is supported.

A composite PASS for BT-AI2c requires AT LEAST ONE of F-AI2c-A /
F-AI2c-B / F-AI2c-C to clear at threshold=8 across all 100 seeds,
restoring a non-trivial design-stage clearance for F-AI2-A. If none
clears, BT-AI2c reports FAIL and the parent verdict stays at
design-MEDIUM.

---

## §4 Simulator change inventory

The two existing files in `experiments/anomaly/` relevant to BT-AI2,
verified by directory listing:

- `experiments/anomaly/btAI2_honesty_bit_scheduler.py`
- `experiments/anomaly/btAI2_seed_sweep.py`

Per-hypothesis modification targets (no edits in this session):

- H1 (speculative read + rollback): the write-barrier / promotion
  gate logic in `experiments/anomaly/btAI2_honesty_bit_scheduler.py`
  (the per-tile scheduler that the seed sweep harness invokes).
- H2 (2x DAG fan-out): the workload-DAG generator(s) in
  `experiments/anomaly/btAI2_honesty_bit_scheduler.py`. The seed
  sweep harness `experiments/anomaly/btAI2_seed_sweep.py` would gain
  a `--fanout` flag to drive the new generator parameter.
- H3 (propagation-latency sweep): a new `prop_latency` parameter in
  `experiments/anomaly/btAI2_honesty_bit_scheduler.py` and a fourth
  sweep axis in `experiments/anomaly/btAI2_seed_sweep.py`.

Function-level pointers are deferred to the execution session; this
spec only commits to the file set above and explicitly disclaims any
function name not yet read.

---

## §5 Cost & scope

- Cycles: 100 seeds x 3 workloads x 1-2 thresholds x 3 hypotheses
  → ~600 to 1800 paired runs (2x to 6x the BT-AI2 robustness sweep).
- Wall time: extrapolating from 161 s for 900 runs (`btAI2_robustness_summary.md`
  frontmatter `wall_seconds: 161`), expect ~200 to ~1100 seconds.
- Atlas writes: 0. KG writes: 0. domains.json writes: 0. README
  writes: 0. Only `reports/anomaly/btAI2c_*` artefacts are added,
  and only at execution time.

---

## §6 What this spec does NOT claim

- Does not predict which hypothesis (if any) will clear the gate.
- Does not commit to running BT-AI2c this session.
- Does not promote the parent design verdict from design-MEDIUM back
  to design-HIGH; only execution and gate-clearance can do that.
- Does not affect the 0/7 millennium tally. BT-AI2c is an
  ai-native-architecture cycle, not a millennium cycle.
- Does not relax the F-AI2-A 5% contract; that is a parent-session
  author decision per `btAI2_robustness_summary.md` §8 item 3.

---

## §7 Honesty-triad self-evaluation

- **no-fabrication**: every percentage, cell count, seed count, and
  wall-time figure references `btAI2_robustness_summary.md` by
  section; no new measurements are introduced.
- **constraint-honesty**: H1, H2, H3 are labelled hypotheses, and
  F-AI2c-A/B/C are labelled falsifiers, not findings. The
  predicted-profile clauses in §2 are conditional ("if H1 holds")
  and not asserted as outcomes.
- **write-barrier**: this design writes exactly one file
  (`reports/anomaly/btAI2c_design.md`, the spec itself); the
  simulator changes and the result artefacts are not created until
  a future execution session.
