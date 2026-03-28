"""
SEDI Training Monitor
======================
4-lens system ported from SEDI for real-time training diagnostics:
1. R-filter: windowed FFT on loss curve
2. PH barcode: persistent homology of loss landscape
3. Euler product: convergence diagnostic on gradient norms
4. Consciousness: pattern detection on activation statistics

Outputs anomaly score (0-5+) and phase classification.
"""

import numpy as np
import math


def rfilter_score(loss_history, windows=(6, 12, 24, 36)):
    if len(loss_history) < max(windows):
        return 0.0, {}

    scores = {}
    signal = np.array(loss_history[-max(windows):])
    signal = signal - signal.mean()

    for w in windows:
        if len(signal) < w:
            continue
        chunk = signal[-w:]
        fft = np.fft.rfft(chunk)
        power = np.abs(fft) ** 2
        if len(power) < 2:
            continue

        n6_freqs = [w // 6, w // 4, w // 3]
        n6_power = sum(power[min(f, len(power)-1)] for f in n6_freqs if f > 0)
        total_power = power[1:].sum() + 1e-10
        ratio = n6_power / total_power
        scores[w] = ratio

    if not scores:
        return 0.0, scores

    avg_ratio = np.mean(list(scores.values()))
    return min(5.0, avg_ratio * 15.0), scores


def ph_persistence_score(loss_history, window=24):
    if len(loss_history) < window:
        return 0.0

    recent = np.array(loss_history[-window:])
    sorted_vals = np.sort(recent)
    gaps = np.diff(sorted_vals)

    if len(gaps) == 0:
        return 0.0

    median_gap = np.median(gaps)
    if median_gap < 1e-10:
        return 0.0

    significant = (gaps > 2 * median_gap).sum()
    return min(5.0, significant / 3.0)


def euler_convergence_score(grad_norms, window=12):
    if len(grad_norms) < window:
        return 0.0

    recent = np.array(grad_norms[-window:])
    if recent.mean() < 1e-10:
        return 5.0

    half = window // 2
    early = recent[:half].mean()
    late = recent[half:].mean()

    if early < 1e-10:
        return 5.0

    ratio = late / early
    if ratio < 0.5:
        return 4.0
    elif ratio < 0.8:
        return 2.0
    elif ratio < 1.0:
        return 1.0
    else:
        return 0.0


def consciousness_pattern_score(activation_stats):
    score = 0.0

    if not activation_stats:
        return 0.0

    sparsity = activation_stats.get("sparsity", 0)
    target_sparsity = 1.0 - 1.0 / math.e
    if abs(sparsity - target_sparsity) < 0.1:
        score += 1.5

    entropy = activation_stats.get("entropy", 0)
    h_target = sum(-p * math.log(p) for p in [1/2, 1/3, 1/6])
    if abs(entropy - h_target) < 0.1:
        score += 1.5

    mean_act = activation_stats.get("mean", 0)
    if abs(mean_act - 5/6) < 0.1:
        score += 1.0

    std_act = activation_stats.get("std", 0)
    if abs(std_act - 1/math.sqrt(6)) < 0.1:
        score += 1.0

    return min(5.0, score)


class SEDITrainingMonitor:
    LEVELS = {
        (0, 2): "NORMAL",
        (2, 3): "YELLOW",
        (3, 5): "ORANGE",
        (5, float('inf')): "RED",
    }

    def __init__(self):
        self.loss_history = []
        self.grad_norms = []
        self.activation_stats_history = []
        self.scores_history = []

    def update(self, loss, grad_norm=None, activation_stats=None):
        self.loss_history.append(loss)
        if grad_norm is not None:
            self.grad_norms.append(grad_norm)
        if activation_stats is not None:
            self.activation_stats_history.append(activation_stats)

    def evaluate(self):
        s1, rfilter_details = rfilter_score(self.loss_history)
        s2 = ph_persistence_score(self.loss_history)
        s3 = euler_convergence_score(self.grad_norms)
        s4 = consciousness_pattern_score(
            self.activation_stats_history[-1] if self.activation_stats_history else {}
        )

        combined = (s1 + s2 + s3 + s4) / 4.0

        level = "NORMAL"
        for (lo, hi), name in self.LEVELS.items():
            if lo <= combined < hi:
                level = name
                break

        result = {
            "rfilter": s1,
            "ph_persistence": s2,
            "euler_convergence": s3,
            "consciousness": s4,
            "combined": combined,
            "level": level,
        }
        self.scores_history.append(result)
        return result

    def is_phase_transition(self):
        if len(self.scores_history) < 2:
            return False
        delta = self.scores_history[-1]["combined"] - self.scores_history[-2]["combined"]
        return abs(delta) > 1.0


def main():
    print("=" * 70)
    print("  SEDI Training Monitor")
    print("  4-lens real-time training diagnostic")
    print("=" * 70)

    monitor = SEDITrainingMonitor()
    np.random.seed(42)

    print(f"\n{'Step':>5} {'Loss':>8} {'R-filt':>7} {'PH':>7} {'Euler':>7} {'Consc':>7} {'Combined':>9} {'Level':<8}")
    print("-" * 68)

    for step in range(100):
        if step < 30:
            loss = 3.0 - 0.02 * step + np.random.randn() * 0.3
            grad_norm = 2.0 + np.random.randn() * 0.5
        elif step < 60:
            loss = 2.4 - 0.04 * (step - 30) + np.random.randn() * 0.1
            grad_norm = 1.0 - 0.02 * (step - 30) + np.random.randn() * 0.2
        else:
            loss = 1.2 + 0.05 * np.sin(2 * np.pi * step / 6) + np.random.randn() * 0.02
            grad_norm = 0.3 + np.random.randn() * 0.05

        act_stats = {
            "mean": 0.5 + 0.003 * step,
            "std": 0.5 - 0.002 * step,
            "sparsity": 0.3 + 0.003 * step,
            "entropy": 0.5 + 0.004 * step,
        }

        monitor.update(loss, grad_norm, act_stats)

        if step % 5 == 0 and step >= 10:
            result = monitor.evaluate()
            phase_marker = " ** TRANSITION **" if monitor.is_phase_transition() else ""
            print(f"{step:>5} {loss:>8.3f} {result['rfilter']:>7.2f} "
                  f"{result['ph_persistence']:>7.2f} {result['euler_convergence']:>7.2f} "
                  f"{result['consciousness']:>7.2f} {result['combined']:>9.2f} "
                  f"{result['level']:<8}{phase_marker}")

    print(f"\nFinal level: {monitor.scores_history[-1]['level']}")
    print(f"Phase transitions detected: "
          f"{sum(1 for i in range(1, len(monitor.scores_history)) if abs(monitor.scores_history[i]['combined'] - monitor.scores_history[i-1]['combined']) > 1.0)}")


if __name__ == "__main__":
    main()
