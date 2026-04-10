"""H-EE-5: R(d_model) correlates with training efficiency.
Compute R-spectrum for candidate dims, then train tiny char-LM to check correlation."""
import math, time, json

def sigma(n):
    return sum(d for d in range(1, n+1) if n % d == 0)

def phi(n):
    result = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0: temp //= p
            result -= result // p
        p += 1
    if temp > 1: result -= result // temp
    return result

def tau(n):
    return sum(1 for d in range(1, n+1) if n % d == 0)

def R(n):
    return sigma(n) * phi(n) / (n * tau(n))

# Compute R for all candidate dims
dims = [60, 64, 120, 128, 180, 240, 256, 360, 512, 720, 1024]
print("=" * 60)
print("H-EE-5: R-Spectrum for Model Dimensions")
print("=" * 60)
print(f"{'d':>6} {'sigma':>8} {'phi':>8} {'tau':>5} {'R(d)':>10}")
print("-" * 45)
for d in dims:
    s, p, t, r = sigma(d), phi(d), tau(d), R(d)
    print(f"{d:>6} {s:>8} {p:>8} {t:>5} {r:>10.4f}")

# Now train tiny char-LMs for a subset of dims to measure actual loss
import torch
import torch.nn as nn

torch.manual_seed(42)
text = "".join(chr(32 + (i * 7 + 13) % 95) for i in range(20000))  # synthetic text
chars = sorted(set(text))
stoi = {c: i for i, c in enumerate(chars)}
data = torch.tensor([stoi[c] for c in text], dtype=torch.long)
vocab = len(chars)
seq_len, batch = 32, 32

def make_batches(data, seq_len, batch):
    n = len(data) - seq_len - 1
    xs, ys = [], []
    for _ in range(batch * 50):  # 50 batches worth
        i = torch.randint(0, n, (1,)).item()
        xs.append(data[i:i+seq_len])
        ys.append(data[i+1:i+seq_len+1])
    xs = torch.stack(xs).reshape(-1, batch, seq_len)
    ys = torch.stack(ys).reshape(-1, batch, seq_len)
    return xs, ys

xs, ys = make_batches(data, seq_len, batch)

class TinyLM(nn.Module):
    def __init__(self, d_model, n_heads=4, n_layers=2):
        super().__init__()
        self.emb = nn.Embedding(vocab, d_model)
        self.pos = nn.Embedding(seq_len, d_model)
        layer = nn.TransformerEncoderLayer(d_model, n_heads, d_model*4, dropout=0, batch_first=True)
        self.tf = nn.TransformerEncoder(layer, n_layers)
        self.out = nn.Linear(d_model, vocab)
    def forward(self, x):
        pos = torch.arange(x.size(1), device=x.device)
        h = self.emb(x) + self.pos(pos)
        mask = nn.Transformer.generate_square_subsequent_mask(x.size(1), device=x.device)
        return self.out(self.tf(h, mask=mask))

test_dims = [60, 64, 120, 128, 240, 256]  # keep it fast
results = []
for d in test_dims:
    nh = 4 if d % 4 == 0 else (3 if d % 3 == 0 else 2)
    model = TinyLM(d, nh, 2)
    nparams = sum(p.numel() for p in model.parameters())
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.CrossEntropyLoss()
    t0 = time.time()
    for step in range(200):
        bi = step % xs.size(0)
        logits = model(xs[bi])
        loss = loss_fn(logits.reshape(-1, vocab), ys[bi].reshape(-1))
        opt.zero_grad(); loss.backward(); opt.step()
    final_loss = loss.item()
    elapsed = time.time() - t0
    r_val = R(d)
    results.append((d, r_val, tau(d), nparams, final_loss, elapsed))
    print(f"d={d:>4} R={r_val:.4f} tau={tau(d):>3} params={nparams:>8} loss={final_loss:.4f} time={elapsed:.1f}s")

print("\n" + "=" * 60)
print("CORRELATION ANALYSIS")
print("=" * 60)
import statistics
rs = [r[1] for r in results]
losses = [r[4] for r in results]
params = [r[3] for r in results]
# Spearman rank correlation (manual)
def rank(arr):
    indexed = sorted(enumerate(arr), key=lambda x: x[1])
    ranks = [0]*len(arr)
    for r, (i, _) in enumerate(indexed): ranks[i] = r
    return ranks

def spearman(a, b):
    ra, rb = rank(a), rank(b)
    n = len(a)
    d2 = sum((ra[i]-rb[i])**2 for i in range(n))
    return 1 - 6*d2/(n*(n*n-1))

# Normalize loss by params (efficiency = -loss / params)
eff = [-l/p for l, p in zip(losses, params)]
print(f"Spearman(R, raw_loss):        {spearman(rs, losses):.4f}")
print(f"Spearman(R, loss/params):     {spearman(rs, [-l/p for l,p in zip(losses,params)]):.4f}")
print(f"Spearman(tau, raw_loss):      {spearman([r[2] for r in results], losses):.4f}")
print(f"Spearman(params, raw_loss):   {spearman(params, losses):.4f}")

# Compare matched pairs
print("\n--- Matched Pair Comparisons (HCN vs 2^k) ---")
pairs = [(60,64), (120,128), (240,256)]
for h, p2 in pairs:
    rh = [r for r in results if r[0]==h][0]
    rp = [r for r in results if r[0]==p2][0]
    print(f"d={h} vs d={p2}: loss {rh[4]:.4f} vs {rp[4]:.4f}, params {rh[3]} vs {rp[3]}, R {rh[1]:.2f} vs {rp[1]:.2f}")
