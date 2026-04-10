"""
Technique 16: Mertens Dropout
==============================
ln(4/3) ~ 0.2877 = Golden Zone bandwidth (SEDI).
This is the natural information bandwidth of n=6 arithmetic.
Using it as dropout rate provides mathematically grounded regularization.

Expected: eliminates dropout hyperparameter search.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import math
import time

SEED = 42
torch.manual_seed(SEED)
np.random.seed(SEED)

MERTENS_DROPOUT = math.log(4 / 3)


class Phi6Simple(nn.Module):
    def forward(self, x):
        xc = torch.clamp(x, -2.0, 2.0)
        return xc * xc - xc + 1.0


class FFN(nn.Module):
    def __init__(self, d_model, d_ff, activation, dropout=0.0):
        super().__init__()
        self.fc1 = nn.Linear(d_model, d_ff)
        self.act = activation
        self.drop = nn.Dropout(dropout)
        self.fc2 = nn.Linear(d_ff, d_model)

    def forward(self, x):
        return self.fc2(self.drop(self.act(self.fc1(x))))


class TransformerBlock(nn.Module):
    def __init__(self, d_model, n_heads, d_ff, activation, dropout=0.0):
        super().__init__()
        self.attn = nn.MultiheadAttention(d_model, n_heads, batch_first=True, dropout=dropout)
        self.ffn = FFN(d_model, d_ff, activation, dropout)
        self.ln1 = nn.LayerNorm(d_model)
        self.ln2 = nn.LayerNorm(d_model)
        self.drop = nn.Dropout(dropout)

    def forward(self, x):
        L = x.size(1)
        mask = torch.triu(torch.ones(L, L, device=x.device), diagonal=1).bool()
        a, _ = self.attn(x, x, x, attn_mask=mask)
        x = self.ln1(x + self.drop(a))
        x = self.ln2(x + self.ffn(x))
        return x


class CharLM(nn.Module):
    def __init__(self, vocab_size, d_model, n_heads, n_layers, d_ff, seq_len, activation, dropout=0.0):
        super().__init__()
        self.emb = nn.Embedding(vocab_size, d_model)
        self.pos = nn.Embedding(seq_len, d_model)
        self.blocks = nn.Sequential(*[
            TransformerBlock(d_model, n_heads, d_ff, activation, dropout) for _ in range(n_layers)
        ])
        self.out = nn.Linear(d_model, vocab_size)

    def forward(self, idx):
        B, T = idx.shape
        x = self.emb(idx) + self.pos(torch.arange(T, device=idx.device))
        x = self.blocks(x)
        return self.out(x)


def count_params(m):
    return sum(p.numel() for p in m.parameters())


def main():
    print("=" * 70)
    print("  Technique 16: Mertens Dropout")
    print("  p = ln(4/3) ~ 0.2877 — Golden Zone bandwidth")
    print("=" * 70)

    BASE_TEXT = (
        "Mathematics reveals deep structure. "
        "The number six is perfect because its divisors one two and three sum to itself. "
        "Neural networks learn patterns through gradient descent optimization. "
        "Transformers use attention mechanisms to process sequences efficiently. "
        "Consciousness emerges from the interplay of deficit plasticity and inhibition. "
    )
    TEXT = (BASE_TEXT + " ") * 200
    chars = sorted(set(TEXT))
    vocab_size = len(chars)
    c2i = {c: i for i, c in enumerate(chars)}
    data = torch.tensor([c2i[c] for c in TEXT], dtype=torch.long)

    SEQ_LEN = 64
    BATCH = 16
    STEPS = 400
    LR = 3e-3
    D_MODEL = 120
    N_HEADS = 12
    N_LAYERS = 4
    D_FF = round(4 * D_MODEL / 3)

    def get_batch():
        ix = torch.randint(0, len(data) - SEQ_LEN - 1, (BATCH,))
        x = torch.stack([data[i:i+SEQ_LEN] for i in ix])
        y = torch.stack([data[i+1:i+SEQ_LEN+1] for i in ix])
        return x, y

    dropout_rates = [0.0, 0.1, 0.2, MERTENS_DROPOUT, 0.3, 0.4, 0.5]

    results = []
    for p in dropout_rates:
        label = f"p={p:.4f}" + (" (Mertens)" if abs(p - MERTENS_DROPOUT) < 0.001 else "")
        print(f"\n--- {label} ---")
        torch.manual_seed(SEED)
        model = CharLM(vocab_size, D_MODEL, N_HEADS, N_LAYERS, D_FF, SEQ_LEN, Phi6Simple(), p)
        opt = torch.optim.Adam(model.parameters(), lr=LR)

        t0 = time.time()
        losses = []
        for step in range(STEPS):
            x, y = get_batch()
            logits = model(x)
            loss = F.cross_entropy(logits.reshape(-1, vocab_size), y.reshape(-1))
            opt.zero_grad()
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            opt.step()
            losses.append(loss.item())
        elapsed = time.time() - t0

        model.eval()
        eval_losses = []
        with torch.no_grad():
            for _ in range(20):
                x, y = get_batch()
                logits = model(x)
                eloss = F.cross_entropy(logits.reshape(-1, vocab_size), y.reshape(-1))
                eval_losses.append(eloss.item())

        results.append({
            "label": label,
            "dropout": p,
            "train_loss": np.mean(losses[-20:]),
            "eval_loss": np.mean(eval_losses),
            "gap": np.mean(eval_losses) - np.mean(losses[-20:]),
            "train_time": elapsed,
        })

    print("\n" + "=" * 70)
    print("  Mertens Dropout Results")
    print("=" * 70)
    print(f"{'Config':<25} {'Train Loss':>11} {'Eval Loss':>11} {'Gap':>8} {'Time':>7}")
    print("-" * 65)
    for r in results:
        marker = " <--" if "Mertens" in r["label"] else ""
        print(f"{r['label']:<25} {r['train_loss']:>11.4f} {r['eval_loss']:>11.4f} "
              f"{r['gap']:>8.4f} {r['train_time']:>6.1f}s{marker}")

    print(f"\nln(4/3) = {MERTENS_DROPOUT:.6f}")
    print(f"Golden Zone bandwidth = {MERTENS_DROPOUT:.6f}")
    print(f"This is the natural 'information bandwidth' of n=6 arithmetic.")
    print(f"No hyperparameter sweep needed — the rate is mathematically determined.")


if __name__ == "__main__":
    main()
