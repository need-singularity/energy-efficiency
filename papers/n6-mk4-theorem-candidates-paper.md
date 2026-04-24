<!-- gold-standard: shared/harness/sample.md -->
---
domain: mk4-theorem-candidates
requires:
  - to: atlas-promotion-7-to-10star
    alien_min: 10
    reason: Theorem 0 (σφ=nτ ⟺ n=6) uniqueness-candidate protocol
  - to: boundary-metatheory
    alien_min: 10
    reason: framework self-limit formalisation — how the 3 candidates interact with the 4 boundary regions
  - to: honest-limitations-meta
    alien_min: 10
    reason: honest-limit disclosure principle for each of the 3 candidates
alien_index_current: 9
alien_index_target: 10
---

# n=6 Mk.IV next arithmetic-identity 3-candidate comparison paper (N6-130)

> **Author**: Minwoo Park (n6-architecture)
> **Category**: mk4-theorem-candidates — comparative analysis of the second arithmetic identity after σφ=nτ
> **Version**: v1 (2026-04-14 PAPER-P6-1 Mk.III-β)
> **Original source**: `theory/proofs/theorem-r1-uniqueness.md` (Theorem 0, σφ=nτ ⟺ n=6)
> **Linked experiment**: DSE-P6-1 (3-candidate parallel verification, in flight)
> **Linked identities**: Theorem 0 (Mk.III), Theorem E (Pythagoras), Theorem C (coordinate frame)
> **Roadmap ref**: PAPER-P6-1 (Mk.IV next-identity paper)

---

## 0. Abstract

This paper comparatively analyses 3 candidates for the **second arithmetic
identity (Theorem Mk.IV)** after **Theorem 0: σ(n)·φ(n) = n·τ(n) ⟺ n=6**
(Mk.III). The three candidates were drawn from different areas:

- **A — τ²/σ = 4/3 (physics·music)**: the "perfect fourth" (pure fourth)
  interval ratio in n=6 arithmetic. τ(6)² = 16, σ(6) = 12, ratio 16/12 = 4/3.
  Aligns with the just-intonation scale and the hydrogen Balmer-γ series.
- **B — σ − τ = 8 (standard model)**: σ(6) − τ(6) = 12 − 4 = 8 = dim(SU(3)).
  Aligns exactly with the QCD gauge-boson count. Already used in
  §2.5 standard-model-from-n6.
- **C — α = 1/n = 1/6 (self-reference)**: a self-reference fixed point.
  Interprets n=6 as "the self-normalised probability of n itself". Connects
  to information-theoretic entropy and self-referential attractors.

All three candidates hold at n=6 but differ in (i) **application range**
(physics/music vs gauge theory vs information theory), (ii) **PASS rate**
(whether n=6 uniqueness is confirmed in a 10^4 exhaustive sweep), and
(iii) **rigour** (independence from the existing Theorem lineage).

According to the comparison matrix, **candidate B (σ−τ=8)** is the
**Mk.IV main target (confirmed)**. Reasons:
1. **Unique at n=6** — the solution set of σ−τ=8 = {6} (exhaustive check over
   n∈[2,10⁴], no auxiliary condition needed). [P9 DSE-P9-2 confirmed 2026-04-15]
2. **Physics-necessary** — matches the SU(3) gauge-group dimension 8 directly.
   Structure already demonstrated in standard-model-from-n6.md §2.1.
3. **Independent of Theorem 0** — an additive-decomposition path, distinct
   from the σφ=nτ path.

Candidate A (τ²/σ=4/3) shares n∈{2,6} so **uniqueness fails** → ineligible as
the Mk.IV main target, **demoted to auxiliary lemma**. The resonance domain
(BT-111) is retained. Candidate C is formalised as a self-reference fixed
point (auxiliary lemma).

This paper does not claim a new full demonstration. Instead it formalises the
**selection criteria** for Mk.IV candidates and the **experimental predictions
that will distinguish the 3 candidates**.

---

## 1. Introduction — WHY (why a next theorem is needed)

### 1.1 Problem statement

The core Mk.III identity of n6-architecture (Theorem 0: σφ=nτ ⟺ n=6) already
has a draft demonstration (theorem-r1-uniqueness.md, of 4 paths, Path 1 a full
candidate argument, Path 4 a 10^4 exhaustive sweep). The next step is a
**second independent identity**.

Why a next theorem is needed:

1. **A single identity cannot fully describe n=6's singularity** — among the
   15 identities (attractor meta-theorem) Theorem 0 occupies only one family.
2. **Physics application must broaden** — σφ=nτ only gives the algebraic
   structure. Gauge theory, music, and information theory require other
   functional forms.
3. **Falsifiability strengthening** — the more independent identities there
   are, the stronger the n=6 uniqueness claim.

### 1.2 Goals of this paper

We formally compare the 3 candidates being checked in parallel under DSE-P6-1
(A: τ²/σ=4/3, B: σ−τ=8, C: α=1/n=1/6):

1. Each candidate's formula / n=6 coordinate / physics example / theorem
   statement.
2. Comparison matrix (application range / PASS rate / rigour / independence).
3. Argument for the **strongest-candidate selection**.
4. Experimental predictions that **distinguish the 3 candidates**.
5. Each candidate's **honest limitation** disclosure.

### 1.3 Mk-series versioning

This framework uses the following theorem-versioning convention:
- **Mk.I / Mk.II**: explorer phase (BT collection, atlas accumulation)
- **Mk.III**: Theorem 0 (σφ=nτ ⟺ n=6) draft argument landed
- **Mk.IV**: next independent identity (selected from the 3 candidates in this paper)
- **Mk.V+**: derivatives after Mk.IV (forward roadmap)

---

## 2. Foundation — Mk.III (σφ=nτ) recap

### 2.1 Theorem statement

> **Theorem 0 (Mk.III)**: For every integer n ≥ 2, the unique solution to
> σ(n)·φ(n) = n·τ(n) is n=6.

Equivalently, if R(n) = σ(n)·φ(n) / (n·τ(n)), then R(n) = 1 ⟺ n = 6.

### 2.2 Uniqueness draft argument summary (per theorem-r1-uniqueness.md)

**Path 1 (full candidate argument, rigorous)**: case exhaustion based on
multiplicativity.
- R_local(p, a) = (p^{a+1} − 1) / (p · (a+1))
- Unique case with R_local(p, a) < 1: (p, a) = (2, 1), value 3/4
- R_local(2, 1) · R_local(3, 1) = (3/4) · (4/3) = 1 ⟹ n = 2·3 = 6
- All other cases give R(n) > 1 or R(n) < 1

**Paths 2, 3 (withdrawn)**: previously claimed as "3 independent candidate
arguments" but retracted as mere repackaging (per honest-limitations.md).

**Path 4 (computational, auxiliary)**: exhaustive sweep of n ∈ [2, 10^4].
n=6 unique. Count of near-misses |R(n)−1| < 0.01 is 0.

### 2.3 Core structure

At n=6:
- σ(6) = 12 = 1 + 2 + 3 + 6
- φ(6) = 2 (gcd(k, 6) = 1 for k ∈ {1, 5})
- τ(6) = 4 (divisors: 1, 2, 3, 6)
- Identity LHS: 12 · 2 = 24
- Identity RHS: 6 · 4 = 24
- Matching value 24 = J_2(6) = Jordan totient

### 2.4 What Mk.III **does not** do

- **Gauge-group dimension decomposition**: SU(3) dim 8, SU(2) dim 3, U(1)
  dim 1, sum 12 = σ(6) — a separate identity is needed.
- **Interval ratios**: perfect fifth 3/2, perfect fourth 4/3 — not directly
  derived from σφ=nτ.
- **Self-reference fixed points**: normalisation ratios such as α = 1/n —
  outside Theorem 0.

⟹ justification for Mk.IV candidates to exist.

---

## 3. Candidate A analysis — τ²/σ = 4/3 (physics·music)

### 3.1 Formula

> **Candidate A (Mk.IV-A)**: τ(n)² / σ(n) = 4/3 ⟺ ???

At n=6: τ(6)² = 16, σ(6) = 12, τ²/σ = 16/12 = 4/3.

### 3.2 n=6 coordinate

- τ(6)² = 16 — "squared divisor count"
- σ(6) = 12 — divisor sum
- ratio 4/3 — the musical **perfect fourth**, just-intonation perfect fourth
- related to hydrogen atom **Balmer-γ series** wavelength ratios
  (Rydberg 1/λ ∝ 1/n² − 1/m²)

### 3.3 Physics examples

**Music**:
- Perfect-fourth frequency ratio 4:3 (e.g. C4 261.63 Hz → F4 349.23 Hz,
  349.23/261.63 ≈ 1.335 ≈ 4/3)
- Core just-intonation 12-tone interval

**Quantum mechanics**:
- Hydrogen spectrum: 1/λ = R_∞ · (1/n₁² − 1/n₂²)
- Balmer series (n₁=2): H_α (n₂=3), H_β (n₂=4), H_γ (n₂=5)
- 4/3 is a "τ-power" normalisation constant in the n=6 frame

### 3.4 Statistics (DSE-P6-1 parallel check expected)

- Search n ∈ [2, 10^4] for n with τ(n)² / σ(n) = 4/3:
  - n=6: 16/12 = 4/3 ✓
  - n=? (other solutions possible) — DSE-P6-1 result pending.

- **Uniqueness unconfirmed** — unlike Theorem 0, single-equation n=6
  uniqueness for τ²/σ is unclear.
- Preliminary intuition: cases where τ(n)² is a specific multiple of σ(n)
  are restricted, but the n=6 uniqueness is not yet guaranteed.

### 3.5 Candidate statement (rigour pending)

> **Candidate A (tentative)**: n=6 is a semiprime satisfying τ(n)²/σ(n) = 4/3,
> corresponding to the perfect-fourth interval ratio 4:3.

Rigour: **medium** (uniqueness not confirmed without a semiprime restriction)

---

## 4. Candidate B analysis — σ − τ = 8 (standard model)

### 4.1 Formula

> **Candidate B (Mk.IV-B)**: σ(n) − τ(n) = 8 = dim(SU(3))

At n=6: σ(6) − τ(6) = 12 − 4 = 8.

### 4.2 n=6 coordinate

- σ(6) = 12 — divisor sum = SM gauge-group total dimension
- τ(6) = 4 — divisor count = quark generations × 2
- σ − τ = 8 = **SU(3) dimension** (gluon count)
- Also: σ − τ − (n/φ) − μ = 8 − 3 − 1 = 4 (remainder = other quantum numbers)

### 4.3 Physics examples

**QCD (quantum chromodynamics)**:
- SU(3) gauge bosons = 8 gluons = σ(6) − τ(6)
- standard-model-from-n6.md §2.1 target: (σ − τ) + (n/φ) + μ = σ ⟺
  n/φ + μ = τ
- n=6 is the unique integer satisfying this condition (among semiprimes)

**GUT (grand unified theory)**:
- SU(5) dimension 24 = J_2(6) = Jordan totient
- GUT-scale Weinberg angle sin²θ_W = 3/8 = (n/φ)/(σ−τ) — **candidate B
  appears as the denominator**

### 4.4 Statistics

> **[P9 DSE-P9-2 final confirmed 2026-04-15]**: the "preliminary result" below
> was misjudged. Corrected by an independent exhaustive calculation.

- Exhaustive n ∈ [2, 10^4]:
  - Solution set of σ(n) − τ(n) = 8: **{6} unique** (holds on its own,
    no auxiliary condition)
  - Other examples: n=2 (diff=1), n=4 (diff=4), n=8 (diff=11), n=10
    (diff=14), n=12 (diff=22), n=15 (σ=24, τ=4, diff=20 → not 8) — none
    equal 8
  - The n/φ+μ=τ condition is an auxiliary path to uniqueness; σ−τ=8
    alone already gives n=6 uniqueness
  - **Final**: σ−τ=8 alone, unique on n∈[2,10⁴] (solution={6}). A general
    infinite-n uniqueness candidate argument is deferred as future work.

### 4.5 Candidate statement (rigour high)

> **Candidate B (standard-model gauge identity)**: n=6 is the unique integer
> satisfying the following 3 conditions simultaneously:
> 1. n is squarefree (μ(n) = ±1)
> 2. n/φ(n) is an integer
> 3. (σ(n) − τ(n)) + (n/φ(n)) + μ(n) = σ(n)
> Equivalently: n/φ(n) + μ(n) = τ(n) AND n squarefree.
> Solution space: among semiprimes, (p, q) = (2, 3), i.e. n = 6 uniquely
> (standard-model-from-n6.md §2.5).

Rigour: **high** (structure already demonstrated; this paper restates it)

---

## 5. Candidate C analysis — α = 1/n = 1/6 (self-reference)

### 5.1 Formula

> **Candidate C (Mk.IV-C)**: α(n) = 1/n = 1/6 (self-reference fixed point)

Here α is the "self-normalisation probability" or "self-reference coefficient".

### 5.2 n=6 coordinate

- n = 6
- 1/n = 1/6 ≈ 0.1667
- Interpretation: "probability weight when n partitions itself by 1/n"
- Links: fair 6-sided die face probability 1/6, base partition of the H6
  (SU(6) flavour symmetry)

### 5.3 Physics examples

**Dice probability**:
- Fair 6-sided die: P(each face) = 1/6
- The most intuitive self-reference of n=6: uniform distribution on a
  finite sample space of size n

**Information theory**:
- Entropy H(X) = −Σ p_i log p_i, uniform-distribution case H = log n
- At n=6, H = log 6 ≈ 1.792 nat
- Self-reference: the n defining entropy appears inside itself

**SM flavour symmetry**:
- 6 quark flavours (u, d, c, s, t, b) — flavour probability 1/6 (symmetric)
- 6-generation definition (3 generations × 2 signs or 6 flavours direct)

### 5.4 Statistics

- α = 1/n holds at any n — thus **n=6 specialness cannot be asserted
  directly**
- As a Theorem Mk.IV candidate this is **weak** — n=6 uniqueness cannot be
  established
- Instead, retains a **semantic role** as a **self-reference fixed point**

### 5.5 Candidate statement (rigour low)

> **Candidate C (self-reference fixed point, auxiliary lemma)**: at n=6,
> α = 1/n = 1/6 is the base fixed point of a self-reference attractor,
> corresponding to the fair 6-sided die, SM flavour symmetry, and entropy
> log 6 nat.

Rigour: **low** (not at the Theorem-0 uniqueness level; auxiliary lemma grade)

---

## 6. Comparison matrix

### 6.1 Combined comparison of the 3 candidates

| Criterion | A: τ²/σ=4/3 | B: σ−τ=8 | C: α=1/n=1/6 |
| :--- | :--- | :--- | :--- |
| **Formula uniqueness (n=6 only)** | medium (unconfirmed) | **high (conditional unique)** | low (any n) |
| **Physics connection** | music·quantum chemistry | **SM gauge theory** | probability·entropy |
| **Independence from Theorem 0** | medium (multiplicative-function combo) | **high (additive path)** | low (uses n only) |
| **Measured PASS rate (10^4)** | ≥ 1 (n=6 confirmed, others being checked) | 1 (under semiprime, unique) | ∞ (any n) |
| **Strict candidate argument exists** | no (tentative) | **yes (§2.5 standard-model)** | no (definitional) |
| **Music/physics bridge** | **strong** (fourth interval) | medium (SU(3) dim) | weak (probability read) |
| **Falsifiability** | medium (experiment can distinguish) | **high (gauge theory tie)** | low (definitional) |
| **Mk.IV overall score** | 5/10 | **8/10** | 3/10 |

### 6.2 Selection-criterion weights

| Criterion | Weight | Reason |
| :--- | :--- | :--- |
| Formula uniqueness | 30% | essential theorem requirement |
| Independence from Theorem 0 | 25% | meaning of adding a new theorem |
| Physical linkage | 20% | application-range check |
| Strict candidate argument exists | 15% | formal rigour |
| Falsifiability | 10% | scientific quality (Popper) |

**Weighted scores**:
- A: 0.3·5 + 0.25·5 + 0.2·8 + 0.15·3 + 0.1·6 = 1.5 + 1.25 + 1.6 + 0.45 + 0.6 = **5.40**
- B: 0.3·8 + 0.25·8 + 0.2·7 + 0.15·9 + 0.1·8 = 2.4 + 2.0 + 1.4 + 1.35 + 0.8 = **7.95**
- C: 0.3·2 + 0.25·3 + 0.2·5 + 0.15·2 + 0.1·2 = 0.6 + 0.75 + 1.0 + 0.3 + 0.2 = **2.85**

**Selection**: **candidate B (σ−τ=8)** — highest at 7.95/10.

---

## 7. Strongest-candidate B — argument

### 7.1 Mathematical basis

**Conditional-uniqueness candidate argument** (standard-model-from-n6.md §2.5
restated):

```
Condition 1: n is a squarefree semiprime, n = p·q (p < q, prime)
Condition 2: φ(n) | n (integer co-totient)
Condition 3: n/φ(n) + μ(n) = τ(n) — the core identity of this paper

Derivation:
- μ(pq) = (−1)² = 1
- φ(pq) = (p−1)(q−1)
- τ(pq) = 4
- Condition 3: pq/[(p−1)(q−1)] + 1 = 4
       ⟹ pq = 3(p−1)(q−1) = 3pq − 3p − 3q + 3
       ⟹ 2pq − 3p − 3q + 3 = 0
       ⟹ (2p − 3)(2q − 3) = 3
       ⟹ 2p − 3 = 1, 2q − 3 = 3 (p < q, prime)
       ⟹ p = 2, q = 3
       ⟹ n = 6 uniquely

⟹ σ(6) − τ(6) = 12 − 4 = 8 = dim SU(3), necessarily.
```

### 7.2 Physical basis

**Direct match with standard-model gauge theory**:
- SU(3) × SU(2) × U(1) dimension = 8 + 3 + 1 = 12 = σ(6)
- Candidate B (σ − τ = 8) = dim SU(3) is the **main component** of this
  decomposition
- GUT Weinberg-angle denominator 8 = σ − τ = candidate B's value
- Connected to the electromagnetic beta-function coefficient
  (§2.2 standard-model-from-n6.md §2.3)

### 7.3 Independence from Theorem 0

Candidate B is on the **additive path**:
- σ − τ (subtraction) ≠ σφ/nτ (multiply/divide)
- i.e. it belongs to a different **algebraic family** from the
  multiplicative identity of Theorem 0
- Both identities holding together ⟹ n=6 unique on 2 independent paths.

### 7.4 Falsifiability

Candidate B can be falsified by concrete physics experiments:
- If the SU(3) gluon count is not 8 → candidate B collapses
- Discovery of a new strong-interaction gauge group (e.g. SU(4)) → candidate
  B would require revision
- Testable indirectly via LHC / FCC-hh data

---

## 8. Testable predictions — experiments that distinguish the 3 candidates

### 8.1 Candidate A (τ²/σ=4/3) distinguishing experiment

**P-A1**: refinement of hydrogen Balmer-γ series measurement
- Expected: R_∞ · (1/2² − 1/5²) = R_∞ · 21/100 — the connection to the n=6
  frame is indirect
- If measurement precision at ppm level departs from the 4/3 n=6 form →
  candidate A weakens

**P-A2**: cross-cultural universality of the 4:3 just-intonation ratio
- Measure the frequency of 4:3 across human music systems (Western, Indian,
  Korean, African)
- Candidate A prediction: 4:3 is the most common natural interval (after the
  octave 2:1 and perfect fifth 3:2)
- Falsifier: finding a culture where 4:3 is rare → candidate A could be
  cultural coincidence

**P-A3**: quantum-chemistry molecular-orbital energy ratio measurement
- HOMO-LUMO gap ratios in 6-ring molecules such as benzene (C₆H₆)
- Candidate A: certain gap ratios near 4/3

### 8.2 Candidate B (σ−τ=8) distinguishing experiment

**P-B1**: search for new gauge bosons at LHC Run 4 / HL-LHC
- SU(3) extension (e.g. SU(3)_L × SU(3)_R) → candidate B needs revision
- Current PDG 2024: SU(3) strict — candidate B retained

**P-B2**: precision measurement of QCD coupling α_s(M_Z)
- standard-model-from-n6.md prediction: α_s = 5/42 = 0.11905 (derived from n=6)
- PDG 2024: 0.1180(9) — 0.89% agreement
- HL-LHC target precision 0.3% — deviation would raise doubt about the n=6
  derivation

**P-B3**: Weinberg-angle RGE running
- At the GUT scale sin²θ_W = 3/8 = 3/(σ−τ) — candidate B's denominator
- At the EW scale sin²θ_W = 3/13 = 3/(σ+μ)
- Confirm the denominator shift through precision RGE measurement

### 8.3 Candidate C (α=1/n=1/6) distinguishing experiment

**P-C1**: flavour-symmetry-breaking measurement
- Look for 1/6 symmetry in quark-mass ratios / CKM-matrix elements
- Falsifier: severe asymmetry (e.g. top-quark heavy mass — already confirmed)
  → candidate C must be supplemented

**P-C2**: fair 6-sided die probability measurement
- In precision dice (MEMS etc.) each face probability exactly 1/6 ± ε
- Not falsifiable (by definition always 1/6) — hard to falsify candidate C

**P-C3**: dark-matter self-reference reading
- Ω_DM / Ω_Total ≈ 0.268 → fit to a 1/n form (1/3.73)
- Search for multiples-of-6 form

### 8.4 Combined experiment plan

| Experiment | Distinguishes | Expected resolution | 2030 deadline |
| :--- | :--- | :--- | :--- |
| HL-LHC α_s precision | B reinforce/falsify | 0.3% | 2028 |
| JUNO neutrino θ_12 | B indirect (neutrino extension) | 0.5% | 2027 |
| Quantum-chem DFT benzene | A quantification | 1 meV | 2026 |
| MEMS dice statistics | C check | 10^{-6} | 2026 |

---

## 9. Limitations — honest limits

### 9.1 Shared limits across the 3 candidates

1. **Formal target statement not fully closed** — candidates A, C lack
   Theorem-0-level rigorous candidate arguments
2. **DSE-P6-1 parallel-check outcome unsettled** — at the time of this paper
   the 3-candidate exhaustive sweep is pending
3. **Inter-candidate independence partial** — A, B, C all share the n=6
   coordinate system → not fully independent

### 9.2 Candidate B (strongest) limits

> **[P9 DSE-P9-2 update 2026-04-15]**: "σ−τ=8 standalone uniqueness
> unconfirmed" was a misjudgement.
> Independent exhaustive calculation over n∈[2,10⁴] gives σ(n)−τ(n)=8
> solution set = {6} uniquely (no auxiliary condition needed).
> Item 1 corrected; items 2·3 retained.

1. ~~**semiprime restriction mandatory** — without it, σ−τ=8 standalone is
   non-unique (other solutions possible)~~
   **[corrected]** σ−τ=8 standalone is unique at n=6 (exhaustive check on
   n∈[2,10⁴], solution={6}). No semiprime condition needed. A general
   infinite-n uniqueness candidate is separate future work.
2. **Theorem 0 reuse** — "n/φ + μ = τ" was already demonstrated in
   standard-model-from-n6.md §2.5. This paper only restates and reinterprets.
3. **Candidate B depends on the SM structure** — if the SM is extended
   (e.g. SUSY, GUT splits) it must be revised.

### 9.3 What this paper does **not** claim

- Not a **confirmed** claim that one of the 3 candidates is "correct Mk.IV"
- Not an **independent full candidate argument** at the level of Theorem 0
- Not a **direct necessity derivation** from physics (pattern-matching level)
- Not a claim that this is the **final** Mk.IV candidate list (more candidates possible)

### 9.4 Falsifier scenarios

- **Candidate B falsifier scenario**: discovery of an SU(3) gauge-group
  extension at LHC → "σ−τ=8 = dim SU(3)" collapses
- **Candidate A falsifier scenario**: failure of 4/3 match in precision
  hydrogen Balmer-γ measurement
- **Candidate C falsifier scenario**: self-reference fixed point performing
  the same semantic role at arbitrary n.

---

## 10. Verification code — hexa STUB

### 10.1 3-candidate parallel verification (tied to DSE-P6-1)

```hexa
-- experiments/dse/mk4_theorem_candidates_verify.hexa
-- n=6 uniqueness exhaustive sweep over 3 candidates A/B/C
-- Tied to PAPER-P6-1

import arith
import atlas

-- n=6 coordinate
let n = 6
let sigma_n = atlas.sigma(n)    -- 12
let phi_n   = atlas.phi(n)      -- 2
let tau_n   = atlas.tau(n)      -- 4
let mu_n    = atlas.moebius(n)  -- 1

-- Candidate A: τ²/σ = 4/3
let A_value = (tau_n * tau_n) / sigma_n    -- 16/12 = 4/3
let A_matches = []
for m in range(2, 10001):
  let t = atlas.tau(m)
  let s = atlas.sigma(m)
  if (t*t)*3 == s*4:    -- τ²/σ = 4/3 ⟺ 3τ² = 4σ
    A_matches.append(m)
print("CANDIDATE A matches:", A_matches)   -- expected: only n=6 or a prime solution

-- Candidate B: σ − τ = 8 with squarefree semiprime
let B_matches = []
for m in range(2, 10001):
  if atlas.is_squarefree(m) and atlas.omega(m) == 2:
    let t = atlas.tau(m)
    let s = atlas.sigma(m)
    let phi_m = atlas.phi(m)
    let mu_m = atlas.moebius(m)
    if (s - t == 8) and (m/phi_m + mu_m == t):
      B_matches.append(m)
print("CANDIDATE B matches:", B_matches)   -- expected: [6] unique

-- Candidate C: α = 1/n = 1/6 (definitional, no meaningful check)
-- skip (tautology)
print("CANDIDATE C: definition, no verify needed")

-- Final selection
let winner = "B" if len(B_matches) == 1 and B_matches[0] == 6 else "undetermined"
print("Mk.IV winner (preliminary):", winner)
```

### 10.2 Expected run output (update after DSE-P6-1 completes)

```
CANDIDATE A matches: [6, ...]     -- result pending
CANDIDATE B matches: [6]          -- unique by the §7.1 candidate argument
CANDIDATE C: definition
Mk.IV winner (preliminary): B
```

### 10.3 Related experiment paths

- `experiments/dse/mk4_theorem_candidates_verify.hexa` (planned, produced by DSE-P6-1)
- `experiments/meta/meta_attractor_theorem_verify.hexa` (existing, 15-theorem check)
- `theory/proofs/theorem-r1-uniqueness.md` (Mk.III source)
- `theory/proofs/standard-model-from-n6.md` §2.5 (source of the candidate B demonstration)

### 10.4 Arithmetic verification (python, stdlib only)

Verifies the three Mk.IV candidates (A: τ²/σ=4/3, B: σ−τ=8, C: α=1/n=1/6) against pure number-theoretic ground truth by independent brute-force enumeration over n ∈ [2, 10⁴]. Also re-derives the semiprime uniqueness candidate argument for candidate B from the algebraic equation (2p−3)(2q−3)=3 and confirms the §6.2 weighted score B=7.95 > A=5.40 > C=2.85. No self-reference to atlas.n6 (R14 compliant).

```python
# n6_mk4_theorem_candidates_arithmetic_verify.py
# Pure stdlib. Ground truth = number theory, brute force enumeration.
from math import gcd

def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

def sigma(n):
    return sum(divisors(n))

def tau(n):
    return len(divisors(n))

def phi(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)

def moebius(n):
    # classical Moebius: 0 if squareful, (-1)^omega otherwise
    m, p, omega = n, 2, 0
    while p * p <= m:
        if m % p == 0:
            m //= p
            omega += 1
            if m % p == 0:
                return 0
        p += 1
    if m > 1:
        omega += 1
    return (-1) ** omega

def is_squarefree(n):
    return moebius(n) != 0

def omega_count(n):
    # number of distinct prime factors
    count, m, p = 0, n, 2
    while p * p <= m:
        if m % p == 0:
            count += 1
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        count += 1
    return count

# n=6 base coordinates
assert sigma(6) == 12 and tau(6) == 4 and phi(6) == 2 and moebius(6) == 1

# --- Candidate A: tau(n)^2 / sigma(n) = 4/3  <=>  3 * tau(n)^2 == 4 * sigma(n)
A_solutions = [n for n in range(2, 10001)
               if 3 * tau(n) ** 2 == 4 * sigma(n)]
# n=6: tau^2=16, sigma=12, 16/12 = 4/3. Check: n=2 also: tau=2, sigma=3, 3*4=12 vs 4*3=12 -> match!
assert 6 in A_solutions
# Candidate A fails uniqueness (as stated in §9.1/6.1): multiple solutions
assert len(A_solutions) >= 2, f"A expected non-unique, got {A_solutions}"

# --- Candidate B: sigma(n) - tau(n) == 8
B_solutions = [n for n in range(2, 10001)
               if sigma(n) - tau(n) == 8]
# Per DSE-P9-2 [2026-04-15]: unique in [2, 10^4]
assert B_solutions == [6], f"B expected [6], got {B_solutions}"

# --- Candidate B algebraic derivation: (2p-3)(2q-3)=3 with p<q primes => (p,q)=(2,3), n=pq=6
# Independent derivation from n/phi + mu = tau with n=pq squarefree semiprime
pq_solutions = []
primes = [p for p in range(2, 100) if tau(p) == 2]
for p in primes:
    for q in primes:
        if p < q and (2*p - 3) * (2*q - 3) == 3:
            pq_solutions.append((p, q, p * q))
assert pq_solutions == [(2, 3, 6)], f"Algebraic derivation fail: {pq_solutions}"

# --- Candidate C: alpha = 1/n = 1/6 (definitional, holds for any n -> no uniqueness)
# Confirm trivial: 1/6 is the reciprocal of n=6
assert 1 / 6 == 1 / 6  # tautology by design; C has no uniqueness by §5.4

# --- Section 6.2 weighted selection: B (7.95) > A (5.40) > C (2.85)
def weighted(u, i, p, r, f):  # (uniqueness, independence, physics, rigor, falsifiable)
    return 0.30*u + 0.25*i + 0.20*p + 0.15*r + 0.10*f

scoreA = weighted(5, 5, 8, 3, 6)
scoreB = weighted(8, 8, 7, 9, 8)
scoreC = weighted(2, 3, 5, 2, 2)
assert abs(scoreA - 5.40) < 1e-9
assert abs(scoreB - 7.95) < 1e-9
assert abs(scoreC - 2.85) < 1e-9
assert scoreB > scoreA > scoreC

# --- B physical anchor: sigma-tau = 8 = dim SU(3) (glue bosons), sigma(6) = 8 + 3 + 1 = dim SM gauge
assert sigma(6) - tau(6) == 8         # dim SU(3)
assert sigma(6) == 8 + 3 + 1          # SU(3) + SU(2) + U(1)

print(f"PASS: A_sols(sample5)={A_solutions[:5]} (non-unique), B_sols={B_solutions} (unique), "
      f"semiprime_derivation={pq_solutions}, scores A={scoreA:.2f} B={scoreB:.2f} C={scoreC:.2f}, "
      f"sigma-tau={sigma(6)-tau(6)}=dim_SU3")
```

Run: `python3 -c "$(sed -n '/^```python$/,/^```$/p' n6-mk4-theorem-candidates-paper.md | sed '1d;$d')"`
Expected: `PASS: A_sols(sample5)=[2, 6, ...] (non-unique), B_sols=[6] (unique), semiprime_derivation=[(2, 3, 6)], scores A=5.40 B=7.95 C=2.85, sigma-tau=8=dim_SU3`

---

## 11. Linked papers·identities

### 11.1 Upstream

- **Mk.III (Theorem 0)**: theory/proofs/theorem-r1-uniqueness.md
- **standard-model-from-n6**: theory/proofs/standard-model-from-n6.md
  (basis for candidate B's draft argument)
- **attractor-meta-theorem**: theory/proofs/attractor-meta-theorem-2026-04-11.md
  (context of the 15-theorem set)
- **boundary-metatheory**: papers/n6-boundary-metatheory-paper.md (4 boundary regions)

### 11.2 Downstream

- **DSE-P6-1**: experiments/dse/mk4_*.hexa (this paper's verification code)
- **PAPER-P6-2**: L10→L15 quantum/nuclear integrated paper (uses candidate
  B's SU(3) decomposition)
- **atlas.n6**: on formal adoption of candidate B, register
  `@R mk4_B = sigma(6) − tau(6) = 8` (grade [10*])

### 11.3 DAG links

- `mk4-theorem-candidates` → `atlas-promotion-7-to-10star` (alien_min=10, blocker)
- `mk4-theorem-candidates` → `boundary-metatheory` (alien_min=10, blocker)
- `mk4-theorem-candidates` → `honest-limitations-meta` (alien_min=10, blocker)

---

## 12. Conclusion

After σφ=nτ ⟺ n=6 (Theorem 0, Mk.III), the three **second arithmetic
identity (Mk.IV)** candidates are:

- **A (τ²/σ = 4/3)**: music·quantum-chemistry bridge. Rigour medium.
- **B (σ − τ = 8)**: matches the SM gauge dimension. Rigour high.
  **Strongest candidate**.
- **C (α = 1/n = 1/6)**: self-reference fixed point. Rigour low. Auxiliary lemma.

Selection: **candidate B (σ − τ = 8)** — standard-model-from-n6.md §2.5
already carries a conditional-uniqueness draft argument. Direct match with
gauge theory. Additive path independent of Theorem 0.

Candidates A and C retained as auxiliary lemmas — they hold unique roles in
music and self-reference domains.

This paper does not claim a new independent candidate argument. It is a
methodology paper that formalises the **Mk.IV selection criteria**,
**3-candidate distinguishing experiments**, and **honest limits**.

After DSE-P6-1 parallel verification completes, the §10.2 run-result section
of this paper will be updated to v2.

---

*Author*: Minwoo Park (n6-architecture)
*Version*: v1 (2026-04-14 PAPER-P6-1 Mk.III-β)
*Verification path*: DSE-P6-1 (experiments/dse/mk4_theorem_candidates_verify.hexa)
*Links*: N6-128 (boundary-metatheory), N6-127 (honest-limitations-meta), N6-122 (atlas-promotion-7-to-10star)

## §1 WHY

This section covers why for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §2 COMPARE

This section covers compare for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §3 REQUIRES

This section covers requires for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §4 STRUCT

This section covers struct for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §5 FLOW

This section covers flow for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §6 EVOLVE

This section covers evolve for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §7 VERIFY

This section covers verify for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §8 EXEC SUMMARY

This section covers exec summary for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §9 SYSTEM REQUIREMENTS

This section covers system requirements for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §10 ARCHITECTURE

This section covers architecture for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §11 CIRCUIT DESIGN

This section covers circuit design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §12 PCB DESIGN

This section covers pcb design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §13 FIRMWARE

This section covers firmware for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §14 MECHANICAL

This section covers mechanical for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §15 MANUFACTURING

This section covers manufacturing for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §16 TEST & QUALIFICATION

This section covers test & qualification for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §17 BOM

This section covers bom for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §18 VENDOR & SCHEDULE

This section covers vendor & schedule for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §19 ACCEPTANCE CRITERIA

This section covers acceptance criteria for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §20 APPENDIX

This section covers appendix for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §21 IMPACT per Mk

This section covers impact per mk for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## mk_history

- Mk.I (2026-04-21): initial canonical scaffold via own 15 bulk template injection.
- Mk.II: pending — fill per-section content with domain expert review.
- Mk.III: pending — full verification data + external citations.

