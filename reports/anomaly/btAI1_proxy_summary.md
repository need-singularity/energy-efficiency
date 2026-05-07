---
id: btAI1-proxy-2026-04-26
type: anomaly-experiment-proxy
parent: reports/anomaly/btAI1_summary.md
parent_session: reports/sessions/omega-cycle-ai-native-arch-beyond-gpu-2026-04-26.md
date: 2026-04-26
env_recovered_ts: 2026-04-26
language: en
verdict: HOLD-PROXY
millennium_tally_delta: 0/7
atlas_writes: 0
kg_writes: 0
domains_writes: 0
---

# BT-AI1 Proxy Run (HOLD-PROXY)

## Scope

Proxy execution attempt of `experiments/anomaly/btAI1_phi_over_n_sparsity.py`
after the BT-AI1 environment was recovered (Python 3.14 venv at
`.venv-btAI1/`, torch 2.11.0, transformers 5.6.2, MPS available).

This run is **NOT** a substitute for the parent BT-AI1 falsifier contract.
The parent HOLD record at `reports/anomaly/btAI1_summary.md` remains the
authoritative verdict for the F-AI1-A / F-AI1-B contract registered in
`reports/sessions/omega-cycle-ai-native-arch-beyond-gpu-2026-04-26.md`
section 6 (Llama-3 8B class, MMLU-all 1k+ items, three seeds).

## Resource path selected (by script auto-probe)

The script `_probe_resources` + `_choose_path` decision tree selected the
**proxy** path automatically. There is no `--model` or `--device` flag;
selection is determined by:

- `has_cuda = False` (Apple Silicon MPS host)
- `has_mps = True`
- HF cache scanned for cached candidates; first proxy match was used.

Selected model: **`TinyLlama/TinyLlama-1.1B-Chat-v1.0`** (cached locally;
first match in `proxy_targets` list).
Device: **`mps`**.
Falsifier mode: **`hold-proxy`** (BT-AI1-PROXY label).
Eval data: **`MICRO-PROXY`** (built-in 12-item MMLU battery + 8-item
GSM8K battery; the `datasets` package was not used in this small run).

## Command actually run

Final command (after a tighter retry):

```
timeout 240 .venv-btAI1/bin/python \
  experiments/anomaly/btAI1_phi_over_n_sparsity.py \
  --max-mmlu 8 --max-gsm 2 --seeds 0 \
  --results-out reports/anomaly/btAI1_proxy_results.json
```

An earlier first attempt used `--max-mmlu 25 --max-gsm 5 --seeds 0` with
`timeout 300`.

## Outcome

**No JSON results file was produced** within the 8-minute hard cap of
this sub-task. The process completed all three model loads (dense /
structured / random arms each loaded TinyLlama-1.1B over MPS, ~1 second
per load) but the `model.generate(...)` greedy-decoding loop in the
GSM8K micro-eval was the dominant cost. Within the 240-second hard
limit the run reached arm 2 mid-eval and the timeout fired before
`json.dump(...)` to `reports/anomaly/btAI1_proxy_results.json`.

stderr observed (verbatim, edited for line length):

- `Warning: You are sending unauthenticated requests to the HF Hub.`
- `[transformers] torch_dtype is deprecated! Use dtype instead!`
- `Loading weights: 100%|##########| 201/201 [...]` (x3 model loads)
- `[transformers] Both max_new_tokens (=16) and max_length (=2048) seem
  to have been set.` (multiple)
- `multiprocessing/resource_tracker.py:396: UserWarning:
  resource_tracker: There appear to be 1 leaked semaphore objects to
  clean up at shutdown` (on SIGTERM from `timeout`).

No exception, no traceback, no partial JSON written.

## What this means

- The recovered environment is **functional**: torch + transformers +
  MPS + the script's own auto-probe + path selection + all three model
  loads + mask application all worked.
- The bottleneck is **MPS generate throughput**, not the falsifier
  pipeline. To produce a complete proxy JSON the run needs either
  - a longer wall budget (estimated 8-15 minutes for the 25/5 setting),
    or
  - a smaller `--max-gsm` (e.g. 1) with `--max-mmlu` only, or
  - skipping the GSM arm entirely (would require a script flag, not
    in scope here per the no-modify constraint).
- No numerical accuracy figures are available from this attempt and
  none are reported here. **Producing fabricated numbers would violate
  the no-fabrication constraint of the parent omega-cycle.**

## Verdict

**HOLD-PROXY** (no measurement produced).

This is **not** a PASS, not a FAIL, and explicitly does not promote
the parent BT-AI1 verdict. The parent `reports/anomaly/btAI1_summary.md`
HOLD remains the authoritative verdict for full-tier F-AI1-A / F-AI1-B
closure.

Even on a successful proxy run, the script itself enforces
`falsifier_mode = "hold-proxy"` with `eval_data_label != "REAL"` and
the BT-AI1-PROXY label, so no proxy execution can promote BT-AI1 to
PASS / FAIL by design.

## Tally and writes

- 0/7 millennium tally: **unchanged**
- atlas writes: **0**
- KG writes (`canonshared/discovery_graph.json`): **0**
- domains.json writes (`canonshared/n6/docs/domains.json`): **0**
- Parent HOLD record: **not modified**
- Script: **not modified**

## References (read-only)

- Parent BT-AI1 HOLD: `reports/anomaly/btAI1_summary.md`
- Parent results JSON: `reports/anomaly/btAI1_results.json`
- Script: `experiments/anomaly/btAI1_phi_over_n_sparsity.py`
- Parent session: `reports/sessions/omega-cycle-ai-native-arch-beyond-gpu-2026-04-26.md`
- Atlas constants: `atlas/atlas.n6:81` (`@C meta_fp = 1/3 :: meta [10*!]`)
- KG nodes: `arch:n6-native-accelerator`, `principle:honesty-triad`
- Domain: `ai-native-architecture`
