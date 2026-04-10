#!/usr/bin/env python3
"""
H-EE-18: Egyptian Fraction MoE Routing Verification

Hypothesis: Using expert weights {1/2, 1/3, 1/6} (the unique perfect-number
Egyptian fraction that sums to 1) as fixed routing weights outperforms
equal weighting {1/3, 1/3, 1/3} and competes with learned softmax routing.

Test: 8-class spiral, 3-expert MoE, 500 training steps x 5 seeds.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from collections import defaultdict
import math

# ─── Synthetic Dataset: 8-class spiral (hard) ───

def make_spiral(n_samples=2000, n_classes=8, noise=0.3, seed=42):
    """8-class spiral dataset -- much harder than concentric circles."""
    rng = np.random.RandomState(seed)
    n_per_class = n_samples // n_classes
    X_list, y_list = [], []
    for c in range(n_classes):
        theta = np.linspace(c * 2 * np.pi / n_classes,
                            c * 2 * np.pi / n_classes + 3 * np.pi / n_classes,
                            n_per_class)
        r = np.linspace(0.3, 2.5, n_per_class)
        x1 = r * np.cos(theta) + rng.normal(0, noise, n_per_class)
        x2 = r * np.sin(theta) + rng.normal(0, noise, n_per_class)
        X_list.append(np.stack([x1, x2], axis=1))
        y_list.append(np.full(n_per_class, c))
    X = np.concatenate(X_list).astype(np.float32)
    y = np.concatenate(y_list).astype(np.int64)
    # Project to 64 dims via random projection with noise
    proj = rng.randn(2, 64).astype(np.float32) * 0.3
    X_proj = X @ proj + rng.randn(n_samples, 64).astype(np.float32) * 0.1
    return torch.from_numpy(X_proj), torch.from_numpy(y)


# ─── Expert MLP ───

class Expert(nn.Module):
    def __init__(self, input_dim=64, hidden_dim=32, output_dim=32):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim),
        )

    def forward(self, x):
        return self.net(x)


# ─── MoE Layer ───

class MoELayer(nn.Module):
    def __init__(self, input_dim=64, hidden_dim=32, output_dim=32,
                 n_experts=3, routing="egyptian"):
        super().__init__()
        self.routing = routing
        self.n_experts = n_experts
        self.experts = nn.ModuleList([
            Expert(input_dim, hidden_dim, output_dim) for _ in range(n_experts)
        ])
        # Router: produces score per expert
        self.router = nn.Linear(input_dim, n_experts)

        # Fixed weights for Egyptian and Equal routing
        self.egyptian_weights = torch.tensor([1/2, 1/3, 1/6])
        self.egyptian_reverse = torch.tensor([1/6, 1/3, 1/2])
        self.equal_weights = torch.tensor([1/3, 1/3, 1/3])

    def forward(self, x):
        # Get router scores
        router_logits = self.router(x)  # (B, n_experts)

        # Get expert outputs
        expert_outputs = torch.stack([e(x) for e in self.experts], dim=1)  # (B, n_experts, D)

        if self.routing == "equal":
            weights = self.equal_weights.to(x.device).unsqueeze(0).expand(x.size(0), -1)

        elif self.routing == "egyptian":
            # Assign 1/2 to highest-scoring expert, 1/3 to second, 1/6 to third
            order = router_logits.argsort(dim=-1, descending=True)  # (B, 3)
            weights = torch.zeros_like(router_logits)
            eg = self.egyptian_weights.to(x.device)
            for i in range(self.n_experts):
                val = eg[i].expand(x.size(0), 1)
                weights.scatter_(1, order[:, i:i+1], val)

        elif self.routing == "egyptian_reverse":
            # Assign 1/6 to highest-scoring expert (reverse order)
            order = router_logits.argsort(dim=-1, descending=True)
            weights = torch.zeros_like(router_logits)
            eg = self.egyptian_reverse.to(x.device)
            for i in range(self.n_experts):
                val = eg[i].expand(x.size(0), 1)
                weights.scatter_(1, order[:, i:i+1], val)

        elif self.routing == "top2":
            # Activate only top 2 experts with softmax weights
            topk_vals, topk_idx = router_logits.topk(2, dim=-1)
            topk_weights = F.softmax(topk_vals, dim=-1)
            weights = torch.zeros_like(router_logits)
            weights.scatter_(1, topk_idx, topk_weights)

        elif self.routing == "softmax":
            # Standard learned softmax routing
            weights = F.softmax(router_logits, dim=-1)

        else:
            raise ValueError(f"Unknown routing: {self.routing}")

        # Weighted combination: (B, n_experts, D) * (B, n_experts, 1) -> sum -> (B, D)
        out = (expert_outputs * weights.unsqueeze(-1)).sum(dim=1)
        return out, weights


# ─── Full Model ───

class MoEClassifier(nn.Module):
    def __init__(self, input_dim=64, hidden_dim=32, n_classes=8,
                 n_experts=3, routing="egyptian"):
        super().__init__()
        self.moe = MoELayer(input_dim, hidden_dim, hidden_dim, n_experts, routing)
        self.classifier = nn.Linear(hidden_dim, n_classes)

    def forward(self, x):
        h, weights = self.moe(x)
        logits = self.classifier(F.relu(h))
        return logits, weights


# ─── Training ───

def train_and_evaluate(routing, seed, n_steps=500, lr=0.01, batch_size=128):
    torch.manual_seed(seed)
    np.random.seed(seed)

    X, y = make_spiral(n_samples=2000, n_classes=8, noise=0.3, seed=seed)

    # Train/test split
    n_train = 1600
    X_train, y_train = X[:n_train], y[:n_train]
    X_test, y_test = X[n_train:], y[n_train:]

    model = MoEClassifier(routing=routing, n_classes=8)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()

    model.train()
    losses = []
    for step in range(n_steps):
        idx = torch.randint(0, n_train, (batch_size,))
        xb, yb = X_train[idx], y_train[idx]

        logits, weights = model(xb)
        loss = criterion(logits, yb)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if step % 50 == 0:
            losses.append(loss.item())

    # Evaluate
    model.eval()
    with torch.no_grad():
        logits_test, weights_test = model(X_test)
        test_loss = criterion(logits_test, y_test).item()
        preds = logits_test.argmax(dim=-1)
        acc = (preds == y_test).float().mean().item()

        # Expert utilization: average weight per expert
        avg_weights = weights_test.mean(dim=0).numpy()

    return {
        "accuracy": acc,
        "test_loss": test_loss,
        "expert_weights": avg_weights,
        "train_losses": losses,
    }


# ─── Main ───

def main():
    print("=" * 70)
    print("H-EE-18: Egyptian Fraction MoE Routing Verification")
    print("=" * 70)
    print()
    print("Egyptian fraction: 1/2 + 1/3 + 1/6 = 1")
    print("  (unique proper-divisor reciprocal sum of perfect number 6)")
    print()
    print("Routing strategies:")
    print("  equal           : {1/3, 1/3, 1/3}")
    print("  egyptian        : {1/2, 1/3, 1/6} sorted by router score (best gets 1/2)")
    print("  egyptian_reverse: {1/6, 1/3, 1/2} reverse order (best gets 1/6)")
    print("  top2            : top-2 experts with softmax weights")
    print("  softmax         : standard learned softmax over all 3")
    print()
    print("Task: 8-class spiral (hard), 64-dim input, 500 steps, 5 seeds")
    print("=" * 70)

    strategies = ["equal", "egyptian", "egyptian_reverse", "top2", "softmax"]
    seeds = [42, 123, 456, 789, 1024]
    results = defaultdict(list)

    for strategy in strategies:
        print(f"\n--- {strategy} ---")
        for seed in seeds:
            r = train_and_evaluate(strategy, seed)
            results[strategy].append(r)
            print(f"  seed={seed:4d}  acc={r['accuracy']:.4f}  loss={r['test_loss']:.4f}  "
                  f"expert_w=[{r['expert_weights'][0]:.3f}, {r['expert_weights'][1]:.3f}, {r['expert_weights'][2]:.3f}]")

    # ─── Summary Table ───
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print(f"{'Strategy':<20s} {'Mean Acc':>10s} {'Std Acc':>10s} {'Mean Loss':>10s} {'Std Loss':>10s}")
    print("-" * 60)

    summary = {}
    for strategy in strategies:
        accs = [r["accuracy"] for r in results[strategy]]
        losses = [r["test_loss"] for r in results[strategy]]
        mean_acc = np.mean(accs)
        std_acc = np.std(accs)
        mean_loss = np.mean(losses)
        std_loss = np.std(losses)
        summary[strategy] = (mean_acc, std_acc, mean_loss, std_loss)
        print(f"{strategy:<20s} {mean_acc:>10.4f} {std_acc:>10.4f} {mean_loss:>10.4f} {std_loss:>10.4f}")

    # ─── Key Comparisons ───
    print("\n" + "=" * 70)
    print("KEY COMPARISONS")
    print("=" * 70)

    eg_acc, eg_std = summary["egyptian"][:2]
    eq_acc, eq_std = summary["equal"][:2]
    sm_acc, sm_std = summary["softmax"][:2]
    t2_acc, t2_std = summary["top2"][:2]
    er_acc, er_std = summary["egyptian_reverse"][:2]

    diff_eq = eg_acc - eq_acc
    diff_sm = eg_acc - sm_acc
    diff_t2 = eg_acc - t2_acc
    diff_rev = eg_acc - er_acc

    print(f"\n  Egyptian vs Equal:           {diff_eq:+.4f}  ({'Egyptian wins' if diff_eq > 0 else 'Equal wins'})")
    print(f"  Egyptian vs Softmax:         {diff_sm:+.4f}  ({'Egyptian wins' if diff_sm > 0 else 'Softmax wins'})")
    print(f"  Egyptian vs Top-2:           {diff_t2:+.4f}  ({'Egyptian wins' if diff_t2 > 0 else 'Top-2 wins'})")
    print(f"  Egyptian vs Egyptian Reverse: {diff_rev:+.4f}  ({'Order matters: correct > reverse' if diff_rev > 0 else 'Order matters: reverse > correct'})")

    # ─── Statistical Test (paired t-test approximation) ───
    print("\n" + "=" * 70)
    print("STATISTICAL SIGNIFICANCE (paired differences across seeds)")
    print("=" * 70)

    def paired_test(name_a, name_b):
        accs_a = [r["accuracy"] for r in results[name_a]]
        accs_b = [r["accuracy"] for r in results[name_b]]
        diffs = [a - b for a, b in zip(accs_a, accs_b)]
        mean_d = np.mean(diffs)
        std_d = np.std(diffs, ddof=1)
        n = len(diffs)
        if std_d < 1e-10:
            t_stat = 0.0
        else:
            t_stat = mean_d / (std_d / math.sqrt(n))
        # Approximate p-value (2-tailed) using normal approx for n=5
        p_approx = 2 * (1 - 0.5 * (1 + math.erf(abs(t_stat) / math.sqrt(2))))
        return mean_d, std_d, t_stat, p_approx

    comparisons = [
        ("egyptian", "equal", "Egyptian vs Equal"),
        ("egyptian", "softmax", "Egyptian vs Softmax"),
        ("egyptian", "top2", "Egyptian vs Top-2"),
        ("egyptian", "egyptian_reverse", "Egyptian vs Reverse"),
    ]

    print(f"\n{'Comparison':<30s} {'Mean Diff':>10s} {'t-stat':>10s} {'p-value':>10s} {'Sig?':>6s}")
    print("-" * 70)
    for a, b, label in comparisons:
        mean_d, std_d, t_stat, p_val = paired_test(a, b)
        sig = "Yes" if p_val < 0.05 else "No"
        print(f"{label:<30s} {mean_d:>+10.4f} {t_stat:>10.3f} {p_val:>10.4f} {sig:>6s}")

    # ─── Expert Utilization ───
    print("\n" + "=" * 70)
    print("EXPERT UTILIZATION (mean routing weights across test set)")
    print("=" * 70)
    print(f"\n{'Strategy':<20s} {'Expert 0':>10s} {'Expert 1':>10s} {'Expert 2':>10s} {'Entropy':>10s}")
    print("-" * 60)
    for strategy in strategies:
        ws = np.mean([r["expert_weights"] for r in results[strategy]], axis=0)
        # Shannon entropy
        ws_safe = np.clip(ws, 1e-10, 1.0)
        entropy = -np.sum(ws_safe * np.log(ws_safe))
        max_entropy = np.log(3)
        print(f"{strategy:<20s} {ws[0]:>10.4f} {ws[1]:>10.4f} {ws[2]:>10.4f} {entropy/max_entropy:>10.4f}")

    # ─── ASCII Bar Chart ───
    print("\n" + "=" * 70)
    print("ACCURACY BAR CHART")
    print("=" * 70)
    print()
    max_acc = max(summary[s][0] for s in strategies)
    for strategy in strategies:
        acc = summary[strategy][0]
        bar_len = int(acc / max_acc * 40)
        bar = "#" * bar_len
        print(f"  {strategy:<20s} |{bar:<40s}| {acc:.4f}")

    # ─── Verdict ───
    print("\n" + "=" * 70)
    print("VERDICT")
    print("=" * 70)

    best = max(strategies, key=lambda s: summary[s][0])
    print(f"\n  Best strategy: {best} (mean acc = {summary[best][0]:.4f})")

    if diff_eq > 0.005:
        print("  Egyptian routing OUTPERFORMS equal routing.")
        print("  -> The {1/2, 1/3, 1/6} structure provides meaningful inductive bias.")
    elif diff_eq > -0.005:
        print("  Egyptian routing COMPARABLE to equal routing.")
        print("  -> Marginal difference; larger scale needed for conclusive evidence.")
    else:
        print("  Egyptian routing UNDERPERFORMS equal routing.")
        print("  -> Fixed asymmetric weights may be too rigid for this task.")

    if diff_rev > 0.005:
        print("  Order MATTERS: assigning 1/2 to best expert is better than reverse.")
    elif diff_rev > -0.005:
        print("  Order effect is MARGINAL.")
    else:
        print("  Reverse order is BETTER (unexpected).")

    print()
    print("Note: This is a small-scale CPU test on synthetic data.")
    print("Results are indicative but not conclusive for large-scale MoE models.")
    print("Golden Zone dependency: YES (Egyptian fraction from n=6 perfect number)")


if __name__ == "__main__":
    main()
