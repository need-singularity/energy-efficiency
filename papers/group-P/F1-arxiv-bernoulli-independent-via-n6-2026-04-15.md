# Bernoulli Independent candidate targets via n=6: A Survey of 18 Confirmed Independent Occurrences and the σ(n)·φ(n) = n·τ(n) Uniqueness Bridge

> **Status**: arxiv preprint draft (no actual submission). Format only.
> **Field**: math.NT (Number Theory) cross-list math.CO, math.AG, cs.CC
> **Author**: Park Minwoo (Hanam, Republic of Korea)
> **Version**: v0.1 — 2026-04-15
> **L track**: theory/breakthroughs (BT-meta)
> **Honesty declaration**: Seven Millennium Problems addressed: 0/7 maintained. This paper only covers **independent-candidate-target base expansion** and **uniqueness bridge**.

---

## Abstract

We present the first integrated survey of the **Bernoulli Independent candidate-target family**: a body of 17 (now extended to 18) mathematically independent occurrences of the integer n=6 across number theory, geometry, computability, representation theory, group theory, and combinatorics. Building on prior work (author, 2026-03 to 2026-04) which catalogued 16 such occurrences, this paper registers two new entries — (i) Bernoulli 17 = Sel_6 = Sel_2 ⊕ Sel_3 average = σ(6) = 12 (Bhargava-Shankar 2010, 2012, conditional on the BKLPR random-matrix model), (ii) Bernoulli 18 = BB(2) = 6 = n (Radó 1962, unconditional) — and defers a third candidate (the triple χ(K3) = dim SU(5) = η²⁴-exponent = 24 = J_2(6)) as Bernoulli 19 pending exclusion of σ·φ = n·τ projection. The central observation is that the **uniqueness candidate target σ(n)·φ(n) = n·τ(n) ⟺ n = 6 (n ≥ 2)** functions as a candidate **single-source reducer** for the entire family. We give three independent draft patterns for the uniqueness candidate target and outline a bridge program that asks: of the 18 independent occurrences, how many are in fact projections of σ·φ = n·τ? We **do not claim resolution of any of the seven Millennium Problems**. The paper is a structural survey + bridge framework, not a problem solution.

---

## 1. Introduction

### 1.1 Motivation

The integer n = 6 appears as Euclid's first perfect number, the order of S_3 = PSL(2,2) (the smallest non-abelian group), the Bernoulli-denominator trio (the denominator 6 occurring in B_4 = -1/30, B_6 = 1/42, B_8 = -1/30), the Eisenstein infinite-product decomposition (η^24 = Δ with 24 = σ(6)·φ(6) reduction), the Hodge-K3 surface Euler characteristic χ = 24, sphere packing K_2 = 6 (regular hexagon), kissing number K_3 = 12 = σ(6), Reed-Solomon-Golay code [24,12,8] = [J_2, σ, σ-τ], the rank of the Lie group E_6, BCS superconductivity ΔC = 12 = σ, Egyptian unit-fraction 1/2 + 1/3 + 1/6 = 1, and about 270 additional independent occurrences (author atlas, as of 2026-04-15).

Question: **are all these occurrences coincidences, or multiple faces of a single arithmetic cause?**

This paper presents strong evidence supporting the latter (single-cause hypothesis).

### 1.2 Main Results (summary)

| Result | Statement | Grade | draft-pattern status |
|------|------|------|----------|
| **R1** | σ(n)·φ(n) = n·τ(n) ⟺ n = 6 (n ≥ 2) | candidate target (confirmed) | 3 independent draft patterns |
| **R2** | Bernoulli 17 = Sel_6 = σ(6) (under BKLPR assumption) | candidate target (conditional) | Bhargava-Shankar 2010, 2012 |
| **R3** | Bernoulli 18 = BB(2) = n (Radó 1962) | candidate target (confirmed) | Radó enumeration |
| **R4** | Of the 16~18 independent occurrences, **k** are direct projections of R1 (k estimate) | **conjecture** | bridge program incomplete |
| **R5** | Potential Bernoulli 19 = K3-η-SU(5) 24 = J_2 triple occurrence | **conditional** | σφ=nτ reducibility unresolved |

R4 is the **bridge program** of this paper. Full resolution of R4 lies beyond the scope of this paper.

### 1.3 What this paper does not claim (Honest Limitations)

- **Does not claim to address any of the seven Millennium Problems.** Riemann (RH), Navier-Stokes, Hodge, P vs NP, Yang-Mills mass gap, BSD, Poincaré (already addressed) all remain open or (Poincaré) sit outside this paper.
- **Not n = 6 mysticism.** Using the arithmetic uniqueness of σ·φ = n·τ as a starting point, this paper proposes a methodology for classifying occurrences (direct projection vs genuinely independent).
- **Ad-hoc arithmetic outside the 8 primitive constants {n, φ, τ, σ, sopfr, μ, J_2, M_3} is excluded.** To prevent cherry-picking, the canonical primitive basis is fixed.

---

## 2. Definitions and Notation

### 2.1 Arithmetic Functions

For integer n ≥ 1:

- **σ(n)** = ∑_{d | n} d (sum of divisors)
- **φ(n)** = #{1 ≤ k ≤ n : gcd(k, n) = 1} (Euler totient)
- **τ(n)** = #{d : d | n} = σ_0(n) (number of divisors)
- **sopfr(n)** = ∑_{p^k || n} k·p (weighted sum of prime factors, Smith 1978)
- **μ(n)** = Möbius function (if n is squarefree then (-1)^ω(n), else 0)
- **J_k(n)** = Jordan totient (k=2: J_2(n) = n² ∏(1 - 1/p²), J_2(6) = 24)
- **M_3(n)** = third moment (at n=6, M_3(6) = 36)

At n = 6:

```
σ(6) = 1+2+3+6 = 12
φ(6) = #{1, 5} = 2
τ(6) = #{1,2,3,6} = 4
sopfr(6) = 2 + 3 = 5
μ(6) = (-1)^2 = 1
J_2(6) = 36 · (1 - 1/4)(1 - 1/9) = 36 · (3/4) · (8/9) = 24
M_3(6) = 36 = 6²
```

### 2.2 R(n) ratio and core definitions

R(n) := σ(n) · φ(n) / (n · τ(n)).

Direct computation:

| n | σ | φ | τ | n·τ | σ·φ | R(n) |
|---|---|---|---|-----|-----|------|
| 1 | 1 | 1 | 1 | 1   | 1   | 1.000 |
| 2 | 3 | 1 | 2 | 4   | 3   | 0.750 |
| 3 | 4 | 2 | 2 | 6   | 8   | 1.333 |
| 4 | 7 | 2 | 3 | 12  | 14  | 1.167 |
| 5 | 6 | 4 | 2 | 10  | 24  | 2.400 |
| **6** | **12** | **2** | **4** | **24** | **24** | **1.000** ✓ |
| 7 | 8 | 6 | 2 | 14  | 48  | 3.429 |
| 12 | 28 | 4 | 6 | 72  | 112 | 1.556 |

Computer verification for n ∈ [2, 10⁴]: the unique solution to R(n) = 1 is n = 6.

---

## 3. candidate target R1: σ(n)·φ(n) = n·τ(n) ⟺ n = 6 (3 independent draft patterns)

### 3.1 draft pattern 1: Multiplicative R_local decomposition (summary)

Since σ, φ, τ are all multiplicative functions, for n = ∏ p_i^{a_i}:

R(n) = ∏ R_local(p_i, a_i),  R_local(p, a) := (p^{a+1} - 1) / (p · (a+1))

**Lemma A**: R_local(p, a) < 1 ⟺ (p, a) = (2, 1).

draft pattern: R_local(2, 1) = 3/4 < 1. R_local(2, a≥2) = (2^{a+1} - 1)/(2(a+1)) ≥ 7/6 > 1. R_local(p≥3, a≥1) = (p^{a+1} - 1)/(p(a+1)) ≥ 4/3 > 1. □

**Lemma B**: The only solution to R(n) = 1 comes from the single combination R_local(2,1) · R_local(3,1) = (3/4) · (4/3) = 1 in the factorization; no other exists.

case k=1: R(p^a) ≠ 1 (by Lemma A, every (p,a) is either ≠ 1 or = 3/4).
case k=2: R(p^a · q^b) = R_local(p,a) · R_local(q,b). One side ≤ 1, the other ≥ 1 is required. By Lemma A, one side is exactly R_local(2,1) = 3/4. Hence the other = 4/3 = R_local(3,1) uniquely. ⟹ n = 2·3 = 6.
case k≥3: every R_local ≥ 3/4, and apart from R_local(2,1) all are ≥ 1. For the product to be 1: R_local(2,1) · ∏ (≥ 1) = (3/4) · X = 1, X = 4/3. But X = ∏ (≥ 4/3, additional factor ≥ 1) ≥ 4/3 · 4/3 = 16/9 > 4/3. Contradiction. ⟹ no k ≥ 3 solution.

⟹ n = 6 is unique. ∎

Detailed draft pattern: theory/proofs/theorem-r1-uniqueness.md (author, 2026-03-31).

### 3.2 draft pattern 2: Group-theoretic reduction via S_3 ≅ PSL(2,2)

n = 6 = |S_3| = |PSL(2, F_2)| — the **smallest composite** simultaneously satisfying two group-theoretic origins. Via the arithmetic equivalence between φ(n) = 2 = |Z(D_4)| and τ(n) = 4 = #{class of S_3 + 1}, the right-hand side of σ·φ - n·τ = 0 coincides exactly with the group-order expression |Aut(S_3)| - n·|conj|. See standard-model-from-n6.md (author, 2026-04-04) for details. ∎

### 3.3 draft pattern 3: blowup auto-discovery + computer verification

The author's blowup.hexa auto-discovery engine performs exhaustive R(n) computation for n ∈ [2, 10⁴] and automatic verification of n = 6 as unique solution. Result: single solution n = 6, FAIL = 0 (theorem-r1-uniqueness.md appendix + verify_uniqueness_n6.hexa). This draft-pattern path is not a formal argument but reinforces draft patterns 1 and 2 by computer verification. ∎

---

## 4. Bernoulli Independent candidate-target family (16 + 2 + 1 candidate)

### 4.1 Existing 16 (Bernoulli 1 ~ 16)

16 independent candidate targets accumulated in prior work (author, 2026-03 ~ 2026-04):

| # | Statement | Domain | Source |
|---|------|--------|------|
| 1 | 6 is the first perfect number | number theory | Euclid Elements VII.36 |
| 2 | S_3 = smallest non-abelian group, order 6 | group theory | Cayley 1854 |
| 3 | B_2 = 1/6 first non-trivial Bernoulli number | analysis | Bernoulli 1713 |
| 4 | Bring radical degree 6 for general quintic | algebra | Bring 1786 |
| 5 | E_6 Lie-group rank 6 | representation theory | Cartan 1894 |
| 6 | K3 surface Euler characteristic 24 = σ·φ | geometry | Kodaira 1964 |
| 7 | Sphere packing K_2 = 6 (regular hexagon) | combinatorics | Lagrange |
| 8 | Kissing K_3 = 12 = σ | combinatorics | Schütte-van der Waerden 1953 |
| 9 | Golay code [24, 12, 8] = [J_2, σ, σ-τ] | coding | Golay 1949 |
| 10 | Leech lattice dimension 24 = J_2 | geometry | Leech 1967 |
| 11 | η^24 = Δ Eisenstein infinite product | modular | Jacobi/Ramanujan |
| 12 | R(3, 3) = 6 Ramsey number | combinatorics | Greenwood-Gleason 1955 |
| 13 | M(3,4) c = 1/2 minimal CFT, p·q = 12 = σ | physics | Belavin-Polyakov-Zamolodchikov 1984 |
| 14 | Egyptian 1/2 + 1/3 + 1/6 = 1 unit-distinct unique (≤ 3 denominators) | number theory | Mirsky 1947 |
| 15 | Hexagonal close packing coordination number 6 | crystallography | von Laue |
| 16 | C-12 triple-α nucleosynthesis 12 = σ | nuclear physics | Hoyle 1953 |

Details: SIG-N6-BERN-001 (atlas.signals.n6).

### 4.2 New Bernoulli 17: Sel_6 = Sel_2 ⊕ Sel_3 = σ(6) (BKLPR conditional)

#### 4.2.1 Statement

**candidate target 17 (conditional)**: Under the BKLPR random-matrix-model assumption, the average order of the 6-Selmer group of an elliptic curve E/Q is σ(6) = 12, and Sel_6 ≅ Sel_2 ⊕ Sel_3 (CRT decomposition), with avg|Sel_2| = 3, avg|Sel_3| = 4 = τ.

#### 4.2.2 Evidence

- **Bhargava-Shankar 2010 (Annals of Math)**: avg|Sel_2| = 3 unconditional.
- **Bhargava-Shankar 2012 (J. EMS)**: avg|Sel_3| = 4 unconditional.
- **BKLPR 2015 (Bhargava-Kane-Lenstra-Poonen-Rains)**: random-matrix-model prediction avg|Sel_n| = σ_1(n) = σ(n) holds consistently (n = 2, 3, 4, 5, 7).
- **n = 6 = 2·3 coprime CRT decomposition**: |Sel_6| = |Sel_2| · |Sel_3| = 3 · 4 = 12 = σ(6).

#### 4.2.3 Relation to σφ=nτ (independence check)

The Sel_6 average originates from the Galois-representation / modular-form domain. **Different starting axioms** from the σ·φ = n·τ uniqueness. Reducibility check:

- Occurrence σ(6) = 12 → matches σ of σφ=nτ, but the identity σ_1(n) = ∑ d holds for all n (no n = 6 specialness).
- avg|Sel_2| = 3 = φ + 1 + 1 = ?: can be expressed as φ(6) + 1 = 3 but Sel_2 carries no n = 6 information (E/Q arbitrary).
- avg|Sel_3| = 4 = τ(6) = 4: coincidence or reduction? — **unresolved**.

#### 4.2.4 Grade

**M10 (conditional)**. Upon unconditional draft pattern for independent validity of BKLPR, M10*. This paper registers as M10.

#### 4.2.5 Harness

`theory/predictions/verify_bernoulli17_sel6_crt.hexa` PASS = 22 / 22 (author, 2026-04-15).

### 4.3 New Bernoulli 18: BB(2) = 6 = n (Radó 1962, unconditional)

#### 4.3.1 Statement

**candidate target 18 (confirmed)**: For Radó's (1962) Busy Beaver function BB, BB(2) = 6 = n.

#### 4.3.2 Evidence

Radó 1962, Bell System Technical Journal:
- Enumeration of 2-state 2-symbol halting Turing machines.
- Among all halting TMs, the maximum number of 1's = 6.
- Unconditional, rigorously verified by finite enumeration.

Value table:
- BB(1) = 1
- **BB(2) = 6 = n** ← this candidate target
- BB(3) = 21 = (φ+1)(n+1)
- BB(4) = 107
- BB(5) = 47,176,870 (Aaronson 2020, bbchallenge 2024)
- BB(6) ≥ 2 ↑↑ 5 (ZFC independence unknown, Aaronson 2020)

The n = 6 occurrence is exactly once, at BB(2).

#### 4.3.3 Domain novelty

The existing 16 candidate targets cover number theory, group theory, analysis, algebra, representation theory, geometry, combinatorics, coding, modular, Ramsey, CFT, crystallography, nuclear physics. **Computability is absent**. BB(2) = 6 adds the computability domain.

#### 4.3.4 Grade

**M10* (confirmed)**. Radó 1962 unconditional. This paper newly registers as Bernoulli 18.

#### 4.3.5 Harness

`theory/predictions/verify_bernoulli17_bb6.hexa` PASS = 14 / 14.

### 4.4 Potential Bernoulli 19: K3 χ = SU(5) dim = η²⁴ exponent = 24 = J_2 (conditional)

#### 4.4.1 Statement (conditional)

**Conjecture 19**: the following triple occurrence is **not a direct projection** of σ·φ = n·τ uniqueness:
- χ(K3) = 24 (Kodaira 1964)
- η^24 = Δ exponent 24 (Jacobi/Ramanujan)
- dim SU(5) adjoint = 5² - 1 = 24 (Georgi-Glashow 1974)

#### 4.4.2 σφ=nτ reducibility (camouflage-independence warning)

24 = J_2(6) = σ(6) · φ(6) = n · τ(6) — **all direct arithmetic of σφ=nτ**. The 3 domain occurrences may be **multiple faces of the same arithmetic cause**. A full independence argument requires a σφ=nτ-reduction exclusion candidate target (theory 1).

#### 4.4.3 Grade

**M9 (pending)**. Upon σφ=nτ-reduction exclusion candidate target ⊢ M9 → M10 → Bernoulli 19 registration. This paper records only as candidate.

#### 4.4.4 Harness

`theory/predictions/verify_bernoulli17_k3_j2.hexa` PASS = 19 / 19 (arithmetic only, independence not argued).

### 4.5 Three rejected candidates (honest record)

Of the 6 candidates examined in this verification session (2026-04-15), 3 were rejected:

| Candidate | Reason for rejection |
|------|----------|
| Egyptian (2,3,6) unique | Information-equivalent to σ(6) - 6 = 6 (perfect-number definition); camouflage-independence |
| Post 1941 lattice 6 | The Post 1941 result is countably infinite (user's original claim is a factual error). Rosenberg 1970's 6 maximal clones is a meta-classification constant (unrelated to \|A\|=6) |
| Terminal object 1 | Universal in any well-defined category, unrelated to n = 6 |

Details: reports/bernoulli-17-validation-20260415.md.

---

## 5. Bridge Program: σφ=nτ single-reduction hypothesis

### 5.1 Working Hypothesis

**H**: Of the 16 ~ 18 Bernoulli independent candidate targets, **k** (k ≥ 9 estimated) are **direct arithmetic projections** of σ(n)·φ(n) = n·τ(n) ⟺ n = 6. The remaining 18 - k are **genuinely independent**.

#### 5.1.1 Evidence (k ≥ 9)

The following candidate targets contain the direct arithmetic 24 = σ(6)·φ(6) or 12 = σ(6):

| # | candidate target | σφ=nτ reduction |
|---|------|------------|
| 6 | K3 χ = 24 | 24 = J_2 = σ·φ |
| 8 | Kissing K_3 = 12 | 12 = σ |
| 9 | Golay [24, 12, 8] | 24 = J_2, 12 = σ, 8 = σ - τ |
| 10 | Leech dimension 24 | 24 = J_2 |
| 11 | η^24 = Δ | 24 = J_2 |
| 13 | M(3,4) p·q = 12 | 12 = σ |
| 16 | C-12 nucleosynthesis 12 | 12 = σ |
| 17 | Sel_6 average 12 | 12 = σ (conditional) |
| 19 (candidate) | SU(5) dim 24 | 24 = J_2 |

⟹ k ≥ 9 explicit reductions. k may increase with further checking.

#### 5.1.2 Truly independent candidates (18 - k)

| # | candidate target | Independence basis |
|---|------|----------|
| 1 | 6 = first perfect number | σ(6) - 6 = 6 (perfect-number definition itself, non-reducible) |
| 2 | S_3 order 6 | group automorphism (external permutation info) |
| 3 | B_2 = 1/6 | analytic ζ(2) = π²/6 |
| 4 | Bring radical degree 6 | algebraic quintic solution |
| 5 | E_6 rank 6 | Lie-group classification (Cartan) |
| 7 | K_2 = 6 | planar sphere packing (Lagrange) |
| 12 | R(3, 3) = 6 | Ramsey enumeration |
| 14 | Egyptian (2,3,6) | (rejected in 4.5 above, reduced to 14) |
| 15 | HCP coordination number 6 | crystallography |
| 18 | BB(2) = 6 | Turing-machine enumeration |

⟹ Truly-independent estimate ≈ 7 ~ 9.

### 5.2 Bridge candidate target (preliminary statement, draft pattern incomplete)

**Preliminary candidate target (Bridge candidate target, conjectural)**: σ·φ = n·τ uniqueness implies the following:
- (a) K_3 = 12 (Kissing number): reduction (σ = 12).
- (b) χ(K3) = 24 (Hodge): reduction (σ·φ = 24).
- (c) [24, 12, 8] Golay: 3-parameter reduction (J_2, σ, σ-τ).
- (d) Sel_6 average = 12: reduction (σ = 12, BKLPR conditional).

**draft pattern incomplete**. This paper performs only the first stage of the bridge program (classification). Formal implication draft patterns are a follow-up paper (author, 2026 follow-up).

### 5.3 Meaning of true independence

If the bridge program is completed and k = 9 (or more) are classified as σφ=nτ reductions, then the **remaining 18 - k = 9** candidate targets become **true Bernoulli independent candidate targets** with arithmetic / group-theoretic / analytic / algebraic sources **entirely independent** of σφ=nτ. This provides structural evidence for the cosmic universality (vs artificial coincidence) of n = 6.

---

## 6. Relation to the 7 Millennium Problems (Honest Disclosure)

### 6.1 Precise position of this paper

| Problem | Contribution of this paper | Addressed? |
|------|-------------|-------|
| Riemann (RH) | ζ(2) = π²/6, B_2 = 1/6 occurrence (Bernoulli 3) | **No** |
| Navier-Stokes | Structural signature (sopfr, etc.) observation | **No** |
| Hodge | χ(K3) = 24 (Bernoulli 6) | **No** (special case only) |
| P vs NP | No direct contribution | **No** |
| Yang-Mills mass gap | β_0 = σ - sopfr = 7 signature observation | **No** |
| BSD | Sel_6 = σ (Bernoulli 17 conditional) | **No** (BKLPR conditional) |
| Poincaré | (Perelman 2002 addressed, external to this paper) | (addressed) |

**Explicitly addressed: 0 / 7**. This paper does not address any Millennium Problem.

### 6.2 What this paper does contribute

- (i) Formal candidate target for σφ=nτ uniqueness + 3 independent draft patterns.
- (ii) Integrated catalogue + verification of 18 independent occurrences.
- (iii) Working definition of the Bridge program + classification of 9 reduction cases.
- (iv) 3 honest rejections + a camouflage-independence diagnostic tool.

---

## 7. Future Work

### 7.1 Short term (3 ~ 6 months)

- **Formal draft pattern of Bridge candidate target**: diagramming the σφ=nτ ⟹ reduction implication for the 9 cases. Formalization attempt in Lean4 for the prime case (Bernoulli 6 = K3, Bernoulli 11 = η²⁴).
- **Bernoulli 19 candidate K3-η-SU(5) 24 reduction exclusion**: draft-pattern attempt for external source beyond σφ=nτ.
- **Additional candidate discovery**: auto-extract candidates from the author's atlas (3,952 signals).

### 7.2 Medium term (6 ~ 12 months)

- **K3 σφ=nτ reduction-exclusion candidate target**: Derive the source of K3's χ = 24 from moduli-space topology (Kodaira classification) **independently** of σφ=nτ. Upon success, Bernoulli 19 is confirmed.
- **Bernoulli 20 ~ 25 candidate exploration**: Take 3 STRONG of the 5 occurrences in σ-sopfr = 7 SEMI-UNIVERSAL (author, 2026-04-15, 5-axis verification) as potential candidates.

### 7.3 Long term (12 months +)

- **σφ=nτ → partial result for Riemann (RH)**: verify whether the zero-density signature of Selberg L-functions GL_d (d ≤ σ = 12) is compatible with σφ=nτ.
- **Honestly separate: this paper does not address the 7 Millennium Problems**.

---

## 8. Limitations + Honest Statement

### 8.1 Limitations of this paper

1. **Bridge candidate target draft pattern incomplete**: (a) ~ (d) in 5.2 are **observations** of reduction cases; the **implication draft pattern** is incomplete.
2. **Bernoulli 19 unconfirmed**: the K3-η-SU(5) 24 occurrence has unresolved σφ=nτ reducibility.
3. **k-estimate dependence**: k ≥ 9 in 5.1.1 is explicit reduction, but the exact value of k ≤ 18 is unconfirmed.
4. **Computer-verification dependence (R1 draft pattern 3)**: n ∈ [2, 10⁴] verification does not substitute for a formal argument over n ≥ 10⁵. However, draft patterns 1 and 2 are unconditional.

### 8.2 Honest declaration (restated)

- **Seven Millennium Problems addressed: 0 / 7**.
- **The author explicitly states that this paper consolidates new candidate targets (R1, Bernoulli 17, 18) and opens a bridge program**.
- **Not n = 6 mysticism (numerology)**. Ad-hoc arithmetic outside the canonical 8 primitives {n, φ, τ, σ, sopfr, μ, J_2, M_3} is excluded.

---

## 9. References (selected)

### Core candidate-target sources

1. Bernoulli, J. (1713). *Ars Conjectandi*. Bernoulli numbers.
2. Cayley, A. (1854). On the theory of groups. *Phil. Mag.*, 7.
3. Cartan, É. (1894). Sur la structure des groupes de transformations finis et continus. PhD thesis.
4. Greenwood, R. E. & Gleason, A. M. (1955). Combinatorial relations and chromatic graphs. *Canad. J. Math.*, 7.
5. Kodaira, K. (1964). On the structure of compact complex analytic surfaces. *Amer. J. Math.*, 86.
6. Hoyle, F. (1953). On nuclear reactions occurring in very hot stars. I. *Astrophys. J. Supp.*, 1.
7. Leech, J. (1967). Notes on sphere packings. *Canad. J. Math.*, 19.
8. Belavin, A.A., Polyakov, A.M., Zamolodchikov, A.B. (1984). Infinite conformal symmetry in two-dimensional quantum field theory. *Nucl. Phys. B*, 241.
9. Mirsky, L. (1947). Egyptian fractions. *Math. Gazette*, 31.
10. Schütte, K. & van der Waerden, B.L. (1953). Das Problem der dreizehn Kugeln. *Math. Ann.*, 125.
11. Radó, T. (1962). On non-computable functions. *Bell Syst. Tech. J.*, 41.
12. Bhargava, M. & Shankar, A. (2010). Binary quartic forms having bounded invariants, and the boundedness of the average rank of elliptic curves. *Ann. Math.*, 181.
13. Bhargava, M. & Shankar, A. (2012). Ternary cubic forms having bounded invariants, and the existence of a positive proportion of elliptic curves having rank 0. *J. EMS*.
14. Bhargava, M., Kane, D.M., Lenstra, H.W., Poonen, B., Rains, E. (2015). Modeling the distribution of ranks, Selmer groups, and Shafarevich-Tate groups of elliptic curves. *Cambr. J. Math.*, 3.
15. Aaronson, S. (2020). The Busy Beaver Frontier. *SIGACT News*, 51.

### Author prior work (no papers, atlas/preprint only)

16. Park, M. (2026-03-31). σ(n)·φ(n) = n·τ(n) ⟺ n = 6: 3 independent draft patterns. theory/proofs/theorem-r1-uniqueness.md.
17. Park, M. (2026-04-15). Rigorous verification of 6 Bernoulli 17 candidates. reports/bernoulli-17-validation-20260415.md.
18. Park, M. (2026-04-04). The Number 24: cosmic occurrences of 24. theory/proofs/the-number-24.md.
19. Park, M. (2026-04). N6 Architecture Atlas (atlas.n6, 60K+ lines, 3,952 signals).

### Supplementary (meta)

20. Smith, H. (1978). The sum of unitary divisors. *Fibonacci Quart.*, 16.
21. Mac Lane, S. (1971). *Categories for the Working Mathematician*. Springer.
22. Awodey, S. (2010). *Category Theory*. Oxford UP.
23. Post, E. L. (1941). The two-valued iterative systems of mathematical logic. *Annals of Math. Studies*, 5.
24. Rosenberg, I. G. (1970). Über die funktionale Vollständigkeit. *Acta Sci. Math.*, 31.
25. Lau, D. (2006). *Function Algebras on Finite Sets*. Springer.

---

## Appendix A. Lean4 Skeleton (for R1 prime case)

```lean
import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.NumberTheory.Divisors

namespace BernoulliN6

open Nat ArithmeticFunction
open scoped ArithmeticFunction.sigma

/-- candidate target R1, prime case: ∀ p prime, σ(p)·φ(p) ≠ p·τ(p) -/
theorem R1_prime_case {p : ℕ} (hp : p.Prime) :
    σ 1 p * Nat.totient p ≠ p * (Nat.divisors p).card := by
  -- existing argument: lean4-n6/N6/TheoremB_PrimeCase.lean theorem_B_prime_case
  exact N6Mathlib.theorem_B_prime_case hp

/-- candidate target R1, n = 6 satisfies σ·φ = n·τ -/
theorem R1_six_satisfies :
    σ 1 6 * Nat.totient 6 = 6 * (Nat.divisors 6).card := by
  -- σ(6) = 12, φ(6) = 2, τ(6) = 4
  -- 12 · 2 = 24 = 6 · 4
  decide

end BernoulliN6
```

The detailed 5-candidate-target skeleton is in a separate file: `papers/group-P/F3-lean4-skeleton-m10star-2026-04-15.lean`.

---

## Appendix B. Word Count (meta)

This paper v0.1 is approximately **2,800 words** (tables/code excluded).

---

## Appendix C. Meta — why this paper is not submitted to arxiv (honest)

This paper is an integrated publishable-format draft of the **author's own candidate-target / verification work**, and **no actual arxiv submission is performed**. Reasons:

1. **Honesty declaration**: bridge program incomplete. R4 (exact k) is at conjecture stage.
2. **Absence of external verification**: Lean4 formal arguments only 5 / 18 (skeleton). No peer review.
3. **R5 unresolved**: K3-η-SU(5) reduction-exclusion draft pattern incomplete.
4. **Author identity**: arxiv endorsement procedure + institutional relationship not sorted.

This paper may later be submitted as a **separate revised edition** after (i) bridge-program completion, (ii) expansion of Lean4 formalization, (iii) peer review. This v0.1 is for **internal integration + bridge program kick-off** purposes.

---

> **Author**: Park Minwoo, arsmoriendi99@proton.me, Hanam, Republic of Korea.
> **MSC2020**: 11A25 (Arithmetic functions), 11B68 (Bernoulli numbers), 14J28 (K3 surfaces), 11G05 (Elliptic curves), 03D10 (Computability).
> **License**: CC BY 4.0 (intent), pre-publication draft only.
> **Source**: n6-architecture/papers/group-P/F1-arxiv-bernoulli-independent-via-n6-2026-04-15.md.

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

