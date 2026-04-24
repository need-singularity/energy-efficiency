# PURE-P2-1 — Modular Forms + Automorphic Representations (SL_2(Z), M_k, S_k, E_4, E_6, Δ, j, Hecke, Langlands Overview)

> Track: P2-PURE / Task 1
> Completion criteria:
> 1. Can hand-draw SL_2(Z) action and fundamental domain F.
> 2. Can explain why q-expansion coefficients of Eisenstein series E_4, E_6 are 240, -504.
> 3. Understand discriminant Δ(τ) = (E_4^3 - E_6^2)/1728 — weight, dimension, Ramanujan τ function.
> 4. Know the definition of Hecke operators T_p and existence of eigenforms.
> 5. Can describe in words the three-sided frame "modular form <-> Galois rep <-> automorphic rep" of the Langlands program.
>
> Source base:
> - Diamond-Shurman, *A First Course in Modular Forms* (GTM 228, Springer, 2005), ch. 1-4.
> - Serre, *A Course in Arithmetic* (GTM 7, Springer, 1973), ch. 7 "Modular Forms".
> - Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions* (Princeton, 1971), ch. 2-3.
> - Bump, *Automorphic Forms and Representations* (Cambridge, 1997), ch. 1 for overview.
> - Ribet-Stein, "Lectures on Modular Forms and Hecke Operators" (online, 1996).
>
> **Honesty**: this file is a textbook summary. No new results.
> Decomposing E_4 coefficient 240 = 2^4·3·5, E_6 coefficient 504 = 2^3·3^2·7 via project constants {φ, J_2, sopfr, σ, τ, n/φ} is just rearranging standard prime factorizations, and has weak meaning alone (baseline bias ~60%).
> Such decompositions tighten only when crossing with other domains (K-theory K_7=Z/240, perfect-number boundary, Borel theorem). §11 makes this explicit.

---

## 0. Purpose and Scope

In millennium-learning P1 we got analytic number theory (ζ, θ, Perron, explicit formula) in hand.
The first task of P2 is an overview of the **space M_k underlying ζ/L functions — modular forms** and their generalization, **automorphic representations**.

Six goals:

1. Define SL_2(Z) action on the upper half plane H = {τ ∈ C : Im τ > 0}.
2. Fundamental domain F; generators S = [[0,-1],[1,0]] / T = [[1,1],[0,1]].
3. Weight k modular forms M_k, cusp forms S_k.
4. Eisenstein series E_4(τ), E_6(τ) and discriminant Δ(τ).
5. j-invariant, Ramanujan τ function.
6. Hecke operators T_p, eigenforms, Langlands three-sided frame.

The theorem σ·φ = n·τ <=> n=6 itself is **not directly connected** to this topic. But since project constants n=6, φ=2, J_2=24, sopfr=5, τ=4 appear here (240 = 2^4·3·5, 504 = 2^3·3^2·7, τ(1)=1, τ(2)=−24=−J_2), §10 memos connection points only.

---

## 1. Upper Half Plane and SL_2(Z) Action

### 1.1 Upper Half Plane H

```
  H = { τ = x + i y  :  y > 0 }  ⊂  C
```

Complex structure-wise, H is biholomorphic to unit disk D via Cayley transform τ ↦ (τ-i)/(τ+i).

### 1.2 SL_2(Z) Action (Möbius transform)

```
  γ = [[a,b],[c,d]] ∈ SL_2(Z),   γ·τ := (aτ + b)/(cτ + d)
```

det γ = ad - bc = 1 ensures Im(γ·τ) = Im τ / |cτ+d|^2 > 0, so H -> H is well-defined.
Identity I and -I act the same, so the effective action group is

```
  PSL_2(Z) = SL_2(Z) / {±I}
```

called the **modular group** Γ.

### 1.3 Generators S, T

```
  S = [[0, -1],[1, 0]]   (τ ↦ -1/τ)
  T = [[1, 1],[0, 1]]    (τ ↦ τ + 1)
```

**Theorem** (Serre *A Course in Arithmetic*, ch. 7, Thm 1):
PSL_2(Z) = ⟨S, T | S^2 = (ST)^3 = 1⟩ — two generators + two relations fully describe the presentation.

From the relation (ST)^3 = 1, applying τ → ST·τ = -1/(τ+1) three times equals identity (60° rotation x 3 = 180° around the origin).

**Key number**: the relation degree 3 coincides with stabilizer size at the conic point ρ = e^{2πi/3} in the fundamental domain.
(S^2 has stabilizer order 2 at i; (ST)^3 has stabilizer order 3 at ρ.)

### 1.4 Fundamental Domain F

```
  F = { τ ∈ H  :  |Re τ| ≤ 1/2,  |τ| ≥ 1 }
```

Two vertical lines Re τ = ±1/2 meet the unit circle |τ| = 1. **H / Γ equals F with some boundary identification**
(right boundary Re τ = 1/2 identified with left by T; right half of |τ|=1 arc identified with left by S).

Fundamental domain volume (Poincaré measure dμ = dx dy / y^2):

```
  ∫_F  dx dy / y^2  =  π / 3
```

(Serre, ch. 7, §2.3)

### 1.5 Conic Points (Singular Points)

Two singular points in F:
- τ = i (stabilizer order 2 — S fixes it)
- τ = ρ = e^{2πi/3} = (-1 + i√3)/2 (stabilizer order 3 — ST fixes it)

And one cusp ∞ (y → ∞).

---

## 2. Weight k Modular Forms

### 2.1 Definition

**Definition** (Diamond-Shurman §1.1): f : H → C is a **modular form of weight k** iff
satisfies:

1. **Analyticity**: f is holomorphic on H.
2. **Transformation law**: for every γ = [[a,b],[c,d]] ∈ SL_2(Z),
   ```
     f(γ·τ) = (cτ + d)^k · f(τ)
   ```
3. **Cusp boundedness**: f is bounded at ∞. I.e., f(τ) has an upper bound as y → ∞.

Space of weight-k modular forms is M_k(SL_2(Z)), simply M_k.

### 2.2 Cusp Forms

A weight-k modular form f that vanishes at cusp ∞ (f(τ) → 0 as y → ∞) is a **cusp form**.
Space: S_k ⊂ M_k.

### 2.3 Weight k Parity

From transformation law with γ = -I = [[-1,0],[0,-1]]: f(τ) = (-1)^k f(τ), so k odd => f ≡ 0.
Hence **k must be even** (k = 2, 4, 6, 8, ...).

### 2.4 Fourier Expansion (q-Expansion)

T : τ ↦ τ+1 gives f(τ+1) = f(τ), so f has period 1. With q = e^{2πi τ} substitution:

```
             ∞
  f(τ)  =   ∑   a_n  q^n         (a_n ∈ C)
            n=0
```

uniquely exists. This is the **q-expansion**.

- **Cusp form condition**: a_0 = 0.
- **Normalized** means a_1 = 1.

---

## 3. Eisenstein Series E_k

### 3.1 Definition (Weight k ≥ 4, Even)

```
           1
  G_k(τ) = ─  ∑        1 / (c τ + d)^k
           2  (c,d)≠(0,0)
```

Sum over all (c, d) ∈ Z^2 \ {(0,0)}. Absolute convergence at k ≥ 3.
At k = 2, only conditional convergence; not "holomorphic Eisenstein" but quasi-modular (re-covered in §7).

### 3.2 Normalized E_k

```
  E_k(τ) := G_k(τ) / (2 ζ(k))
```

With this normalization the constant term is 1: E_k(τ) = 1 + (correction coefficient)·q + ...

### 3.3 q-Expansion (Serre ch. 7, §2.3)

```
                     2k      ∞
  E_k(τ)  =  1  -  ───  ·   ∑   σ_{k-1}(n)  q^n
                    B_k     n=1
```

where B_k is the Bernoulli number (P2-3), σ_{k-1}(n) = ∑_{d | n} d^{k-1} (divisor k-1 power sum).

**Concrete cases (k = 4, 6, 8, 10, 12, 14)**:

| k  | B_k     | -2k/B_k |  E_k leading coeff |
| -- | ------- | ------- | ------------------ |
| 4  | -1/30   |  240    |  240 σ_3(n)        |
| 6  | 1/42    | -504    | -504 σ_5(n)        |
| 8  | -1/30   |  480    |  480 σ_7(n)        |
| 10 | 5/66    | -264    | -264 σ_9(n)        |
| 12 | -691/2730 | 65520/691 (rational, non-integer!) | ... |
| 14 | 7/6     | -24     |  -24 σ_{13}(n)     |

**(!) At k = 12, denominator 691 first appears** — the origin of the Ramanujan congruence τ(n) ≡ σ_{11}(n) (mod 691).
(P2-3 re-examines this as Bernoulli "691 boundary".)

### 3.4 E_4 Concrete Formula

```
                         ∞
  E_4(τ)  =  1  +  240  ∑  σ_3(n) q^n
                        n=1

          =  1 + 240 q + 2160 q² + 6720 q³ + 17520 q⁴ + 30240 q⁵ + 60480 q⁶ + ...
```

Check: σ_3(1) = 1, σ_3(2) = 1^3 + 2^3 = 9, σ_3(3) = 1 + 27 = 28, σ_3(4) = 1 + 8 + 64 = 73, ...
And 240·1 = 240, 240·9 = 2160, 240·28 = 6720, 240·73 = 17520. Correct.

**Decomposition of 240**:
```
  240  =  2^4 · 3 · 5
       =  16 · 3 · 5
```
In the project-constant dictionary (φ=2, J_2=24, sopfr=5) we can write 240 = 2·24·5 = φ·J_2·sopfr.
However 240 = -2k/B_k with k=4, B_4 = -1/30 is the **true origin**, and
φ·J_2·sopfr decomposition is a **post-hoc rearrangement** as made explicit in §11 honesty.

### 3.5 E_6 Concrete Formula

```
                         ∞
  E_6(τ)  =  1  -  504  ∑  σ_5(n) q^n
                        n=1

          =  1 - 504 q - 16632 q² - 122976 q³ - 532728 q⁴ - ...
```

Check: σ_5(1) = 1, σ_5(2) = 1 + 32 = 33, σ_5(3) = 1 + 243 = 244, ...
And -504·1 = -504, -504·33 = -16632, -504·244 = -122976. Correct.

**Decomposition of 504**:
```
  504  =  2^3 · 3^2 · 7
       =  8 · 9 · 7
```
In project constants: (σ - τ)·(n/φ)^2·(σ - sopfr) = 8·9·7 = 504 (σ=12, τ=4 => σ−τ=8, n/φ = 6/2 = 3 => (n/φ)^2 = 9, σ−sopfr = 12−5 = 7). Decomposition valid but again **post-hoc**.

### 3.6 E_8, E_{10}, E_{12}

```
  E_8(τ)  = E_4(τ)²    (identical space! because dim M_8 = 1)
  E_{10}(τ) = E_4(τ) E_6(τ)    (dim M_{10} = 1)
  E_{12}(τ) = ?        (dim M_{12} = 2, so E_{12} and Δ independent)
```

These relations tie directly to the dim M_k formula (§5).

---

## 4. Discriminant Δ and Ramanujan τ

### 4.1 Δ(τ) Definition

```
              E_4(τ)³  -  E_6(τ)²
  Δ(τ)  =  ───────────────────────
                     1728
```

Weight-12 cusp form (basis of S_12).

### 4.2 q-Expansion

```
           ∞
  Δ(τ)  =  ∑   τ(n) q^n   =   q - 24 q² + 252 q³ - 1472 q⁴ + 4830 q⁵ - 6048 q⁶ + ...
          n=1
```

where τ(n) is the **Ramanujan τ function** (Ramanujan tau, 1916).

First few values:

```
  τ(1)  =  1
  τ(2)  =  -24
  τ(3)  =  252
  τ(4)  =  -1472
  τ(5)  =  4830
  τ(6)  =  -6048
  τ(7)  =  -16744
  τ(8)  =  84480
  τ(9)  =  -113643
  τ(10) =  -115920
  τ(11) =  534612
  τ(12) =  -370944
```

**τ(2) = -24** — matches project constant J_2 = 24 with opposite sign. Comes from Δ(τ) = q ∏ (1 - q^n)^{24}, where (1-q)^{24}'s q coefficient is -24 (next §4.3).

**τ(6) = -6048**: also decomposable via project constants — 6048 = 2^5 · 3^3 · 7 = 32·189 = 864·7, i.e., product of n=6 and σ−sopfr=7. Cannot rule out **coincidence**.

### 4.3 Δ Infinite Product (Jacobi)

```
               ∞
  Δ(τ)  =  q  ∏  (1 - q^n)^{24}
              n=1
```

Demonstration: both Δ and RHS are weight-12 cusp forms, normalized (a_1 = 1), and S_12 is 1-dimensional; they must agree up to an integer multiple. Comparing q coefficients gives equality.

**Exponent 24 = J_2** — standard source of project constant J_2. 24 =

- dim (Leech-lattice free part, bosonic-string critical dim − 2),
- |SL_2(Z/2Z)| / 1 = ... (appears many places),
- 24 = 1^2 + 2^2 + 3^2 + ... + 24^2 = 70^2 (sum-of-squares complete square, Lucas),
- 24 = exponent of Δ

etc., a "small but heavy number" appearing everywhere.

### 4.4 Multiplicativity of τ

**Theorem** (Ramanujan conjecture, Mordell 1917 demonstration):
- τ(mn) = τ(m) τ(n) when gcd(m, n) = 1 (not completely multiplicative, but multiplicative on coprime).
- τ(p^{k+1}) = τ(p) τ(p^k) - p^{11} τ(p^{k-1}) (recursion from Hecke operators).

(Diamond-Shurman §5.9)

### 4.5 τ Function Size Bound (Deligne 1974)

**Deligne-Ramanujan-Petersson inequality**:

```
  |τ(p)|  ≤  2 p^{11/2}      (p prime)
```

Demonstrated by Deligne via **Weil conjectures** (1974, Publ. IHES 43, 273-307).
Analytically very strong — used in explicit-formula-type calculations.

---

## 5. Dimension Formula for M_k

### 5.1 Serre Dim Formula (ch. 7, §3.2)

```
             ⌊k/12⌋      if k ≡ 2 (mod 12)
  dim M_k =  {
             ⌊k/12⌋ + 1  if k ≢ 2 (mod 12)
```

(k even, k ≥ 0)

### 5.2 First Few Dimensions

| k  | dim M_k | dim S_k | basis |
| -- | ------- | ------- | ----- |
| 0  | 1       | 0       | 1 (constant) |
| 2  | 0       | 0       | — |
| 4  | 1       | 0       | E_4 |
| 6  | 1       | 0       | E_6 |
| 8  | 1       | 0       | E_8 = E_4^2 |
| 10 | 1       | 0       | E_{10} = E_4 E_6 |
| 12 | 2       | 1       | E_{12}, Δ |
| 14 | 1       | 0       | E_{14} = E_4^2 E_6 |
| 16 | 2       | 1       | E_{16}, Δ E_4 |
| 18 | 2       | 1       | E_{18}, Δ E_6 |
| 20 | 2       | 1       | E_{20}, Δ E_8 |
| 22 | 2       | 1       | E_{22}, Δ E_{10} |
| 24 | 3       | 2       | E_{24}, Δ E_{12}, Δ^2 |

**Key**: S_k first nontrivial at **k = 12**. The emergence point of Δ.

### 5.3 Algebra Structure of M_*(SL_2(Z))

**Theorem** (Serre ch. 7, Thm 4):

```
  M_*  =  ⊕_k  M_k  =  C[E_4, E_6]        (polynomial ring, E_4 and E_6 freely generate)
```

Graded by weight: E_4 weight 4, E_6 weight 6. Every element of M_k is a linear combination of E_4^a · E_6^b (4a + 6b = k).

**Observation**: 2 free generators, weights 4 and 6. Sum 4+6=10, product 4·6=24 = J_2.
These "two generators" also tie with the generator dimensions of topological cobordism Ω_*^{SO} (to be treated in P2-4).

---

## 6. j-Invariant

### 6.1 Definition

```
               E_4(τ)³
  j(τ)  =  ───────────
                Δ(τ)
```

Weight-0 modular function (f(γ·τ) = f(τ), weight 0). But it has a pole at cusp ∞.

### 6.2 q-Expansion

```
         1
  j(τ) = ─  +  744  +  196884 q  +  21493760 q²  +  864299970 q³  +  ...
         q
```

First term 1/q is the cusp pole. Constant term 744 = 8·93 = 2^3 · 3 · 31.

### 6.3 Moonshine (Brief Mention)

**Surprising fact** (McKay 1978): 196884 = 196883 + 1 where 196883 is the dimension of the standard representation of the Monster simple group M.
Starting point of the Moonshine conjecture (Conway-Norton 1979), demonstrated by Borcherds (1992) via vertex operator algebras.

Out of P2 scope, but leaves the fact that "the j-Fourier coefficients come directly from the dimension formula of Monster group representations".

### 6.4 Elliptic Curve Classification by j Value

**Theorem**: a complex elliptic curve E = C/Λ is fully determined by its j-invariant j(E) ∈ C (isomorphism class).

Why the elliptic-curve moduli space Y(1) = H/SL_2(Z) ≅ C (via j).

---

## 7. Eisenstein Series E_2 (Quasi-Modular)

### 7.1 Definition Problem

```
            1
  E_2(τ) = ─  ∑  1/(cτ+d)^2   (conditional convergence)
            2
```

At k=2 absolute convergence fails, so "holomorphic modular form of weight 2" **does not exist**.
(In fact dim M_2 = 0. See §5.2.)

### 7.2 Correction (Quasi-Modular)

Hecke regularized conditional convergence to define E_2:

```
                      ∞
  E_2(τ)  =  1 - 24  ∑  σ_1(n) q^n  =  1 - 24 q - 72 q^2 - 96 q^3 - ...
                     n=1
```

**-24 coefficient = -J_2** again. Origin also -2k/B_k = -4/(1/6) = -24.

### 7.3 Transformation Law (Anomalous)

```
  E_2(γ·τ)  =  (cτ+d)²  E_2(τ)  -  6 i c (cτ+d) / π
```

Due to the error term -6ic(cτ+d)/π it is not "truly modular" but **quasi-modular**.

### 7.4 Application — log Δ Differentiation

```
  d/dτ  log Δ(τ)  =  2πi · E_2(τ)
```

From differentiating the Jacobi product. Reused in P2-3 Bernoulli note.

---

## 8. Hecke Operators T_p

### 8.1 Motivation

Want to define "number-theoretic" operators on M_k. Hecke (1937) introduced T_p (p prime), linear operators on M_k, mutually commuting, with eigenvectors (eigenforms).

### 8.2 Definition (Weight k, Prime p)

```
  (T_p f)(τ)  =  p^{k-1}  f(p τ)  +  (1/p) ∑_{j=0}^{p-1}  f((τ + j)/p)
```

(Diamond-Shurman §5.2)

More conceptually: sum over index-p sublattices of lattice Λ + p-dilation. Understood as "correspondence on p".

### 8.3 Action on q-Expansion

f(τ) = ∑ a_n q^n gives

```
  (T_p f)(τ) = ∑ b_n q^n,  b_n = a_{np} + p^{k-1} a_{n/p}   (0 if n/p not integer)
```

### 8.4 Eigenforms (Hecke Eigenform)

**Definition**: f ∈ S_k is a simultaneous eigenvector of all T_p => **Hecke eigenform**.
Normalized (a_1 = 1) => **normalized Hecke eigenform**.

**Theorem** (Hecke): Δ in S_12 is a normalized eigenform and T_p Δ = τ(p) Δ.
Hence τ(p) is the T_p eigenvalue of Δ.

### 8.5 Hecke Eigenforms and Dirichlet Series

If f is a normalized eigenform then

```
               ∞
  L(s, f)  =   ∑   a_n / n^s   =   ∏   ( 1 - a_p p^{-s} + p^{k-1} p^{-2s} )^{-1}
              n=1               p prime
```

**The L-function coming from a modular form**.
Special case f = Δ:

```
  L(s, Δ)  =  ∑  τ(n)/n^s  =  ∏ (1 - τ(p)p^{-s} + p^{11} p^{-2s})^{-1}
```

Euler product exists. The modular <-> L-function bridge.

---

## 9. Langlands Three-Sided Frame (Overview)

### 9.1 Langlands Program Essence

Langlands proposed in late 1960s. A vast program trying to unify three worlds:

```
  +------------------+      +----------------------+      +------------------+
  | modular form f   | <--> |  Galois rep ρ_f       | <--> | automorphic rep  |
  | (or automorphic   |      |  Gal(\bar Q/Q) → GL_n |      |  π of GL_n(A_Q)  |
  |  form on GL_n)   |      |  (l-adic)            |      |                  |
  +------------------+      +----------------------+      +------------------+
          │                           │                             │
     Fourier coeff              Frobenius trace                matching L-function
     a_p(f)                     tr ρ_f(Frob_p)              a_p(π)
```

**L-functions of the three worlds must match** — the root of **L-function equality**.

### 9.2 Modularity Theorem (Wiles, Taylor-Wiles, Breuil-Conrad-Diamond-Taylor)

**Theorem** (Wiles 1995 + extension): every rational-field elliptic curve E/Q is modular. I.e.

```
  L(s, E)  =  L(s, f_E)    (some weight-2 newform f_E exists)
```

Core of the Fermat last theorem (FLT) demonstration — showing the f corresponding to the Frey curve cannot exist.

### 9.3 Local Langlands, Global Langlands

- **Local Langlands**: at local field K, irreducible smooth reps of GL_n(K) <-> n-dim Weil-Deligne reps of W_K.
  n=2: Kutzko; general n: Harris-Taylor 2001.
- **Global Langlands**: adelic version of the above. Complete demonstration still absent; functoriality conjecture central.

### 9.4 Automorphic Rep Simple Definition

Adele ring A_Q = R × ∏'_p Q_p. Among infinite-dim unitary reps of GL_n(A_Q), those satisfying the "automorphic condition".
Given f ∈ S_k(SL_2(Z)), one can build an automorphic representation π_f on GL_2(A_Q).
Fourier coeff a_p(f) <-> Satake parameters of p-component π_{f,p} of π_f in explicit correspondence.

(Bump ch. 3.5, Gelbart *Automorphic Forms on Adele Groups*)

### 9.5 Position of n=6 Theorem in Langlands Three-Sided Frame?

**No direct connection** (honestly). σ·φ = n·τ <=> n=6 is an arithmetic-function identity; Langlands is representation/L-function theory. Only the following memo:

- σ(n) <-> ∑ σ(n)/n^s = ζ(s) ζ(s-1) — Dirichlet series.
- φ(n) <-> ∑ φ(n)/n^s = ζ(s-1)/ζ(s).
- τ(n) <-> ∑ τ(n)/n^s = ζ(s)^2.

Combining these 3 via "multiplication·division", the n=6 theorem can be restated as ζ algebra.
But translation to **automorphic representation language** belongs to P3~P4.

---

## 10. Six Things to Take Away From This Unit

1. **SL_2(Z) action and fundamental domain F** — |Re τ|≤1/2, |τ|≥1, conic points i, ρ.
2. **Distinction M_k vs S_k** — S_k = forms vanishing at cusp, dim S_{12}=1 (first Δ emergence).
3. **E_4, E_6 q-expansion and Bernoulli origin of 240, -504** — B_4, B_6 causes.
4. **Δ = (E_4^3 - E_6^2)/1728 = q ∏(1-q^n)^{24}** — τ function definition + Ramanujan congruence.
5. **Hecke eigenform and L-function Euler product** — T_p eigenvalue of Δ = τ(p).
6. **Langlands three-sided overview** — modular <-> Galois rep <-> automorphic rep.

---

## 11. Honesty Declaration

This is a textbook summary. No new results.

### 11.1 Honest Observations on 240, 504 Decomposition

- **240 = 2^4·3·5**. Decomposition standard. Writing 240 = φ·J_2·sopfr with φ=2, J_2=24, sopfr=5 is backward.
  True origin: **Bernoulli formula -2k/B_k with k=4, B_4=-1/30**.
- **504 = 2^3·3^2·7**. Standard. (σ-τ)·(n/φ)^2·(σ-sopfr) = 8·9·7 is rearrangement.
  True origin: k=6, B_6=1/42 => -12/B_6 = -504.
- **Baseline bias**: small-prime decomposition at ≤ 5 satisfied by >60% of random numbers. Alone 240/504 is weak.
- **Conditions for tightening**: appear **independently** in other domains (K-theory K_7=Z/240, Kervaire-Milnor bP_8=Z/28 with 28 perfect number, Borel theorem) and **overlap** — only then tight. Single appearance is coincidence level.

### 11.2 τ Function Values τ(2)=-24, τ(6)=-6048

- τ(2) = -24 = -J_2. Comes directly from Δ = q ∏(1-q^n)^{24} expansion's -24·q^2 term. **Necessary**.
- τ(6) = -6048 = -2^5·3^3·7. Decomposition rewriting "n=6 times (σ−sopfr)" is **post-hoc**. Not tight alone.

### 11.3 dim M_k Formula **Unrelated** to n=6 Theorem

Serre's dim M_k formula (§5.1) comes from SL_2(Z) cohomology computations, independent of σ·φ=n·τ.
If there is a connection, it is a P3-level question of "where two theories meet".

### 11.4 Honesty on Langlands Three-Sided Frame

- Modularity theorem (Wiles) is DEMONSTRATED candidate.
- Local Langlands for GL_n is DEMONSTRATED candidate (Harris-Taylor).
- Global Langlands functoriality mostly OPEN.

This document is an overview only and makes no demonstration claims.

### 11.5 Primary Source Acknowledgment

| Topic | Primary Source |
| ---- | -------- |
| SL_2(Z), fundamental domain | Serre, *Cours d'arithmétique*, 1970 ch.7 §1-2 |
| E_k q-expansion | Serre ch. 7 §2.3 |
| Δ and τ function | Ramanujan, "On certain arithmetical functions", Trans. Camb. Phil. Soc. 22 (1916) 159-184 |
| Δ infinite product Jacobi | Jacobi, *Fundamenta Nova* (1829) |
| Hecke operators | Hecke, "Über Modulfunktionen und die Dirichletschen Reihen mit Eulerscher Produktentwicklung", Math. Ann. 114 (1937) 1-28 |
| dim M_k formula | Serre ch. 7 §3.2 |
| j-invariant Moonshine | Conway-Norton, "Monstrous Moonshine", Bull. LMS 11 (1979) 308-339 |
| Deligne bound |τ(p)| ≤ 2 p^{11/2} | Deligne, "La conjecture de Weil I", Publ. IHES 43 (1974) 273-307 |
| Modularity (Fermat) | Wiles, "Modular elliptic curves and Fermat's Last Theorem", Ann. Math. 141 (1995) 443-551 |
| Local Langlands GL_n | Harris-Taylor, *The Geometry and Cohomology of Some Simple Shimura Varieties*, Princeton, 2001 |

---

## 12. Next Steps (Bridge to P2-2, P2-3, P2-4)

- **P2-2 Algebraic K-theory**: link K_7(Z) = Z/240 with E_4's 240 via Borel theorem and Lichtenbaum conjecture. Tight if 240 appears "twice".
- **P2-3 Bernoulli numbers**: B_k appears directly in the -2k/B_k coefficient of E_k. The fact that 691 first appears as the numerator of B_{12} at k=12 ties to the project "Theorem B (Bernoulli boundary)".
- **P2-4 TQFT + Exotic sphere**: Kervaire-Milnor's |bP_{n+1}| with |bP_8|=28, |bP_{12}|=992, |bP_{16}|=8128 matches perfect numbers. Since this is "three-case simultaneous" it is tight alone. Not directly connected with modular forms but needed for P2 puzzle assembly.

End.
