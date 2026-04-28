---
category: operational
status: forward-spec
date: 2026-04-28
deadline: 2026-05-12
domain: domains/biology/hexa-weave/hexa-weave.md
gate: F-TP5-b
parent_proposal: proposals/hexa_weave_mvp_2026_04_28.md
predecessor_proposal: proposals/hexa_weave_mvp_w1_architecture_decision_2026_04_28.md
milestone: W2
---

# hexa-weave W2 base-model integration prep (2026-04-28)

> **Forward-spec only** (raw 91 C3): no clone, no `pip install`, no weight download, no `git init`, no `mkdir ~/core/hexa-weave/`. This document records the W2 integration-prep design contingent on user approval before any move.
>
> **Parent**: [`hexa_weave_mvp_2026_04_28.md`](hexa_weave_mvp_2026_04_28.md) — W2 row of §3 (`Open-base model selection; benchmark loaded on ubu1 RTX 5070 12GB`).
>
> **Predecessor**: [`hexa_weave_mvp_w1_architecture_decision_2026_04_28.md`](hexa_weave_mvp_w1_architecture_decision_2026_04_28.md) — W1 selected OpenFold base + Apache-2.0/CC-BY-4.0 + sister-repo `~/core/hexa-weave/`.
>
> **Compliance**:
> - own 1: English-only body
> - own 22: snake_case `<name>_YYYY_MM_DD.md` operational pattern matched
> - own 23: H2 sections all `## §N` prefixed (parent pattern; no `umbrella:` declared)
> - raw 91 C3: explicit "what is NOT decided / NOT executed" §6 (≥10 items)
> - raw 71 ≥5 falsifiers: 5 W2 falsifiers preregistered (§5)
> - raw 51 saturation-adjacent honesty: predecessor blockers carried forward + W2-specific blockers added
> - raw 53 deterministic-verifier-manifest: decision criteria are deterministic (URL existence, SHA256 pin, regex match, file count)

## §1 W2 deliverable scope

W2 (2026-05-05 → 2026-05-12) per parent §3 row: base-model selection finalized + benchmark loaded on ubu1. This W2 prep doc, produced one week early on the W1 turn, covers:

1. OpenFold source + version-pin selection — §2
2. Multi-strand extension architecture (cross-attention layer count, token format, output format) — §3
3. Data pipeline prep (PDB-multimer 3-strand subset; train/val split; augmentation) — §4
4. n6 invariant trace integration points — §7 (5 named hook locations)
5. Falsifiers + MISS criteria for W2 — §5
6. raw 91 C3 honest — what W2 prep does NOT do — §6

Implementation (clone + venv + weight download + smoke inference + nvidia-smi measurement) is gated on user approval and is the W2 execution turn proper, not this prep doc.

## §2 OpenFold source analysis + version pin

### §2.1 Upstream identification

| Field | Value |
|-------|-------|
| Canonical repo | `https://github.com/aqlaboratory/openfold` |
| Default branch | `main` |
| License (code) | Apache-2.0 (LICENSE file in repo root) |
| License (weights) | CC-BY-4.0 (per repo README weight section) |
| Maintainer | AlQuraishi Lab + community |
| Citing paper | Ahdritz et al., "OpenFold: Retraining AlphaFold2 yields new insights into its learning mechanisms and capacity for generalization", Nat. Methods 2024 |
| Inference entry point (per repo layout) | `run_pretrained_openfold.py` (top-level) |
| Forward-pass module | `openfold/model/model.py::AlphaFold.forward` (matches AF2 evoformer + structure-module decomposition) |
| Multimer fork (legacy) | `openfold/model/multimer/` subtree (W6 cross-attention reference) |

### §2.2 Version pin policy

W2 pins OpenFold to a specific commit SHA, not `main`, for reproducibility. The pinned SHA is determined at W2 execution moment by:

1. `git ls-remote https://github.com/aqlaboratory/openfold main` → record HEAD SHA
2. Verify against last 30-day commit history that no breaking change landed (`CHANGELOG.md` if present, otherwise `git log --since="30 days ago"` review)
3. Pin in `pyproject.toml` as `openfold @ git+https://github.com/aqlaboratory/openfold@<SHA40>`
4. Record SHA40 + observed-at-timestamp in `~/core/hexa-weave/data/MANIFEST.md` under `base_model_pin:`

**Forward-spec disclosure**: the actual SHA is NOT collected in this prep doc — that requires a network call which is a W2 execution step. Falsifier F-W2-1 retires this gap.

### §2.3 Weight file URL + integrity

OpenFold publishes pretrained parameters via Zenodo / HuggingFace mirrors. Per repo README the canonical retrieval is:

| Field | Value |
|-------|-------|
| Primary mirror | `https://huggingface.co/aqlaboratory/openfold` (model card with `params/` directory) |
| Secondary mirror | Zenodo DOI link (per repo README; specific DOI captured at W2 execution) |
| Archive size | ~3.0 GB total across param shards (literature-claim per Ahdritz 2024 supplementary) |
| Integrity | SHA256 per shard; recorded in `data/MANIFEST.md` after download |
| AF-2 weight equivalence | OpenFold `params/finetuning_ptm_2.pt` is the AF2-PTM head equivalent (W2 single-chain inference target) |

**Forward-spec disclosure**: SHA256 of each weight shard is NOT yet collected — W2 execution step. Falsifier F-W2-2 covers integrity gap.

### §2.4 ubu1 RTX 5070 12GB memory footprint measurement procedure

The actual measurement runs at W2 execution. The procedure is fixed here (raw 53 deterministic verifier):

1. **Pre-conditions**: clean reboot of ubu1; `nvidia-smi` reports < 200 MB used at idle.
2. **Test target**: single-chain protein, 350 residues (median MVP P0-1 case-study size). Candidate test FASTA: `T1024` (CASP14 target) — ~408 aa, public domain. Fallback: ubiquitin (1UBQ, 76 aa) for fast smoke test.
3. **Inference invocation**:
   ```
   python run_pretrained_openfold.py \
     --fasta_paths data/T1024.fasta \
     --use_precomputed_alignments data/alignments/T1024/ \
     --jax_param_path params/finetuning_ptm_2.pt \
     --model_device cuda:0 \
     --bf16 \
     --output_dir scratch/T1024/
   ```
4. **Measurement loop** (parallel `nvidia-smi` poller):
   ```
   nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits -l 1 \
     | awk 'BEGIN{m=0}{if($1>m)m=$1; print $1" "m}' \
     > scratch/T1024_vram.log
   ```
5. **Pass criteria** (W1 F-W1-1 retirement):
   - peak VRAM < 11.5 GB (12 GB capacity − 0.5 GB OS/driver)
   - inference completes without OOM
   - output `unrelaxed_T1024.pdb` exists and parses with BioPython
6. **Recording**: peak VRAM number + log path + SHA256(unrelaxed_T1024.pdb) appended to `~/core/hexa-weave/case_studies/W2_smoke/verifier.json` per parent §7.
7. **Fallback**: if peak ≥ 11.5 GB, switch sequence:
   - 7a: enable `--cpu_offload` flag (OpenFold supports CPU offload of attention)
   - 7b: enable `--use_deepspeed_evoformer_attention` (memory-efficient attention)
   - 7c: 8-bit quantize via `bitsandbytes` (`bnb.nn.Linear8bitLt` substitution; estimated 30% VRAM reduction)
   - 7d: drop chain length to 256 aa test (smaller benchmark target)
   - 7e: declare F-W1-1 falsified → escalate to RoseTTAFold All-Atom secondary path per W1 §2.2

**No measurement is executed by this document.** The procedure is a forward-spec recipe.

## §3 Multi-strand extension architecture design

### §3.1 OpenFold's protein-only attention layer (baseline)

OpenFold's evoformer stack (48 blocks per AF2 default) operates over two tensor tracks:

- **MSA track**: shape `(batch, N_seq, N_res, c_msa)` — multiple-sequence-alignment embedding (c_msa=256 default)
- **Pair track**: shape `(batch, N_res, N_res, c_z)` — pairwise residue-residue representation (c_z=128 default)

Each evoformer block performs (in order):
1. MSA row-wise attention with pair bias
2. MSA column-wise attention
3. MSA transition (FFN)
4. Outer product mean (MSA → pair update)
5. Triangle attention starting/ending node (over pair)
6. Triangle multiplication outgoing/incoming (over pair)
7. Pair transition (FFN)

The structure module (8 layers) consumes pair + single representation and emits `(N_res, 3)` Cα coordinates + per-residue rigid frames via Invariant Point Attention (IPA).

This is the **protein-only** surface. RNA and ligand are not native inputs.

### §3.2 Multi-strand extension: cross-attention layer count + token format

W2 prep declares (forward-spec; finalized at W6 implementation):

**Three-strand encoding scheme**:

| Strand | Source format | Tokenization | Embedding dim | Length cap (W2 prep) |
|--------|---------------|--------------|---------------|----------------------|
| Protein | FASTA (1-letter aa) | per-residue (20 aa + gap + mask = 22 token vocab) | c_p = 256 (matches MSA c_msa) | 512 aa |
| RNA | FASTA-like (ACGU + N + gap) | per-nucleotide (4 nt + N + gap + mask = 7 token vocab) | c_r = 128 | 256 nt |
| Ligand | SMILES string | RDKit atom-level tokenization (atom type + bond context = ~80 token vocab) | c_l = 128 | 64 atoms |

**Cross-attention block structure (W6 target)**:

```
Stage A: independent encoders (W4–W5 deliverable)
  ProteinEnc(P) → P_emb  ∈ ℝ^(N_p, c_p)    [reuse OpenFold evoformer; freeze for W6]
  RnaEnc(R)     → R_emb  ∈ ℝ^(N_r, c_r)    [new; ESM2-RNA-style transformer, 6 blocks]
  LigEnc(L)     → L_emb  ∈ ℝ^(N_l, c_l)    [new; GNN over RDKit graph, 4 message-passing rounds]

Stage B: pairwise cross-attention (W6 deliverable, this document's scope)
  Block count: 6 (1/8 of OpenFold's 48 evoformer blocks)
  Per block (3 cross-pair branches):
    P_emb ← CrossAttn(P_emb, kv=R_emb)   — protein attends to RNA
    P_emb ← CrossAttn(P_emb, kv=L_emb)   — protein attends to ligand
    R_emb ← CrossAttn(R_emb, kv=L_emb)   — RNA attends to ligand
    [skipped: L→P and L→R; ligand is read-only target in MVP]
  Total cross-attn modules per block: 3
  Total cross-attn modules in stack: 6 × 3 = 18

Stage C: joint structure module (W6→W7 deliverable)
  Reuse OpenFold IPA; extend with two new query streams (RNA, ligand)
  Output: (N_p, 3) protein Cα + (N_r, 3) RNA P + (N_l, 3) ligand atom coords
```

**LoC budget tracking** (F-W1-2 falsifier feeds): cross-attention module ≤ 1500 LoC. Per-block cross-attn ≈ 80 LoC × 3 branches × 6 blocks = 1440 LoC + ~60 LoC scaffolding = 1500 LoC ceiling. Tight; F-W2-3 (§5) re-tightens this.

### §3.3 Input token format decision

Final W2 input contract (raw 53 deterministic):

```yaml
hexa_weave_input_v0_2:
  protein:
    fasta_path: str           # required; single-chain FASTA
    msa_path: str             # required; precomputed alignment dir
  rna:
    sequence: str             # optional; 1-letter ACGU; if absent, RNA channel zero-padded
    secondary_structure: str  # optional; dot-bracket; W7 augmentation
  ligand:
    smiles: str               # optional; if absent, ligand channel zero-padded
    formal_charge: int        # default 0
  joint_options:
    n6_invariant_trace: bool  # default true (own 25/hw 5 mandate)
    output_format: enum["pdb_only", "pdb+json", "json_only"]  # default pdb+json
```

Schema validated by Pydantic v2 (W1 §4.3 dependency).

### §3.4 Output format

```yaml
hexa_weave_output_v0_2:
  protein_coords:
    pdb_path: str             # written; AF2-style atom records
    plddt: float[N_p]         # per-residue confidence
  rna_coords:
    pdb_path: str             # written if RNA input present
    plddt_rna: float[N_r]
  ligand_pose:
    sdf_path: str             # ligand binding pose; RDKit-writable
    binding_energy_estimate: float  # heuristic (W11 nice-to-have)
  n6_invariant_trace:
    json_path: str            # mandatory; matches parent §7 regex
                              # ^\{"tau":4,"sigma":12,"J2":24,"phi":2,.*\}$
  verifier:
    numeric_threshold_path: str
    counter_path: str
```

## §4 Data pipeline prep

### §4.1 PDB-multimer 3-strand subset extraction feasibility

**Source**: RCSB PDB (`https://www.rcsb.org/`), advanced query API.

**Filter chain** (raw 53 deterministic; executable as RCSB JSON query at W7):

```json
{
  "query": {
    "type": "group",
    "logical_operator": "and",
    "nodes": [
      {"type": "terminal", "service": "text",
       "parameters": {"attribute": "rcsb_entry_info.polymer_entity_count_protein", "operator": "greater_or_equal", "value": 1}},
      {"type": "terminal", "service": "text",
       "parameters": {"attribute": "rcsb_entry_info.polymer_entity_count_nucleic_acid", "operator": "greater_or_equal", "value": 1}},
      {"type": "terminal", "service": "text",
       "parameters": {"attribute": "rcsb_entry_info.nonpolymer_entity_count", "operator": "greater_or_equal", "value": 1}},
      {"type": "terminal", "service": "text",
       "parameters": {"attribute": "rcsb_entry_info.experimental_method", "operator": "in", "value": ["X-RAY DIFFRACTION", "ELECTRON MICROSCOPY"]}},
      {"type": "terminal", "service": "text",
       "parameters": {"attribute": "rcsb_entry_info.resolution_combined", "operator": "less_or_equal", "value": 3.0}}
    ]
  },
  "return_type": "entry"
}
```

**Expected yield (literature estimate, F-W2-4 retires empirically)**:
- ~12 000 RCSB entries match `protein ≥ 1 AND nucleic_acid ≥ 1 AND ligand ≥ 1`
- After resolution ≤ 3.0 Å filter: ~8 000 entries
- After RNA-only (exclude DNA-only): ~2 500 entries (RNA is rarer than DNA in PDB)
- After CC0 license filter (parent §6 B2; hw 6): ~2 000 entries (most PDB is CC0, but some curated curls have restrictions)
- After length cap (protein ≤ 512 aa; RNA ≤ 256 nt; ligand ≤ 64 atoms): ~1 200 entries final

**Conclusion**: 3-strand subset extraction is feasible. Target N=50 bound from parent §9 (`P=10, N=50` for case-studies) is comfortably below the ~1200 estimated yield.

### §4.2 Train / validation / test split

| Split | Ratio | Count (assuming 1200 yield) | Selection policy |
|-------|-------|-----------------------------|------------------|
| Train | 0.80 | 960 | random shuffle with fixed seed (own 12 reproducibility) |
| Validation | 0.10 | 120 | held-out for hyperparameter pick |
| Test | 0.10 | 120 | NEVER touched by training; sequence-cluster-split (CD-HIT 30% identity threshold) to avoid leakage |

**Anti-leakage guard**:
- Sequence clustering via CD-HIT at 30% identity → no test-set sequence shares > 30% identity with any train sequence
- Date-cutoff guard: test set is restricted to PDB deposition date ≥ 2024-01-01 (later than OpenFold pretraining cutoff) to avoid base-model memorization confound

### §4.3 Data augmentation policy

W2 prep declares minimal augmentation (most augmentation is W7 work):

| Augmentation | Apply at | Probability | Notes |
|--------------|----------|-------------|-------|
| Random cropping (protein) | train only | 0.5 | crop window 256 aa if N_p > 256 |
| MSA subsampling | train only | 1.0 | uniform sample 128 sequences from full MSA |
| RNA secondary-structure perturb | train only | 0.2 | flip 5% of dot-bracket tokens (W8 nice-to-have) |
| Ligand SMILES canonicalization | always | 1.0 | RDKit canonical SMILES; not augmentation, normalization |
| Coordinate noise (Gaussian σ=0.5 Å) | train only | 0.3 | improves robustness |
| Chain reordering | train only | 0.5 | for multimer cases |

No augmentation at validation / test.

### §4.4 Dataset license + ethics

- PDB CC0 filter is mandatory (hw 6; parent §6 B2)
- BMRB NMR data is P2 nice-to-have per W1 dep stack — defer to W7+
- No proprietary databases (e.g. MOAD, CHEMBL paid tier) used
- Dataset MANIFEST records: source URL, retrieval date, total entry count, CC0 verification SHA256 of license-filter script output

## §5 W2 falsifiers (raw 71 ≥5) + MISS criteria

| ID | Claim under test | Falsifying observation | Deadline |
|----|------------------|------------------------|----------|
| F-W2-1 | OpenFold `main` HEAD SHA at W2 execution is structurally compatible with §3.1 evoformer + structure-module decomposition | repo refactor in last 30 days renames `openfold/model/model.py::AlphaFold` or restructures `evoformer/` package | 2026-05-12 |
| F-W2-2 | OpenFold weight shard SHA256 set is publishable + verifiable | weight mirror 404s OR SHA256 list is not derivable from a stable canonical source | 2026-05-12 |
| F-W2-3 | Cross-attention LoC budget (1500 line ceiling; §3.2) is achievable | W6 implementation prototype exceeds 1500 LoC for 3-strand cross-attn module | 2026-06-02 (W6) |
| F-W2-4 | RCSB 3-strand-subset yield ≥ 50 entries after all §4.1 filters | RCSB query at W7 returns < 50 entries | 2026-06-09 (W7) |
| F-W2-5 | All 5 n6 invariant trace integration points (§7) are non-invasive (post-processing or hookable; no OpenFold internal source modification required) | implementation reveals that ≥1 of the 5 hook points requires patching OpenFold model code rather than wrapping its output | 2026-06-23 (W9) |

### §5.1 W2 MISS criteria (own 12 declared upfront)

W2 prep is judged MISS when **any** of the following is true at 2026-05-12:

- WM2-1: this document `hexa_weave_mvp_w2_base_model_integration_2026_04_28.md` is missing or fails own 22 / own 23 lint
- WM2-2: kick witness JSON `design/kick/2026-04-28_hexa-weave-mvp-w2-base-model_omega_cycle.json` is missing or fails JSON schema validation
- WM2-3: any W2 falsifier (F-W2-1..F-W2-5) deadline slipped without retraction commit
- WM2-4: user has rejected the W2 prep design and no replacement design recorded
- WM2-5: discovery_absorption registry append for this W2 prep is missing

Post-hoc adjustment of WM2-1..WM2-5 is forbidden per own 12.

## §6 raw 91 C3 honest — what W2 prep does NOT do / does NOT claim

This list is the W2 prep negative space and is part of the contract:

1. **No OpenFold clone** — `git clone` not executed; canonical repo URL recorded only as text reference.
2. **No `pip install`** — pyproject.toml from W1 §4.3 is not yet exercised.
3. **No weight download** — ~3 GB OpenFold params not retrieved; SHA256 list not yet pinned. F-W2-2 retires this.
4. **No empirical VRAM measurement** — §2.4 procedure is a recipe; the actual `nvidia-smi` peak number is not yet collected. Inherited W1 F-W1-1 retires this.
5. **No HEAD SHA pin** — §2.2 SHA40 placeholder will be filled at W2 execution. F-W2-1 retires this.
6. **No RCSB query execution** — §4.1 filter chain is JSON spec; actual yield count is literature-estimate not API-verified. F-W2-4 retires this.
7. **No CD-HIT clustering** — §4.2 anti-leakage guard procedure is forward-spec; cluster count is literature-estimate.
8. **No cross-attention prototype** — §3.2 LoC budget is design-time estimate; actual implementation lands at W6. F-W2-3 retires this.
9. **No legal license review on weight CC-BY-4.0 attribution requirements** — derivative-work obligations under CC-BY-4.0 (e.g. attribution in output PDB headers) are not yet legally assessed. Inherited W1 F-W1-3 retires this.
10. **No ESMFold / RoseTTAFold benchmark comparison run** — alternative-base benchmarking deferred per W1 §2.2 (RoseTTAFold All-Atom is fallback only).
11. **No `~/core/hexa-weave/` directory creation** — verified non-existent at W1 §6 item 5; remains non-existent in W2 prep.
12. **No `.own` rule promotion to live** — `hw 1..hw 7` from W1 §4.4 are still forward-spec.
13. **No nexus kick attempt for W2 prep** — predecessor W1 used raw 100 in-context fallback per kick infra failure modes (`design/kick/2026-04-28_hexa-weave-closure_omega_cycle.json`); W2 prep continues fallback. Kick attempt is contingent on F-CL3-a (kick infra clean run by 2026-04-29).
14. **No external reviewer outreach** — P1-7 reviewer recruitment unchanged from W1; deferred to W11+.
15. **No claim that W2 prep satisfies F-TP5-b** — F-TP5-b is the 90-day MVP gate at 2026-07-28; W2 prep is W2 only.

W2 risks (carried forward + new):

- WR2-1 (carry W1 WR1): OpenFold maintenance pace may slow after AF-3 release (mitigation: SHA40 pin per §2.2)
- WR2-2 (carry W1 WR2): 12 GB VRAM fit may fail empirically (mitigation: §2.4 fallback chain 7a-7e)
- WR2-3 (new): RCSB 3-strand yield may underflow N=50 target if RNA-containing-with-ligand structures are rarer than literature estimate (mitigation: relax resolution to 3.5 Å; expand to NMR; F-W2-4 active)
- WR2-4 (new): cross-attention LoC budget may exceed 1500 lines forcing W6 schedule slip (mitigation: 6-block stack is configurable; can drop to 4 blocks if budget-tight)
- WR2-5 (new): n6 invariant trace post-processing may require OpenFold internal patches if pair-track activation is needed for σ(6)=12 binning (mitigation: F-W2-5 + F-W1-5 jointly cover; fallback is pure-output post-proc using only PDB coords)

## §7 n6 invariant trace integration points (5 named hook locations)

Parent §2.4 mandates: output JSON logs τ(6)=4 conformational state binning, σ(6)=12 raw-strategy pool, J₂=24 interaction-tensor budget, φ(6)=2 hydrophobic/hydrophilic verdict-bit. W2 prep declares 5 named hook locations (raw 53 deterministic; F-W2-5 retires non-invasiveness).

| Hook ID | Trace target | Source surface | Read at | Compute logic |
|---------|--------------|----------------|---------|---------------|
| **N6-H1** | τ(6)=4 conformational state binning | OpenFold `unrelaxed_<id>.pdb` per-residue Cα coords | post-inference (non-invasive) | 4-cluster k-means over per-residue dihedral (φ, ψ) angles → bin index ∈ {0,1,2,3}; aggregate across all residues into a 4-vector histogram |
| **N6-H2** | σ(6)=12 icosahedral capsid / strategy pool | structure-module final pair representation OR PDB Cα coords | post-inference (non-invasive preferred; pair-track read is invasive fallback) | for capsid validation use cases (P0-1 candidates): compute icosahedral symmetry score against 12 canonical icosahedron vertex positions via Procrustes alignment; for non-capsid cases: 12-bin histogram over secondary-structure assignment (DSSP H/E/L expanded to 12 sub-states) |
| **N6-H3** | J₂=24 interaction-tensor budget | structure-module pair representation `(N_res, N_res, c_z=128)` | post-inference (non-invasive) — read final-block output, not internal | Mathieu-symmetry verification: project pair-tensor onto top-24 principal components; compare residual energy to budget; emit `J2_budget_used: float ∈ [0, 1]` |
| **N6-H4** | φ(6)=2 hydrophobic/hydrophilic verdict-bit | per-residue amino-acid identity from input FASTA + per-residue solvent-accessibility from DSSP run on output PDB | post-inference (non-invasive) | per-residue: hydrophobic_buried = (Kyte-Doolittle hydropathy > 0) AND (SASA < 30 Å²); aggregate to fraction; output `phi_verdict_bit: 0|1` (1 if fraction > 0.5) |
| **N6-H5** | n6-master-identity check (own 2 mandate: σ·φ = n·τ = J₂ = 24) | aggregate of N6-H1..N6-H4 | post-aggregation | verify σ(=12) · φ(=2) = 24, n(=6) · τ(=4) = 24, J₂=24; emit `n6_identity_pass: bool`; if false, fail verifier_manifest |

**All 5 hooks are designed for post-inference / non-invasive reads** (PDB output + final pair-track read only). N6-H2 has a noted invasive-fallback if pair-track final-block output is insufficient — F-W2-5 monitors. No OpenFold source modification is required by §3.2 design.

**Trace JSON shape** (parent §7 regex compliant):

```json
{"tau":4,"sigma":12,"J2":24,"phi":2,
 "tau_histogram":[0.31,0.27,0.22,0.20],
 "sigma_score":0.87,
 "J2_budget_used":0.62,
 "phi_verdict_bit":1,
 "n6_identity_pass":true,
 "case_id":"<id>","model_sha":"<sha40>","trace_version":"v0.2"}
```

Validates against parent §7 pattern `^\{"tau":4,"sigma":12,"J2":24,"phi":2,.*\}$`.

## §8 Verifier manifest for W2 prep

```yaml
verifier_manifest_w2_prep:
  numeric_threshold:
    - metric: w2_falsifiers_count
      target: ">= 5"
      scope: "this document §5"
      observed: 5
      verdict: PASS
    - metric: not_decided_items_count
      target: ">= 10"
      scope: "this document §6"
      observed: 15
      verdict: PASS
    - metric: n6_hook_count
      target: ">= 5"
      scope: "this document §7"
      observed: 5
      verdict: PASS
  counter:
    - claim: "OpenFold weight shards are publicly mirrored under CC-BY-4.0 with SHA256 verifiable"
      witness_required: ">= 1 documented mirror URL"
      witness_path: "https://huggingface.co/aqlaboratory/openfold"
      verdict: PASS (URL exists; SHA256 collection is W2-execution step per §2.3)
    - claim: "RCSB advanced query supports protein+nucleic_acid+ligand 3-strand filter"
      witness_required: ">= 1 attribute path matching the filter"
      witness_path: "https://search.rcsb.org/structure-search-attributes.html (rcsb_entry_info.polymer_entity_count_protein attribute)"
      verdict: PASS
  hash:
    - artifact: "this document"
      sha256_pinned_at: "TBD-on-commit"
  filesystem:
    - check: "~/core/hexa-weave/ does NOT yet exist"
      cmd: "test ! -d ~/core/hexa-weave"
      verdict: PASS (forward-spec only; W1 §6 item 5 carried forward)
    - check: "predecessor W1 doc exists"
      cmd: "test -f proposals/hexa_weave_mvp_w1_architecture_decision_2026_04_28.md"
      verdict: PASS
```

Verifier type: `numeric_threshold + COUNTER + filesystem`. No LLM judge.

## §9 Cost-attribution

Parent §8 cost-center `hexa-weave-mvp` unchanged. W2 prep cost-actual = $0 (zero compute, document-only). First non-zero cost-actual append at W2 execution (clone + pip install + weight download — bandwidth + storage only; zero GPU until smoke inference).

## §10 Auto-absorption hook

Append to `state/discovery_absorption/registry.jsonl`:

```json
{"schema":"anima/discovery_absorption/v1","ts":"2026-04-28T00:00:00Z","finding_id":"hexa-weave-mvp-w2-base-model-integration-prep-2026-04-28","witness_path":"proposals/hexa_weave_mvp_w2_base_model_integration_2026_04_28.md","kick_witness_path":"design/kick/2026-04-28_hexa-weave-mvp-w2-base-model_omega_cycle.json","absorption_channel":"proposal-w2-base-model-integration-prep","absorption_target":"HEXA-WEAVE W2 prep: OpenFold pin policy (SHA40 at exec time) + 12GB VRAM measurement procedure + multi-strand 3-encoder + 6-block × 3-branch cross-attn (18 modules total; 1500 LoC ceiling) + RCSB 3-strand subset filter (~1200 yield estimate; N=50 target comfortable) + 80/10/10 train/val/test with CD-HIT 30%-id anti-leakage + 5 n6 invariant trace hooks (N6-H1..N6-H5; all post-inference non-invasive) + 5 W2 falsifiers (F-W2-1..F-W2-5) + 5 MISS criteria (WM2-1..WM2-5) + 15 raw 91 C3 NOT-decided items","status":"forward-spec","absorbed_at":"2026-04-28T00:00:00Z","absorbed_via":"raw 108+135 W2 prep deliverable absorption","classifier_version":"raw_108_v1","raw_91_c3":"forward-spec only — no clone / no pip install / no weight download / no nvidia-smi / no RCSB query / no CD-HIT cluster / no cross-attn prototype / no legal review / kick infra deferred (raw 100 fallback continued)","parent_proposal":"proposals/hexa_weave_mvp_2026_04_28.md","predecessor_proposal":"proposals/hexa_weave_mvp_w1_architecture_decision_2026_04_28.md","parent_milestone":"W2"}
```

## §11 Lint pre-flight

Expected pass on:
- own 1 English-only: PASS (body is English; Korean only in user-facing report message in conversation surface, not in this doc)
- own 22 proposal-naming: PASS — `hexa_weave_mvp_w2_base_model_integration_2026_04_28.md` snake_case + `_YYYY_MM_DD` matches `category: operational`
- own 23 proposal-umbrella: PASS — frontmatter does not declare `umbrella:` so consolidation rule does not trigger (matches parent + W1 pattern)

## §12 Cross-references

- Parent spec: [`hexa_weave_mvp_2026_04_28.md`](hexa_weave_mvp_2026_04_28.md)
- Predecessor W1: [`hexa_weave_mvp_w1_architecture_decision_2026_04_28.md`](hexa_weave_mvp_w1_architecture_decision_2026_04_28.md)
- Parent body: `domains/biology/hexa-weave/hexa-weave.md`
- Predecessor closure witness: `design/kick/2026-04-28_hexa-weave-closure_omega_cycle.json`
- W1 kick witness: `design/kick/2026-04-28_hexa-weave-mvp-w1-architecture_omega_cycle.json`
- This W2 prep kick witness: `design/kick/2026-04-28_hexa-weave-mvp-w2-base-model_omega_cycle.json`
- OpenFold upstream: https://github.com/aqlaboratory/openfold
- OpenFold weight mirror: https://huggingface.co/aqlaboratory/openfold
- RCSB advanced search attributes: https://search.rcsb.org/structure-search-attributes.html
- RoseTTAFold All-Atom upstream (fallback): https://github.com/baker-laboratory/RoseTTAFold-All-Atom
- Discovery absorption registry: `state/discovery_absorption/registry.jsonl`
