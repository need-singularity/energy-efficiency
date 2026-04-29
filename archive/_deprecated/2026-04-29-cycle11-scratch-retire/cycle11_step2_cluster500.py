#!/usr/bin/env python3
"""
HEXA-WEAVE W5 Alt-2 cycle 11 fan-out 3/5 — Step 2.

Reads /tmp/cdhit_emul_cycle11_step1_data.json (500 FASTA records).
- Extracts first protein chain (≥30 aa, AA alphabet) from each entry.
- Pairwise difflib.SequenceMatcher.ratio() on first 300 aa.
- Greedy 30%-id clustering (length-descending seed order).
- Cluster-aware 80/10/10 split with deterministic seed.
- Writes /tmp/cdhit_emul_cycle11_step2_clusters.json
"""
import json
import time
import difflib
import hashlib
import random

STEP1 = "/tmp/cdhit_emul_cycle11_step1_data.json"
STEP2 = "/tmp/cdhit_emul_cycle11_step2_clusters.json"
ID_THRESHOLD = 0.30
PROT_PREFIX_AA = 300
MIN_PROT_LEN = 30
RNA_NUC_SET = set("ACGU")  # check if predominantly RNA
AA_SET = set("ACDEFGHIKLMNPQRSTVWY")
SPLIT_TRAIN = 0.80
SPLIT_VAL = 0.10
# split test = 1 - train - val

def parse_first_protein_chain(fasta_text):
    """Return (chain_label, sequence) of first protein-like chain ≥MIN_PROT_LEN aa, else None."""
    chains = []
    cur_label = None
    cur_seq = []
    for line in fasta_text.splitlines():
        if line.startswith(">"):
            if cur_label is not None:
                chains.append((cur_label, "".join(cur_seq).strip()))
            cur_label = line[1:]
            cur_seq = []
        else:
            cur_seq.append(line.strip())
    if cur_label is not None:
        chains.append((cur_label, "".join(cur_seq).strip()))

    for label, seq in chains:
        if len(seq) < MIN_PROT_LEN:
            continue
        # Heuristic: protein chain has ≥2 distinct AA-only residues outside RNA alphabet (DEFHIKLMNPQRSTVWY).
        non_rna = set(seq.upper()) - RNA_NUC_SET - {"N", "T"}
        protein_residues = non_rna & AA_SET
        if len(protein_residues) >= 5:  # robust protein detection
            return label, seq.upper()
    return None

def main():
    t0 = time.time()
    with open(STEP1) as f:
        d = json.load(f)
    records = d["fasta_records"]
    print(f"[cycle11/step2] loaded {len(records)} fasta records", flush=True)

    # Extract first protein chains
    extracted = []
    no_protein = []
    for rec in records:
        pid = rec["pdb_id"]
        parsed = parse_first_protein_chain(rec["fasta"])
        if parsed is None:
            no_protein.append(pid)
        else:
            label, seq = parsed
            extracted.append({"pdb_id": pid, "chain_label": label, "seq": seq, "len": len(seq)})

    print(f"[cycle11/step2] protein chains extracted: {len(extracted)}/{len(records)} (no_protein={len(no_protein)})", flush=True)
    if len(no_protein):
        print(f"[cycle11/step2] sample no-protein IDs: {no_protein[:10]}", flush=True)

    # Stats
    lens = [r["len"] for r in extracted]
    lens_sorted = sorted(lens)
    median_len = lens_sorted[len(lens_sorted)//2] if lens_sorted else 0
    min_len = min(lens) if lens else 0
    max_len = max(lens) if lens else 0
    print(f"[cycle11/step2] seq len stats: median={median_len} min={min_len} max={max_len}", flush=True)

    # Pairwise
    n = len(extracted)
    pairs_total = n * (n - 1) // 2
    print(f"[cycle11/step2] pairwise on N={n} → {pairs_total} pairs (difflib, prefix={PROT_PREFIX_AA}aa)", flush=True)

    seqs_pref = [r["seq"][:PROT_PREFIX_AA] for r in extracted]
    sim_above_30 = 0
    sum_ratio = 0.0
    max_ratio = 0.0
    # We won't store the full N×N matrix (would be 1.0M floats = ~8 MB) — OK actually, keep dict of edges ≥0.30 for cluster recall
    edges = {}  # (i, j) -> ratio (i<j)

    t_pair_start = time.time()
    progress_every = 50
    for i in range(n):
        si = seqs_pref[i]
        for j in range(i + 1, n):
            r = difflib.SequenceMatcher(None, si, seqs_pref[j], autojunk=False).ratio()
            sum_ratio += r
            if r > max_ratio:
                max_ratio = r
            if r >= ID_THRESHOLD:
                sim_above_30 += 1
                edges[(i, j)] = r
        if (i + 1) % progress_every == 0:
            elapsed = time.time() - t_pair_start
            done_pairs = sum((n - 1 - k) for k in range(i + 1))  # not exact; rough
            print(f"[cycle11/step2] processed row {i+1}/{n} elapsed={elapsed:.1f}s edges_so_far={sim_above_30}", flush=True)
    pair_dt = time.time() - t_pair_start
    mean_ratio = sum_ratio / pairs_total if pairs_total else 0.0
    throughput = pairs_total / pair_dt if pair_dt > 0 else 0.0
    print(f"[cycle11/step2] pairwise DONE pairs={pairs_total} t={pair_dt:.2f}s tput={throughput:.1f} p/s", flush=True)
    print(f"[cycle11/step2] mean_ratio={mean_ratio:.4f} max_ratio={max_ratio:.4f} pairs≥30%={sim_above_30}", flush=True)

    # Greedy clustering — sort by length descending
    order = sorted(range(n), key=lambda k: -extracted[k]["len"])
    cluster_of = [None] * n
    clusters = []  # list of {rep_idx, members: [idx]}
    for idx in order:
        # Try to attach to first existing cluster whose rep is similar
        attached = False
        for c in clusters:
            rep = c["rep_idx"]
            a, b = (rep, idx) if rep < idx else (idx, rep)
            r = edges.get((a, b), 0.0)
            if r >= ID_THRESHOLD:
                c["members"].append(idx)
                cluster_of[idx] = c["cl_id"]
                attached = True
                break
        if not attached:
            cl_id = len(clusters)
            clusters.append({"cl_id": cl_id, "rep_idx": idx, "members": [idx]})
            cluster_of[idx] = cl_id

    sizes = sorted([len(c["members"]) for c in clusters], reverse=True)
    n_singleton = sum(1 for s in sizes if s == 1)
    n_ge5 = sum(1 for s in sizes if s >= 5)
    print(f"[cycle11/step2] clusters={len(clusters)} singletons={n_singleton} ≥5={n_ge5} top10={sizes[:10]}", flush=True)

    # Top-10 by size
    cl_sorted = sorted(clusters, key=lambda c: -len(c["members"]))[:10]
    top10 = []
    for c in cl_sorted:
        rep = extracted[c["rep_idx"]]
        member_pids = [extracted[m]["pdb_id"] for m in c["members"]]
        top10.append({
            "cl_id": c["cl_id"],
            "rep_pdb": rep["pdb_id"],
            "rep_len": rep["len"],
            "size": len(c["members"]),
            "members_first5": member_pids[:5],
        })

    # Cluster-aware 80/10/10 split (deterministic seed)
    cl_ids = [c["cl_id"] for c in clusters]
    cl_ids_sorted = sorted(cl_ids)
    seed_str = ",".join(extracted[c["rep_idx"]]["pdb_id"] for c in clusters)
    seed_int = int(hashlib.sha256(seed_str.encode()).hexdigest()[:16], 16)
    rng = random.Random(seed_int)
    shuffled = list(cl_ids_sorted)
    rng.shuffle(shuffled)
    n_total = len(shuffled)
    n_train = int(n_total * SPLIT_TRAIN)
    n_val = int(n_total * SPLIT_VAL)
    n_test = n_total - n_train - n_val
    train_cl = set(shuffled[:n_train])
    val_cl = set(shuffled[n_train:n_train + n_val])
    test_cl = set(shuffled[n_train + n_val:])

    train_pdbs, val_pdbs, test_pdbs = [], [], []
    for c in clusters:
        pids = [extracted[m]["pdb_id"] for m in c["members"]]
        if c["cl_id"] in train_cl:
            train_pdbs.extend(pids)
        elif c["cl_id"] in val_cl:
            val_pdbs.extend(pids)
        elif c["cl_id"] in test_cl:
            test_pdbs.extend(pids)
    inter = (set(train_pdbs) & set(val_pdbs)) | (set(train_pdbs) & set(test_pdbs)) | (set(val_pdbs) & set(test_pdbs))
    print(f"[cycle11/step2] split: train_cl={len(train_cl)}/{len(train_pdbs)}pdb val_cl={len(val_cl)}/{len(val_pdbs)}pdb test_cl={len(test_cl)}/{len(test_pdbs)}pdb intersection={len(inter)}", flush=True)

    out = {
        "meta": {
            "schema": "n6/hexa-weave/cycle11/cdhit_emul_step2/v1",
            "n_records_input": len(records),
            "n_extracted": len(extracted),
            "n_no_protein": len(no_protein),
            "id_threshold": ID_THRESHOLD,
            "prot_prefix_aa": PROT_PREFIX_AA,
            "pairs_total": pairs_total,
            "pair_seconds": round(pair_dt, 3),
            "throughput_p_s": round(throughput, 1),
            "mean_ratio": round(mean_ratio, 4),
            "max_ratio": round(max_ratio, 4),
            "pairs_above_30pct": sim_above_30,
            "n_clusters": len(clusters),
            "n_singletons": n_singleton,
            "n_clusters_ge5": n_ge5,
            "top10_sizes": sizes[:10],
            "split_seed_int": seed_int,
            "split_seed_hex": hex(seed_int),
            "split_n_train_cl": len(train_cl),
            "split_n_val_cl": len(val_cl),
            "split_n_test_cl": len(test_cl),
            "split_n_train_pdb": len(train_pdbs),
            "split_n_val_pdb": len(val_pdbs),
            "split_n_test_pdb": len(test_pdbs),
            "split_intersection_count": len(inter),
            "median_seq_len": median_len,
            "min_seq_len": min_len,
            "max_seq_len": max_len,
            "wall_clock_total_s": round(time.time() - t0, 3),
            "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        },
        "no_protein_pdbs": no_protein,
        "top10_clusters": top10,
        "split": {
            "train_pdbs": sorted(set(train_pdbs)),
            "val_pdbs": sorted(set(val_pdbs)),
            "test_pdbs": sorted(set(test_pdbs)),
        },
    }
    with open(STEP2, "w") as f:
        json.dump(out, f)
    print(f"[cycle11/step2] DONE wall={out['meta']['wall_clock_total_s']}s wrote={STEP2}", flush=True)

if __name__ == "__main__":
    main()
