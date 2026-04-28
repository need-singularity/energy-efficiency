---
category: external-disclosure
date: 2026-04-28
parent_witness: design/kick/2026-04-28_w5-supporting-scripts-cycle15_omega_cycle.json
parent_proposal: proposals/hexa_weave_mvp_w5_sandbox_cycle14_prep_2026_04_28.md
predecessor_proposal: proposals/hexa_weave_mvp_w5_sandbox_cycle14_prep_2026_04_28.md
mission: cycle 15 — sister repo ~/core/hexa-weave/README.md spec (1-of-3 W5 supporting prep) — F-TP5-b 90d MVP linkage
status: SPEC only. README.md NOT written to ~/core/hexa-weave/. agent does not mkdir sibling repo. user creates on dispatch.
---

# HEXA-WEAVE sister repo README.md — spec for user dispatch (cycle 15)

raw 9 hexa-only data path. raw 13 NO external comms. raw 91 C3 honest:
this proposal contains the **textual spec only** for the sister repo
`~/core/hexa-weave/README.md`. The agent does NOT create the sibling
repo directory and does NOT write the README to disk. The user creates
the file at W5 dispatch time using this spec verbatim.

## §0 WHY a separate spec, why now (cycle 15)

Cycle 14 W5 sandbox prep (`proposals/hexa_weave_mvp_w5_sandbox_cycle14_prep_2026_04_28.md`)
disclosed in §"deliverables_NOT_produced_this_cycle":

> ~/core/hexa-weave/README.md (spec'd in proposal §4 only; not written to
> disk per raw 91 C3 — agent does not create the sister repo dir)

Cycle 15 (this) addresses that gap by producing a **dispatch-ready spec**
in `n6-architecture/proposals/`. The spec is consumed by the user's
single command at W5 dispatch:

```sh
mkdir -p ~/core/hexa-weave
cat > ~/core/hexa-weave/README.md <<'EOF'
<contents of §3 below>
EOF
```

This proposal complements the supporting scripts authored in cycle 15
(`scripts/rcsb_cluster_split_fetch.py`, `scripts/w5_verdict.py`,
`tool/hexa_weave_vram_ladder.hexa`) so that, by the end of cycle 15, a
single user command suffices to dispatch the entire W5 8-step runbook
with all referenced scripts present.

## §1 F-TP5-b 90d MVP linkage

`F-TP5-b` is the falsifier "HEXA-WEAVE 90-day MVP delivers a single
empirical inference (6L1U or equivalent) with RMSD<5Å + TM>0.4 +
VRAM<12GB on RTX 5070" deadline 2026-07-28 (90d from 2026-04-28).
The sister-repo README is the **public-facing artifact** that the
user/community sees first; it must:

- declare **Apache-2.0** license (matching OpenFold v2.2.0)
- disclose **OpenFold weights are CC-BY-4.0** (params_model_*.pkl)
- enumerate the 12-package torch+bio dependency stack (cycle-7 spec)
- link back to `n6-architecture/proposals/hexa_weave_mvp_w5_sandbox_cycle14_prep_2026_04_28.md`
- record the F-TP5-b deadline and verifier path

## §2 5-section structure

| # | Section | Purpose |
|---|---------|---------|
| 1 | Overview | What HEXA-WEAVE is, F-TP5-b 90d MVP scope, n6 hook positions (N6-H1..H5) |
| 2 | Setup | mkdir + venv + torch+11pkg + clone + weights + RCSB-split + sm_120 deepspeed |
| 3 | Inference | 6L1U dry-run command + expected outputs (predictions/*.pdb) + log paths |
| 4 | Verification | scripts/w5_verdict.py thresholds + tool/hexa_weave_vram_ladder.hexa 4-rung |
| 5 | License | Apache-2.0 (code) + CC-BY-4.0 (weights) + citation block + Zenodo DOI placeholder |

## §3 Verbatim README.md content

```markdown
<!--
SPDX-License-Identifier: Apache-2.0
Copyright (c) 2026 multi404error@proton.me
HEXA-WEAVE — n6-invariant cross-modal protein/RNA fold sandbox
F-TP5-b 90-day MVP (deadline 2026-07-28)
Parent: github.com/<user>/n6-architecture
-->

# HEXA-WEAVE

n6-invariant cross-modal protein/RNA fold sandbox. 90-day MVP per
falsifier F-TP5-b.

> **Status (cycle 15 / 2026-04-28):** sandbox dir + venv + torch +
> OpenFold v2.2.0 + AlphaFold weights + 6L1U dry-run pending user
> dispatch. See `n6-architecture/proposals/hexa_weave_mvp_w5_sandbox_cycle14_prep_2026_04_28.md`
> for the 8-step runbook.

## 1. Overview

HEXA-WEAVE evaluates the **n6 invariant** (`n6 = 6 × (φ=2 × τ=4 × σ=12 × J2=24 × κ=12)`)
as a regularizer on cross-modal protein folding. Five hook positions
attach the invariant non-invasively to OpenFold v2.2.0:

| Hook | Name | Position | Invasive |
|------|------|----------|----------|
| N6-H1 | τ=4 dihedral kmeans | post-process on output PDB | no |
| N6-H2 | σ=12 icosahedral / DSSP | post-process / StructureModule subclass | fallback only |
| N6-H3 | J2=24 PC project | evoformer block 47 pair-tensor z | yes |
| N6-H4 | φ=2 hydropathy/SASA bit | post-process FASTA + DSSP | no |
| N6-H5 | master identity check | aggregator `n6/master_identity.py` | no |

F-TP5-b deadline: **2026-07-28** (90d from 2026-04-28).

## 2. Setup

Single-command dispatch (run from `n6-architecture/`):

```sh
hexa run tool/hexa_weave_w5_setup.hexa
```

Steps (idempotent + rollback-able per `tool/hexa_weave_w5_setup.hexa`):

1. mkdir tree (`~/core/hexa-weave/{openfold,weights,test_inputs,outputs,...}`)
2. python3.10 venv
3. PyTorch 2.5.1+cu124 + 11-package install (`numpy<2 + biopython + biotite + rdkit + pydantic + einops + ml_collections + dm-tree + ...`)
4. OpenFold v2.2.0 shallow clone (commit pin `e938c184`)
5. AlphaFold weights download (~3 GB; `params_model_{1..5}.pkl` + ptm)
6. RCSB cluster-split download (78 train / 13 val / 9 test; seed `0xf927314f`)
7. sm_120 deepspeed source compile (CUDA arches 8.6;9.0;12.0)
8. 6L1U FASTA dry-run inference (single-seq + bf16)

Total: ~74 min sequential, ~8.6 GB disk, ~8.0 GB network. All steps
reversible via `--rollback`.

## 3. Inference

```sh
source ~/core/hexa-weave/venv/bin/activate
cd ~/core/hexa-weave/openfold
PYTHONHASHSEED=42 python run_pretrained_openfold.py \
  --fasta_paths ~/core/hexa-weave/test_inputs/6L1U.fasta \
  --use_single_seq_inference \
  --jax_param_path ~/core/hexa-weave/weights/params/params_model_1.pkl \
  --model_device cuda:0 \
  --bf16 \
  --output_dir ~/core/hexa-weave/outputs/
```

Expected output: `~/core/hexa-weave/outputs/predictions/6L1U_unrelaxed_model_1.pdb`.

VRAM polling (background): `nvidia-smi -lms 500` -> `~/core/hexa-weave/logs/vram_poller_*.csv`.

## 4. Verification

Deterministic verdict (no LLM judge):

```sh
python ~/core/n6-architecture/scripts/w5_verdict.py \
  --pred ~/core/hexa-weave/outputs/predictions/6L1U_unrelaxed_model_1.pdb \
  --ref  ~/core/hexa-weave/test_inputs/6L1U_ref.pdb \
  --fasta ~/core/hexa-weave/test_inputs/6L1U.fasta \
  --vram-csv "~/core/hexa-weave/logs/vram_poller_*.csv" \
  --rmsd-max 5.0 --tm-min 0.4 --vram-max-mb 11000 \
  --out ~/core/hexa-weave/outputs/verdict.json
```

Pass: `RMSD < 5.0 Å` + `TM-score > 0.4` + `VRAM peak < 11000 MB` +
`inference rc == 0` + `wall < 1800s` + residue count match.

4-rung VRAM ladder:

```sh
hexa run ~/core/n6-architecture/tool/hexa_weave_vram_ladder.hexa
```

| Rung | Case | Length | VRAM target | Pass |
|------|------|--------|-------------|------|
| L1 | 6L1U mini | 60 aa | 3-4 GB | RMSD<5Å, TM>0.4 |
| L2 | ESM3 mid | 100 aa | 5-6 GB | no OOM |
| L3 | 1UBQ proxy | 76 aa | 7-8 GB | RMSD<3Å |
| L4 | post-W6 target | 350 aa | 10-11 GB | VRAM<11GB |

## 5. License

- **Code**: Apache License 2.0. See `LICENSE`. SPDX: `Apache-2.0`.
- **OpenFold weights** (`params_model_*.pkl`): CC-BY-4.0 from
  https://github.com/aqlaboratory/openfold (commit pin `e938c184`).
- **AlphaFold weights derived** subject to DeepMind original terms; see
  https://github.com/google-deepmind/alphafold.

### Citation

```
@software{hexa_weave_2026,
  author    = {multi404error},
  title     = {HEXA-WEAVE: n6-invariant cross-modal protein fold sandbox},
  year      = {2026},
  url       = {https://github.com/<user>/hexa-weave},
  doi       = {10.5281/zenodo.<TBD-cycle-13-zenodo-deposit>}
}
```

Parent: `n6-architecture/proposals/hexa_weave_mvp_w5_sandbox_cycle14_prep_2026_04_28.md`.
Falsifier: `F-TP5-b` (deadline 2026-07-28).
```

## §4 raw 91 C3 honest disclosure

- This proposal does NOT mkdir `~/core/hexa-weave/`.
- This proposal does NOT write `README.md` to `~/core/hexa-weave/`.
- This proposal does NOT create a git repo at the sister path.
- The user is responsible for creating the file via the §0 cat heredoc
  during W5 dispatch on the appropriate host (Mac for §3 only; ubu1 for
  steps 3+).
- The Zenodo DOI is `<TBD-cycle-13-zenodo-deposit>` until
  `proposals/hexa_weave_zenodo_deposit_prep_2026_04_28.md` cycle 13+
  prep is dispatched + DOI minted.

## §5 own-doc-lint expectations

- own#1 English-only: PASS (no Korean prose; rune labels in tool/* only)
- own#22 snake_case + _YYYY_MM_DD naming: PASS (`hexa_weave_sister_repo_README_spec_2026_04_28.md`)
- own#23 umbrella declaration: PASS (no umbrella declared; sub-doc of W5 cycle-14 prep)
- own#16 cross-link to parent: PASS (`parent_proposal:` in front-matter + §0 prose)

## §6 falsifier hooks

This spec is non-falsifiable on its own (textual spec only). Empirical
verification is gated on:

- F-W5C14-1 (8-step runbook completion) — deadline 2026-05-26
- F-W5C14-2 (Step 8 6L1U PASS) — deadline 2026-05-26
- F-TP5-b (90d MVP 6L1U RMSD<5Å + TM>0.4 + VRAM<12GB) — deadline 2026-07-28

If the user dispatches W5 and Step 8 returns a verdict.json with
`verdict=PASS`, this README spec is **redeemed** as the public-facing
artifact for the empirical evidence.
