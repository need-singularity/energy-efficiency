"""
H-EE-10: Phi-bottleneck + MoE (more experts, smaller each)
===========================================================
Hypothesis: Using 1/3 expansion per expert but 3x more experts gives
same total params but better routing / specialization.

Configs:
  A. Standard MoE: 8 experts, d_ff=4*d_model (top-2)
  B. Phi MoE:     24 experts, d_ff=4/3*d_model (top-2)
  C. Dense baseline: single FFN, d_ff=4*d_model (no MoE)

Architecture: 4-layer transformer, d_model=64, 4 heads, 500 steps
Task: Character-level LM on structured text
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
VOCAB = len(chars)
c2i = {c: i for i, c in enumerate(chars)}
data = torch.tensor([c2i[c] for c in TEXT], dtype=torch.long)

SEQ_LEN = 32
BATCH = 16
D_MODEL = 64
N_HEADS = 4
N_LAYERS = 4
STEPS = 500
LR = 1e-3
TOP_K = 2

PHI6 = 2
D_FF_STD = 4 * D_MODEL             # 256
D_FF_PHI = round(4 * D_MODEL * PHI6 / 6)  # 43

N_EXPERTS_STD = 8
N_EXPERTS_PHI = 24

class MultiHeadSelfAttention(nn.Module):
    def __init__(self, d_model, n_heads):
        super().__init__()
        self.n_heads = n_heads
        self.d_head = d_model // n_heads
        self.qkv = nn.Linear(d_model, 3 * d_model)
        self.proj = nn.Linear(d_model, d_model)
    def forward(self, x):
        B, T, C = x.shape
        qkv = self.qkv(x).reshape(B, T, 3, self.n_heads, self.d_head).permute(2, 0, 3, 1, 4)
        q, k, v = qkv[0], qkv[1], qkv[2]
        attn = (q @ k.transpose(-2, -1)) / math.sqrt(self.d_head)
        mask = torch.tril(torch.ones(T, T, device=x.device)).bool()
        attn = attn.masked_fill(~mask, float('-inf'))
        attn = F.softmax(attn, dim=-1)
        out = (attn @ v).transpose(1, 2).reshape(B, T, C)
        return self.proj(out)

class ExpertFFN(nn.Module):
    def __init__(self, d_model, d_ff):
        super().__init__()
        self.fc1 = nn.Linear(d_model, d_ff)
        self.fc2 = nn.Linear(d_ff, d_model)
    def forward(self, x):
        return self.fc2(F.gelu(self.fc1(x)))

class MoELayer(nn.Module):
    def __init__(self, d_model, d_ff, n_experts, top_k):
        super().__init__()
        self.n_experts = n_experts
        self.top_k = top_k
        self.experts = nn.ModuleList([ExpertFFN(d_model, d_ff) for _ in range(n_experts)])
        self.gate = nn.Linear(d_model, n_experts)
    def forward(self, x):
        B, T, C = x.shape
        x_flat = x.reshape(-1, C)
        gate_logits = self.gate(x_flat)
        gate_scores = F.softmax(gate_logits, dim=-1)
        topk_scores, topk_indices = torch.topk(gate_scores, self.top_k, dim=-1)
        topk_scores = topk_scores / topk_scores.sum(dim=-1, keepdim=True)
        out = torch.zeros_like(x_flat)
        for k in range(self.top_k):
            for e in range(self.n_experts):
                mask = (topk_indices[:, k] == e)
                if mask.any():
                    expert_input = x_flat[mask]
                    expert_output = self.experts[e](expert_input)
                    out[mask] += topk_scores[mask, k:k+1] * expert_output
        return out.reshape(B, T, C)

class DenseFFN(nn.Module):
    def __init__(self, d_model, d_ff):
        super().__init__()
        self.fc1 = nn.Linear(d_model, d_ff)
        self.fc2 = nn.Linear(d_ff, d_model)
    def forward(self, x):
        return self.fc2(F.gelu(self.fc1(x)))

class TransformerBlock(nn.Module):
    def __init__(self, d_model, n_heads, ffn_module):
        super().__init__()
        self.attn = MultiHeadSelfAttention(d_model, n_heads)
        self.ln1 = nn.LayerNorm(d_model)
        self.ln2 = nn.LayerNorm(d_model)
        self.ffn = ffn_module
    def forward(self, x):
        x = x + self.attn(self.ln1(x))
        x = x + self.ffn(self.ln2(x))
        return x

class SmallTransformer(nn.Module):
    def __init__(self, vocab, d_model, n_heads, n_layers, ffn_builder):
        super().__init__()
        self.embed = nn.Embedding(vocab, d_model)
        self.pos_embed = nn.Embedding(SEQ_LEN, d_model)
        self.blocks = nn.ModuleList([
            TransformerBlock(d_model, n_heads, ffn_builder(i)) for i in range(n_layers)
        ])
        self.ln_f = nn.LayerNorm(d_model)
        self.head = nn.Linear(d_model, vocab, bias=False)
    def forward(self, idx):
        B, T = idx.shape
        pos = torch.arange(T, device=idx.device).unsqueeze(0)
        x = self.embed(idx) + self.pos_embed(pos)
        for block in self.blocks:
            x = block(x)
        x = self.ln_f(x)
        return self.head(x)

def count_params(model):
    return sum(p.numel() for p in model.parameters())

def get_batch():
    ix = torch.randint(len(data) - SEQ_LEN - 1, (BATCH,))
    x = torch.stack([data[i:i+SEQ_LEN] for i in ix])
    y = torch.stack([data[i+1:i+SEQ_LEN+1] for i in ix])
    return x, y

def train(name, ffn_builder):
    torch.manual_seed(SEED)
    model = SmallTransformer(VOCAB, D_MODEL, N_HEADS, N_LAYERS, ffn_builder)
    optimizer = torch.optim.AdamW(model.parameters(), lr=LR)
    n_params = count_params(model)
    losses = []
    t0 = time.time()
    for step in range(1, STEPS + 1):
        x, y = get_batch()
        logits = model(x)
        loss = F.cross_entropy(logits.reshape(-1, VOCAB), y.reshape(-1))
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        losses.append(loss.item())
    elapsed = time.time() - t0
    final_loss = sum(losses[-50:]) / 50
    return {
        'name': name,
        'n_params': n_params,
        'final_loss': final_loss,
        'ppl': math.exp(final_loss),
        'elapsed': elapsed,
        'losses': losses,
    }

# --- Builders ---
def std_moe_builder(i):
    return MoELayer(D_MODEL, D_FF_STD, N_EXPERTS_STD, TOP_K)

def phi_moe_builder(i):
    return MoELayer(D_MODEL, D_FF_PHI, N_EXPERTS_PHI, TOP_K)

def dense_builder(i):
    return DenseFFN(D_MODEL, D_FF_STD)

# --- Run ---
print("=" * 70)
print("H-EE-10: Phi-bottleneck MoE (more experts, smaller each)")
print(f"  Text vocab: {VOCAB}, Text length: {len(data)}")
print("=" * 70)

configs = [
    (f"A: Std MoE ({N_EXPERTS_STD}exp x d_ff={D_FF_STD})", std_moe_builder),
    (f"B: Phi MoE ({N_EXPERTS_PHI}exp x d_ff={D_FF_PHI})", phi_moe_builder),
    ("C: Dense (no MoE)", dense_builder),
]

results = []
for name, builder in configs:
    print(f"\nTraining {name}...", flush=True)
    r = train(name, builder)
    results.append(r)
    print(f"  Loss={r['final_loss']:.4f}  PPL={r['ppl']:.2f}  Params={r['n_params']:,}  Time={r['elapsed']:.1f}s")

# --- Results ---
print("\n" + "=" * 70)
print("RESULTS TABLE")
print("=" * 70)
print(f"\n| Config | Total Params | Final Loss | PPL | Time(s) |")
print(f"|--------|-------------|------------|-----|---------|")
for r in results:
    print(f"| {r['name']} | {r['n_params']:,} | {r['final_loss']:.4f} | {r['ppl']:.2f} | {r['elapsed']:.1f} |")

# Active params per token
std_active = 2 * (D_MODEL * D_FF_STD + D_FF_STD * D_MODEL) + D_MODEL * N_EXPERTS_STD
phi_active = 2 * (D_MODEL * D_FF_PHI + D_FF_PHI * D_MODEL) + D_MODEL * N_EXPERTS_PHI
print(f"\n--- Active Params per Token (per MoE layer) ---")
print(f"  Std MoE (top-2 of {N_EXPERTS_STD}): {std_active:,}")
print(f"  Phi MoE (top-2 of {N_EXPERTS_PHI}): {phi_active:,}")
print(f"  Ratio: {phi_active/std_active:.3f}")

base_loss = results[2]['final_loss']
for r in results:
    delta = (r['final_loss'] - base_loss) / base_loss * 100
    print(f"  {r['name']:50s}: {delta:+.2f}% vs dense")

phi_vs_std = (results[1]['final_loss'] - results[0]['final_loss']) / results[0]['final_loss'] * 100
print(f"\n  Phi MoE vs Std MoE: {phi_vs_std:+.2f}%")
if phi_vs_std <= 0:
    print(f"  VERDICT: Phi MoE matches or beats Std MoE with more routing diversity!")
elif phi_vs_std < 5:
    print(f"  VERDICT: Phi MoE slightly worse, but may have routing advantages")
else:
    print(f"  VERDICT: Phi MoE underperforms — fewer params per expert hurts")

# Loss curves
print(f"\n--- Loss Curves (every 50 steps) ---")
print(f"| Step | " + " | ".join(r['name'][:30] for r in results) + " |")
print(f"|------|" + "|".join(["--------" for _ in results]) + "|")
for step in range(49, STEPS, 50):
    vals = " | ".join(f"{r['losses'][step]:.4f}" for r in results)
    print(f"| {step+1:4d} | {vals} |")

print("\nDone.")
