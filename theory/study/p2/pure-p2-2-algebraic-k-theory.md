# PURE-P2-2 — Algebraic K-theory (K_0, K_1, K_2, Quillen higher, K_n(Z), Borel, Lichtenbaum)

> Track: P2-PURE / task 2
> Completion criteria:
> 1. Able to explain the classical definitions of K_0(R), K_1(R), K_2(R) (Grothendieck, Bass–Milnor, Milnor).
> 2. Understand why Quillen's +-construction / Q-construction makes K_n behave as a generalized cohomology theory.
> 3. Memorize the table of Borel (1974) K_n(Z) computation results.
> 4. Understand the Lichtenbaum conjecture (K_n(O_F) ↔ étale cohomology) at the level of statement.
> 5. See at the statement level the Borel–Quillen link ζ_F(1-2k) ↔ K_{4k-1}(O_F) / torsion.
>
> Source-grounded:
> - Weibel, *The K-book: An Introduction to Algebraic K-Theory* (AMS GSM 145, 2013), ch. I~VI (especially ch. IV "Definitions of higher K-theory", ch. VI "Computing K_*(Z)").
> - Rosenberg, *Algebraic K-Theory and Its Applications* (GTM 147, Springer, 1994), ch. 1~5.
> - Milnor, *Introduction to Algebraic K-Theory* (Ann. Math. Studies 72, Princeton, 1971) — the original K_2 book.
> - Quillen, "Higher algebraic K-theory: I" in *Algebraic K-Theory I*, LNM 341 (Springer, 1973) 85–147.
> - Borel, "Stable real cohomology of arithmetic groups", Ann. Sci. ENS 7 (1974) 235–272.
> - Lichtenbaum, "Values of zeta-functions, étale cohomology, and algebraic K-theory" in *Algebraic K-Theory II*, LNM 342 (Springer, 1973) 489–501.
>
> **Honesty**:
> - The K_n(Z) table (K_7=Z/240, K_{11}=Z/1008, etc.) is an **established result**. Detailed derivation in Weibel ch. VI §8.
> - The Borel theorem (rank K_{2n-1}(O_F)) is an **established result** (1974).
> - The Lichtenbaum conjecture is a **partial result** (Bloch–Kato conjecture + Voevodsky 2003 + Rost 2008 for certain cases).
> - "240 = E_4 coefficient = K_7 = agreement" is a **post-hoc observation**, and the deeper "why are they the same" goes all the way down to Stickelberger / Adams / J-homomorphism,
>   a deep reason and not a simple rearrangement of project constants (see §10 honesty).

---

## 0. Purpose and scope

The second task of the P2 stage is to get the basics of **algebraic K-theory** under one's hands.
K-theory began in the 1950s when Grothendieck introduced K_0 to demonstrate a generalized Riemann–Roch.
Thereafter

1. Bass–Milnor–Serre introduced K_1 (early 1960s)
2. Milnor defined K_2 (1971)
3. Quillen defined **higher K_n** in two ways in 1972–73 (+-construction, Q-construction)
4. Borel determined the rank of higher K_n of the ring of integers O_F of a number field in 1974
5. Lichtenbaum conjectured the relation between ζ values and K-groups (1973)

— a five-stage development.

Goals of this note:
- Definitions of K_0, K_1, K_2
- Overview of Quillen higher K_n
- Concrete **table of K_n(Z) values** (Borel + Weibel)
- **Project-constant decomposition** of the K_n(Z) values at n=3, 7, 11, namely Z/48, Z/240, Z/1008
- Statements of the Borel theorem and the Lichtenbaum conjecture

---

## 1. K_0 — Grothendieck

### 1.1 Definition (ring R)

**Definition** (Weibel ch. II §1): When R is an (associative unital) ring,

```
  K_0(R)  :=  ( monoid of isomorphism classes of f.g. projective R-modules )^{group completion}
```

The monoid operation is direct sum ⊕; group completion is the Grothendieck construction (form m+n = k+m).

### 1.2 Examples

- **K_0(F) = Z** (F a field) — for finite-dimensional vector spaces one only needs to look at dimension.
- **K_0(Z) = Z** — f.g. projective over Z = free, given by rank.
- **K_0(Z[G]) = Z ⊕ C(G)** (G a finite group, Wall finiteness obstruction).
- **K_0(C(X)) = K^0(X)_{top}** — topological K-theory of vector bundles on compact X (Swan's theorem).

### 1.3 Original motivation (Grothendieck)

Riemann–Roch theorem:

```
  χ(X, F) = deg F + rk F (1 - g)
```

To generalize (relativize) this, one needs a "Grothendieck group of vector bundles". Defining the class of F ∈ Coh(X) in K_0(X)_{coherent}
makes χ a natural group homomorphism K_0(X) → Z.

### 1.4 Morita invariance

R and M_n(R) have the same K_0 (Morita equivalence). The same is true of higher K_n.

---

## 2. K_1 — Bass, Milnor, Serre

### 2.1 Definition

**Definition** (Weibel ch. III §1):

```
  K_1(R)  :=  GL(R)_{ab}  =  GL(R) / [GL(R), GL(R)]
```

Here GL(R) = ∪_n GL_n(R) (infinite general linear, with limit included), and [,] is the commutator subgroup.

By Whitehead's theorem, [GL(R), GL(R)] = E(R) (elementary matrices subgroup, without requiring R commutative).

```
  K_1(R)  =  GL(R) / E(R)
```

### 2.2 For commutative rings R

If R is commutative, then det : GL_n(R) → R* descends to K_1(R) → R*, and

```
  K_1(R)  ≅  R*  ⊕  SK_1(R)
```

with SK_1 = ker det. In many cases SK_1 = 0.

### 2.3 Examples

- **K_1(F) = F*** (F a field) — nonzero elements.
- **K_1(Z) = Z/2** — {±1} (units).
- **K_1(O_F)** (F a number field, O_F ring of integers) **= O_F*** — by Dirichlet's unit theorem, a f.g. abelian group (rank r_1 + r_2 - 1 + torsion = roots of unity).
- **K_1(Z/n) = (Z/n)*** — unit group.

### 2.4 Whitehead group Wh(G)

K_1(Z[G]) / ±G is called the Whitehead group. Used in the s-cobordism theorem (Milnor 1962) and in the consolidation of h-cobordism.

---

## 3. K_2 — Milnor (1971)

### 3.1 Definition

**Definition** (Milnor, *Introduction to Algebraic K-Theory*, 1971):

```
  K_2(R)  :=  H_2(E(R), Z)  =  π_2(BE(R)^+)
```

Here E(R) = [GL(R), GL(R)] and H_2 is group homology. Equivalently, as the center of the Steinberg group St(R):

```
  K_2(R)  =  ker( St(R) → E(R) )
         =  center(St(R))    (surjection)
```

### 3.2 Milnor symbol {a, b}

For R commutative and a, b ∈ R*, the Milnor symbol {a, b} ∈ K_2(R) satisfies the following relations:

- **Steinberg**: {a, 1-a} = 0 (when both a and 1-a are units)
- **Bilinear**: {a₁a₂, b} = {a₁, b} + {a₂, b}, and similarly for b
- **Skew-symmetry**: {a, b} = -{b, a}

### 3.3 Examples

- **K_2(F) = K^M_2(F)** (F a field, Matsumoto's theorem). Generated by Milnor symbols.
- **K_2(Z) = Z/2** — generated solely by the Steinberg symbol {-1,-1}.
- **K_2(F_q) = 0** (F_q a finite field, all elements of the form 1-a). This is demonstrated by Quillen (1972).

### 3.4 Merkurjev–Suslin theorem (1982)

**Theorem**: F a field, n invertible, μ_n ⊂ F, then

```
  K_2(F) / n  ≅  Br(F)[n]
```

The case n=2 is from 1982; the general n case is part of the Bloch–Kato conjecture (completed by Voevodsky 2003).

This theorem shows that K_2 is not merely an abelian group but a **deep object connected to the Brauer group / Galois cohomology**.

---

## 4. Quillen higher K_n — +-construction

### 4.1 Motivation

Unifying K_0, K_1, K_2 so that "K_n for all n ≥ 0" could be defined was unclear until the early 1970s.
Quillen (1972) unified it via **topology**.

### 4.2 +-construction (Quillen 1969, 1972)

BGL(R) = classifying space of GL(R). **This has K_1(R) as π_1, but K_n(R) for n≥2 does not come out directly.**

Quillen introduced: since E(R) is a perfect subgroup (commutator), the "+-construction":

```
  BGL(R)^+ := BGL(R) with 2-cells attached to kill E(R)
```

As a result, π_1(BGL(R)^+) = K_1(R), π_2(BGL(R)^+) = K_2(R), ...

**Definition** (Quillen 1972):

```
  K_n(R)  :=  π_n( BGL(R)^+ )       (n ≥ 1)
  K_0(R)  :=  (defined as with Grothendieck)
```

### 4.3 Topological character of BGL(R)^+

This space is a genuine CW complex, and computing its homotopy groups yields the higher part of algebraic K-theory.
Quillen computed exactly the homotopy type of BGL(F_q)^+ (1972, "On the cohomology and K-theory of the general linear groups over a finite field", Ann. Math. 96, 552–586):

```
  K_n(F_q)  =  0               (n even, n ≥ 2)
              = Z/(q^m - 1)    (n = 2m - 1 odd)
```

### 4.4 Q-construction (Quillen 1973)

The +-construction is only for rings. For a more general setting (exact categories), Quillen introduced the Q-construction.

```
  K_n(P)  :=  π_{n+1} (BQ P)    (P an exact category, QP the Q-construction)
```

Applied to P = P(R) (f.g. projective R-modules) this coincides with the +-construction.
Applied to P = Coh(X) and others, it yields various forms of "big K-theory".

### 4.5 Karoubi–Villamayor and other definitions

There were several different definitions (Karoubi–Villamayor (1971), Gersten (1971), Wagoner (1972), etc.),
and Quillen unified them. The modern formulation is the **Waldhausen S-construction** (1985) which generalizes to simplicial categories.

---

## 5. Concrete values of K_n(Z) — Borel + Weibel

### 5.1 Borel theorem (1974)

**Theorem** (Borel, Ann. ENS 7 (1974) 235–272): For F a number field and O_F its ring of integers,

```
             { 0                      n=0
             { r_1 + r_2 - 1          n=1   (Dirichlet units)
             { 0                      n=2
             { r_2                    n=3   (Borel regulator)
  rank K_n(O_F) =
             { 0                      n=4
             { r_1 + r_2              n=5
             { 0                      n=6
             { r_2                    n=7
             { 0                      n=8
             { r_1 + r_2              n=9
             ...  (period 4)
```

Summary: rank = 0 at even n (>0). For odd n, with period 4, r_2 (n ≡ 3) / r_1+r_2 (n ≡ 1) alternate.

In particular, **for F = Q we have r_1 = 1, r_2 = 0**, so:
- rank K_n(Z) = 1 if n ≡ 1 (mod 4), n ≥ 5
- rank K_n(Z) = 0 otherwise

### 5.2 Concrete table of K_n(Z) (Weibel ch. VI §8)

| n  | K_n(Z)     | size    | project-constant decomposition |
| -- | ---------- | ------- | ------------------ |
| 0  | Z          | ∞       | rank 1             |
| 1  | Z/2        | 2       | = φ                |
| 2  | Z/2        | 2       | = φ                |
| 3  | Z/48       | 48      | = φ·J₂ = 2·24      |
| 4  | 0          | 1       |                    |
| 5  | Z          | ∞       | rank 1             |
| 6  | 0          | 1       |                    |
| 7  | Z/240      | 240     | = 2^4·3·5 = φ·J₂·sopfr? (§10 honesty) |
| 8  | 0          | 1       |                    |
| 9  | Z ⊕ Z/2    | ∞       | rank 1 + Z/2       |
| 10 | Z/2        | 2       | = φ                |
| 11 | Z/1008     | 1008    | = 2^4·3^2·7 = φ·504 |
| 12 | 0          | 1       |                    |
| 13 | Z ⊕ Z/2    | ∞       |                    |
| 14 | 0          | 1       |                    |
| 15 | Z/480 ⊕ Z/2 | 960     |                    |
| 16 | 0          | 1       |                    |
| 17 | Z ⊕ Z/2    | ∞       |                    |
| 18 | Z/2        | 2       | = φ                |
| 19 | Z/528      | 528     | = 2^4·3·11         |
| 20 | 0          | 1       |                    |
| 21 | Z ⊕ Z/2    | ∞       |                    |

(Weibel ch. VI §8 Thm 8.1; detailed values in Rognes–Weibel 2000 "Two-primary algebraic K-theory of rings of integers in number fields", J. AMS 13.)

### 5.3 Key observation — periodicity

n ≡ 0 (mod 4) gives K_n(Z) = 0.
n ≡ 1 (mod 4) gives K_n(Z) = Z (+ 2-torsion).
n ≡ 2 (mod 4) gives K_n(Z) = Z/2 (+ small).
n ≡ 3 (mod 4) gives K_n(Z) = Z/(large).

**"Large" values**:

- K_3(Z) = Z/48
- K_7(Z) = Z/240
- K_{11}(Z) = Z/1008
- K_{15}(Z) = Z/480 (together with Z/2)
- K_{19}(Z) = Z/528

In the sequence 48, 240, 504, 480 (K_{15} odd part), 264 (=K_{10}), 24 (=K_{2} of finite field adjustment), etc.,
**Bernoulli numbers** appear. The connection is understood via the **Lichtenbaum conjecture**.

### 5.4 Bernoulli number connection

**Lichtenbaum conjecture (original form)**: For F = Q,

```
  |K_{4k-2}(Z)|  =  numerator (B_{2k} / 4k)   (up to 2-power)
  size / rank of K_{4k-1}(Z)  ~  denominator (B_{2k} / 4k)
```

Most of the demonstration is complete via Voevodsky (2003) Bloch–Kato conjecture + Rost (2008) Bloch–Kato argument.

Concrete correspondence:
- k=1: B_2 = 1/6, related to |K_2(Z)|.
- k=2: B_4 = -1/30, K_7(Z) = Z/240. Here **240 = -1·-2·4·30 / ??**
  More precisely: ζ(1-2k) = -B_{2k}/(2k), so ζ(-3) = -B_4/4 = (1/30)/4 = 1/120. And 240 = 2·120.
- k=3: B_6 = 1/42, ζ(-5) = -B_6/6 = -(1/42)/6 = -1/252. K_{11}(Z) = Z/1008 = 4·252.
- k=4: B_8 = -1/30, ζ(-7) = -B_8/8 = (1/30)/8 = 1/240. K_{15}(Z) = Z/480 = 2·240.
- k=5: B_{10} = 5/66, ζ(-9) = -B_{10}/10 = -(5/66)/10 = -1/132. K_{19}(Z) = Z/528 = 4·132.
- k=6: B_{12} = -691/2730. **691 appears here** — **691 should enter K_{23}(Z)**.
  In fact: K_{23}(Z) = Z/(65520) with 65520 = 2^4·3^2·5·7·13 — **691 went to the cokernel** (slightly more complex).

This table is the key link for the P2-3 Bernoulli-numbers chapter.

### 5.5 K_7(Z) = Z/240 and the coincidence with 240

This **240** shows up:

- in the q-expansion coefficient of E_4(τ) (P2-1 §3.4), and
- in K_7(Z), and
- in bP_8 = Z/28 where 28 = perfect number (P2-4), and
- in the J-homomorphism image Im(J)_8 = Z/240 (topological K-theory, Adams 1966).

The reason these four "240"s are the same number lies in **Stickelberger relations** and the pattern of Bernoulli denominators.
By Adams' J-homomorphism theorem (1966, "On the groups J(X) IV"),

```
  Im J_n  ≅  Z / denominator(B_{2k}/4k)    (n = 4k-1)
```

denominator(B_2/4) = 24, denominator(B_4/8) = 240, ...

Hence **240 = denominator(B_4/8)** is the "real reason" and is the common source appearing simultaneously in the q-expansion of E_4,
K_7, the J-homomorphism, and bP_8.

---

## 6. Borel regulator

### 6.1 Borel regulator map

The key tool in the demonstration of Borel's theorem:

```
  regulator : K_{2n-1}(O_F) ⊗ R  →  R^{d(n)}
```

where d(n) = r_1 + r_2 if n is even and r_2 if n is odd. Borel demonstrated that this map is an **isomorphism**.

This fixes rank K_{2n-1}(O_F) = d(n).

### 6.2 Value of the Borel regulator

When normalized by volumes of units with ζ_F(1-2n), the determinant of the Borel regulator relates to ζ_F(1-2n).

**Borel theorem (stronger)**: For F a number field and n ≥ 2 even,

```
  ζ_F(1-2n)  =  ± (integer) · det(regulator on K_{2n-1}(O_F))  / ( some torsion factor )
```

This is the precursor of the Lichtenbaum conjecture (Borel himself stated it "up to a ±Q-rational").

### 6.3 Beilinson–Deligne regulator (extension)

Borel's regulator was generalized by Beilinson (1985) to Deligne cohomology. It links the "higher-dimensional" part of K-theory to
**Deligne cohomology** (= singular cohomology augmented by a Hodge structure).

This Beilinson regulator is the starting point for generalizations of the BSD conjecture ("special-value formula for L-functions").

---

## 7. Lichtenbaum conjecture (in detail)

### 7.1 Original conjecture (Lichtenbaum 1973)

**Conjecture** (Lichtenbaum, LNM 342, 1973): For F totally real number field and ℓ an odd prime,

```
  |K_{2n-2}(O_F)[ℓ]|        ℓ-part      
  ─────────────────────   =   of  ζ_F(1-n)   (n even)
  |K_{2n-1}(O_F)[ℓ]|
```

A more general formulation is the "étale cohomology version":

```
  K_n(O_F) ⊗ Z_ℓ  ≅  H_ét^{i}(Spec O_F[1/ℓ], Z_ℓ(j))   (appropriate i, j)
```

### 7.2 Bloch–Kato conjecture (generalization)

Bloch–Kato (1990, "L-functions and Tamagawa numbers of motives") generalized Lichtenbaum using motives.
For a motive M,

```
  L^*(M, 0) = (regulator)·(period)·(Tamagawa)·(Sha)
```

is the form of the formula. The BSD conjecture (treated in P1-3) is the case M = h^1(E) of an elliptic curve.

### 7.3 State of the demonstration

| result | demonstrator | year |
| ---- | ------ | ---- |
| Merkurjev–Suslin (K_2 / n = Br[n]) | Merkurjev–Suslin | 1982 |
| Bloch–Kato mod 2 | Voevodsky | 2003 |
| Bloch–Kato for odd primes | Voevodsky + Rost | 2008~2011 |
| Lichtenbaum full for cyclotomic fields | Kolster, Levine | 1989~1999 |
| Wiles main conjecture (Iwasawa) | Mazur–Wiles, Wiles | 1984, 1990 |

That is, **many parts of the Lichtenbaum conjecture are established**, but it is not fully complete for all number fields.

### 7.4 Voevodsky's motivic cohomology

Voevodsky introduced **motivic cohomology** (derived category of motives).
It became the framework for the Bloch–Kato argument, earning the 2002 Fields medal.

Motivic cohomology H^p(X, Z(q)) is given by Voevodsky's axiomatic definition. It obeys

```
  H^{p+q}_{mot}(Spec F, Z(q))  ≅  K^M_q(F)       (p=0 case)
  H^{p}_{mot}(X, Z(q))          ≅  K-theoretic information (general)
```

---

## 8. Milnor K-theory K^M_n

### 8.1 Definition

For R commutative and a_1, ..., a_n ∈ R*, Milnor K-theory is generated by symbols {a_1, ..., a_n}:

```
  K^M_n(R)  :=  T^n(R*) / (Steinberg relations)
```

Here Steinberg says {..., a, 1-a, ...} = 0.

### 8.2 Quillen K vs Milnor K

**Generally** Quillen K_n(R) ≠ K^M_n(R). There is a natural map K^M_n(R) → K_n(R), and typically neither surjective nor injective.

### 8.3 Milnor conjecture (Voevodsky 2003 demonstration)

**Milnor conjecture**:

```
  K^M_n(F) / 2  ≅  H^n_ét(F, Z/2)
```

(F a field, characteristic ≠ 2)

Voevodsky demonstrated this in 2003, receiving the Fields medal.

---

## 9. Overview of applications of K-theory

### 9.1 topological K-theory and Bott periodicity

**Bott periodicity (1957)**: topological K^*(S^{2n}) repeats with period 2.

```
  KU^*(pt)  =  Z[β, β^{-1}],  β of weight 2 (Bott element)
```

### 9.2 Atiyah–Singer index theorem

For an elliptic operator P : Γ(E) → Γ(F),

```
  index(P)  =  ∫_X  ch(σ(P)) · Td(X)     ∈  Z
```

where ch is the Chern character (K-theory → cohomology) and Td is the Todd class. K-theory is essential.

### 9.3 J-homomorphism

```
  J : π_n(O)  →  π_n^S(S^0)       (stable homotopy)
```

The image Im J_n ⊂ π_n^S was computed exactly by Adams (1966).

```
  Im J_{4k-1}  =  Z / denom(B_{2k}/4k)
```

**denom(B_2/4) = 24**, denom(B_4/8) = **240**, denom(B_6/12) = **504**, ...

These 240, 504 match the E_4, E_6 coefficients seen above (P2-1) and K_7(Z), bP_8 (P2-4).
That it comes from a **single Bernoulli-denominator origin** is remarkable.

---

## 10. Six takeaways from this chapter

1. **Definitions of K_0, K_1, K_2** — Grothendieck, Bass–Milnor, Milnor (Steinberg symbol).
2. **Quillen +-construction** — K_n := π_n(BGL(R)^+), n ≥ 1.
3. **K_n(Z) table** — K_3=Z/48, K_7=Z/240, K_{11}=Z/1008, K_{15}=Z/480·Z/2, period 4.
4. **Borel theorem** — complete computation of rank K_{2n-1}(O_F), regulator map.
5. **Lichtenbaum conjecture** — K_n ↔ étale cohomology ↔ special values of ζ_F.
6. **Unifying role of Bernoulli denominators** — why 240, 504 appear simultaneously in several places.

---

## 11. Honesty declaration

This note is a textbook summary. No new results.

### 11.1 Decomposition K_3(Z) = Z/48

48 = 2·24 = φ·J₂. This decomposition is exact. However,
- The reason 48 is the value appears in **Lee–Szczarba 1976** in detail; the actual derivation is the homotopy computation of BGL(Z)^+.
- Writing it as a project-constant product φ·J₂ is not a meaningful rearrangement since "J₂ = 24 is a prior, and 48 = 2·24 is trivial."

### 11.2 K_7(Z) = Z/240 and the match with the E_4 coefficient 240

- Both values come from **denominator(B_4/8) = 240**. This is the **same mathematical object** (J-homomorphism image).
- It can be written as the project-constant product φ·J₂·sopfr = 2·24·5 = 240, but the exact origin is the Bernoulli number B_4 = -1/30.
- Whether sopfr=5 fits here exactly may be a coincidence or a necessity.
  (5 is the only "large" prime appearing in the denominator 30 = 2·3·5 of B_4, so there is some necessity.)

### 11.3 K_{11}(Z) = Z/1008

- 1008 = 2^4·3^2·7 = 16·63 = 48·21 = 504·2. Can be written as the project-constant product φ·504.
- Exact origin: denominator(B_6/12) = 504, multiplied by 2. See Rognes–Weibel (2000) for the detailed computation.
- 504 itself originates from B_6 = 1/42 and 12·42 = 504.

### 11.4 The real reason "240 appears in several places"

- **Unique source**: denom(B_4/8) = 240.
- This number underlies K_7(Z), the E_4 coefficient, Im J_7, |bP_8|,
- and on the surface it looks like "the same number appearing four times = miracle", but dug deeper it is the **same origin (Bernoulli denominator + J-homomorphism)**.
- Hence the observation that "240 decomposes nicely into project constants" is the surface of a **number-theoretic fact that Bernoulli denominators are products of small primes**.
- This by itself is **an interesting observation but not direct evidence for the n=6 theorem**.

### 11.5 State of the Lichtenbaum conjecture

- Established for totally real fields and cyclotomic fields.
- For general number fields, the Bloch–Kato part was completed by Voevodsky.
- A "complete" Lichtenbaum (including detailed regulator formulas) is still open.

### 11.6 Primary sources listed

| topic | primary source |
| ---- | -------- |
| K_0 (Grothendieck) | Grothendieck, "Classes de faisceaux et théorème de Riemann–Roch", SGA 6 (1966) |
| K_1 (Bass) | Bass, *Algebraic K-Theory* (Benjamin, 1968) |
| K_2 (Milnor) | Milnor, *Introduction to Algebraic K-Theory* (Princeton, 1971) |
| Quillen higher K | Quillen, "Higher algebraic K-theory I", LNM 341 (1973) |
| K_n(F_q) | Quillen, "On the cohomology and K-theory of the general linear groups over a finite field", Ann. Math. 96 (1972) |
| Borel rank theorem | Borel, "Stable real cohomology of arithmetic groups", Ann. ENS 7 (1974) |
| Lichtenbaum conjecture | Lichtenbaum, LNM 342 (1973) 489–501 |
| Merkurjev–Suslin | Merkurjev–Suslin, Izv. AN SSSR 46 (1982) |
| Bloch–Kato / Voevodsky | Voevodsky, "Motivic cohomology with Z/2 coefficients", Publ. IHES 98 (2003) |
| Rognes–Weibel K(Z) | Rognes–Weibel, J. AMS 13 (2000) 1–54 |
| Adams J-homomorphism | Adams, "On the groups J(X) IV", Topology 5 (1966) |
| Bloch–Kato Tamagawa | Bloch–Kato, "L-functions and Tamagawa numbers of motives", *Grothendieck Festschrift I* (1990) |
| Weibel K-book | Weibel, *The K-book* (AMS GSM 145, 2013) |

---

## 12. Next steps (bridge to P2-3, P2-4)

- **P2-3 Bernoulli numbers**: B_{2k} seen here is the common source of ζ(1-2k), K_n(Z), Im J_n. In particular 691 first appears at B_{12} = -691/2730.
- **P2-4 Exotic spheres**: |bP_8| = 28, |bP_{12}| = 992, |bP_{16}| = 8128 match perfect numbers. Perfect numbers are related to Mersenne primes (2^p-1), and bP_n comes from the cokernel of the J-homomorphism. Hence K-theory and a topological viewpoint are linked.

End.
