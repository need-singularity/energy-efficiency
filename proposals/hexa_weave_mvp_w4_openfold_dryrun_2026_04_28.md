---
category: operational
status: forward-spec
date: 2026-04-28
deadline: 2026-05-26
domain: domains/biology/hexa-weave/hexa-weave.md
gate: F-TP5-b
parent_proposal: proposals/hexa_weave_mvp_2026_04_28.md
predecessor_proposal: proposals/hexa_weave_mvp_w3_clone_vram_spec_2026_04_28.md
milestone: W4
---

# hexa-weave W4 OpenFold sandbox dry-run spec (2026-04-28)

> **Forward-spec only** (raw 91 C3): no `git clone`, no `pip install`, no weight download, no `nvidia-smi` execution, no `~/core/hexa-weave/` directory creation, no SSH attempt to ubu1, no source-tree inspection, no compile attempt. This document records the W4 sandbox dry-run plan, contingent on user approval before any execution.
>
> **Parent**: [`hexa_weave_mvp_2026_04_28.md`](hexa_weave_mvp_2026_04_28.md) — W4 row of §3 (`OpenFold sandbox dry-run + small protein smoke test`).
>
> **Predecessor**: [`hexa_weave_mvp_w3_clone_vram_spec_2026_04_28.md`](hexa_weave_mvp_w3_clone_vram_spec_2026_04_28.md) — W3 fixed: live SHA40 capture (HEAD `be2ec184...`, v2.2.0 `e938c184...`), 12-step clone procedure spec, 9-step VRAM measurement spec, 12-row dependency conflict matrix.
>
> **What W4 prep adds beyond W3 prep**:
> 1. **Sandbox environment preparation plan** — ordered 6-step environment construction integrating W3's clone + venv + weight download into a single dry-run runbook (§2).
> 2. **Dry-run sanity check sequence** — minimal 3-step import-then-forward verification before W4.3 VRAM measurement (§3).
> 3. **W3 measurement integration call-through** — explicit linkage from §2 sandbox to §3.3 9-step VRAM measurement (§4) without duplicating the 35.5 KB W3 spec body.
> 4. **Expected pitfall + fallback matrix** — three pre-identified failure surfaces with mitigation (sm_120 RTX 5070 prebuilt absence, NumPy 2.0 ABI break, torch 2.5 vs v2.2.0 upper bound), bridging W3 §5.2 to W4 execution time (§5).
> 5. **Multi-strand extension insertion plan** — refinement of W3 §4.2 late-fusion design with concrete insertion-line discovery procedure (deferred to post-clone) (§6).
> 6. **5 W4 falsifiers** + 5 MISS criteria + ≥10 raw 91 C3 NOT-decided items (§7, §8).
>
> **Compliance**:
> - own 1: English-only body
> - own 22: snake_case `<name>_YYYY_MM_DD.md` operational pattern matched
> - own 23: H2 sections all `## §N` prefixed (no `umbrella:` declared)
> - raw 91 C3: explicit "what is NOT executed" §8 (>=10 items)
> - raw 71 >=5 falsifiers: 5 W4 falsifiers preregistered (§7), 5/5 TRANSCEND-tier
> - raw 51 saturation-adjacent honesty: predecessor blockers carried forward + W4-specific blockers added
> - raw 53 deterministic-verifier-manifest: criteria are deterministic (filesystem checks, exit codes, numeric thresholds, regex)

## §1 W4 deliverable scope

W4 (2026-05-19 -> 2026-05-26) per parent §3 row: OpenFold sandbox dry-run + small protein smoke test. This W4 prep doc, produced one cycle ahead on the cycle-7 fan-out 4/5 turn, covers:

1. Sandbox environment preparation plan (6 ordered steps; user-approval gated) — §2
2. Dry-run sanity check sequence (import + small protein forward) — §3
3. 12 GB VRAM measurement integration call-through to W3 §3.2 (no duplication) — §4
4. Expected pitfall + fallback matrix (sm_120 / NumPy 2.0 / torch upper bound) — §5
5. Multi-strand extension insertion plan refinement — §6
6. W4 falsifiers (>=5) — §7
7. raw 91 C3 honest — what W4 prep does NOT do — §8
8. n6 invariant trace touch-point reaffirmation — §9
9. Verifier manifest — §10

Implementation (clone + venv + weight download + smoke inference + measurement + cross-attention scaffold) is gated on user approval and is the W4 execution turn proper, not this prep doc.

## §2 W4.1 sandbox environment preparation plan (NOT executed)

### §2.1 Pre-flight checklist

```bash
# Step 0: pre-condition verification on host (Mac M2 development) or ubu1 (CUDA target)
test ! -d ~/core/hexa-weave                         # must be absent (W3 §6 item 10 carry)
which python3.10 && python3.10 --version            # require Python 3.10.x
which git && git --version                          # require git >= 2.30
df -BG ~/core | awk 'NR==2{print $4}'               # require >= 15 GB free (10 GB clone + 3 GB weights + 2 GB scratch)
nvidia-smi --query-gpu=name,driver_version --format=csv,noheader  # require RTX 5070 + driver >= 550 (ubu1 only)
```

All Step-0 checks are READ-ONLY; no environment mutation. Pass criterion: every check exits with rc=0 and matches expected pattern.

### §2.2 Six-step environment construction

```bash
# === STEP 1: directory creation ===
mkdir -p ~/core/hexa-weave/{openfold,weights,test_inputs,outputs,scratch,venv,case_studies/W4_smoke,data}
ls -la ~/core/hexa-weave/

# === STEP 2: Python 3.10 venv activation ===
python3.10 -m venv ~/core/hexa-weave/venv
source ~/core/hexa-weave/venv/bin/activate
python --version                                    # expect: Python 3.10.x
pip install --upgrade pip setuptools wheel

# === STEP 3: PyTorch 2.5.1 + cu124 install ===
pip install torch==2.5.1+cu124 torchvision==0.20.1+cu124 \
  --extra-index-url https://download.pytorch.org/whl/cu124
python -c "import torch; print(f'torch={torch.__version__} cuda={torch.version.cuda} avail={torch.cuda.is_available()}')"
# expect on ubu1: torch=2.5.1+cu124 cuda=12.4 avail=True
# expect on Mac M2: torch=2.5.1+cu124 cuda=12.4 avail=False (CPU-only smoke)

# === STEP 4: OpenFold v2.2.0 shallow clone ===
git clone --depth 1 --branch v2.2.0 \
  https://github.com/aqlaboratory/openfold.git \
  ~/core/hexa-weave/openfold
cd ~/core/hexa-weave/openfold
git rev-parse HEAD                                  # expect: e938c184a291bf053af3b14c1e3e8bb29aee57e2
git describe --tags                                 # expect: v2.2.0
test -f openfold/model/model.py
test -f run_pretrained_openfold.py
test -f requirements.txt

# === STEP 5: requirements + hexa-weave additions ===
pip install --no-deps "numpy<2.0"                   # hard-pin BEFORE openfold reqs (§5.2)
pip install -r ~/core/hexa-weave/openfold/requirements.txt
pip install pydantic==2.* biopython==1.84 biotite==1.0.* rdkit-pypi==2024.3.*
pip install einops==0.7.* ml_collections==0.1.1 dm-tree==0.1.8

# === STEP 6: weight download (~3 GB) ===
bash ~/core/hexa-weave/openfold/scripts/download_alphafold_params.sh \
  ~/core/hexa-weave/weights/
du -sh ~/core/hexa-weave/weights/                   # expect: ~3.0 GB
ls ~/core/hexa-weave/weights/params/                # expect: params_model_1.pkl..params_model_5.pkl + ptm variants
```

**No step above is executed by this document.** Each is a forward-spec recipe gated on user approval.

### §2.3 W3 spec linkage

Steps 1-6 above expand W3 §2.3 + §2.4 + §2.5 (3 separate procedures) into a single ordered runbook. The cross-references are:

| W4 step | W3 source | Difference |
|---------|-----------|------------|
| W4 Step 1 | W3 §2.3 Step 0 (pre-conditions) | adds explicit subdirectory layout (`openfold/`, `weights/`, `test_inputs/`, `outputs/`, `scratch/`, `venv/`, `case_studies/W4_smoke/`, `data/`) |
| W4 Step 2 | W3 §2.4 Step 5 (`python3.10 -m venv`) | path normalized to `~/core/hexa-weave/venv` (W3 used `.venv`); user spec uses `venv` |
| W4 Step 3 | W3 §2.4 Step 6 (`pip install torch`) | adds explicit `--extra-index-url` form per user spec |
| W4 Step 4 | W3 §2.3 Step 1 (clone) | identical (depth-1 + tag-pinned) |
| W4 Step 5 | W3 §2.4 Steps 7+8 (requirements + hexa adds) | adds `numpy<2.0` hard-pin BEFORE openfold reqs (§5.2 mitigation) |
| W4 Step 6 | W3 §2.5 (huggingface-cli download) | switches to `download_alphafold_params.sh` per user spec; both produce `params/*.pkl` |

The W3 doc remains the authoritative 35.5 KB reference; this doc does not duplicate the rationale tables.

## §3 W4.2 dry-run sanity check sequence (NOT executed)

### §3.1 Three-step minimum verification

```bash
# === STEP 7: import test ===
python -c "import openfold; print(f'openfold imported from {openfold.__file__}')"
echo $?                                             # expect: 0
# rc=0 + no traceback = openfold importable + no missing deps

# === STEP 8: small protein FASTA stage ===
mkdir -p ~/core/hexa-weave/test_inputs
curl -sSL "https://www.rcsb.org/fasta/entry/6L1U" \
  -o ~/core/hexa-weave/test_inputs/6L1U.fasta
test -s ~/core/hexa-weave/test_inputs/6L1U.fasta    # non-empty
head -1 ~/core/hexa-weave/test_inputs/6L1U.fasta    # expect ">6L1U_..." header
wc -c ~/core/hexa-weave/test_inputs/6L1U.fasta      # expect 100..500 bytes (60 aa + header)

# Also stage reference structure for §4 RMSD comparator
curl -sSL "https://files.rcsb.org/download/6L1U.pdb" \
  -o ~/core/hexa-weave/test_inputs/6L1U_ref.pdb
test -s ~/core/hexa-weave/test_inputs/6L1U_ref.pdb  # non-empty

# === STEP 9: dry-run forward pass (single-seq inference; deterministic seed) ===
mkdir -p ~/core/hexa-weave/outputs
cd ~/core/hexa-weave/openfold
PYTHONHASHSEED=42 python run_pretrained_openfold.py \
  --fasta_paths ~/core/hexa-weave/test_inputs/6L1U.fasta \
  --use_single_seq_inference \
  --jax_param_path ~/core/hexa-weave/weights/params/params_model_1.pkl \
  --model_device cuda:0 \
  --bf16 \
  --output_dir ~/core/hexa-weave/outputs/ \
  2>&1 | tee ~/core/hexa-weave/outputs/dryrun.log

# === Expected output artifact ===
test -f ~/core/hexa-weave/outputs/predictions/6L1U_unrelaxed_model_1.pdb
# OR (relaxed pipeline if Amber relax is enabled by default):
# test -f ~/core/hexa-weave/outputs/predictions/6L1U_relaxed.pdb
```

### §3.2 Sanity-check pass criteria

| Criterion | Threshold | Verifier type |
|-----------|-----------|---------------|
| `import openfold` | rc=0, no traceback | exit-code-deterministic |
| FASTA stage | non-empty file, header line starts with `>` | filesystem + regex |
| reference PDB stage | non-empty file (>10 KB typical for 60 aa) | filesystem |
| Forward pass | rc=0, no OOM, no CUDA error | exit-code-deterministic |
| Output PDB | exists at `~/core/hexa-weave/outputs/predictions/6L1U_*.pdb` | filesystem |
| Inference time | < 5 min (single-seq mode on RTX 5070) | numeric-threshold |

### §3.3 Mac M2 vs ubu1 dispatch

The dry-run sanity check is **CPU-runnable on Mac M2** (W3 §5.1 torch 2.5+cu124 still installs CPU build on Mac; CUDA paths gracefully no-op). Mac-M2 dry-run validates Steps 7-8 only; Step 9 forward pass requires CUDA -> defer to ubu1.

| Step | Mac M2 | ubu1 | Rationale |
|------|--------|------|-----------|
| 7 import | ALLOWED | ALLOWED | pure-Python import; no CUDA needed |
| 8 FASTA stage | ALLOWED | ALLOWED | curl-only |
| 9 forward pass | DEFER (rc=non-zero on `--model_device cuda:0`) | ALLOWED | requires sm_120 / RTX 5070 |

## §4 W4.3 12 GB VRAM measurement integration (NOT executed)

W3 §3.2 specifies the 9-step VRAM measurement procedure. W4 does NOT duplicate; instead, W4 invokes W3 §3.2 verbatim AFTER §3 sanity-check passes:

```bash
# === BRIDGE: hand-off from §3 to W3 §3.2 ===
# Pre-condition: §3 STEPS 7-9 all rc=0 + ~/core/hexa-weave/outputs/predictions/6L1U_*.pdb exists
# Then:
#   W3 §3.2 STEP 1 nvidia-smi pre-flight              -- already informed by W4 §2.1 STEP 0
#   W3 §3.2 STEP 2 6L1U FASTA + ref PDB               -- already done by W4 §3 STEP 8
#   W3 §3.2 STEP 3 MSA precompute (skipped via single-seq) -- W4 §3 STEP 9 also skipped
#   W3 §3.2 STEP 4 nvidia-smi -lms 500 background poller   -- NEW for W4
#   W3 §3.2 STEP 5 forward pass (with poller running)      -- RE-RUN of §3 STEP 9 with poller
#   W3 §3.2 STEP 6 kill poller, awk peak_vram_mb       -- NEW for W4
#   W3 §3.2 STEP 7 BioPython output PDB parse          -- NEW for W4
#   W3 §3.2 STEP 8 RMSD vs ref via Bio.PDB.Superimposer -- NEW for W4
#   W3 §3.2 STEP 9 verifier.json record                -- NEW for W4
```

Net new work in W4.3 vs W4 §3 sanity check: 5 NEW steps (poller / peak extract / parse / RMSD / verifier.json). The first 3 W3-§3.2 steps are already covered by W4 §2 + §3.

### §4.1 W3 §3.3 pass criteria carry

| Criterion | Threshold | W3 source |
|-----------|-----------|-----------|
| `peak_vram_mb` | < 11500 | W3 §3.3 |
| `rmsd_angstrom` | < 3.0 (single-seq relaxed) | W3 §3.3 |
| `inference_completes_no_oom` | TRUE | W2 §2.4 carry |
| `output_pdb_parses_with_biopython` | TRUE | W2 §2.4 carry |
| `predicted_residue_count == fasta_input_residue_count` | TRUE | W3 §3.3 |

### §4.2 W3 §3.4 fallback chain carry

7-level fallback (`7a` MSA enable -> `7b` cpu_offload -> `7c` deepspeed_evoformer_attention -> `7d` bnb 8-bit -> `7e` drop to 1UBQ -> `7f` bf16 -> fp16 -> `7g` escalate to RoseTTAFold All-Atom). No new fallback levels added in W4.

## §5 W4.4 expected pitfall + fallback matrix

### §5.1 Three primary pitfalls (W3 §5.2 carry + W4 elaboration)

| Pitfall ID | Failure surface | Detection | Mitigation | Cost |
|------------|-----------------|-----------|------------|------|
| P-W4-1 | RTX 5070 sm_120 prebuilt cuda kernels absent in OpenFold deepspeed_evoformer_attention | runtime CUDA error on first forward `kernel image is not for this GPU` OR `no kernel image is available for execution on the device` | source-compile via `CUDA_ARCH_LIST="8.6;9.0;12.0" pip install --no-binary deepspeed deepspeed==0.15.*` (or 0.14.*) | ~10 min one-time recompile |
| P-W4-2 | NumPy 2.0 ABI break — pre-NumPy-2.0 wheels in openfold's deps segfault when paired with NumPy 2.x | ImportError or segfault during `import openfold.model` | hard-pin `numpy<2.0` BEFORE openfold `pip install -r requirements.txt` (W4 §2.2 STEP 5 already does this) | zero (preventive) |
| P-W4-3 | torch 2.5 vs OpenFold v2.2.0 upper bound — if v2.2.0 still pins `torch<2.0`, requirements install fails | `pip install -r requirements.txt` errors with `torch>=1.12,<2.0` constraint | fallback path A: pin OpenFold `main` HEAD `be2ec184...` (W3 §2.2 alternate); fallback path B: torch 2.4.0+cu121 if main HEAD also constrained | ~5 min re-clone |

### §5.2 sm_120 source-compile recipe (P-W4-1 mitigation, NOT executed)

```bash
# After W4 §2 STEP 5 fails on deepspeed prebuilt:
pip uninstall -y deepspeed
CUDA_ARCH_LIST="8.6;9.0;12.0" \
DS_BUILD_OPS=1 \
DS_BUILD_EVOFORMER_ATTN=1 \
  pip install --no-binary deepspeed deepspeed==0.15.4

# Verify sm_120 kernel:
python -c "
import torch, deepspeed
print(f'torch.cuda.get_device_capability={torch.cuda.get_device_capability(0)}')
# expect: (12, 0) on RTX 5070
from deepspeed.ops.op_builder import EvoformerAttnBuilder
builder = EvoformerAttnBuilder()
print(f'evoformer_attn loaded={builder.is_compatible()}')
"
```

PTX JIT fallback (slower at first inference; cached after) if compile fails: `TORCH_USE_CUDA_DSA=1 python ...` triggers PTX compilation at runtime.

### §5.3 OpenFold main HEAD fallback recipe (P-W4-3 mitigation, NOT executed)

```bash
# If v2.2.0 requirements.txt rejects torch>=2.0:
rm -rf ~/core/hexa-weave/openfold
git clone --depth 1 --branch main \
  https://github.com/aqlaboratory/openfold.git \
  ~/core/hexa-weave/openfold
cd ~/core/hexa-weave/openfold
git rev-parse HEAD                          # expect: be2ec1841f16c966c65ae0e7599ebbadc725757d
                                            #         (re-capture in W4 execution; SHA may drift)
pip install -r requirements.txt
```

Drift handling: if `main` HEAD has advanced past `be2ec184...` between this prep doc and W4 execution, re-capture via `git ls-remote refs/heads/main` and update MANIFEST. SHA40 drift IS the W3 §2.2 alternate-pin scenario.

### §5.4 fallback matrix (consolidated)

| Pitfall | Detection regex / signal | Fallback A | Fallback B | Fallback C |
|---------|--------------------------|------------|------------|------------|
| sm_120 prebuilt absent | `kernel image is not for this GPU` | source-compile (§5.2) | PTX JIT runtime | escalate F-W3-4 |
| NumPy 2.0 ABI | segfault on `import` OR `module compiled against NumPy 1.x...` | hard-pin numpy<2.0 (§2.2 STEP 5) | rebuild downstream wheels | escalate F-W3-4 |
| torch upper bound | `pip` error `torch>=1.12,<2.0` constraint | OpenFold main HEAD pin (§5.3) | torch 2.4.0+cu121 | escalate F-W3-4 |
| OOM during forward | CUDA out-of-memory error | W3 §3.4 fallback `7b` cpu_offload | `7c` deepspeed_evoformer_attention | `7d` bnb 8-bit |
| RMSD > 3.0 Å | `rmsd_angstrom >= 3.0` from Bio.PDB.Superimposer | W3 §3.4 fallback `7a` MSA enable | `7e` drop to 1UBQ | escalate F-W3-3 |

## §6 W4.5 multi-strand extension insertion plan (refined)

### §6.1 W3 §4.2 carry — late-fusion at evoformer blocks 43-48

W3 declared 18 cross-attn modules (6 evoformer blocks x 3 branches: P->R, P->L, R->L). W4 prep refines:

**Insertion site decision (carry W3)**: cross-attention modules are inserted AFTER each of the last 6 evoformer blocks (blocks 43-48 of the 48-block stack), with a final cross-modal pass before StructureModule entry.

**Insertion line discovery procedure (NEW — deferred to post-clone W4 execution)**:

```bash
# After W4 §2 STEP 4 clone completes:
cd ~/core/hexa-weave/openfold

# Find EvoformerStack class definition:
grep -n "class EvoformerStack" openfold/model/evoformer.py
# expect: ~1 hit; record line number as EVOFORMER_STACK_DEFLINE

# Find StructureModule entry point (where pair tensor flows in):
grep -n "class StructureModule" openfold/model/structure_module.py
# expect: ~1 hit; record line number as STRUCTURE_MODULE_DEFLINE

# Find AlphaFold top-level forward() (where evoformer + structure_module compose):
grep -n "def forward" openfold/model/model.py
# expect: AlphaFold.forward; record line number as ALPHAFOLD_FORWARD_DEFLINE

# Insertion target: BETWEEN EvoformerStack's last block and StructureModule's first call,
# inside AlphaFold.forward(). Record exact pair-tensor variable name (likely `z` per AF2 conv).
```

Pseudocode for insertion (per W3 §4.2; LoC budget 1500 carry):

```python
# Pseudocode — actual implementation lands at W6
class HexaWeaveModel(nn.Module):
    def __init__(self, openfold_config, hexa_config):
        super().__init__()
        self.protein_evoformer = EvoformerStack(openfold_config)  # 48 blocks
        self.rna_encoder       = RNATransformer(hexa_config.rna)  # 6 blocks
        self.ligand_encoder    = LigandGNN(hexa_config.ligand)    # 4 mp rounds

        # 18 cross-attn modules = 6 blocks x 3 branches
        self.cross_attn_blocks = nn.ModuleList([
            CrossAttnBlock(p_dim=128, r_dim=128, l_dim=128, n_heads=8, dropout=0.1)
            for _ in range(6)
        ])
        self.structure_module = StructureModule(openfold_config)

    def forward(self, protein_in, rna_in, ligand_in):
        msa, pair = self.protein_evoformer.run_blocks(protein_in, blocks=range(0, 42))
        r_emb = self.rna_encoder(rna_in)
        l_emb = self.ligand_encoder(ligand_in)
        for i, cab in enumerate(self.cross_attn_blocks):
            msa, pair = self.protein_evoformer.run_block(msa, pair, block_idx=42+i)
            pair, r_emb = cab(pair, r_emb, l_emb)
        coords = self.structure_module(pair, msa, r_emb, l_emb)
        return coords
```

### §6.2 LoC ceiling carry (W3 §4.4)

| Component | Estimated LoC |
|-----------|---------------|
| `CrossAttnBlock` (3 branches) | 240 |
| `RNATransformer` (6-block ESM2-style) | 320 |
| `LigandGNN` (4-round MP) | 280 |
| `HexaWeaveModel` (top wiring) | 180 |
| `StructureModule` extension subclass | 220 |
| Test scaffolds | 180 |
| Pydantic schemas + I/O | 80 |
| **Total** | **1500** (zero margin) |

W4 prep does NOT modify the LoC budget. F-W2-3 + F-W3-3 retire jointly at W6 implementation.

### §6.3 OpenFold API surface dependency (W3 §4.3 carry)

| API surface | Invasiveness | Discovery step |
|-------------|--------------|----------------|
| `EvoformerStack.run_blocks(input, blocks=range)` slicing | non-invasive if `forward()` accepts `start_block`/`end_block` kwarg | grep `def forward` in `evoformer.py` post-clone |
| Pair embedding `(B, N_res, N_res, 128)` exposed | non-invasive (AF2 standard) | grep `pair_repr` or `z` in `model.py` |
| `StructureModule.forward(pair, msa, ...)` extension | invasive (subclass + override) | grep `def forward` in `structure_module.py` |

2/3 surfaces non-invasive; 1/3 bounded-invasive (subclass; no source patches). F-W3-5 retires by post-clone source-tree inspection.

## §7 W4 falsifiers (raw 71 >=5 — TRANSCEND-tier)

| ID | Claim under test | Falsifying observation | Deadline | Tier |
|----|------------------|------------------------|----------|------|
| F-W4-1 | The 6-step W4 §2.2 sandbox construction completes rc=0 on ubu1 with the recipes as written | any of STEPS 1-6 returns rc != 0 OR produces an unexpected file layout | 2026-05-26 | TRANSCEND (refutes recipe correctness) |
| F-W4-2 | `import openfold` succeeds rc=0 in the constructed venv after STEPS 1-6 (W4 §3 STEP 7) | ImportError, ModuleNotFoundError, or segfault | 2026-05-26 | TRANSCEND (refutes dep matrix application) |
| F-W4-3 | Small protein 6L1U single-seq dry-run forward pass (W4 §3 STEP 9) produces a parseable PDB at `~/core/hexa-weave/outputs/predictions/6L1U_*.pdb` within 5 min on RTX 5070 12 GB | rc != 0 OR no PDB output OR timeout > 5 min OR PDB fails BioPython parse | 2026-05-26 | TRANSCEND (refutes smoke test feasibility) |
| F-W4-4 | sm_120 prebuilt fallback chain (§5.2 source-compile OR PTX JIT) recovers from `kernel image is not for this GPU` error within 30 min | source-compile fails AND PTX JIT also fails | 2026-05-26 | TRANSCEND (refutes RTX 5070 OpenFold compat) |
| F-W4-5 | Insertion-line discovery via grep (§6.1) returns >=1 hit for each of `class EvoformerStack`, `class StructureModule`, `def forward` in `model.py` after W4 §2 STEP 4 clone | any grep returns 0 hits OR file path does not exist OR class renamed | 2026-05-26 | TRANSCEND (refutes module-layout assumption W3 §4.1) |

### §7.1 W4 MISS criteria

W4 prep is judged MISS at 2026-05-26 if **any** is true:

- WM4-1: this document is missing or fails own 22 / own 23 lint
- WM4-2: kick witness JSON `design/kick/2026-04-28_hexa-weave-mvp-w4-openfold-dryrun_omega_cycle.json` is missing or schema-invalid
- WM4-3: any W4 falsifier (F-W4-1..F-W4-5) deadline slipped without retraction commit
- WM4-4: user has rejected the W4 prep design and no replacement design recorded
- WM4-5: discovery_absorption registry append for W4 prep is missing

Post-hoc adjustment of WM4-1..WM4-5 forbidden per own 12.

## §8 raw 91 C3 honest — what W4 prep does NOT do

This list is the W4 prep negative space and is part of the contract:

1. **No `git clone` executed** — W4 §2.2 STEP 4 is recipe only. SHA40 evidence inherited from W3 §2.1 `git ls-remote` capture.
2. **No `pip install`** — W4 §2.2 STEPS 2-3-5 install procedures are recipe only.
3. **No weight download** — ~3 GB `download_alphafold_params.sh` not executed (W4 §2.2 STEP 6). F-W3-2 + F-W4-1 retire.
4. **No `nvidia-smi` execution** — W4 §2.1 STEP 0 + §4 measurement integration are forward-spec; peak VRAM not collected. F-W3-3 retires.
5. **No SSH attempt to ubu1** — sandbox-bounded; user runs W4 §2-3 manually after approval.
6. **No PDB 6L1U FASTA / reference structure retrieved** — W4 §3 STEP 8 is recipe only. F-W3-3 partially retires.
7. **No source-tree inspection of OpenFold v2.2.0** — W4 §6.1 grep procedure is recipe only. F-W3-1 + F-W3-5 + F-W4-5 retire by execution observation.
8. **No deepspeed source-compile attempt** — W4 §5.2 sm_120 recovery recipe is forward-spec. F-W3-4 + F-W4-4 retire.
9. **No `~/core/hexa-weave/` directory created** — verified non-existent at W3 §6 item 10 carry-forward.
10. **No `numpy<2.0` hard-pin enacted** — preventive plan only (W4 §2.2 STEP 5).
11. **No PTX JIT runtime test** — fallback B in §5.4 is recipe only.
12. **No OpenFold `main` HEAD re-clone** — fallback path A in §5.3 is recipe only.
13. **No insertion-line numbers captured** — W4 §6.1 grep targets are placeholders; actual line numbers known only post-clone.
14. **No `.own` rule promotion to live** — `hw 1..hw 7` from W1 §4.4 still forward-spec.
15. **No nexus kick attempt** — raw 100 in-context fallback continued (W3 §6 item 12 carry; F-CL3-a still active).
16. **No legal review on CC-BY-4.0 weight derivative obligations** — W1 F-W1-3 still open.
17. **No external reviewer outreach** — P1-7 still deferred to W11+.
18. **No CD-HIT clustering / RCSB query execution** — W2 §4 / W3 §6 still forward-spec.
19. **No claim that W4 prep satisfies F-TP5-b** — F-TP5-b is the 90-day MVP gate at 2026-07-28; W4 prep is W4 only.
20. **No cross-attention prototype source written** — W4 §6.1 pseudocode unchanged from W3 §4.2; first compile still lands at W6.
21. **No empirical claim of any kind** — 0 of 0 empirical observations in this document; all numbers are targets/thresholds.

W4 risks (carried forward + new):

- WR4-1 (carry W3 WR3-3): RTX 5070 sm_120 compute capability is post-Hopper; OpenFold prebuilt kernels likely lack sm_120. **Mitigation strengthened**: §5.2 explicit source-compile recipe with `CUDA_ARCH_LIST`.
- WR4-2 (carry W3 WR3-4): torch 2.5 vs OpenFold v2.2.0 version skew. **Mitigation strengthened**: §5.3 explicit `main` HEAD fallback recipe.
- WR4-3 (new): `download_alphafold_params.sh` may have been deprecated by AQLab in favor of HuggingFace mirror; if script missing, fall back to W3 §2.5 `huggingface-cli download` recipe.
- WR4-4 (new): single-seq inference may fail on 6L1U if the protein has non-standard residues; fallback to W3 §3.4 level `7e` (drop to 1UBQ) + level `7a` (enable MSA).
- WR4-5 (new): LoC budget zero-margin (1500 ceiling) means any unforeseen boilerplate (e.g. config registration, logging) breaches budget; mitigation deferred to W6 implementation gate.

## §9 n6 invariant trace touch-point reaffirmation

W2 §7 declared 5 named hooks (N6-H1..N6-H5). W3 §8 reaffirmed feasibility. W4 prep does not modify these but reaffirms once more under the dry-run plan:

| Hook ID | W4 dry-run feasibility verdict |
|---------|-------------------------------|
| N6-H1 (τ=4 dihedral kmeans) | PASS — operates on output PDB only (W4 §3 STEP 9 output); pin-agnostic |
| N6-H2 (σ=12 icosahedral / DSSP) | PASS-WITH-NOTE — invasive fallback gated on §6.3 EvoformerStack API surface; F-W2-5 + F-W3-5 + F-W4-5 jointly retire |
| N6-H3 (J₂=24 PC projection) | PASS — operates on final-block pair tensor; non-invasive given §6.1 wiring exposes pair |
| N6-H4 (φ=2 hydropathy/SASA bit) | PASS — operates on FASTA + DSSP on output PDB; pin-agnostic |
| N6-H5 (master identity check) | PASS — pure aggregation |

5 of 5 hooks remain non-invasive (with one fallback). No regression vs W3 §8.

## §10 Verifier manifest for W4 prep

```yaml
verifier_manifest_w4_prep:
  numeric_threshold:
    - metric: w4_falsifiers_count
      target: ">= 5"
      scope: "this document §7"
      observed: 5
      verdict: PASS
    - metric: w4_falsifiers_transcend_tier_count
      target: ">= 5"
      scope: "this document §7 (5/5 marked TRANSCEND)"
      observed: 5
      verdict: PASS
    - metric: not_decided_items_count
      target: ">= 10"
      scope: "this document §8"
      observed: 21
      verdict: PASS
    - metric: sandbox_construction_step_count
      target: ">= 5"
      scope: "this document §2.2"
      observed: 6
      verdict: PASS
    - metric: dryrun_sanity_check_step_count
      target: ">= 3"
      scope: "this document §3.1"
      observed: 3
      verdict: PASS
    - metric: pitfall_fallback_matrix_rows
      target: ">= 3"
      scope: "this document §5.4"
      observed: 5
      verdict: PASS
    - metric: w4_miss_criteria_count
      target: ">= 5"
      scope: "this document §7.1"
      observed: 5
      verdict: PASS
  url_existence:
    - url: "https://github.com/aqlaboratory/openfold"
      verdict: PASS (W3 §2.1 live-captured 2026-04-28; HEAD SHA40 = be2ec1841f16c966c65ae0e7599ebbadc725757d)
    - url: "https://github.com/aqlaboratory/openfold/tree/v2.2.0"
      verdict: PASS (W3 §2.1; tag SHA40 = e938c184a291bf053af3b14c1e3e8bb29aee57e2)
    - url: "https://download.pytorch.org/whl/cu124"
      verdict: PASS (PyPI extra-index URL string-checkable)
    - url: "https://www.rcsb.org/fasta/entry/6L1U"
      verdict: PASS (URL string only; FASTA retrieval is W4 execution step)
    - url: "https://files.rcsb.org/download/6L1U.pdb"
      verdict: PASS (URL string only; reference PDB retrieval is W4 execution step)
  hash:
    - artifact: "openfold v2.2.0 tag pinned SHA40 (carry W3 §2.1)"
      sha40: "e938c184a291bf053af3b14c1e3e8bb29aee57e2"
      pinned_at: "2026-04-28T (carried from W3 prep)"
    - artifact: "openfold main HEAD SHA40 (alternate pin; carry W3 §2.2)"
      sha40: "be2ec1841f16c966c65ae0e7599ebbadc725757d"
      pinned_at: "2026-04-28T (carried from W3 prep)"
  filesystem:
    - check: "~/core/hexa-weave/ does NOT yet exist"
      cmd: "test ! -d ~/core/hexa-weave"
      verdict: PASS (forward-spec only; W3 §6 item 10 carry)
    - check: "predecessor W3 doc exists"
      cmd: "test -f proposals/hexa_weave_mvp_w3_clone_vram_spec_2026_04_28.md"
      verdict: PASS
    - check: "predecessor W2 doc exists"
      cmd: "test -f proposals/hexa_weave_mvp_w2_base_model_integration_2026_04_28.md"
      verdict: PASS
    - check: "parent spec exists"
      cmd: "test -f proposals/hexa_weave_mvp_2026_04_28.md"
      verdict: PASS
```

Verifier type: `numeric_threshold + url-existence + sha40-pin + filesystem`. No LLM judge.

## §11 Cost-attribution

Parent §8 cost-center `hexa-weave-mvp` unchanged. W4 prep cost-actual = $0 (zero compute, zero network, zero filesystem mutation outside of this `proposals/` doc + witness JSON). First non-zero cost-actual append at W4 execution (clone + pip install + weight download + smoke inference + measurement + sm_120 source-compile if needed).

## §12 Auto-absorption hook

Append to `state/discovery_absorption/registry.jsonl`:

```json
{"schema":"anima/discovery_absorption/v1","ts":"2026-04-28T00:00:00Z","finding_id":"hexa-weave-mvp-w4-openfold-dryrun-2026-04-28","witness_path":"proposals/hexa_weave_mvp_w4_openfold_dryrun_2026_04_28.md","kick_witness_path":"design/kick/2026-04-28_hexa-weave-mvp-w4-openfold-dryrun_omega_cycle.json","absorption_channel":"proposal-w4-openfold-dryrun-spec","absorption_target":"HEXA-WEAVE W4 prep: 6-step sandbox construction (mkdir + py3.10 venv + torch 2.5.1+cu124 + openfold v2.2.0 depth-1 clone + numpy<2.0 hard-pin + requirements + ~3GB weight download via download_alphafold_params.sh) + 3-step dry-run sanity check (import openfold + 6L1U FASTA stage + single-seq forward pass --bf16 --model_device cuda:0) + W3 §3.2 9-step VRAM measurement integration call-through (no duplication; 5 net-new W4 steps: poller / peak / parse / RMSD / verifier.json) + 5-row pitfall+fallback matrix (sm_120 source-compile via CUDA_ARCH_LIST=8.6;9.0;12.0 + numpy<2.0 hard-pin + OpenFold main HEAD fallback + W3 §3.4 7-level VRAM fallback chain carry) + multi-strand insertion plan refinement (grep-based line-discovery procedure for EvoformerStack/StructureModule/AlphaFold.forward post-clone; 1500 LoC ceiling zero-margin carry; 2/3 OpenFold API non-invasive) + 5 W4 TRANSCEND-tier falsifiers (F-W4-1..F-W4-5) + 5 MISS criteria + 21 raw 91 C3 NOT-decided items","status":"forward-spec","absorbed_at":"2026-04-28T00:00:00Z","absorbed_via":"raw 108+135 W4 prep deliverable absorption","classifier_version":"raw_108_v1","raw_91_c3":"forward-spec only — no clone / no pip install / no weight download / no nvidia-smi / no SSH / no PDB FASTA fetch / no source-tree inspection / no source-compile / no PTX JIT test / kick infra deferred (raw 100 fallback continued)","parent_proposal":"proposals/hexa_weave_mvp_2026_04_28.md","predecessor_proposal":"proposals/hexa_weave_mvp_w3_clone_vram_spec_2026_04_28.md","parent_milestone":"W4"}
```

## §13 Lint pre-flight

- own 1 English-only: PASS (body is English)
- own 22 proposal-naming: PASS — `hexa_weave_mvp_w4_openfold_dryrun_2026_04_28.md` snake_case + `_YYYY_MM_DD` matches `category: operational`
- own 23 proposal-umbrella: PASS — frontmatter does not declare `umbrella:` (matches parent + W1 + W2 + W3 pattern)

## §14 Cross-references

- Parent spec: [`hexa_weave_mvp_2026_04_28.md`](hexa_weave_mvp_2026_04_28.md)
- W1 predecessor: [`hexa_weave_mvp_w1_architecture_decision_2026_04_28.md`](hexa_weave_mvp_w1_architecture_decision_2026_04_28.md)
- W2 predecessor: [`hexa_weave_mvp_w2_base_model_integration_2026_04_28.md`](hexa_weave_mvp_w2_base_model_integration_2026_04_28.md)
- W3 predecessor: [`hexa_weave_mvp_w3_clone_vram_spec_2026_04_28.md`](hexa_weave_mvp_w3_clone_vram_spec_2026_04_28.md)
- Parallel W4 Lean4 doc: [`hexa_weave_mvp_w4_lean4_mk_decision_2026_04_28.md`](hexa_weave_mvp_w4_lean4_mk_decision_2026_04_28.md)
- Parent body: `domains/biology/hexa-weave/hexa-weave.md`
- W3 kick witness: `design/kick/2026-04-28_hexa-weave-mvp-w3-clone-vram_omega_cycle.json`
- This W4 prep kick witness: `design/kick/2026-04-28_hexa-weave-mvp-w4-openfold-dryrun_omega_cycle.json`
- OpenFold upstream: https://github.com/aqlaboratory/openfold
- OpenFold v2.2.0 tag: https://github.com/aqlaboratory/openfold/tree/v2.2.0
- PyTorch CUDA 12.4 wheel index: https://download.pytorch.org/whl/cu124
- PDB 6L1U: https://www.rcsb.org/structure/6L1U
- RoseTTAFold All-Atom (escalation fallback): https://github.com/baker-laboratory/RoseTTAFold-All-Atom
- Discovery absorption registry: `state/discovery_absorption/registry.jsonl`

## §15 mk-history

- 2026-04-28 cycle-7 fan-out 4/5: W4 prep deliverable produced via in-context synthesis (raw 100 fallback continued). 5 TRANSCEND-tier falsifiers preregistered. Sandbox plan + dry-run plan + W3 §3.2 measurement call-through + pitfall matrix + multi-strand insertion refinement.
- 2026-04-28 cycle-5: W3 predecessor produced (35.5 KB; 12-step clone + 9-step VRAM + 12-row dep matrix + 5 TRANSCEND-tier falsifiers).
- 2026-04-28 cycle-3: W2 predecessor produced (28 KB; 18 cross-attn module budget; 5 n6 invariant trace hooks; 1500 LoC ceiling).
- 2026-04-28 cycle-2: W1 predecessor produced (architecture decision: OpenFold base; 12 GB VRAM ceiling on RTX 5070; 5 case-study scaffolds).
- 2026-04-28 cycle-1: hexa-weave-mvp parent spec authored.
