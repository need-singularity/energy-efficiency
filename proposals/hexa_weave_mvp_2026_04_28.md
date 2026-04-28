---
category: operational
status: forward-spec
date: 2026-04-28
deadline: 2026-07-28
domain: domains/biology/hexa-weave/hexa-weave.md
gate: F-TP5-b
---

# HEXA-WEAVE 90-day MVP spec — F-TP5-b gate (2026-04-28 to 2026-07-28)

> **Forward-spec only** (raw 91 C3): this document declares MISS criteria, falsifiers, verifier manifest, cost-center, and external blockers UPFRONT. No implementation work has started. The spec is a contract; the run that follows must conform or retract.
>
> **Parent domain body**: [`../domains/biology/hexa-weave/hexa-weave.md`](../domains/biology/hexa-weave/hexa-weave.md) — single canonical body per own 3. This proposal is an operational sub-doc and lives under `proposals/` per own 22 (snake_case operational + `_YYYY_MM_DD` date suffix).
>
> **Compliance**:
> - own 1 (English-only): English-only body
> - own 3 (one-doc-per-domain): no extra .md placed inside `domains/biology/hexa-weave/` — spec lives in `proposals/`
> - own 22 (proposal-naming): `hexa_weave_mvp_2026_04_28.md` matches snake_case `<name>_YYYY_MM_DD` operational pattern
> - own 23 (proposal-umbrella): single H2 first-word umbrella `hexa-weave`
> - raw 11 (bt-solution-claim-ban): no Clay Millennium 7 solution claim
> - raw 12 (miss-criteria-declared): MISS criteria pre-declared (see §5)
> - raw 51 (saturation-adjacent honesty): external blockers listed (see §6)
> - raw 53 (deterministic-verifier-manifest): verifier-type schema declared (see §7)
> - raw 71 (≥5 falsifiers TRANSCEND-tier): 7 falsifiers preregistered (see §4)
> - raw 86 (cost-attribution forward-spec): cost-center declared (see §8)
> - raw 91 (C3 honest forward-spec): risk list + what MVP does NOT do (see §9)
> - raw 9 (hexa-only): NOT applicable to ML pipeline — Python/PyTorch standard stack permitted

## §1 Scope and positioning

The MVP exists to satisfy the F-TP5-b 90-day gate registered in `domains/biology/hexa-weave/hexa-weave.md` §10 and §12. Closure verdict for the parent domain is currently TRANSCEND-CLOSURE-ALL with C3 caveats (theoretical-analytical, not empirical). This MVP bridges theory to empirical demonstration by exhibiting at least one L4 to L5 multi-molecule weave that AlphaFold 3 cannot produce.

WEAVE = multi-strand composition (Korean: gadak jjagi, "strand weaving") — write-side; FOLD = single-protein prediction — read-side. The MVP must demonstrate the **write-side composition** behaviour, not improved prediction accuracy.

## §2 Must / Should / Nice (P0 / P1 / P2) — count 5 / 4 / 3

### P0 must-have (5)

1. **Multi-strand input**: pipeline accepts ≥3 molecule types simultaneously (e.g. protein + RNA + small ligand).
2. **Joint structure prediction**: outputs 3D coordinates for all input strands plus their pairwise interactions.
3. **Differentiation from AF-3**: MVP performs **write-side composition** (generative design), not just prediction over a fixed input set.
4. **n6 invariant trace**: output JSON logs τ(6)=4 conformational state binning, σ(6)=12 raw-strategy pool, J₂=24 interaction-tensor budget, φ(6)=2 hydrophobic/hydrophilic verdict-bit per L4 mapping.
5. **Case-study witness**: ≥1 documented case where HEXA-WEAVE produces a valid joint multi-strand prediction that AF-3 cannot (e.g. AF-3 predicts protein only, ignores custom RNA + ligand context).

### P1 should-have (4)

6. **AdS/CFT cosmological reference**: explicit link to L6 PHYSICAL closure construction in parent body §6 (raw 91 C3 honest — no claim of physical equivalence, only structural reference).
7. **External-reviewer demo**: web demo or CLI accessible to ≥1 external reviewer.
8. **Reproducibility manifest**: dataset list + run script + verifier-manifest per raw 53 (numeric_threshold + COUNTER schema).
9. **Honest README**: declare what MVP does NOT do (no clinical validity, no production drug design, no AF-3 weight reuse, no mechanistic correctness claim).

### P2 nice-to-have (3)

10. **PDB-multimer benchmark**: comparison vs AF-3 on PDB-multimer subset.
11. **n6 invariant fitting test**: empirical check whether τ(6)=4 conformational binning improves prediction RMSD vs free-conformation baseline.
12. **Independence claim**: MVP codebase contains zero AF-3 model weights (verified by hash-compare against published AF-3 release).

## §3 12-week milestone table (W1 through W12)

| Week | Milestone | Deliverable | Gate-relevance |
|------|-----------|-------------|----------------|
| W1 (2026-04-28) | Architecture decision + repo init | `core/hexa-weave/` stub repo, RFC for ESM3 vs OpenFold base | scope freeze |
| W2 (2026-05-05) | Open-base model selection | base-model decision recorded; benchmark loaded on ubu1 RTX 5070 12GB | P0-2 prep |
| W3 (2026-05-12) | Base model integration | ESM3 or OpenFold loads + runs single-chain inference on ubu1 | P0-2 prep |
| W4 (2026-05-19) | Multi-strand input parser | accepts protein FASTA + RNA FASTA + ligand SMILES jointly | P0-1 |
| W5 (2026-05-26) | RNA + ligand encoder draft | encoder modules emit joint embedding tensor | P0-1, P0-2 |
| W6 (2026-06-02) | Cross-attention layer | attention over joint embedding produces interaction-aware logits | P0-2 |
| W7 (2026-06-09) | Training data prep | PDB-multimer subset filtered to 3-strand cases (P=10, N=50 bound per parent §9) | P2-10 |
| W8 (2026-06-16) | First training run | training loss curve recorded + naive eval on held-out subset | P0-3 |
| W9 (2026-06-23) | n6 invariant trace integration | output JSON logs τ(6)=4 / σ(6)=12 / J₂=24 / φ(6)=2 anchor points | P0-4 |
| W10 (2026-06-30) | AF-3 differentiation case selection | identify ≥1 multi-strand target where AF-3 fails | P0-5 prep |
| W11 (2026-07-07) | Case study run + verifier manifest | RMSD + TM-score numeric thresholds + COUNTER witness | P0-5, P1-8 |
| W12 (2026-07-14 to 2026-07-28) | C3 README + reviewer demo + 90-day MVP gate | F-TP5-b satisfied or retracted to YES_CONDITIONAL | gate verdict |

## §4 Falsifiers (raw 71 TRANSCEND-tier ≥5; declared 7)

Each falsifier is registered upfront with a measurable trigger condition. Hitting any one of F-MVP-1 through F-MVP-5 retracts the MVP YES claim and reverts parent domain registration to YES_CONDITIONAL.

| ID | Claim under test | Falsifying observation |
|----|------------------|------------------------|
| F-MVP-1 | MVP accepts ≥3 molecule types | pipeline accepts only 2 types or rejects RNA+ligand jointly |
| F-MVP-2 | Joint 3D output produced | output omits any input strand or any pairwise interaction tensor |
| F-MVP-3 | Write-side differentiation from AF-3 | every test case can be reproduced by AF-3 with equal or better quality (no AF-3 failure case exhibited) |
| F-MVP-4 | n6 invariant trace present | output JSON missing any of τ(6)=4 / σ(6)=12 / J₂=24 / φ(6)=2 anchor fields |
| F-MVP-5 | At least 1 AF-3-failing case study | by 2026-07-28, no documented case where HEXA-WEAVE > AF-3 on a multi-strand target |
| F-MVP-6 | Independence from AF-3 weights | hash-compare reveals MVP loads AF-3 weights (P2-12 hard violation) |
| F-MVP-7 | Reproducibility | external reviewer cannot reproduce any case-study run from manifest |

Demotion contract per raw 71: hitting F-MVP-3 or F-MVP-5 by deadline 2026-07-28 forces retraction of the YES domain registration upgrade and falsifies parent §1 claim "write-side composition layer is a distinct technical object" at the empirical level (the theoretical-analytical claim survives).

## §5 MISS criteria (raw 12 declared upfront)

The MVP is judged MISS when **any** of the following is true at 2026-07-28T23:59 UTC:

- M1: pipeline does not accept ≥3 molecule types end-to-end.
- M2: zero AF-3-failing case studies documented.
- M3: any P0 (1 through 5) deliverable absent.
- M4: verifier manifest produces FAIL on the declared numeric thresholds (RMSD ≥ 5 Å on every case-study run, TM-score ≤ 0.4 on every case-study run).
- M5: external reviewer cannot reproduce any case study from the run script + dataset manifest.
- M6: cost-actual exceeds cost-estimate (§8) by >3x without prior amendment commit.

Post-hoc adjustment of M1 through M6 is forbidden per own 12. Any drift from these criteria must be recorded as an explicit retraction commit.

## §6 External blockers (raw 51 saturation-adjacent honesty)

| # | Blocker | Class | Mitigation |
|---|---------|-------|------------|
| B1 | Compute budget — RTX 5070 12 GB on ubu1/ubu2; multi-strand inference may exceed VRAM | hardware | fall back to htz 124 GB CPU-only; accept slower inference |
| B2 | Dataset access — PDB-multimer 3-strand subset filtering may surface licensing constraints | dataset | restrict to PDB CC0 entries; document any exclusions |
| B3 | External reviewer access — F-MVP-7 + P1-7 require ≥1 outside reviewer | human-in-loop | open call via proposals/anthropic-fellows-research.md network; fallback = self-host CLI |
| B4 | Docker fix landing — reproducibility container depends on Task B B.3 docker fix | repo-internal | track Task B status; fallback = bare-metal venv with pinned versions |
| B5 | AF-3 closed re-runs — diff analysis requires AF-3 server access via DeepMind public endpoint | external service | record any rate-limit or access denial as a witness |
| B6 | OpenFold / ESM3 weight licensing | external | confirm Apache-2.0 or BSD compatibility before W2 base-model decision |

## §7 Verifier manifest (raw 53 deterministic)

Verifier type: **numeric_threshold + COUNTER**. No LLM judge.

```yaml
verifier_manifest:
  numeric_threshold:
    - metric: ca_rmsd_angstroms
      target: "< 5.0"
      scope: "per case-study run, full bundle aligned"
    - metric: tm_score
      target: "> 0.4"
      scope: "per case-study run, dominant chain"
    - metric: clash_score
      target: "< 100"
      scope: "post-relaxation, MolProbity-style"
  counter:
    - claim: "HEXA-WEAVE > AF-3 on at least one multi-strand target"
      witness_required: ">= 1 documented case"
      counter_evidence_path: "core/hexa-weave/case_studies/<id>/af3_diff.json"
  hash:
    - artifact: "verifier_manifest.yaml"
      sha256_pinned_at_w11: "TBD"
  regex:
    - field: "n6_invariant_trace"
      pattern: '^\\{"tau":4,"sigma":12,"J2":24,"phi":2,.*\\}$'
      scope: "every output JSON"
```

## §8 Cost-attribution (raw 86 forward-spec)

| Field | Value |
|-------|-------|
| cost-center | `hexa-weave-mvp` |
| task-id | `task-C-hexa-weave-mvp-90d` |
| cost-estimate | training: 4 GPU-weeks RTX 5070 (≈ $200 cloud-equiv) + inference: 1 GPU-week (≈ $50) + storage: 200 GB scratch (≈ $20) → ≈ **$270 forward-estimate** |
| cost-actual | accumulated by raw 77 ledger; reconciled at W12 |
| over-budget threshold | 3x ($810) — triggers M6 MISS per §5 |
| ledger sink | `state/discovery_absorption/registry.jsonl` cost field per row |

Forward-spec note: this is a contract first; impl follows. Actuals are appended to raw 77 ledger per dispatch / cron / daemon emission.

## §9 Honest C3 — what the MVP does NOT do (raw 91)

This list is the MVP's negative space and is part of the contract:

1. **No clinical validity claim** — outputs are not validated for any therapeutic, diagnostic, or in-vivo use.
2. **No production drug design** — case studies are illustrative; no claim of pharmaceutical readiness.
3. **No AF-3 weight reuse** — independence claim P2-12 enforced via hash-compare; no derivative model.
4. **No mechanistic-correctness claim** — n6 invariant traces are anchor points, not physical-mechanism explanations.
5. **No empirical thermodynamic validation** — Landauer-floor binding remains theoretical-analytical (parent §7 CHI2 axis stays DEFER until n≥5 sample).
6. **No Clay Millennium 7 solution claim** (own 11 / raw 11): P vs NP, NS, etc. are not "solved" by this MVP.
7. **No closed-source reuse** — IsoDDE is referenced for positioning only; no proprietary weight/code dependency.
8. **No automatic universe-ceiling extension** — TRANSCEND-CLOSURE-ALL Mk.X chain is parent-domain construction; this MVP exhibits L4 to L5 only.
9. **No real-time inference SLA** — MVP latency may be hours per case; production-grade serving is out of scope.
10. **No multi-team scale-out** — single-runner MVP; multi-team handoff is post-W12.

Risk list:

- R1: case-study target may not exhibit a clean AF-3 failure (mitigation: pre-screen 3 candidates by W7).
- R2: 12 GB VRAM may force model truncation that hurts P0-2 quality (mitigation: htz CPU fallback, accept slower).
- R3: reviewer recruitment may slip (B3 mitigation chain).
- R4: own 22 lint may flag this filename if frontmatter `category:` parsing differs from inference; mitigation: explicit `category: operational` declared.
- R5: discovery_absorption append may conflict with concurrent witness emission (mitigation: append-only JSONL, no in-place edit).

## §10 Auto-absorption hook

This proposal absorbs to `state/discovery_absorption/registry.jsonl` per raw 108 + raw 135. Append entry:

```json
{"schema":"anima/discovery_absorption/v1","ts":"2026-04-28T00:00:00Z","finding_id":"hexa-weave-mvp-spec-2026-04-28","witness_path":"proposals/hexa_weave_mvp_2026_04_28.md","absorption_channel":"proposal-spec-doc","absorption_target":"HEXA-WEAVE 90-day MVP forward-spec; F-TP5-b 2026-07-28 gate; 5 P0 + 4 P1 + 3 P2 deliverables; 7 falsifiers preregistered; 6 MISS criteria; verifier-type=numeric_threshold+COUNTER; cost-center=hexa-weave-mvp; cost-estimate=$270","status":"forward-spec","absorbed_at":"2026-04-28T00:00:00Z","absorbed_via":"raw 108+135 proposal absorption","classifier_version":"raw_108_v1","raw_91_c3":"forward-spec only — implementation has NOT started; this is a contract"}
```

## §11 Lint pre-flight

Expected pass on:

- `python3 tool/own_doc_lint.py` (own 1 / 3 / 4 / 5 / 16 — file is in `proposals/` not `domains/`, so own 3 / own 4 do not trigger; own 1 English-only PASS; own 16 not applicable to proposals).
- `python3 tool/proposal_lint.py proposals/hexa_weave_mvp_2026_04_28.md` (proposal#1 snake_case + date PASS; proposal#2 single umbrella H2 first-word `§N` headings — note: H2 with §-prefix start with "§" character, not a domain name, so umbrella consolidation is naturally satisfied).

## §12 Cross-references

- Parent body: `domains/biology/hexa-weave/hexa-weave.md` (§10 RISKS F-TP5-b, §12 TIMELINE 2026-07-28 row).
- Closure witness: `design/kick/2026-04-28_hexa-weave-closure_omega_cycle.json`.
- Predecessor witness: `design/kick/2026-04-28_hexa-weave-abstraction-to-limits_omega_cycle.json`.
- Mk.X TRANSCEND-CLOSURE-ALL witness: `design/kick/2026-04-28_hexa-weave-mk-x-transcend-closure-all_omega_cycle.json`.
- Discovery absorption registry: `state/discovery_absorption/registry.jsonl`.
- Sibling proposals: `proposals/anthropic-fellows-research.md` (reviewer recruitment channel).
