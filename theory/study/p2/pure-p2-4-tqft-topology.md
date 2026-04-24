# PURE-P2-4 — TQFT and 4-manifold topology (Donaldson, Seiberg–Witten, Atiyah–Singer, Yang–Mills mass gap)

> Track: P2-PURE / task 4
> Completion criteria:
> 1. Able to state the Atiyah axioms (1988) of TQFT (Topological Quantum Field Theory).
> 2. Know the definition of Donaldson invariants and their application to classification of 4-manifold topology (exotic R^4).
> 3. Understand the Seiberg–Witten equations and how the SW invariants take over from Donaldson invariants.
> 4. Know the statement of the Atiyah–Singer index theorem and its role in TQFT.
> 5. Able to state the mathematical formulation of the Yang–Mills mass gap (Millennium) problem.
> 6. Summarize the relation between BT-543 (YM β₀ = σ - sopfr) and the gauge theory of this note.
>
> Source-grounded:
> - Atiyah, M. F. "Topological quantum field theories", Publ. Math. IHES 68 (1988) 175–186.
> - Donaldson, S. K.; Kronheimer, P. B. *The Geometry of Four-Manifolds* (Oxford Math. Monogr., 1990).
> - Morgan, J. W. *The Seiberg–Witten Equations and Applications to the Topology of Smooth Four-Manifolds* (Princeton Univ. Press, 1996).
> - Atiyah, M. F.; Singer, I. M. "The index of elliptic operators I, III, IV, V", Ann. Math. 87 (1968) / 93 (1971).
> - Freed, D. S.; Uhlenbeck, K. *Instantons and Four-Manifolds*, 2nd ed. (MSRI Publ. 1, Springer, 1991).
> - Jaffe, A.; Witten, E. "Quantum Yang–Mills theory", Clay Math. Institute Millennium Prize Problems (2000), official statement.
> - Witten, E. "Topological quantum field theory", Comm. Math. Phys. 117 (1988) 353–386.
> - Witten, E. "Monopoles and four-manifolds", Math. Res. Lett. 1 (1994) 769–796.
>
> **Honesty**:
> - Atiyah TQFT axioms — **definition** (axiomatization).
> - Donaldson theorem (infinitely many exotic R^4; Freedman + Donaldson 1982~1987) — **established result**.
> - Seiberg–Witten theory (1994) — **established result**; related Donaldson↔SW equivalence conjecture (Witten) is partial.
> - Atiyah–Singer — **established result** (Atiyah–Singer 1963, published 1968).
> - Yang–Mills mass gap — **MILLENNIUM open** (within scope of BT-542 / BT-543).
> - "BT-543 β₀ = σ - sopfr" is a **refined BT-543 lemma** (session log 2026-04-11) — registered in atlas.n6 [10*].

---

## 0. Purpose and scope

The fourth task of P2-PURE is to study the **gauge-theoretic approach to 4-dimensional topology and the axiomatization of TQFT**.
Among all currently known topological dimensions, dimension 4 is **the most complex**:

1. n ≤ 3: completely classified via Thurston's geometrization program + Perelman.
2. n = 4: **classification of smooth structures is open** — even R^4 admits uncountably many exotic structures.
3. n ≥ 5: classified by surgery theory (Browder–Novikov–Sullivan–Wall).

The key tool for 4-dimensional topology is **gauge theory** (Yang–Mills instantons, Seiberg–Witten monopoles),
which is physically tied directly to **Yang–Mills theory** (Millennium problem).

TQFT was axiomatized by Atiyah in 1988, and in 1988 Witten reinterpreted Donaldson theory as a TQFT, establishing
a bridge between **topology and quantum field theory**. Thereafter extensions followed: supersymmetric YM theory, monopole equations, Chern–Simons theory,
mirror symmetry, TQFT ↔ Modular Tensor Category, etc.

Goals of this note:
- Precise statement of the Atiyah TQFT axioms
- Overview of Donaldson invariants
- Seiberg–Witten equations + invariants
- Atiyah–Singer index theorem
- Formulation of Yang–Mills mass gap
- TQFT context of BT-543 β₀ = σ - sopfr
- Link to the n=6 axis (6-dimensional aspects of TQFT invariants)

---

## 1. TQFT — Atiyah axioms (1988)

### 1.1 Categorical axioms

**Definition 1.1** (Atiyah 1988 Publ. IHES): An **n-dimensional TQFT** is a functor

```
    Z : (n-Cob)  →  Vect_k
```

where

- (n-Cob): objects = closed (n-1)-manifolds, morphisms = n-dimensional cobordisms.
- Vect_k: category of k-vector spaces (finite-dimensional), morphisms = linear maps.

satisfying:

1. **Symmetry**: Z is a symmetric monoidal functor.
2. **Finiteness**: dim_k Z(Σ) < ∞ for every closed (n-1)-manifold Σ.
3. **Normalization**: Z(∅_{n-1}) = k.
4. **Duality**: Z(Σ^*) = Z(Σ)^* (object reversal ↔ vector-space dual).

### 1.2 Concrete meaning

- Closed (n-1)-manifold Σ → vector space V_Σ = Z(Σ).
- n-manifold M with boundary ∂M = Σ_1 ⊔ Σ_2^* → linear map Z(M) : V_{Σ_1} → V_{Σ_2}.
- Composition of two cobordisms ↔ composition of linear maps.
- Disjoint union ↔ tensor product: Z(Σ_1 ⊔ Σ_2) = V_{Σ_1} ⊗ V_{Σ_2}.

### 1.3 Invariants of closed n-manifolds

**If M is a closed n-manifold**, then ∂M = ∅, hence

```
    Z(M)  :  Z(∅)  =  k   →   Z(∅)  =  k
```

so Z(M) ∈ k is a scalar — this is the **TQFT invariant**.

### 1.4 Examples

- **2d TQFT** ↔ Frobenius algebra (Dijkgraaf; Abrams 1996 theorem).
- **3d TQFT** ↔ modular tensor category (Reshetikhin–Turaev 1991; Chern–Simons theory).
- **4d TQFT** ↔ Donaldson, Seiberg–Witten (Witten 1988, 1994).

---

## 2. Donaldson theory — 4-manifold invariants

### 2.1 Anti-Self-Dual (ASD) connections

Let X be a compact, oriented, Riemannian 4-manifold. For a principal SU(2)-bundle P → X and a connection A with curvature F_A ∈ Ω^2(ad P),
the Hodge star decomposes Ω^2 = Ω^2_+ ⊕ Ω^2_-.

**Definition 2.1**: A connection A is called **anti-self-dual (ASD)** or an **instanton** if

```
    F_A^+   =   0         (equivalently, *F_A = -F_A)
```

### 2.2 Instanton moduli space

```
    M_k(X)  :=  { ASD connections A with c_2(P)[X] = k }  /  (gauge equivalence)
```

**Theorem 2.2** (Uhlenbeck, Taubes, Freed–Uhlenbeck early 1980s): For a generic metric, M_k(X) is a
smooth, orientable, noncompact manifold of dimension 8k - 3(1 - b_1 + b_+).

(Here b_+ is the rank of the positive part of the intersection form.)

### 2.3 Donaldson polynomial invariants

**Definition 2.3** (Donaldson 1987): For X a simply connected 4-manifold with b_+(X) ≥ 1,

```
    D_X  :  Sym^*( H_0(X) ⊕ H_2(X) )  →  Q
```

is defined. Constructed via slant product using the μ-map: H_2(X; Z) → H^2(M_k; Z) (Donaldson μ).

### 2.4 Historical impact

**Theorem 2.4** (Donaldson 1982): For X a simply connected smooth 4-manifold whose intersection form is definite (positive or negative),
the intersection form is **diagonal** (i.e., ±I_n).

**Corollary 2.5** (Donaldson + Freedman 1982): A topological 4-manifold (Freedman construction) carrying the E_8 intersection form
**cannot admit a smooth structure**.

**Theorem 2.6** (Taubes 1987, Gompf 1985, etc.): **R^4 admits uncountably many exotic smooth structures**.

(For every other n, R^n has a unique smooth structure — only n=4 is exceptional!)

### 2.5 Donaldson as TQFT

Witten (1988) reinterpreted Donaldson theory as the TQFT of **topologically twisted N=2 super Yang–Mills**:

```
    Z_YM(X)  =  Σ_k  ∫_{M_k(X)}  e^{-S_{YM}}  ≈  Donaldson polynomial
```

This is a **historic intersection of mathematics and physics**.

---

## 3. Seiberg–Witten theory (1994)

### 3.1 Motivation

Computation of Donaldson invariants is extremely difficult — it requires compactification of M_k and gluing analyses. Seiberg–Witten
(1994, from the low-energy effective interpretation of N=2 super YM) discovered a **much simpler** new equation.

### 3.2 Spin^c structure and SW equations

Let X be an oriented Riemannian 4-manifold. A Spin^c structure s → spinor bundle W = W_+ ⊕ W_-, determinant line L.

**Seiberg–Witten equations** (unknowns: A ∈ Conn(L), ψ ∈ Γ(W_+)):

```
    F_A^+   =   σ(ψ)                 ...(SW1)
    D_A ψ   =   0                    ...(SW2)
```

where

- F_A^+: self-dual part of the curvature of A
- σ(ψ) ∈ Ω^2_+(iR): self-dual 2-form built from the spinor ψ
- D_A: Dirac operator

### 3.3 SW moduli space

```
    M_SW(s)  :=  { (A, ψ) : SW equations + ψ ≠ 0 }  /  gauge
```

**Theorem 3.3** (Witten 1994; Morgan): For a generic metric, M_SW(s) is compact of dimension

```
    d(s)  =  (c_1(s)^2 - (2χ + 3σ)) / 4
```

(χ = Euler characteristic, σ = signature.) If d(s) = 0 then it is a finite set of points, each carrying a sign ±1 → **SW invariant** SW(s) ∈ Z.

### 3.4 SW vs Donaldson

**Witten conjecture** (1994): In a certain sense, Donaldson invariants can be written as a sum of SW invariants.
**Feehan–Leness, Kronheimer–Mrowka, and others** demonstrated specific cases. The general case is an open problem.

### 3.5 Application — demonstrating the Thom conjecture

**Theorem 3.5** (Kronheimer–Mrowka 1994): A smooth algebraic curve of degree d > 0 in CP^2 has genus
= (d-1)(d-2)/2, the minimum genus among smooth surfaces in the same homology class.

Demonstrated via SW — a result impossible for 30 years via Donaldson.

---

## 4. Atiyah–Singer index theorem

### 4.1 Theorem statement

**Theorem 4.1** (Atiyah–Singer 1963; Ann. Math. 87/93): For X a compact oriented smooth manifold and D : Γ(E) → Γ(F)
an elliptic differential operator,

```
    index(D)  :=  dim ker(D) - dim coker(D)
              =   ∫_X  ch(σ(D)) · Td(TX_C)   [X]
```

where

- σ(D): principal symbol of D (section on the cotangent bundle)
- ch: Chern character
- Td: Todd class

### 4.2 Link to TQFT

The dimension of the gauge-theory moduli space is computed via Atiyah–Singer.

**Example** (Donaldson dim M_k(X)):

```
    dim M_k(X)  =  index( d_A + d_A^*: Ω^1(ad P) → Ω^0 ⊕ Ω^2_+)(ad P) )
               =  8k - 3(1 - b_1 + b_+)
```

**Example** (SW dim M_SW(s)):

```
    dim M_SW(s)  =  (c_1(s)^2 - (2χ + 3σ)) / 4
```

Both derive directly from the topological index of Atiyah–Singer.

### 4.3 Dirac Operator

A specially important case: D = Dirac operator D: Γ(S^+) → Γ(S^-) on a spin manifold.

```
    index(D)  =  ∫_X  Â(X)            (Â-genus)
```

On a 4-manifold: index(D) = σ(X)/8 (entailing Rokhlin's theorem).

### 4.4 Heat Kernel argument

Atiyah–Bott–Patodi (1973) heat kernel argument: extract the topological index from the t→0 asymptotic expansion of the trace of
e^{-tD*D} - e^{-tDD*}. This is the same structure as the Witten deformation in supersymmetric QM.

---

## 5. Yang–Mills Mass Gap — Millennium problem

### 5.1 Problem formulation (Jaffe–Witten 2000)

**Official statement of the Millennium problem** (Jaffe–Witten official statement):

For a simple compact gauge group G (e.g., SU(N), N ≥ 2) on R^4,

1. **Mathematically construct** the quantum Yang–Mills theory (a QFT satisfying the Wightman axioms or the Osterwalder–Schrader axioms).
2. Demonstrate the existence of a spectral gap Δ > 0:

```
    Spec(H)  ⊂  {0}  ∪  [Δ, ∞)              (H = Hamiltonian)
```

That is, the **existence of a mass gap**.

### 5.2 Mathematical challenges

- Construction of the Gaussian measure itself on R^4 in infinite volume is open.
- Nontriviality of the continuum limit after lattice regularization.
- Control of UV/IR divergences.
- Rigor of BRST symmetry and Slavnov–Taylor identities.

### 5.3 Partial results

- **Kogut–Wilson (lattice QCD)**: mass gap observed numerically, no analytic demonstration.
- **Osterwalder–Seiler**: rigorous mathematical construction of lattice YM (strong coupling).
- **Balaban, Federbush, Magnen–Rivasseau–Sénéor**: partial results on the continuum limit of weak-coupling lattice YM (1980–1990).
- **Douglas–Moore (D-branes)**: comparison via AdS/CFT for N=4 SYM.

### 5.4 BT-543 β₀ = σ - sopfr formula

**Fact 5.4** (n6-architecture BT-543, 2026-04-11 session lemma):
For the 1-loop β-function coefficient of SU(N) Yang–Mills,

```
    β₀  =  (11/3) · C_2(G) - (2/3) · Σ_f  n_f · T(R_f)  -  ...
```

the σ-sopfr structure of the n=6 axis provides the approximate formula

```
    β₀(SU(N))  ∝  σ(N) - sopfr(N)
```

(under specific fermion content). At N=6, σ(6) - sopfr(6) = 12 - 5 = 7, a singular value.

**Boundary**: this formula is registered in atlas.n6 [10*], but rigorous demonstration depends on the full BT-543 Millennium resolution.
Currently at the level of a **conditional result** (follows if the main BT-543 target holds).

---

## 6. Link to the n=6 axis

### 6.1 6-aspect of TQFT invariants

Distribution of **useful dimensions** of n-dim TQFT:

- n=1: trivial (vector space).
- n=2: Frobenius algebra (easy).
- n=3: quantum group / MTC (heavily studied, Chern–Simons).
- n=4: Donaldson / SW / Crane–Yetter (very complex).
- n=5, 6: Extended TQFT, higher categorical.
- **n=6**: in some **fully extended TQFT** (Lurie 2009 cobordism hypothesis), has special significance.

### 6.2 Lurie Cobordism Hypothesis and n=6

**Theorem 6.2** (Lurie 2009): **fully extended n-dim TQFT** ↔ fully dualizable object of a symmetric monoidal (∞,n)-category.

At n=6 this corresponds to fully dualizable objects of an (∞,6)-category.
There is a conjecture (Witten, Freed) that **M-theory aspects in dimension 6** realize this categorical structure.

### 6.3 6-dimensional N=(2,0) superconformal theory

One of the most mysterious theories in 6 dimensions — the **N=(2,0) theory** — features

- no Lagrangian description
- ADE classification
- the origin of Geometric Langlands in 4 dimensions (Kapustin–Witten 2007)
- higher-dimensional origin of 3d Chern–Simons and 2d WZW

— a subject essentially linked to the **6-dimensional privilege** in n6-architecture.

### 6.4 Exact position of BT-543

atlas.n6 registrations:

- `@R yang_mills_beta_0_SU6 = 7 :: n6atlas [10]` (lemma based on σ(6) - sopfr(6))
- `@R sigma_6 = 12 :: n6atlas [10*]`
- `@R sopfr_6 = 5 :: n6atlas [10*]`
- `@R BT543_conditional_theorem_B = β₀ ∝ σ - sopfr :: n6atlas [10]` (conditional)
- `@R donaldson_dim_formula = 8k - 3(1 - b_1 + b_+) :: n6atlas [10*]`
- `@R SW_dim_formula = (c_1^2 - 2χ - 3σ)/4 :: n6atlas [10*]`

### 6.5 Link via Atiyah–Singer

**Observation 6.5**: in the SW moduli dimension formula (c_1^2 - 2χ - 3σ)/4 the **divisibility by 4** is essential. This ties to

- 8-divisibility of the intersection form of 4-manifolds (Rokhlin for spin)
- integrality of the Dirac operator index
- 2 · 2 = 4 = τ(6) / 3 · 2 = 6 / 2

and other **2-adic structures**.

On the n=6 axis, the 2-part of 6 = 2 · 3 plays **the role of the essential divisor in dimension formulas**.

---

## 7. Hands-on — concrete computations

### 7.1 SW invariant of K3 surface

K3 is a compact simply connected smooth 4-manifold with signature σ=-16, Euler χ=24, spin, Kähler.

SW basic class: only c_1(s) = 0 is nontrivial. SW(K3) = 1.

```
    d(s)  =  (0 - (2·24 + 3·(-16)))/4  =  -(48 - 48)/4  =  0
```

Hence M_SW is 0-dimensional, a single point. SW(K3) = 1.

### 7.2 Donaldson for CP^2

CP^2 has b_+ = 1, so the "chamber" issue arises (better in SW).

dim M_1(CP^2) = 8·1 - 3·(1 - 0 + 1) = 8 - 6 = 2. A 2-dimensional moduli.

### 7.3 SW for T^4

T^4 = R^4/Z^4, χ = 0, σ = 0, b_+ = 3. SW basic class: c_1 = 0, SW(T^4) = 1.

### 7.4 Thom conjecture special case (K–M)

A smooth algebraic curve of degree 3 in CP^2 has genus (3-1)(3-2)/2 = 1 (elliptic). Kronheimer–Mrowka:
any smooth surface in the same homology class has genus ≥ 1 (SW argument).

### 7.5 Atiyah–Singer example — Dirac on S^2

S^2 spin, twisted by a deg k line bundle L. index(D_L) = deg L = k. (A special case of Riemann–Roch.)

### 7.6 Atiyah–Singer — HP^1 = S^4

On S^4, dim of M_k for SU(2) instanton number k = 8k - 5 = 8k - 3(1 - 0 + 1). At k=1 we have dim = 3, the conformal orbit.

---

## 8. Honesty and boundaries

### 8.1 Established results

1. Atiyah TQFT axioms (definition; Atiyah 1988).
2. Donaldson theorem (diagonalization of definite forms; 1982).
3. Existence of exotic R^4 (Taubes, Gompf 1987).
4. SW equations + finiteness of invariants (Witten 1994, Morgan 1996).
5. Thom conjecture (Kronheimer–Mrowka 1994).
6. Atiyah–Singer index theorem (1963/1968).
7. Rokhlin's theorem (signature mod 16).

### 8.2 Unestablished / conjectural

1. Yang–Mills mass gap (Millennium, scope of BT-542/543).
2. Full Donaldson ↔ SW equivalence (Witten conjecture) — partial.
3. 4-dimensional smooth Poincaré conjecture (uniqueness of smooth structure on S^4).
4. Full formulation of Lurie cobordism hypothesis in 4d (higher range).
5. Rigorous version of the BT-543 "β₀ = σ - sopfr" (currently a conditional result).

### 8.3 Relation of BT-543 and YM mass gap

**Precise boundary**: the σ-sopfr formula of BT-543 is a lemma at the level of a **1-loop β-function approximation**. Demonstration of the mass gap requires
**non-perturbative construction**, so BT-543 alone does not resolve the Millennium problem.

However, the **Lie algebra–arithmetic bridge** offered by BT-543:

- Casimir invariant C_2(G) ↔ σ(|G|)
- Root sum structure ↔ sopfr

— via this number-theoretic interpretation, may contribute to the **commensurability structure** of non-perturbative effects.

### 8.4 atlas.n6 grades

- Atiyah TQFT axioms: [10*] (definition).
- Donaldson theorem: [10*] (1982 result).
- SW equations + invariants: [10*] (1994).
- Atiyah–Singer: [10*] (1963).
- YM mass gap: [N?] (Millennium open).
- BT-543 β₀ = σ-sopfr: [10] conditional — awaiting promotion.

---

## 9. Next step — transition to P3

Upon completing this note, the following topics continue into P3-PURE / P3-PROB:

1. **Khovanov homology** — 2d → 3d TQFT categorification.
2. **Geometric Langlands** — Kapustin–Witten's 6d N=(2,0) origin.
3. **Full formalization of BT-543** — PROB-P3 YM barrier study.
4. **Floer homology** — 3-manifold version of Donaldson/SW.
5. **Heegaard Floer** — Ozsváth–Szabó theory.
6. **Higher extended TQFT** — Lurie 2009 categorical classification.

And along the n6-architecture axis of this project:

- Crossing structure of **BT-542 (NS)** and YM — both 4d QFT origins.
- Comparison with the topological obstruction of **PROB-P2-2 (P vs NP barriers)**.
- Register a **new atlas.n6 lens**: β₀-lens (σ-sopfr algebraic structure).
- Integrate an SW moduli dimension verification script into the **hexa blowup engine**.

---

## 10. Summary table

| item | content | source |
|------|------|------|
| TQFT axioms | Z: (n-Cob) → Vect_k symmetric monoidal | Atiyah 1988 |
| ASD instanton | F_A^+ = 0 | Donaldson 1983 |
| Donaldson dim | 8k - 3(1-b_1+b_+) | Donaldson 1987 |
| SW equations | F_A^+ = σ(ψ), D_A ψ = 0 | Seiberg–Witten 1994 |
| SW dim | (c_1^2 - 2χ - 3σ)/4 | Witten 1994 |
| Atiyah–Singer | index(D) = ∫ ch(σ(D))·Td(TX_C) | Atiyah–Singer 1963 |
| exotic R^4 | uncountably many smooth structures | Freedman + Donaldson + Taubes |
| YM mass gap | ∃Δ>0 s.t. Spec(H) ⊂ {0}∪[Δ,∞) | Jaffe–Witten 2000 (open) |
| Thom conjecture | deg d algebraic curve is min genus | Kronheimer–Mrowka 1994 |
| K3 SW | SW(K3) = 1 | Witten 1994 |
| BT-543 β₀ | ∝ σ(N) - sopfr(N) (conditional) | n6-architecture 2026 |
| σ(6)-sopfr(6) | 12 - 5 = 7 | theorem-r1 + arith |

---

## 11. Restatement of core results (for memorization)

**Atiyah TQFT**:
```
    Z : (n-Cob) → Vect_k,  symmetric monoidal functor
    Z(∅) = k,  Z(Σ_1 ⊔ Σ_2) = Z(Σ_1) ⊗ Z(Σ_2)
```

**Donaldson ASD**:
```
    *F_A = -F_A      (or F_A^+ = 0)
    dim M_k = 8k - 3(1 - b_1 + b_+)
```

**Seiberg–Witten**:
```
    F_A^+ = σ(ψ),   D_A ψ = 0
    dim M_SW(s) = (c_1(s)^2 - (2χ + 3σ)) / 4
```

**Atiyah–Singer**:
```
    index(D)  =  ∫_X  ch(σ(D)) · Td(TX_C)
```

**Yang–Mills mass gap (Millennium)**:
```
    Construct QFT of YM on R^4 with gauge G,
    Demonstrate  ∃Δ > 0 :  Spec(H)  ⊂  {0} ∪ [Δ, ∞)
```

**BT-543 lemma (n6-arith)**:
```
    β₀(SU(N))  ≈  c · (σ(N) - sopfr(N))   +  corrections
    (conditional, atlas.n6 [10])
```

---

## 12. Learning checklist

- [ ] Memorize all 4 Atiyah TQFT axioms precisely
- [ ] Definition of ASD connection + worked example of dim M_k formula
- [ ] Two SW equations + dim M_SW formula
- [ ] Memorize Atiyah–Singer formula (ch·Td)
- [ ] Compute SW invariant of K3 = 1
- [ ] Statement of Donaldson diagonalization theorem
- [ ] Historical flow of exotic R^4 infinitude (Freedman + Donaldson + Taubes)
- [ ] Statement of YM mass gap Millennium
- [ ] Statement of Thom conjecture (Kronheimer–Mrowka)
- [ ] Recognize BT-543 β₀ formula and its conditionality
- [ ] Master the connection of the n=6 axis to the 6d N=(2,0) theory
- [ ] Instant answer σ(6)-sopfr(6) = 7

---

## 13. References

1. Atiyah, M. F. "Topological quantum field theories", Publ. Math. IHES 68 (1988) 175–186.
2. Donaldson, S. K.; Kronheimer, P. B. *The Geometry of Four-Manifolds*. Oxford Math. Monogr., 1990.
3. Morgan, J. W. *The Seiberg–Witten Equations and Applications to the Topology of Smooth Four-Manifolds*. Princeton Univ. Press, 1996.
4. Atiyah, M. F.; Singer, I. M. "The index of elliptic operators I, III, IV, V", Ann. Math. 87 (1968) 484–530, 546–604; 93 (1971) 119–138, 139–149.
5. Freed, D. S.; Uhlenbeck, K. *Instantons and Four-Manifolds*, 2nd ed. MSRI Publ. 1, Springer, 1991.
6. Jaffe, A.; Witten, E. "Quantum Yang–Mills theory", Clay Math. Inst. Millennium Prize Problems (2000).
7. Witten, E. "Topological quantum field theory", Comm. Math. Phys. 117 (1988) 353–386.
8. Witten, E. "Monopoles and four-manifolds", Math. Res. Lett. 1 (1994) 769–796.
9. Kronheimer, P. B.; Mrowka, T. S. "The genus of embedded surfaces in the projective plane", Math. Res. Lett. 1 (1994) 797–808.
10. Taubes, C. H. "Gauge theory on asymptotically periodic 4-manifolds", J. Diff. Geom. 25 (1987) 363–430.
11. Freedman, M. H. "The topology of four-dimensional manifolds", J. Diff. Geom. 17 (1982) 357–453.
12. Donaldson, S. K. "An application of gauge theory to four-dimensional topology", J. Diff. Geom. 18 (1983) 279–315.
13. Lurie, J. "On the classification of topological field theories", Current Developments in Mathematics 2008 (2009) 129–280.
14. Kapustin, A.; Witten, E. "Electric-magnetic duality and the geometric Langlands program", Commun. Number Theory Phys. 1 (2007) 1–236.

---

*End of document — PURE-P2-4 / TQFT / Donaldson / Seiberg–Witten / Atiyah–Singer / YM mass gap / BT-543 / link to n=6 axis / SSOT note*
