#!/usr/bin/env python3
"""
BT-54 Verification: AdamW β₂ Optimality Test
=============================================
Tests P-21: β₂=0.95 = 1-1/(J₂-τ) vs β₂=0.999 (original Adam default)

Hypothesis: β₂=0.95 achieves lower final loss than β₂=0.999 for
transformer training, confirming the n=6 arithmetic value as optimal.

Setup: Small transformer on synthetic sequence prediction task.
3 seeds × 5 β₂ values = 15 runs.
"""

import torch
import torch.nn as nn
import math
import time
import json

# ─── n=6 constants ───
SIGMA = 12
PHI = 2
TAU = 4
SOPFR = 5
J2 = 24
MU = 1

# β₂ candidates
BETA2_VALUES = [0.9, 0.95, 0.99, 0.999, 0.9999]
BETA1 = 0.9  # = 1 - 1/(σ-φ), universal
WEIGHT_DECAY = 0.1  # = 1/(σ-φ), universal
SEEDS = [42, 137, 256]

# Architecture: small n=6-aligned transformer
D_MODEL = 128  # 2^(σ-sopfr) = d_head universal
N_HEADS = 4    # τ
N_LAYERS = 2   # φ
D_FFN = int(D_MODEL * 8/3)  # SwiGLU ratio (σ-τ)/(n/φ)
SEQ_LEN = 64   # 2^n
VOCAB = 256    # 2^(σ-τ)
BATCH = 32
STEPS = 2000
LR = 3e-4      # (n/φ)·10^(-τ)


class SmallTransformer(nn.Module):
    def __init__(self):
        super().__init__()
        self.embed = nn.Embedding(VOCAB, D_MODEL)
        self.pos = nn.Embedding(SEQ_LEN, D_MODEL)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=D_MODEL, nhead=N_HEADS,
            dim_feedforward=D_FFN, dropout=0.0,
            activation='gelu', batch_first=True
        )
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=N_LAYERS)
        self.head = nn.Linear(D_MODEL, VOCAB)

    def forward(self, x):
        B, T = x.shape
        pos = torch.arange(T, device=x.device).unsqueeze(0)
        h = self.embed(x) + self.pos(pos)
        mask = nn.Transformer.generate_square_subsequent_mask(T, device=x.device)
        h = self.encoder(h, mask=mask)
        return self.head(h)


def generate_data(batch_size, seq_len, device):
    """Structured sequence: repeating patterns with noise."""
    base = torch.randint(0, VOCAB, (batch_size, seq_len // 4), device=device)
    data = base.repeat(1, 4)
    noise_mask = torch.rand_like(data.float()) < 0.1
    noise = torch.randint(0, VOCAB, data.shape, device=device)
    data = torch.where(noise_mask, noise, data)
    return data


def train_one(beta2, seed, device):
    torch.manual_seed(seed)
    model = SmallTransformer().to(device)
    opt = torch.optim.AdamW(
        model.parameters(),
        lr=LR,
        betas=(BETA1, beta2),
        eps=1e-8,       # 10^{-(σ-τ)}
        weight_decay=WEIGHT_DECAY
    )
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=STEPS, eta_min=LR/10)
    criterion = nn.CrossEntropyLoss()

    losses = []
    for step in range(STEPS):
        data = generate_data(BATCH, SEQ_LEN, device)
        inp, tgt = data[:, :-1], data[:, 1:]

        logits = model(inp)
        loss = criterion(logits.reshape(-1, VOCAB), tgt.reshape(-1))

        opt.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)  # R(6) = 1.0
        opt.step()
        scheduler.step()

        if step % 100 == 0 or step == STEPS - 1:
            losses.append((step, loss.item()))

    final_loss = sum(l for _, l in losses[-5:]) / 5  # average last 500 steps
    return final_loss, losses


def main():
    device = 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'
    print(f"Device: {device}")
    print(f"BT-54 Verification: AdamW β₂ Optimality")
    print(f"β₁={BETA1}, wd={WEIGHT_DECAY}, ε=1e-8, clip=1.0")
    print(f"β₂ candidates: {BETA2_VALUES}")
    print(f"Seeds: {SEEDS}")
    print(f"Architecture: d={D_MODEL}, h={N_HEADS}, L={N_LAYERS}, ffn={D_FFN}")
    print("=" * 70)

    results = {}
    for beta2 in BETA2_VALUES:
        seed_losses = []
        for seed in SEEDS:
            t0 = time.time()
            final_loss, trace = train_one(beta2, seed, device)
            dt = time.time() - t0
            seed_losses.append(final_loss)
            print(f"  β₂={beta2:.4f}, seed={seed}: final_loss={final_loss:.4f} ({dt:.1f}s)")
        avg = sum(seed_losses) / len(seed_losses)
        std = (sum((l - avg)**2 for l in seed_losses) / len(seed_losses)) ** 0.5
        results[str(beta2)] = {
            'mean': avg,
            'std': std,
            'seeds': seed_losses
        }
        print(f"  β₂={beta2:.4f} → mean={avg:.4f} ± {std:.4f}")
        print()

    # Rank by mean loss
    ranked = sorted(results.items(), key=lambda x: x[1]['mean'])
    print("=" * 70)
    print("RANKING (lower loss = better):")
    for i, (b2, r) in enumerate(ranked):
        marker = " ← n=6 prediction" if b2 == "0.95" else ""
        winner = " ★ BEST" if i == 0 else ""
        print(f"  #{i+1}: β₂={b2} → {r['mean']:.4f} ± {r['std']:.4f}{marker}{winner}")

    # Verdict
    best_b2 = ranked[0][0]
    n6_rank = [i for i, (b, _) in enumerate(ranked) if b == "0.95"][0] + 1
    print()
    if best_b2 == "0.95":
        print("✅ P-21 CONFIRMED: β₂=0.95 = 1-1/(J₂-τ) is OPTIMAL")
    elif n6_rank <= 2:
        print(f"⚠️ P-21 CLOSE: β₂=0.95 ranked #{n6_rank}/5 (best: β₂={best_b2})")
    else:
        print(f"❌ P-21 FALSIFIED: β₂=0.95 ranked #{n6_rank}/5 (best: β₂={best_b2})")

    # Save results
    with open('experiments/bt54_results.json', 'w') as f:
        json.dump({
            'experiment': 'BT-54 AdamW β₂ Optimality',
            'prediction': 'P-21',
            'n6_value': '0.95 = 1-1/(J₂-τ)',
            'results': results,
            'ranking': [(b, r['mean']) for b, r in ranked],
            'verdict': 'CONFIRMED' if best_b2 == '0.95' else f'RANK_{n6_rank}'
        }, f, indent=2)
    print("\nResults saved to experiments/bt54_results.json")


if __name__ == '__main__':
    main()
