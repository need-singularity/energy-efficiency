#!/usr/bin/env python3
import re, json, random, statistics
from collections import defaultdict, Counter
from itertools import combinations

txt = open('/Users/ghost/Dev/n6-architecture/docs/breakthrough-theorems.md').read()
parts = re.split(r'\n## BT-(\d+)', txt)
bts = {}
for i in range(1, len(parts), 2):
    bts[int(parts[i])] = parts[i+1]
print('BT count:', len(bts))

norm = {'σ':'sigma','sigma':'sigma','τ':'tau','tau':'tau','φ':'phi','phi':'phi','sopfr':'sopfr','Ω':'sopfr'}
pat = re.compile(r'(σ|sigma|τ|tau|φ|phi|sopfr|Ω)\s*[=:\(]\s*(\d+)')
bt_sigs = defaultdict(set)
for bid, body in bts.items():
    for m in pat.finditer(body[:4000]):
        bt_sigs[bid].add((norm[m.group(1)], int(m.group(2))))
with_sigs = sum(1 for v in bt_sigs.values() if v)
print('BTs with sigs:', with_sigs)

sig_freq = defaultdict(int)
for sigs in bt_sigs.values():
    for s in sigs:
        sig_freq[s] += 1
rare_cutoff = max(2, int(0.08 * with_sigs))
rare_sigs = {s for s, c in sig_freq.items() if c <= rare_cutoff}
print(f'sig_freq distinct={len(sig_freq)} rare_cutoff={rare_cutoff} rare_sigs={len(rare_sigs)}')

edges = []
bids = sorted(bt_sigs.keys())
for a, b in combinations(bids, 2):
    sh = bt_sigs[a] & bt_sigs[b]
    if len(sh) >= 2 or (sh & rare_sigs):
        edges.append((a, b, len(sh)))
print('structural edges:', len(edges))

deg = defaultdict(int)
adj = defaultdict(set)
for a, b, _ in edges:
    deg[a] += 1; deg[b] += 1
    adj[a].add(b); adj[b].add(a)
top = sorted(deg.items(), key=lambda x: -x[1])[:10]
print('top hubs:', top)

def bfs(src):
    seen = {src: 0}; q = [src]
    while q:
        nq = []
        for u in q:
            for v in adj[u]:
                if v not in seen:
                    seen[v] = seen[u] + 1; nq.append(v)
        q = nq
    far = max(seen.items(), key=lambda x: x[1])
    return far, seen

if not bids:
    print('no bids'); exit()
(f1, _), _ = bfs(bids[0])
(f2, d2), _ = bfs(f1)
print('diameter approx:', d2, 'endpoints:', f1, f2)

sample = random.sample(bids, min(150, len(bids)))
lens = []
for s in sample:
    _, dd = bfs(s)
    lens.extend(v for v in dd.values() if v > 0)
dist = dict(sorted(Counter(lens).items()))
print('path len dist:', dist)

# giant component
seen = set(); comps = []
for s in bids:
    if s in seen: continue
    st = [s]; c = 0
    while st:
        u = st.pop()
        if u in seen: continue
        seen.add(u); c += 1
        for v in adj[u]:
            if v not in seen: st.append(v)
    comps.append(c)
real_giant = max(comps)
print('real giant:', real_giant, '/', len(bids))

N = len(bids); E = len(edges)
# Null model: shuffle signature assignments across BTs (preserve per-BT signature count distribution)
all_sigs_pool = []
for sigs in bt_sigs.values():
    all_sigs_pool.extend(sigs)
per_bt_sizes = [(bid, len(s)) for bid, s in bt_sigs.items() if s]

def null_trial():
    pool = all_sigs_pool[:]
    random.shuffle(pool)
    idx = 0
    fake = {}
    for bid, sz in per_bt_sizes:
        fake[bid] = set()
        tries = 0
        while len(fake[bid]) < sz and idx < len(pool) and tries < sz * 5:
            fake[bid].add(pool[idx]); idx += 1; tries += 1
        if idx >= len(pool): idx = 0
    # rebuild rare set based on shuffled frequencies
    fsf = defaultdict(int)
    for s in fake.values():
        for x in s: fsf[x] += 1
    frare = {s for s, c in fsf.items() if c <= rare_cutoff}
    # count edges and giant
    fbids = sorted(fake.keys())
    fadj = defaultdict(set); fe = 0
    for a, b in combinations(fbids, 2):
        sh = fake[a] & fake[b]
        if len(sh) >= 2 or (sh & frare):
            fadj[a].add(b); fadj[b].add(a); fe += 1
    sn = set(); big = 0
    for s in fbids:
        if s in sn: continue
        st = [s]; c = 0
        while st:
            u = st.pop()
            if u in sn: continue
            sn.add(u); c += 1
            for v in fadj[u]:
                if v not in sn: st.append(v)
        if c > big: big = c
    return fe, big

print('running null model (50 trials)...')
rs_e, rs_g = [], []
for _ in range(50):
    fe, fg = null_trial()
    rs_e.append(fe); rs_g.append(fg)
mu_e = statistics.mean(rs_e); sd_e = statistics.pstdev(rs_e) or 1
z_edges = (E - mu_e) / sd_e
print(f'null edges: mean={mu_e:.1f} sd={sd_e:.1f} real={E} z={z_edges:.2f}')
rs = rs_g
mu = statistics.mean(rs); sd = statistics.pstdev(rs) or 1
z = (real_giant - mu) / sd
print(f'random giant mean={mu:.2f} sd={sd:.2f} z={z:.3f}')

# path density: edges / C(N,2)
density = E / (N*(N-1)/2)
print(f'path density: {density:.4f}')

# longest simple path on giant (approx via DFS from hub, limited)
def longest_from(src, cap=20):
    best = [src]
    def dfs(u, path, visited):
        nonlocal best
        if len(path) > len(best): best = path[:]
        if len(path) >= cap: return
        for v in adj[u]:
            if v not in visited:
                visited.add(v); path.append(v)
                dfs(v, path, visited)
                path.pop(); visited.remove(v)
    dfs(src, [src], {src})
    return best
hub_bid = top[0][0] if top else bids[0]
lp = longest_from(hub_bid, cap=15)
print('longest simple path from hub (capped):', len(lp), lp[:20])

out = {
    'bt_total': len(bts),
    'bt_with_sigs': with_sigs,
    'structural_edges': E,
    'diameter_approx': d2,
    'diameter_endpoints': [f1, f2],
    'top_hubs': top,
    'path_len_dist': dist,
    'path_len_mean': round(statistics.mean(lens), 2) if lens else 0,
    'giant_component': real_giant,
    'random_giant_mean': round(mu, 2),
    'random_giant_sd': round(sd, 2),
    'z_score': round(z, 3),
    'path_density': round(density, 4),
    'longest_path_hub_cap15': lp,
}
json.dump(out, open('/tmp/bt_structural_stats.json', 'w'), ensure_ascii=False, indent=2)
print('saved /tmp/bt_structural_stats.json')
