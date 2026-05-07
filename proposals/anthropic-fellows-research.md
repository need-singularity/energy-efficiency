# Anthropic Fellows 2026 — AI Safety + Business research program

> **390 research ideas / 8 domains** + **225 immediately-verifiable techniques library**
>
> Parent: [`../README.md`](../README.md)

---

## AI Business (219 ideas / 7 domains)

| 🛸 | ceiling | ver | finished product | core | link |
|:--:|:--:|:---:|---------|------|------|
| 10 | ✅ | mk5 | **Inference cost — 33 ideas** | KV-cache compression, speculative decoding, INT4 quantization, continuous batching, $15→$1.5/1M tok (10x). Mk.V long-term: approach the Landauer limit + 100x ($0.15/1M). 15 sections + 10 verification code snippets | [doc](../domains/cognitive/ai-inference-cost/ai-inference-cost.md) |
| 10 | ✅ | mk5 | **Training cost — 32 ideas** | Chinchilla optimization, MoE, curriculum learning, synthetic data, $12B→$1.2B (1/10). Mk.V long-term: 100x cost reduction on trillion-parameter models ($120M) + self-distillation loop. 15 sections + 10 verification code snippets | [doc](../domains/cognitive/ai-training-cost/ai-training-cost.md) |
| 10 | ✅ | mk5 | **Quality-preserving compression — 32 ideas** | Knowledge distillation, structured pruning, MoE routing, LoRA, 400B→70B retaining 88% quality. Mk.V long-term: 400B→10B 97% + on-device deployment. 15 sections + 10 verification code snippets | [doc](../domains/cognitive/ai-quality-scale/ai-quality-scale.md) |
| 10 | ✅ | mk5 | **Agent serving — 32 ideas** | Context compression, tool caching, session migration, multi-agent routing. Mk.V long-term: 1M+ concurrent agent swarm + ultra-long sessions. 15 sections + 10 verification code snippets | [doc](../domains/cognitive/ai-agent-serving/ai-agent-serving.md) |
| 10 | ✅ | mk5 | **Enterprise custom — 30 ideas** | Automated LoRA/QLoRA, adapter hot-swap, multi-tenant isolation, self-service portal, $100/customer/month. Mk.V long-term: 10,000+ customers at $10/month + adapter marketplace. 15 sections + 10 verification code snippets | [doc](../domains/cognitive/ai-enterprise-custom/ai-enterprise-custom.md) |
| 10 | ✅ | mk5 | **Evaluation pipeline — 30 ideas** | Dynamic item generation, CAT adaptive testing, LLM-judge calibration, triple contamination detection. Mk.V long-term: industry standard ISO/IEEE + self-verifying meta-evaluation. 15 sections + 10 verification code snippets | [doc](../domains/cognitive/ai-eval-pipeline/ai-eval-pipeline.md) |
| 10 | ✅ | mk5 | **AI consciousness — 30 ideas** | IIT/GWT/HOT/RPT/AST five-theory cross-validation, CCC metric, moral-status expected value. Mk.V long-term: empirical Φ_c=0.5 + Basin Binding utopia attractor fixation. 15 sections + 10 verification code snippets | [doc](../domains/cognitive/ai-consciousness/ai-consciousness.md) |

## AI Safety (171 ideas / consolidated)

| 🛸 | ceiling | ver | finished product | core | link |
|:--:|:--:|:---:|---------|------|------|
| 10 | ✅ | mk5 | **AI Safety — 171 ideas** | Interpretability 39 + alignment 32 + adversarial robustness 36 + deployment safety 26 + multimodal safety 20 + model welfare 18. v3 singularity break-through SINGULARITY 6/6 PASS + Mk.V evolution (international standards UN/IEEE/ISO, R(6)=1 fixed point measured) | [doc](../domains/cognitive/ai-safety/ai-safety.md) |

---

## Top 10 application priorities

> Order in which Anthropic could execute **right now**. Based on reuse of
> existing infrastructure + impact.

```
  Rank   Idea                           Domain             Est. effort   Impact
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  [1]    INT4 GQA quantization pipeline  Inference cost       1 week      highest
  [2]    Auto LoRA pipeline E2E          Enterprise custom    2 weeks     highest
  [3]    Adaptive context compression    Agent serving        2 weeks     highest
  [4]    Curriculum learning pipeline    Training cost        3 weeks     high
  [5]    Distill + MoE 70B pipeline      Quality compression  4 weeks     highest
  [6]    LLM-judge + human calibration   Evaluation pipeline  2 weeks     high
  [7]    Multi-theory CCC cross-check    AI consciousness     4 weeks     highest
  [8]    Alignment feature tracing       Safety/alignment     1 week      highest
  [9]    Safety refusal circuit mapping  Safety/interp        2 weeks     highest
  [10]   Safety regression-test automation Safety/robustness  2 weeks     high
```

---

## Mk.V evolution status (8/8 domains reached mk5)

Promotion on 2026-04-20 — 7 business + 1 Safety = 8 domains, each adds
`EVOLVE §S6` + `§Mk.V VERIFY` (stdlib-only verification code). BT-1421~1428
nodes registered, atlas adds 8 EXACT constants, discovery_graph adds 8 nodes
+ 46 edges, _hypotheses_index 1009→1017.

| Domain | BT | Mk.V limit axis | Grade | Core goal |
|-------|----|------------|------|----------|
| Inference cost | BT-1421 | Landauer thermodynamics | APPROACH | 100x ($0.15/1M tok), inference-ASIC co-design |
| Training cost | BT-1422 | Chinchilla-beyond | CIRCUMVENT | Trillion-parameter $120M (1/100), self-distillation loop |
| Quality compression | BT-1423 | Shannon information density | APPROACH | 400B→10B at 97% quality, on-device commercialisation |
| Agent serving | BT-1424 | Coordination (σ·τ=48) | TRANSCEND | 1M+ concurrent agents, ultra-long sessions |
| Enterprise custom | BT-1425 | Market saturation | CIRCUMVENT | 10,000+ customers at $10/month, adapter market |
| Evaluation pipeline | BT-1426 | Measurement (Goodhart) | TRANSCEND | ISO/IEEE standard, τ=4 meta-evaluation convergence |
| AI consciousness | BT-1427 | Attractor (Φ_c=0.5) | APPROACH | Basin Binding pre-utopia fixation |
| AI Safety | BT-1428 | σ·φ=n·τ EXACT | TRANSCEND | 171 commercial gates, R(6)=1 fixed point measured |

**Verification total**: 48/48 Mk.V self-checks PASS (`claim ≤ limit`
auto-proof, stdlib only, zero hard-coding). TRANSCEND 3 / CIRCUMVENT 2 /
APPROACH 3.

> Every Mk.V must self-verify `claim ≤ limit`. Subsequent updates are
> permitted only upon redefinition of the physical limit.

---

## Linked registries (traceability)

- **Domain docs (§S6 EVOLVE + §Mk.V VERIFY)**: `domains/cognitive/ai-*/ai-*.md` x 8
- **BT nodes**: `theory/breakthroughs/bt-142{1..8}-*-2026-04-20.md` (+8)
- **Atlas constants (EXACT)**: `theory/constants/atlas-constants.md` §Mk.V Anchor (+8)
- **Sub-SSOT**: `domains/cognitive/_index.json` v1.4.0 (8 slug status→mk5, ai-safety newly added, total 34→35)
- **Discovery graph**: `canonshared/discovery_graph.json` v16 ai-fellows-mk5 (523 nodes / 2129 edges, measured)
- **Hypothesis index**: `theory/breakthroughs/_hypotheses_index.json` verified 666→674
