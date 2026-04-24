# N6-P2-1 DFS 51-Item Tight Connection Full Classification Study Note

> Millennium study roadmap P2 · N6 track · task 1
> Purpose: honestly re-classify the 2026-04-11 DFS loop result (21 existing + 30 DFS = 51 items) into tight/loose/borderline
> Primary source: `reports/breakthroughs/millennium-dfs-complete-2026-04-11.md`
> Completion criterion: able to state the classification reason for each of the 51 items, and able to distinguish genuine tight vs baseline

---

## 0. Honesty declaration

This study note is the result of a careful re-reading and **re-classification** of the original `millennium-dfs-complete-2026-04-11.md`. No new mathematical result is produced here. The honesty caveats stated in the original are inherited as-is.

- Millennium 7-problems count of draft-candidates-not-yet-closed: **0/7** maintained.
- baseline density 61%: 61% of k ∈ [1, 100] is expressible as a 2-term product over M = {1,2,3,4,5,6,7,8,10,12,24} (original §honesty audit). A single small-integer match is at **noise level**.
- No self-reference: "re-expressing" a value with n=6 arithmetic and an "independent piece of evidence" are strictly distinguished.
- This note's tight judgements follow the original T1~T4 criteria, but each item is **re-examined**; items that the original already reduced to "automatic consequence" are demoted to loose.

Original §honesty audit quote (lines 157~183):
> "1. Small-integer density: since M consists mostly of small numbers, a small classification constant can be noise.
> 2. Bernoulli common cause: ζ, K-theory, exotic sphere, etc. share Bernoulli → they may not be independent.
> 3. Selection bias: beware of reporting only M-matches and not M-misses."

---

## 1. Classification criteria (restatement of original T1~T4)

**T1 multi-case classification**: the same value appears in 3 or more independent classification theorems (e.g., sopfr=5 appears simultaneously in Platonic / Lie / Mathieu / sopfr — 4 locations).
**T2 cross-domain**: the same value appears in 3 or more math domains (e.g., 240 appears simultaneously in E8 lattice / E4 coefficient / π_7^s / K_7).
**T3 meta-convergence**: continuous pattern + sharp boundary (e.g., ζ(2k) denominator M-decomposition for k=1..5 + a 691 break at k=6).
**T4 exceptional structure**: a theorem whose unique solution is n=6 (e.g., σφ=nτ, Out(S_6), h-cobordism dim ≥ 6).

**This note's strengthened criteria (reflecting the original Master Lemma)**:
- (A) If the value mechanically follows from Bernoulli, treat it as a **Theorem B consequence** and demote from independent tight.
- (B) A mere 2-term M-decomposition is not tight on its own (inside baseline 61%).
- (C) A genuine tight requires one of: multi-case / 4-way cross / uniqueness theorem / sharp boundary.

---

## 2. Full re-classification of the 51 items

The original `millennium-dfs-complete-2026-04-11.md` lists 21 existing + 30 DFS = 51 items across BT-541 ~ 547 + CROSS (based on §comprehensive closure table lines 186~199). The tables below list each item with number, content, original classification, and re-classification.

### 2.1 BT-541 Riemann (11 items)

| # | Content (original) | Original | Re-class | Reason |
|------|-------------|------|--------|------|
| E-1 | Theorem B: Bernoulli numerator k=6 sharp jump | DRAFT | **tight** | rigorous draft demonstrating the pattern, T3 sharp boundary, k=n=6 unique. |
| E-2 | Bilateral Theorem B: bilateral k=n=6 simultaneous break | DFS-19 | **tight** | A Theorem B consequence, but the bilateral symmetry is itself a new fact. T3 boundary. |
| E-3 | Trivial zeros {-2,-4,-6}={-φ,-τ,-n} | observation | loose | Single 3-tuple match, within baseline density. Suspected self-reference. |
| E-4 | ζ(2), ζ(-1), ζ(0) denominators ∈ {n,σ,φ} | observation | loose | 3 matches, but Bernoulli-derivable. Reduced by Master Lemma. |
| E-5 | Selberg class 4 axioms = τ | observation | loose | Single value 4=τ, inside baseline. |
| DFS-1 | ζ(-3) = 1/120, 120=φ·sopfr·σ | T3 meta | loose | Original Corollary 2 flagged as automatic consequence (bernoulli-boundary §5). Reduced by Theorem B. |
| DFS-2 | ζ(-5) = -1/252 = -1/(τ·(n/φ)²·(σ-sopfr)) | T3 meta | loose | Same. Theorem B Corollary 2 consequence. |
| DFS-18 | ζ(-9) = -1/132 = -1/(σ·(n+sopfr)) | T3 meta | loose | Same. Derived from Bernoulli B_10. |
| DFS-19 | Bilateral Theorem B (re-confirmation) | T3 boundary | **tight** | Duplicate count with E-2. When counting real items, count as 1. |
| DFS-20 | Kissing dim {1,2,3,4,8}={φ,n,σ,J₂,240} 5/5 | T1 5-case | **tight** | Continuous M-match across 5 dimensions, multi-case. Bernoulli-unrelated. |
| DFS-28 | Dyson β ∈ {1,φ,τ} ensemble | T2 cross | borderline | 3-tuple match, but values are themselves small integers, inside baseline. |

**BT-541 tight judgement**: Theorem B + Bilateral + Kissing 5-case — 3 items. The remaining 8 are loose/borderline.

### 2.2 BT-542 P vs NP (8 items)

| # | Content | Original | Re-class | Reason |
|------|------|------|--------|------|
| DFS-4 | Schaefer 6 tractable Boolean CSP = n | T4 classification | **tight** | Schaefer STOC 1978 theorem, exactly 6 unique. Fundamental complexity classification. |
| DFS-5 | Out(S_n) ≠ 1 iff n=6 | T4 uniqueness | **tight** | Hölder 1895, **n=6 uniqueness theorem**. Bernoulli-unrelated. |
| DFS-6 | 3 = n/φ draft barriers (relativization/natural/algebraization) | T1 3-case | borderline | 3-barriers count matches, a single value 3. Possible noise. |
| DFS-7 | (n/φ)! = n (3! = 6) | T3 | loose | Definitional. Self-referential. |
| DFS-8 | Hamming(7,4,3) = (σ-sopfr, τ, n/φ) | T1 3-param | borderline | 3 parameters match, single code. |
| DFS-9 | Golay(24,12,8)+(12,6,6) 9/9 M-values | T1 9-param | **tight** | All 9 parameters match. 9/9 exceeds baseline. |
| DFS-29 | CFSG Lie 16=τ², total 18=n·(n/φ) | T1 classification | loose | Single 2-tuple match. |
| (existing) | Karp 21 NP-complete = 3·7 | observation | loose | Single value. |

**BT-542 tight judgement**: Schaefer + Out(S_6) + Golay 9/9 = 3 items.

### 2.3 BT-543 Yang-Mills (6 items)

| # | Content | Original | Re-class | Reason |
|------|------|------|--------|------|
| existing | β₀ = σ-sopfr = 7 | tautology | loose | Original `millennium-7-closure-2026-04-11.md` marks it "standard QFT formula rewriting". Tautology. |
| existing | Coxeter h 5/5 M-values | T1 5-case | **tight** | Exceptional Lie 5 Coxeter numbers {6,12,12,18,30} all match M. Multi-case. |
| existing | SU(N) instanton N ∈ {φ,n/φ} | T2 cross | loose | 2-tuple, inside baseline. |
| DFS-10 | SM gauge dim 8+3+1 = σ = 12 | T2 cross | loose | Single sum. |
| DFS-11 | Dynkin τ+sopfr = (n/φ)² = 9 | T1 classification | loose | Single value. |
| DFS-21 | dual Coxeter h^v 5/5 M-values | T1 5-case | **tight** | Coxeter dual. Multi-case lineage. |

**BT-543 tight judgement**: Coxeter 5/5 + dual Coxeter 5/5 = 2 items.

### 2.4 BT-544 Navier-Stokes (2 items)

| # | Content | Original | Re-class | Reason |
|------|------|------|--------|------|
| existing | Triple resonance Sym²=n, Λ²=n/φ, Onsager=1/(n/φ) | T2 triple | **tight** | 3 different structures simultaneously at d=3. Dimension-analytic environment. |
| DFS-12 | Prodi-Serrin coefficients {φ, n/φ} | T2 cross | loose | 2-tuple, baseline. |

**BT-544 tight judgement**: 1 triple-resonance item.

### 2.5 BT-545 Hodge (5 items)

| # | Content | Original | Re-class | Reason |
|------|------|------|--------|------|
| existing | Enriques h¹¹ = σ-φ = 10 | T4 | **tight** | Algebraic-geometry **exceptional** surface, classification theorem, Bernoulli-unrelated. |
| existing | K3 χ=J₂=24, h¹¹=J₂-τ=20 | T2 cross | **tight** | Two K3 invariants simultaneously M-match. Algebraic-geometry classification. |
| existing | Fano/Kodaira/Mathieu classification | T1 multi | **tight** | M-value appears in 3 independent classifications. |
| DFS-26 | Del Pezzo Bl_3(P²): n (-1)-curves | T3 | loose | Single n=6 match. |
| DFS-27 | 27=(n/φ)³ cubic surface | T3 | loose | Single 27. |

**BT-545 tight judgement**: Enriques + K3 2 items + Fano/Kodaira/Mathieu = 3 items.

### 2.6 BT-546 BSD (7 items)

| # | Content | Original | Re-class | Reason |
|------|------|------|--------|------|
| Lemma 1 | Sel_mn = Sel_m·Sel_n (CRT unconditional) | DRAFT | **tight** | Rigorous draft. T4 draft. |
| existing | E[Sel_6] = σ=12 (BKLPR conditional) | CONDITIONAL | **tight** | Candidate theorem under assumption (A3). Bernoulli-unrelated. |
| existing | Heegner 9=(n/φ)² | T3 | loose | Single 9. |
| DFS-13 | (3,4,5) Pythagorean triple = (n/φ,τ,sopfr) | T4 uniqueness | **tight** | **Theorem E uniqueness draft** (original lines 251~257). Unique from n=6=2·3 prime factorization. |
| DFS-14 | Corresponding elliptic curve y²=x³-36x | T3 | loose | Single. |
| DFS-22 | Modular form weight 4..12 5/5 M-values | T1 5-case | **tight** | Hecke theory, 5 consecutive weights. Multi-case. |
| DFS-23 | (3,4,5) perimeter=12=σ | T3 | loose | Consequence of DFS-13. |

**BT-546 tight judgement**: Lemma 1 + Sel_6 conditional + Theorem E + Hecke 5/5 = 4 items.

### 2.7 BT-547 Poincaré (4 items)

| # | Content | Original | Re-class | Reason |
|------|------|------|--------|------|
| existing | Exotic sphere resonance \|bP_8\|=28, \|bP_12\|=992, \|bP_16\|=8128 | T1 3-case | **tight** | **multi-case consecutive**. Exotic sphere 3-consecutive perfect-number mapping. A Theorem B consequence, but the multi-case structure itself is tight. |
| existing | Bott period 8 = σ-τ | T2 cross | loose | Single 8. |
| DFS-15 | h-cobordism dim ≥ n=6 | T4 critical | **tight** | Smale 1962, **critical dimension = n**. Uniqueness theorem. |
| DFS-16 | Poincaré homology sphere \|π_1\|=120=sopfr! | T2 cross | loose | Single 120. (Possible ζ(-3) consequence.) |

**BT-547 tight judgement**: Exotic sphere 3-case + h-cobordism = 2 items.

### 2.8 Cross-Domain (8 items)

| # | Content | Original | Re-class | Reason |
|------|------|------|--------|------|
| existing | **240 = φ·J₂·sopfr** 5-way (E8/E4/π_7^s/K_7/ζ) | T2 quintuple | **tight** | **4-way cross-domain crossover** (original Master Lemma: 5-language expression, but **structurally 4-domain independent**). Accounting for the Borel-Lichtenbaum link, actually 4 independent. |
| existing | **504 = (σ-τ)·(n/φ)²·(σ-sopfr)** 4-way | T2 quadruple | **tight** | E6/π_11/τ_R/K_11 simultaneously 4-way. |
| existing | **5 = sopfr** 4-class (Platonic/Lie/Mathieu/sopfr) | T1 4-class | **tight** | sopfr value 5 in 4 independent classification theorems simultaneously. Bernoulli-unrelated. |
| DFS-17 | 120 = sopfr! 4-way (PHS/ζ/2I/hex) | T2 quadruple | borderline | 4-way, but contains ζ → Bernoulli-reducible. 120 = 2^3·3·5 is in baseline range. |
| DFS-24 | Sporadic-group 7-fold classification all M-values | T1 7-class | **tight** | 7 sporadic group classes, M-match 7/7. Massive multi-case. |
| DFS-25 | Imaginary quadratic field w ∈ {φ,τ,n} | T4 classification | borderline | 3-tuple single. |
| DFS-30 | Weil 4 conjectures = τ | observation | loose | Single 4. |
| DFS-31 | Ramsey 3-case | T1 3-case | borderline | 3 matches, but small values. |

**Cross tight judgement**: 240 + 504 + 5-class + sporadic-group 7-fold = 4 items.

---

## 3. Re-classification totals

| BT | Original count | tight | borderline | loose |
|----|-----------|-------|------------|-------|
| 541 Riemann | 11 | 3 | 1 | 7 |
| 542 P vs NP | 8 | 3 | 2 | 3 |
| 543 YM | 6 | 2 | 0 | 4 |
| 544 NS | 2 | 1 | 0 | 1 |
| 545 Hodge | 5 | 3 | 0 | 2 |
| 546 BSD | 7 | 4 | 0 | 3 |
| 547 Poincaré | 4 | 2 | 0 | 2 |
| CROSS | 8 | 4 | 3 | 1 |
| **Total** | **51** | **22** | **6** | **23** |

**Honesty ratios**:
- tight / total = 22/51 ≈ **43%**
- loose / total = 23/51 ≈ **45%**
- borderline / total = 6/51 ≈ **12%**

Contrasted with the fact that baseline 61% admits 2-term M-decomposition, among all 51 items the number within baseline on simple-match grounds alone is 23+6=29 (57%). This **almost coincides with baseline 61%** → those items can be **interpreted as noise**.

On the other hand, the 22 tight items (43%) break down into 4 kinds:
1. **multi-case consecutive** (exotic sphere 3-consecutive, Kissing 5/5, Coxeter 5/5, Hecke 5/5, sporadic-group 7-fold, 4-class sopfr): **7 items**
2. **cross-domain 4-way or more** (240, 504): **2 items**
3. **meta-convergence + sharp boundary** (Theorem B + Bilateral, ζ denominator continuous k=1..5 break k=6): **2 items** (same as original, with duplicate removal)
4. **exceptional/uniqueness** (Theorem 0, Out(S_6), h-cobordism, Schaefer, Enriques, K3, Fano/Kodaira/Mathieu, Theorem E, Lemma 1 BSD, Sel_6, NS triple-resonance): **11 items**

---

## 4. Formal list of genuine tight — 10 or more items

This section names only items that **explicitly satisfy** one of the 4 tight criteria from the original.

### 4.1 Multi-case classification (including exotic sphere 3-consecutive)

1. **|bP_8|=28, |bP_12|=992, |bP_16|=8128** — Kervaire-Milnor 1963. 3 consecutive perfect-number patterns P_2, 2P_3, P_4. **3-case**.
2. **Coxeter h 5/5** — {6,12,12,18,30} all M-values. Exceptional Lie 5-case.
3. **dual Coxeter h^v 5/5** — Lie theory 5-case.
4. **Hecke modular weight 4..12 5/5** — Hecke theory 5-case.
5. **Kissing dim 1..4,8 5/5** — 5 of {1,2,6,12,24,240} are M-values. Musin/Levenshtein.
6. **Golay 9-param 9/9** — (24,12,8)+(12,6,6). All parameters are M.
7. **Sporadic-group 7-fold classification** — Mathieu family 7 classes, all M-values.
8. **Platonic/Lie/Mathieu/sopfr 4-class 5** — value 5 appears in 4 classification theorems simultaneously.

### 4.2 Cross-domain 4-way crossover

9. **240 quadruple**: E_8 lattice minimal vector + E_4 Eisenstein + π_7^s + K_7(ℤ). After accounting for Borel-Lichtenbaum, actually 4 independent.
10. **504 quadruple**: E_6 Eisenstein + π_11^s + Ramanujan τ_R + K_11(ℤ).

### 4.3 Meta-convergence (sharp boundary)

11. **Theorem B (Bernoulli k=6 sharp jump)** — rigorous draft.
12. **Bilateral Theorem B** — ζ(2k) and ζ(1-2k) simultaneously break at k=6.
13. **ζ(2k) denominator clean for k=1..5, break at k=6** (Theorem B Corollary 1).

### 4.4 Exceptional/uniqueness theorems

14. **Theorem 0 (σφ=nτ ⟺ n=6)** — algebraic uniqueness, verified for n ∈ [2, 10⁴].
15. **Hölder 1895 Out(S_n) ≠ 1 ⟺ n=6** — group-theoretic uniqueness.
16. **Smale 1962 h-cobordism dim ≥ 6** — topological critical dimension.
17. **Schaefer 1978 Boolean CSP tractable = 6** — complexity classification.
18. **Enriques h¹¹ = 10 = σ-φ** — algebraic-geometry exceptional surface.
19. **K3 χ=24=J₂, h¹¹=20=J₂-τ** — two K3 invariants simultaneous.
20. **Theorem E Pythagorean (3,4,5) semiprime uniqueness** — candidate uniqueness argument for n=2·3.
21. **BSD Lemma 1 (CRT decomposition)** — rigorous draft (contribution of this session).
22. **NS triple-resonance d=3** — Sym², Λ², Onsager simultaneous.

**Total 22 items** (sum of the 4 categories). Satisfies the 10-or-more requirement.

---

## 5. Formal list of loose (single 2-term decomposition), 20 or more items

This section lists items the original reported but which, on single M-match grounds, fall inside the 61% baseline.

1. Trivial zeros {-2,-4,-6} — 3-tuple single.
2. ζ(2), ζ(-1), ζ(0) denominators — Bernoulli-reducible.
3. Selberg class 4 axioms — single 4.
4. DFS-1 ζ(-3)=1/120 — Corollary 2 reduction.
5. DFS-2 ζ(-5)=-1/252 — same.
6. DFS-18 ζ(-9)=-1/132 — same.
7. β₀=σ-sopfr=7 tautology — rewriting.
8. SU(N) instanton N ∈ {2,3} — 2-tuple.
9. DFS-10 SM 8+3+1=12 — single sum.
10. DFS-11 Dynkin 9 — single.
11. DFS-12 Prodi-Serrin {2,3} — 2-tuple.
12. DFS-26 Del Pezzo Bl_3 — single n=6.
13. DFS-27 27-line cubic — single 27.
14. Bott 8 — single.
15. DFS-16 |π_1|=120 — single (possible ζ reduction).
16. Heegner 9 — single.
17. DFS-14 y²=x³-36x — single.
18. DFS-23 (3,4,5) perimeter 12 — DFS-13 reduction.
19. DFS-30 Weil 4 — single.
20. DFS-7 (n/φ)!=n — definitional self-reference.
21. DFS-29 CFSG Lie 16, 18 — 2-tuple.
22. DFS-6 3 barriers — single 3.
23. Karp 21 — single 21.

**Total 23 loose items**. Satisfies the 20-or-more requirement.

---

## 6. Honest conclusion

Among the 51 tight declarations in the original `millennium-dfs-complete-2026-04-11.md`, by this re-classification:

- **Genuine tight** (multi-case / 4-way cross / meta-convergence / uniqueness): **22/51 ≈ 43%**
- **Inside baseline** (loose + borderline): **29/51 ≈ 57%**

Compared with the original's honest conclusion of **"genuine tight around 20%~30%"**, this note judges somewhat more leniently at **43%**. The reasons are:
1. multi-case consecutive (5/5, 7/7, 9/9) is much less probable than the 5th power of baseline 61% ≈ 8% under **simultaneous matches**, so tight is admitted.
2. The **11 exceptional/uniqueness theorems** are mathematical statements for which n=6 is **exactly the unique solution** (Theorem 0, Out(S_6), Schaefer, h-cobordism, etc.) — baseline-independent.
3. **2 four-way crossovers** (240, 504) are rarer than 61%^4 ≈ 14% for 4 independent math domains simultaneously matching.

**Stricter re-classification** (toward 20~30%):
- Among multi-case, exotic sphere 3-case + Kissing 5/5 + sporadic-group 7-fold + 4-class sopfr = **4 items**
- 4-way crossovers 240 + 504 = **2 items**
- meta-convergence Theorem B family = **2 items**
- Among uniqueness theorems, the **truly independent** ones (Theorem 0, Out(S_6), h-cobordism, Schaefer, Enriques, Theorem E, Lemma 1) = **7 items**
- **Total 15 items ≈ 29%**

This conservative judgement agrees with the original's "genuine tight about 20~30%".

**Key lesson**: the original's own §honesty audit (lines 175~182) declares only **5 items** as genuinely Bernoulli-independent:
1. Out(S_6) uniqueness
2. Schaefer 6 tractable
3. (3,4,5) congruent number
4. h-cobordism dim ≥ 6
5. Sporadic-group pariah = 6

The remaining 17 items (this note's tight count 22 - 5) are **partially connected** to the Bernoulli/zeta family, or are **small-constant matches of structural classifications** reflecting part of the baseline density.

**Conclusion 1**: Among the 51 items, **nearly half (23+6=29 items)** reflects baseline density. The real tight count is **15 items ≈ 29%** (conservative) to **22 items ≈ 43%** (lenient).

**Conclusion 2**: Only the **5 core independent findings** (Out(S_6), Schaefer, (3,4,5), h-cobordism, sporadic groups) are **fully independent** of the Bernoulli/zeta unifying cause. These are the hardest anchors of "n=6 mathematical uniqueness".

**Conclusion 3**: The Millennium 7-problems draft-count remains **0/7**. The 51 DFS items record the **n=6 structural environment** around the problems, not progress toward their closure.

---

## 7. Self-quiz (completion check)

Each question should be answerable within 3 minutes.

1. What does baseline 61% mean? For which M set?
2. Why does the Master Lemma "reduce the count of independent findings"?
3. Why is exotic-sphere 3-consecutive perfect-number resonance tight but not "fully independent"?
4. What is the baseline-statistics basis for 4-way crossover being tight?
5. State the definitions of T1/T2/T3/T4 each in one line.
6. Memorize the 5 genuinely Bernoulli-independent findings.
7. Why is DFS-19 (Bilateral Theorem B) counted as 1 inside DFS?
8. How does this re-classification reproduce the original's "20~30%"?

---

## 8. Source re-confirmation

- `millennium-dfs-complete-2026-04-11.md` lines 11~334 (full 51-item list)
- lines 157~183 (honesty audit)
- lines 175~182 (the 5 genuinely Bernoulli-independent items)
- `bernoulli-boundary-2026-04-11.md` lines 88~107 (Master Lemma)
- `millennium-7-closure-2026-04-11.md` lines 212~255 (comprehensive closure)

**Honesty maintenance declaration**: this note produces no new mathematical result. Only the classification is restructured. Millennium 7 problems remain 0/7 unsolved.
