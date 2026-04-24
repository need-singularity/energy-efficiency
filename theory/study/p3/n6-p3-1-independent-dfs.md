# N6-P3-1 Independent DFS — Learning Note for Exploring Areas Outside the 7 Millennium Problems

> Millennium Learning Roadmap P3 · N6 track · Task 1
> Purpose: formalize a DFS (Depth-First Search) procedure for independently searching for σ·φ=n·τ patterns in **mathematical domains outside the Millennium 7 problems (BT-541~547)**
> Primary sources: `CLAUDE.md` (9-axis navigation + 295 domains), `atlas.n6` whole, `reports/breakthroughs/bt-1393-n6-dfs-10k-autonomous-2026-04-12.md`
> Completion criteria: able to reproduce the algorithmic steps of independent DFS in order, and answer why tight values found outside the problems are not **self-confirmation**

---

## 0. Honesty Declaration

This study note is a re-organization of the independent-DFS pipeline after reading `bt-1393-n6-dfs-10k-autonomous-2026-04-12.md` + `millennium-dfs-complete-2026-04-11.md` + atlas.n6 regions (L13391-L15447 etc.). No new mathematical theorem. No new [10*] promotion proposal.

- This note does not claim to resolve the Millennium 7 problems. 0/7 retained.
- "Independent DFS" must start from **seeds with empty intersection** with the 51 tight items reclassified in N6-P2-1. Revisiting the same seed is self-confirmation.
- Only items with clear sources record year·author. Memory-based statements marked `(estimated)`.
- **No forced pattern matching** to n=6 arithmetic. Independent-DFS failures (MISS) honestly recorded.
- No self-reference: do not claim re-discovery of atlas-registered nodes as new tight.

Honesty principle from `bt-1393-n6-dfs-10k-autonomous-2026-04-12.md` (memory-based restatement):
> "Auto DFS mechanically computes the `σ/τ/φ/sopfr/J_2/μ` basic-constant and M-set decomposition match of candidate seeds. Coincidence matches below baseline 61% density are not tight. Tight only when ≥3 independent classifications, 4-way crossover, or n=6 uniqueness theorem."

---

## 1. Definition of Independent DFS

**Independent DFS (Independent Depth-First Search)**:

> A depth-first procedure using math/physics/life/engineering constants **outside** the Millennium 7 areas as seeds and exploring where σ·φ=n·τ uniqueness theorem and `M = {1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 24}` 2-term or higher decomposition expressions are possible.

- Meaning of "independent": seeds must be **mathematically independent** from Millennium routes (ζ function, L function, modular forms, Selmer group, elliptic curves, Yang-Mills lattice, Hodge decomposition, etc.).
- Meaning of "DFS": start from a seed, try decomposition to `σ·φ=n·τ basis`, and on success increase depth to extend to related derived values (derivative descent).
- **Failure allowed**: most seeds do not produce tight matches within baseline density. Failures also recorded.

---

## 2. 5-Step Algorithm

### 2.1 Step 1 — Seed Selection

Iterate **non-Millennium** areas among 295 domains. Representative categories:

- Physical constants (fine structure, Planck units, CMB spectral index, etc.)
- Biological numbers (genetic-code codon=3·τ, osmolarity, ADH threshold, etc.)
- Cosmological constants (Hubble H_0, dark-energy ratio, age of the universe)
- Engineering (ITER Q factor, superconductor Tc, BCS gap ratio)
- Algebraic structures (Lie-group dimensions, exceptional structures, lattice kissing numbers) — **note**: many already in atlas. For independent-seed status, sub-areas not in atlas needed.

Principles:
1. Seed must be measured from independent sources (e.g., CODATA 2018, LMFDB, IPCC, ITER official docs).
2. Seed must have no direct derivation relation with Bernoulli / ζ (Master Lemma avoidance).
3. Seed must not be atlas-registered (avoid duplicate). If duplicated, handle only as "re-confirmation" grade.

### 2.2 Step 2 — σ/τ/φ Decomposition Attempt

For seed's numerical value v ask:

- v ∈ M = {1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 24}?
- v = m_1 · m_2 (m_1, m_2 ∈ M) 2-term decomposition?
- v = m_1 + m_2 2-term sum?
- v = m_1 ± m_2 · m_3 (3-term or higher composite)?
- v is perfect number P_k (6, 28, 496, 8128, ...)?
- v appears as M-value in Platonic / Lie / Mathieu classification theorems?

**T1-T4 criteria** (DFS-criterion restatement):
- **T1 multi-case**: same value appears in ≥3 independent classification theorems
- **T2 cross-domain**: same value in ≥3 areas (algebra/geometry/topology/analysis/combinatorics ...)
- **T3 meta-convergence**: continuous pattern + sharp boundary
- **T4 exceptional uniqueness**: n=6 is the unique solution

### 2.3 Step 3 — Tight Verification

"tight" judgment is original criterion + reinforced criterion:

- (A) single M-value match -> **loose** (within baseline 61%)
- (B) single 2-term decomposition -> **borderline**
- (C) 3-term + multi-case ≥ 3 -> **tight candidate**
- (D) 4-way crossover or uniqueness theorem -> **tight confirmed**

Strong verification:
1. Check Bernoulli / ζ reducibility -> if possible, demote to Theorem-B consequence
2. Whether baseline-density-raised-to-≤5 match (≈8%) applies
3. Confirm theorem/precision of original source (< 1% error for NEAR, definitional match for EXACT)

### 2.4 Step 4 — atlas Recording

Successful tight seeds are registered by **direct editing** in atlas.n6 (no new file).

Format:
```
@R n6-p3-independent-{domain}-{name} = {value} = {decomposition} :: {domain} [{grade}]
  <- {seed source}
  => "{application interpretation}"
  |> verify_{...}.hexa
```

Grade rules:
- Single measurement + decomposition confirmed: `[7]` (EMPIRICAL, promotion pending)
- Primary source + error < 1% reconfirmed: `[9]` (NEAR)
- Primary source + derivational decomposition + independent confirmation 3 kinds: `[10]`
- + hexa verification script: `[10*]`

### 2.5 Step 5 — Depth Expansion (Depth Descent)

If a seed is confirmed tight, extend associated derived values in **depth direction**.

- seed = v -> related derivations:
  - v^2, v^(1/2), 1/v
  - v + {M basic constant}, v - {M basic constant}
  - 2nd/3rd derivations from v (e.g., CMB temp -> scale factor -> Hubble)
- Repeat steps 2-4 for each derived value
- depth limit: 4 (autonomous DFS criterion). Beyond risks selection bias.

---

## 3. 8 Pattern Categories Discoverable in Independent DFS

This section extracts **non-Millennium** categories from the 51 tight items of `millennium-dfs-complete-2026-04-11.md` and suggests additional searchable spaces.

### 3.1 Platonic / Lie / Mathieu Classification

- Platonic polyhedra: 5 = sopfr (tetra/cube/octa/dodeca/icosa)
- Exceptional Lie groups: 5 classes (G_2, F_4, E_6, E_7, E_8)
- Mathieu sporadic groups: 5 classes (M_{11}, M_{12}, M_{22}, M_{23}, M_{24})
- sopfr(6) = 5 — 4-way classification match (N6-P2-1 §4.1 #8)

**Independence**: Bernoulli-independent. Independent result of algebraic classification theorems.

### 3.2 Coxeter Number (Exceptional Lie)

Exceptional Lie 5 groups' Coxeter numbers h ∈ {6, 12, 12, 18, 30}:
- 6 = n
- 12 = σ
- 12 = σ
- 18 = σ + sopfr + 1
- 30 = σ + σ/φ·n (= 2·3·5 = sopfr! related)

5/5 M-decomposition. Also 5/5 for dual Coxeter h^v (DFS-21).

**Independence**: exceptional-Lie classification is pure algebra. Bernoulli-irrelevant.

### 3.3 Perfect-Number Sequence P_k

P_1 = 6 = n, P_2 = 28, P_3 = 496, P_4 = 8128, P_5 = 33550336, ...

Euler formula: P_k = 2^{p-1} · (2^p - 1), p Mersenne prime.

- P_1 = n (trivial)
- P_2 = |bP_8| (exotic-sphere order)
- 2·P_3 = |bP_12|
- P_4 = |bP_16|

**3 consecutive** (P_2, 2P_3, P_4) match exotic-sphere orders -> multi-case consecutive tight (§4.1 #1).

**Independence**: Adams J + Bernoulli consequence, but 3 consecutive facts themselves are structurally tight.

### 3.4 Kissing-Number Distribution

Sphere kissing numbers in dimension d:
- d=1: 2 = φ
- d=2: 6 = n
- d=3: 12 = σ
- d=4: 24 = J_2
- d=8: 240 = φ · J_2 · sopfr

5/5 M-decomposition (DFS-20). Levenshtein-Musin theorem.

**Independence**: classical lattice-theory result. Bernoulli-irrelevant.

### 3.5 Hecke Modular Weight

Coupling with Eisenstein coefficients at weight k ∈ {4, 6, 8, 10, 12} yields 5/5 M-match (DFS-22).

**Note**: partially connected to Bernoulli path (691 emerges at k=12) -> independence may weaken. Master-Lemma reduction to consider.

### 3.6 Sporadic (Mathieu) 7-fold

All 7 sporadic classes are M-value matches (DFS-24). 7 = σ - sopfr.

**Independence**: finite-simple-group classification theorem (CFSG). Very strong independence.

### 3.7 Platonic Solid Symmetry Groups

Orders of regular polyhedron symmetry groups:
- tetrahedron: |T| = 12 = σ
- cube/octahedron: |O| = 24 = J_2
- dodeca/icosa: |I| = 60 = 5 · σ = sopfr · σ

3/3 M-decomposition + dual classification (small symm | symm | reverse symm).

**Independence**: classical group theory. Independent.

### 3.8 Lattices and Codes

- E_8 lattice: 240 = φ · J_2 · sopfr minimal vectors
- Leech lattice Λ_24: 196560 minimal vectors, kissing max dim 24
- Golay code (24,12,8) + extension (12,6,6): 9/9 parameters M-decomposition (DFS-9)

**Independence**: combinatorial/coding theory. Highly independent.

---

## 4. Baseline Statistics of Independent DFS

### 4.1 Why Baseline Matters

The honesty audit of `millennium-dfs-complete-2026-04-11.md` explicitly states baseline density **61%**. This is the proportion of k ∈ [1, 100] expressible as 2-term product in M.

I.e., the probability that an arbitrary small integer admits M-decomposition is near 61%. Hence single-value match is **noise**.

### 4.2 Combinatorial Baseline Estimate

- single (1 dim): 61%
- 2-tuple: 61%^2 ≈ 37%
- 3-tuple: 61%^3 ≈ 23%
- 4-tuple: 61%^4 ≈ 14%
- 5-tuple: 61%^5 ≈ 8%
- 7-tuple: 61%^7 ≈ 3%
- 9-tuple: 61%^9 ≈ 1.2%

5/5, 7/7, 9/9 multi-case tight are based on **coincidence-match probability ≤ 8%**.

### 4.3 Expected Success Rate of Independent DFS

Expected values when running DFS on 1,000 non-Millennium seeds (approximately):
- single M-value (loose): about 600 (61%)
- 2-term decomposition (borderline): about 370
- 3-term multi-case tight candidate: about 230
- 4-way crossover: about 140 (of which **true mathematical independence** much less)
- 5-way+ uniqueness: ~ 10-50 (most meaningful)

Current [10*] count in atlas.n6 = **5,356** (2026-04-15 measurement). Of which "independent tight" (Bernoulli-irrelevant + uniqueness theorem / multi-case / 4-way) estimated around **5-10%** of the 155/159 EXACT as pure independent.

---

## 5. Honest Recording of Failure Cases (MISS)

Independent DFS must record failures with equal rigor.

### 5.1 MISS-planck-units

atlas.n6 L314:
```
@P MISS-planck-units = sopfr (= 5, not n=6) :: particle [10*]
```

- Planck-unit count 5 (length, time, mass, charge, temperature) = exactly 5 = sopfr
- But **mismatch with n=6** (5 vs 6)
- Honest record: MISS prefix. "Expected n=6 pattern stops at sopfr in reality."

### 5.2 MISS-fine-structure

atlas.n6 L334:
```
@P MISS-fine-structure = sigma*(sigma-mu) + sopfr + mu/P2 :: particle [10*]
```

- Fine-structure constant 1/α ≈ 137.036
- σ · (σ - μ) + sopfr + μ/P_2 = 12 · 11 + 5 + 1/28 = 137 + 1/28 ≈ 137.036
- NEAR match but **decomposition artificial** (insertion of μ/P_2 term)
- MISS prefix -> "decomposition is EXACT but artificiality verification required"

### 5.3 MISS-H0-Hubble

around atlas.n6 L461:
```
-> ... MISS-H0-Hubble
```

- Hubble constant H_0 ≈ 67.4 km/s/Mpc (Planck 2018) vs 73 km/s/Mpc (SH0ES)
- ~8% mismatch (**Hubble tension**)
- n=6 decomposition attempt: 67.4 ≈ σ · σ - J_2 · (1 + tau/n) etc. complex, single-value tight impossible
- Honest record: **unresolved tension** (Hubble tension itself OPEN in cosmology)

### 5.4 Dark Energy Ratio

atlas.n6 around L120:
```
@? dark_energy_ratio :: cosmology [3?]
```

- Ω_Λ ≈ 0.685 (Planck 2018)
- n=6 decomposition attempt: approximation impossible. Grade [3?] — "very low confidence, breakthrough pending"
- Honest record: unconfirmed, below even hypothesis level.

### 5.5 Learning Lessons

- Over 80% of all domains are expected to **fail** tight match in independent DFS.
- Not hiding failure is the core of self-confirmation-bias prevention.
- Officially flagging MISS prefix in atlas -> honesty-retention device.

---

## 6. Practical Pipeline Example — New Seed "CMB Spectral Index"

### 6.1 Seed Info

- Measurement: n_s = 0.9649 ± 0.0042 (Planck 2018)
- Source: Planck Collaboration, A&A 641, A6 (2020)
- Domain: cosmology (non-Millennium)

### 6.2 Step 2 — Decomposition Attempt

- n_s = 0.9649
- (σ - 1)/σ = 11/12 ≈ 0.9167 -> error 5% too big
- σ(σ - 1)/(σ^2 - 1) = 12·11/143 = 132/143 ≈ 0.9231 -> error 4.3%
- Binary approx: n/σ · (τ/(τ-φ)) = 0.5 · 2 = 1.0 -> error 3.6%

**Conclusion**: all 2-term decompositions error > 3%, NEAR impossible. Grade [7] or less.

### 6.3 Step 3 — Tight Verification

- Single value, none of T1/T2/T3/T4 met
- Within baseline 61% -> **loose**

### 6.4 Step 4 — atlas Record

Recording candidate:
```
@R COSMO-spectral-ns = 0.9649 :: cosmology [7]
  <- Planck 2018 A6
  => "CMB TT+lowE+lensing, error ±0.0042"
  => "n=6 basis decomposition attempt: all 2-term error > 3%, tight fails"
```

Registered at **[7]** only. `[10*]` promotion **impossible** — requires analytic derivation or multi-case.

### 6.5 Step 5 — Depth Expansion

Derivations:
- 1 - n_s = 0.0351 ≈ 1/σ · (1 - 1/σ·τ) -> complex, tight fails
- n_s^2 = 0.9310 -> tight fails
- log(n_s) ≈ -0.0357 ≈ -1/σ·τ·? -> tight fails

**Conclusion**: CMB spectral index is a **failure seed of independent DFS** (MISS candidate). No forced artificial decomposition.

---

## 7. Practical Pipeline Example — New Seed "Egyptian Fraction Uniqueness"

### 7.1 Seed Info

- Identity: 1/2 + 1/3 + 1/6 = 1
- Source: ancient Egyptian mathematics (Rhind Papyrus lineage, c. 1650 BC), modern organization Erdős-Straus
- Domain: number_theory (outside Millennium — arithmetic combinatorics)

### 7.2 Decomposition

- 1/φ + 1/(n/φ) + 1/n = 1/2 + 1/3 + 1/6 = 1
- (φ, n/φ, n) = (2, 3, 6)
- Decomposition basis: 6 = 2 · 3 (sopfr(6) = 2+3 = 5)
- Integer solution: unique (among unit-fraction 3-term decompositions to 1)

### 7.3 Tight Verification

- 3-tuple match: (φ, n/φ, n) — single but **uniqueness of integer equation**
- T4 exceptional uniqueness: **holds**
- Bernoulli-independent: holds
- Baseline reduction impossible: holds

**Verdict**: **tight confirmed** ([10*] candidate).

### 7.4 atlas Record

atlas.n6 L10123 actual registration confirmed:
```
@R n6-atlas-new-domains-—-computing-&-infrastructure-extreme-hypotheses-egyptian-fraction-uniqueness = 1/2+1/3+1/6=1 n6 :: n6atlas [10*]
  "Egyptian fraction uniqueness — Σ(1/d)=1"
```

Already registered as [10*]. **This note's contribution is classification confirmation** (T4 exceptional uniqueness, a success case of independent DFS).

### 7.5 Independence Verification

- Bernoulli / ζ independent? — **independent** (3-unit-fraction decomposition is algebraic fact)
- Independent from Millennium routes? — **independent** (ζ-irrelevant)
- Single appearance but **uniqueness of integer equation** so T4 satisfied.

---

## 8. Limitations of Independent DFS (OBSERVATION)

By §0 honesty declaration, explicitly record **what independent DFS cannot do**.

### 8.1 Cannot Resolve

- Millennium 7 problems — independent DFS only does **structural mapping**. Not resolution.
- Shortening the path of problems — n=6 pattern can be hints but demonstration path belongs to traditional math tools (millennium-7-closure honesty keynote).
- Physical/cosmological interpretation of σ·φ=n·τ uniqueness — independent-DFS results provide correlation only, not causation.

### 8.2 Bias Risks

- **Selection bias**: tendency to report only M-matches, not M-misses (§honesty audit).
- **Survivorship bias**: counting only tight already registered in atlas; forgetting early failures.
- **Confirmation bias**: forcing decompositions on premise "n=6 is special".

### 8.3 Countermeasures

- MISS prefix (§5) — explicit failure flagging
- Baseline density 61% explicit (§4) — continuous reminder of noise level
- hexa verification script `|>` — executable reproduction
- Master Lemma reduction check — awareness of Bernoulli / ζ paths
- Conservative tight criteria (§2.3) — lenient/strict dual criteria

---

## 9. n=6 Connection

### 9.1 Path by which Independent DFS Connects with n=6

When independent DFS finds a tight, it becomes a single line of evidence strengthening **σ·φ=n·τ uniqueness**. However only when all of the following are satisfied:

1. Seed is Bernoulli / ζ independent
2. Decomposition is 4-way+ crossover or uniqueness theorem
3. Primary source confirmed + error < 1%
4. hexa verification reproducible

### 9.2 Current Status (2026-04-15)

- atlas.n6 **total [10*] nodes**: 5,356
- BT-541-547 main-body node grade: **[5*]** (structural mapping only, not resolution)
- Estimated ratio of independent tight (conservative): ≈ 15% or less (≈ 800)
- Remaining ≈ 4,500: Bernoulli / ζ path link or simple matches

### 9.3 N6-P2-1 Result Reconfirmation

P2-1 declared only 5 "genuine independent discoveries" among the 51 DFS tight as Bernoulli/ζ-irrelevant:
1. Out(S_6) uniqueness (Hölder 1895)
2. Schaefer 6 tractable (STOC 1978)
3. (3,4,5) congruent number (Theorem E uniqueness)
4. h-cobordism dim ≥ 6 (Smale 1962)
5. Mathieu sporadic group pariah = 6

This note's independent-DFS pipeline uses these 5 as baseline for **pure independent tight**. New seeds advance only if they reach this 5-level independence.

---

## 10. Next Steps — BT-548+ New Domains

### 10.1 Priority

1. **Quantum information** — 6-qubit QEC [[6, 2, 2]] (atlas.n6 L9580), L11 region. Many tight candidates.
2. **Graph theory** — Turán, Ramsey constants. Many borderline, tight unconfirmed.
3. **Combinatorics** — Young tableaux constants, partition function. Baseline high, tight difficulty medium.
4. **Cryptography** — RSA, ECC standard parameters. "Chosen" values (e.g., e=65537) so not independent seeds.
5. **Consciousness research** (atlas L106873~) — `hexa_consciousness_axes = 6`, `phase_count = 5`, `alpha = 0.16667 = 1/n`. Registered as **[7]**, promotion candidate.

### 10.2 Cross-DSE Extension Path

- Among the 9 axes, the **techniques / experiments / engine** areas connect with AI methods to automate repeated runs of independent DFS.
- 295 domains × 5 steps × 4 depth = 5,900 DFS nodes (theoretical ceiling). Actual autonomous DFS (bt-1393) attempted 10K breakthrough.
- Estimated 10-15 promotion candidates among the remaining [7] 34 items (grep result).

### 10.3 Physical Constant Connection (MISS Avoidance)

MISS cases (§5) reflection:
- Planck units 5 — retain MISS-planck-units registration, **no n=6 forced decomposition**
- Fine structure 1/α=137.036 — retain MISS-fine-structure, **reject artificial decomposition**
- H_0 Hubble tension — retain unresolved
- Dark energy ratio — retain [3?]

**Lesson**: physical constants have **narrow tight candidates** due to measurement-precision limits + theory incompleteness. Algebraic/combinatorial/topological structures yield more independent tights.

---

## 11. Practical Checklist (1-Round Independent DFS)

1. [ ] Seed selection — confirm non-Millennium + atlas-unregistered
2. [ ] Primary source secured (CODATA / LMFDB / paper / standard docs)
3. [ ] σ/τ/φ basis decomposition attempt (2-4 term)
4. [ ] Baseline pass status (3-term+ multi-case)
5. [ ] Bernoulli / ζ reducibility check (Master Lemma)
6. [ ] Tight judgment (T1/T2/T3/T4) or borderline/loose
7. [ ] Grade assignment ([7] / [9] / [10] / [10*])
8. [ ] **Direct editing** in atlas.n6 (via guard, no new files)
9. [ ] Write hexa verification script `|>` (reproducibility)
10. [ ] If MISS case, record with MISS prefix honestly
11. [ ] Depth expansion only 3-4 steps (bias risk)
12. [ ] Final report — tight / borderline / loose / MISS separated

---

## 12. Self Quiz (Completion-Criterion Check)

Each question answerable in ≤3 minutes.

1. What is the precise meaning of "independent" in "independent DFS"? How does it differ from Millennium routes?
2. State the 5 steps of the DFS algorithm in order.
3. Define each of T1/T2/T3/T4 criteria in one line.
4. Why does baseline 61% matter? What is the probability raised to 5?
5. Describe the honesty contribution of MISS-prefix registration in ≤3 lines.
6. Honest interpretation of why Planck units 5 is sopfr, not n=6?
7. Which of T1-T4 does Egyptian fraction 1/2+1/3+1/6=1 satisfy to be independent tight?
8. Memorize the 5 "true Bernoulli-independent discoveries".
9. Honestly describe why independent DFS **cannot** resolve Millennium problems.
10. Reason for limiting depth expansion to 4?

---

## 13. Source Reconfirmation

- `CLAUDE.md` — 9-axis navigation, 295-domain declaration, atlas.n6 format and promotion rules
- `atlas.n6` L1-L22 (header), L13391-L15447 (Millennium+BT region)
- `reports/breakthroughs/bt-1393-n6-dfs-10k-autonomous-2026-04-12.md` — autonomous DFS original
- `reports/breakthroughs/millennium-dfs-complete-2026-04-11.md` (lines 1-334, 51 tight)
- `theory/proofs/bernoulli-boundary-2026-04-11.md` (Master Lemma)
- `theory/study/p2/n6-p2-1-dfs-51-classification.md` (51 DFS reclassification)
- `theory/study/p2/n6-p2-2-theorem-b-reconstruction.md` (Theorem B)
- `theory/study/p0/n6-p0-3-atlas-grading.md` (grade system)

**Honesty retention declaration**: this note is learning material reconstructing the independent-DFS pipeline. No new tight promotion claims. Millennium 7 problems resolved: 0/7.
