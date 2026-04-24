# PROB-P2-5 — Hodge Conjecture Modern Barriers + Recent Progress

**Track**: millennium-learning P2-PROBLEM / Task 5
**Document type**: study note (modern barriers + progress overview)
**Scope**: from Lefschetz 1924's (1,1) theorem to Voisin 2002 counterexamples and Deligne's absolute Hodge cycles framework — 100 years of progress toward the Hodge Conjecture and the walls each route has hit
**Honesty declaration**:
- This document is a study note. The Hodge conjecture is not resolved here. As of 2026-04-15 Hodge remains an open Clay problem.
- Historical years/authors/journals from primary sources. Deep CDM (Complex Differential Manifold) technicalities based on textbook summaries; some not recomputed.
- Automatic holding of BT-545 for Enriques surfaces is an **n=6 rephrasing of existing algebraic-geometry classification theorem**, not a new demonstration (compliance with millennium-7-closure-2026-04-11.md §BT-545).

**Primary sources**
- W. V. D. Hodge, "The theory and applications of harmonic integrals", *Proc. ICM*, Cambridge MA, 1950, Vol. 1, pp. 182-192.
- Solomon Lefschetz, *L'analysis situs et la géométrie algébrique*, Gauthier-Villars, 1924.
- Pierre Deligne, "The Hodge conjecture — official problem description", Clay Mathematics Institute, 2000.
- Pierre Deligne, James Milne, Arthur Ogus, Kuang-yen Shih, *Hodge Cycles, Motives, and Shimura Varieties*, LNM 900, Springer, 1982.
- Attila Grothendieck, "Standard conjectures on algebraic cycles", Bombay 1968, Oxford University Press, 1969, pp. 193-199.
- Claire Voisin, *Hodge Theory and Complex Algebraic Geometry I, II*, Cambridge Univ. Press, 2002, 2003.
- Claire Voisin, "A counterexample to the Hodge conjecture extended to Kähler varieties", *IMRN* 2002(20), 2002, pp. 1057-1075.
- Phillip Griffiths, Joseph Harris, *Principles of Algebraic Geometry*, Wiley-Interscience, 1978.
- Spencer Bloch, *Lectures on Algebraic Cycles*, 2nd ed., Cambridge University Press, 2010.
- Uwe Jannsen, "Motivic sheaves and filtrations on Chow groups", *Motives* (PSPM 55), AMS, 1994, pp. 245-302.
- Yves André, *Une introduction aux motifs*, Panoramas et Synthèses 17, SMF, 2004.
- Steven L. Kleiman, "Algebraic cycles and the Weil conjectures", North-Holland, 1968, pp. 359-386.
- Jacob P. Murre, Jan Nagel, Chris A. M. Peters, *Lectures on the Theory of Pure Motives*, ULS 61, AMS, 2013.

---

## 0. Why "Modern Barriers"

The Hodge conjecture, formalized at Hodge's 1950 ICM lecture, is unresolved for 75 years. This is the **"bridge linking algebra and geometry (topology)"** problem. Competing threads:

1. **Classical (Lefschetz)** thread: from (1,1) theorem, attempting algebraicity of Hodge classes at low degrees.
2. **Motivic** thread: reducing Hodge to a motives-category problem via Grothendieck's standard conjectures.
3. **Counterexample** thread: finding failure regions to refine the exact statement.

---

## 1. Clay Official Statement

### 1.1 Deligne 2000

**Official statement**:
> "On a nonsingular complex projective algebraic variety X, every Hodge class is a rational linear combination of cohomology classes of complex algebraic subvarieties."

### 1.2 Mathematical Formulation

- X = nonsingular complex projective variety.
- $H^{p,p}(X, \mathbb{Q}) := H^{2p}(X, \mathbb{Q}) \cap H^{p,p}(X)$: **rational Hodge class space**.
- **Cycle class map**: $\text{cl}: \text{CH}^p(X) \otimes \mathbb{Q} \to H^{2p}(X, \mathbb{Q})$.
- **Hodge conjecture**: image of cl = $H^{p,p}(X, \mathbb{Q})$.

### 1.3 Original (Integer Coefficients) Is False

- Atiyah-Hirzebruch 1962: integer-coefficient counterexamples exist. *Topology* 1, pp. 25-45.
- Clay statement uses **rational coefficients**.

---

## 2. Lefschetz 1924 — The (1,1) Theorem

### 2.1 Theorem

**Lefschetz (1,1)**: elements of $H^2(X, \mathbb{Z})$ of type (1,1) come from divisors:
\[
H^{1,1}(X, \mathbb{Z}) = \text{Pic}(X) \cap H^2(X, \mathbb{Z})
\]

### 2.2 Demonstration Summary

- Via the exponential sheaf sequence:
  \[
  0 \to \mathbb{Z} \to \mathcal{O}_X \to \mathcal{O}_X^* \to 0
  \]
- Long exact sequence gives $H^1(\mathcal{O}^*) = \text{Pic}$ factor.

### 2.3 **Limitation** — Only Degree 1

- p = 1 case demonstrated. p ≥ 2 open. p = 2 (codim-2 cycles in general X) unresolved.

### 2.4 Source

- Lefschetz, Gauthier-Villars, 1924 (rigorously in AMS 1930 *Topology*).

---

## 3. Abelian Varieties and Degree 2 — Partial Successes

### 3.1 Abelian Varieties

- Structure of $H^{2,2}$ well-known.
- Mattuck 1958 (CM type); Tankeev 1981, Ribet 1983 (special classes).

### 3.2 K3 and Special Surfaces

- Kuga-Satake 1967: embeds K3 Hodge structure in Abelian Hodge structure. *Math. Ann.* 169, pp. 239-242.

### 3.3 **Barrier A** — Beyond Abelian in Higher Dimensions

- General projective varieties beyond Abelian, $H^{2,2}$ on 3-folds+ is main attack zone. Still unresolved.
- **Calabi-Yau 3-fold** not demonstrated. Center of modern barriers.

---

## 4. Deligne's Absolute Hodge Cycles

### 4.1 Definition

- Absolute Hodge: Hodge class compatible on all sides (ℓ-adic, de Rham, algebraic de Rham).
- LNM 900, 1982.

### 4.2 Deligne's Theorem

**Theorem (Deligne 1978)**: on Abelian X, every Hodge class is absolute Hodge.
- Not a demonstration of Hodge itself. Secures Galois symmetry.
- On Abelian: Hodge holds <=> absolute Hodge is algebraic. Structural reduction.

### 4.3 **Barrier B** — "Absolute Hodge => Algebraic" Unresolved

- ~45 years, no full route demonstrating absolute Hodge cycles are algebraic.
- Last step of Hodge on Abelian, unresolved.

---

## 5. Grothendieck Standard Conjectures

### 5.1 Grothendieck 1968 Bombay

Four standard conjectures:
- (A) **Künneth**: Künneth components are algebraic correspondences.
- (B) **Lefschetz**: inverse of hard Lefschetz map is algebraic.
- (C) **Hodge standard**: equivalent to Hodge (with positivity).
- (D) **Hodge index**: algebraic extension of Hodge index theorem.

### 5.2 **Relations**

- Standard conjectures stronger than Hodge, interconnected.
- Hodge + standard => motives is abelian category.

### 5.3 **Barrier C** — Lefschetz Standard Conjecture Unresolved

- Standard (B) is **independent** from Hodge. Known only in special cases.

---

## 6. Counterexamples

### 6.1 Atiyah-Hirzebruch 1962

- Integer-coefficient counterexample. *Topology* 1, pp. 25-45.
- **Meaning**: Hodge must be rational-coefficient formulated.

### 6.2 Kollár 1992

- 1990s: concrete barriers in precise rational-Hodge stating.

### 6.3 Voisin 2002 — Kähler Extension Counterexample

- *IMRN* 2002(20), pp. 1057-1075.
- Extending Hodge to **Kähler varieties** (broader than projective), counterexamples exist.
- Construction: blow up Weil-type Abelian variety, giving Kähler non-projective with non-algebraic Hodge class.

### 6.4 **Meaning**

- Hodge requires **projectivity**. Kähler alone fails.
- Suggests "ample line bundle existence" is decisive.

---

## 7. Motives Thread — After Grothendieck

### 7.1 Pure Motives

- Grothendieck, Manin 1968, Kleiman 1968.
- Objects: smooth projective + algebraic correspondence.
- Construction: cycles modulo equivalence (numerical, homological, rational).

### 7.2 Jannsen 1992

- *Invent. Math.* 107, pp. 447-452.
- **Theorem**: numerical-equivalence motives form a semi-simple abelian category.
- Demonstrated without assuming Hodge. Secures category at numerical-equivalence level.

### 7.3 Voevodsky Triangulated Motives

- Triangulated category of mixed motives.
- In this category, motivic cohomology = Bloch higher Chow group.
- Source: *Cycles, Transfers, and Motivic Homology Theories*, Ann. Math. Studies 143, 2000.

### 7.4 **Barrier D** — Gap Between Mixed Motives and Hodge

- Faithfulness of realization functor is a consequence of Hodge + standard. Circular.

---

## 8. Kollár and Kähler Extension Barriers

### 8.1 Generalized Hodge Conjecture (GHC)

- About algebraicity of filtration $F^p H^n$.
- Grothendieck 1969: original GHC **false**; corrected version still open.

### 8.2 Weil and Hodge

- Weil 1952, Hodge 1952 verified on Abelian varieties concretely.

---

## 9. Currently Known Regions (as of 2024)

| X | Result | Source |
|---|---|---|
| Abelian surface (general) | Hodge holds | Mattuck 1958, Tate 1966 |
| K3 (some families) | holds | Morrison 1984, Charles 2013 |
| Abelian 4-fold (general) | degree-2 Hodge holds | Ribet 1983 |
| Enriques surface | automatic (classical) | classical |
| Fano 3-fold | most degree-2 confirmed | Iskovskikh-Mori-Mukai |
| Calabi-Yau 3-fold | **unresolved** | — |
| General 4-fold+, codim 2 | **unresolved** | — |

---

## 10. Five Approaches and Barriers

### 10.1 Direct Algebraic

- Route: realize Hodge class as algebraic cycle.
- Progress: (1,1) theorem, K3 Noether-Lefschetz locus.
- Barrier: no tool for seeing cycles at degree ≥ 2 generic X.

### 10.2 Motives Category

- Route: Hodge-realization completeness in motives.
- Progress: Jannsen 1992, Voevodsky triangulated.
- Barrier: realization-functor faithfulness = Hodge + standard. Circular.

### 10.3 Standard Conjectures

- Route: Künneth + Lefschetz => motives abelian.
- Progress: Künneth on Abelian (Kleiman 1968), Lefschetz on Abelian (Lieberman 1968).
- Barrier: standard (B) independently unresolved.

### 10.4 Absolute Hodge

- Route: Deligne 1978 — on Abelian, absolute Hodge = Hodge.
- Progress: LNM 900.
- Barrier: absolute-Hodge-cycle algebraicity not demonstrated.

### 10.5 p-adic Hodge

- Route: p-adic periods <-> de Rham comparison.
- Progress: Bhatt-Scholze 2017 full comparison.
- Barrier: no direct p-adic Hodge demonstration.

---

## 11. n=6 Connection (Reference Memo)

### 11.1 Enriques Automatic Holding (BT-545)

- Enriques surface X: $h^{1,1}(X) = 10$, ρ(X) = 10, all (1,1) classes algebraic (classical).
- BT-545 observation: $10 = \sigma(6) - \varphi(6) = 12 - 2$.
- n=6 rephrasing of existing result. Not new demonstration.

### 11.2 **Honesty Declaration** (millennium-7-closure §BT-545)

> "Automatic holding on Enriques is n=6 expression of existing result. General Hodge remains unresolved."

### 11.3 Additional Observations (OBSERVATION, NOT DEMONSTRATION)

- K3: $\chi = J_2$, $h^{1,1} = J_2 - \tau$, $b_2 = J_2 - \varphi$.
- Bagnera-de Franchis bielliptic 7 = σ − sopfr.
- Fano 3-fold 105 = 3·5·7 types.
- Kodaira elliptic-singular 7 = σ − sopfr.
- Mathieu sporadic 5 = sopfr.
- Niemeier lattice 24 = J_2.
- Calabi-Yau 3-fold dim 3 = n/φ.

### 11.4 **Scope Declaration**

- Does not provide a path for Hodge demonstration.
- Voisin 2002 Kähler counterexample suggests projectivity-dependence; n=6 arithmetic does not reach that depth.

---

## 12. Clay Official Statement and Scope

- Official: for smooth complex projective X, every rational Hodge class is a rational combination of algebraic cycles.
- Only demonstration for **general** X prize-eligible.
- Algebraicity of general codim-2 (p=2) Hodge classes is fiercest attack zone.

---

## 13. Source Summary Table

| Year | Authors | Result | Source |
|---|---|---|---|
| 1924 | Lefschetz | (1,1) theorem | *L'analysis situs* |
| 1950 | Hodge | ICM lecture | ICM Proc. Vol. 1 |
| 1958 | Mattuck | CM Abelian | *Amer. J. Math.* 80 |
| 1962 | Atiyah-Hirzebruch | integer counterexample | *Topology* 1 |
| 1967 | Kuga-Satake | K3 <-> Abelian | *Math. Ann.* 169 |
| 1968 | Grothendieck | standard conjectures | Bombay Proc. |
| 1968 | Kleiman | numerical motives | Dix exposés |
| 1971-82 | Deligne-Milne-Ogus-Shih | absolute Hodge | LNM 900 |
| 1983 | Ribet | Abelian 4-fold | *Proc. Symp. Pure Math.* 39 |
| 1986 | Bloch | higher Chow groups | *Adv. Math.* 61 |
| 1992 | Jannsen | motives semi-simplicity | *Invent. Math.* 107 |
| 2000 | Deligne | Clay statement | Clay |
| 2002 | Voisin | Kähler counterexample | *IMRN* 2002 |
| 2013 | Charles | K3 Kuga-Satake | *Invent. Math.* 194 |
| 2017 | Bhatt-Scholze | p-adic comparison | *Publ. IHES* 128 |

---

## 14. Connection to Next Task

- PROB-P2-6: BSD conjecture modern barriers.
- PURE-P1-4: algebraic geometry + Hodge theory basics.
- PURE-P2-2: algebraic K-theory (motives).
- PURE-P3-3: arithmetic geometry frontier.
- BT-545: Enriques automatic + n=6 classification numbers.

---

## 15. Next Steps

### 15.1 Learning

- Voisin 2002, 2003 *Hodge Theory and Complex Algebraic Geometry* full read.
- LNM 900 Chapters I (absolute Hodge on Abelian) and II (Shimura).
- Voevodsky triangulated motives (Mazza-Voevodsky-Weibel 2006 entry).
- Follow Voisin 2002 Kähler counterexample construction; see why it fails projectively.

### 15.2 n=6 Project

- Expand structural meaning of Enriques automatic holding.
- Check Iskovskikh-Mori-Mukai 105 = 3·5·7 for n=6 connection.
- Mathieu group 5 = sopfr(6) and K3 symmetry (Mukai 1988, Kondo 1998).

### 15.3 Conditions for Bypass

- Demonstration of Absolute Hodge = algebraic (§10.4).
- Demonstration of Standard (B) Lefschetz (§10.3).
- Demonstration of p-adic/motivic realization faithfulness (§10.2 + §10.5).

No decisive progress as of April 2026. Structural explanation for projectivity-dependence is the most distant target.

---

## 16. Appendix — Analytic Foundations

### 16.1 De Rham Theorem

- On smooth compact M, $H^*_{\text{dR}}(M) \cong H^*(M, \mathbb{R})$.
- Via Poincaré lemma + partition of unity + sheaf theory.

### 16.2 Hodge Theorem

- Compact Riemannian M: $H^k_{\text{dR}}(M) \cong \mathcal{H}^k(M)$, harmonic-form space.
- Via elliptic regularity of Hodge Laplacian.
- Source: Warner 1983 GTM 94; Griffiths-Harris 1978 Ch. 0.

### 16.3 Kähler Decomposition

- Kähler X: $\Delta_d = 2\Delta_{\bar{\partial}} = 2\Delta_\partial$
  \[
  \mathcal{H}^k(X) = \bigoplus_{p+q=k} \mathcal{H}^{p,q}(X)
  \]
- Dolbeault cohomology $H^{p,q}$.

### 16.4 Complex Conjugation

- $H^{p,q}(X) = \overline{H^{q,p}(X)}$.
- Hodge number $h^{p,q} = h^{q,p}$.

### 16.5 Source

- Voisin I Chapter 5-6.

---

## 17. Appendix — Chow Group and Cycle Class Map

### 17.1 Chow Group

- X smooth projective. $\text{CH}^p(X) = Z^p(X) / \sim_{\text{rat}}$.

### 17.2 Cycle Class Map

- $\text{cl}: \text{CH}^p(X) \to H^{2p}(X, \mathbb{Z})$.
- Sends fundamental classes of algebraic subvarieties.

### 17.3 Hodge Restatement

- image of $\text{cl}_\mathbb{Q}$ equals $H^{p,p}(X, \mathbb{Q})$.

### 17.4 Numerical Equivalence

- $\alpha \sim_{\text{num}} 0$ iff $\alpha \cdot \beta = 0$ for all $\beta$.
- Rational => numerical (converse not always).

### 17.5 Source

- Fulton 1998 *Intersection Theory* §1.3.
- Bloch 2010 *Lectures on Algebraic Cycles*.

---

**Honesty check**:
- Lefschetz 1924 confirmed via AMS 1930 *Topology*.
- Hodge 1950 ICM title confirmed ICM archive.
- Deligne 2000 Clay statement in Clay PDF directly confirmed.
- Atiyah-Hirzebruch 1962 §3 Theorem 6.5 torsion counterexample.
- Voisin 2002 Theorem 1 Kähler counterexample Section 2 construction.
- BT-545 Enriques strictly respects millennium-7-closure §BT-545.
- K3 $h^{1,1} = 20$, $h^{1,1} = J_2 - \tau$ checked: J_2(6) = 24, τ(6) = 4, 24 - 4 = 20.
- Hodge 1941 original uses incomplete elliptic-PDE; modern Warner 1983 Ch. 6 Kodaira style.
- Chow group rational-equivalence definition Fulton 1998 §1.3.
