---
name: hexa-weave-mvp-w5-mac-cpu-fallback
type: phased
phase: cycle-23
date: 2026-04-28
parent: hexa_weave_mvp_w5_sandbox_cycle14_prep_2026_04_28.md
status: forward-spec
category: phased
---

# HEXA-WEAVE MVP W5 — Mac CPU-Only Fallback Path (cycle 23)

## §1 WHY

Cycle 14 spec `hexa_weave_mvp_w5_sandbox_cycle14_prep_2026_04_28.md`
defines an 8-step ubu1-GPU-bound runbook (RTX 5070 sm_120 prebuilt CUDA
kernel absent → CUDA_ARCH_LIST source compile required, ~10min). User
manual approval not yet given (cycle 14 → 23, 9 cycles elapsed). This
fallback spec defines a Mac-arm64 CPU-only path so OpenFold 6L1U 60aa
dry-run can validate the runbook plumbing **without** GPU access. The
full alien-grade-6 unlock (mvp 5/6 → 6/6) still requires GPU; the Mac
CPU path only validates Steps 1-6 (env + clone + RCSB) plus a degraded
Step 8 (CPU forward pass, ~30-60min instead of GPU 5min).

raw 91 C3 honest disclosure: this is a **dev/test fallback**, NOT a
production-grade replacement for ubu1 GPU. mvp 6/6 PASS still gated on
GPU.

## §2 COMPARE

| Path | Host | Wall-clock | VRAM ladder | Production grade |
|------|------|-----------|-------------|------------------|
| Original (cycle 14) | ubu1 + RTX 5070 12GB | ~74min | L1 3-4GB → L4 10-11GB | YES (mvp 6/6 unlock) |
| Mac CPU-only (cycle 23) | Mac arm64 24GB unified | ~120min | unified L1 5-7GB | NO (dev/test only) |

Disk + network footprint same (~9GB / ~8.2GB). Wall-clock dominated by
Step 8 forward pass (CPU 30-60min vs GPU 5min). sm_120 CUDA source
compile NOT NEEDED on Mac (CPU-only branch).

## §3 REQUIRES

- Mac arm64 (M1/M2/M3/M4) with ≥16GB unified memory (24GB recommended)
- Python 3.10 (homebrew pyenv or system)
- ~9GB free disk (homedir partition)
- Network: PyPI + GitHub + RCSB
- raw 42 jetsam-safe: ≤7GB peak resident set
- raw 9 hexa-only: setup runbook is .hexa native; PyTorch CPU wheel from
  PyPI (allowed via raw 14 ext-ssot declaration)
- raw 91 C3 disclose: PyPI external dependency required (not vendored)

## §4 STRUCT

8-step runbook delta from cycle 14 spec:

```
Step 1: 디렉토리 생성                    [unchanged]
Step 2: python3.10 venv                  [unchanged]
Step 3: pip install (CPU wheel)          [DELTA — cpu wheel not cu124]
Step 4: OpenFold clone                   [unchanged]
Step 5: weights download                 [DELTA — esm3 small only ~1GB]
Step 6: RCSB 6L1U FASTA                  [unchanged]
Step 7: sm_120 source compile            [SKIP — CPU branch]
Step 8: 6L1U dry-run forward pass        [DELTA — --device cpu]
```

## §5 FLOW

User approval → ssh-less Mac local → setup script with `--mode=mac-cpu`
flag → 6 step-pairs (1+2 prep, 3+4 deps, 5+6 inputs, 8 forward) →
`__W5_MAC_CPU_RESULT__ PASS|FAIL` sentinel.

## §6 EVOLVE

cycle 22 saturation: Felgner 11/11 mechanical + lean axiom 1 + biology
4-sister tetrahedron + F-VIROCAPSID-2 RESOLVED. cycle 23 Mac CPU
fallback unblocks W5 plumbing validation without GPU sandbox approval
delay. Future cycles will extend with full ubu1 GPU path once user
approves.

## §7 VERIFY

```python
# tool/hexa_weave_w5_mac_cpu_verify.py (forward-spec, not yet authored)
import sys
import os

def verify_mac_cpu_runbook():
    """raw 53 deterministic verification of Mac CPU fallback path."""
    checks = []
    checks.append(("step_1_dir_tree", os.path.isdir(os.path.expanduser("~/core/hexa-weave/openfold"))))
    checks.append(("step_2_venv_py310", os.path.isfile(os.path.expanduser("~/core/hexa-weave/venv/bin/python3.10"))))
    checks.append(("step_3_torch_cpu", subprocess_check_torch_cpu_only()))
    checks.append(("step_4_openfold_clone", os.path.isfile(os.path.expanduser("~/core/hexa-weave/openfold/setup.py"))))
    checks.append(("step_5_esm3_small_weights", os.path.isfile(os.path.expanduser("~/core/hexa-weave/weights/esm3_small.pt"))))
    checks.append(("step_6_rcsb_fasta", os.path.isfile(os.path.expanduser("~/core/hexa-weave/test_inputs/6L1U.fasta"))))
    checks.append(("step_8_forward_pass_completed", os.path.isfile(os.path.expanduser("~/core/hexa-weave/outputs/6L1U_predicted.pdb"))))
    pass_count = sum(1 for _, p in checks if p)
    return pass_count, len(checks), checks

def subprocess_check_torch_cpu_only():
    """torch installed AND torch.cuda.is_available() == False (Mac CPU branch)"""
    try:
        import torch
        return not torch.cuda.is_available()
    except ImportError:
        return False

if __name__ == "__main__":
    p, t, details = verify_mac_cpu_runbook()
    print(f"verify Mac CPU runbook: {p}/{t} PASS")
    sys.exit(0 if p == t else 1)
```

## §8 IDEAS

Optional Step 8b: ablation comparison — same 6L1U via OpenFold CPU on
Mac vs OpenFold GPU on ubu1 (when both paths land), TM-score delta
should be < 0.01 (numerical precision) per F-W5-MAC-CPU-2.

## §9 METRICS

- step_pass_count target ≥ 6/7 (Step 7 sm_120 SKIP-as-PASS for CPU path)
- forward pass wall-clock ≤ 60min on Mac M1/M2 (≤ 30min on M3/M4)
- TM-score 6L1U ≥ 0.4 (same threshold as ubu1 GPU)
- raw 42 RSS ≤ 7GB peak (jetsam-safe)

## §10 RISKS

| Risk | Likelihood | Mitigation |
|------|-----------|-----------|
| OpenFold main HEAD CPU branch stale | MED | fallback to v2.2.0 tag, vendored CPU patch |
| ESM3 weights CPU-incompatible (likely OK) | LOW | ESM3 is torch native, CPU works |
| MPS (Mac GPU) vs CPU divergence | LOW | force CPU via `torch.device("cpu")` |
| Wall-clock > 120min user impatience | MED | progress bar + checkpoint every 10min |

## §11 DEPENDENCIES

- raw 14 ext-ssot: PyPI (PyTorch CPU + biopython + RDKit + Pydantic)
- raw 9 hexa-only: setup runbook native
- raw 47 cross-repo: cycle 24 path migration — empirical sandbox now lives
  at `~/core/nexus/sim_bridge/weave/` (sim_bridge sub-module pattern,
  peer of multiverse / bostrom_test / godel_q). Original `~/core/hexa-weave/`
  proposal retired in cycle 24; sister-repo init NOT pursued.
- raw 91 C3: external PyPI required, not vendored

## §12 TIMELINE

- cycle 23 (today): forward-spec authored
- cycle 24+ (gated on user OK): Mac CPU runbook execution + verify
- cycle 25+ (gated on user GPU OK): ubu1 GPU full path (alien-grade
  6 unlock)

## §13 TOOLS

- `tool/hexa_weave_w5_setup.hexa --mode=mac-cpu` (cycle 23 enhancement
  to existing runbook; cycle 24 path target updated to
  `~/core/nexus/sim_bridge/weave/`)
- `tool/hexa_weave_w5_mac_cpu_verify.py` (forward-spec, cycle 24+; will
  also live in `nexus/sim_bridge/weave/` once authored)
- `~/core/nexus/sim_bridge/weave/runner.sh` (cycle 24 LIVE — pipeline
  driver: `--cage-only` / `--audit-only` / `--extended` / default both
  for `cage_assembly_simulation.py` + `polyhedral_cage_bayesian_audit.py`)

## §14 TEAM

Solo / AI-assisted. raw 105 ai-cli-kick-autonomous-invocation grants
agent autonomous re-invocation if Mac CPU path fails Step N — fallback
is Step N retry with cleaner state, then user notification.

## §15 REFERENCES

- cycle 14 parent: `proposals/hexa_weave_mvp_w5_sandbox_cycle14_prep_2026_04_28.md`
- OpenFold v2.2.0: https://github.com/aqlaboratory/openfold
- ESM3: https://github.com/evolutionaryscale/esm
- raw 9 hexa-only mandate
- raw 42 jetsam-safe

## raw 71 falsifier preregistration

- F-W5-MAC-CPU-1: forward pass wall-clock > 120min on Mac M1 — retire
  fallback path or downgrade to ESM2 small only (deadline 2026-07-28)
- F-W5-MAC-CPU-2: TM-score 6L1U Mac CPU vs ubu1 GPU divergence > 0.01 —
  numerical precision issue, investigate (deadline 2026-07-28)
- F-W5-MAC-CPU-3: Mac arm64 wheel install failure (PyPI absent) — pin
  alternative (PyTorch nightly or homebrew built) (deadline 2026-05-28)

## raw 91 C3 honest disclosure

- This is a **dev/test fallback**, NOT a production-grade ubu1 GPU
  replacement
- mvp 5/6 → 6/6 alien-grade unlock STILL requires ubu1 GPU (Mac CPU
  validates plumbing only, not production performance)
- raw 47 cross-repo: ~/core/hexa-weave/ directory absent, user approval
  required to init (W5 user-OK item #1 in cycle 14 spec)
- raw 14 ext-ssot: PyPI external dependency declared but not yet
  vendored — agent does NOT auto-install (sandbox-out)
