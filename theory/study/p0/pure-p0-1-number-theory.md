# PURE-P0-1 Foundations of Number Theory Study Note

> Track: millennium-learning / P0 / PURE #1
> Format: self-contained study note
> Approach principle: **develop pure mathematics first, and record n=6 arithmetic only as a posteriori observation**
> Drafted: 2026-04-15

---

## 0. Purpose of This Note

This note systematically organizes **foundations of number theory** at P0 stage of the canon project's millennium-learning roadmap. It covers five topics in a self-contained manner and, in its final section, independently writes out the project's core theorem `σ(n)·φ(n) = n·τ(n) ⟺ n = 6` (Proof 1: multiplicative decomposition + local case analysis).

1. Prime number theorem π(x) ~ x/ln x, Chebyshev θ/ψ, Mertens' theorem
2. Divisor functions σ, τ, φ, J_k: definitions and multiplicativity, local formulas
3. Perfect numbers and the Euclid-Euler theorem (even perfect ↔ Mersenne prime)
4. Möbius function μ and Möbius inversion formula
5. Euler product formula ζ(s) = ∏ (1-p^{-s})^{-1}

At the end of each section the **primary sources** are cited down to chapter/section number of the textbook. The final section cross-references the corresponding chapters of Hardy-Wright / Apostol / Ireland-Rosen.

Honesty declaration is at the end.

---

## 1. Prime Number Theorem (PNT)

### 1.1 Definition of π(x)

```
π(x) := #{ p ∈ ℕ : p prime, p ≤ x },   x ∈ ℝ_{>0}.
```

Euclid (Elements IX.20) proved the infinitude of primes. Suppose there are finitely many, {p₁, …, p_n}. Then N = p₁·p₂·…·p_n + 1 is not divisible by any p_i, so a prime factor lies outside the set. Contradiction.

### 1.2 Chebyshev Functions

For proper asymptotic analysis introduce **log-weighted** counts.

```
θ(x) := Σ_{p ≤ x, p prime}        ln p
ψ(x) := Σ_{p^k ≤ x, p prime, k ≥ 1} ln p
     = Σ_{n ≤ x} Λ(n)
```

Here the **von Mangoldt** function Λ is

```
Λ(n) = { ln p   if n = p^k (k ≥ 1)
       { 0      otherwise.
```

### 1.3 Three Equivalences

The following three statements are **equivalent** (Apostol, ch. 4 §4.3).

```
(i)   π(x) ~ x / ln x
(ii)  θ(x) ~ x
(iii) ψ(x) ~ x
```

- (i) ⇔ (ii) follows directly via Abel summation (θ(x) = Σ ln p, π(x) = Σ 1).
- (ii) ⇔ (iii) via ψ(x) - θ(x) = O(√x · ln² x) = o(x).

### 1.4 Chebyshev Inequality (1852)

The best result before PNT. By **elementary methods** (log analysis of binomial coefficients)

```
0.921 · x/ln x ≤ π(x) ≤ 1.106 · x/ln x   (x ≫ 1)
```

The key tool is Σ_{p ≤ 2n} ln p ≤ 2n · ln 2 (prime factorization of C(2n,n)).

**Bertrand's postulate**: For every n ≥ 1 there exists a prime p with n < p ≤ 2n.
Proved by Chebyshev in 1852. Erdős's (1932) elementary proof is also famous.

### 1.5 PNT (Hadamard & de la Vallée Poussin 1896)

**Theorem**. ψ(x) ~ x. Hence π(x) ~ x/ln x.

**Proof sketch** (analytic). The Riemann zeta function ζ(s) = Σ n^{-s} (Re s > 1) is a meromorphic function on ℂ with a simple pole at s = 1 and has an analytic continuation to the whole plane. The following holds.

```
-ζ'(s)/ζ(s) = Σ Λ(n) n^{-s}     (Re s > 1)
```

By Perron's formula,

```
ψ(x) = (1/2πi) ∫_{c-i∞}^{c+i∞} (-ζ'(s)/ζ(s)) · x^s / s ds.
```

The obstruction when shifting the contour to Re s = 1 is precisely the **zeros of ζ(s)**. Hadamard and de la Vallée Poussin's core contribution: **ζ(1+it) ≠ 0** (t ∈ ℝ). From this, ψ(x) = x + o(x) follows.

### 1.6 Error Term and Riemann Hypothesis

**More precisely** (de la Vallée Poussin 1899)

```
π(x) = Li(x) + O(x · exp(-c √(ln x)))
```

where Li(x) := ∫₂^x dt/ln t. Under the **Riemann hypothesis**

```
π(x) = Li(x) + O(√x · ln x)
```

improves the estimate. This is Millennium problem BT-542.

### 1.7 Mertens' Theorems (1874)

Three **log-mean** results obtained before the PNT stage.

**Theorem 1 (Mertens)**.

```
Σ_{p ≤ x} ln p / p = ln x + M₁ + o(1)
```

M₁ is a constant.

**Theorem 2**.

```
Σ_{p ≤ x} 1/p = ln ln x + M + o(1)
```

Here M ≈ 0.2614972… is the **Meissel-Mertens constant**.

**Theorem 3**.

```
∏_{p ≤ x} (1 - 1/p) ~ e^{-γ} / ln x
```

γ is the Euler-Mascheroni constant. This formula underlies Rosser-Schoenfeld inequalities and connects directly with limit analysis of σ/n.

**Proof summary (Theorem 2)**. Apply Abel summation to θ(x) ≤ x·C. Chebyshev's inequality suffices; PNT is not needed.

### 1.8 Primary Sources

- Hardy-Wright, *An Introduction to the Theory of Numbers*, 6th ed., ch. 22 "The series of primes", §22.3–§22.10 (Chebyshev inequality, Mertens).
- Apostol, *Introduction to Analytic Number Theory*, Springer 1976, ch. 4 "Some elementary theorems on the distribution of prime numbers", §4.2 Chebyshev ψ and θ, §4.5 Mertens, ch. 13 "Analytic proof of the prime number theorem".
- Davenport, *Multiplicative Number Theory*, ch. 7 (Hadamard approach).

---

## 2. Divisor Functions σ, τ, φ, J_k

### 2.1 Basic Definitions

For n ∈ ℤ_{≥1},

```
τ(n) = #{ d ∈ ℕ : d | n }                  count of divisors
σ(n) = Σ_{d | n} d                          sum of divisors
σ_k(n) = Σ_{d | n} d^k                      k-th divisor sum (σ = σ₁, τ = σ₀)
φ(n) = #{ 1 ≤ a ≤ n : gcd(a, n) = 1 }       Euler totient
J_k(n) = n^k · ∏_{p | n} (1 - p^{-k})        Jordan totient (J₁ = φ)
```

### 2.2 Multiplicativity

A function f : ℕ → ℂ is **multiplicative** if gcd(m, n) = 1 ⇒ f(mn) = f(m)·f(n).
**Totally multiplicative** means the equality holds without the gcd condition.

**Theorem**. σ_k, τ, φ, J_k are all multiplicative.

**Proof (σ_k)**. If gcd(m, n) = 1, every divisor of mn decomposes **uniquely** as d_m · d_n (d_m | m, d_n | n). Hence

```
σ_k(mn) = Σ_{d_m | m} Σ_{d_n | n} (d_m d_n)^k
        = (Σ d_m^k)(Σ d_n^k) = σ_k(m) σ_k(n).  ∎
```

For φ, use the group isomorphism (ℤ/mnℤ)* ≅ (ℤ/mℤ)* × (ℤ/nℤ)* from the Chinese Remainder Theorem; the orders of both sides are φ(mn) and φ(m)·φ(n).

### 2.3 Prime-power Formulas

```
τ(p^a)   = a + 1
σ(p^a)   = (p^{a+1} - 1) / (p - 1)
σ_k(p^a) = (p^{k(a+1)} - 1) / (p^k - 1)
φ(p^a)   = p^a - p^{a-1} = p^{a-1}(p - 1)
J_k(p^a) = p^{ka} - p^{k(a-1)} = p^{k(a-1)}(p^k - 1)
```

### 2.4 Prime-factorization Forms

For n = p₁^{a₁} · p₂^{a₂} · … · p_r^{a_r},

```
τ(n) = ∏ (a_i + 1)
σ(n) = ∏ (p_i^{a_i + 1} - 1) / (p_i - 1)
φ(n) = n · ∏ (1 - 1/p_i)
```

### 2.5 Representative Identities

- In the **Dirichlet convolution** view τ = 1 ∗ 1, σ = id ∗ 1, φ = id ∗ μ,
  where (f ∗ g)(n) = Σ_{d | n} f(d) g(n/d).
- **Relations with ζ**: Σ τ(n)/n^s = ζ(s)², Σ σ(n)/n^s = ζ(s)ζ(s-1),
  Σ φ(n)/n^s = ζ(s-1)/ζ(s).

### 2.6 Inequalities and Asymptotics

- τ(n) = O(n^ε) (∀ ε > 0). More precisely, τ(n) ≤ 2^{(1+o(1)) ln n / ln ln n}.
- σ(n)/n and n/φ(n) both have the form ∏ (1 + 1/p_i + …). Upper bound at loglog scale:
  Gronwall (1913): lim sup σ(n)/(n · ln ln n) = e^γ.
- Lower bound: at primes n, σ(n)/n = 1 + 1/n → 1, so lim inf = 1.

### 2.7 Primary Sources

- Hardy-Wright, ch. 16 "The arithmetical functions φ(n), μ(n), d(n), σ(n), r(n)",
  §16.3–§16.4 (multiplicativity), §16.7 (prime-power formulas).
- Apostol, ch. 2 "Arithmetical functions and Dirichlet multiplication",
  §2.6–§2.10 (multiplicativity · Dirichlet convolution).
- Ireland-Rosen, *A Classical Introduction to Modern Number Theory*, ch. 2 §3.

---

## 3. Perfect Numbers and the Euclid-Euler Theorem

### 3.1 Definition

**Definition**. n ∈ ℤ_{≥2} is a **perfect number** if σ(n) = 2n, i.e., the sum of the proper divisors of n equals n.

Examples: 6 = 1+2+3, 28 = 1+2+4+7+14, 496, 8128, 33550336, …

### 3.2 Mersenne Primes

If p is prime and M_p = 2^p - 1 is also prime, M_p is a **Mersenne prime**.

Note: For M_p to be prime, p must be prime (2^{ab} - 1 is a multiple of 2^a - 1).
The converse is false: M_{11} = 2047 = 23 · 89.

Currently 52 Mersenne primes are known (as of GIMPS 2024). Infinitude is unresolved.

### 3.3 Euclid-Euler Theorem

**Theorem (Euclid IX.36 + Euler posthumously 1849)**.

An even number n is perfect ⟺ n = 2^{p-1} · (2^p - 1) and 2^p - 1 is prime.

**⇐ direction (Euclid)**. Let M = 2^p - 1 be prime and n = 2^{p-1} · M. Since M is prime and coprime to 2, σ is multiplicative.

```
σ(n) = σ(2^{p-1}) · σ(M)
     = (2^p - 1) · (M + 1)
     = (2^p - 1) · 2^p
     = 2 · 2^{p-1} · (2^p - 1)
     = 2n. ∎
```

**⇒ direction (Euler)**. Let n be an even perfect number. Write n = 2^{k-1} · m (k ≥ 2, m odd). By multiplicativity of σ,

```
σ(n) = σ(2^{k-1}) · σ(m) = (2^k - 1) · σ(m) = 2n = 2^k · m.
```

Hence σ(m) = 2^k · m / (2^k - 1). Since the LHS is an integer, (2^k - 1) | m. Writing m = (2^k - 1) · q,

```
σ(m) = 2^k · q.
```

Now m and q are divisors of m (q = m / (2^k - 1) ≤ m). If q < m, then m + q ≤ σ(m) and m + q = (2^k - 1)·q + q = 2^k · q = σ(m). That means the divisors of m are exactly {m, q}, so m is prime and q = 1. Hence

```
m = 2^k - 1    (prime),     n = 2^{k-1} · (2^k - 1).
```

If q = m then σ(m) = 2^k · m > 2m, making m an abundant number — contradictions can be shown directly (by computing σ(m)/m). ∎

### 3.4 Do Odd Perfect Numbers Exist?

**Unresolved**. Ochem–Rao (2012): If one exists, n > 10^{1500}, number of prime factors ≥ 101, largest prime factor ≥ 10^8, etc. Most number theorists conjecture that none exists, but no proof.

### 3.5 Primary Sources

- Hardy-Wright, ch. 9 "The representation of numbers by decimals" followed by §16.8 "Perfect numbers" (end of ch. 16).
- Burton, *Elementary Number Theory*, 7th ed., ch. 11 "Numbers of special form", §11.3 "Perfect numbers".
- Dickson, *History of the Theory of Numbers* vol. 1, ch. 1 (historical background).

---

## 4. Möbius Function and Möbius Inversion Formula

### 4.1 Definition

```
μ(n) = { 1        if n = 1
       { (-1)^k   if n = p₁ · p₂ · … · p_k (distinct primes, square-free)
       { 0        otherwise (some p² divides n)
```

### 4.2 Basic Identity

**Theorem**.

```
Σ_{d | n} μ(d) = [n = 1] = { 1 if n=1
                             { 0 if n≥2
```

**Proof**. n = 1 is trivial. For n ≥ 2 let the distinct prime factors of n be p₁, …, p_k. Only square-free divisors contribute:

```
Σ_{d | n} μ(d) = Σ_{S ⊂ {1,…,k}} (-1)^{|S|} = (1-1)^k = 0.  ∎
```

### 4.3 Möbius Inversion Formula

**Theorem (Apostol ch. 2 §2.9)**. For f, g : ℕ → ℂ,

```
g(n) = Σ_{d | n} f(d)    ⟺    f(n) = Σ_{d | n} μ(d) · g(n/d).
```

**Proof (⇒)**. Substitute and use the ⟂ identity.

```
Σ_{d | n} μ(d) · g(n/d) = Σ_{d | n} μ(d) · Σ_{e | n/d} f(e)
                       = Σ_{e | n} f(e) · Σ_{d | n/e} μ(d)
                       = Σ_{e | n} f(e) · [n/e = 1]
                       = f(n).  ∎
```

### 4.4 Applications

**Euler totient formula**. n = Σ_{d | n} φ(d) (grouping of 1, 2, …, n by gcd). Möbius inversion gives

```
φ(n) = Σ_{d | n} μ(d) · n/d = n · Σ_{d | n} μ(d) / d.
```

For n = p₁^{a₁} · … · p_r^{a_r},

```
Σ_{d | n} μ(d) / d = ∏ (1 - 1/p_i)
```

(only square-free divisors survive). Hence φ(n) = n · ∏ (1 - 1/p_i).

**Prime count**. π(x) can be computed with Möbius weights (Legendre sieve).

### 4.5 Mean of μ

**Theorem**. M(x) := Σ_{n ≤ x} μ(n). Equivalent to PNT,

```
M(x) = o(x).
```

Under the Riemann hypothesis M(x) = O(x^{1/2 + ε}). (The Mertens conjecture "M(x) ≤ √x" was disproved by Odlyzko-te Riele 1985.)

### 4.6 Primary Sources

- Apostol, ch. 2 §2.6 definition of μ, §2.9 Möbius inversion, ch. 3 §3.7 mean of M(x).
- Hardy-Wright, ch. 16 §16.3–§16.5 Möbius.
- Ireland-Rosen, ch. 2 §4 "The Möbius function".

---

## 5. Euler Product Formula

### 5.1 Zeta and Euler Product

**Theorem (Euler 1737)**. For s ∈ ℂ, Re s > 1,

```
ζ(s) := Σ_{n=1}^∞ n^{-s} = ∏_{p prime} (1 - p^{-s})^{-1}.
```

**Proof**. Expand the RHS geometrically:

```
(1 - p^{-s})^{-1} = 1 + p^{-s} + p^{-2s} + …
```

For finitely many primes p₁, …, p_N,

```
∏_{i=1}^N (1 - p_i^{-s})^{-1} = Σ_{n : prime factors ⊂ {p_i}} n^{-s}.
```

Letting N → ∞, by unique factorization of integers, every n ∈ ℕ appears exactly once. Absolute convergence in Re s > 1. ∎

### 5.2 Divergence at s = 1

**Corollary**. Σ 1/p diverges (hence there are infinitely many primes).

**Proof**. If finite, ∏ (1 - 1/p)^{-1} < ∞. But at s = 1, ∏_{p ≤ x} (1 - 1/p)^{-1} ≥ Σ_{n ≤ x} 1/n → ∞. Contradiction. ∎

This is the starting point of Euler's number-theoretic revolution.

### 5.3 General Multiplicative Functions

If f is multiplicative and Σ |f(n)| n^{-σ} < ∞, then

```
Σ f(n) n^{-s} = ∏_p ( Σ_{a ≥ 0} f(p^a) p^{-as} ).
```

**Examples**.

```
Σ τ(n) n^{-s}   = ζ(s)²         = ∏ (1 - p^{-s})^{-2}
Σ σ(n) n^{-s}   = ζ(s) ζ(s-1)   = ∏ (1 - p^{-s})^{-1} (1 - p^{1-s})^{-1}
Σ φ(n) n^{-s}   = ζ(s-1)/ζ(s)
Σ μ(n) n^{-s}   = 1/ζ(s)        = ∏ (1 - p^{-s})
Σ |μ(n)| n^{-s} = ζ(s)/ζ(2s)
```

### 5.4 Preview of the Functional Equation

ζ(s) extends to the completed zeta ξ(s) := (1/2) s (s-1) π^{-s/2} Γ(s/2) ζ(s) with the s ↔ 1-s symmetry (Riemann 1859). This functional equation is revisited in PURE-P0-3 (complex analysis note).

### 5.5 Primary Sources

- Apostol, ch. 11 "Dirichlet series and Euler products", §11.6–§11.8.
- Hardy-Wright, ch. 17 "Generating functions of arithmetical functions".
- Ireland-Rosen, ch. 3 §1 "The zeta function".
- Titchmarsh, *The Theory of the Riemann Zeta-Function*, ch. 1 (analytic properties).

---

## 6. Follow-through of the σ(n)·φ(n) = n·τ(n) Uniqueness Theorem

This section gives an **independent writeup** of the project L0 invariant `theory/proofs/theorem-r1-uniqueness.md` (approach = multiplicative decomposition + local case analysis, Proof-1 family).

### 6.1 Statement

**Theorem R1**. For every n ∈ ℤ_{≥2},

```
σ(n) · φ(n) = n · τ(n)  ⟺  n = 6.
```

### 6.2 Local Ratio R_local

Define R : ℤ_{≥1} → ℚ_{>0} by

```
R(n) := σ(n) · φ(n) / (n · τ(n))
```

The theorem reduces to finding all solutions of R(n) = 1 for n ≥ 2.

Since σ, φ, τ are all **multiplicative** and id(n) = n is totally multiplicative, R is multiplicative. For n = ∏ p_i^{a_i},

```
R(n) = ∏ R_local(p_i, a_i)
```

with

```
R_local(p, a) := σ(p^a) · φ(p^a) / (p^a · τ(p^a)).
```

### 6.3 Closed Form of R_local

Substitute the prime-power formulas of §2.3.

```
σ(p^a) = (p^{a+1} - 1) / (p - 1)
φ(p^a) = p^{a-1} (p - 1)
τ(p^a) = a + 1
```

Hence

```
R_local(p, a) = [ (p^{a+1} - 1) / (p - 1) ] · [ p^{a-1} (p - 1) ]
                ───────────────────────────────────────────────
                            p^a · (a + 1)

              = (p^{a+1} - 1) · p^{a-1}
                ───────────────────────
                    p^a · (a + 1)

              = (p^{a+1} - 1) / ( p · (a + 1) ).
```

### 6.4 Table of Local Values

| (p, a)  | R_local           | Value  | Relation to 1 |
|---------|-------------------|--------|---------------|
| (2, 1)  | (4-1)/(2·2) = 3/4 | 0.75   | **< 1**       |
| (2, 2)  | (8-1)/(2·3) = 7/6 | 1.1667 | > 1           |
| (2, 3)  | (16-1)/(2·4) =15/8| 1.875  | > 1           |
| (3, 1)  | (9-1)/(3·2) = 4/3 | 1.333  | > 1           |
| (3, 2)  | (27-1)/(3·3) =26/9| 2.889  | > 1           |
| (5, 1)  | (25-1)/(5·2)=12/5 | 2.4    | > 1           |
| (7, 1)  | (49-1)/(7·2)=24/7 | 3.429  | > 1           |
| (p, 1), p≥3 | (p²-1)/(2p)   | ≥4/3   | > 1 (monotone↑) |

### 6.5 Lemma — R_local < 1 Occurs Uniquely

**Lemma L1**. R_local(p, a) < 1 ⟺ (p, a) = (2, 1).

**Proof**. R_local(2, 1) = 3/4 < 1 is confirmed in the table. Check the rest.

- **p = 2, a = 1**: 3/4 (unique < 1 case).
- **p = 2, a ≥ 2**: R_local(2, a) = (2^{a+1} - 1)/(2(a+1)).
  For a=2 it is 7/6, for a=3 it is 15/8. In general the numerator is exponential 2^{a+1} and the denominator linear 2(a+1).
  For a ≥ 2 induction shows R_local(2, a) > 1: (2^{a+1}-1)/(2(a+1)) > 1 ⟺ 2^{a+1} > 2(a+1)+1.
  At a=2, 8 > 7, thereafter LHS doubles and RHS grows by 2, so monotone.
- **p ≥ 3, a = 1**: R_local(p, 1) = (p² - 1)/(2p) = p/2 - 1/(2p).
  At p = 3 it is 4/3. For p ≥ 3, p/2 - 1/(2p) ≥ 3/2 - 1/6 = 4/3 > 1, monotone increasing.
- **p ≥ 3, a ≥ 2**: R_local(p, a) > R_local(p, 1) (numerator p^{a+1} - 1 grows rapidly in a, denominator linear in a). ∎

### 6.6 Case 1 — Prime Power n = p^a

R(n) = R_local(p, a). By Lemma L1,

- (p, a) = (2, 1): R = 3/4 ≠ 1.
- Otherwise: R > 1 ≠ 1.

No solution in the prime-power case. ∎

### 6.7 Case 2 — Two Prime Factors n = p^a · q^b (p < q)

R(n) = R_local(p, a) · R_local(q, b). For R = 1 **exactly one local factor must be < 1** (Lemma L1 makes the < 1 case unique; otherwise the rest cannot go below 1, and if both are ≥ 1 their product is ≥ 1 with equality only if both are 1, but no local factor equals 1 either).

Hence (p, a) = (2, 1) is the only candidate. Since R_local(2, 1) = 3/4,

```
R_local(q, b) = 4/3.
```

Find (q, b).

- **(q, b) = (3, 1)**: R_local(3, 1) = (9-1)/(3·2) = 4/3. **Match**.
- (q, b) = (3, 2): 26/9 ≈ 2.889 ≠ 4/3.
- (q, b) = (3, ≥2): monotone growth exceeds 4/3.
- (q, b) = (5, 1): 12/5 = 2.4 ≠ 4/3.
- (q, b) = (q, 1), q ≥ 5: (q²-1)/(2q) ≥ 12/5 > 4/3.

The unique solution is (p, a, q, b) = (2, 1, 3, 1), i.e., **n = 6**.

Check:

```
σ(6) = 1+2+3+6 = 12
φ(6) = |{1, 5}| = 2
τ(6) = |{1,2,3,6}| = 4
σ·φ = 12·2 = 24
n·τ = 6·4 = 24.   ✓
```

### 6.8 Case 3 — Three or More Prime Factors

n = ∏_{i=1}^k p_i^{a_i} (k ≥ 3). By Lemma L1, **at most one local factor** is less than 1, and it must be R_local(2, 1) = 3/4. The other k-1 local factors are ≥ 4/3 (≥ R_local(3, 1)).

**Case 3a**: p₁ = 2, a₁ = 1.

```
R(n) ≥ (3/4) · (4/3)^{k-1}
     ≥ (3/4) · (4/3)² = (3/4) · (16/9) = 48/36 = 4/3 > 1.
```

**Case 3b**: p₁ ≥ 3 (or p₁ = 2, a₁ ≥ 2).

All local factors ≥ 4/3 and

```
R(n) ≥ (4/3)^k ≥ (4/3)³ = 64/27 ≈ 2.370 > 1.
```

No solutions with three or more prime factors either. ∎

### 6.9 Conclusion

Combining Cases 1, 2, 3, the unique solution of R(n) = 1 is **n = 6**. ∎

```
╔═══════════════════════════════════════════════════════════════╗
║  Theorem R1 (restated)                                         ║
║                                                               ║
║  For every n ∈ ℤ_{≥2},                                         ║
║    σ(n) · φ(n) = n · τ(n)  ⟺  n = 6                          ║
║                                                               ║
║  Proof: multiplicativity of σ, φ, τ + R_local(p, a) case      ║
║  analysis.                                                    ║
║  Core: R_local < 1 occurs only at (2,1), value 3/4.           ║
║  The only combination that compensates is (2,1)·(3,1), i.e.   ║
║  n = 6.                                                       ║
║                                                               ║
║  Q.E.D.                                                      ║
╚═══════════════════════════════════════════════════════════════╝
```

### 6.10 Posterior Observation

This note **starts from pure mathematics** and obtains n = 6 as a result of case analysis. The fact is **not** presupposed with n = 6 in mind. The form of the theorem is "the set of n ∈ ℤ_{≥2} satisfying σ·φ = n·τ", and at the end of the case analysis we confirm that the set is {6}.

Unlike general perfect numbers, this theorem has equality only at the **first perfect number n = 6**; at n = 28, 496, 8128, … the values R = 4, 48, 576 diverge rapidly. Hence R1 is a **finer** characterization than perfect numbers.

### 6.11 Primary Sources

- The present proof is an independent reconstruction of Proof 1 from theorem-r1-uniqueness.md (L0 invariant).
- Multiplicativity of σ/φ/τ: Apostol ch. 2 §2.6–§2.10.
- Prime-power formulas: Hardy-Wright ch. 16 §16.7.
- Local case-analysis method for multiplicative functions: Apostol ch. 2 exercise-style solutions.

---

## 7. Next-step Guide

- **PURE-P0-2 (Introduction to Group Theory)**: covers the uniqueness of Out(S_6) — a separate reason n = 6 appears in the world of symmetric groups.
- **PURE-P0-3 (Introduction to Complex Analysis)**: proof of ζ(2) = π²/6 and the gamma function.
- **P1 stage**: analytic number theory (Dirichlet L, prime distribution), algebraic number theory (class group, Ostrowski).

Once this note is mastered, the goal is to be able to rewrite Proof 1 of `theory/proofs/theorem-r1-uniqueness.md` from scratch with only a textbook as companion.

---

## Honesty Declaration

This note is a **study summary**. It does not contain new theorems or Millennium-problem targets. The status of the seven Millennium problems in the canon project is **0/7**, and this note does not change that number. Cited theorems · authors · textbook chapter numbers are all real; anything uncertain was not included when written. Adhering to the no-self-referential-verification rule, the result n = 6 is recorded only as an **a posteriori consequence** of general number-theoretic logic.
