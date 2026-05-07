---
category: operational
status: forward-spec
date: 2026-04-28
deadline: 2026-05-05
domain: domains/biology/hexa-weave/hexa-weave.md
gate: F-TP5-b
parent_proposal: proposals/hexa_weave_mvp_2026_04_28.md
milestone: W1
---

# hexa-weave W1 architecture decision (2026-04-28)

> **Forward-spec only** (raw 91 C3): no repo init / clone / dependency install has been executed. This document records the W1 architecture decision and is contingent on user approval before any implementation move.
>
> **Parent spec**: [`hexa_weave_mvp_2026_04_28.md`](hexa_weave_mvp_2026_04_28.md) — W1 row of §3 12-week milestone table.
>
> **Compliance**:
> - own 1: English-only body
> - own 22: snake_case `<name>_YYYY_MM_DD` operational pattern matched
> - own 23: H2 sections all `## §N` prefixed (parent spec pattern; umbrella not declared so umbrella consolidation rule does not trigger)
> - raw 91 C3: explicit "what is NOT decided" §6
> - raw 71 ≥5 falsifiers: 5 W1 falsifiers preregistered (§5)
> - raw 51 saturation-adjacent honesty: external blockers carried forward from parent §6 + W1-specific blockers added
> - raw 53 deterministic-verifier-manifest: decision criteria are deterministic (VRAM fit measurement, license SPDX check, repo path existence)

## §1 W1 deliverable scope

W1 (2026-04-28 to 2026-05-05) per parent §3 row: scope freeze + architecture decision + repo init stub. This document covers:

1. base-model decision (ESM3 vs OpenFold vs RoseTTAFold) — §2
2. repo location decision (Option A vs B vs C vs D) — §3
3. license decision — §4
4. dependency stack — §4
5. falsifiers + MISS criteria for W1 — §5
6. raw 91 C3 honest — what W1 does NOT decide — §6

Implementation (clone, env setup, weight download) is gated on user approval and is W2 work per parent §3.

## §2 Base model decision: **OpenFold (Apache-2.0)** primary, ESM3 fallback

### §2.1 Comparison matrix

| Axis | ESM3 | OpenFold | RoseTTAFold |
|------|------|----------|-------------|
| License | Cambrian Non-Commercial Community License (NOT OSI-approved; commercial restriction on ESM3 weights) | Apache-2.0 (code) + CC-BY-4.0 (weights) — fully open | BSD-3 + MIT (code), weight redistribution OK |
| VRAM (single-chain ~350 aa inference) | ESM3-small ~6 GB; ESM3-medium ~14 GB (exceeds 12 GB ubu1 RTX 5070) | OpenFold ~10 GB inference (BF16) for ~350 aa; AF2-equivalent | RoseTTAFold All-Atom ~14 GB (exceeds 12 GB) |
| Multi-strand extension | Native multi-modal (sequence + structure + function tokens) but write-side composition for novel multi-strand requires custom adapter | OpenFold Multimer fork + Uni-Fold Multimer demonstrate cross-attention extension paths; clean PyTorch codebase | RoseTTAFold All-Atom natively handles protein+DNA+RNA+ligand jointly (closest to MVP §2 P0-1) |
| Codebase quality | Closed-ish (ESM3 inference released, training code partial) | Fully open PyTorch reimplementation of AlphaFold2 (matches AF2 RMSD within 0.1 Å on CASP14) | Fully open; All-Atom variant (2024) is the published multi-modal baseline |
| AF-3 weight independence (P2-12) | Independent (ESM is a separate lineage from AF) | Independent (open AF2 reimplementation, no AF3 weights) | Independent (RF lineage, no AF3 weights) |
| ubu1 12 GB fit | Borderline (must use ESM3-small or quantize) | YES at BF16 inference | NO without quantization |
| Cross-attention modification difficulty | HIGH (closed weight format + license) | LOW (clean PyTorch modules; OpenFold Multimer fork pattern available) | MEDIUM (codebase open but more complex; All-Atom layer already does multi-strand, less room for custom extension) |
| Community + docs | Strong (Meta backing) | Strong (AlQuraishi lab + community) | Strong (Baker lab + RFAA paper) |

### §2.2 Decision: **OpenFold primary**, RoseTTAFold All-Atom secondary reference, ESM3 not selected

**Rationale**:

1. **License clean** (Apache-2.0): satisfies parent §6 B6 OpenFold/ESM3 weight licensing blocker. ESM3's Community License has commercial-use restrictions that would jam P1-7 external-reviewer demo if any reviewer is commercial.
2. **12 GB VRAM fit confirmed (literature)**: OpenFold inference at BF16 ~10 GB for 350-aa chain — fits ubu1 RTX 5070 12 GB with margin. Empirical fit verification is W2 work (raw 91 C3: not yet measured locally).
3. **Cross-attention modification surface**: OpenFold's PyTorch modules (`openfold/model/`) follow AF2 IPA + structure-module decomposition cleanly; the cross-attention layer for joint protein+RNA+ligand encoding (parent §3 W6) can be added by extending `EvoformerStack` with a third strand-token track. RoseTTAFold All-Atom already handles this jointly (advantage: less coding) but loses the "write-side composition" margin because the layer is fixed; OpenFold's emptier slate is better for MVP P0-3 differentiation from AF-3.
4. **AF-3 independence (P2-12)**: OpenFold has zero AF-3 weights by construction (AF2 reimplementation predates AF-3). Hash-compare for P2-12 verification trivially passes.
5. **Fallback path**: if OpenFold cross-attention extension exceeds W6 budget, switch to RoseTTAFold All-Atom for "borrow joint encoder, replace prediction head" approach. ESM3 is rejected as fallback because of license + write-side surface mismatch.

### §2.3 Honest C3 limits on §2 decision

- VRAM fit is **literature-claimed not measured**; raw 91 C3. W2 must run an actual `nvidia-smi` measurement on ubu1 with a 350-aa test inference. Falsifier F-W1-1 (§5).
- ESM3 license has reportedly relaxed in some channel updates (community version vs research version); W1 decision uses the **most restrictive interpretation** to avoid commercial reviewer block. F-W1-3 falsifier monitors for license-relaxation evidence that would re-open ESM3 candidacy.
- "Cross-attention modification difficulty" is a qualitative coding judgment; no concrete LoC estimate has been validated. F-W1-4 falsifier triggers if W6 cross-attention layer exceeds 1500 LoC (3x typical AF2 module size).

## §3 Repo location decision: **Option A — `~/core/hexa-weave/` sister repo**

### §3.1 Option comparison

| Option | Path | Pro | Con |
|--------|------|-----|-----|
| **A** | `~/core/hexa-weave/` (new sister) | clean separation; no own/raw rule pollution; matches parent spec's `core/hexa-weave/` references in §3 W1/W2 rows | requires new repo + .own/CLAUDE.md scaffold + CI integration |
| B | `canon/experiments/hexa-weave/` | reuses existing repo + own gates | **violates own 5 theory-report-separation** (experiments/ is for time-stamped results, not for live ML pipeline code) — disqualifying |
| C | `~/core/anima/<sub-domain>/` | anima already has anima-physics, anima-cpgd-research with research-pipeline patterns | anima is consciousness/physics-focused; hexa-weave is biology/ML; thematic mismatch + risks anima's own-rule scope creep |
| D | `~/core/nexus/labs/hexa-weave/` | nexus has lab pattern conceptually | `nexus/labs/` does not exist (verified by `ls /Users/ghost/core/nexus/`); nexus is engine/dispatch infra, not lab incubator |

### §3.2 Decision: **Option A — `~/core/hexa-weave/` (new sister repo)**

**Rationale**:

1. **Parent spec already references `core/hexa-weave/`** (parent §3 W1 deliverable text, parent §7 verifier_manifest path `core/hexa-weave/case_studies/<id>/af3_diff.json`). Option A is consistent with the spec contract; B/C/D would require parent spec amendment.
2. **own 5 violation blocks Option B**: `experiments/` is project-local for time-stamped artifacts (per own 5 scope text). Hosting a 12-week live ML pipeline there would violate the theory-report separation gate.
3. **Option D path doesn't exist**: `~/core/nexus/labs/` was hypothesized but `ls` confirms no such directory. Creating it would extend nexus's footprint into a new responsibility (lab incubation) that nexus's current scope (engine/dispatch/discovery) doesn't claim.
4. **Option C thematic mismatch**: anima's existing sub-repos (anima-physics, anima-cpgd-research, anima-eeg, anima-hexad, etc.) are consciousness/physics/EEG-themed. Adding a protein-folding ML pipeline would break anima's umbrella coherence.
5. **Sister repo isolation**: hexa-weave has its own dependency stack (PyTorch, BioPython, OpenFold), CI cadence, and dataset weight (~50 GB PDB-multimer subset). Sister-repo isolation prevents these from polluting canon's repo size or CI.

### §3.3 Repo init plan (W1 mock-up only — NOT executed)

```
~/core/hexa-weave/
├── README.md                  # raw 91 C3 honest from day-1; declares MVP NOT-claims (parent §9)
├── LICENSE                    # Apache-2.0 (§4 decision)
├── .own                       # 6 rules carried forward + 3 hexa-weave-specific (§4.4)
├── pyproject.toml             # Python 3.11 + pinned deps (§4.3)
├── src/hexa_weave/
│   ├── __init__.py
│   ├── encoders/              # protein / RNA / ligand encoder stubs (W4-W5)
│   ├── cross_attention/       # joint embedding cross-attn (W6)
│   ├── n6_invariant/          # τ(6)=4, σ(6)=12, J₂=24, φ(6)=2 trace emitter
│   └── verifier/              # numeric_threshold + COUNTER per parent §7
├── case_studies/              # parent §7 verifier_manifest path
├── tests/
├── notebooks/                 # exploratory only; not authoritative
├── data/                      # gitignore'd; manifest in data/MANIFEST.md
└── .github/workflows/
    └── ci.yml                 # lint + test + verifier-dry-run
```

User approval required before `mkdir ~/core/hexa-weave/` executes.

## §4 License + dependency stack

### §4.1 License decision: **Apache-2.0**

**Rationale**:

1. **Compatibility with OpenFold**: OpenFold base is Apache-2.0; downstream MIT or BSD-3 is fine but Apache-2.0 retains the patent-grant clause that OpenFold inherits.
2. **Reviewer accessibility (P1-7)**: Apache-2.0 is OSI-approved + commercial-friendly; external reviewers (parent §6 B3) face zero license friction.
3. **MIT alternative rejected**: MIT lacks explicit patent grant; given protein-folding patent landscape (DeepMind AF-3 patents pending), Apache-2.0's defensive patent clause is materially safer.
4. **Proprietary rejected**: violates parent §1 "open-source license" P0 implicit + parent §9 NOT-list item 7 "no closed-source reuse".

### §4.2 Honest C3 on license decision

- Apache-2.0 + CC-BY-4.0 (OpenFold weights) is the working assumption; raw 91 C3 — legal review by counsel has NOT been performed. Falsifier F-W1-3 (§5) covers license-validity surprise.
- PDB data licensing (parent §6 B2) is a separate dimension — most PDB entries are CC0 but a minority have curated restrictions. Dataset filter at W7 must enforce CC0-only per parent §6 B2 mitigation.

### §4.3 Dependency stack

```toml
# pyproject.toml (forward-spec; not yet executed)
[project]
name = "hexa-weave"
version = "0.0.1-w1"
requires-python = ">=3.11,<3.13"
dependencies = [
  "torch==2.5.1+cu124",          # PyTorch primary (JAX rejected — OpenFold is PyTorch)
  "openfold @ git+https://github.com/aqlaboratory/openfold@main",  # base model
  "biopython>=1.83",             # FASTA / PDB parsing
  "biotite>=0.40",               # structure-aware ops, RNA support
  "rdkit>=2024.3",               # ligand SMILES + small-molecule handling
  "numpy>=1.26,<2.0",            # OpenFold compatibility pin
  "scipy>=1.13",
  "pyyaml>=6.0",                 # verifier_manifest.yaml parsing
  "pydantic>=2.7",               # n6 invariant trace schema
  "pytest>=8.0",                 # tests
]

[project.optional-dependencies]
dev = ["ruff", "mypy", "pre-commit"]
gpu-quant = ["bitsandbytes>=0.43"]  # fallback if 12 GB VRAM tight
```

**Key rejections**:
- **JAX**: rejected because OpenFold canonical impl is PyTorch; JAX would force a re-implementation cost we cannot afford in 12 weeks.
- **AF2/AF3 official weights**: rejected per parent §9 NOT-list item 3 ("no AF-3 weight reuse").
- **HuggingFace ESMFold**: rejected for now — overlaps with ESM3 license concerns; OpenFold standalone is cleaner.

### §4.4 .own rules carried forward + hexa-weave-local

The new sister repo inherits the principle but not the literal rule-IDs. Proposed `~/core/hexa-weave/.own` rules (forward-spec):

1. `hw 1`: doc-english-required (mirror own 1)
2. `hw 2`: license-spdx-declared (every source file has SPDX-License-Identifier: Apache-2.0 header)
3. `hw 3`: af3-weight-hash-ban (CI checks no file matches AF-3 weight SHA256; P2-12 enforcement)
4. `hw 4`: verifier-numeric-threshold-required (every case-study run emits a numeric_threshold + COUNTER pair per parent §7)
5. `hw 5`: n6-invariant-trace-required (output JSON validates against `^\\{"tau":4,"sigma":12,"J2":24,"phi":2,.*\\}$` per parent §7 regex)
6. `hw 6`: pdb-cc0-only (dataset filter enforces CC0-licensed PDB entries; parent §6 B2)
7. `hw 7`: vram-budget-12gb (CI gate: model.parameters() * dtype-size + activation estimate < 11 GB to leave 1 GB margin)

These are W1 forward-spec; rule IDs are placeholders. Final IDs assigned at W2 repo init.

## §5 Falsifiers (raw 71 ≥5 W1 deliverable) + MISS criteria

| ID | Claim under test | Falsifying observation | Deadline |
|----|------------------|------------------------|----------|
| F-W1-1 | OpenFold inference fits 12 GB VRAM on RTX 5070 for 350-aa chain at BF16 | empirical `nvidia-smi` measurement on ubu1 reports peak > 11.5 GB during single-chain inference | 2026-05-05 (W2 entry) |
| F-W1-2 | OpenFold cross-attention layer extension is feasible within W6 budget | LoC estimate for joint protein+RNA+ligand cross-attn module exceeds 1500 lines (3x AF2 evoformer block) | 2026-06-02 (W6) |
| F-W1-3 | Apache-2.0 + CC-BY-4.0 licensing is clean for commercial-reviewer use | OSI / SPDX / counsel review surfaces a patent or copyright restriction blocking P1-7 external reviewer access | 2026-05-19 (W4) |
| F-W1-4 | sister repo `~/core/hexa-weave/` is the right home (parent spec consistent) | parent spec amendment forced because external constraint (e.g. user directive, license geofencing) requires moving the repo | 2026-05-05 (W2 entry) |
| F-W1-5 | n6 invariant trace schema (`^\\{"tau":4,"sigma":12,"J2":24,"phi":2,.*\\}$`) is generatable from OpenFold output post-processing | extraction of τ/σ/J₂/φ anchor points from OpenFold inference output requires modification of OpenFold internals (not just post-processing) | 2026-06-23 (W9) |

### §5.1 W1 MISS criteria (own 12 declared upfront)

W1 is judged MISS when **any** of the following is true at 2026-05-05:

- WM1: this document `hexa_weave_mvp_w1_architecture_decision_2026_04_28.md` is missing or fails own 22 / own 23 lint
- WM2: kick witness JSON `design/kick/2026-04-28_hexa-weave-mvp-w1-architecture_omega_cycle.json` is missing or fails JSON schema validation
- WM3: any W1 falsifier (F-W1-1..F-W1-5) deadline has slipped without a retraction commit
- WM4: user has rejected the architecture decision and no replacement decision is recorded
- WM5: discovery_absorption registry append for this W1 decision is missing

Post-hoc adjustment of WM1..WM5 is forbidden per own 12.

## §6 raw 91 C3 honest — what W1 does NOT decide / does NOT do

This list is the W1 negative space and is part of the contract:

1. **No code execution** — no clone, no `pip install`, no `git init`. All §3 init plan steps are mock-up only; user approval gates W2 execution.
2. **No empirical VRAM measurement** — §2 12 GB fit is literature-claim only. F-W1-1 retires this.
3. **No legal license review** — §4 Apache-2.0 + CC-BY-4.0 is forward assumption. F-W1-3 retires this.
4. **No multi-strand benchmark** — RoseTTAFold All-Atom vs OpenFold-extended performance comparison is W7-W11 work, not W1.
5. **No actual `~/core/hexa-weave/` directory** — verified non-existent; will be created only after user approval.
6. **No `.own` rule promotion** — `hw 1..hw 7` are forward-spec; promoted to live at W2 repo init.
7. **No hash-compare baseline** — P2-12 AF-3 weight ban is declared (`hw 3`) but actual AF-3 release SHA256 list is gathered at W2.
8. **No external reviewer outreach** — P1-7 reviewer recruitment uses parent §6 B3 channel, not started in W1.
9. **No cost ledger entry yet** — parent §8 ledger gets the first append only when W2 execution begins.
10. **No JAX-vs-PyTorch benchmark** — JAX rejection is qualitative (OpenFold canonical is PyTorch), not benchmarked.
11. **No nexus kick attempt for W1** — predecessor cycles showed kick infra exhibited 3 orthogonal failure modes (OAuth, slot, container-no-node) per `2026-04-28_hexa-weave-closure_omega_cycle.json`. W1 witness JSON is in-context synthesis per raw 100 fallback; nexus kick will be attempted at W2 entry only if at least one prior kick has succeeded by 2026-04-29 (per closure witness F-CL3-a).
12. **No claim that W1 satisfies F-TP5-b** — F-TP5-b is the 90-day MVP gate at 2026-07-28. W1 is W1 only; mistaking W1 closure for F-TP5-b closure is a category error.

W1 risks (carried forward + new):

- WR1: OpenFold maintenance pace may slow after AF-3 release (mitigation: pin OpenFold to verified commit hash at W2)
- WR2: 12 GB VRAM fit may fail empirically (mitigation: bitsandbytes 8-bit fallback + htz 124 GB CPU per parent §6 B1)
- WR3: license-relaxation evidence for ESM3 may emerge mid-MVP (mitigation: F-W1-3 active; can re-open §2 candidate matrix)
- WR4: sister-repo CI overhead may delay W2-W3 (mitigation: minimal CI at W2; expand at W8 once first training run lands)
- WR5: user may request a different license (e.g. MIT) at approval time (mitigation: §4.1 alternatives matrix is non-blocking; switch to MIT requires only header rewrite)

## §7 Verifier manifest for W1

```yaml
verifier_manifest_w1:
  numeric_threshold:
    - metric: w1_falsifiers_count
      target: ">= 5"
      scope: "this document §5"
      observed: 5
      verdict: PASS
    - metric: not_decided_items_count
      target: ">= 10"
      scope: "this document §6"
      observed: 12
      verdict: PASS
  counter:
    - claim: "Apache-2.0 + CC-BY-4.0 stack is a viable hexa-weave license"
      witness_required: ">= 1 documented OpenFold-Apache-2.0 + CC-BY-4.0 production reference"
      witness_path: "https://github.com/aqlaboratory/openfold/blob/main/LICENSE"
      verdict: PASS
  hash:
    - artifact: "this document"
      sha256_pinned_at: "TBD-on-commit"
  filesystem:
    - check: "~/core/hexa-weave/ does NOT yet exist"
      cmd: "test ! -d ~/core/hexa-weave"
      verdict: PASS (forward-spec only)
```

Verifier type: `numeric_threshold + COUNTER + filesystem`. No LLM judge.

## §8 Cost-attribution carry-forward

Parent §8 cost-center `hexa-weave-mvp` is unchanged. W1 cost-actual = $0 (zero compute, document-only). First cost-actual append at W2 with venv build + OpenFold checkout.

## §9 Auto-absorption hook

Append to `state/discovery_absorption/registry.jsonl`:

```json
{"schema":"anima/discovery_absorption/v1","ts":"2026-04-28T00:00:00Z","finding_id":"hexa-weave-mvp-w1-architecture-decision-2026-04-28","witness_path":"proposals/hexa_weave_mvp_w1_architecture_decision_2026_04_28.md","kick_witness_path":"design/kick/2026-04-28_hexa-weave-mvp-w1-architecture_omega_cycle.json","absorption_channel":"proposal-w1-architecture-decision","absorption_target":"HEXA-WEAVE W1 architecture decision: base=OpenFold (Apache-2.0); repo=~/core/hexa-weave/ Option A new sister; license=Apache-2.0 + CC-BY-4.0 weights; deps=PyTorch 2.5+OpenFold+BioPython+Biotite+RDKit; 5 W1 falsifiers F-W1-1..F-W1-5; 5 MISS criteria WM1..WM5; raw 91 C3 with 12 NOT-decided items","status":"forward-spec","absorbed_at":"2026-04-28T00:00:00Z","absorbed_via":"raw 108+135 W1 deliverable absorption","classifier_version":"raw_108_v1","raw_91_c3":"forward-spec only — no repo init / no code execution / no empirical VRAM measurement / no legal license review","parent_proposal":"proposals/hexa_weave_mvp_2026_04_28.md","parent_milestone":"W1"}
```

## §10 Lint pre-flight

Expected pass on:
- own 1 English-only: PASS (this document is English; Korean only in user-facing report message, not in body)
- own 22 proposal-naming: PASS — `hexa_weave_mvp_w1_architecture_decision_2026_04_28.md` snake_case + `_YYYY_MM_DD` matches `category: operational`
- own 23 proposal-umbrella: PASS — frontmatter does not declare `umbrella:` so consolidation rule does not trigger (matches parent spec pattern)

## §11 Cross-references

- Parent spec: [`hexa_weave_mvp_2026_04_28.md`](hexa_weave_mvp_2026_04_28.md)
- Parent body: `domains/biology/hexa-weave/hexa-weave.md`
- Predecessor closure witness: `design/kick/2026-04-28_hexa-weave-closure_omega_cycle.json`
- This W1 kick witness: `design/kick/2026-04-28_hexa-weave-mvp-w1-architecture_omega_cycle.json`
- OpenFold upstream: https://github.com/aqlaboratory/openfold
- RoseTTAFold All-Atom upstream: https://github.com/baker-laboratory/RoseTTAFold-All-Atom
- ESM3 upstream: https://github.com/evolutionaryscale/esm
- Discovery absorption registry: `state/discovery_absorption/registry.jsonl`
