# Tier-1 Prediction Experiment Protocols

> **Roadmap gates**: VER-P1-1 through VER-P1-4
> **Registration date**: 2026-04-16
> **Purpose**: Concrete, runnable experiment designs for all 4 Tier-1 predictions
> **Hardware budget**: 1x A100 80GB per experiment (cloud or on-prem)
> **Total wall time**: ~14 days sequential, ~5 days parallelized across 4 GPUs
> **Framework**: PyTorch 2.3+ / HuggingFace Transformers 4.44+ / PEFT 0.12+

---

## VER-P1-1: Egyptian Fraction Attention (EFA) Quality

### Claim

Splitting sigma=12 attention heads as 6(full-span local) + 4(medium-span) + 2(global sparse) -- following the Egyptian fraction decomposition 1/2 + 1/3 + 1/6 = 1 -- achieves >=98% of standard uniform multi-head attention quality on GLUE benchmark tasks while reducing attention FLOPs by approximately 40%, at sequence length 2048.

### Falsification Criteria

The prediction is **FALSIFIED** if ANY of the following hold:
- EFA average GLUE score drops >2 percentage points below standard attention baseline (i.e., quality retention <98%)
- EFA attention FLOPs savings are <25% compared to standard uniform 12-head attention at seq_len=2048
- Standard attention beats EFA on >=7/8 individual GLUE tasks

The prediction is **INCONCLUSIVE** if the GLUE score difference is within noise (|delta| < 0.3%) with fewer than 5 random seeds.

### Experimental Setup

- **Model**: BERT-base architecture (d_model=768, 6 encoder layers, vocab=30522)
  - Baseline: 12 uniform heads, d_head=64 each
  - EFA variant: 3 head groups with d_head = {384, 256, 128} (ratio 6:4:2 of 768)
- **Dataset**: GLUE benchmark (MNLI, QQP, QNLI, SST-2, CoLA, STS-B, MRPC, RTE)
- **Pre-training data**: English Wikipedia + BookCorpus (~16GB), standard BERT MLM+NSP
- **Hardware**: 1x NVIDIA A100 80GB
- **Framework**: PyTorch 2.3 + HuggingFace Transformers
- **Sequence length**: 512 for pre-training, 2048 for attention FLOP measurement

### Protocol

1. **Pre-train baseline BERT-base** on Wikipedia+BookCorpus for 1M steps, batch_size=256, lr=1e-4 with linear warmup (10K steps) + linear decay, AdamW (beta1=0.9, beta2=0.999, wd=0.01). Checkpoint at steps {200K, 400K, 600K, 800K, 1M}. Use mixed precision (bf16). Estimated: ~18 GPU-hours.

2. **Pre-train EFA BERT-base** with identical hyperparameters, replacing the standard multi-head attention module as follows:
   - **Head Group A** (6 heads equivalent, d=384): Full causal/bidirectional attention over the complete sequence. This is the "1/2" fraction (384/768 = 1/2).
   - **Head Group B** (4 heads equivalent, d=256): Sliding window attention with window_size=256 tokens. This is the "1/3" fraction (256/768 = 1/3).
   - **Head Group C** (2 heads equivalent, d=128): Global sparse attention attending to every 8th token (stride=8) plus [CLS] and [SEP]. This is the "1/6" fraction (128/768 = 1/6).
   - Each group computes Q, K, V projections at its own dimension, applies its attention pattern, and outputs are concatenated (384+256+128=768) before the output projection.

3. **Fine-tune both models** on each of the 8 GLUE tasks independently:
   - Learning rate: {2e-5, 3e-5, 5e-5} (grid search, report best)
   - Epochs: 3 for large tasks (MNLI, QQP, QNLI, SST-2), 10 for small tasks (CoLA, STS-B, MRPC, RTE)
   - Batch size: 32
   - 5 random seeds per configuration: {42, 123, 456, 789, 1024}

4. **Measure attention FLOPs** at seq_len=2048 using `fvcore.nn.FlopCountAnalysis` or manual counting:
   - Standard: 12 heads x (2048^2 x 64) x 2 (QK + AV) = known baseline
   - EFA: Group_A (2048^2 x 384 x 2) + Group_B (2048 x 256 x 256 x 2) + Group_C (2048 x 256 x 128 x 2)
   - Report both raw FLOPs and ratio.

5. **Record** per-task metrics, compute GLUE average, measure FLOP ratio, log training curves.

### Configurations to Compare

| Config | Heads | d_head | Attention Pattern | Expected FLOPs (relative) |
|--------|-------|--------|-------------------|--------------------------|
| Baseline | 12 uniform | 64 each | Full bidirectional | 1.00 |
| EFA-n6 | 3 groups (6+4+2 equiv) | 384/256/128 | Full + Window-256 + Sparse-stride8 | ~0.55-0.65 |
| Ablation-A | 2 groups (6+6 equiv) | 384/384 | Full + Window-256 | ~0.75 |
| Ablation-B | 12 uniform | 64 each | All Window-256 | ~0.13 |

### Metrics

- **Primary**: Average GLUE score (accuracy for classification tasks, Pearson/Spearman for STS-B, Matthews for CoLA)
- **Secondary**:
  - Per-task GLUE scores (8 individual values)
  - Pre-training MLM loss curve (convergence speed)
  - Attention FLOPs at seq_len = {512, 1024, 2048, 4096}
  - Throughput: tokens/second during training and inference
  - Peak GPU memory usage

### Statistical Rigor

- **Seeds**: 5 per configuration per task (total: 4 configs x 8 tasks x 5 seeds = 160 fine-tuning runs)
- **Significance test**: Paired t-test (Baseline vs EFA) across seeds for each task. Bonferroni correction for 8 tasks (alpha = 0.05/8 = 0.00625).
- **Minimum effect size**: Cohen's d >= 0.5 required to declare one config superior. Differences with d < 0.2 are considered equivalent.
- **Reporting**: Mean +/- std across seeds. Report all individual run results in appendix.

### Estimated Cost & Time

- **Pre-training (2 models)**: 2 x 18 = 36 GPU-hours
- **Fine-tuning (4 configs x 8 tasks x 5 seeds x 3 LR)**: ~12 GPU-hours
- **Total GPU-hours**: ~48
- **Cloud cost**: ~$96 at $2/hr (Lambda Cloud A100) or ~$192 at $4/hr (AWS p4d spot)
- **Wall time**: ~2 days

### Success Criteria

| Outcome | Condition |
|---------|-----------|
| **PASS** | EFA GLUE average >= 98% of Baseline AND FLOPs savings >= 30% |
| **STRONG PASS** | EFA GLUE average >= 99% of Baseline AND FLOPs savings >= 40% |
| **PARTIAL** | EFA GLUE average >= 96% of Baseline AND FLOPs savings >= 25% |
| **MISS** | EFA GLUE average < 96% of Baseline, OR FLOPs savings < 25% |
| **FALSIFIED** | EFA GLUE average < 98% of Baseline (>2pp drop) |

---

## VER-P1-2: LoRA Rank r=sigma-tau=8 Pareto Optimality

### Claim

LoRA fine-tuning with rank r=8 (= sigma(6) - tau(6) = 12 - 4) achieves the highest accuracy-per-trainable-parameter on standard NLU and code generation benchmarks, making it Pareto-optimal compared to r in {2, 4, 16, 32}. That is, no other rank achieves both higher accuracy AND fewer trainable parameters.

### Falsification Criteria

The prediction is **FALSIFIED** if:
- r=16 achieves higher accuracy/parameter-efficiency on >=3 out of 5 tasks (Pareto-dominates r=8)
- r=4 achieves equal accuracy to r=8 on >=4/5 tasks (making r=8 wasteful)
- Any rank r != 8 Pareto-dominates r=8 on the accuracy vs trainable-params frontier across all 5 tasks simultaneously

The prediction is **INCONCLUSIVE** if r=8 and r=16 are statistically indistinguishable on all tasks.

### Experimental Setup

- **Model**: Llama-3.1-8B-Instruct (meta-llama/Llama-3.1-8B-Instruct on HuggingFace)
- **Datasets** (5 tasks):
  1. SST-2 (sentiment, GLUE) -- classification
  2. MRPC (paraphrase, GLUE) -- classification
  3. RTE (entailment, GLUE) -- classification
  4. MMLU (5-shot, hendrycks/test) -- multiple choice
  5. HumanEval (code generation, openai/human-eval) -- pass@1
- **Hardware**: 1x NVIDIA A100 80GB
- **Framework**: PyTorch 2.3 + PEFT 0.12 + bitsandbytes (4-bit quantization for QLoRA)
- **LoRA config**: alpha=16, target_modules=["q_proj", "k_proj", "v_proj", "o_proj"], dropout=0.05

### Protocol

1. **Load base model** in 4-bit NF4 quantization (QLoRA setup) to fit within single A100 memory.

2. **For each rank r in {2, 4, 8, 16, 32}**, fine-tune on each of the 5 tasks:
   - **SST-2/MRPC/RTE**: Standard classification fine-tuning
     - lr=2e-4, batch_size=16, epochs=3 (SST-2) / 5 (MRPC, RTE)
     - Optimizer: AdamW (beta1=0.9, beta2=0.999, wd=0.01)
     - Schedule: cosine with 100 warmup steps
   - **MMLU**: 5-shot evaluation on the fine-tuned model (fine-tune on a 10K-sample instruction-following dataset first, e.g., databricks/databricks-dolly-15k subset)
     - lr=2e-4, batch_size=8, 1 epoch
   - **HumanEval**: Fine-tune on CodeAlpaca-20k for 1 epoch, then evaluate pass@1 (temperature=0.1, n=20 samples)
     - lr=1e-4, batch_size=4, 1 epoch

3. **Record** for each (rank, task, seed) triple:
   - Task accuracy / pass@1
   - Number of trainable parameters (function of rank)
   - Training time
   - Peak memory

4. **Compute Pareto frontier**: For each task, plot accuracy (y-axis) vs trainable parameters (x-axis). A rank is Pareto-optimal if no other rank achieves both higher accuracy and fewer parameters.

5. **Cross-task summary**: Count on how many tasks r=8 lies on the Pareto frontier.

### Configurations to Compare

| Config | Rank (r) | Alpha | Trainable Params | Param % of Full |
|--------|----------|-------|-------------------|-----------------|
| LoRA-2 | 2 | 4 | ~1.6M | 0.020% |
| LoRA-4 | 4 | 8 | ~3.1M | 0.040% |
| **LoRA-8** | **8** | **16** | **~6.3M** | **0.079%** |
| LoRA-16 | 16 | 32 | ~12.6M | 0.158% |
| LoRA-32 | 32 | 64 | ~25.2M | 0.316% |

Note: alpha = 2 * rank (standard scaling ratio of alpha/r = 2, matching n=6 prediction sigma/n=2).

### Metrics

- **Primary**: Accuracy / Trainable Parameter (normalized efficiency score per task)
- **Secondary**:
  - Raw accuracy on each task
  - Pareto frontier membership count (out of 5 tasks)
  - Training loss convergence curves
  - Training wall time per task
  - Peak GPU memory per configuration

### Statistical Rigor

- **Seeds**: 5 per (rank, task) pair. Total runs: 5 ranks x 5 tasks x 5 seeds = 125.
- **Significance test**: Friedman test across ranks (non-parametric, accounts for task differences), followed by Nemenyi post-hoc for pairwise comparisons.
- **Minimum effect size**: Accuracy difference >= 0.5 percentage points between adjacent ranks to declare a meaningful difference.
- **Pareto analysis**: A rank is Pareto-dominated if another rank beats it by >= 0.3pp accuracy while using fewer parameters.

### Estimated Cost & Time

- **Fine-tuning runs**: 125 runs x ~0.5 hr average = ~63 GPU-hours
- **Evaluation**: ~12 GPU-hours (MMLU 5-shot + HumanEval generation)
- **Total GPU-hours**: ~75
- **Cloud cost**: ~$150 (Lambda A100) to ~$300 (AWS p4d spot)
- **Wall time**: ~3-4 days on 1x A100

### Success Criteria

| Outcome | Condition |
|---------|-----------|
| **PASS** | r=8 is on the Pareto frontier for >=4/5 tasks |
| **STRONG PASS** | r=8 is on the Pareto frontier for 5/5 tasks AND has highest efficiency score on >=3/5 tasks |
| **PARTIAL** | r=8 is on the Pareto frontier for 3/5 tasks |
| **MISS** | r=8 is on the Pareto frontier for <=2/5 tasks |
| **FALSIFIED** | r=16 Pareto-dominates r=8 on >=3/5 tasks |

---

## VER-P1-3: MoE (8 experts, top-2) vs Alternatives

### Claim

At a fixed total parameter budget of approximately 1B, a Mixture-of-Experts transformer with sigma-tau=8 experts and top-phi=2 routing achieves lower validation perplexity than configurations (4,2), (16,2), (8,1), and (8,4) on C4 language modeling.

### Falsification Criteria

The prediction is **FALSIFIED** if:
- (16,2) achieves lower validation perplexity than (8,2) by >= 0.3 perplexity points
- Any non-(8,2) configuration achieves the lowest perplexity across >=3 of 5 seeds
- (8,1) matches (8,2) in perplexity while using fewer active FLOPs

The prediction is **INCONCLUSIVE** if all configurations are within 0.2 perplexity points of each other.

### Experimental Setup

- **Architecture**: GPT-2-style decoder-only transformer with MoE FFN layers
  - d_model=1024, n_heads=16, d_head=64, n_layers=12
  - MoE FFN in every other layer (layers 2, 4, 6, 8, 10, 12) = 6 MoE layers
  - Dense FFN in layers 1, 3, 5, 7, 9, 11
  - FFN inner dim = d_model x 4 / n_experts_per_token (scaled to keep active FLOPs constant where possible)
- **Total parameter budget**: ~1B (all configs adjusted to match within 5%)
- **Dataset**: C4 (allenai/c4, English, streaming), 10B tokens for training, 500M tokens held-out validation
- **Hardware**: 1x NVIDIA A100 80GB (models fit in bf16; for (16,x) configs use gradient checkpointing)
- **Framework**: PyTorch 2.3 + Megablocks 0.6+ (for efficient MoE training)
- **Tokenizer**: GPT-2 BPE (50257 vocab)

### Protocol

1. **Implement MoE layer** using Megablocks (block-sparse MoE) with token-choice routing and load-balancing auxiliary loss (coefficient = 0.01).

2. **Configure 5 MoE variants**, adjusting FFN inner dim per expert to keep total params at ~1B:

   | Config | Experts | Top-k | FFN inner (per expert) | Total Params |
   |--------|---------|-------|-----------------------|--------------|
   | (4, 2) | 4 | 2 | 2048 | ~1.02B |
   | **(8, 2)** | **8** | **2** | **1024** | **~1.01B** |
   | (16, 2) | 16 | 2 | 512 | ~1.03B |
   | (8, 1) | 8 | 1 | 1024 | ~1.01B |
   | (8, 4) | 8 | 4 | 1024 | ~1.01B |

   Note: (8,1) has lower active FLOPs per token than (8,2), while (8,4) has higher. This is intentional -- the claim is about quality, not just efficiency.

3. **Train each configuration** for 50K steps:
   - Batch size: 512K tokens (512 sequences x 1024 context length)
   - Total tokens seen: 50K x 512K = ~25.6B tokens
   - Learning rate: 3e-4, cosine schedule with 2000 warmup steps
   - Optimizer: AdamW (beta1=0.9, beta2=0.95, wd=0.1)
   - Gradient clipping: max_norm=1.0
   - Mixed precision: bf16

4. **Evaluate** on held-out C4 validation split:
   - Validation perplexity every 5K steps
   - Final perplexity at step 50K
   - Also evaluate on Lambada (zero-shot), HellaSwag (zero-shot), and WikiText-103 perplexity for generalization check

5. **Measure active FLOPs per token** for each configuration to enable efficiency-adjusted comparison.

### Configurations to Compare

| Config | n_experts | top_k | Active Params/Token | Expert Utilization |
|--------|-----------|-------|--------------------|--------------------|
| (4, 2) | 4 | 2 | ~660M | 50% |
| **(8, 2)** | **8** | **2** | **~420M** | **25%** |
| (16, 2) | 16 | 2 | ~290M | 12.5% |
| (8, 1) | 8 | 1 | ~270M | 12.5% |
| (8, 4) | 8 | 4 | ~570M | 50% |

### Metrics

- **Primary**: Validation perplexity on C4 at step 50K
- **Secondary**:
  - Lambada accuracy (zero-shot)
  - HellaSwag accuracy (zero-shot)
  - WikiText-103 perplexity
  - Expert load balance (max/min utilization ratio across experts)
  - Training throughput (tokens/sec)
  - Router entropy (should be high for good expert utilization)

### Statistical Rigor

- **Seeds**: 5 per configuration (total: 5 configs x 5 seeds = 25 training runs)
- **Significance test**: One-way ANOVA on final validation perplexity across configs, followed by Tukey HSD post-hoc test for pairwise comparisons.
- **Minimum effect size**: Perplexity difference >= 0.3 between (8,2) and runner-up to declare a winner. If difference < 0.15, declare equivalent.
- **Confound control**: All configurations share identical non-MoE layers, same data order per seed, same tokenizer. The ONLY difference is the MoE layer design.

### Estimated Cost & Time

- **Training**: 25 runs x ~8 GPU-hours = ~200 GPU-hours
- **Evaluation**: ~10 GPU-hours
- **Total GPU-hours**: ~210
- **Cloud cost**: ~$420 (Lambda) to ~$840 (AWS)
- **Wall time**: ~5 days on 1x A100 (sequential) or ~2 days on 4x A100
- **Note**: This is the most expensive Tier-1 experiment. If budget-constrained, reduce to 3 seeds and 30K steps (cuts cost by ~50% with moderate statistical power loss).

### Success Criteria

| Outcome | Condition |
|---------|-----------|
| **PASS** | (8,2) has lowest C4 validation perplexity among all 5 configs (mean across seeds) |
| **STRONG PASS** | (8,2) has lowest perplexity AND lowest perplexity-per-active-FLOP |
| **PARTIAL** | (8,2) is within top-2 configs by perplexity, and no other config beats it by >0.3pp |
| **MISS** | (8,2) ranks 3rd or worse among the 5 configs |
| **FALSIFIED** | (16,2) beats (8,2) by >0.3 perplexity points on >=3/5 seeds |

---

## VER-P1-4: Mertens Dropout p=ln(4/3) ~ 0.288

### Claim

Dropout with p=ln(4/3) ~ 0.288 (derived from the Mertens function of n=6 arithmetic) matches or outperforms the standard p=0.3 on fine-tuning tasks with small training sets (<10K samples), and outperforms all other tested dropout rates on average.

### Falsification Criteria

The prediction is **FALSIFIED** if:
- p=0.3 beats p=0.288 by >0.5 percentage points on >=3/5 small GLUE tasks
- p=0.1 or p=0.2 achieves higher average accuracy than p=0.288 across all tasks
- The optimal dropout rate is consistently p=0.5 or p=0.0 (indicating the 0.288 vs 0.3 distinction is irrelevant)

The prediction is **INCONCLUSIVE** if:
- p=0.288 and p=0.3 are within 0.3pp on all tasks (difference is below noise floor)

### Experimental Setup

- **Model**: BERT-base-uncased (google-bert/bert-base-uncased, pre-trained checkpoint from HuggingFace)
- **Datasets** (5 small GLUE tasks, all with training set <10K samples):
  1. CoLA (8.5K train) -- linguistic acceptability, Matthews correlation
  2. MRPC (3.7K train) -- paraphrase, accuracy/F1
  3. RTE (2.5K train) -- textual entailment, accuracy
  4. STS-B (5.7K train) -- semantic similarity, Pearson/Spearman
  5. WNLI (635 train) -- coreference/entailment, accuracy
- **Hardware**: 1x NVIDIA A100 80GB (overkill, but ensures no memory issues)
- **Framework**: PyTorch 2.3 + HuggingFace Transformers

### Protocol

1. **Download pre-trained BERT-base-uncased** from HuggingFace.

2. **For each dropout rate p in {0.0, 0.1, 0.2, 0.288, 0.3, 0.5}**, modify ALL dropout layers in the BERT model:
   - `attention_probs_dropout_prob = p`
   - `hidden_dropout_prob = p`
   - classifier head dropout = p

3. **Fine-tune on each of the 5 tasks**:
   - Learning rate: 2e-5
   - Batch size: 16
   - Epochs: 10 (small datasets benefit from longer training)
   - Optimizer: AdamW (beta1=0.9, beta2=0.999, wd=0.01)
   - Schedule: linear warmup (6% of total steps) + linear decay
   - Evaluation: every epoch on dev set, report best dev metric
   - Max sequence length: 128

4. **Repeat** with 10 random seeds per (dropout, task) pair: {42, 123, 234, 345, 456, 567, 678, 789, 890, 1024}. This high seed count is critical because the differences between p=0.288 and p=0.3 are expected to be small.

5. **Record** for each (dropout, task, seed) triple:
   - Best dev metric (accuracy, F1, Matthews correlation, or Pearson correlation depending on task)
   - Epoch at which best dev metric was achieved (to check if p=0.288 converges faster)
   - Training loss at end of training (to check overfitting)

6. **Compute**:
   - Mean and std of dev metric across seeds, per (dropout, task)
   - Average rank of each dropout rate across all 5 tasks
   - Whether p=0.288 vs p=0.3 shows a consistent directional advantage

### Configurations to Compare

| Config | Dropout p | Keep Rate | Scale Factor | Derived From |
|--------|-----------|-----------|--------------|--------------|
| No-Drop | 0.000 | 1.000 | 1.000 | Baseline (no regularization) |
| Low | 0.100 | 0.900 | 1.111 | 1/(sigma-phi) |
| Medium | 0.200 | 0.800 | 1.250 | phi/(sigma-phi) |
| **Mertens** | **0.288** | **0.712** | **1.404** | **ln(tau/3) = ln(4/3)** |
| Standard | 0.300 | 0.700 | 1.429 | Industry default |
| High | 0.500 | 0.500 | 2.000 | 1/phi |

### Metrics

- **Primary**: Average dev metric across 5 tasks (each task's metric normalized to [0,1] first)
- **Secondary**:
  - Per-task dev metrics with confidence intervals
  - Win/loss count: tasks where p=0.288 beats p=0.3 vs tasks where p=0.3 wins
  - Overfitting gap: (train accuracy - dev accuracy) per dropout rate
  - Convergence speed: epoch number of best dev performance
  - Effect of dropout on training stability (variance of final metrics across seeds)

### Statistical Rigor

- **Seeds**: 10 per (dropout, task) pair. Total runs: 6 dropouts x 5 tasks x 10 seeds = 300.
- **Significance test**: Wilcoxon signed-rank test for paired comparison of p=0.288 vs p=0.3 (non-parametric, appropriate for small sample sizes and non-normal distributions). Separate test per task, plus an overall test on mean ranks.
- **Minimum effect size**: 0.5 percentage points to declare p=0.288 superior to p=0.3 on a given task. For the overall average, 0.3pp.
- **Multiple comparison correction**: Holm-Bonferroni for the 5 per-task tests (alpha=0.05).
- **Power analysis**: With 10 seeds and expected effect size of 0.3-0.5pp, Cohen's d ~ 0.3, statistical power ~ 0.6. This is marginal but sufficient for a directional test. If power is insufficient, the result is INCONCLUSIVE (not FALSIFIED).

### Estimated Cost & Time

- **Fine-tuning runs**: 300 runs x ~0.05 hr average = ~15 GPU-hours
- **Total GPU-hours**: ~15
- **Cloud cost**: ~$30 (Lambda A100) to ~$60 (AWS p4d spot)
- **Wall time**: ~1 day on 1x A100

### Success Criteria

| Outcome | Condition |
|---------|-----------|
| **PASS** | p=0.288 has highest average rank across 5 tasks among all 6 dropout values |
| **STRONG PASS** | p=0.288 beats p=0.3 on >=4/5 tasks AND has highest average metric |
| **PARTIAL** | p=0.288 beats p=0.3 on >=3/5 tasks OR is within 0.2pp of top dropout on average |
| **MISS** | p=0.288 beats p=0.3 on <=2/5 tasks AND ranks 3rd or worse overall |
| **FALSIFIED** | p=0.3 beats p=0.288 by >0.5pp on >=3/5 tasks |

---

## Cross-Experiment Summary

### Resource Totals

| Experiment | GPU-hours | Cloud Cost (est.) | Wall Time | Priority |
|------------|-----------|-------------------|-----------|----------|
| VER-P1-1 (EFA) | 48 | $96-$192 | 2 days | HIGHEST (novel technique) |
| VER-P1-2 (LoRA r=8) | 75 | $150-$300 | 3-4 days | HIGH (directly actionable) |
| VER-P1-3 (MoE 8,2) | 210 | $420-$840 | 5 days | MEDIUM (expensive but decisive) |
| VER-P1-4 (Mertens Dropout) | 15 | $30-$60 | 1 day | HIGH (cheapest, quickest) |
| **TOTAL** | **348** | **$696-$1392** | **11-12 days** | |

### Recommended Execution Order

1. **VER-P1-4 (Mertens Dropout)** -- cheapest, fastest, establishes experimental pipeline
2. **VER-P1-1 (EFA)** -- highest novelty, most impactful for the N6 framework
3. **VER-P1-2 (LoRA r=8)** -- directly reproducible with existing tools
4. **VER-P1-3 (MoE 8,2)** -- most expensive, run last or in parallel if multi-GPU available

### Pre-Registration Commitment

All experiment protocols defined above are FROZEN as of 2026-04-16. The following are immutable:
- Falsification criteria
- Primary metrics
- Model and dataset choices
- Success/failure thresholds

The following may be adjusted during execution:
- Learning rate grid (additional values may be tested)
- Number of seeds (may be increased, never decreased)
- Additional ablations (do not affect primary results)
- Hardware (equivalent or better; never weaker)

### Reporting Template

Each completed experiment will produce a report at `reports/tier1/VER-P1-X_results.md` containing:
1. Exact configuration used (git commit hash of code)
2. Raw numerical results (all seeds, all tasks)
3. Statistical test outputs (p-values, effect sizes, confidence intervals)
4. Verdict: PASS / STRONG PASS / PARTIAL / MISS / FALSIFIED / INCONCLUSIVE
5. Unexpected observations or anomalies
6. atlas.n6 promotion recommendation (if PASS: [7] -> [10*] candidate)
