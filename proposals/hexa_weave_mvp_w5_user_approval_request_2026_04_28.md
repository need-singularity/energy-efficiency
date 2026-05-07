# HEXA-WEAVE MVP — W5 User Approval Request

**Date**: 2026-04-28
**Cycle**: 8 / fan-out 4/5
**Author**: cycle-8 sub-agent (canon)
**Status**: AWAITING USER APPROVAL — no destructive ops executed

---

## 1. Purpose

W3 spec (clone+VRAM, 35.5 KB) and W4 spec (8-subdir + sm_120 deepspeed + 6L1U dry-run + 5-row fallback, 34.3 KB) are complete on paper. **Implementation has not started.** Before any directory creation, package install, or weight download is performed, the user must approve each item below.

This document is the gating checklist. Every item is independently checkable; the user may approve a subset (e.g. items 1-4 only, defer 5-8) and W5 will execute exactly the approved subset.

raw 91 C3 honest: **none of the destructive ops have been performed**. This cycle (W5) is plan + dry-run verification only.

---

## 2. Environment dry-run (read-only, completed)

| # | check | command | result | implication |
|---|-------|---------|--------|-------------|
| D1 | hexa-weave dir absent | `ls ~/core/hexa-weave` | `No such file or directory` | clean slate confirmed |
| D2 | python3.10 available | `python3.10 --version` | `command not found` (only python3.14 present) | **GAP** — must install py3.10 or relax pin |
| D3 | PyTorch CUDA | `python3 -c "import torch; print(torch.cuda.is_available())"` | `torch 2.10.0`, `cuda_available=False` | **GAP** — local Mac has no CUDA; GPU work must run on remote (ubu1) |
| D4 | OpenFold v2.2.0 SHA | `git ls-remote https://github.com/aqlaboratory/openfold.git v2.2.0` | `e938c184a291bf053af3b14c1e3e8bb29aee57e2` | matches W3 spec pin exactly |
| D5 | RCSB FASTA endpoint | `curl -sI https://www.rcsb.org/fasta/entry/6L1U` | HTTP/2 200, `text/x-fasta` | live, ready |
| D6 | nvidia-smi | `nvidia-smi` | `command not found` | **GAP** — local Mac has no GPU; required on ubu1 |

Verdict: 3/6 PASS (D1, D4, D5), 3/6 GAP (D2, D3, D6 — all expected on Mac dev box). The 3 gaps are environmental (Mac vs remote CUDA host) and do not block plan; they redirect actual execution to the ubu1 host described in W3 spec.

---

## 3. Approval Checklist (8 items)

The user is asked to approve or defer each item. Approval form: please reply with a list like `approve: 1,2,4,5; defer: 3,6,7,8`.

### Item 1 — `~/core/hexa-weave/` directory creation

- **What**: `mkdir -p ~/core/hexa-weave/{models,data,checkpoints,logs,configs,scripts,tests,docs}` (8-subdir per W4 spec)
- **Where**: local Mac (this host), `/Users/ghost/core/hexa-weave/`
- **Disk**: ~0 bytes (empty dirs); will grow to ~10-20 GB over W6+ as code/data lands
- **Reversible**: yes — `rm -rf ~/core/hexa-weave/`
- **Estimated cost**: $0 (local disk), 1 minute
- **Approve?** [ ]

### Item 2 — python3.10 venv creation

- **What**: install python3.10 (Homebrew or pyenv), `python3.10 -m venv ~/core/hexa-weave/venv`
- **Where**: local Mac
- **Disk**: ~50 MB (python interpreter) + ~30 MB (empty venv)
- **Reversible**: yes — `rm -rf ~/core/hexa-weave/venv` and `brew uninstall python@3.10`
- **Estimated cost**: $0, 5 minutes
- **Risk**: minor — extra python version on system, no system-wide impact
- **Approve?** [ ]

### Item 3 — PyTorch 2.5.1+cu124 install

- **What**: `pip install torch==2.5.1+cu124 --index-url https://download.pytorch.org/whl/cu124`
- **Where**: target host = **ubu1** (remote CUDA box, since Mac has no CUDA per D3/D6); not local
- **Disk**: ~5 GB (torch wheels + CUDA libs)
- **Bandwidth**: ~5 GB download
- **Reversible**: yes — `pip uninstall torch` (within venv)
- **Estimated cost**: GPU-week 0 (install only), storage 5 GB-month, ~10 minutes
- **Approve?** [ ]

### Item 4 — OpenFold v2.2.0 shallow clone

- **What**: `git clone --depth 1 --branch v2.2.0 https://github.com/aqlaboratory/openfold.git` → SHA `e938c184` (verified via D4)
- **Where**: ubu1, under `~/core/hexa-weave/models/openfold/`
- **Disk**: ~120 MB (shallow clone)
- **Reversible**: yes — `rm -rf models/openfold/`
- **Estimated cost**: $0, 2 minutes
- **License**: Apache 2.0 (verified)
- **Approve?** [ ]

### Item 5 — OpenFold weight download (~3 GB)

- **What**: download `params_model_1.npz`-style weights from OpenFold S3 / DeepMind mirror (per OpenFold v2.2.0 README)
- **Where**: ubu1, `~/core/hexa-weave/models/openfold/openfold/resources/`
- **Disk**: ~3 GB
- **Bandwidth**: ~3 GB download (one-shot)
- **Reversible**: yes — delete files
- **Estimated cost**: $0 (free download), 5-15 minutes depending on bandwidth
- **License**: CC BY 4.0 (DeepMind AlphaFold weights)
- **Approve?** [ ]

### Item 6 — sm_120 DeepSpeed source compile (~10 min build)

- **What**: source-compile DeepSpeed against PyTorch 2.5.1+cu124 with `TORCH_CUDA_ARCH_LIST="12.0"` for Blackwell sm_120 (per W4 spec)
- **Where**: ubu1
- **Disk**: ~500 MB (source + build artifacts)
- **CPU**: 8-12 cores × 10 min build (heavy)
- **Reversible**: yes — `pip uninstall deepspeed`
- **Estimated cost**: GPU-week 0 (CPU compile), ~10 minutes wall, ~30 CPU-minutes
- **Risk**: medium — sm_120 is bleeding-edge; build may fail and require fallback to pre-built deepspeed for sm_90 (W4 spec fallback row)
- **Approve?** [ ]

### Item 7 — PDB 6L1U FASTA fetch

- **What**: `curl -o data/6L1U.fasta https://www.rcsb.org/fasta/entry/6L1U` (verified live via D5)
- **Where**: ubu1 or local Mac (CPU-only step)
- **Disk**: <10 KB
- **Bandwidth**: <10 KB
- **Reversible**: trivial
- **Estimated cost**: $0, <1 second
- **License**: PDB public domain
- **Approve?** [ ]

### Item 8 — ubu1 GPU forward pass dry-run

- **What**: load OpenFold v2.2.0 weights → run inference on 6L1U sequence → emit PDB coords + confidence; record VRAM peak, wall time, GPU util
- **Where**: ubu1 GPU (per W3 spec target host)
- **Disk**: ~50 MB output (PDB + logs)
- **GPU**: 1 GPU × 10-30 min (one inference)
- **Reversible**: yes — output files only
- **Estimated cost**: **GPU-week 0.001** (one ~30-min inference), storage <100 MB-month, ~30 minutes wall
- **Risk**: medium — may OOM on consumer GPU (W4 spec defines 5-row VRAM fallback if so)
- **Approve?** [ ]

---

## 4. Aggregate cost estimate (raw 86 cost-attribution)

| resource | item-by-item | total |
|----------|--------------|-------|
| local disk (Mac) | items 1+2 | ~80 MB |
| remote disk (ubu1) | items 3+4+5+6+8 | ~8.6 GB |
| network bandwidth | items 3+5+7 | ~8 GB one-shot |
| GPU-week | item 8 only | ~0.001 (one ~30-min inference) |
| GPU-week (W6+ training, NOT in this cycle) | future | TBD |
| CPU-minutes | item 6 | ~30 |
| wall time (sequential) | all 8 items | ~60-90 minutes |
| **storage GB-month** (rolling) | 8.6 GB × ~1 month retention | ~8.6 GB-month |
| **dollar cost** (estimated) | ubu1 already provisioned | ~$0 marginal (electricity only) |

**F-TP5-b 90d MVP gate**: this W5 plan + dry-run execution moves the gate from `spec only (W3+W4)` to `spec + 1-shot inference verified (W5)` — approximately 25% of the 90-day MVP gate. Items 1-8 collectively are the **W5→W6 transition**: completing all 8 brings MVP to "first forward pass verified" = ~30% gate. Training (W7+) and downstream task evaluation (W8+) are the remaining 70%.

---

## 5. Approval Modes

**Mode A — full approval**: user replies `approve: 1-8`. W5 sub-agent (next cycle) executes all 8 items in order; ~60-90 min wall time.

**Mode B — partial approval**: user approves subset. Common partial paths:
- **B1 GPU-free path**: approve 1, 2, 4, 7 only (no torch install, no weight download, no GPU). Yields: empty repo skeleton + OpenFold source clone + 6L1U FASTA. Validates architecture without burning GPU/disk. ~10 min.
- **B2 install-only path**: approve 1-7 (no item 8 forward pass). Yields: full env staged, ready-to-run. Defers actual GPU burn. ~45 min.
- **B3 weights-deferred**: approve 1-4, 6, 7 only (skip item 5 weight download). Yields: env staged, no weights → cannot do item 8. ~30 min.

**Mode C — full deferral**: user replies `defer: 1-8`. W5 sub-agent stops at spec; no implementation. (Current state — equivalent to declining to approve.)

**Mode D — alternate**: user proposes different sequencing or different host (e.g. "do all on ubu1 not Mac" or "use sm_90 prebuilt deepspeed instead of sm_120 source"). Sub-agent re-plans accordingly.

---

## 6. Safety guarantees

- No item executes without explicit approval token in user reply.
- Each item is individually reversible (uninstall / rm / git delete).
- No system-level changes (no sudo, no root, no PATH edits, no shell rc edits).
- All work confined to `~/core/hexa-weave/` (Mac) and `~/core/hexa-weave/` (ubu1) — does not touch `~/core/canon/` artifacts.
- Failure of any item halts the chain; no retry without explicit user permission.

---

## 7. Connection to F-TP5-b 90d MVP gate

| W milestone | gate share | status |
|-------------|-----------|--------|
| W1 architecture decision | ~5% | DONE (cycle 5) |
| W2 base model integration spec | ~5% | DONE (cycle 5) |
| W3 clone+VRAM spec (35.5 KB) | ~10% | DONE (cycle 6) |
| W4 8-subdir+dryrun spec (34.3 KB) | ~10% | DONE (cycle 7) |
| W5 plan + dry-run + approval doc (this) | ~5% | DONE (cycle 8 — this) |
| W5 actual exec (items 1-8 above) | ~10% | **AWAITING USER APPROVAL** |
| W6+ training, ax2/mkbridge integration | ~55% | future |

Total spec progress through W5 plan = **35%**. Awaiting user approval to begin execution and reach **45%**.

---

## 8. Honest caveats (raw 91 C3)

- python3.10 pin in W3 may need relaxation: local box has 3.14 only. ubu1 may need `apt install python3.10` (additional sudo step not in checklist — flag this if approving Item 2).
- sm_120 (Blackwell) deepspeed source build is bleeding-edge; W4 spec fallback row exists for sm_90 prebuilt — recommend approving Item 6 with explicit fallback authorization.
- Item 8 (forward pass) has nontrivial OOM risk on consumer GPUs; if ubu1 has < 24 GB VRAM, W4's 5-row VRAM fallback engages (smaller batch / shorter seq / fewer recycle iters).
- This document does not create or download anything. It only requests permission. Reply with approval list to begin.
