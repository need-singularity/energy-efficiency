"""
H-EE-3: Phi6Simple Training Stability
=======================================
Hypothesis: Phi6Simple's bounded output [0.75, 7.0] prevents gradient explosion
without needing gradient clipping.

Test plan:
  1. Train GELU and Phi6Simple MLP on same task WITHOUT gradient clipping
  2. Train with deliberately high learning rates to provoke instability
  3. Measure: max gradient norm, gradient norm over time, NaN/Inf occurrences, loss spikes
  4. Compare stability metrics
"""

import numpy as np
import time
import sys

np.random.seed(42)

# ── Activations ──

def act_gelu(x):
    return 0.5 * x * (1.0 + np.tanh(0.7978845608028654 * (x + 0.044715 * x**3)))

def act_gelu_grad(x):
    c = 0.7978845608028654
    x3 = x**3
    t = np.tanh(c * (x + 0.044715 * x3))
    dt = 1.0 - t*t
    return 0.5 * (1.0 + t) + 0.5 * x * dt * c * (1.0 + 3 * 0.044715 * x**2)

def act_phi6(x):
    xc = np.clip(x, -2.0, 2.0)
    return xc * xc - xc + 1.0

def act_phi6_grad(x):
    mask = ((x >= -2.0) & (x <= 2.0)).astype(x.dtype)
    xc = np.clip(x, -2.0, 2.0)
    return mask * (2.0 * xc - 1.0)

def act_relu(x):
    return np.maximum(0.0, x)

def act_relu_grad(x):
    return (x > 0).astype(x.dtype)

def act_silu(x):
    sig = 1.0 / (1.0 + np.exp(-np.clip(x, -30, 30)))
    return x * sig

def act_silu_grad(x):
    sig = 1.0 / (1.0 + np.exp(-np.clip(x, -30, 30)))
    return sig + x * sig * (1.0 - sig)

ACTIVATIONS = {
    "GELU":   (act_gelu, act_gelu_grad),
    "ReLU":   (act_relu, act_relu_grad),
    "SiLU":   (act_silu, act_silu_grad),
    "Phi6":   (act_phi6, act_phi6_grad),
}


# ── MLP with gradient tracking ──

class MLP:
    def __init__(self, d_in, d_hidden, d_out, act_fwd, act_bwd, rng):
        scale = np.sqrt(2.0 / d_in)
        self.W1 = rng.standard_normal((d_in, d_hidden)).astype(np.float64) * scale
        self.b1 = np.zeros(d_hidden)
        self.W2 = rng.standard_normal((d_hidden, d_out)).astype(np.float64) * np.sqrt(2.0 / d_hidden)
        self.b2 = np.zeros(d_out)
        self.act_fwd = act_fwd
        self.act_bwd = act_bwd

    def forward(self, x):
        self._x = x
        self._h_pre = x @ self.W1 + self.b1
        self._h = self.act_fwd(self._h_pre)
        return self._h @ self.W2 + self.b2

    def backward(self, dout, lr, clip_norm=None):
        """Returns gradient norms before and after any clipping."""
        dh = dout @ self.W2.T
        dh_pre = dh * self.act_bwd(self._h_pre)
        dW2 = self._h.T @ dout
        db2 = dout.sum(0)
        dW1 = self._x.T @ dh_pre
        db1 = dh_pre.sum(0)

        # Compute gradient norms
        grad_norm = np.sqrt(np.sum(dW1**2) + np.sum(db1**2) + np.sum(dW2**2) + np.sum(db2**2))

        # Gradient clipping if requested
        clipped_norm = grad_norm
        if clip_norm is not None and grad_norm > clip_norm:
            scale = clip_norm / grad_norm
            dW1 *= scale; db1 *= scale; dW2 *= scale; db2 *= scale
            clipped_norm = clip_norm

        self.W1 -= lr * dW1
        self.b1 -= lr * db1
        self.W2 -= lr * dW2
        self.b2 -= lr * db2

        # Track activation stats
        act_max = np.max(np.abs(self._h))
        act_mean = np.mean(np.abs(self._h))

        return {
            "grad_norm": grad_norm,
            "clipped_norm": clipped_norm,
            "act_max": act_max,
            "act_mean": act_mean,
            "has_nan": bool(np.any(np.isnan(self.W1)) or np.any(np.isnan(self.W2))),
            "has_inf": bool(np.any(np.isinf(self.W1)) or np.any(np.isinf(self.W2))),
        }


def softmax_np(x):
    ex = np.exp(x - x.max(-1, keepdims=True))
    return ex / ex.sum(-1, keepdims=True)

def cross_entropy_and_grad(logits, targets):
    probs = softmax_np(logits)
    N = logits.shape[0]
    loss = -np.log(probs[np.arange(N), targets] + 1e-9).mean()
    dlogits = probs.copy()
    dlogits[np.arange(N), targets] -= 1.0
    dlogits /= N
    return loss, dlogits


def make_corpus(d_in=32, n_classes=32, n_batches=200, batch_size=64):
    rng = np.random.default_rng(0)
    batches = []
    patterns = [
        np.arange(n_classes),
        np.roll(np.arange(n_classes), 3),
        (np.arange(n_classes) * 3) % n_classes,
        (np.arange(n_classes) * 5) % n_classes,
    ]
    for _ in range(n_batches):
        pat = rng.integers(0, len(patterns))
        idx = rng.integers(0, n_classes, batch_size)
        targets = patterns[pat][idx]
        x = np.zeros((batch_size, d_in))
        x[np.arange(batch_size), idx % d_in] = 1.0
        x += rng.standard_normal((batch_size, d_in)) * 0.05
        batches.append((x.astype(np.float64), targets.astype(np.int32)))
    return batches


def run_stability_test(act_name, act_fwd, act_bwd, corpus, lr, n_steps=500, clip_norm=None):
    """Run training and collect stability metrics."""
    rng = np.random.default_rng(42)
    model = MLP(32, 128, 32, act_fwd, act_bwd, rng)

    losses = []
    grad_norms = []
    act_maxes = []
    nan_step = None
    inf_step = None
    loss_spikes = 0

    for step in range(n_steps):
        x, targets = corpus[step % len(corpus)]
        logits = model.forward(x)

        # Check for NaN in logits
        if np.any(np.isnan(logits)) or np.any(np.isinf(logits)):
            if nan_step is None:
                nan_step = step
            losses.append(float('inf'))
            grad_norms.append(float('inf'))
            act_maxes.append(float('inf'))
            break

        loss, dlogits = cross_entropy_and_grad(logits, targets)
        info = model.backward(dlogits, lr, clip_norm=clip_norm)

        losses.append(loss)
        grad_norms.append(info["grad_norm"])
        act_maxes.append(info["act_max"])

        if info["has_nan"]:
            if nan_step is None:
                nan_step = step
            break
        if info["has_inf"]:
            if inf_step is None:
                inf_step = step
            break

        # Count loss spikes (>2x previous)
        if len(losses) > 1 and losses[-1] > 2 * losses[-2]:
            loss_spikes += 1

    survived_steps = len(losses)
    final_loss = np.mean(losses[-min(50, len(losses)):]) if len(losses) > 0 else float('inf')

    return {
        "act": act_name,
        "lr": lr,
        "clip": clip_norm,
        "survived": survived_steps,
        "final_loss": final_loss,
        "max_grad_norm": max(grad_norms) if grad_norms else 0,
        "mean_grad_norm": np.mean(grad_norms) if grad_norms else 0,
        "max_act": max(act_maxes) if act_maxes else 0,
        "loss_spikes": loss_spikes,
        "nan_step": nan_step,
        "inf_step": inf_step,
        "grad_norms": grad_norms,
        "losses": losses,
    }


# ── Main ──

def main():
    SEP = "=" * 78
    corpus = make_corpus()

    print(SEP)
    print("  H-EE-3: Phi6Simple Training Stability")
    print("  Hypothesis: Bounded output prevents gradient explosion without clipping")
    print(SEP)

    # Test 1: Normal learning rate, no clipping
    print("\n  TEST 1: Normal LR (0.01), NO gradient clipping")
    print("  " + "-" * 70)
    print(f"  {'Activation':10s}  {'Survived':>8s}  {'Final Loss':>10s}  {'Max GradNorm':>12s}  "
          f"{'Mean GradNorm':>13s}  {'Max Act':>8s}  {'Spikes':>6s}")
    print("  " + "-" * 78)

    for act_name, (fwd, bwd) in ACTIVATIONS.items():
        res = run_stability_test(act_name, fwd, bwd, corpus, lr=0.01, clip_norm=None)
        print(f"  {act_name:10s}  {res['survived']:8d}  {res['final_loss']:10.4f}  "
              f"{res['max_grad_norm']:12.4f}  {res['mean_grad_norm']:13.4f}  "
              f"{res['max_act']:8.2f}  {res['loss_spikes']:6d}")

    # Test 2: High learning rate stress test
    high_lrs = [0.05, 0.1, 0.5, 1.0]
    print(f"\n  TEST 2: HIGH LR stress test, NO gradient clipping")
    print("  " + "-" * 70)
    print(f"  {'Activation':10s}  {'LR':>6s}  {'Survived':>8s}  {'Final Loss':>10s}  "
          f"{'Max GradNorm':>12s}  {'NaN@step':>8s}  {'Spikes':>6s}")
    print("  " + "-" * 70)

    stability_scores = {}
    for act_name, (fwd, bwd) in ACTIVATIONS.items():
        stability_scores[act_name] = 0
        for lr in high_lrs:
            res = run_stability_test(act_name, fwd, bwd, corpus, lr=lr, clip_norm=None, n_steps=200)
            nan_str = str(res['nan_step']) if res['nan_step'] is not None else "-"
            fl = f"{res['final_loss']:.4f}" if res['final_loss'] < 100 else f"{res['final_loss']:.1f}"
            print(f"  {act_name:10s}  {lr:6.2f}  {res['survived']:8d}  {fl:>10s}  "
                  f"{res['max_grad_norm']:12.2f}  {nan_str:>8s}  {res['loss_spikes']:6d}")
            if res['survived'] == 200 and res['final_loss'] < 50:
                stability_scores[act_name] += 1

    # Test 3: With vs Without gradient clipping for Phi6 and GELU
    print(f"\n  TEST 3: Effect of gradient clipping (clip_norm=1.0)")
    print("  " + "-" * 70)
    print(f"  {'Activation':10s}  {'Clipping':>8s}  {'LR':>6s}  {'Survived':>8s}  "
          f"{'Final Loss':>10s}  {'Max GradNorm':>12s}")
    print("  " + "-" * 70)

    for act_name in ["GELU", "Phi6"]:
        fwd, bwd = ACTIVATIONS[act_name]
        for lr in [0.01, 0.1]:
            for clip in [None, 1.0]:
                res = run_stability_test(act_name, fwd, bwd, corpus, lr=lr, clip_norm=clip, n_steps=300)
                clip_str = f"{clip:.1f}" if clip else "None"
                fl = f"{res['final_loss']:.4f}" if res['final_loss'] < 100 else f"{res['final_loss']:.1f}"
                print(f"  {act_name:10s}  {clip_str:>8s}  {lr:6.2f}  {res['survived']:8d}  "
                      f"{fl:>10s}  {res['max_grad_norm']:12.4f}")

    # Test 4: Gradient norm over training (ASCII plot)
    print(f"\n  TEST 4: Gradient Norm Evolution (LR=0.05, 300 steps)")
    print("  " + "-" * 70)

    traces = {}
    for act_name in ["GELU", "Phi6"]:
        fwd, bwd = ACTIVATIONS[act_name]
        res = run_stability_test(act_name, fwd, bwd, corpus, lr=0.05, clip_norm=None, n_steps=300)
        traces[act_name] = res["grad_norms"]

    # ASCII plot
    width = 60
    height = 12
    all_norms = []
    for norms in traces.values():
        all_norms.extend([n for n in norms if np.isfinite(n)])
    if all_norms:
        y_max = min(np.percentile(all_norms, 99), max(all_norms))
        y_min = 0

        grid = [[" "] * width for _ in range(height)]
        chars = {"GELU": "G", "Phi6": "P"}
        for act_name, norms in traces.items():
            n_pts = len(norms)
            for col in range(width):
                idx = int(col * (n_pts - 1) / (width - 1)) if n_pts > 1 else 0
                if idx < len(norms) and np.isfinite(norms[idx]):
                    val = norms[idx]
                    row = height - 1 - int((val - y_min) / (y_max - y_min + 1e-9) * (height - 1))
                    row = max(0, min(row, height - 1))
                    ch = chars.get(act_name, "?")
                    grid[row][col] = ch if grid[row][col] == " " else "+"

        print(f"  Gradient Norm (y: 0..{y_max:.2f}, x: step 1..300)")
        print("  " + "-" * (width + 2))
        for row_i, row in enumerate(grid):
            y_val = y_max - (row_i / (height - 1)) * (y_max - y_min)
            print(f"  {y_val:6.3f}|{''.join(row)}|")
        print("  " + "-" * (width + 2))
        print("  Legend: G=GELU  P=Phi6")

    # Verdict
    print(f"\n  STABILITY SCORES (survived high-LR tests out of {len(high_lrs)}):")
    for name, score in stability_scores.items():
        print(f"    {name:10s}: {score}/{len(high_lrs)}")

    phi6_score = stability_scores.get("Phi6", 0)
    gelu_score = stability_scores.get("GELU", 0)

    print(f"\n  VERDICT:")
    if phi6_score > gelu_score:
        print(f"    SUPPORTED: Phi6 survived {phi6_score}/{len(high_lrs)} high-LR tests vs GELU's {gelu_score}/{len(high_lrs)}")
        print(f"    Bounded output range does provide better stability.")
        print(f"    Grade: SUPPORTED")
    elif phi6_score == gelu_score:
        print(f"    PARTIAL: Phi6 and GELU have equal stability ({phi6_score}/{len(high_lrs)})")
        print(f"    Bounded range doesn't clearly help at this scale.")
        print(f"    Grade: PARTIAL")
    else:
        print(f"    REFUTED: GELU ({gelu_score}) is more stable than Phi6 ({phi6_score})")
        print(f"    Grade: REFUTED")

    print(SEP)


if __name__ == "__main__":
    main()
