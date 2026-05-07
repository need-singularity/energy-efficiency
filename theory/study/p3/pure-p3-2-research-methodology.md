# PURE P3-2 — Research-Mathematics Methodology

This study note is the 2nd output of the P3 PURE track in the canon millennium-learning roadmap. It organizes, on the basis of primary literature, the tools actually used in number theory / arithmetic geometry research (LMFDB, Sage, Magma, PARI/GP), the corresponding workflows, and conditional-draft techniques.

## Honesty declaration

- This document is a **methodology summary**. No new mathematical result.
- The "5 practical examples" below are standard examples recorded in a textbook (Silverman-Tate) and in official literature (LMFDB labels). The author has not personally accessed the LMFDB web during the writing of this document; cited numbers come from textbooks / official papers. Values the author has not checked are marked "(example from literature — needs re-check)".
- The Sage code is in the official Sage documentation syntax. The author has not executed it and pasted results; execution is the reader's (or the follow-up note's) job.
- The no-self-reference / no-fabrication rule is observed. BSD / BKLPR-related claims are deferred to P3-1.

## 0. Why tools matter

Computing the rank of a single elliptic curve by hand is algebraically high complexity. Selmer groups, Shafarevich-Tate groups, analytic rank of L functions, etc. cannot be experimented with unless one uses modern computer-algebra systems. The "experimental stage" of number-theory research happens on these tools. Separation of theorems and counterexamples is the output of that stage.

## 1. LMFDB — L-functions and Modular Forms Database

**URL**: https://www.lmfdb.org

**Background**: A shared database of the US / UK / European number-theory community, opened in 2016. Provides L-functions, elliptic curves, modular forms, number fields, Galois representations, Hilbert / Bianchi modular forms, etc. as interlinked objects.

**Main features**:
- For an elliptic curve E/Q: label (Cremona / LMFDB), conductor, j-invariant, discriminant, rank (analytic + algebraic), torsion, Sha_an approximation, Selmer rank 2, Tamagawa product, regulator, L(E,1), isogeny class.
- E/K (K a number field) is also cataloged.
- For each L function: zero distribution, functional equation.
- Modular forms — by weight / level / character.
- Search: conductor range, rank range, specific invariant constraints.

**Role in number-theory research**:
1. Conjecture check: "is this property observed" — verify immediately.
2. Counterexample search: produce counterexample candidates for conditional claims.
3. Statistics gathering: empirical approximations of quantities like E[|Sel_n|].

### 5 practical examples (example from literature — needs re-check)

Below are standard examples recorded in the Silverman-Tate text and in Cremona's elliptic-curve tables. The labels and numerics originate in official sources, but the author has not personally accessed LMFDB to confirm, so they are tagged "literature example".

**Example 1 — E: y² = x³ − x**
- Literature label: conductor 32 (32a2 class), j=1728, CM by Z[i].
- rank: 0, torsion Z/2Z × Z/2Z.
- L(E,1) ≠ 0 (BSD confirmed in this case).
- Methodology note: CM curves have L functions that split as products of Hecke characters, so a portion of BSD is drafted (Coates-Wiles 1977).

**Example 2 — E: y² = x³ − x + 1**
- Literature label: an "11a…" candidate from the old Cremona label family, conductor 11. (Exact label needs re-check.)
- rank: 0.
- Historical meaning: conductor 11 is the smallest non-CM-grade modular example.

**Example 3 — E: y² + y = x³ − x**
- Label: 37a1 (Cremona). **First rank-1 curve** — conductor 37, finite j-invariant.
- rank: 1.
- analytic rank: 1 (BSD confirmed).
- Methodology note: the representative example for which rank ≤ 1 BSD was drafted by the Gross-Zagier theorem (1986) and Kolyvagin (1989).

**Example 4 — E: y² + y = x³ − x²**
- Label: 37b1. Conductor 37, rank 0. A different isogeny class from 37a.
- Methodology note: two curves at the same conductor with different ranks — illustrating the importance of the isogeny class.

**Example 5 — E: y² = x³ − 2**
- A rank-1 example. Generator: (3, 5) (to be checked).
- Methodology note: in Mordell's family y² = x³ + k, k=-2 has rank 1 and the integer solutions are finite and recorded.

For each, BSD predicts rank = ord_{s=1} L(E,s). The examples above all have rank ≤ 1, so they lie in the range for which BSD has been drafted by Gross-Zagier-Kolyvagin. Examples with rank ≥ 2 (e.g., conductor 389, 389a1, rank 2) remain BSD conjectures.

## 2. Sage Math — elliptic-curve computation

**URL**: https://www.sagemath.org

**Background**: Started in 2005 by W. Stein. Python-based, GPL, an upper layer integrating multiple math systems (PARI, Singular, Maxima, GAP, NumPy, R, …). The de facto standard for elliptic curves / modular forms / L-functions.

### Standard workflow

```python
# Define an elliptic curve
E = EllipticCurve([-1, 0])    # y^2 = x^3 - x
# Or the full Weierstrass coefficients
E = EllipticCurve([0, 0, 1, -1, 0])  # y^2 + y = x^3 - x (37a1)

# Basic invariants
E.conductor()            # conductor
E.j_invariant()          # j-invariant
E.discriminant()         # discriminant
E.cremona_label()        # Cremona label

# rank / torsion
E.rank()                 # algebraic rank (2-descent-based)
E.analytic_rank()        # order of vanishing of the L function at s=1
E.torsion_subgroup()     # torsion subgroup

# Selmer / Sha
E.selmer_group_order(2)  # |Sel_2|
E.sha().an()             # Sha_an (analytic Sha approximation)

# L values
L = E.lseries()
L(1)                     # L(E,1)
L.taylor_series(1, 5)    # 5-th Taylor around s=1
```

### Sage practical script example (execution is the reader's job)

```python
# Batch compute for 5 example curves
curves = [
    ('32a2', [1, 0, 0, -1, 0]),    # y^2 = x^3 - x (variant)
    ('11a1', [0, -1, 1, -10, -20]),
    ('37a1', [0, 0, 1, -1, 0]),    # first rank 1
    ('37b1', [0, 1, 1, -23, -50]),
    ('389a1', [0, 1, 1, -2, 0]),   # first rank 2
]
for label, coeffs in curves:
    E = EllipticCurve(coeffs)
    print(label,
          'rank=', E.rank(),
          'tor=', E.torsion_subgroup().order(),
          'cond=', E.conductor(),
          '|Sel2|=', E.selmer_group_order(2))
```

Output should be checked in a Sage runtime. This document only records the code.

## 3. Magma, PARI/GP — auxiliary tools

**Magma** (University of Sydney, commercial, not free): deeper than Sage on elliptic-curve p-descent, 3-descent, 4-descent — i.e., Sel_n computation for n>2. Standard for BSD experimentation.

```
// Magma example
E := EllipticCurve([0, 0, 1, -1, 0]);
Rank(E);
MordellWeilShaInformation(E);
ThreeSelmerGroup(E);
```

**PARI/GP** (Bordeaux, free software): fast number-theory primitives. Called inside Sage. Direct use:

```
\\ PARI/GP
E = ellinit([0,0,1,-1,0]);
ellanalyticrank(E)    \\ analytic rank
ellL1(E)              \\ L(E,1)
```

**Selection criteria**:
- Typical rank ≤ 2 experiments: Sage suffices.
- 3/4-descent, higher Selmer: Magma.
- Fast statistical collection (millions of curves): PARI/GP directly.

## 4. Systematic counterexample search — design principle

For a conditional claim (e.g., "if rank ≤ 1 then P holds"), a counterexample-search program has the following structure.

### Structure
1. **Candidate generator**: enumerate isogeny-class representatives in the range conductor N ≤ N_max. Use Cremona's table (currently cataloging conductor ≤ 500000).
2. **Filter**: select only curves satisfying the claim's hypothesis (the range where P applies).
3. **Evaluation**: compute the claim's conclusion in Sage / Magma.
4. **Record**: log as counterexample candidates when the conclusion fails.
5. **Verification**: recompute candidates with a more precise (slower) method — eliminate false positives.

### Example — observing Selmer means
Goal: for fixed squarefree n, collect |Sel_n(E)| over E in range and compare the mean to σ(n).

```python
from sage.schemes.elliptic_curves.ell_rational_field import cremona_curves
n = 6
total, count = 0, 0
for E in cremona_curves(range(1, 1000)):  # conductor 1..999
    # |Sel_6| = |Sel_2| * |Sel_3| (unconditional, CRT)
    s2 = E.selmer_group_order(2)
    s3 = E.selmer_group_order(3)  # Sel_3 needs 3-descent, heavy
    total += s2 * s3
    count += 1
print('mean |Sel_6| =', total / count, 'vs sigma(6)=12')
```

Caveat: Sel_3 computation is slow even at conductor in the hundreds. For statistical significance, Magma 3-descent or a pre-computed LMFDB dump is needed.

## 5. Conditional-draft techniques — GRH etc.

In pure drafts, some rely on still-unproven assumptions (GRH, BKLPR, modular generalizations, etc.) to reach conclusions. These are "conditional theorems".

### Representative example — results under GRH (Generalized Riemann Hypothesis)
- **Bach 1990**: deterministic bound for Miller-Rabin primality testing under GRH. Bach, "Explicit bounds for primality testing and related problems", Math. Comp. 55 (1990), 355–380.
- **Artin conjecture (primitive root)**: Hooley 1967 gave a draft of Artin's conjecture under GRH.
- **Elkies 1987**: supersingular prime distribution under GRH.
- **Titchmarsh, "The Theory of the Riemann Zeta-function", 2nd ed. (Heath-Brown ed.), Oxford 1986, ch. 14**: ζ estimates under GRH.

### Conrad's notes
Brian Conrad's lecture notes (Stanford) are often cited as a textbook source for conditional-draft techniques. In particular, the GRH-assumption write-ups for BSD / Iwasawa theory.

### Writing principles
When presenting a conditional theorem:
1. Make the hypothesis explicit in the statement.
2. Separate the unconditional part obtainable without the hypothesis as a lemma.
3. Cite the source (which conjecture) of the hypothesis.
4. Present as a Corollary the consequence that follows if the hypothesis is drafted.

This project's BT-546 follows the principle by separating Lemma 1 (unconditional CRT) and Theorem 1 (BKLPR conditional). See P3-1.

## 6. Computer-algebra verification workflow

### Standard 4 steps
1. **Observation (Sage / LMFDB)**: pattern discovery.
2. **Counterexample search**: try larger conductors for counterexamples.
3. **Hypothesis formation**: a partial-theorem candidate.
4. **Draft / counter-draft**: mathematical argument. On failure, return to step 1.

### Cautions
- All computation must be **reproducible**. Record Sage version, library versions, random seeds.
- **Numerical error**: analytic rank, L(E,1), etc. are floating point. Choose thresholds carefully.
- **Precision lift**: Sage allows bit precision via RealField(prec). Essential when judging whether an L value is zero.
- **Heuristic vs draft distinction**: E.rank() may internally use some heuristics. For final claims, check the draft-rank flag.

## 7. Sources

1. J.H. Silverman, J. Tate, "Rational Points on Elliptic Curves", 2nd ed., Springer Undergraduate Texts in Math. (2015).
2. LMFDB Collaboration, "The L-functions and Modular Forms Database", https://www.lmfdb.org (2016–present).
3. W. Stein et al., Sage Math Documentation, https://doc.sagemath.org.
4. Magma Handbook, University of Sydney, http://magma.maths.usyd.edu.au.
5. PARI/GP User's Manual, Bordeaux, https://pari.math.u-bordeaux.fr.
6. J.E. Cremona, "Algorithms for Modular Elliptic Curves", 2nd ed., Cambridge (1997). Elliptic-curve table appendix.
7. E.C. Titchmarsh, "The Theory of the Riemann Zeta-function", 2nd ed., D.R. Heath-Brown ed., Oxford (1986), ch. 14.
8. E. Bach, "Explicit bounds for primality testing and related problems", Math. Comp. 55 (1990), 355–380.
9. B. Conrad, lecture notes (Stanford), http://math.stanford.edu/~conrad/ — BSD · Iwasawa family.
10. B. Gross, D. Zagier, "Heegner points and derivatives of L-series", Invent. Math. 84 (1986), 225–320. (foundation of the 37a1 rank-1 draft)
11. V. Kolyvagin, "Finiteness of E(Q) and Ш(E,Q) for a subclass of Weil curves", Izv. Akad. Nauk SSSR 52 (1988), 522–540.

## 8. Follow-up

- P3-3: arithmetic-geometry frontier — what new tools emerge in BSD / RH from perfectoid, prismatic.
- Practical exercise for this project: collect |Sel_2| statistics in Sage over the BT-546 range → compare with σ(2)=3. (agenda post-P4)
