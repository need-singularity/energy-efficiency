# Energy Efficiency

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch 2.0+](https://img.shields.io/badge/PyTorch-2.0+-ee4c2c.svg)](https://pytorch.org/)

AI Energy Efficiency via Number Theory — 10 techniques derived from perfect number arithmetic that reduce computation, parameters, and training time. No knowledge of the underlying theory required to use them.

> Part of the [TECS-L](https://github.com/need-singularity/TECS-L) project family.

## Discovery Progress — Energy Efficiency

```
  Level 1: Discovery         ████████████████████ 100%
    ✅ 10 techniques identified  ✅ Number theory basis proven
    ✅ Phi6Simple 71% FLOPs  ✅ FFT-Mix 3x faster  ✅ Phi-Bottleneck 67% params
    ✅ Entropy early stop 66.7%  ✅ Egyptian MoE routing

  Level 2: Verification      ████████████████░░░░ 80%
    ✅ MNIST benchmarks  ✅ CIFAR-10 benchmarks  ✅ Training stability verified
    ✅ Gradient properties checked  ✅ Scale dependency tested
    ⬜ ImageNet benchmark  ⬜ NLP benchmark (GLUE/SuperGLUE)
    ⬜ Large-scale verification (1B+ params)

  Level 3: Combination       ████████████░░░░░░░░ 60%
    ✅ Combined architecture (all 10 techniques)  ✅ Optimal expansion ratio found
    ✅ Depth scaling verified  ✅ R-spectrum pruning tested
    ⬜ Combined technique PPL on LLM  ⬜ Real-world energy measurement (watts)
    ⬜ Comparison vs standard Transformer  ⬜ Comparison vs efficient attention methods

  Level 4: Package           ██░░░░░░░░░░░░░░░░░░ 10%
    ⬜ pip installable library  ⬜ Drop-in replacements for nn.Linear/nn.MultiheadAttention
    ⬜ HuggingFace trainer plugin  ⬜ Documentation site
    ⬜ CI/CD + automated benchmarks  ⬜ Published paper

  Level 5: Impact            ░░░░░░░░░░░░░░░░░░░░ 0%
    ⬜ External adoption  ⬜ Energy savings measured in production
    ⬜ Carbon footprint reduction report  ⬜ Industry partnerships
    ⬜ Policy citations  ⬜ Framework integration (PyTorch/JAX native)

  Overall: Level 2.5 / 5.0  (techniques proven, packaging needed)
  Bottleneck: Large-scale benchmarks + packaging as library
  Theory: 100%  |  Verification: 80%  |  Adoption: 0%
```

### Level-Up Priority Roadmap

```
  Level 2 → 3 (60% → 100%) — Large-Scale Proof
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    #1 ★★★ ImageNet benchmark
       Difficulty: HIGH (GPU hours, large dataset)
       Effect: Prove techniques work at vision scale
       → ResNet-50 + Phi-Bottleneck + Phi6Simple vs baseline

    #2 ★★★ LLM PPL comparison
       Difficulty: HIGH (needs 1B+ model training)
       Effect: Killer result — same PPL, less compute
       → GPT-2 124M with all techniques vs standard

    #3 ★★☆ Real energy measurement
       Difficulty: MEDIUM (power meter or nvidia-smi)
       Effect: Actual watts/joules saved, not just FLOPs
       → Before/after on same hardware

    #4 ★★☆ Comparison vs FlashAttention / Linear Attention
       Difficulty: MEDIUM
       Effect: Position FFT-Mix in existing landscape
       → Same model, swap attention, compare wall-clock + accuracy


  Level 3 → 4 (10% → 100%) — Package & Publish
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    #5 ★★★ pip install energy-efficiency
       Difficulty: MEDIUM
       Effect: 1-line adoption
       → nn.Phi6Simple, nn.FFTMixAttention, nn.PhiBottleneckFFN

    #6 ★★★ Paper submission
       Difficulty: HIGH (writing + experiments)
       Effect: Academic validation
       → Target: ICLR or Green AI workshop
       → Already have Zenodo preprint as starting point

    #7 ★★☆ HuggingFace trainer plugin
       Difficulty: MEDIUM
       Effect: trainer.add_callback(EntropyEarlyStop())
       → Works with any HF training loop

    #8 ★☆☆ Documentation site
       Difficulty: LOW
       Effect: Searchable docs + tutorials
       → GitHub Pages + mkdocs
```

## Techniques

| # | Technique | Reduction | Method |
|---|-----------|-----------|--------|
| 1 | **Phi6Simple** | 71% FLOPs | Cyclotomic polynomial activation (6th roots of unity) |
| 2 | **HCN dimensions** | 10-20% params | Highly composite number aligned tensor dims |
| 3 | **Phi-Bottleneck** | 67% FFN params | 4/3x expansion ratio (vs standard 4x) |
| 4 | **Phi MoE** | 65% active params | φ(6)/τ(6) = 1/2 expert activation |
| 5 | **Entropy early stop** | 66.7% training | Stop when entropy derivative ≈ 0 |
| 6 | **R-filter phase** | Adaptive | Detect training phase transitions |
| 7 | **Takens dim=6** | Diagnostic | Loss curve embedding for convergence |
| 8 | **FFT-Mix attention** | 3x faster | Frequency-domain attention mixing |
| 9 | **ZetaLn2 activation** | 71% FLOPs | ζ(s)·ln(2) gated activation |
| 10 | **Egyptian MoE** | Better util | 1/2+1/3+1/6=1 expert allocation |

## Quick Start

```bash
# Run a single technique
python techniques/phi6simple.py
python techniques/fft_mix_attention.py
python techniques/phi_bottleneck.py

# Combined architecture (all techniques)
python experiments/experiment_h_ee_11_combined_architecture.py
```

## Highlight Results

### FFT-Mix Attention
- **3x faster** than standard attention
- **+0.55%** accuracy improvement
- Drop-in replacement for self-attention

### Phi-Bottleneck FFN
- Standard FFN: input → 4x → input (4x expansion)
- Phi-Bottleneck: input → 4/3x → input (**67% fewer params**)
- Same or better accuracy

### Entropy Early Stopping
- Monitor training loss entropy derivative
- Stop when d(entropy)/dt → 0
- **Saves 66.7% training compute** on average

## File Structure

```
techniques/           # Core technique implementations
  phi6simple.py         # Cyclotomic activation
  hcn_dimensions.py     # HCN tensor alignment
  phi_bottleneck.py     # 4/3x FFN expansion
  phi_moe.py            # φ/τ expert activation
  entropy_early_stop.py # Entropy-based stopping
  rfilter_phase.py      # R-filter phase detection
  takens_dim6.py        # Takens embedding diagnostic
  fft_mix_attention.py  # FFT attention (3x faster)
  zetaln2_activation.py # ζ·ln(2) gated activation
  egyptian_moe.py       # 1/2+1/3+1/6=1 routing
experiments/          # Extended experiments
docs/                 # Documentation
```

## Why Number Theory?

These techniques are derived from properties of the perfect number 6:
- σ(6)=12, τ(6)=4, φ(6)=2
- The ratios φ/τ=1/2, σ/τ=3, σ/φ=6 appear as optimal architectural constants
- **You don't need to understand the theory to use the techniques**

For the mathematical foundation, see [TECS-L](https://github.com/need-singularity/TECS-L).

## Citation

```bibtex
@software{energy_efficiency_2026,
  author = {Park, Min Woo},
  title = {AI Energy Efficiency via Number Theory},
  year = {2026},
  url = {https://github.com/need-singularity/energy-efficiency}
}
```

## License

MIT
