"""
H-EE-9: Phi-bottleneck + Phi6Simple activation recovery test
=============================================================
Hypothesis: Replacing GELU with Phi6Simple in phi-bottleneck FFN compensates
the ~4.8% loss increase from reduced FFN width.

Test: 4 configs (2x2 factorial):
  A. Standard FFN (4x) + GELU
  B. Standard FFN (4x) + Phi6Simple
  C. Phi-bottleneck (4/3x) + GELU
  D. Phi-bottleneck (4/3x) + Phi6Simple

Architecture: 4-layer char-level transformer, d_model=128, 4 heads
Task: Next-char prediction on structured text
Steps: 500
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
    "Consciousness emerges from the interplay of deficit plasticity and inhibition. "
    "The golden zone lies between one half and one half minus log four thirds."
)
TEXT = (BASE_TEXT + " ") * 200
chars = sorted(set(TEXT))
vocab_size = len(chars)
c2i = {c: i for i, c in enumerate(chars)}
data = torch.tensor([c2i[c] for c in TEXT], dtype=torch.long)

# --- Hyperparameters ---
D_MODEL  = 128
N_HEADS  = 4
N_LAYERS = 4
SEQ_LEN  = 64
BATCH    = 16
STEPS    = 500
LR       = 3e-3

PHI6 = 2
D_FF_STANDARD = 4 * D_MODEL          # 512
D_FF_PHI      = round(4 * D_MODEL * PHI6 / 6)  # 171 (4/3 expansion)

# --- Activation functions ---
class Phi6Simple(nn.Module):
    """x^2 - x + 1, clamped to [-2, 2]"""
    def forward(self, x):
        xc = torch.clamp(x, -2.0, 2.0)
        return xc * xc - xc + 1.0

class GELUAct(nn.Module):
    def forward(self, x):
        return F.gelu(x)

# --- Model components ---
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
    return total, ffn

def get_batch():
    ix = torch.randint(len(data) - SEQ_LEN - 1, (BATCH,))
    x = torch.stack([data[i:i+SEQ_LEN] for i in ix])
    y = torch.stack([data[i+1:i+SEQ_LEN+1] for i in ix])
    return x, y

def train_config(label, d_ff, activation):
    torch.manual_seed(SEED)
    model = CharLM(vocab_size, D_MODEL, N_HEADS, N_LAYERS, d_ff, SEQ_LEN, activation)
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
        "label": label,
        "d_ff": d_ff,
        "total_params": total_params,
        "ffn_params": ffn_params,
        "final_loss": final_loss,
        "perplexity": math.exp(final_loss),
        "train_time": elapsed,
        "loss_history": loss_history,
    }

# --- Run 2x2 factorial ---
print("=" * 70)
print("H-EE-9: Phi-bottleneck + Phi6Simple Recovery Test")
print("=" * 70)

configs = [
    ("A: Standard+GELU",       D_FF_STANDARD, GELUAct()),
    ("B: Standard+Phi6Simple", D_FF_STANDARD, Phi6Simple()),
    ("C: PhiBot+GELU",        D_FF_PHI,      GELUAct()),
    ("D: PhiBot+Phi6Simple",  D_FF_PHI,      Phi6Simple()),
]

results = []
for label, d_ff, act in configs:
    print(f"\nTraining {label} (d_ff={d_ff})...", flush=True)
    r = train_config(label, d_ff, act)
    results.append(r)
    print(f"  Loss={r['final_loss']:.4f}  PPL={r['perplexity']:.2f}  Params={r['total_params']:,}  FFN={r['ffn_params']:,}  Time={r['train_time']:.1f}s")

# --- Results table ---
print("\n" + "=" * 70)
print("RESULTS TABLE")
print("=" * 70)
print(f"\n| Config | d_ff | Total Params | FFN Params | Loss | PPL | Time(s) |")
print(f"|--------|------|-------------|------------|------|-----|---------|")
for r in results:
    print(f"| {r['label']} | {r['d_ff']} | {r['total_params']:,} | {r['ffn_params']:,} | {r['final_loss']:.4f} | {r['perplexity']:.2f} | {r['train_time']:.1f} |")

# --- Analysis ---
base = results[0]['final_loss']
print(f"\n--- Loss relative to baseline (A: Standard+GELU) ---")
for r in results:
    delta_pct = (r['final_loss'] - base) / base * 100
    print(f"  {r['label']:30s}: {delta_pct:+.2f}%")

# Check recovery: does D recover loss compared to C?
loss_C = results[2]['final_loss']
loss_D = results[3]['final_loss']
recovery = (loss_C - loss_D) / (loss_C - base) * 100 if loss_C != base else 0
print(f"\n--- Recovery Analysis ---")
print(f"  PhiBot+GELU loss gap vs baseline: {(loss_C - base)/base*100:+.2f}%")
print(f"  PhiBot+Phi6Simple loss gap vs baseline: {(loss_D - base)/base*100:+.2f}%")
print(f"  Recovery by adding Phi6Simple: {recovery:.1f}%")
if loss_D <= base * 1.02:
    print(f"  VERDICT: Phi6Simple FULLY compensates phi-bottleneck loss (within 2%)")
elif loss_D < loss_C:
    print(f"  VERDICT: Phi6Simple PARTIALLY compensates phi-bottleneck loss")
else:
    print(f"  VERDICT: Phi6Simple does NOT help compensate phi-bottleneck loss")

# Param savings
param_savings = (results[0]['total_params'] - results[3]['total_params']) / results[0]['total_params'] * 100
print(f"\n  Param savings (D vs A): {param_savings:.1f}%")
print(f"  Quality-adjusted efficiency = loss_A / loss_D * param_savings = {base / loss_D * param_savings:.1f}%")

# Learning curves (sampled)
print(f"\n--- Learning Curves (every 50 steps) ---")
print(f"| Step | {'  |  '.join(r['label'][:20] for r in results)} |")
print(f"|------|" + "|".join(["------" for _ in results]) + "|")
for step in range(49, STEPS, 50):
    vals = "  |  ".join(f"{r['loss_history'][step]:.4f}" for r in results)
    print(f"| {step+1:4d} | {vals} |")

print("\nDone.")
