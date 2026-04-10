"""H-EE-8: tau(d) predicts performance better than d itself.
d=120(tau=16) vs d=128(tau=8) at matched param count (adjust n_layers)."""
import torch, torch.nn as nn, time, math

torch.manual_seed(42)
text = "".join(chr(32 + (i * 7 + 13) % 95) for i in range(20000))
chars = sorted(set(text))
stoi = {c: i for i, c in enumerate(chars)}
data = torch.tensor([stoi[c] for c in text], dtype=torch.long)
vocab, seq_len, batch = len(chars), 32, 32

def make_batches(data):
    n = len(data) - seq_len - 1
    xs, ys = [], []
    for _ in range(batch * 50):
        i = torch.randint(0, n, (1,)).item()
        xs.append(data[i:i+seq_len]); ys.append(data[i+1:i+seq_len+1])
    return torch.stack(xs).reshape(-1, batch, seq_len), torch.stack(ys).reshape(-1, batch, seq_len)

xs, ys = make_batches(data)

class TinyLM(nn.Module):
    def __init__(self, d, nh, nl):
        super().__init__()
        self.emb = nn.Embedding(vocab, d)
        self.pos = nn.Embedding(seq_len, d)
        layer = nn.TransformerEncoderLayer(d, nh, d*4, dropout=0, batch_first=True)
        self.tf = nn.TransformerEncoder(layer, nl)
        self.out = nn.Linear(d, vocab)
    def forward(self, x):
        pos = torch.arange(x.size(1), device=x.device)
        h = self.emb(x) + self.pos(pos)
        mask = nn.Transformer.generate_square_subsequent_mask(x.size(1), device=x.device)
        return self.out(self.tf(h, mask=mask))

def tau(n):
    return sum(1 for d in range(1, n+1) if n % d == 0)

print("=" * 60)
print("H-EE-8: tau(d) as Performance Predictor")
print("=" * 60)

# Match param counts by adjusting layers
# d=120, 2 layers: ~174K params
# d=128, 2 layers: ~198K params
# d=120, 3 layers: ~255K params
# d=128, 3 layers: ~293K params
# For fair comparison: d=120 nl=3 vs d=128 nl=2 (both ~200K range)
# Also test more dims with varying layers

configs = [
    # (d, n_heads, n_layers, label)
    (60,  4, 4, "HCN tau=12"),
    (64,  4, 4, "2^k tau=7"),
    (120, 8, 2, "HCN tau=16 nl=2"),
    (120, 8, 3, "HCN tau=16 nl=3"),
    (128, 8, 2, "2^k tau=8 nl=2"),
    (128, 8, 3, "2^k tau=8 nl=3"),
    (240, 8, 1, "HCN tau=20 nl=1"),
    (256, 8, 1, "2^k tau=9 nl=1"),
]

results = []
loss_fn = nn.CrossEntropyLoss()

for d, nh, nl, label in configs:
    model = TinyLM(d, nh, nl)
    nparams = sum(p.numel() for p in model.parameters())
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    t0 = time.time()
    losses_end = []
    for step in range(300):
        bi = step % xs.size(0)
        logits = model(xs[bi])
        loss = loss_fn(logits.reshape(-1, vocab), ys[bi].reshape(-1))
        opt.zero_grad(); loss.backward(); opt.step()
        if step >= 250: losses_end.append(loss.item())
    avg_loss = sum(losses_end) / len(losses_end)
    elapsed = time.time() - t0
    t_d = tau(d)
    results.append((d, nh, nl, t_d, nparams, avg_loss, elapsed, label))
    print(f"{label:<20} d={d:>4} tau={t_d:>3} nl={nl} params={nparams:>8} loss={avg_loss:.4f} t={elapsed:.1f}s")

print("\n" + "=" * 60)
print("MATCHED PARAM COMPARISONS")
print("=" * 60)
# Compare d=120 nl=3 vs d=128 nl=2 (closest param match)
r120_3 = [r for r in results if r[0]==120 and r[2]==3][0]
r128_2 = [r for r in results if r[0]==128 and r[2]==2][0]
print(f"d=120 nl=3: params={r120_3[4]:>8} tau={r120_3[3]:>3} loss={r120_3[5]:.4f}")
print(f"d=128 nl=2: params={r128_2[4]:>8} tau={r128_2[3]:>3} loss={r128_2[5]:.4f}")
print(f"  -> Higher tau({r120_3[3]}) {'WINS' if r120_3[5]<r128_2[5] else 'LOSES'}")

print(f"\nd=60 nl=4 vs d=64 nl=4:")
r60 = [r for r in results if r[0]==60][0]
r64 = [r for r in results if r[0]==64][0]
print(f"d=60  nl=4: params={r60[4]:>8} tau={r60[3]:>3} loss={r60[5]:.4f}")
print(f"d=64  nl=4: params={r64[4]:>8} tau={r64[3]:>3} loss={r64[5]:.4f}")
print(f"  -> Higher tau({r60[3]}) {'WINS' if r60[5]<r64[5] else 'LOSES'}")

r240 = [r for r in results if r[0]==240][0]
r256 = [r for r in results if r[0]==256][0]
print(f"\nd=240 nl=1 vs d=256 nl=1:")
print(f"d=240 nl=1: params={r240[4]:>8} tau={r240[3]:>3} loss={r240[5]:.4f}")
print(f"d=256 nl=1: params={r256[4]:>8} tau={r256[3]:>3} loss={r256[5]:.4f}")
print(f"  -> Higher tau({r240[3]}) {'WINS' if r240[5]<r256[5] else 'LOSES'}")

# Overall: does tau rank correlate with loss rank?
def rank(arr):
    indexed = sorted(enumerate(arr), key=lambda x: x[1])
    ranks = [0]*len(arr)
    for r, (i, _) in enumerate(indexed): ranks[i] = r
    return ranks

taus = [r[3] for r in results]
losses = [r[4] for r in results]  # note: r[4] is nparams, r[5] is loss
losses = [r[5] for r in results]
params_list = [r[4] for r in results]
eff = [-l/p for l, p in zip(losses, params_list)]  # loss-per-param efficiency

def spearman(a, b):
    ra, rb = rank(a), rank(b)
    n = len(a)
    d2 = sum((ra[i]-rb[i])**2 for i in range(n))
    return 1 - 6*d2/(n*(n*n-1))

print(f"\nSpearman(tau, -loss):          {spearman(taus, [-l for l in losses]):.4f}")
print(f"Spearman(params, -loss):       {spearman(params_list, [-l for l in losses]):.4f}")
print(f"Spearman(tau, efficiency):     {spearman(taus, eff):.4f}")
print(f"Spearman(d, -loss):            {spearman([r[0] for r in results], [-l for l in losses]):.4f}")
print(f"\nConclusion: tau is {'a better' if abs(spearman(taus, eff)) > abs(spearman([r[0] for r in results], eff)) else 'NOT a better'} predictor than d for efficiency")
