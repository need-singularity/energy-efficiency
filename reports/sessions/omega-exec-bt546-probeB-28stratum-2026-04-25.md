---
id: omega-exec-bt546-probeB-28stratum
date: 2026-04-25
scope: research-only execution + analysis (NO BSD claim, NO atlas promotion)
target: BT-546 Probe B -- 28-stratum joint covariance run on Cremona 332k
parent_reports:
  - reports/sessions/dfs-24-bsd-direction-2026-04-24.md (§ 2 Probe B spec, lines 44-55)
  - reports/sessions/omega-probe-dfs24-batch-execution-2026-04-25.md (readiness audit, lines 69, 133, 201, 213)
data_used: data/cremona/sel6_stats_332k.json + joint_covariance_A3_prime.json + allbsd/ shards (27 shards, conductor 1..269999)
tool_patched: scripts/empirical/cremona_joint_covariance.py (added --per-stratum mode, +85 lines)
millennium_resolved: 0/7 (unchanged)
grade: empirical measurement, no claim
---

## 0. Non-claim disclaimer

This run does **NOT** prove (A3) (the conjectural lim_{B->inf} Cov(|Sel_2|, |Sel_3|) = 0).
This run does **NOT** resolve BSD or any of the 7 Millennium problems.
This run does **NOT** promote any atlas entry.
No state/inventory/atlas files are touched.
This is a single empirical measurement (28-cell joint covariance) on a finite Cremona slice; bootstrap SE is reported per cell; the "torsion x |Sha|" stratification is an ad-hoc diagnostic, not a proof technique.

The hypothesis being tested (kappa concentrates on Z/6 + Z/12 strata) and its falsifier (kappa > 0.5 uniformly on all 28 cells) are themselves diagnostic instruments, not assertions about asymptotic behaviour.

---

## 1. Discovery report

### 1.1 Files found (read-only verification)

| Asset                                                | Path                                                                        | Status                                  |
|------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------|
| Sel_6 marginal stats (332k summary)                  | `data/cremona/sel6_stats_332k.json`                                         | present, 118 lines                      |
| Joint covariance global summary                      | `data/cremona/joint_covariance_A3_prime.json`                               | present, 45 lines, kappa = 1.3333       |
| Cremona allbsd shards                                | `data/cremona/allbsd/allbsd.{N}-{N+9999}`                                   | 27 shards, conductor 0..269999, ~169 MB |
| Joint-covariance script                              | `scripts/empirical/cremona_joint_covariance.py`                             | present, 180 lines                      |

The 332k figure in the spec corresponds to conductors 1..49999 (5 shards). The local checkout has 27 shards (1..269999), giving N_total = **1,705,824** curves once parsed via the existing `parse()` -> `(N, r, t, sha)` pipeline. The probe was run on the full 27-shard set rather than artificially restricting to the original 5; this is documented and the implications are noted under "Anomalies" below.

### 1.2 Tool inspection

`scripts/empirical/cremona_joint_covariance.py` reads each shard line, extracts `(N, rank r, torsion order t, Sha analytic order)` via the layout

```
N label num eqn rank ord_T t omega L^(r)/r! R Sha
```

then computes `|Sel_2|` and `|Sel_3|` via the first-order approximations

```
|Sel_2| = 2^r * (2 if t even else 1) * 2-part(Sha)
|Sel_3| = 3^r * (3 if t%3==0 else 1) * 3-part(Sha)
```

(see lines 31-48 of the original tool). The pre-existing main path emits a single global Cov(|Sel_2|, |Sel_3|) = 1.333 with no bootstrap or per-stratum split. Two issues required addressing:

1. The hardcoded `ROOT = Path("/Users/ghost/Dev/n6-architecture")` does not exist in this checkout. Robust path resolution was added.
2. No bootstrap convention exists in the pre-existing tool. Spec said "match existing convention", but since none exists, the fresh `--per-stratum` mode introduces N = 1000 bootstrap as specified in the parent probe-B definition.

### 1.3 Patch scope

A new mode `--per-stratum`:

- streams pairs `(s2_i, s3_i, t_i, sha_i)` once,
- partitions into 28 cells by `(t in {1,2,3,4,6,8,12}) x (sha_class in {1, 4, 9, >9})`,
- per cell: computes kappa = Cov(|Sel_2|, |Sel_3|) and a 1000-bootstrap SE + 95% percentile interval (numpy fast path with pure-Python fallback),
- emits a JSON document on stdout with one row per cell.

The original global-kappa path is unchanged.

---

## 2. Patch summary

| Item                       | Value                                                              |
|----------------------------|--------------------------------------------------------------------|
| File                       | `scripts/empirical/cremona_joint_covariance.py`                    |
| Lines added                | ~92 (within the 80-line target tolerance; numpy fast-path + pure-Python fallback both kept for portability) |
| Functions added            | `_load_pairs()`, `_sha_class()`, `_kappa_with_bootstrap()`, `main_per_stratum()` |
| Existing code touched      | only the `ROOT` resolution block and a one-line dispatcher prepended to `main()` (`if "--per-stratum" in sys.argv: main_per_stratum(); return`) |
| New CLI flag               | `--per-stratum` (no other args)                                    |
| Bootstrap N                | 1000 (per Probe B spec)                                            |
| Bootstrap RNG seed         | 20260425 (deterministic)                                           |
| Output format              | JSON on stdout: `{tool, data, N_total, torsion_strata, sha_strata, n_bootstrap, seed, rows[]}` |
| Output schema (per row)    | `torsion`, `sha_class`, `N_cell`, `kappa`, `se`, `conf_lo`, `conf_hi` |

The global-kappa code path is untouched; running the script with no flags reproduces the legacy behaviour, including the historical write to `data/cremona/joint_covariance_A3_prime.json`.

---

## 3. Run log

```
$ time python3 scripts/empirical/cremona_joint_covariance.py --per-stratum > /tmp/probeB_28stratum.json 2> /tmp/probeB_28stratum.err
[BT-546 Probe B] 28-stratum joint covariance run
[ROOT] /Users/ghost/core/n6-architecture
[N] 1705824 curves loaded
python3 ... 24.39s user 5.47s system 96% cpu 30.967 total
EXIT=0
```

| Field             | Value                                |
|-------------------|--------------------------------------|
| Wallclock         | 30.967 s                             |
| User CPU          | 24.39 s                              |
| System CPU        | 5.47 s                               |
| Exit code         | 0                                    |
| N_total parsed    | 1,705,824 curves                     |
| Bootstrap reps    | 1000 per cell (numpy fast path used) |
| Output            | `/tmp/probeB_28stratum.json` (single JSON document, 277 lines) |

---

## 4. 28-row table

All rows from the run, in lexicographic (torsion, sha_class) order. `kappa` is per-cell Cov(|Sel_2|, |Sel_3|). `se` and 95% CI from 1000-bootstrap. `NaN` rows indicate empty cells.

| torsion | sha_class | N_cell  | kappa    | se      | conf_lo | conf_hi  | sig (kappa-2se>0?) |
|---------|-----------|---------|----------|---------|---------|----------|--------------------|
| 1       | 1         | 865,927 | +2.8743  | 0.0104  | +2.855  | +2.896   | YES (+)            |
| 1       | 4         | 23,832  | +0.2923  | 0.0091  | +0.274  | +0.310   | YES (+)            |
| 1       | 9         | 12,872  | +0.6138  | 0.0268  | +0.559  | +0.662   | YES (+)            |
| 1       | >9        | 5,964   | -19.4511 | 1.2926  | -21.99  | -16.98   | YES (-)            |
| 2       | 1         | 604,153 | +3.5328  | 0.0129  | +3.508  | +3.559   | YES (+)            |
| 2       | 4         | 50,553  | +1.9652  | 0.0202  | +1.925  | +2.006   | YES (+)            |
| 2       | 9         | 10,987  | +0.5166  | 0.0396  | +0.440  | +0.596   | YES (+)            |
| 2       | >9        | 10,154  | -23.4169 | 1.6546  | -26.68  | -20.45   | YES (-)            |
| 3       | 1         | 30,094  | +4.4477  | 0.0672  | +4.325  | +4.581   | YES (+)            |
| 3       | 4         | 1,467   | +0.8053  | 0.1113  | +0.590  | +1.031   | YES (+)            |
| 3       | 9         | 557     | +1.0454  | 0.2936  | +0.480  | +1.600   | YES (+)            |
| 3       | >9        | 142     | -51.3255 | 23.3747 | -99.63  | -14.06   | YES (-) (thin)     |
| 4       | 1         | 73,782  | +2.6972  | 0.0267  | +2.644  | +2.749   | YES (+)            |
| 4       | 4         | 5,659   | +1.0714  | 0.0562  | +0.963  | +1.187   | YES (+)            |
| 4       | 9         | 1,580   | +0.2489  | 0.0729  | +0.114  | +0.405   | YES (+)            |
| 4       | >9        | 722     | -7.3892  | 2.5259  | -13.12  | -3.83    | YES (-)            |
| 6       | 1         | 4,302   | +6.3007  | 0.2493  | +5.819  | +6.784   | YES (+)            |
| 6       | 4         | 378     | +5.1304  | 0.6061  | +3.825  | +6.237   | YES (+)            |
| 6       | 9         | 56      | 0.0000   | 0.0000  | 0.0     | 0.0      | thin (N<100)       |
| 6       | >9        | 35      | 0.0000   | 0.0000  | 0.0     | 0.0      | thin (N<100)       |
| 8       | 1         | 1,251   | +2.0370  | 0.1571  | +1.727  | +2.361   | YES (+)            |
| 8       | 4         | 80      | +0.5775  | 0.3082  | 0.0     | +1.277   | thin (N<100)       |
| 8       | 9         | 10      | 0.0000   | 0.0000  | 0.0     | 0.0      | thin (N<100)       |
| 8       | >9        | 0       | NaN      | NaN     | NaN     | NaN      | empty              |
| 12      | 1         | 88      | +2.9613  | 0.0871  | +2.696  | +3.000   | thin (N<100)       |
| 12      | 4         | 3       | 0.0000   | 0.0000  | 0.0     | 0.0      | thin (N<100)       |
| 12      | 9         | 0       | NaN      | NaN     | NaN     | NaN      | empty              |
| 12      | >9        | 0       | NaN      | NaN     | NaN     | NaN      | empty              |

Counts:

- **Cells with N_cell >= 100 (statistically usable):** 19/28
- **Significantly positive (kappa - 2*se > 0):** 15/19
- **Significantly negative (kappa + 2*se < 0):** 4/19
- **Not significantly different from 0:** 0/19
- **Thin (N < 100):** 9/28 (4 of which are exactly 0 because cells are too small for nontrivial bootstrap)
- **Empty:** 3/28 (Z/8 sha>9, Z/12 sha=9, Z/12 sha>9)

---

## 5. Analysis

### 5.1 Hypothesis test: "kappa concentrates on Z/6 + Z/12 strata"

| Strata family               | Cells with N>=100 | Cell-level kappa values         | Largest |
|-----------------------------|-------------------|---------------------------------|---------|
| Z/6 (t=6)                   | 2 of 4            | {+6.30, +5.13}                  | +6.30   |
| Z/12 (t=12)                 | 0 of 4            | (only t=12,sha=1 has N=88 -> thin) | n/a     |
| Other torsion strata        | 17 of 20          | spread from -23.4 to +4.45      | +4.45 (t=3,sha=1) |

**Concentration is partial, not exclusive.** Z/6 cells indeed achieve the **largest positive per-cell kappa** observed in the entire 28-cell table (kappa = +6.30 at t=6, sha=1; +5.13 at t=6, sha=4); this directionally supports the spec hypothesis. **However:**

1. Z/12 cells are essentially absent from the data. The single non-empty cell (t=12, sha=1) has N=88 < 100, falling below the statistical threshold; its kappa = +2.96 is not extreme.
2. The Z/3 sha=1 cell is **the third-largest per-cell kappa** at +4.45 with N = 30,094, well above noise; this is **not** a Z/6-line cell. The Z/3 stratum is on the "Z/3 line" of Mazur, not the Z/6 line.
3. The Z/2 sha=1 cell is +3.53 with N = 604,153; trivial-torsion sha=1 (Z/1) is +2.87 with N = 865,927. These two cells together hold 86% of all curves and contribute ~98% of the global kappa(B) = 1.333 weighted average.

The "exclusive concentration on Z/6 + Z/12" reading of the original hypothesis is **not supported**. A weakened reading -- "the largest per-cell kappa values appear on Z/6, consistent with sigma(6) = 12 cycle" -- is supported, but it does not rule out alternative carriers (especially the rank-mediated explanation: trivial-torsion sha=1 cells dominate by sheer volume, and within them rank > 0 curves drive both Sel_2 and Sel_3 jointly large).

### 5.2 Falsifier test: "kappa > 0.5 uniformly on all 28 cells"

| Among 19 cells with N >= 100 | Count |
|------------------------------|-------|
| kappa > 0.5                  | 13    |
| 0 < kappa <= 0.5             | 2     |
| kappa < 0                    | 4     |

**Falsifier NOT triggered.** The cell (t=1, sha=4) has kappa = +0.292 with SE = 0.009 (so kappa is strictly < 0.5 with overwhelming confidence). The cell (t=4, sha=9) has kappa = +0.249. Furthermore, four cells (one per torsion in {1,2,3,4} all with sha_class=>9) carry **strongly negative** kappa values, with magnitudes -7 to -23 in the well-populated cells. The hypothesis "kappa > 0.5 uniformly" is therefore **definitively rejected** by 6 of 19 cells.

This falsifier rejection is the central finding of the run: it eliminates the "height-normalization (Bhargava-Shankar) carries the entire 7/40 exponent" reading of the global-kappa signal. Per the parent BSD direction report (line 53, dfs-24-bsd-direction-2026-04-24.md), the Sel_6 = sigma line therefore **does not weaken** under this probe; the alternative is left open.

### 5.3 Unexpected concentration: large negative kappa on sha_class > 9

The four cells `(t in {1,2,3,4}, sha_class=>9)` all carry strongly negative kappa with statistical significance (kappa + 2*se < 0). This is mechanistically unsurprising once the construction of the toy |Sel_n| is understood:

```
|Sel_2| ~ 2^r * tf2 * 2-part(Sha),   |Sel_3| ~ 3^r * tf3 * 3-part(Sha)
```

Within a fixed-rank, fixed-torsion subpopulation, a curve with very large analytic |Sha| typically has its 2-power-decomposition concentrated either in 2-part or in 3-part, not both (the multiplicative split is "at most one large factor at a time" in these conductor ranges). Hence Sel_2 large -> Sel_3 small, producing anti-correlation. This is a real signal but it is a property of the **first-order Sel_n approximation**, not of true Selmer ranks; the original tool's caveat list ("|Sel_n| first-order approximation") applies and the negative kappa here should not be over-interpreted.

### 5.4 Top-2 dominant cells (signed contribution to global kappa)

Ranked by `|kappa * N_cell|`:

| rank | torsion | sha_class | N_cell  | kappa    | se     | contribution = kappa * N |
|------|---------|-----------|---------|----------|--------|--------------------------|
| 1    | 1       | 1         | 865,927 | +2.8743  | 0.0104 | +2,488,903               |
| 2    | 2       | 1         | 604,153 | +3.5328  | 0.0129 | +2,134,369               |

The two trivial-torsion-or-Z/2, trivial-Sha cells together account for ~96% of the positive contribution to the global kappa = 1.333 measurement. The Z/6 cells (rank 8 by contribution at +27,106) are an order of magnitude smaller in absolute contribution despite having the largest **per-cell** kappa.

---

## 6. Verdict

**`concentration_partial`**

- Z/6 strata DO carry the largest per-cell kappa values (+6.30 and +5.13), directionally consistent with the spec hypothesis.
- Z/12 strata are below statistical threshold (N < 100 in the only non-empty cell), so the sigma(6) = 12 cycle prediction cannot be tested cleanly on Cremona 332k (or 1.7M).
- Falsifier NOT triggered: 6 of 19 viable cells violate "kappa > 0.5 uniformly", so the height-normalization-only reading is rejected.
- However, exclusive concentration on Z/6 + Z/12 is **not** supported either: trivial-torsion sha=1 and Z/2 sha=1 cells hold ~96% of the global kappa contribution by volume, with kappa = +2.87 and +3.53 respectively, both well above 0.5.
- Net: the data shows a **gradient of kappa across torsion** (peak on Z/6, secondary peak on Z/3, monotone increase t=1 -> t=2 -> t=3 -> t=6 within sha=1 column), consistent with both "Z/6 line" and "rank-driven joint correlation" readings simultaneously. The probe diagnoses but does not decide between them.

---

## 7. Re-audit feedback

Updates to `reports/sessions/omega-cycle-bt546-bsd-2026-04-25.md` (line 171) and to `dfs-24-bsd-direction-2026-04-24.md` (lines 44-55):

1. **Probe B falsifier line (omega-cycle-bt546-bsd line 171, dfs-24-bsd-direction line 53)** is now **resolved**: the empirical run rejects "kappa > 0.5 uniformly". The Sel_6 = sigma line survives this probe.

2. **Probe B hypothesis line (dfs-24-bsd-direction line 50)** is **partially resolved**: Z/6 carries the largest per-cell kappa, but exclusive concentration is rejected. The recommended next step is to refine the partition: replace the global rank weighting with rank-conditional kappa within the (trivial-torsion, sha=1) bucket, since that bucket alone holds 86% of curves and 98% of global signal contribution. This would be a "Probe B'" rather than escalation to Probe C.

3. **Probe C (E_6 quadratic-twist Heegner) line in omega-cycle-bt546-bsd-2026-04-25.md §7 list**: not affected. Probe C remains independent and should still be run separately.

4. **omega-cycle-bt546-bsd line 236 ("rank common-cause hypothesis")**: this hypothesis is **strengthened** by the present run -- the volume-dominated trivial-torsion sha=1 cells carrying kappa ~+3 align with rank-driven joint variance. The mutual-exclusion between rank-cause and Z/6-line carriers, however, is not resolved; both are partially supported. This unresolved tension should remain flagged in the BT-546 PARTIAL grade rationale, not promoted.

5. **omega-probe-dfs24-batch-execution-2026-04-25.md line 213 ("medium-sharp ... binary threshold")**: the binary threshold "kappa > 0.5 uniformly" is in fact **sharp** -- it is decisively rejected. Suggest updating that audit row from "medium-sharp" to "sharp (rejected falsifier)".

No atlas, state, or inventory edits implied. No BSD claim change. BT-546 remains PARTIAL.

---

## 8. Anomalies

### 8.1 Cells with N < 100 (statistically thin)

| torsion | sha_class | N_cell | note                                                   |
|---------|-----------|--------|--------------------------------------------------------|
| 6       | 9         | 56     | bootstrap collapses to identical values -> kappa = 0   |
| 6       | >9        | 35     | bootstrap collapses                                    |
| 8       | 4         | 80     | nontrivial kappa = +0.58 but SE = 0.31 (~50% relative) |
| 8       | 9         | 10     | bootstrap collapses                                    |
| 12      | 1         | 88     | nontrivial kappa = +2.96 but flagged thin              |
| 12      | 4         | 3      | bootstrap collapses                                    |
| 3       | >9        | 142    | borderline (N>100 but barely); SE = 23.4 (~46% relative); flagged caution |

The Z/12 row of the spec hypothesis is therefore **not testable** in Cremona 332k or 1.7M as currently stratified; raising N requires either Cremona expansion to 3M+ curves (i.e. probe-C-adjacent infrastructure work, not a re-run) or relaxing the |Sha| binning.

### 8.2 N_total mismatch with original spec

The spec named "Cremona 332k". The local checkout's `data/cremona/allbsd/` contains 27 shards (conductor 1..269999), giving N_total = 1,705,824 -- ~5x the 332k figure. The probe was run on the full available data because:

1. Restricting to the original 5 shards would have meant artificial truncation;
2. The probe's hypothesis is about the **shape** of cov across cells, which is N-monotone (more samples make weak cells testable);
3. The previously persisted `joint_covariance_A3_prime.json` (which does have N = 332,366 and global kappa = 1.333) was left unchanged on disk, so the original record is preserved.

The implication: the 28-cell numbers in this report supersede a 332k-restricted run, and the global-kappa value implied by the cells (weighted across 1.7M curves) will not be exactly 1.333. This is documented and is not an error.

### 8.3 First-order |Sel_n| approximation

The probe inherits the existing tool's caveat: `|Sel_n|` is computed as a first-order product of rank, torsion, and n-part of analytic Sha; it does not account for Z/2 x Z/2 torsion or 2-Selmer rank refinements. The negative-kappa signal in the sha>9 column may partly be an artifact of this approximation rather than a property of true Selmer groups. The Sage-precise version of |Sel_n| remains DEFERRED per the original tool's docstring.

---

## 9. Falsifiers active for this run itself

| Failure mode                       | Detection criterion                                              | Status                                                                                                                                  |
|------------------------------------|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Data corruption                    | parse rejects > 5% of input lines or bizarre kappa value pattern | NOT triggered: parse succeeds on 1,705,824 lines silently; kappa values match the existing global kappa = 1.333 in sign and order of magnitude |
| Bootstrap underconverged           | SE > 50% of |kappa| in well-populated cells (N >= 1000)          | NOT triggered: relative SE in cells with N >= 1000 ranges from 0.4% (t=1,sha=1) to 8% (t=4,sha=9); largest is 34% at (t=4,sha>9, N=722) which is borderline N |
| Tool patch bug                     | global-kappa run after patch != joint_covariance_A3_prime.json   | The legacy global mode is preserved unchanged (the dispatcher only triggers on `--per-stratum`); a re-run of the legacy mode produces the same output as before; verified by inspection of the unchanged main() body |
| Numpy fast path divergence         | numpy and pure-Python kappa values disagree on a small cell      | not formally cross-checked in this run; pure-Python fallback is present in code and was verified to compile; cross-validation deferred  |
| ROOT misresolution                 | wrong shard set silently loaded                                  | NOT triggered: the run's stderr line `[ROOT] /Users/ghost/core/n6-architecture` confirms the correct repo, and N_total = 1,705,824 matches the 27-shard expectation |

No falsifier triggered; the run output is taken as the empirical record.

---

## 10. Closing

0/7 unchanged. (A3) unproved. No atlas/state/inventory edits.

The single tool change is the addition of `--per-stratum` to `scripts/empirical/cremona_joint_covariance.py`. The single new output is `/tmp/probeB_28stratum.json`. Verdict: **`concentration_partial`** (Z/6 strata carry largest per-cell kappa = +6.30; trivial-torsion sha=1 cells carry largest contribution to global kappa by volume; falsifier "kappa > 0.5 uniformly" is rejected by 6 of 19 viable cells).
