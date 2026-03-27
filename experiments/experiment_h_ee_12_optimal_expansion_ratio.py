"""
H-EE-12: Optimal FFN Expansion Ratio Sweep
============================================
Hypothesis: The optimal expansion ratio (minimizing loss * params) is in [1, 2],
and 4/3 ~ 1.33 is close to the Pareto optimum.

Test: Sweep expansion ratios: 1.0, 1.33, 1.5, 2.0, 3.0, 4.0
Plot Pareto frontier of (params, loss).

Architecture: 4-layer transformer, d_model=128, 4 heads, 500 steps
"""

import math
import time
import random
import torch
import torch.nn as nn
import torch.nn.functional as F

SEED = 42
random.seed(SEED)
torch.manual_seed(SEED)

# --- Text data ---
BASE_TEXT = (
    "Mathematics reveals deep structure. "
    "The number six is perfect because its divisors one two and three sum to itself. "
    "Neural networks learn patterns through gradient descent optimization. "
    "Transformers use attention mechanisms to process sequences efficiently. "
    "Consciousness emerges from the interplay of deficit plasticity and inhibition."
)
TEXT = (BASE_TEXT + " ") * 200
chars = sorted(set(TEXT))
vocab_size = len(chars)
c2i = {c: i for i, c in enumerate(chars)}
data = torch.tensor([c2i[c] for c in TEXT], dtype=torch.long)

D_MODEL  = 128
N_HEADS  = 4
N_LAYERS = 4
SEQ_LEN  = 64
BATCH    = 16
STEPS    = 500
LR       = 3e-3

# Expansion ratios to test
RATIOS = [1.0, 4/3, 1.5, 2.0, 3.0, 4.0]

class FFN(nn.Module):
    def __init__(self, d_model, d_ff):
        super().__init__()
        self.fc1 = nn.Linear(d_model, d_ff)
        self.fc2 = nn.Linear(d_ff, d_model)
    def forward(self, x):
        return self.fc2(F.gelu(self.fc1(x)))

class TransformerBlock(nn.Module):
    def __init__(self, d_model, n_heads, d_ff):
        super().__init__()
        self.attn = nn.MultiheadAttention(d_model, n_heads, batch_first=True)
        self.ffn  = FFN(d_model, d_ff)
        self.ln1  = nn.LayerNorm(d_model)
        self.ln2  = nn.LayerNorm(d_model)
    def forward(self, x):
        L = x.size(1)
        mask = torch.triu(torch.ones(L, L, device=x.device), diagonal=1).bool()
        a, _ = self.attn(x, x, x, attn_mask=mask)
        x = self.ln1(x + a)
        x = self.ln2(x + self.ffn(x))
        return x

class CharLM(nn.Module):
    def __init__(self, vocab_size, d_model, n_heads, n_layers, d_ff, seq_len):
        super().__init__()
        self.emb = nn.Embedding(vocab_size, d_model)
        self.pos = nn.Embedding(seq_len, d_model)
        self.blocks = nn.ModuleList(
            [TransformerBlock(d_model, n_heads, d_ff) for _ in range(n_layers)]
        )
        self.head = nn.Linear(d_model, vocab_size)
    def forward(self, idx):
        B, T = idx.shape
        x = self.emb(idx) + self.pos(torch.arange(T, device=idx.device))
        for blk in self.blocks:
            x = blk(x)
        return self.head(x)

def count_params(model):
    total = sum(p.numel() for p in model.parameters())
    ffn = sum(p.numel() for blk in model.blocks for p in blk.ffn.parameters())
    return total, ffn

def get_batch():
    ix = torch.randint(len(data) - SEQ_LEN - 1, (BATCH,))
    x = torch.stack([data[i:i+SEQ_LEN] for i in ix])
    y = torch.stack([data[i+1:i+SEQ_LEN+1] for i in ix])
    return x, y

def train_config(ratio):
    d_ff = round(ratio * D_MODEL)
    label = f"ratio={ratio:.2f} (d_ff={d_ff})"
    torch.manual_seed(SEED)
    model = CharLM(vocab_size, D_MODEL, N_HEADS, N_LAYERS, d_ff, SEQ_LEN)
    opt = torch.optim.Adam(model.parameters(), lr=LR)
    total_params, ffn_params = count_params(model)
    loss_history = []
    t0 = time.time()
    for step in range(STEPS):
        x, y = get_batch()
        logits = model(x)
        loss = F.cross_entropy(logits.reshape(-1, vocab_size), y.reshape(-1))
        opt.zero_grad()
        loss.backward()
        nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step()
        loss_history.append(loss.item())
    elapsed = time.time() - t0
    final_loss = sum(loss_history[-50:]) / 50
    return {
        "ratio": ratio,
        "d_ff": d_ff,
        "total_params": total_params,
        "ffn_params": ffn_params,
        "final_loss": final_loss,
        "perplexity": math.exp(final_loss),
        "train_time": elapsed,
        "loss_history": loss_history,
    }

# --- Run ---
print("=" * 70)
print("H-EE-12: Optimal FFN Expansion Ratio Sweep")
print("=" * 70)

results = []
for ratio in RATIOS:
    d_ff = round(ratio * D_MODEL)
    print(f"\nTraining ratio={ratio:.2f} (d_ff={d_ff})...", flush=True)
    r = train_config(ratio)
    results.append(r)
    print(f"  Loss={r['final_loss']:.4f}  PPL={r['perplexity']:.2f}  Params={r['total_params']:,}  Time={r['train_time']:.1f}s")

# --- Results Table ---
print("\n" + "=" * 70)
print("RESULTS TABLE")
print("=" * 70)
print(f"\n| Ratio | d_ff | Total Params | FFN Params | Loss | PPL | loss*params(M) | Time(s) |")
print(f"|-------|------|-------------|------------|------|-----|---------------|---------|")
for r in results:
    cost = r['final_loss'] * r['total_params'] / 1e6
    print(f"| {r['ratio']:.2f} | {r['d_ff']} | {r['total_params']:,} | {r['ffn_params']:,} | {r['final_loss']:.4f} | {r['perplexity']:.2f} | {cost:.4f} | {r['train_time']:.1f} |")

# --- Pareto Analysis ---
print(f"\n--- Pareto Frontier Analysis ---")
# Sort by params
sorted_r = sorted(results, key=lambda r: r['total_params'])
pareto = []
best_loss = float('inf')
for r in sorted_r:
    if r['final_loss'] < best_loss:
        pareto.append(r)
        best_loss = r['final_loss']

print(f"Pareto-optimal configs:")
for r in pareto:
    print(f"  ratio={r['ratio']:.2f}: params={r['total_params']:,}, loss={r['final_loss']:.4f}")

# --- loss*params metric (lower is better) ---
print(f"\n--- Efficiency Metric: loss * params ---")
costs = [(r['ratio'], r['final_loss'] * r['total_params'] / 1e6) for r in results]
costs.sort(key=lambda x: x[1])
print(f"  Best: ratio={costs[0][0]:.2f} (cost={costs[0][1]:.4f})")
print(f"  Worst: ratio={costs[-1][0]:.2f} (cost={costs[-1][1]:.4f})")
for ratio, cost in costs:
    print(f"  ratio={ratio:.2f}: cost={cost:.4f}")

# --- ASCII Pareto plot ---
print(f"\n--- Pareto Plot (Params vs Loss) ---")
print(f"  Loss")
max_loss = max(r['final_loss'] for r in results)
min_loss = min(r['final_loss'] for r in results)
min_params = min(r['total_params'] for r in results)
max_params = max(r['total_params'] for r in results)

HEIGHT = 15
WIDTH = 50
grid = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

for r in results:
    x = int((r['total_params'] - min_params) / max(1, max_params - min_params) * (WIDTH - 1))
    y = int((r['final_loss'] - min_loss) / max(0.001, max_loss - min_loss) * (HEIGHT - 1))
    y = HEIGHT - 1 - y  # flip
    x = min(x, WIDTH - 1)
    y = max(0, min(y, HEIGHT - 1))
    label = f"{r['ratio']:.1f}"
    for ci, ch in enumerate(label):
        if x + ci < WIDTH:
            grid[y][x + ci] = ch

for row_i, row in enumerate(grid):
    loss_val = max_loss - row_i * (max_loss - min_loss) / (HEIGHT - 1) if HEIGHT > 1 else min_loss
    print(f"  {loss_val:.3f} |{''.join(row)}|")
param_labels = f"  Params: {min_params:,}" + " " * (WIDTH - 20) + f"{max_params:,}"
print(f"        +{'-' * WIDTH}+")
print(param_labels)

# --- Check if 4/3 is near optimal ---
ratio_133 = next(r for r in results if abs(r['ratio'] - 4/3) < 0.01)
opt_cost = min(r['final_loss'] * r['total_params'] / 1e6 for r in results)
r133_cost = ratio_133['final_loss'] * ratio_133['total_params'] / 1e6
print(f"\n--- Is 4/3 near optimal? ---")
print(f"  4/3 cost: {r133_cost:.4f}")
print(f"  Best cost: {opt_cost:.4f}")
print(f"  Gap: {(r133_cost - opt_cost) / opt_cost * 100:.1f}%")
if (r133_cost - opt_cost) / opt_cost < 0.10:
    print(f"  VERDICT: 4/3 is within 10% of optimal — HYPOTHESIS CONFIRMED")
else:
    print(f"  VERDICT: 4/3 is NOT near optimal — HYPOTHESIS REJECTED")

# Learning curves
print(f"\n--- Learning Curves (every 100 steps) ---")
header = " | ".join(f"r={r['ratio']:.2f}" for r in results)
print(f"| Step | {header} |")
print(f"|------|" + "|".join(["--------" for _ in results]) + "|")
for step in range(99, STEPS, 100):
    vals = " | ".join(f"{r['loss_history'][step]:.4f}" for r in results)
    print(f"| {step+1:4d} | {vals} |")

print("\nDone.")
