# PAPER-P4-2 — bipartite fit>=0.95 Top 10 Pairs grep Audit

**Date**: 2026-04-14
**Basis**: PAPER-P4-2 roadmap item
**Source**: papers/lint_progress.jsonl (3023 edges, record_type=edge)
**Audit method**: For each pair's tech keyword, grep the body of the corresponding
  papers/n6-{paper}-paper.md with exact match + 5 variants (underscore→space, dash,
  Korean translation, abbreviation)

---

## Audit targets — top 10 by fit (descending)

| # | tech | paper | fit | Search variants | Result |
|---|------|-------|-----|-----------|------|
| 1 | mamba2 | anima-soc | 1.0000 | mamba, mamba2, mamba-2, ssm, state space | **MISS** |
| 2 | rwkv | anima-soc | 1.0000 | rwkv, RWKV, receptance weighted | **MISS** |
| 3 | boltzmann_gate | anima-soc | 0.9863 | boltzmann, energy gate, Boltzmann (KR) | **MISS** |
| 4 | rfilter_phase | anima-soc | 0.9851 | rfilter, phase filter, phase filter (KR) | **MISS** |
| 5 | hyena | anima-soc | 0.9810 | hyena, long conv, long-range convolution (KR) | **MISS** |
| 6 | bitnet | anima-soc | 0.9751 | bitnet, 1-bit, binary weight (KR) | **MISS** |
| 7 | vq_vae | anima-soc | 0.9739 | vq-vae, vqvae, vector quantiz, vector quantization (KR) | **MISS** |
| 8 | rwkv | unified-soc | 0.9711 | rwkv, RWKV, receptance weighted | **MISS** |
| 9 | hyena | unified-soc | 0.9681 | hyena, long conv, long-range convolution (KR) | **MISS** |
| 10 | top_k_sparsity | anima-soc | 0.9675 | top-k, top_k, sparsity, sparse (KR) | **MISS** |

## Audit result

**0 / 10 PASS — all MISS**

## Diagnosis

### Root cause analysis

The bipartite matching's 3023 edges were produced by a heuristic based on
**domain tags, technique categories, and title tokens**, not a full body-text search.

The top 10 pairs being entirely MISS confirms that the matching algorithm reflects
**metadata similarity** only and does not validate the **in-body technique description**
at all.

In particular, the 2 fit=1.0 cases (mamba2, rwkv → anima-soc) are presumed to arise
from a "if it is a SOTA technique in the SoC domain, then fit=1.0" rule applied via
the "sota" lens. The words mamba2 and rwkv never appear in the body of the anima-soc
paper even once.

### False positive rate

| Band | Targets | PASS | MISS | False positive rate |
|------|------|------|------|-----------|
| fit=1.0 | 2 | 0 | 2 | 100% |
| fit>=0.95 | 10 | 0 | 10 | 100% |

The concern recorded in honest-limitations.md §9 is confirmed by this audit.

### Paper status check

- `papers/n6-anima-soc-paper.md`: exists, 698 lines, 24,230 bytes, [CANONICAL v2]
- `papers/n6-unified-soc-paper.md`: exists (length unverified)
- Both papers are written in n=6 arithmetic coordinate mapping form and
  lack sections describing individual AI techniques (mamba2, rwkv, etc.).

## Follow-up recommendations

1. **bipartite matching algorithm needs redesign** — the current keyword heuristic
   produces false positives in bulk regardless of whether the body mentions the
   technique. At minimum, a TF-IDF or body-token intersection filter should be added.

2. **Interpret fit_score with caution** — fit=1.0 does not mean "the paper deeply
   covers the technique." At present it is only at the level of "shares the same
   category tag."

3. **Append statistics to honest-limitations.md §9** — append this audit's result
   (0/10 PASS, false positive rate 100%) to §9.

4. **Estimate in-body mention rate across 3023 edges** — full audit is cost-prohibitive,
   so estimate via random 50-edge sampling is recommended.

---

## Honesty record

This audit adheres to R0 (honesty verification) and R3 (measured values required).
MISS results are neither downplayed nor softened via partial matching.

Even with 5-variant search expansion the result is 0/10, so the finding is robust.
