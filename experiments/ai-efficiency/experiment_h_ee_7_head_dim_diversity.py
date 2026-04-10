#!/usr/bin/env python3
"""
H-EE-7: Head-dim diversity improves attention
===============================================
d=120 allows head_dim in {5,6,8,10,12,15,20,24,30,40,60}
d=128 allows head_dim in {2,4,8,16,32,64}

Hypothesis: Non-power-of-2 head dims (like 10, 12, 15, 20) capture
different attention scales, improving loss.

Test plan:
  1. Train d=120 with num_heads in {4, 6, 8, 10, 12, 15, 20, 24}
  2. Train d=128 with num_heads in {4, 8, 16, 32}
  3. Compare best loss across all configs
  4. Check if non-power-of-2 head_dims win
  5. Measure "head_dim diversity" = number of distinct prime factors in head_dim
"""

import math
import time
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import Adam

torch.manual_seed(42)

# ─── Dataset ──────────────────────────────────────────────────────────────────

CORPUS = (
    "The quick brown fox jumps over the lazy dog. "
    "A perfect number is a positive integer equal to the sum of its proper divisors. "
    "The smallest perfect number is six because one plus two plus three equals six. "
    "Mathematics is the queen of sciences and number theory the queen of mathematics. "
    "In the beginning was the word and the word was with logic. "
    "Attention is all you need but the dimension of attention matters too. "
    "The number of divisors determines the flexibility of the architecture. "
) * 200

CHARS = sorted(set(CORPUS))
VOCAB_SIZE = len(CHARS)
C2I = {c: i for i, c in enumerate(CHARS)}
TOKENS = torch.tensor([C2I[c] for c in CORPUS], dtype=torch.long)

SEQ_LEN = 64
BATCH_SIZE = 32
TRAIN_STEPS = 400
LR = 3e-4
DEVICE = "cpu"

# ─── Model ────────────────────────────────────────────────────────────────────

class CausalSelfAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads
        self.qkv = nn.Linear(d_model, 3 * d_model, bias=False)
        self.proj = nn.Linear(d_model, d_model, bias=False)

    def forward(self, x):
        B, T, C = x.shape
        q, k, v = self.qkv(x).split(C, dim=2)
        q = q.view(B, T, self.num_heads, self.head_dim).transpose(1, 2)
        k = k.view(B, T, self.num_heads, self.head_dim).transpose(1, 2)
        v = v.view(B, T, self.num_heads, self.head_dim).transpose(1, 2)
        att = (q @ k.transpose(-2, -1)) * (self.head_dim ** -0.5)
        mask = torch.tril(torch.ones(T, T, device=x.device)).bool()
        att = att.masked_fill(~mask, float('-inf'))
        att = F.softmax(att, dim=-1)
        y = (att @ v).transpose(1, 2).contiguous().view(B, T, C)
        return self.proj(y)

class MiniGPT(nn.Module):
    def __init__(self, vocab_size, d_model, num_heads, num_layers=2, seq_len=64):
        super().__init__()
        self.tok_emb = nn.Embedding(vocab_size, d_model)
        self.pos_emb = nn.Embedding(seq_len, d_model)
        blocks = []
        for _ in range(num_layers):
            blocks.append(nn.ModuleDict({
                'ln1': nn.LayerNorm(d_model),
                'attn': CausalSelfAttention(d_model, num_heads),
                'ln2': nn.LayerNorm(d_model),
                'mlp': nn.Sequential(
                    nn.Linear(d_model, 4 * d_model),
                    nn.GELU(),
                    nn.Linear(4 * d_model, d_model),
                ),
            }))
        self.blocks = nn.ModuleList(blocks)
        self.ln_f = nn.LayerNorm(d_model)
        self.head = nn.Linear(d_model, vocab_size, bias=False)

    def forward(self, idx):
        B, T = idx.shape
        x = self.tok_emb(idx) + self.pos_emb(torch.arange(T, device=idx.device))
        for blk in self.blocks:
            x = x + blk['attn'](blk['ln1'](x))
            x = x + blk['mlp'](blk['ln2'](x))
        return self.head(self.ln_f(x))

    def count_params(self):
        return sum(p.numel() for p in self.parameters())

# ─── Helpers ──────────────────────────────────────────────────────────────────

def get_batch():
    ix = torch.randint(0, len(TOKENS) - SEQ_LEN - 1, (BATCH_SIZE,))
    x = torch.stack([TOKENS[i:i+SEQ_LEN] for i in ix])
    y = torch.stack([TOKENS[i+1:i+SEQ_LEN+1] for i in ix])
    return x.to(DEVICE), y.to(DEVICE)

def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

def prime_factors(n):
    factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    return factors

def train_config(d_model, num_heads, seed=42):
    torch.manual_seed(seed)
    model = MiniGPT(VOCAB_SIZE, d_model, num_heads, num_layers=2, seq_len=SEQ_LEN).to(DEVICE)
    n_params = model.count_params()
    opt = Adam(model.parameters(), lr=LR)

    losses = {}
    t0 = time.time()
    for step in range(1, TRAIN_STEPS + 1):
        x, y = get_batch()
        logits = model(x)
        loss = F.cross_entropy(logits.view(-1, VOCAB_SIZE), y.view(-1))
        opt.zero_grad()
        loss.backward()
        opt.step()
        if step % 100 == 0:
            losses[step] = loss.item()

    wall = time.time() - t0
    return {
        'd_model': d_model,
        'num_heads': num_heads,
        'head_dim': d_model // num_heads,
        'n_params': n_params,
        'final_loss': losses[TRAIN_STEPS],
        'wall_time': wall,
        'losses': losses,
        'head_dim_is_pow2': is_power_of_2(d_model // num_heads),
        'head_dim_prime_factors': len(prime_factors(d_model // num_heads)),
    }

# ─── Experiment ───────────────────────────────────────────────────────────────

print("=" * 80)
print("H-EE-7: Head-Dim Diversity Improves Attention")
print("=" * 80)
print()

# d=120 configs: all divisors that give head_dim >= 4
d120_heads = [h for h in range(1, 121) if 120 % h == 0 and 120 // h >= 4 and h >= 4 and h <= 30]
# d=128 configs: all divisors
d128_heads = [h for h in range(1, 129) if 128 % h == 0 and 128 // h >= 4 and h >= 4 and h <= 32]

print(f"d=120 configs (num_heads): {d120_heads}")
print(f"  -> head_dims: {[120//h for h in d120_heads]}")
print(f"d=128 configs (num_heads): {d128_heads}")
print(f"  -> head_dims: {[128//h for h in d128_heads]}")
print()

# Run all configs with 2 seeds
NUM_SEEDS = 2
all_results = []

print("Training d=120 configurations...")
for nh in d120_heads:
    seed_losses = []
    for seed in range(NUM_SEEDS):
        r = train_config(120, nh, seed=42+seed)
        seed_losses.append(r['final_loss'])
    avg = sum(seed_losses) / NUM_SEEDS
    r['final_loss'] = avg
    r['std_loss'] = (sum((l - avg)**2 for l in seed_losses) / NUM_SEEDS) ** 0.5
    all_results.append(r)
    print(f"  heads={nh:>3}  head_dim={120//nh:>3}  pow2={'Y' if r['head_dim_is_pow2'] else 'N'}  loss={avg:.4f} +/- {r['std_loss']:.4f}")

print()
print("Training d=128 configurations...")
for nh in d128_heads:
    seed_losses = []
    for seed in range(NUM_SEEDS):
        r = train_config(128, nh, seed=42+seed)
        seed_losses.append(r['final_loss'])
    avg = sum(seed_losses) / NUM_SEEDS
    r['final_loss'] = avg
    r['std_loss'] = (sum((l - avg)**2 for l in seed_losses) / NUM_SEEDS) ** 0.5
    all_results.append(r)
    print(f"  heads={nh:>3}  head_dim={128//nh:>3}  pow2={'Y' if r['head_dim_is_pow2'] else 'N'}  loss={avg:.4f} +/- {r['std_loss']:.4f}")

# ─── Results table ────────────────────────────────────────────────────────────

print()
print("=" * 80)
print("FULL RESULTS TABLE")
print("=" * 80)
print()

print(f"| {'d':>4} | {'heads':>5} | {'h_dim':>5} | {'pow2':>4} | {'pf':>2} | {'Params':>8} | {'Loss':>8} | {'Std':>7} |")
print("|" + "-"*6 + "|" + "-"*7 + "|" + "-"*7 + "|" + "-"*6 + "|" + "-"*4 + "|" + "-"*10 + "|" + "-"*10 + "|" + "-"*9 + "|")

for r in sorted(all_results, key=lambda x: (x['d_model'], x['final_loss'])):
    print(f"| {r['d_model']:>4} | {r['num_heads']:>5} | {r['head_dim']:>5} | {'Y' if r['head_dim_is_pow2'] else 'N':>4} | {r['head_dim_prime_factors']:>2} | {r['n_params']:>8,} | {r['final_loss']:>8.4f} | {r.get('std_loss', 0):>7.4f} |")

# ─── Analysis: pow2 vs non-pow2 head dims ────────────────────────────────────

print()
print("=" * 80)
print("ANALYSIS: Power-of-2 vs Non-Power-of-2 Head Dims")
print("=" * 80)
print()

# d=120 only (has both types)
d120_results = [r for r in all_results if r['d_model'] == 120]
pow2_results = [r for r in d120_results if r['head_dim_is_pow2']]
nonpow2_results = [r for r in d120_results if not r['head_dim_is_pow2']]

if pow2_results:
    avg_pow2 = sum(r['final_loss'] for r in pow2_results) / len(pow2_results)
    best_pow2 = min(pow2_results, key=lambda r: r['final_loss'])
    print(f"  d=120, pow2 head_dims:     avg_loss={avg_pow2:.4f}  best={best_pow2['final_loss']:.4f} (h_dim={best_pow2['head_dim']})")

if nonpow2_results:
    avg_nonpow2 = sum(r['final_loss'] for r in nonpow2_results) / len(nonpow2_results)
    best_nonpow2 = min(nonpow2_results, key=lambda r: r['final_loss'])
    print(f"  d=120, non-pow2 head_dims: avg_loss={avg_nonpow2:.4f}  best={best_nonpow2['final_loss']:.4f} (h_dim={best_nonpow2['head_dim']})")

if pow2_results and nonpow2_results:
    delta = avg_nonpow2 - avg_pow2
    print(f"  Delta (non-pow2 - pow2):   {delta:+.4f}  ({'non-pow2 better' if delta < 0 else 'pow2 better'})")

# Best overall for each d
print()
best_120 = min(d120_results, key=lambda r: r['final_loss'])
d128_results = [r for r in all_results if r['d_model'] == 128]
best_128 = min(d128_results, key=lambda r: r['final_loss'])

print(f"  Best d=120: heads={best_120['num_heads']} h_dim={best_120['head_dim']} loss={best_120['final_loss']:.4f} pow2={'Y' if best_120['head_dim_is_pow2'] else 'N'}")
print(f"  Best d=128: heads={best_128['num_heads']} h_dim={best_128['head_dim']} loss={best_128['final_loss']:.4f} pow2={'Y' if best_128['head_dim_is_pow2'] else 'N'}")
print(f"  Cross-dimension winner: {'d=120' if best_120['final_loss'] < best_128['final_loss'] else 'd=128'} ({best_120['final_loss']:.4f} vs {best_128['final_loss']:.4f})")

# ─── ASCII bar chart ──────────────────────────────────────────────────────────

print()
print("=" * 80)
print("ASCII BAR CHART: Loss by head_dim (d=120)")
print("=" * 80)
print()

d120_sorted = sorted(d120_results, key=lambda r: r['head_dim'])
max_loss = max(r['final_loss'] for r in d120_sorted)
min_loss = min(r['final_loss'] for r in d120_sorted)

for r in d120_sorted:
    bar_len = int((r['final_loss'] - min_loss) / (max_loss - min_loss + 1e-9) * 40)
    base_bar = int(min_loss / max_loss * 40)
    marker = '*' if not r['head_dim_is_pow2'] else '#'
    p2_tag = "     " if r['head_dim_is_pow2'] else " <--N"
    print(f"  h_dim={r['head_dim']:>3} |{'=' * (base_bar + bar_len)}{marker} {r['final_loss']:.4f}{p2_tag}")

print()
print("  # = power-of-2 head_dim    * = non-power-of-2 head_dim    N = non-pow2")

# ─── Convergence comparison ───────────────────────────────────────────────────

print()
print("=" * 80)
print("CONVERGENCE: Best d=120 config vs Best d=128 config")
print("=" * 80)
print()

print(f"| {'Step':>6} | {'d=120 best':>12} | {'d=128 best':>12} | {'Delta':>8} |")
print("|" + "-"*8 + "|" + "-"*14 + "|" + "-"*14 + "|" + "-"*10 + "|")
for step in [100, 200, 300, 400]:
    l120 = best_120['losses'].get(step, float('nan'))
    l128 = best_128['losses'].get(step, float('nan'))
    d = l120 - l128
    print(f"| {step:>6} | {l120:>12.4f} | {l128:>12.4f} | {d:>+8.4f} |")

# ─── Verdict ──────────────────────────────────────────────────────────────────

print()
print("=" * 80)
print("VERDICT")
print("=" * 80)
print()

if pow2_results and nonpow2_results:
    if avg_nonpow2 < avg_pow2 - 0.005:
        grade = "SUPPORTED"
        detail = "Non-power-of-2 head dims show lower average loss"
    elif abs(avg_nonpow2 - avg_pow2) < 0.005:
        grade = "PARTIALLY SUPPORTED"
        detail = "Non-pow2 head dims are competitive; diversity provides options"
    else:
        grade = "NOT SUPPORTED"
        detail = "Power-of-2 head dims perform at least as well"
else:
    grade = "INCONCLUSIVE"
    detail = "Insufficient data for comparison"

n_configs_120 = len(d120_heads)
n_configs_128 = len(d128_heads)

print(f"  H-EE-7 Grade: {grade}")
print(f"  Detail: {detail}")
print()
print(f"  d=120 allows {n_configs_120} head configs vs d=128 with {n_configs_128} configs")
print(f"  This {n_configs_120/n_configs_128:.1f}x config diversity is the main practical advantage")
print(f"  Best d=120 head_dim: {best_120['head_dim']} (pow2={'Y' if best_120['head_dim_is_pow2'] else 'N'})")
print()
print("=" * 80)
print("END H-EE-7")
print("=" * 80)
