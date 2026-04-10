"""
H-EE-11: Full Combined Architecture
====================================
Hypothesis: d_model=120 (HCN) + Phi6Simple + phi-bottleneck + 8 heads (head_dim=15)
gives >40% savings with minimal quality loss.

Configs:
  A. Standard: d=128, GELU, 4x FFN, 8 heads (head_dim=16)
  B. Combined: d=120, Phi6Simple, 4/3x FFN, 8 heads (head_dim=15)
  C. Partial:  d=120, GELU, 4x FFN, 8 heads (only HCN dimension)
  D. Partial:  d=128, Phi6Simple, 4/3x FFN, 8 heads (only activation+bottleneck)

Architecture: 4-layer transformer, char-level LM, 500 steps
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

N_HEADS  = 8
N_LAYERS = 4
SEQ_LEN  = 64
BATCH    = 16
STEPS    = 500
LR       = 3e-3

PHI6 = 2

class Phi6Simple(nn.Module):
    def forward(self, x):
        xc = torch.clamp(x, -2.0, 2.0)
        return xc * xc - xc + 1.0

class GELUAct(nn.Module):
    def forward(self, x):
        return F.gelu(x)

class FFN(nn.Module):
    def __init__(self, d_model, d_ff, activation):
        super().__init__()
        self.fc1 = nn.Linear(d_model, d_ff)
        self.act = activation
        self.fc2 = nn.Linear(d_ff, d_model)
    def forward(self, x):
        return self.fc2(self.act(self.fc1(x)))

class TransformerBlock(nn.Module):
    def __init__(self, d_model, n_heads, d_ff, activation):
        super().__init__()
        self.attn = nn.MultiheadAttention(d_model, n_heads, batch_first=True)
        self.ffn  = FFN(d_model, d_ff, activation)
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
    def __init__(self, vocab_size, d_model, n_heads, n_layers, d_ff, seq_len, activation):
        super().__init__()
        self.emb = nn.Embedding(vocab_size, d_model)
        self.pos = nn.Embedding(seq_len, d_model)
        self.blocks = nn.ModuleList(
            [TransformerBlock(d_model, n_heads, d_ff, activation) for _ in range(n_layers)]
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
    attn = sum(p.numel() for blk in model.blocks for p in blk.attn.parameters())
    return total, ffn, attn

def get_batch():
    ix = torch.randint(len(data) - SEQ_LEN - 1, (BATCH,))
    x = torch.stack([data[i:i+SEQ_LEN] for i in ix])
    y = torch.stack([data[i+1:i+SEQ_LEN+1] for i in ix])
    return x, y

def estimate_flops_per_step(d_model, d_ff, n_heads, n_layers, seq_len, batch):
    """Rough FLOPs estimate per training step (forward only)."""
    # Attention: 4 * seq^2 * d per layer
    attn_flops = 4 * seq_len * seq_len * d_model * n_layers
    # FFN: 2 * seq * d * d_ff per layer (up + down projections)
    ffn_flops = 2 * seq_len * d_model * d_ff * 2 * n_layers
    return (attn_flops + ffn_flops) * batch

def train_config(label, d_model, d_ff, activation):
    torch.manual_seed(SEED)
    model = CharLM(vocab_size, d_model, N_HEADS, N_LAYERS, d_ff, SEQ_LEN, activation)
    opt = torch.optim.Adam(model.parameters(), lr=LR)
    total_params, ffn_params, attn_params = count_params(model)
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
    flops = estimate_flops_per_step(d_model, d_ff, N_HEADS, N_LAYERS, SEQ_LEN, BATCH)
    return {
        "label": label,
        "d_model": d_model,
        "d_ff": d_ff,
        "total_params": total_params,
        "ffn_params": ffn_params,
        "attn_params": attn_params,
        "final_loss": final_loss,
        "perplexity": math.exp(final_loss),
        "train_time": elapsed,
        "flops_per_step": flops,
        "loss_history": loss_history,
    }

# --- Configs ---
print("=" * 70)
print("H-EE-11: Full Combined Architecture Test")
print("=" * 70)

configs = [
    ("A: Standard (d=128,GELU,4x)", 128, 4*128, GELUAct()),
    ("B: Combined (d=120,Phi6,4/3x)", 120, round(4*120*PHI6/6), Phi6Simple()),
    ("C: HCN-only (d=120,GELU,4x)", 120, 4*120, GELUAct()),
    ("D: Act+Bot (d=128,Phi6,4/3x)", 128, round(4*128*PHI6/6), Phi6Simple()),
]

results = []
for label, d_model, d_ff, act in configs:
    print(f"\nTraining {label} (d_model={d_model}, d_ff={d_ff})...", flush=True)
    r = train_config(label, d_model, d_ff, act)
    results.append(r)
    print(f"  Loss={r['final_loss']:.4f}  PPL={r['perplexity']:.2f}  Params={r['total_params']:,}  Time={r['train_time']:.1f}s")

# --- Results ---
print("\n" + "=" * 70)
print("RESULTS TABLE")
print("=" * 70)
print(f"\n| Config | d_model | d_ff | Total Params | FFN Params | Attn Params | Loss | PPL | FLOPs/step | Time(s) |")
print(f"|--------|---------|------|-------------|------------|-------------|------|-----|------------|---------|")
for r in results:
    print(f"| {r['label']} | {r['d_model']} | {r['d_ff']} | {r['total_params']:,} | {r['ffn_params']:,} | {r['attn_params']:,} | {r['final_loss']:.4f} | {r['perplexity']:.2f} | {r['flops_per_step']:,} | {r['train_time']:.1f} |")

# --- Savings Analysis ---
base = results[0]
print(f"\n--- Savings vs Standard (A) ---")
print(f"| Config | Param Savings | FLOP Savings | Loss Delta | Quality-Adjusted |")
print(f"|--------|-------------- |------------- |----------- |-----------------|")
for r in results[1:]:
    param_save = (base['total_params'] - r['total_params']) / base['total_params'] * 100
    flop_save = (base['flops_per_step'] - r['flops_per_step']) / base['flops_per_step'] * 100
    loss_delta = (r['final_loss'] - base['final_loss']) / base['final_loss'] * 100
    # Quality-adjusted: savings * (1 - loss_penalty)
    qa = param_save * max(0, 1 - abs(loss_delta)/100)
    print(f"| {r['label']} | {param_save:.1f}% | {flop_save:.1f}% | {loss_delta:+.2f}% | {qa:.1f}% |")

# Check >40% savings with minimal loss
combined = results[1]
param_save_combined = (base['total_params'] - combined['total_params']) / base['total_params'] * 100
loss_delta_combined = (combined['final_loss'] - base['final_loss']) / base['final_loss'] * 100
print(f"\n--- Combined Architecture Verdict ---")
print(f"  Param savings: {param_save_combined:.1f}%")
print(f"  Loss delta: {loss_delta_combined:+.2f}%")
if param_save_combined > 40 and abs(loss_delta_combined) < 5:
    print(f"  VERDICT: >40% savings with <5% loss delta — HYPOTHESIS CONFIRMED")
elif param_save_combined > 40:
    print(f"  VERDICT: >40% savings but {loss_delta_combined:+.1f}% loss — PARTIAL (quality tradeoff)")
else:
    print(f"  VERDICT: Only {param_save_combined:.1f}% savings — HYPOTHESIS REJECTED")

# Memory estimate
print(f"\n--- Memory Estimate (fp32, params only) ---")
for r in results:
    mem_mb = r['total_params'] * 4 / (1024 * 1024)
    print(f"  {r['label']}: {mem_mb:.2f} MB")

# Learning curves
print(f"\n--- Learning Curves (every 50 steps) ---")
header = " | ".join(r['label'][:25] for r in results)
print(f"| Step | {header} |")
print(f"|------|" + "|".join(["-------" for _ in results]) + "|")
for step in range(49, STEPS, 50):
    vals = " | ".join(f"{r['loss_history'][step]:.4f}" for r in results)
    print(f"| {step+1:4d} | {vals} |")

print("\nDone.")
