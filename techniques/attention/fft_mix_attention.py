#!/usr/bin/env python3
"""
H-SEDI-EE-3: Windowed FFT as Learned Attention Replacement
============================================================
Hypothesis: Replace self-attention (O(n^2)) with windowed FFT mixing (O(n log n))
at HCN window sizes {6, 12, 24, 36} for faster inference with comparable quality.

SEDI connection: SEDI uses windowed FFT at these specific sizes to capture
multi-scale structure. Same principle applied to sequence mixing in transformers.

Test plan:
  1. Build tiny transformer with self-attention (sequence classification on MNIST)
  2. Build FFT-mixer variant: replace attention with windowed FFT at sizes 6,12,24
  3. Compare: accuracy, training time, parameter count
  4. Ablate: which window sizes matter most
"""

import sys
sys.path.insert(0, '/Users/ghost/Dev/TECS-L')

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import math
import time

from model_utils import load_mnist

torch.manual_seed(42)
np.random.seed(42)

SEQ_LEN = 28  # Treat 28x28 MNIST as 28 tokens of dim 28
DIM = 28


# ─── Self-Attention Block ───────────────────────────────────────────────────

class SelfAttentionBlock(nn.Module):
    def __init__(self, dim, n_heads=4):
        super().__init__()
        self.attn = nn.MultiheadAttention(dim, n_heads, batch_first=True)
        self.norm = nn.LayerNorm(dim)
        self.ff = nn.Sequential(
            nn.Linear(dim, dim * 2),
            nn.GELU(),
            nn.Linear(dim * 2, dim),
        )
        self.norm2 = nn.LayerNorm(dim)

    def forward(self, x):
        # x: (B, seq_len, dim)
        h = self.norm(x)
        h, _ = self.attn(h, h, h)
        x = x + h
        x = x + self.ff(self.norm2(x))
        return x


# ─── Windowed FFT Mixer Block ───────────────────────────────────────────────

class WindowedFFTMixer(nn.Module):
    """Replace attention with windowed FFT at multiple scales.

    For each window size w:
      1. Split sequence into windows of size w
      2. Apply FFT along window dimension
      3. Apply learned filter (element-wise multiply in frequency domain)
      4. Inverse FFT
    Concatenate multi-scale outputs.
    """
    def __init__(self, dim, window_sizes=[6, 12, 24]):
        super().__init__()
        self.window_sizes = [w for w in window_sizes if w <= SEQ_LEN]
        self.norm = nn.LayerNorm(dim)

        # Learned frequency-domain filters for each window size
        self.filters = nn.ParameterList()
        for w in self.window_sizes:
            freq_dim = w // 2 + 1  # rfft output size
            self.filters.append(nn.Parameter(torch.randn(freq_dim, dim) * 0.02))

        # Projection to combine multi-scale outputs
        self.proj = nn.Linear(dim * len(self.window_sizes), dim)

        self.ff = nn.Sequential(
            nn.Linear(dim, dim * 2),
            nn.GELU(),
            nn.Linear(dim * 2, dim),
        )
        self.norm2 = nn.LayerNorm(dim)

    def forward(self, x):
        # x: (B, seq_len, dim)
        B, L, D = x.shape
        h = self.norm(x)

        outputs = []
        for i, w in enumerate(self.window_sizes):
            # Pad sequence to multiple of window size
            pad_len = (w - L % w) % w
            if pad_len > 0:
                h_padded = F.pad(h, (0, 0, 0, pad_len))
            else:
                h_padded = h

            # Reshape into windows: (B, n_windows, w, D)
            n_windows = h_padded.size(1) // w
            windowed = h_padded.reshape(B, n_windows, w, D)

            # FFT along window dimension
            freq = torch.fft.rfft(windowed, dim=2)  # (B, n_windows, w//2+1, D)

            # Apply learned filter
            filtered = freq * self.filters[i].unsqueeze(0).unsqueeze(0)

            # Inverse FFT
            mixed = torch.fft.irfft(filtered, n=w, dim=2)  # (B, n_windows, w, D)

            # Reshape back
            mixed = mixed.reshape(B, -1, D)[:, :L, :]  # (B, L, D)
            outputs.append(mixed)

        # Combine multi-scale
        combined = torch.cat(outputs, dim=-1)  # (B, L, D * n_scales)
        mixed = self.proj(combined)  # (B, L, D)

        x = x + mixed
        x = x + self.ff(self.norm2(x))
        return x


# ─── Model wrappers ─────────────────────────────────────────────────────────

class SequenceClassifier(nn.Module):
    def __init__(self, block, n_layers=2, dim=DIM, n_classes=10):
        super().__init__()
        self.pos_emb = nn.Parameter(torch.randn(1, SEQ_LEN, dim) * 0.02)
        self.layers = nn.ModuleList([block() for _ in range(n_layers)])
        self.head = nn.Linear(dim, n_classes)

    def forward(self, x):
        # x: (B, 784) → (B, 28, 28)
        x = x.view(-1, SEQ_LEN, DIM) + self.pos_emb
        for layer in self.layers:
            x = layer(x)
        x = x.mean(dim=1)  # global average pooling
        return self.head(x)


def train_model(model, train_loader, test_loader, epochs=10, lr=0.001):
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()

    epoch_data = []
    t_start = time.time()

    for epoch in range(epochs):
        model.train()
        total_loss = 0
        for X, y in train_loader:
            X = X.view(X.size(0), -1)
            optimizer.zero_grad()
            out = model(X)
            loss = criterion(out, y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        avg_loss = total_loss / len(train_loader)

        model.eval()
        correct = total = 0
        with torch.no_grad():
            for X, y in test_loader:
                X = X.view(X.size(0), -1)
                out = model(X)
                correct += (out.argmax(1) == y).sum().item()
                total += y.size(0)
        acc = correct / total

        epoch_data.append({'epoch': epoch+1, 'loss': avg_loss, 'acc': acc})

    total_time = time.time() - t_start
    return epoch_data, total_time


def main():
    print("=" * 70)
    print("  H-SEDI-EE-3: Windowed FFT vs Self-Attention")
    print("=" * 70)

    EPOCHS = 10
    N_LAYERS = 2

    train_loader, test_loader = load_mnist(batch_size=64)

    configs = {
        'SelfAttn(4head)': lambda: SelfAttentionBlock(DIM, n_heads=4),
        'FFT-Mix(6,12,24)': lambda: WindowedFFTMixer(DIM, [6, 12, 24]),
        'FFT-Mix(6,12)': lambda: WindowedFFTMixer(DIM, [6, 12]),
        'FFT-Mix(6)': lambda: WindowedFFTMixer(DIM, [6]),
        'FFT-Mix(12)': lambda: WindowedFFTMixer(DIM, [12]),
        'FFT-Mix(24)': lambda: WindowedFFTMixer(DIM, [24]),
    }

    results = {}

    for name, block_fn in configs.items():
        print(f"\n  Training: {name} ({N_LAYERS} layers, {EPOCHS} epochs)...")
        model = SequenceClassifier(block_fn, n_layers=N_LAYERS)
        params = sum(p.numel() for p in model.parameters())

        epoch_data, train_time = train_model(model, train_loader, test_loader, epochs=EPOCHS)
        final_acc = epoch_data[-1]['acc']
        final_loss = epoch_data[-1]['loss']

        results[name] = {
            'acc': final_acc, 'loss': final_loss,
            'params': params, 'time': train_time,
            'time_per_epoch': train_time / EPOCHS,
            'epoch_data': epoch_data,
        }

        print(f"    {name}: Acc={final_acc*100:.2f}%, Params={params:,}, "
              f"Time={train_time:.1f}s ({train_time/EPOCHS:.1f}s/epoch)")

    # ─── Results ─────────────────────────────────────────────────────────────

    attn_acc = results['SelfAttn(4head)']['acc']
    attn_time = results['SelfAttn(4head)']['time_per_epoch']
    attn_params = results['SelfAttn(4head)']['params']

    print("\n" + "=" * 90)
    print("  COMPARISON TABLE")
    print("=" * 90)
    print(f"  {'Model':<20} | {'Acc%':>6} | {'Params':>8} | {'Time/ep':>8} | "
          f"{'Speedup':>8} | {'Param Save':>10} | {'vs Attn':>8}")
    print("-" * 90)

    for name, r in sorted(results.items(), key=lambda x: -x[1]['acc']):
        speedup = attn_time / r['time_per_epoch'] if r['time_per_epoch'] > 0 else 0
        param_save = (1 - r['params'] / attn_params) * 100
        acc_diff = (r['acc'] - attn_acc) * 100
        marker = ' <--' if r['acc'] == max(v['acc'] for v in results.values()) else ''
        print(f"  {name:<20} | {r['acc']*100:>5.2f}% | {r['params']:>8,} | "
              f"{r['time_per_epoch']:>7.1f}s | {speedup:>7.2f}x | "
              f"{param_save:>+9.1f}% | {acc_diff:>+7.2f}%{marker}")

    # ─── Learning curves ────────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("  LEARNING CURVES (Accuracy %)")
    print("=" * 70)
    header = f"  {'Epoch':>5}"
    for name in ['SelfAttn(4head)', 'FFT-Mix(6,12,24)', 'FFT-Mix(6)', 'FFT-Mix(12)']:
        header += f" | {name:>18}"
    print(header)
    print("-" * 90)

    for ep in range(EPOCHS):
        row = f"  {ep+1:>5}"
        for name in ['SelfAttn(4head)', 'FFT-Mix(6,12,24)', 'FFT-Mix(6)', 'FFT-Mix(12)']:
            if name in results:
                acc = results[name]['epoch_data'][ep]['acc'] * 100
                row += f" | {acc:>17.2f}%"
        print(row)

    # ─── Verdict ─────────────────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("  VERDICT")
    print("=" * 70)

    best_fft = None
    for name, r in results.items():
        if 'FFT' in name:
            if (attn_acc - r['acc']) < 0.02:  # within 2%
                if best_fft is None or r['time_per_epoch'] < results[best_fft]['time_per_epoch']:
                    best_fft = name

    if best_fft:
        r = results[best_fft]
        speedup = attn_time / r['time_per_epoch']
        print(f"  SUPPORTED: Windowed FFT can replace attention!")
        print(f"  Best: {best_fft}")
        print(f"  Accuracy: {r['acc']*100:.2f}% (attention: {attn_acc*100:.2f}%)")
        print(f"  Speed: {speedup:.2f}x faster per epoch")
        print(f"  Complexity: O(n log n) vs O(n^2)")
    else:
        print(f"  NOT SUPPORTED: FFT mixers lose >2% accuracy vs attention")
        print(f"  Attention Acc: {attn_acc*100:.2f}%")
        best_fft_acc = max((r['acc'] for n, r in results.items() if 'FFT' in n), default=0)
        print(f"  Best FFT Acc: {best_fft_acc*100:.2f}%")
        print(f"  Note: On small MNIST sequences (L=28), attention overhead is minimal")
        print(f"  FFT advantage expected to grow with longer sequences")

    print("=" * 70)


if __name__ == '__main__':
    main()
