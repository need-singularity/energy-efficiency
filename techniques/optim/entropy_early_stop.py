#!/usr/bin/env python3
"""
H-SEDI-EE-1: SEDI Entropy Test as Early Stopping Criterion
============================================================
Hypothesis: Monitoring Shannon entropy H(output) of model's softmax output
during training reveals a stabilization plateau. Stopping at this plateau
saves training energy without losing accuracy.

SEDI connection: SEDI uses normalized entropy to detect structure in signals.
Same principle applied to training dynamics — when output distribution's
entropy stabilizes, the model has "found structure" and further training
yields diminishing returns.

Test plan:
  1. Train PureFieldEngine on MNIST for 30 epochs
  2. Compute H(softmax(output)) per epoch on validation set
  3. Detect plateau: when delta_H < threshold for N consecutive epochs
  4. Compare: accuracy at plateau vs final accuracy
  5. Measure: how many epochs saved (energy proxy)
"""

import sys
sys.path.insert(0, '/Users/ghost/Dev/TECS-L')

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import math
import time

from model_pure_field import PureFieldEngine
from model_utils import load_mnist

torch.manual_seed(42)
np.random.seed(42)

# ─── Entropy computation (SEDI-inspired) ────────────────────────────────────

def compute_output_entropy(model, loader, flatten=True):
    """Compute mean Shannon entropy of softmax output distribution."""
    model.eval()
    all_entropy = []
    with torch.no_grad():
        for X, y in loader:
            if flatten:
                X = X.view(X.size(0), -1)
            out = model(X)
            if isinstance(out, tuple):
                out = out[0]
            probs = F.softmax(out, dim=-1)
            # H = -sum(p * log(p)), handle log(0)
            log_probs = torch.log(probs + 1e-10)
            entropy = -(probs * log_probs).sum(dim=-1)
            all_entropy.append(entropy)
    all_entropy = torch.cat(all_entropy)
    return all_entropy.mean().item(), all_entropy.std().item()


def detect_plateau(entropies, window=3, threshold=0.01):
    """Detect when entropy stabilizes: delta_H < threshold for `window` consecutive epochs."""
    if len(entropies) < window + 1:
        return None
    for i in range(window, len(entropies)):
        deltas = [abs(entropies[j] - entropies[j-1]) for j in range(i - window + 1, i + 1)]
        if all(d < threshold for d in deltas):
            return i - window  # plateau started at this epoch
    return None


# ─── Main experiment ─────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("  H-SEDI-EE-1: SEDI Entropy-Based Early Stopping")
    print("=" * 70)

    MAX_EPOCHS = 30
    THRESHOLDS = [0.005, 0.01, 0.02, 0.05]
    WINDOW = 3

    train_loader, test_loader = load_mnist(batch_size=128)

    model = PureFieldEngine(784, 128, 10)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()
    n_params = sum(p.numel() for p in model.parameters())
    print(f"\n  Model: PureFieldEngine, Parameters: {n_params:,}")
    print(f"  Training for {MAX_EPOCHS} epochs, monitoring entropy\n")

    # Training loop with entropy tracking
    epoch_data = []
    t_start = time.time()

    for epoch in range(MAX_EPOCHS):
        model.train()
        total_loss = 0
        for X, y in train_loader:
            X = X.view(X.size(0), -1)
            optimizer.zero_grad()
            out, tension = model(X)
            loss = criterion(out, y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        avg_loss = total_loss / len(train_loader)

        # Evaluate accuracy
        model.eval()
        correct = total = 0
        with torch.no_grad():
            for X, y in test_loader:
                X = X.view(X.size(0), -1)
                out, _ = model(X)
                correct += (out.argmax(1) == y).sum().item()
                total += y.size(0)
        acc = correct / total

        # Compute entropy
        h_mean, h_std = compute_output_entropy(model, test_loader)

        epoch_data.append({
            'epoch': epoch + 1,
            'loss': avg_loss,
            'acc': acc,
            'entropy': h_mean,
            'entropy_std': h_std,
            'time': time.time() - t_start,
        })

        if (epoch + 1) % 5 == 0 or epoch == 0:
            print(f"    Epoch {epoch+1:>2}/{MAX_EPOCHS}: Loss={avg_loss:.4f}, "
                  f"Acc={acc*100:.1f}%, H={h_mean:.4f} +/- {h_std:.4f}")

    total_time = time.time() - t_start

    # ─── Analysis ────────────────────────────────────────────────────────────

    entropies = [d['entropy'] for d in epoch_data]
    accs = [d['acc'] for d in epoch_data]
    final_acc = accs[-1]

    print("\n" + "=" * 70)
    print("  ENTROPY TRAJECTORY")
    print("=" * 70)
    print(f"  {'Epoch':>5} | {'Loss':>8} | {'Acc%':>6} | {'H(out)':>8} | {'dH':>8} | {'Bar'}")
    print("-" * 70)

    for i, d in enumerate(epoch_data):
        dh = abs(d['entropy'] - epoch_data[i-1]['entropy']) if i > 0 else 0.0
        bar_len = int(d['entropy'] * 20)
        bar = '#' * bar_len
        print(f"  {d['epoch']:>5} | {d['loss']:>8.4f} | {d['acc']*100:>5.1f}% | "
              f"{d['entropy']:>8.4f} | {dh:>8.4f} | {bar}")

    # ─── Plateau detection for multiple thresholds ───────────────────────────

    print("\n" + "=" * 70)
    print("  EARLY STOPPING ANALYSIS")
    print("=" * 70)
    print(f"  {'Threshold':>10} | {'Plateau Epoch':>13} | {'Acc@Plateau':>11} | "
          f"{'Final Acc':>9} | {'Acc Drop':>8} | {'Epochs Saved':>12} | {'Energy Saved':>12}")
    print("-" * 95)

    results = {}
    for thresh in THRESHOLDS:
        plateau_epoch = detect_plateau(entropies, window=WINDOW, threshold=thresh)
        if plateau_epoch is not None:
            plateau_acc = accs[plateau_epoch]
            acc_drop = final_acc - plateau_acc
            epochs_saved = MAX_EPOCHS - (plateau_epoch + 1)
            energy_saved = epochs_saved / MAX_EPOCHS * 100
        else:
            plateau_acc = final_acc
            acc_drop = 0
            epochs_saved = 0
            energy_saved = 0
            plateau_epoch = MAX_EPOCHS - 1

        results[thresh] = {
            'plateau_epoch': plateau_epoch + 1,
            'plateau_acc': plateau_acc,
            'acc_drop': acc_drop,
            'epochs_saved': epochs_saved,
            'energy_saved': energy_saved,
        }

        print(f"  {thresh:>10.3f} | {plateau_epoch+1:>13} | {plateau_acc*100:>10.2f}% | "
              f"{final_acc*100:>8.2f}% | {acc_drop*100:>7.2f}% | {epochs_saved:>12} | "
              f"{energy_saved:>11.1f}%")

    # ─── Verdict ─────────────────────────────────────────────────────────────

    print("\n" + "=" * 70)
    print("  VERDICT")
    print("=" * 70)

    # Find best threshold: most energy saved with <0.5% accuracy drop
    best = None
    for thresh, r in results.items():
        if abs(r['acc_drop']) < 0.005 and r['epochs_saved'] > 0:
            if best is None or r['epochs_saved'] > results[best]['epochs_saved']:
                best = thresh

    if best is not None:
        r = results[best]
        print(f"  SUPPORTED: Entropy early stopping works!")
        print(f"  Best threshold: {best}")
        print(f"  Stop at epoch {r['plateau_epoch']} instead of {MAX_EPOCHS}")
        print(f"  Accuracy drop: {r['acc_drop']*100:.2f}% (< 0.5%)")
        print(f"  Energy saved: {r['energy_saved']:.1f}%")
        print(f"  Total training time: {total_time:.1f}s")
        print(f"  Estimated time saved: {total_time * r['epochs_saved'] / MAX_EPOCHS:.1f}s")
    else:
        # Check if any threshold saves energy with <1% drop
        relaxed_best = None
        for thresh, r in results.items():
            if abs(r['acc_drop']) < 0.01 and r['epochs_saved'] > 0:
                if relaxed_best is None or r['epochs_saved'] > results[relaxed_best]['epochs_saved']:
                    relaxed_best = thresh
        if relaxed_best:
            r = results[relaxed_best]
            print(f"  WEAKLY SUPPORTED: Entropy early stopping works with relaxed threshold")
            print(f"  Best threshold: {relaxed_best}, Stop at epoch {r['plateau_epoch']}")
            print(f"  Accuracy drop: {r['acc_drop']*100:.2f}%, Energy saved: {r['energy_saved']:.1f}%")
        else:
            print(f"  NOT SUPPORTED: No threshold achieves energy savings with <1% accuracy drop")
            print(f"  Entropy may not plateau early enough for this model/dataset combination")

    print("=" * 70)


if __name__ == '__main__':
    main()
