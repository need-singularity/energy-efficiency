"""
H-EE-13: Energy Savings Scale with Model Depth
===============================================
Hypothesis: Deeper models benefit MORE from Phi6Simple
(more activation layers = more cumulative savings).

Test: GELU vs Phi6Simple at depth 2, 4, 6, 8 layers
Measure: loss, training time, time-per-step

Architecture: transformer, d_model=64, 4 heads, d_ff=256, 500 steps
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
D_FF = 4 * D_MODEL  # 256
STEPS = 500
LR = 1e-3

DEPTHS = [2, 4, 6, 8]

class Phi6Simple(nn.Module):
    def forward(self, x):
        xc = torch.clamp(x, -2.0, 2.0)
        return xc * xc - xc + 1.0

class GELUAct(nn.Module):
    def forward(self, x):
        return F.gelu(x)

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
        self.attn = MultiHeadSelfAttention(d_model, n_heads)
        self.ln1 = nn.LayerNorm(d_model)
        self.ln2 = nn.LayerNorm(d_model)
        self.ffn = FFN(d_model, d_ff, activation)
    def forward(self, x):
        x = x + self.attn(self.ln1(x))
        x = x + self.ffn(self.ln2(x))
        return x

class SmallTransformer(nn.Module):
    def __init__(self, vocab, d_model, n_heads, n_layers, d_ff, activation):
        super().__init__()
        self.embed = nn.Embedding(vocab, d_model)
        self.pos_embed = nn.Embedding(SEQ_LEN, d_model)
        self.blocks = nn.ModuleList([
            TransformerBlock(d_model, n_heads, d_ff, activation) for _ in range(n_layers)
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

def train(name, n_layers, activation):
    torch.manual_seed(SEED)
    model = SmallTransformer(VOCAB, D_MODEL, N_HEADS, n_layers, D_FF, activation)
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
        'depth': n_layers,
        'n_params': n_params,
        'final_loss': final_loss,
        'ppl': math.exp(final_loss),
        'elapsed': elapsed,
        'time_per_step': elapsed / STEPS,
        'losses': losses,
    }

# --- Run ---
print("=" * 70)
print("H-EE-13: Activation Energy Savings vs Model Depth")
print(f"  Text vocab: {VOCAB}, Text length: {len(data)}")
print("=" * 70)

gelu_results = []
phi6_results = []

for depth in DEPTHS:
    print(f"\n--- Depth {depth} ---")
    print(f"  Training GELU...", flush=True)
    rg = train(f"GELU-d{depth}", depth, GELUAct())
    gelu_results.append(rg)
    print(f"    Loss={rg['final_loss']:.4f}  PPL={rg['ppl']:.2f}  Time={rg['elapsed']:.1f}s  Params={rg['n_params']:,}")

    print(f"  Training Phi6Simple...", flush=True)
    rp = train(f"Phi6-d{depth}", depth, Phi6Simple())
    phi6_results.append(rp)
    print(f"    Loss={rp['final_loss']:.4f}  PPL={rp['ppl']:.2f}  Time={rp['elapsed']:.1f}s  Params={rp['n_params']:,}")

# --- Results Table ---
print("\n" + "=" * 70)
print("RESULTS TABLE")
print("=" * 70)
print(f"\n| Depth | GELU Loss | Phi6 Loss | Loss Delta(%) | GELU Time/step | Phi6 Time/step | Speed Delta(%) | Params |")
print(f"|-------|-----------|-----------|---------------|---------------|---------------|---------------|--------|")
for i, depth in enumerate(DEPTHS):
    rg = gelu_results[i]
    rp = phi6_results[i]
    loss_delta = (rp['final_loss'] - rg['final_loss']) / rg['final_loss'] * 100
    speed_delta = (rg['time_per_step'] - rp['time_per_step']) / rg['time_per_step'] * 100
    print(f"| {depth} | {rg['final_loss']:.4f} | {rp['final_loss']:.4f} | {loss_delta:+.2f}% | {rg['time_per_step']*1000:.1f}ms | {rp['time_per_step']*1000:.1f}ms | {speed_delta:+.1f}% | {rg['n_params']:,} |")

# --- Scaling Analysis ---
print(f"\n--- Scaling Analysis ---")
loss_deltas = []
speed_deltas = []
for i, depth in enumerate(DEPTHS):
    rg = gelu_results[i]
    rp = phi6_results[i]
    ld = (rp['final_loss'] - rg['final_loss']) / rg['final_loss'] * 100
    sd = (rg['time_per_step'] - rp['time_per_step']) / rg['time_per_step'] * 100
    loss_deltas.append(ld)
    speed_deltas.append(sd)

print(f"\n  Speed savings by depth:")
for i, depth in enumerate(DEPTHS):
    bar_len = max(0, int(speed_deltas[i] * 2))
    bar = '#' * bar_len if speed_deltas[i] > 0 else '-' * min(abs(int(speed_deltas[i] * 2)), 40)
    print(f"    Depth {depth}: {speed_deltas[i]:+.1f}% |{bar}")

print(f"\n  Loss delta by depth (negative = Phi6Simple better):")
for i, depth in enumerate(DEPTHS):
    bar_len = min(abs(int(loss_deltas[i] * 2)), 40)
    sign = '+' if loss_deltas[i] > 0 else '-'
    bar = sign * bar_len
    print(f"    Depth {depth}: {loss_deltas[i]:+.2f}% |{bar}")

if len(speed_deltas) >= 2:
    trend = speed_deltas[-1] - speed_deltas[0]
    print(f"\n  Speed savings trend (d={DEPTHS[0]} to d={DEPTHS[-1]}): {trend:+.1f}% change")
    if trend > 1:
        print(f"  VERDICT: Deeper models benefit MORE from Phi6Simple -- HYPOTHESIS CONFIRMED")
    elif trend > -1:
        print(f"  VERDICT: Benefits roughly constant with depth -- HYPOTHESIS NEUTRAL")
    else:
        print(f"  VERDICT: Deeper models benefit LESS -- HYPOTHESIS REJECTED")

if len(loss_deltas) >= 2:
    loss_trend = loss_deltas[-1] - loss_deltas[0]
    print(f"  Loss penalty trend: {loss_trend:+.2f}%")
    if loss_trend < -2:
        print(f"  NOTE: Loss penalty DECREASES with depth (Phi6Simple learns better at depth)")
    elif loss_trend > 2:
        print(f"  NOTE: Loss penalty INCREASES with depth (Phi6Simple degrades at depth)")
    else:
        print(f"  NOTE: Loss penalty roughly constant across depths")

# ASCII graph
print(f"\n--- ASCII Graph: Loss Comparison ---")
for i, depth in enumerate(DEPTHS):
    rg = gelu_results[i]
    rp = phi6_results[i]
    g_bar = '#' * max(1, int(rg['final_loss'] * 20))
    p_bar = '=' * max(1, int(rp['final_loss'] * 20))
    print(f"  d={depth:2d} GELU [{rg['final_loss']:.4f}] {g_bar}")
    print(f"       Phi6 [{rp['final_loss']:.4f}] {p_bar}")

# Learning curves for deepest
print(f"\n--- Learning Curves: Depth {DEPTHS[-1]} ---")
rg = gelu_results[-1]
rp = phi6_results[-1]
print(f"| Step | GELU | Phi6Simple |")
print(f"|------|------|------------|")
for step in range(49, STEPS, 50):
    print(f"| {step+1:4d} | {rg['losses'][step]:.4f} | {rp['losses'][step]:.4f} |")

print("\nDone.")
