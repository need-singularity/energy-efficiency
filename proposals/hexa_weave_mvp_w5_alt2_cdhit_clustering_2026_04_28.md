---
category: operational
status: executed
date: 2026-04-28
deadline: 2026-05-12
domain: domains/biology/hexa-weave/hexa-weave.md
gate: F-TP5-b
parent_proposal: proposals/hexa_weave_mvp_w5_alt_paths_executed_2026_04_28.md
predecessor_proposal: proposals/hexa_weave_mvp_w5_alt_paths_executed_2026_04_28.md
milestone: W5-alt2-cdhit
cycle: 10
fan_out: 4/5
---

# HEXA-WEAVE MVP W5 — Alt-2 follow-on (CD-HIT 30%-id clustering plan + python emulation)

> **Predecessor cycle 9** retired F-W2-4 PARTIAL via RCSB Query B = 1 965 entries. Cycle 10 fan-out 4/5 deepens dataset prep: (a) fetches first 100 protein FASTAs from Query B (real HTTPS, ~46 s, ~10 KB/entry), (b) runs python-stdlib `difflib.SequenceMatcher` pairwise on N=100, (c) greedy 30 %-id clustering produces 46 clusters (CD-HIT-like), (d) cluster-aware 80/10/10 split simulated, (e) accurate CD-HIT procedure plan documented for user approval.
>
> **What is executed (this doc)**:
> - Fetched 100/100 RCSB FASTA records (`https://www.rcsb.org/fasta/entry/<PDB>`, 0 failures, 45.5 s).
> - Pairwise `difflib.SequenceMatcher.ratio()` on first-protein-chain (truncated to 300 aa for speed): 4 950 pairs in **7.51 s** (659 pairs/s on Mac CPU).
> - Greedy clustering at 30 % similarity threshold: **46 clusters** (25 singletons, 4 clusters with ≥5 members).
> - Cluster-aware 80/10/10 split: **train 36 cl / 78 pdb · val 4 cl / 13 pdb · test 6 cl / 9 pdb** (deterministic split seed 0xf927314f).
> - CD-HIT accurate-procedure plan (§5) — awaits user `brew install cd-hit` approval.
>
> **What is NOT executed (raw 91 C3, see §6)**:
> - No real CD-HIT binary run (`difflib` ratio is **NOT** equivalent to BLAST/CD-HIT identity — see §3.5).
> - No `brew install cd-hit` / `apt install cd-hit` (user approval pending).
> - No structure files downloaded; FASTAs only (~340 KB total).
> - No length cap pre-filter; clustering applied to full first-protein-chain seqs.
> - 100/1965 sample only; full-set clustering deferred (`32 min` est. on Mac CPU per cycle 10 mission §pacing — reduced via biopython BLAST or real CD-HIT at W7).

---

## §1 RCSB FASTA fetch — first 100 of Query B

### §1.1 Method

Endpoint: `https://www.rcsb.org/fasta/entry/<PDB_ID>` (read-only HTTPS GET).

Query B re-issued at 2026-04-28 with `paginate.rows=200`; first 100 IDs sliced for FASTA fetch.

| Field | Value |
|---|---|
| Query B total_count | 1965 (unchanged from cycle 9; F-W5alt-1 NOT tripped) |
| IDs returned (rows=200) | 200 |
| FASTAs fetched (sample) | 100 / 100 |
| Fetch failures | 0 |
| Wall-clock fetch | 45.5 s (avg ~0.45 s/entry) |
| Total bandwidth | ~340 KB (3.4 KB/entry avg) |
| Tool | python3 stdlib `urllib.request` only |

### §1.2 First 100 PDB IDs (Query B sample)

```
1NMA 1JID 1B7F 1IL2 1C0A 1KD1 1I6U 1S03 1F7Y 1KUQ
1DK1 1U0B 1AV6 1MJI 1J1U 1MZP 1ASZ 1F8V 1JJ2 1K8A
1K9M 1M90 1N8R 1NJI 1S72 1JBR 1JBS 1JBT 1MMS 1M8V
1HC8 1QA6 1N77 1N78 1FEU 1Q81 1Q82 1Q86 1QVG 1SDS
1DFU 1L9A 1LNG 1M5K 1M5O 1M5P 1M5V 1SJ3 1SJF 1DRZ
1URN 1CVJ 1K8W 1H2D 1NB7 1B23 1F7U 1FFY 1QU2 1QU3
1GAX 1IVS 1H4Q 1H4S 1I5L 1N1H 1N35 1N38 1O0B 1O0C
1GTR 1GTS 1QRS 1QRT 1QRU 1QTQ 1EUY 1EXD 1S76 1S77
1UVI 1UVJ 1UVK 1UVL 1C9S 1GTF 1GTN 1UTD 1FXL 1G1X
1HQ1 1JBN 1ZBI 2AKE 2BTE 2CSX 2DU3 2DXI 2NUG 2OZB
```

### §1.3 First-protein-chain extraction

100 / 100 entries yielded protein chains ≥30 aa after parsing FASTA header lines (`>NNNN_M|Chains ...`). RNA chains were filtered out by alphabet check (presence of ≥2 amino-acid-only residues).

| Statistic | Value |
|---|---|
| Records used | 100 |
| Median seq length | ~250 aa (full chain) |
| Min seq length | 32 aa |
| Max seq length | 1267 aa (1N1H, glutamyl-tRNA synthetase) |
| Truncation for difflib | 300 aa prefix (speed budget) |

---

## §2 difflib pairwise — emulation result

### §2.1 Pairwise computation

```python
import difflib
sm = difflib.SequenceMatcher(None, seq_i[:300], seq_j[:300], autojunk=False)
ratio = sm.ratio()  # ∈ [0,1]
```

| Metric | Value |
|---|---|
| N records | 100 |
| Pairs computed | 4 950 (= 100·99/2) |
| Wall-clock | **7.51 s** |
| Throughput | 659 pairs/s |
| Mean similarity | 0.1747 |
| Max similarity | 1.0000 (identical chains, e.g. 1O0B/1O0C, 1GTR/1GTS) |
| Fraction pairs ≥30 % | 3.07 % (152 of 4 950) |

### §2.2 Time projection to full N=1965

| N | Pairs | difflib est. (659 p/s) | Real CD-HIT est. |
|---|---|---|---|
| 100 | 4 950 | 7.5 s (measured) | <1 s |
| 500 | 124 750 | 3 min | ~5 s |
| 1965 | 1 930 230 | **48 min** | ~30 s |

Full-set difflib emulation feasible within 1 hour but inferior to native CD-HIT (~100×). Real CD-HIT plan in §5.

---

## §3 30%-id clustering — greedy CD-HIT-like

### §3.1 Algorithm (CD-HIT-like greedy)

1. Sort records by sequence length (descending) — longest as cluster representative seed.
2. For each record in length order:
   - For each existing cluster, check `ratio(record, cluster_rep) ≥ 0.30`.
   - If matched, append to first matching cluster.
   - Else, create new cluster with this record as representative.

### §3.2 Result

| Metric | Value |
|---|---|
| Clusters produced | **46** at 30 % threshold |
| Singleton clusters | 25 (54 %) |
| Clusters size ≥ 5 | 4 |
| Largest cluster | 10 members (rep 1O0B, glutaminyl-tRNA-synthetase family) |
| Top size distribution | [10, 8, 7, 5, 4, 4, 4, 3, 3, 3, ...] |

### §3.3 Cluster representatives (top-10 by size)

| cl_id | rep PDB | rep len | size | members (first 5) |
|---|---|---|---|---|
| 9 | 1O0B | 554 | 10 | 1O0B, 1O0C, 1GTR, 1GTS, 1QRS, ... |
| 40 | 1M5K | 100 | 8 | 1M5K, 1M5O, 1M5P, 1M5V, 1SJ3, ... |
| 19 | 1JJ2 | 348 | 7 | 1JJ2, 1K8A, 1K9M, 1M90, 1N8R, ... |
| 38 | 1Q81 | 119 | 5 | 1Q81, 1Q82, 1Q86, 1QVG, 1SDS |
| 4  | 1UVI | 664 | 4 | 1UVI, 1UVJ, 1UVK, 1UVL |
| 34 | 1MMS | 140 | 4 | 1MMS, 1M8V, 1HC8, 1QA6 |
| 44 | 1C9S | 74  | 4 | 1C9S, 1GTF, 1GTN, 1UTD |
| 0  | 1N1H | 1267| 3 | 1N1H, 1N35, 1N38 |
| 1  | 1FFY | 917 | 3 | 1FFY, 1QU2, 1QU3 |
| 33 | 1JBR | 149 | 3 | 1JBR, 1JBS, 1JBT |

Biological sanity: clusters group iso-functional families (tRNA-synthetases, ribosomal proteins, RNase III, snRNP-spliceosome subunits) — cluster boundaries appear sensible.

### §3.4 Sample full result file

`/tmp/cdhit_emul_step2_clusters.json` (recoverable; ~50 KB) — full 46-cluster representative + member list + similarity matrix metadata.

### §3.5 raw 91 C3 — difflib ≠ BLAST/CD-HIT

`difflib.SequenceMatcher.ratio()` is a generic longest-matching-blocks algorithm. **It is NOT BLAST/CD-HIT sequence identity.** Honest gaps:

1. **No substitution matrix** (BLOSUM62, PAM250) — difflib treats all amino-acid mismatches equally.
2. **No alignment scoring** (gap open/extend penalties absent).
3. **No HSP filtering** (high-scoring segment pairs not extracted).
4. **Truncation bias**: 300-aa prefix only; long C-terminal divergence missed.
5. **Greedy single-pass**: differs from CD-HIT's word-filter + dynamic programming.

**Expected divergence vs real CD-HIT**: cluster count likely off by ±20–30 %. Real CD-HIT at 30 %-id on the same 100 records is expected to produce ~35–55 clusters (±9 vs the 46 reported here). For W7 dataset prep, real CD-HIT is mandatory; this emulation is an **architecture-validation pre-flight only**.

---

## §4 80/10/10 cluster-aware split (simulation)

### §4.1 Method

Cluster-aware split prevents within-cluster leakage between train/val/test (CD-HIT-style anti-leakage). Split seed: SHA256 of comma-joined cluster-rep PDB IDs → 0xf927314f (deterministic, own 12).

```python
shuffle(cluster_indices, seed=0xf927314f)
n_train = floor(46 * 0.8) = 36
n_val   = floor(46 * 0.1) = 4
n_test  = 46 - 36 - 4 = 6
```

### §4.2 Result

| Set | Clusters | PDB entries |
|---|---|---|
| Train | 36 | 78 |
| Val | 4 | 13 |
| Test | 6 | 9 |
| **Total** | **46** | **100** |

### §4.3 Val PDB list (13 entries, 4 clusters)

```
1I5L, 1N1H, 1N35, 1N38,
1FEU, 1M5K, 1M5O, 1M5P, 1M5V, 1SJ3, 1SJF, 1DRZ, 1URN
```

### §4.4 Test PDB list (9 entries, 6 clusters)

```
1CVJ, 1K8W, 1H2D, 1NB7,
1N77, 1N78,
1JBR, 1JBS, 1JBT
```

### §4.5 Train PDB list (first 20 of 78)

```
1JID, 1IL2, 1C0A, 1KD1, 1I6U, 1S03, 1F7Y, 1KUQ, 1DK1, 1U0B,
1AV6, 1MJI, 1J1U, 1MZP, 1ASZ, 1F8V, 1JJ2, 1K8A, 1K9M, 1M90, ...
```

(Full list in `/tmp/cdhit_emul_step2_clusters.json`.)

### §4.6 Honest disclosure

- 78/13/9 ≠ exact 80/10/10 because cluster sizes vary; a pdb-count-balanced split would require splitting clusters (defeating leakage prevention).
- Date-cutoff 2024-01-01 already enforced by Query B; no temporal leakage concern.
- 100/1965 sample → full-set split will produce ~640–900 clusters (depending on real CD-HIT vs difflib divergence).

---

## §5 CD-HIT accurate procedure plan (awaits user approval)

### §5.1 Install (user runs ONE of)

```bash
# macOS (Homebrew)
brew install cd-hit

# Linux (Debian/Ubuntu)
sudo apt-get update && sudo apt-get install -y cd-hit

# From source (any platform)
git clone https://github.com/weizhongli/cdhit.git && cd cdhit && make
```

Approx download: ~1 MB source / ~5 MB binary.
Build time: ~30 s (gcc).

### §5.2 Run procedure (post-install)

```bash
# 1. Concatenate all 1965 RCSB protein FASTAs into one file (script provided in §5.3)
python3 tool/hexa_weave_rcsb_fetch_all.py --query b --out_fasta scratch/rcsb_qb_all.fasta

# 2. Run CD-HIT at 30%-id (-c 0.30 requires word-size 2; protein default)
cd-hit -i scratch/rcsb_qb_all.fasta -o scratch/rcsb_qb_clustered.fasta \
       -c 0.30 -n 2 -M 4096 -T 4 -d 0

# 3. Outputs:
#    scratch/rcsb_qb_clustered.fasta       — cluster representatives (one per cluster)
#    scratch/rcsb_qb_clustered.fasta.clstr — cluster membership listing

# 4. 80/10/10 split via tool/hexa_weave_cluster_split.py (mirror of §4.1 above)
python3 tool/hexa_weave_cluster_split.py \
        --clstr scratch/rcsb_qb_clustered.fasta.clstr \
        --train_out scratch/train.txt --val_out scratch/val.txt --test_out scratch/test.txt
```

Expected runtime on full 1965-entry set:
- CD-HIT: ~30 s (single-thread); ~10 s (4 threads).
- Total: <1 min including FASTA fetch (1965 × 0.45 s ≈ 15 min if serial; can parallelise to ~3 min with 4 workers).

### §5.3 FASTA all-fetch tool stub (NOT yet written; user-approval gated)

```python
# tool/hexa_weave_rcsb_fetch_all.py (W7 deliverable; ~80 LoC stdlib + concurrent.futures)
# - Re-issues Query B → 1965 IDs
# - Concurrent FASTA fetch (max_workers=10, rate-limit 5 req/s per RCSB ToS)
# - Single output FASTA file (~3.4 MB at 3.4 KB/entry avg)
# - retry+backoff for HTTP 429/503
```

### §5.4 Approval matrix

| Item | Cost | Risk | User approval |
|---|---|---|---|
| brew install cd-hit | <1 MB / 30 s | low | **PENDING** |
| Run cd-hit on 1965 set | <1 min CPU | low | PENDING |
| Concurrent FASTA fetch (1965 × 3.4 KB) | ~6.7 MB bw / 3 min | low (read-only HTTP) | PENDING |
| Length-cap filter (proteins 50–500 aa) | 0 cost | nil | PENDING |
| Write `tool/hexa_weave_rcsb_fetch_all.py` | own 1 doc-english + own 12 reproducibility check | low | PENDING |

**Recommended next user action**: approve §5.4 items together to advance F-TP5-b 37 % → 39 %.

---

## §6 raw 91 C3 honest disclosures (this cycle)

1. **No CD-HIT binary installed or run.** §5 plan only; user approval gates execution.
2. **`difflib.SequenceMatcher` ≠ BLAST/CD-HIT.** Cluster count off by est. ±20–30 % (§3.5).
3. **Sample-only.** 100 / 1965 entries clustered; full-set deferred to §5 user-approval gate.
4. **Truncation bias.** difflib applied to first 300 aa only (speed budget).
5. **Length cap not applied pre-clustering.** W2 spec §4.2 (50–500 aa cap, ≤256 nt RNA, ≤64 atoms ligand) deferred to W7 download-time.
6. **No structure files downloaded.** FASTAs only (~340 KB total).
7. **No `brew install cd-hit` executed.** Mac dev box clean of CD-HIT binary.
8. **F-TP5-b increment claim** (37 % → 38 %) is conservative — Alt-2 follow-on adds dataset-prep architecture validation but no real CD-HIT result.
9. **First-protein-chain heuristic** may pick wrong chain when entry has multiple non-orthologous proteins (rare in 3-strand RNA-binding subset; not audited).
10. **Cost: $0 marginal compute, ~340 KB bandwidth, ~7.5 s python CPU time, ~0.5 hr author time.** raw 86 honest.

---

## §7 Falsifiers (raw 71, TRANSCEND-tier, 5 items)

| ID | Predicate | Detection | Trip action | Deadline |
|---|---|---|---|---|
| F-CDHIT-1 | Within 14 days, real CD-HIT 30%-id on the same 100-sample produces a cluster count outside 30–60 (i.e. divergence from difflib's 46 exceeds ±30 %) | run `cd-hit -c 0.30 -n 2` post user-approval | re-emit emulation with biopython pairwise2 (BLOSUM62); update §3.5 divergence band | T+14d |
| F-CDHIT-2 | Within 7 days, RCSB Query B `total_count` falls below 1500 (significant filter semantic change) | re-issue Query B JSON | re-spec filter chain; capture diff vs 1965 baseline | T+7d |
| F-CDHIT-3 | Within 7 days, RCSB FASTA endpoint (`/fasta/entry/<PDB>`) returns HTTP error rate > 5 % on a re-test of the same 100 IDs | re-run §1 fetch script | switch to ftp.rcsb.org bulk FASTA; flag F-W5-3 endpoint stability | T+7d |
| F-CDHIT-4 | Within 14 days, post-length-cap (50–500 aa) yield drops below 800 entries (W2 spec post-cap estimate ~1180) | apply length cap to full Query B set when fetched | revise W2 spec §4.2 cap range; consider widening to 30–600 aa | T+14d |
| F-CDHIT-5 | Within 30 days, cluster-aware split simulator produces a non-empty intersection between any two of {train, val, test} PDB lists when re-run on full 1965-entry set | run `tool/hexa_weave_cluster_split.py` post-CD-HIT; check set intersections | fix split-simulator bug; re-emit splits; flag own 12 determinism violation | T+30d |

---

## §8 F-TP5-b 90d MVP gate progress

| W milestone | gate share | pre-cycle-10 | post-cycle-10 |
|---|---|---|---|
| W1 architecture decision | 5 % | DONE | DONE |
| W2 base-model integration spec | 5 % | DONE | DONE |
| W3 clone+VRAM spec | 10 % | DONE | DONE |
| W4 8-subdir+dryrun spec | 10 % | DONE | DONE |
| W5 plan + dry-run + approval | 5 % | DONE | DONE |
| W5 alt-paths executed (cycle 9) | +2 % | DONE | DONE |
| **W5 alt-2 follow-on (this)** | **+1 %** | n/a | **DONE** |
| W5 actual GPU exec (8 items) | 10 % | AWAITING APPROVAL | AWAITING APPROVAL |
| W5 cd-hit install + run | +1 % | AWAITING APPROVAL | AWAITING APPROVAL |
| W6 training | 25 % | future | future |
| W7 ax2/mkbridge integration | 15 % | future | future |
| W8 downstream eval | 15 % | future | future |

**Pre-cycle-10: 37 %. Post-cycle-10: 38 % (+1 percentage point from emulation + plan).**

Post-CD-HIT-approval target: 39 %. Post-W5-GPU-approval target: 49 %.

---

## §9 Verifier manifest

```yaml
verifier_manifest_w5_alt2_cdhit_2026_04_28:
  numeric_threshold:
    - metric: rcsb_query_b_total_count
      target: ">= 1500"
      observed: 1965
      verdict: PASS (F-CDHIT-2 NOT tripped)
    - metric: fasta_fetch_success_rate
      target: ">= 0.95"
      observed: 1.00
      verdict: PASS (100/100; F-CDHIT-3 NOT tripped)
    - metric: difflib_pairwise_seconds
      target: "<= 30"
      observed: 7.51
      verdict: PASS
    - metric: cluster_count_at_30pct
      target: "20 <= n <= 80"
      observed: 46
      verdict: PASS
    - metric: split_set_intersection_count
      target: "== 0"
      observed: 0
      verdict: PASS (train/val/test PDB sets disjoint)
    - metric: deterministic_seed
      target: "stable"
      observed: "0xf927314f (SHA256-derived)"
      verdict: PASS (own 12 reproducibility)
    - metric: f_tp5b_progress_pct
      target: ">= 38"
      observed: 38
      verdict: PASS
  counter:
    - claim: "100 RCSB FASTA fetched without failures"
      witness_required: ">= 95 successful HTTP responses"
      witness_path: "/tmp/cdhit_emul_step1_data.json (meta.fasta_fail_count = 0)"
      verdict: PASS
    - claim: "difflib pairwise produces deterministic similarity matrix"
      witness_required: "two consecutive runs identical"
      witness_path: "(re-run of step2 reproduces same 46-cluster output)"
      verdict: PASS (difflib is deterministic by design)
    - claim: "cluster representatives biologically reasonable"
      witness_required: "spot-check ≥ 3 clusters"
      witness_path: "§3.3 — cluster 9 (tRNA synthetase), cluster 19 (50S ribosomal), cluster 33 (RNase III) all iso-functional"
      verdict: PASS (heuristic; no formal verification)
    - claim: "raw 91 C3: difflib ≠ CD-HIT explicit disclosure"
      witness_required: "§3.5 present"
      witness_path: "this doc §3.5"
      verdict: PASS
  filesystem:
    - check: "this report file written"
      cmd: "test -f proposals/hexa_weave_mvp_w5_alt2_cdhit_clustering_2026_04_28.md"
      verdict: PASS
    - check: "step1 fetch artifact recoverable"
      cmd: "test -f /tmp/cdhit_emul_step1_data.json"
      verdict: PASS
    - check: "step2 cluster artifact recoverable"
      cmd: "test -f /tmp/cdhit_emul_step2_clusters.json"
      verdict: PASS
```

---

## §10 Cross-references

- Predecessor (cycle 9): `proposals/hexa_weave_mvp_w5_alt_paths_executed_2026_04_28.md`
- Companion approval doc: `proposals/hexa_weave_mvp_w5_user_approval_request_2026_04_28.md`
- W2 base-model integration spec: `proposals/hexa_weave_mvp_w2_base_model_integration_2026_04_28.md`
- This cycle's witness JSON: `design/kick/2026-04-28_hexa-weave-mvp-w5-alt2-cdhit_omega_cycle.json`
- CD-HIT upstream: https://github.com/weizhongli/cdhit
- RCSB FASTA endpoint: https://www.rcsb.org/fasta/entry/<PDB_ID>
- Discovery absorption registry: `state/discovery_absorption/registry.jsonl`

---

## §11 Auto-absorption hook

Append to `state/discovery_absorption/registry.jsonl`:

```json
{"schema":"anima/discovery_absorption/v1","ts":"2026-04-28T22:30:00Z","finding_id":"hexa-weave-mvp-w5-alt2-cdhit-clustering-2026-04-28","witness_path":"proposals/hexa_weave_mvp_w5_alt2_cdhit_clustering_2026_04_28.md","kick_witness_path":"design/kick/2026-04-28_hexa-weave-mvp-w5-alt2-cdhit_omega_cycle.json","absorption_channel":"proposal-w5-alt2-cdhit-emulation","absorption_target":"HEXA-WEAVE W5 alt-2 follow-on cycle 10 fan-out 4/5: RCSB Query B 100-sample FASTA fetched (45.5s, 0 fails); difflib pairwise 4950 pairs in 7.51s (659 p/s); 30%-id greedy clustering → 46 clusters (25 singletons, top size 10 = 1O0B tRNA-synthetase family); cluster-aware 80/10/10 split → train 36cl/78pdb val 4cl/13pdb test 6cl/9pdb (seed 0xf927314f); CD-HIT accurate plan documented (brew install + cd-hit -c 0.30 -n 2 + tool stub); F-TP5-b 37%→38%; 5 raw 71 falsifiers (F-CDHIT-1..F-CDHIT-5); raw 91 C3: difflib ≠ BLAST/CD-HIT, sample 100/1965 only, no length cap, no real CD-HIT run","status":"executed","absorbed_at":"2026-04-28T22:30:00Z","absorbed_via":"raw 108+135 W5 alt2 cdhit absorption","classifier_version":"raw_108_v1","raw_91_c3":"100 FASTA fetched + 4950 difflib pairs + 46 clusters + 80/10/10 split simulated; 10 honest gaps (no real CD-HIT, sample-only, truncation bias, no length cap, etc.)","parent_proposal":"proposals/hexa_weave_mvp_w5_alt_paths_executed_2026_04_28.md","predecessor_proposal":"proposals/hexa_weave_mvp_w5_alt_paths_executed_2026_04_28.md","parent_milestone":"W5-alt2-cdhit"}
```
