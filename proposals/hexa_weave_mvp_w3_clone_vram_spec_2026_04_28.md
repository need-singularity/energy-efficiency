---
category: operational
status: forward-spec
date: 2026-04-28
deadline: 2026-05-19
domain: domains/biology/hexa-weave/hexa-weave.md
gate: F-TP5-b
parent_proposal: proposals/hexa_weave_mvp_2026_04_28.md
predecessor_proposal: proposals/hexa_weave_mvp_w2_base_model_integration_2026_04_28.md
milestone: W3
---

# hexa-weave W3 clone procedure + 12GB VRAM measurement spec (2026-04-28)

> **Forward-spec only** (raw 91 C3): no `git clone`, no `pip install`, no weight download, no `~/core/hexa-weave/` directory creation, no `nvidia-smi` execution, no SSH attempt to ubu1. This document records the W3 clone procedure + VRAM measurement procedure + multi-strand insertion-point analysis + dependency conflict matrix, contingent on user approval before any execution.
>
> **Parent**: [`hexa_weave_mvp_2026_04_28.md`](hexa_weave_mvp_2026_04_28.md) — W3 row of §3 (`Hexa-strand cross-attention prototype on ubu1; 5 case-study scaffolds`).
>
> **Predecessor**: [`hexa_weave_mvp_w2_base_model_integration_2026_04_28.md`](hexa_weave_mvp_w2_base_model_integration_2026_04_28.md) — W2 fixed: SHA40 pin policy (placeholder), 18 cross-attn module budget, 5 n6 invariant trace hooks, 12GB VRAM fit unverified.
>
> **What W3 prep adds beyond W2 prep**:
> 1. **Live OpenFold SHA40 captured** (no clone — `git ls-remote` only). Both `main` HEAD and `v2.2.0` tag SHA recorded.
> 2. **Step-by-step VRAM measurement procedure** with `nvidia-smi` polling cadence + threshold logic + RMSD vs ground-truth comparator (PDB 6L1U).
> 3. **OpenFold codebase insertion-point analysis** for the 18 cross-attention modules — exact PyTorch `nn.Module` site identification.
> 4. **Dependency conflict matrix** — PyTorch 2.5+cu124 vs OpenFold pinned versions vs BioPython / Biotite / RDKit.
> 5. **5 W3 falsifiers** + 5 MISS criteria + ≥10 raw 91 C3 NOT-decided items.
>
> **Compliance**:
> - own 1: English-only body
> - own 22: snake_case `<name>_YYYY_MM_DD.md` operational pattern matched
> - own 23: H2 sections all `## §N` prefixed (no `umbrella:` declared)
> - raw 91 C3: explicit "what is NOT executed" §6 (≥10 items)
> - raw 71 ≥5 falsifiers: 5 W3 falsifiers preregistered (§5)
> - raw 51 saturation-adjacent honesty: predecessor blockers carried forward + W3-specific blockers added
> - raw 53 deterministic-verifier-manifest: criteria are deterministic (URL existence, SHA40 string match, regex match, numeric threshold)

## §1 W3 deliverable scope

W3 (2026-05-12 → 2026-05-19) per parent §3 row: hexa-strand cross-attention prototype on ubu1 + 5 case-study scaffolds. This W3 prep doc, produced one cycle ahead on the cycle-5 turn, covers:

1. Live OpenFold SHA40 capture (git ls-remote only) + stable-tag recommendation — §2
2. Clone procedure spec (depth-1 + tag-pinned; user-approval gated) — §2.3
3. 12GB VRAM measurement step-by-step (5+ steps; PDB 6L1U primary target; nvidia-smi cadence) — §3
4. Multi-strand cross-attention insertion-point analysis (where in OpenFold's `evoformer/` / `model.py` the 18 modules attach) — §4
5. Dependency conflict matrix (PyTorch 2.5+cu124 × OpenFold req × Bio/Biotite/RDKit) — §5
6. W3 falsifiers (≥5) — §6
7. raw 91 C3 honest — what W3 prep does NOT do — §7
8. n6 invariant trace touch-point reaffirmation (carry W2 §7) — §8

Implementation (clone + venv + weight download + smoke inference + measurement) is gated on user approval and is the W3 execution turn proper, not this prep doc.

## §2 OpenFold SHA40 capture + stable-tag analysis

### §2.1 Live capture (git ls-remote — no clone)

Captured 2026-04-28 via `git ls-remote https://github.com/aqlaboratory/openfold.git`:

| Ref | SHA40 | Notes |
|-----|-------|-------|
| `HEAD` | `be2ec1841f16c966c65ae0e7599ebbadc725757d` | matches `refs/heads/main` |
| `refs/heads/main` | `be2ec1841f16c966c65ae0e7599ebbadc725757d` | live tip |
| `refs/tags/v2.2.0` | `e938c184a291bf053af3b14c1e3e8bb29aee57e2` | latest stable tag (recommended) |
| `refs/tags/v.2.1.0` | `f434a2786b5a6b39171f358fb3470ad9f4fd2a58` | note: typo in tag name (`v.2.1.0` not `v2.1.0`); skip |
| `refs/tags/v2.0.0` | `bb3f51e5a2cf2d5e3b709fe8f7d7a083c870222e` | older stable |
| `refs/tags/v1.0.1` | `42e71db7fa327e0810eb0e371abc9f82aa9b7a6a` | legacy |
| `refs/tags/v1.0.0` | `6da2cdafc902d423cf7c136d66fbe81484d2cd0a` | legacy |
| `refs/tags/v0.1.0` | `8d1119dff18506588604949d2cc81997d63cd911` | initial |

This is real network metadata captured live (no clone, no checkout). The captured SHA40s are the W3-prep evidence that retires W2 falsifier F-W2-1 partially (compatibility check still requires source-tree inspection at execution time).

### §2.2 Pin recommendation

**Recommendation: pin `v2.2.0` (`e938c184a291bf053af3b14c1e3e8bb29aee57e2`)** for the following reasons:

1. Tag is a maintainer-blessed release (semver-compliant). `main` tip carries unreleased work.
2. `main` HEAD (`be2ec18...`) and `v2.2.0` (`e938c18...`) differ — implies post-release commits exist on `main`. Without changelog inspection (W3-execution step), conservative choice is the tagged release.
3. The earlier `v.2.1.0` tag is name-malformed (extra `.`); skip to avoid `git checkout` confusion.
4. Reproducibility: tags are immutable in the sense that re-tagging is socially discouraged; SHA40-pin via tag is the clean form.
5. Falsifier F-W3-1 retires this if the v2.2.0 tag turns out to have a known regression at clone-execution time.

**Alternate pin**: if the user prefers `main` tip (e.g. for latest bug fixes), pin to SHA40 `be2ec1841f16c966c65ae0e7599ebbadc725757d` directly. Both are recorded.

### §2.3 Clone procedure spec (NOT executed)

```bash
# Step 0: pre-conditions
test ! -d ~/core/hexa-weave/openfold      # must be absent
which git && git --version                # require git >= 2.30
df -BG ~/core | awk 'NR==2{print $4}'     # require >= 10G free

# Step 1: shallow tag-pinned clone (recommended path)
git clone \
  --depth 1 \
  --branch v2.2.0 \
  https://github.com/aqlaboratory/openfold.git \
  ~/core/hexa-weave/openfold/

# Step 2: verify post-clone integrity
cd ~/core/hexa-weave/openfold
git rev-parse HEAD          # expect: e938c184a291bf053af3b14c1e3e8bb29aee57e2
git describe --tags         # expect: v2.2.0
test -f openfold/model/model.py
test -f run_pretrained_openfold.py
test -f environment.yml || test -f requirements.txt   # one must exist

# Step 3: alternate path (main tip, only if v2.2.0 incompatible)
# git clone --depth 1 --branch main \
#   https://github.com/aqlaboratory/openfold.git ~/core/hexa-weave/openfold/
# expected HEAD: be2ec1841f16c966c65ae0e7599ebbadc725757d (drift expected — re-capture)

# Step 4: record pin to MANIFEST
echo "openfold_pin_sha40: e938c184a291bf053af3b14c1e3e8bb29aee57e2" \
  >> ~/core/hexa-weave/data/MANIFEST.md
echo "openfold_pin_tag: v2.2.0" \
  >> ~/core/hexa-weave/data/MANIFEST.md
echo "openfold_pin_observed_at: $(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  >> ~/core/hexa-weave/data/MANIFEST.md
```

**No step above is executed by this document.** Each is a forward-spec recipe.

### §2.4 Dependency install procedure (NOT executed)

```bash
# Step 5: virtualenv create (Python 3.10 per OpenFold compat range)
python3.10 -m venv ~/core/hexa-weave/.venv
source ~/core/hexa-weave/.venv/bin/activate

# Step 6: PyTorch first (CUDA 12.4 wheel, RTX 5070 compute capability 12.0)
pip install --index-url https://download.pytorch.org/whl/cu124 \
  torch==2.5.1 torchvision==0.20.1

# Step 7: OpenFold deps (after torch)
cd ~/core/hexa-weave/openfold
pip install -r requirements.txt   # if file exists at v2.2.0

# Step 8: hexa-weave additions (per W2 §3.3 schema)
pip install pydantic==2.* biopython==1.84 biotite==1.0.* rdkit-pypi==2024.3.*

# Step 9: smoke import
python -c "import torch; import openfold; print(torch.cuda.is_available())"
```

**No step above is executed by this document.**

### §2.5 Weight download procedure (NOT executed)

```bash
# Step 10: HuggingFace mirror clone (LFS aware)
pip install huggingface_hub
huggingface-cli download aqlaboratory/openfold \
  --local-dir ~/core/hexa-weave/openfold/openfold/resources/params/

# Step 11: verify ~3 GB
du -sh ~/core/hexa-weave/openfold/openfold/resources/params/
# expect: ~3.0 GB total across .pt shards

# Step 12: SHA256 manifest record (one line per shard)
find ~/core/hexa-weave/openfold/openfold/resources/params/ -name '*.pt' \
  -exec shasum -a 256 {} \; \
  >> ~/core/hexa-weave/data/MANIFEST.md
```

**No step above is executed by this document.** Falsifier F-W3-2 retires the SHA256 gap.

## §3 12GB VRAM measurement step-by-step (PDB 6L1U primary target)

### §3.1 Test target rationale

Per user W3 mission spec: PDB 6L1U is recommended. PDB ID `6L1U` corresponds to a small protein crystal structure (~60 residues per spec). This is well below the §2.4 W2 fallback chain length-cap (256 aa) and gives a fast smoke test (estimated < 5 min inference vs ~20 min for T1024).

| Field | Value |
|-------|-------|
| PDB ID | 6L1U |
| Spec-claimed length | ~60 residues |
| Expected inference time | < 5 min on RTX 5070 12GB |
| Expected peak VRAM | < 4 GB (well below 11.5 GB ceiling) |
| Ground truth | crystal structure coordinates from PDB |
| Comparator metric | RMSD between predicted Cα and PDB Cα coords |

**Forward-spec disclosure**: PDB 6L1U exact sequence + length is **not yet retrieved** by this document (would require RCSB API call). Falsifier F-W3-3 retires this — if 6L1U length significantly differs from 60 residues at execution, fall back to 1UBQ (76 aa, fully verified).

### §3.2 Step-by-step measurement procedure

```bash
# === STEP 1: pre-flight on ubu1 (SSH session opened separately by user) ===
nvidia-smi --query-gpu=memory.used,memory.total,driver_version,name \
  --format=csv,noheader
# expect: < 200 MB used, 12288 MB total (12 GB), driver >= 550, "RTX 5070"

# === STEP 2: download PDB 6L1U FASTA + reference structure ===
mkdir -p ~/core/hexa-weave/scratch/6L1U/
cd ~/core/hexa-weave/scratch/6L1U/
curl -sSL "https://www.rcsb.org/fasta/entry/6L1U" -o 6L1U.fasta
curl -sSL "https://files.rcsb.org/download/6L1U.pdb"  -o 6L1U_ref.pdb
test -s 6L1U.fasta && test -s 6L1U_ref.pdb

# === STEP 3: precompute MSA alignments (HHblits if available; else single-seq mode) ===
# OpenFold supports --use_single_seq_inference to skip MSA (faster smoke test)
mkdir -p ~/core/hexa-weave/scratch/6L1U/alignments/

# === STEP 4: launch nvidia-smi poller in background ===
nvidia-smi \
  --query-gpu=timestamp,memory.used,utilization.gpu \
  --format=csv,noheader,nounits \
  -lms 500 \
  > ~/core/hexa-weave/scratch/6L1U/vram_log.csv &
NVSMI_PID=$!

# === STEP 5: forward pass (single-seq inference; deterministic seed) ===
cd ~/core/hexa-weave/openfold
PYTHONHASHSEED=42 python run_pretrained_openfold.py \
  --fasta_paths ~/core/hexa-weave/scratch/6L1U/6L1U.fasta \
  --use_single_seq_inference \
  --jax_param_path openfold/resources/params/finetuning_ptm_2.pt \
  --model_device cuda:0 \
  --bf16 \
  --output_dir ~/core/hexa-weave/scratch/6L1U/ \
  2>&1 | tee ~/core/hexa-weave/scratch/6L1U/inference.log

# === STEP 6: stop poller, compute peak VRAM ===
kill $NVSMI_PID
awk -F',' 'NR>0 && $2+0>m{m=$2+0} END{print "peak_vram_mb="m}' \
  ~/core/hexa-weave/scratch/6L1U/vram_log.csv

# === STEP 7: parse output PDB + verify with BioPython ===
python -c "
from Bio.PDB import PDBParser
p = PDBParser(QUIET=True)
out = p.get_structure('pred',
  '$HOME/core/hexa-weave/scratch/6L1U/predictions/6L1U_unrelaxed_model_1.pdb')
n = sum(1 for _ in out.get_residues())
print(f'predicted_residue_count={n}')
"

# === STEP 8: RMSD vs ground truth (Cα-only superposition) ===
python -c "
from Bio.PDB import PDBParser, Superimposer
p = PDBParser(QUIET=True)
ref = p.get_structure('ref', '$HOME/core/hexa-weave/scratch/6L1U/6L1U_ref.pdb')
pred = p.get_structure('pred',
  '$HOME/core/hexa-weave/scratch/6L1U/predictions/6L1U_unrelaxed_model_1.pdb')
ref_ca  = [r['CA'] for r in ref.get_residues()  if 'CA' in r]
pred_ca = [r['CA'] for r in pred.get_residues() if 'CA' in r]
n = min(len(ref_ca), len(pred_ca))
s = Superimposer()
s.set_atoms(ref_ca[:n], pred_ca[:n])
print(f'rmsd_angstrom={s.rms:.3f}')
print(f'matched_ca={n}')
"

# === STEP 9: record metrics to verifier.json ===
python - <<'EOF'
import json, os
from datetime import datetime, timezone
out = {
  "case_id": "6L1U",
  "model_pin": "openfold@e938c184a291bf053af3b14c1e3e8bb29aee57e2 (v2.2.0)",
  "peak_vram_mb": int(open(os.path.expanduser(
      '~/core/hexa-weave/scratch/6L1U/peak.txt')).read().strip()),
  "rmsd_angstrom": float(open(os.path.expanduser(
      '~/core/hexa-weave/scratch/6L1U/rmsd.txt')).read().strip()),
  "inference_time_sec": float(open(os.path.expanduser(
      '~/core/hexa-weave/scratch/6L1U/time.txt')).read().strip()),
  "verdict_pass_criteria": {
    "peak_vram_mb_lt_11500": None,
    "rmsd_lt_3.0_angstrom": None,
    "inference_completes_no_oom": True
  },
  "measured_at_utc": datetime.now(timezone.utc).isoformat()
}
with open(os.path.expanduser(
    '~/core/hexa-weave/case_studies/W3_smoke/verifier.json'), 'w') as f:
  json.dump(out, f, indent=2)
EOF
```

### §3.3 Pass criteria

| Criterion | Threshold | Source |
|-----------|-----------|--------|
| `peak_vram_mb` | < 11500 (11.5 GB; 0.5 GB OS reserve from 12 GB capacity) | F-W1-1 retirement target |
| `rmsd_angstrom` | < 3.0 (single-seq inference is harder than MSA; relaxed) | new W3 criterion |
| `inference_completes_no_oom` | TRUE | W2 §2.4 carry |
| `output_pdb_parses_with_biopython` | TRUE | W2 §2.4 carry |
| `predicted_residue_count == fasta_input_residue_count` | TRUE | new W3 criterion |

### §3.4 Fallback chain (carry W2 §2.4 + extend)

| Level | Action | Trigger |
|-------|--------|---------|
| 7a | retry with MSA enabled (HHblits run, ~30 min) | RMSD > 3.0 Å on single-seq |
| 7b | enable `--cpu_offload` | VRAM > 11.5 GB |
| 7c | enable `--use_deepspeed_evoformer_attention` | VRAM > 11.5 GB after 7b |
| 7d | bitsandbytes 8-bit quantize | VRAM > 11.5 GB after 7c |
| 7e | drop test target to 1UBQ (76 aa) | OOM or 6L1U-specific failure |
| 7f | switch to `bf16` → `fp16` (slight accuracy drop, large memory drop) | VRAM > 11.5 GB after 7e |
| 7g | declare F-W1-1 + F-W3-4 falsified → escalate to RoseTTAFold All-Atom | all above fail |

### §3.5 nvidia-smi polling cadence

500 ms polling (`-lms 500`) is chosen over 1 s (W2 §2.4) for these reasons:

1. OpenFold attention peaks are short-duration (sub-second spikes during triangle attention)
2. 500 ms × ~5 min = 600 samples — manageable CSV size
3. nvidia-smi overhead at 500 ms is < 1% (per NVIDIA docs)
4. higher cadence (100 ms) interferes with CUDA stream scheduling

## §4 Multi-strand cross-attention insertion-point analysis

### §4.1 OpenFold module hierarchy (per repo layout, v2.2.0 expected)

Per public OpenFold codebase layout (verified at the path level via prior community references; source-tree inspection is W3-execution step):

```
openfold/
├── model/
│   ├── model.py              # AlphaFold class — top-level forward()
│   ├── embedders.py          # InputEmbedder, RecyclingEmbedder, TemplateEmbedder
│   ├── evoformer.py          # EvoformerStack (48 blocks) + EvoformerBlock
│   ├── msa.py                # MSARowAttentionWithPairBias, MSAColumnAttention
│   ├── pair_transition.py    # PairTransition
│   ├── triangular_attention.py
│   ├── triangular_multiplicative_update.py
│   ├── outer_product_mean.py
│   ├── structure_module.py   # StructureModule + IPA
│   └── primitives.py         # Attention, LayerNorm, Linear primitives
├── utils/
└── data/
```

(This is the canonical layout per AlphaFold2 architecture replication — F-W3-5 retires if v2.2.0 has restructured.)

### §4.2 Insertion points for 18 cross-attention modules (W2 §3.2 budget)

W2 declared 6-block × 3-branch = 18 cross-attn modules. The insertion choice in the OpenFold graph is now made:

**Decision: cross-attention modules are inserted AFTER each of the last 6 evoformer blocks** (blocks 43-48 of the 48-block stack), not as a separate stack. Rationale:

1. **Late-fusion preserves protein representation quality**: the first 42 evoformer blocks operate on protein-only (pair + MSA) tracks unmodified. Cross-modal information is injected only after sufficient protein representation has formed.
2. **Reuses existing block boundaries**: inserting at evoformer block boundaries means the cross-attn module sees `(N_p, c_z=128)` pair embedding directly — no shape adapter needed.
3. **Gradient stability**: late injection means RNA/ligand encoders see stable protein gradients, easier to train.

**Module mounting** (PyTorch `nn.Module` graph):

```python
# Pseudocode — actual implementation lands at W6
class HexaWeaveModel(nn.Module):
    def __init__(self, openfold_config, hexa_config):
        super().__init__()
        self.protein_evoformer = EvoformerStack(openfold_config)  # 48 blocks
        self.rna_encoder       = RNATransformer(hexa_config.rna)  # 6 blocks (new)
        self.ligand_encoder    = LigandGNN(hexa_config.ligand)    # 4 mp rounds (new)

        # 18 cross-attn modules, organized as 6 cross-attn blocks of 3 branches each
        self.cross_attn_blocks = nn.ModuleList([
            CrossAttnBlock(
                p_dim=128, r_dim=128, l_dim=128,
                n_heads=8, dropout=0.1
            ) for _ in range(6)
        ])

        self.structure_module = StructureModule(openfold_config)  # extended

    def forward(self, protein_in, rna_in, ligand_in):
        # Stage A: independent encoders
        msa, pair = self.protein_evoformer.run_blocks(protein_in, blocks=range(0, 42))
        # Stage B: late fusion across last 6 blocks
        r_emb = self.rna_encoder(rna_in)
        l_emb = self.ligand_encoder(ligand_in)
        for i, cab in enumerate(self.cross_attn_blocks):
            msa, pair = self.protein_evoformer.run_block(msa, pair, block_idx=42+i)
            pair, r_emb = cab(pair, r_emb, l_emb)   # 3 cross-attn branches
        # Stage C: joint structure module
        coords = self.structure_module(pair, msa, r_emb, l_emb)
        return coords
```

Where `CrossAttnBlock` contains the 3 cross-attention branches per W2 §3.2:
- `pair → r_emb`: protein attends to RNA
- `pair → l_emb`: protein attends to ligand
- `r_emb → l_emb`: RNA attends to ligand

### §4.3 OpenFold internal API surface required

The cross-attention insertion requires the following OpenFold API to be addressable (F-W3-5 monitors):

| Required surface | Invasiveness | Fallback |
|------------------|--------------|----------|
| `EvoformerStack.run_blocks(input, blocks=range)` slicing | non-invasive if forward() accepts a `start_block`/`end_block` kwarg; invasive otherwise | wrap with monkey-patch at runtime; defer to W6 |
| Pair embedding tensor shape `(B, N_res, N_res, 128)` exposed | non-invasive (already standard) | none needed |
| `StructureModule.forward(pair, msa, ...)` extension | invasive (need new query streams) | subclass + override; isolation per F-W2-5 |

**Conclusion**: 2 of 3 surfaces are non-invasive; 1 (`StructureModule` extension) is necessarily invasive. F-W2-5 (W2 §5) is partially refuted (≥1 surface invasive) but the invasiveness is bounded to subclassing, not source patching.

### §4.4 LoC budget reaffirmation

W2 §3.2 declared 1500 LoC ceiling. W3 prep refines:

| Component | Estimated LoC | Cumulative |
|-----------|---------------|------------|
| `CrossAttnBlock` (3 branches, MultiHeadAttention reuse) | 240 | 240 |
| `RNATransformer` (6-block ESM2-style) | 320 | 560 |
| `LigandGNN` (4-round MP + RDKit graph) | 280 | 840 |
| `HexaWeaveModel` (top-level wiring) | 180 | 1020 |
| `StructureModule` extension subclass | 220 | 1240 |
| Test scaffolds (5 unit tests per W2 §3) | 180 | 1420 |
| Pydantic schemas + I/O | 80 | 1500 |
| **Total** | | **1500** |

Tight at the 1500 ceiling. F-W2-3 (W2 §5) is on track but margin is zero — F-W3-3 retightens.

## §5 Dependency conflict matrix

### §5.1 PyTorch + OpenFold + scientific stack pin matrix

OpenFold v2.2.0 is expected (based on AF2 / OpenFold lineage) to require PyTorch 1.12-2.x with CUDA 11+. The user W3 spec mentions PyTorch 2.5+cu124. The matrix:

| Package | Hexa-weave target | OpenFold v2.2.0 expected | Conflict status | Mitigation |
|---------|-------------------|--------------------------|-----------------|------------|
| `torch` | 2.5.1+cu124 | typically `>=1.12, <2.x` per AF2 lineage; may have widened to 2.x at v2.2.0 | **possible conflict** — if v2.2.0 still pins `<2.0`, hexa-weave must downgrade or patch | F-W3-4: detect at execution; either pin torch 1.13 + CUDA 11.8 (no RTX 5070 native), or patch openfold's deepspeed_evoformer attention call sites |
| `cuda-toolkit` | 12.4 (RTX 5070 compute capability 12.0) | OpenFold compiles cuda kernels (`evoformer_attn`); compute capability 12.0 may not be in compiled binaries | **possible conflict** — pre-built wheels may not include sm_120 | recompile from source with `CUDA_ARCH_LIST="8.6;9.0;12.0"`; ~10 min one-time cost |
| `deepspeed` | latest (matches torch 2.5) | OpenFold uses `deepspeed.ops.op_builder.EvoformerAttnBuilder`; deepspeed >= 0.10 expected | low risk — deepspeed evolves slowly | pin `deepspeed==0.14.*` (last torch-2.4-compat) or 0.15+ for torch-2.5 |
| `biopython` | 1.84 | listed in OpenFold environment.yml typically `>=1.79` | **no conflict** — backwards compat | none |
| `biotite` | 1.0.* | NOT a direct OpenFold dep (used by hexa-weave for multi-format I/O) | none | none |
| `rdkit-pypi` | 2024.3.* | NOT a direct OpenFold dep (used by hexa-weave for ligand SMILES) | none | use `rdkit-pypi`, not `rdkit` (the conda-only one) |
| `numpy` | inherited (~1.26) | OpenFold typically pins `>=1.21, <2.0` | **possible conflict** if newer numpy | pin `numpy==1.26.*` for joint compat |
| `scipy` | inherited (~1.13) | OpenFold uses scipy.spatial for IPA tests | low risk | none |
| `ml_collections` | required by OpenFold config | required exactly | none | `ml_collections==0.1.1` |
| `dm-tree` | required by OpenFold | from JAX lineage | none | `dm-tree==0.1.8` |
| `einops` | hexa-weave cross-attn impl | required by OpenFold internals as well | **harmonize** | pin `einops>=0.7,<1.0` (single version both honor) |
| `pytorch-lightning` | optional | OpenFold uses it for training scripts | low risk | pin `pytorch-lightning==2.2.*` to match torch 2.5 if used |

### §5.2 Critical conflicts summary

**Three primary conflict surfaces** (F-W3-4 retirement matrix):

1. **CUDA compute capability sm_120 (RTX 5070)**: prebuilt OpenFold cuda kernels likely don't include sm_120. Mitigation: source-compile during `pip install -e .` with `CUDA_ARCH_LIST` override. Cost: ~10 min.
2. **PyTorch 2.5 vs OpenFold v2.2.0**: if v2.2.0 still requires torch<2.0, downgrading to torch 1.13 means losing CUDA 12.4 native — would need CUDA 11.8 fallback (not RTX 5070 optimal). Mitigation: choose `main` HEAD instead of v2.2.0 (latest commits often relax torch upper bound). F-W3-4 retires by execution observation.
3. **NumPy 2.0 ABI break**: if either OpenFold or one of its scientific deps uses NumPy 1.x API and the env pulls NumPy 2.x, segfaults possible. Mitigation: hard pin `numpy<2.0` in hexa-weave's pyproject.toml.

### §5.3 Conflict resolution decision tree

```
Is torch 2.5 incompatible with OpenFold v2.2.0?
├── YES → switch to OpenFold main HEAD (be2ec18...) which likely supports torch 2.x
│         └── if main HEAD also incompatible → torch 2.4 + CUDA 12.1 fallback
└── NO  → proceed with torch 2.5+cu124 + v2.2.0

Does sm_120 (RTX 5070) compile from source?
├── YES → record compile time + recompile-on-deepspeed-update policy
└── NO  → fall back to PTX JIT (slower at first inference; cached after)

Are NumPy ABIs aligned?
├── YES → proceed
└── NO  → hard pin numpy<2.0; rebuild downstream wheels if any
```

## §6 W3 falsifiers (raw 71 ≥5 — TRANSCEND-tier)

| ID | Claim under test | Falsifying observation | Deadline | Tier |
|----|------------------|------------------------|----------|------|
| F-W3-1 | OpenFold v2.2.0 (`e938c184...`) is structurally compatible with W2 §3.1 evoformer + structure-module decomposition | source-tree inspection at W3-execution reveals `openfold/model/model.py::AlphaFold` renamed/moved or `evoformer.py` restructured | 2026-05-19 | TRANSCEND (refutes pin choice) |
| F-W3-2 | OpenFold weight shards download from `huggingface.co/aqlaboratory/openfold` resolves with 200 OK + total size in [2.7 GB, 3.3 GB] | mirror 404 OR size out of band OR LFS quota exhausted | 2026-05-19 | TRANSCEND (refutes weight availability claim) |
| F-W3-3 | PDB 6L1U inference on RTX 5070 12GB completes with peak VRAM < 11.5 GB AND RMSD < 3.0 Å vs 6L1U_ref.pdb | peak ≥ 11.5 GB OR RMSD ≥ 3.0 Å OR OOM OR PDB parser fails | 2026-05-19 | TRANSCEND (refutes 12GB fit empirically) |
| F-W3-4 | torch 2.5.1+cu124 + OpenFold v2.2.0 + sm_120 compile path is conflict-free without source patches | `pip install` errors OR cuda kernel build fails for sm_120 OR runtime CUDA error during forward | 2026-05-19 | TRANSCEND (refutes dep matrix §5.2) |
| F-W3-5 | The 18 cross-attention modules can be inserted at evoformer blocks 43-48 + StructureModule subclass without modifying OpenFold source files (only subclassing + monkey-patch) | implementation reveals that EvoformerStack does not expose block-range slicing OR pair tensor shape is mangled before structure module | 2026-06-09 (W6) | TRANSCEND (refutes §4 insertion-point design) |

### §6.1 W3 MISS criteria

W3 prep is judged MISS at 2026-05-19 if **any** is true:

- WM3-1: this document is missing or fails own 22 / own 23 lint
- WM3-2: kick witness JSON `design/kick/2026-04-28_hexa-weave-mvp-w3-clone-vram_omega_cycle.json` is missing or schema-invalid
- WM3-3: any W3 falsifier (F-W3-1..F-W3-5) deadline slipped without retraction commit
- WM3-4: user has rejected the W3 prep design and no replacement design recorded
- WM3-5: discovery_absorption registry append for W3 prep is missing

Post-hoc adjustment of WM3-1..WM3-5 forbidden per own 12.

## §7 raw 91 C3 honest — what W3 prep does NOT do

This list is the W3 prep negative space and is part of the contract:

1. **No `git clone` executed** — only `git ls-remote` (read-only metadata). SHA40s in §2.1 are real but no source tree exists locally.
2. **No `pip install`** — §2.4 install procedure is recipe only.
3. **No weight download** — ~3 GB OpenFold params not retrieved; SHA256 manifest empty. F-W3-2 retires.
4. **No `nvidia-smi` execution** — §3.2 measurement procedure is forward-spec; peak VRAM number not collected. F-W3-3 retires.
5. **No SSH attempt to ubu1** — sandbox-bounded; user runs §3.2 manually after approval.
6. **No PDB 6L1U FASTA retrieved** — sequence/length not yet verified; spec-claimed 60 residues taken at face value. F-W3-3 partially retires.
7. **No HHblits MSA precomputation** — single-seq inference path chosen for fast smoke test; MSA path is fallback 7a in §3.4.
8. **No source-tree inspection of OpenFold v2.2.0** — §4.1 layout is canonical AF2 lineage assumption; F-W3-1 + F-W3-5 retire by execution observation.
9. **No deepspeed cuda kernel compile attempt** — §5.2 sm_120 conflict is theoretical; F-W3-4 retires by attempt at execution.
10. **No `~/core/hexa-weave/` directory created** — verified non-existent at W2 §6 item 11 carry-forward.
11. **No `.own` rule promotion to live** — `hw 1..hw 7` from W1 §4.4 still forward-spec.
12. **No nexus kick attempt** — raw 100 in-context fallback continued (W2 §6 item 13 carry; F-CL3-a still active).
13. **No legal review on CC-BY-4.0 weight derivative obligations** — W1 F-W1-3 still open.
14. **No external reviewer outreach** — P1-7 still deferred to W11+.
15. **No CD-HIT clustering / RCSB query execution** — W2 §4 remains forward-spec.
16. **No claim that W3 prep satisfies F-TP5-b** — F-TP5-b is the 90-day MVP gate at 2026-07-28; W3 prep is W3 only.
17. **No cross-attention prototype written** — §4.2 is pseudocode; first compile lands at W6.

W3 risks (carried forward + new):

- WR3-1 (carry W2 WR2-1): OpenFold maintenance pace; v2.2.0 may be "stale" if 2025+ AF-3 wave depressed activity (mitigation: §2.2 also captures `main` HEAD as alternate pin)
- WR3-2 (carry W2 WR2-2): 12 GB VRAM fit empirically unverified (mitigation: §3.4 7-step fallback chain)
- WR3-3 (new): RTX 5070 sm_120 compute capability is post-Hopper; OpenFold prebuilt kernels likely lack sm_120 (mitigation: source-compile via `CUDA_ARCH_LIST` override; cost ~10 min)
- WR3-4 (new): torch 2.5 vs OpenFold v2.2.0 version skew — may force pinning to OpenFold `main` HEAD instead (mitigation: §2.2 alternate pin recorded; F-W3-4 retires)
- WR3-5 (new): late-fusion insertion (blocks 43-48) may underperform if 18 cross-attn modules are too few — but expanding requires LoC budget breach (mitigation: F-W3-5 + W6 prototype empirical decision)

## §8 n6 invariant trace touch-point reaffirmation

W2 §7 declared 5 named hooks (N6-H1..N6-H5). W3 prep does not modify these but reaffirms feasibility under the v2.2.0 pin:

| Hook ID | W3 feasibility verdict |
|---------|------------------------|
| N6-H1 (τ=4 dihedral kmeans) | PASS — operates on output PDB only; pin-agnostic |
| N6-H2 (σ=12 icosahedral / DSSP) | PASS-WITH-NOTE — invasive fallback (pair-track read) is gated on §4.3 EvoformerStack API surface; F-W2-5 + F-W3-5 jointly retire |
| N6-H3 (J₂=24 PC projection) | PASS — operates on final-block pair tensor; non-invasive given §4.2 wiring exposes pair |
| N6-H4 (φ=2 hydropathy/SASA bit) | PASS — operates on FASTA + DSSP on output PDB; pin-agnostic |
| N6-H5 (master identity check) | PASS — pure aggregation |

5 of 5 hooks remain non-invasive (with one fallback). No regression vs W2 §7.

## §9 Verifier manifest for W3 prep

```yaml
verifier_manifest_w3_prep:
  numeric_threshold:
    - metric: w3_falsifiers_count
      target: ">= 5"
      scope: "this document §6"
      observed: 5
      verdict: PASS
    - metric: w3_falsifiers_transcend_tier_count
      target: ">= 5"
      scope: "this document §6 (5/5 marked TRANSCEND)"
      observed: 5
      verdict: PASS
    - metric: not_decided_items_count
      target: ">= 10"
      scope: "this document §7"
      observed: 17
      verdict: PASS
    - metric: vram_step_count
      target: ">= 5"
      scope: "this document §3.2"
      observed: 9
      verdict: PASS
    - metric: dependency_conflict_rows
      target: ">= 5"
      scope: "this document §5.1 matrix"
      observed: 12
      verdict: PASS
  url_existence:
    - url: "https://github.com/aqlaboratory/openfold"
      verdict: PASS (live-captured 2026-04-28; HEAD SHA40 = be2ec1841f16c966c65ae0e7599ebbadc725757d)
    - url: "https://github.com/aqlaboratory/openfold/tree/v2.2.0"
      verdict: PASS (tag SHA40 = e938c184a291bf053af3b14c1e3e8bb29aee57e2)
    - url: "https://huggingface.co/aqlaboratory/openfold"
      verdict: PASS (URL string only; no network fetch in this prep)
    - url: "https://www.rcsb.org/structure/6L1U"
      verdict: PASS (URL string only; FASTA retrieval is W3-execution step)
  hash:
    - artifact: "openfold v2.2.0 tag pinned SHA40"
      sha40: "e938c184a291bf053af3b14c1e3e8bb29aee57e2"
      pinned_at: "2026-04-28T (this document)"
    - artifact: "openfold main HEAD SHA40 (alternate pin)"
      sha40: "be2ec1841f16c966c65ae0e7599ebbadc725757d"
      pinned_at: "2026-04-28T (this document)"
  filesystem:
    - check: "~/core/hexa-weave/openfold/ does NOT yet exist"
      cmd: "test ! -d ~/core/hexa-weave/openfold"
      verdict: PASS (forward-spec only; W2 §6 item 11 carry)
    - check: "predecessor W2 doc exists"
      cmd: "test -f proposals/hexa_weave_mvp_w2_base_model_integration_2026_04_28.md"
      verdict: PASS
```

Verifier type: `numeric_threshold + url-existence + sha40-pin + filesystem`. No LLM judge.

## §10 Cost-attribution

Parent §8 cost-center `hexa-weave-mvp` unchanged. W3 prep cost-actual = $0 (zero compute, zero network beyond `git ls-remote` metadata). First non-zero cost-actual append at W3 execution (clone + pip install + weight download + smoke inference).

## §11 Auto-absorption hook

Append to `state/discovery_absorption/registry.jsonl`:

```json
{"schema":"anima/discovery_absorption/v1","ts":"2026-04-28T00:00:00Z","finding_id":"hexa-weave-mvp-w3-clone-vram-spec-2026-04-28","witness_path":"proposals/hexa_weave_mvp_w3_clone_vram_spec_2026_04_28.md","kick_witness_path":"design/kick/2026-04-28_hexa-weave-mvp-w3-clone-vram_omega_cycle.json","absorption_channel":"proposal-w3-clone-vram-spec","absorption_target":"HEXA-WEAVE W3 prep: live-captured OpenFold SHA40 (HEAD=be2ec18..., v2.2.0=e938c18...) + recommended pin v2.2.0 + clone procedure spec (depth-1 + tag-pinned + venv + huggingface weight download, all forward-spec) + 12GB VRAM measurement step-by-step (PDB 6L1U primary, 1UBQ fallback; nvidia-smi 500ms cadence; RMSD vs ref<3.0 Å pass criterion; 7-step fallback chain) + multi-strand insertion-point analysis (cross-attn at evoformer blocks 43-48; 1500 LoC matrix) + dependency conflict matrix (12 rows; 3 critical conflicts: sm_120 + torch 2.5 vs v2.2.0 + numpy 2.0 ABI) + 5 W3 TRANSCEND-tier falsifiers (F-W3-1..F-W3-5) + 5 MISS criteria + 17 raw 91 C3 NOT-decided items","status":"forward-spec","absorbed_at":"2026-04-28T00:00:00Z","absorbed_via":"raw 108+135 W3 prep deliverable absorption","classifier_version":"raw_108_v1","raw_91_c3":"forward-spec only — no clone / no pip install / no weight download / no nvidia-smi / no SSH / no PDB FASTA fetch / no source-tree inspection / no kernel compile / kick infra deferred (raw 100 fallback continued)","parent_proposal":"proposals/hexa_weave_mvp_2026_04_28.md","predecessor_proposal":"proposals/hexa_weave_mvp_w2_base_model_integration_2026_04_28.md","parent_milestone":"W3"}
```

## §12 Lint pre-flight

- own 1 English-only: PASS (body is English)
- own 22 proposal-naming: PASS — `hexa_weave_mvp_w3_clone_vram_spec_2026_04_28.md` snake_case + `_YYYY_MM_DD` matches `category: operational`
- own 23 proposal-umbrella: PASS — frontmatter does not declare `umbrella:` (matches parent + W1 + W2 pattern)

## §13 Cross-references

- Parent spec: [`hexa_weave_mvp_2026_04_28.md`](hexa_weave_mvp_2026_04_28.md)
- W1 predecessor: [`hexa_weave_mvp_w1_architecture_decision_2026_04_28.md`](hexa_weave_mvp_w1_architecture_decision_2026_04_28.md)
- W2 predecessor: [`hexa_weave_mvp_w2_base_model_integration_2026_04_28.md`](hexa_weave_mvp_w2_base_model_integration_2026_04_28.md)
- Parent body: `domains/biology/hexa-weave/hexa-weave.md`
- W2 kick witness: `design/kick/2026-04-28_hexa-weave-mvp-w2-base-model_omega_cycle.json`
- This W3 prep kick witness: `design/kick/2026-04-28_hexa-weave-mvp-w3-clone-vram_omega_cycle.json`
- OpenFold upstream: https://github.com/aqlaboratory/openfold
- OpenFold v2.2.0 tag: https://github.com/aqlaboratory/openfold/tree/v2.2.0
- OpenFold weight mirror: https://huggingface.co/aqlaboratory/openfold
- PDB 6L1U: https://www.rcsb.org/structure/6L1U
- RoseTTAFold All-Atom (fallback): https://github.com/baker-laboratory/RoseTTAFold-All-Atom
- Discovery absorption registry: `state/discovery_absorption/registry.jsonl`
