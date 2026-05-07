# PAPER-P4-2 — Bipartite Top 10 Pairs Measured Audit

## Purpose

Among the `{tech, paper, fit_score, evidence_lens}` bipartite edges in
`papers/lint_progress.jsonl` (P1-4 output, 3132 lines, 3023 edges + 108 paper records),
audit the top 10 by fit_score via actual grep against paper body text. Check whether
the keyword appears in the body, and compute the MATCH / NEAR / MISS proportions for
the bipartite heuristic.

## Input

- Path: `/Users/ghost/core/canon/papers/lint_progress.jsonl`
- Edge format: `{"tech": ..., "tech_cat": ..., "paper": ..., "fit_score": 0.0~1.0, "evidence_lens": "..."}`
- fit_score distribution:
  - fit == 1.0: 2 (mamba2/anima-soc, rwkv/anima-soc)
  - fit >= 0.96: 10 (all targeting the anima-soc paper)
  - continuous distribution below that
- This audit sampled the top 10 pairs in descending fit order; all 10 converged on the
  single target paper `papers/n6-anima-soc-paper.md`. This is due to the lint_progress
  heuristic funneling "modern ML/DL-adjacent techniques" (compress/sparse/sota) onto
  the single anima-soc paper.

## Audit method

1. For each tech keyword, perform lower-case substring matching with the following variants:
   - original form (`flash_attention`)
   - underscore → space (`flash attention`)
   - underscore → hyphen (`flash-attention`)
   - underscore removed (`flashattention`)
2. Verdict:
   - MATCH: original form or the space/hyphen variant exists in the body
   - NEAR: only a partial keyword (4 chars or more) exists, without the original form
   - MISS: no variant exists
3. Paper file: `/Users/ghost/core/canon/papers/n6-anima-soc-paper.md` (698 lines)

## Results table

| #  | tech                        | tech_cat | paper     | fit   | Status | hit_line | Remarks |
|----|-----------------------------|----------|-----------|-------|-------|----------|------|
| 1  | mamba2                      | sota     | anima-soc | 1.000 | MISS  | 0        | No Mamba / SSM vocabulary at all |
| 2  | rwkv                        | sota     | anima-soc | 1.000 | MISS  | 0        | No RWKV / recurrent vocabulary at all |
| 3  | boltzmann_gate              | sparse   | anima-soc | 0.986 | NEAR  | 2        | "gate" exists but in the sense of sigma(6)=12 process-integration gate — unrelated to boltzmann |
| 4  | rfilter_phase               | sparse   | anima-soc | 0.985 | MISS  | 0        | No r-filter / phase filter vocabulary at all |
| 5  | bitnet                      | compress | anima-soc | 0.975 | MISS  | 0        | No 1-bit LLM / BitNet vocabulary at all |
| 6  | vq_vae                      | compress | anima-soc | 0.974 | MISS  | 0        | No vector quantization / VAE vocabulary at all |
| 7  | top_k_sparsity              | sparse   | anima-soc | 0.968 | MISS  | 0        | No top-k / sparsity vocabulary at all |
| 8  | pruning_lottery_ticket      | compress | anima-soc | 0.965 | MISS  | 0        | No pruning / lottery ticket vocabulary at all |
| 9  | tensor_decomposition        | compress | anima-soc | 0.962 | NEAR  | 1        | "Axis Decomposition" appears — a sigma=12 axis-decomposition sense different from tensor decomposition |
| 10 | mixture_of_tokenizers       | compress | anima-soc | 0.961 | MISS  | 0        | No tokenizer / MoE vocabulary at all |

## Aggregate

| Verdict  | Count | Share |
|-------|------|-------|
| MATCH | 0    | 0.0%  |
| NEAR  | 2    | 20.0% |
| MISS  | 8    | 80.0% |

- **Audit rate (MATCH)**: 0 / 10 = **0.0%**
- **Inclusive match (MATCH + NEAR)**: 2 / 10 = **20.0%**
- **MISS rate**: 8 / 10 = **80.0%**

Even the 2 NEAR cases (boltzmann_gate, tensor_decomposition) have no actual relevance
in context. "gate" means the sigma(6)=12 n=6 process-integration gate, and
"axis decomposition" means partitioning along the sigma=12 axis, which is entirely
different from machine-learning usages of boltzmann gate / tensor decomposition.
Interpreted strictly, the actual MATCH rate converges to **0 / 10 = 0%**.

## Limitations (honesty record)

1. **bipartite is a keyword-based heuristic**. lint_progress assigns fit_score from
   paper-category × technique-category matching and does not verify actual body
   mentions. For this reason, papers with an "ml/dl-direct" section receive high
   fit scores for all modern ML techniques.

2. **Bias of the anima-soc paper**. anima-soc is a paper covering n=6 SoC architecture
   based on sigma=12 / tau=4 / phi=2 parameters; it does not actually describe concrete
   ML techniques like mamba2/rwkv/bitnet in its body. The reason bipartite funneled
   the top ML techniques into this paper is presumed to be over-inclusion of lens tags
   such as evidence_lens = "ml/dl-direct|compress".

3. **Keyword matching blind spots**. The paper might mention things using Korean
   translations (e.g., a Korean phrase for "vector quantization"); this audit tried
   only English keyword variants. If another audit round is needed, Korean-language
   keyword glosses should also be included for techniques such as mamba2
   (state-space-model / SSM gloss), rwkv (recurrent / linear-attention gloss),
   vq_vae (vector-quantization VAE gloss), pruning_lottery_ticket (pruning gloss),
   bitnet (1-bit gloss), and top_k_sparsity (top-k sparsity gloss).

4. **All top 10 on the same paper**. The fact that the entire fit 0.96~1.0 band
   funnels into anima-soc is itself a signal that the bipartite heuristic does not
   reflect real-world relevance. A healthy bipartite would distribute across different
   papers (agi-architecture, ai-17-techniques, etc.).

5. **Correction of optimistic inference**. This audit's real-MATCH rate was 0% in
   the top 10 sample, but this does not mean the entire 3023-edge MATCH rate is 0%.
   In lower fit bands, genuinely related pairs may be more common (random sample
   needed).

## Recommendations

1. In v2 of `lint_progress.jsonl`, weight body-grep matching as a required component
   of fit_score. (e.g., fit_new = 0.5 * category_match + 0.5 * body_grep_match)
2. Exclude or separately categorize n=6-structure-centric papers like anima-soc
   from the ML technique bipartite set.
3. Use a Korean-English paired keyword dictionary when grepping Korean paper bodies.
4. In PAPER-P4-3, audit a random 10 sample of the mid-fit (0.70~0.85) band as well
   to compute the MATCH curve per fit band.

## Artifacts

- This document: `/Users/ghost/core/canon/experiments/paper/p4_bipartite_audit_top10.md`
- Input: `/Users/ghost/core/canon/papers/lint_progress.jsonl`
- Audit target: `/Users/ghost/core/canon/papers/n6-anima-soc-paper.md`
- Audit date: 2026-04-14
