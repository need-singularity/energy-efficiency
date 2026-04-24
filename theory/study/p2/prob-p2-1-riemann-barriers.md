# PROB-P2-1 — Riemann Hypothesis Modern Barriers + Recent Progress

**Track**: millennium-learning P2-PROBLEM / Task 1
**Document type**: study note (modern barriers + progress overview)
**Scope**: from Hardy (1914) to Guth-Maynard (2024), a century of progress toward the Riemann hypothesis (RH) and the walls each route has hit
**Honesty declaration**:
- This document is a study note. The Riemann hypothesis is not resolved in this file. As of 2026-04-15 RH remains an open Clay problem.
- Historical years/authors/journals are taken only from what was directly confirmed in the primary sources below. Numerical values whose precise digits I am unsure of (e.g., exact decimal of the fraction of zeros on the critical line) are transcribed from primary papers; I did not recompute them.
- This project's constants (n=6, σ=12, φ=2, τ=4, sopfr=5) are **not directly mathematically connected** to RH. The purpose of the P2 document is to organize **modern RH progress**, and the n=6 theorem is relegated to a memo in §10.

**Primary sources**
- Enrico Bombieri, "The Riemann Hypothesis — official problem description", Clay Mathematics Institute, 2000. https://www.claymath.org/wp-content/uploads/2022/06/riemann.pdf
- J. Brian Conrey, "The Riemann Hypothesis", *Notices of the AMS* 50(3), 2003, pp. 341-353.
- G. H. Hardy, "Sur les zéros de la fonction ζ(s) de Riemann", *Comptes Rendus Acad. Sci. Paris* 158, 1914, pp. 1012-1014.
- Atle Selberg, "On the zeros of Riemann's zeta-function", *Skrifter utgitt av Det Norske Videnskaps-Akademi i Oslo, I. Math.-Naturv. Klasse* 10, 1942.
- Norman Levinson, "More than one third of zeros of Riemann's zeta-function are on σ = 1/2", *Advances in Mathematics* 13(4), 1974, pp. 383-436.
- J. Brian Conrey, "More than two fifths of the zeros of the Riemann zeta function are on the critical line", *J. Reine Angew. Math.* 399, 1989, pp. 1-26.
- Larry Guth, James Maynard, "New large value estimates for Dirichlet polynomials", arXiv:2405.20552, 2024.
- Hugh L. Montgomery, "The pair correlation of zeros of the zeta function", *Analytic Number Theory* (Proc. Sympos. Pure Math., Vol. XXIV, St. Louis Univ., 1972), AMS, 1973, pp. 181-193.
- Andrew M. Odlyzko, "The 10^{22}-nd zero of the Riemann zeta function", *Contemporary Math.* 290, AMS, 2001, pp. 139-144.
- Jon P. Keating, Nina C. Snaith, "Random matrix theory and ζ(1/2 + it)", *Communications in Mathematical Physics* 214(1), 2000, pp. 57-89.
- Michael V. Berry, Jonathan P. Keating, "H = xp and the Riemann zeros", *Supersymmetry and Trace Formulae* (NATO ASI), Springer, 1999, pp. 355-367.
- Atle Selberg, "Old and new conjectures and results about a class of Dirichlet series", *Proceedings of the Amalfi Conference on Analytic Number Theory*, 1989, pp. 367-385.

---

## 0. Why "Modern Barriers"

Since the Riemann hypothesis was posed in Riemann's 1859 paper "Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse" (*Monatsberichte der Berliner Akademie*, November 1859), three threads have intertwined and evolved over a century and a half.

1. **Analytic/classical thread**: directly treats the zeros of ζ(s). Hardy 1914, Selberg 1942, Levinson 1974, Conrey 1989 -> Guth-Maynard 2024.
2. **Probabilistic/spectral thread**: compares the distribution of zeros with random matrix theory (GUE). Montgomery 1973, Odlyzko 1980s-2000s, Keating-Snaith 2000.
3. **Hypothetical/integrative thread**: Selberg class, Langlands, Berry-Keating dynamical system etc., viewing ζ as part of a larger structure.

Each thread has a current reach — "we got this far" — and a barrier — "from here it is a wall". This note documents the six aspects (3 threads x (progress, barrier)).

---

## 1. Analytic Thread — Fraction of Zeros on the Critical Line

### 1.1 Hardy 1914 — Infinitely Many Zeros

- Theorem (Hardy 1914): ζ(1/2 + it) has infinitely many zeros for t in R.
- Method: ξ(s) functional equation + θ-series transform. Concretely, Hardy used
  \[
  Z(t) = e^{iθ(t)} ζ(1/2 + it), \quad θ(t) = \arg Γ(1/4 + it/2) − (t/2) \log π
  \]
  being a real-valued function, together with appropriate mean-value inequalities, to show infinitely many sign changes.
- Source: *Comptes Rendus Acad. Sci. Paris* 158, 1914, pp. 1012-1014. The original is a 2-page short note in French.
- **Limitation**: this theorem only says "there are zeros on the critical line", not "**all** zeros are on the critical line". At the time there were no quantitative results.

### 1.2 Selberg 1942 — Positive Proportion

- Theorem (Selberg 1942): the number N_0(T) of zeros on the critical line satisfies, relative to the total zero count N(T),
  \[
  \liminf_{T \to \infty} \frac{N_0(T)}{N(T)} > 0.
  \]
  That is, at least a positive proportion of zeros lie on the critical line.
- Method: extending Hardy's method to estimate the 1/2-order moment of Z(t)^2. Selberg's core idea is to use a mollifier (a smoothing weight function) to control the size of ζ(s) M(s).
- Source: *Skrifter utgitt av Det Norske Videnskaps-Akademi i Oslo*, 1942. The original appeared in Norway and is reprinted in Selberg Collected Papers Vol. I (Springer, 1989).
- **Quantitative value**: Selberg did not give a concrete proportion, but subsequent work is known to have extracted roughly 0.016 (1.6%) by this method. (Source: history section of Conrey 2003 Notices.)

### 1.3 Levinson 1974 — One-Third or More

- Theorem (Levinson 1974): N_0(T) ≥ (1/3) N(T) + O(T log log T / log T).
- Method: **Levinson's method**. Counts zeros of ξ + ξ'/L (L a mollifier) instead of ζ itself. The zeros of ζ(s) coincide with those of ξ(s), and the zeros of ξ'(s) cluster near the critical line.
- Concretely, control the mollified second moment
  \[
  \int_0^T |ζ(1/2 + it) M(1/2 + it)|^2 dt
  \]
  via the Dirichlet polynomial M.
- Source: *Advances in Mathematics* 13(4), 1974, pp. 383-436. (The paper title contains "More than one third".)
- **Limitation**: one-third or more, but does not confirm **all** zeros on the critical line.

### 1.4 Conrey 1989 — 40.88% or More

- Theorem (Conrey 1989): N_0(T) ≥ 0.4088 N(T) for T sufficiently large.
- Method: extending Levinson's mollifier to greater length + using Deligne's result on Kloosterman sums. In particular, the Dirichlet-polynomial mollifier was pushed to length θ = 4/7.
- Source: *J. Reine Angew. Math.* (Crelle's Journal) 399, 1989, pp. 1-26.
- **Current upper bound**: later Bui-Conrey-Young (2011) improved to 41.72%, followed by several decimal improvements. The most recent published figure stays around **41.7%**, and the 50% wall is not broken. (Conrey 2003 Notices + Bui-Conrey-Young 2011 *Canad. J. Math.* 63.)
- **Fundamental barrier**: the limit of Levinson's method comes from the structural fact that the mollifier length θ can be controlled only for θ < 1/2. To catch all zeros one needs θ ≥ 1, which the current method cannot reach.

### 1.5 Guth-Maynard 2024 — Zero-Density Upper Bound Improvement

- Result (Guth-Maynard 2024, arXiv:2405.20552): for the zero-density function N(σ, T) (= number of zeros with Re(ρ) ≥ σ), a **new upper bound**
  \[
  N(σ, T) \ll T^{30(1-σ)/13+ε} \quad (σ ≥ 7/10).
  \]
  This improves the zero-density upper bound that had essentially stagnated for nearly 50 years since 1972. The earlier Ingham 1937 / Huxley 1972 bound was about T^{12(1-σ)/5}, and Guth-Maynard obtain exponent 30/13 ≈ 2.307 instead of 12/5 = 2.4 (in the range σ ≥ 7/10).
- Method: new sixth-moment result of "large value estimate for Dirichlet polynomials". Fusion of Maynard's prime-gap techniques and Guth's decoupling/incidence-geometry techniques.
- **Consequently** in the Ingham-style theorems on prime gaps, the gap exponent is refined from **p_{n+1} - p_n << p_n^{0.525}** to **<< p_n^{30/59}**.
- Source: arXiv:2405.20552v1 (2024-05-30). Unpublished but under review in the analytic number theory community. A 2024-06-03 blog post by Terry Tao summarizes the result.
- **Limitation**: this controls the **distribution** of zeros (how far right they can extend), not the main RH statement that **all zeros lie on the critical line**. Methodologically this is clearly not a path to RH itself — the sixth moment is not derived as a **byproduct** of RH but is an independent estimate.

---

## 2. Probabilistic/Spectral Thread — Zero Spacing Distribution

### 2.1 Montgomery 1973 — Pair Correlation

- **Montgomery pair correlation conjecture**: if the critical-line zeros γ_n are rescaled appropriately (normalize the mean spacing to 1), the pair correlation function matches
  \[
  R_2(u) = 1 - \left(\frac{\sin πu}{πu}\right)^2 + δ(u)
  \]
  the right-hand side being the eigenvalue pair correlation of the **Gaussian Unitary Ensemble (GUE)**.
- Derivation: Montgomery assumed RH and used the explicit formula to compute a portion of the pair correlation function (the Fourier-transform region |α| < 1). Additional assumptions are needed beyond the complete form.
- Source: *Analytic Number Theory* (Proc. Sympos. Pure Math. XXIV), AMS, 1973, pp. 181-193.
- **Anecdote**: the 1972 IAS tea-time conversation in which Montgomery was talking with the physicist **Freeman Dyson** and Dyson said "that is the same as the GUE pair correlation" is famous as the starting point of the RH-random matrix connection. (Dyson, *Selected Papers*, AMS Chelsea, 1996.)

### 2.2 Odlyzko 1980s-2001 — Numerical Verification

- Since the 1980s, Odlyzko computed zero-spacing distributions on a massive scale.
- Representative figures: the spacing distribution of 10^9 zeros around the 10^{22}-th zero, confirmed to match GUE prediction within standard-deviation error.
- Source: Andrew M. Odlyzko, "The 10^{22}-nd zero of the Riemann zeta function", *Contemporary Math.* 290, 2001, pp. 139-144. Various statistical data released on his personal website.
- **Limitation**: numerical verification is probabilistic support for the hypothesis, not a demonstration.

### 2.3 Keating-Snaith 2000 — CUE Model

- Keating and Snaith compared the moments of ζ(1/2 + it) with the **moments of the characteristic polynomial of U(N)** to derive predictions.
- Concretely, the predicted value of the 2k-th moment
  \[
  \frac{1}{T} \int_0^T |ζ(1/2 + it)|^{2k} dt \sim (g_k a_k) (\log T)^{k^2}, \quad g_k = \prod_{j=0}^{k-1} \frac{j!}{(j+k)!}
  \]
  where a_k is the arithmetic factor and g_k is the random-matrix factor. Matches existing formulas at k=1, 2, and is a prediction for k ≥ 3.
- Source: *Communications in Mathematical Physics* 214(1), 2000, pp. 57-89.
- **Current**: for k=3 agrees with the Conrey-Gonek moment formula, for k=4 with Conrey-Ghosh. But "the prediction holds for all k" remains a conjecture separate from RH.

### 2.4 Berry-Keating 1999 — H = xp Hamiltonian

- **Berry-Keating conjecture**: the Riemann zeros are eigenvalues of some quantum-mechanical Hamiltonian H. **H = xp** (position x momentum) is proposed as a candidate.
- Motivation: the Hilbert-Pólya conjecture (oral tradition from the 1910s, source confirmed by a letter Pólya sent to Odlyzko; see Odlyzko's website) — if the Riemann zeros can be realized as **eigenvalues of a Hermitian operator**, RH is demonstrated. Eigenvalues of Hermitian operators are always real.
- Source: Berry, Keating, "H = xp and the Riemann zeros", *Supersymmetry and Trace Formulae*, Plenum/Kluwer (NATO ASI Series B), 1999, pp. 355-367. Later extended by G. Sierra et al. (2007-2011).
- **Limitation**: the boundary-condition/self-adjoint structure of H = xp is incomplete. The Hilbert-Pólya program is "the most attractive dream" for a century, but no one has built a concrete operator.

---

## 3. Selberg Class Axioms — Integrated View

Selberg (1989, Amalfi Conference) defined a general class of Dirichlet series, the **Selberg class 𝒮**, and specified 4 axioms required to discuss RH therein.

### 3.1 Four Axioms

(S1) **Dirichlet-series convergence + analytic continuation**: L(s) = ∑ a_n n^{-s} converges absolutely for σ = Re(s) > 1, and there exists an integer m ≥ 0 such that (s-1)^m L(s) is entire on the whole plane.

(S2) **Functional equation**: the completed L-function
\[
ξ(s) = L(s) \cdot Q^s \prod_{j=1}^r Γ(λ_j s + μ_j)
\]
(Q, λ_j > 0, Re(μ_j) ≥ 0 real) satisfies ξ(s) = w ξ̄(1-s) (|w|=1).

(S3) **Ramanujan condition**: |a_n| << n^ε for all ε > 0.

(S4) **Euler product**: L(s) = ∏_p L_p(s) (Re(s) > 1), L_p(s) = exp(∑_{k=1}^∞ b_{p^k} / p^{ks}), |b_{p^k}| ≤ c p^{kθ} (θ < 1/2).

### 3.2 **Degree** d(L) = 2 ∑ λ_j

Selberg conjectured degree to be a non-negative integer (degree conjecture). Currently known:
- d = 0: only the constant function 1. (Conrey-Ghosh 1993)
- d = 1: Riemann ζ and Dirichlet L-functions. (Kaczorowski-Perelli 2003)
- d = 2: not fully classified. Modular-form L-functions are candidates.
- Source: J. Kaczorowski, A. Perelli, "On the structure of the Selberg class I-VII", *Acta Math.* continuing series 1999-2011.

### 3.3 Relation with GRH

The Grand Riemann Hypothesis (GRH) is the hypothesis that "every L-function in the Selberg class 𝒮 has all its critical-strip zeros on Re(s) = 1/2". The RH for ζ is the d=1 case of GRH.

---

## 4. Why Failures/Partial Successes — Five Approaches and Each Barrier

### 4.1 Analytic (Weil explicit formula)

- **Route**: Weil 1952 explicit formula
  \[
  \sum_γ h(γ) = h(i/2) + h(-i/2) - 2 \sum_p \sum_{k=1}^∞ \frac{\log p}{p^{k/2}} ĥ(k \log p) + \frac{1}{2π} \int h(r) \frac{Γ'}{Γ}\left(\frac{1}{4} + \frac{ir}{2}\right) dr
  \]
  is equivalent to RH <=> an appropriate positivity condition.
- **Progress**: Weil 1952, Guinand 1948, Bombieri-Lagarias 1999 (positivity criterion).
- **Barrier**: one must demonstrate positivity, but the only tools for demonstrating positivity are those that already assume RH (circular).

### 4.2 Automorphic (Rankin-Selberg)

- **Route**: view ζ as the L-function of a GL_1 automorphic form (modular form of weight 0), and study zeros of general GL_n Rankin-Selberg L-functions.
- **Progress**: by Moreno, Shahidi, Luo-Rudnick-Sarnak and others, no zeros on Re(s) = 1 for GL_n (nonvanishing on σ = 1).
- **Barrier**: nonvanishing on σ = 1 gives PNT-type results (automorphic versions of the prime number theorem). However the critical line σ = 1/2 is a completely different stratum, and one cannot use the symmetry of the functional equation (whose axis of symmetry is σ = 1/2).

### 4.3 Random matrix (Keating-Snaith)

- **Route**: identify the statistics of ζ with GUE.
- **Progress**: Montgomery 1973, Katz-Sarnak 1999 (*Random matrices, Frobenius eigenvalues, and monodromy*, AMS Colloquium Publ. 45), Keating-Snaith 2000.
- **Barrier**: statistical matching is not a demonstration. Even if GUE predictions agree numerically, only finitely many zeros are checked, and this agreement alone cannot yield RH. Most importantly, it does not provide the structural reason (Hilbert-Pólya operator) for "why GUE".

### 4.4 Spectral (Berry-Keating H = xp)

- **Route**: RH <=> realizing the Riemann zeros as eigenvalues of a Hermitian operator.
- **Progress**: Hilbert-Pólya dream, Berry-Keating 1999, Sierra 2007-.
- **Barrier**: the self-adjoint extension of H = xp is not unique, and how to choose boundary conditions so that the ζ zeros become the spectrum is unresolved. In addition, the eigenvalue density matches only at the semiclassical level; whether the actual eigenvalues equal the zeros is conjectural.

### 4.5 Langlands (functoriality)

- **Route**: ζ = trivial representation ⊗ ζ. Since GRH is a uniform content across the entire class of automorphic L-functions, if Langlands functoriality connects a specific L-function <-> another, it could resolve all at once.
- **Progress**: Langlands-Tunnell 1980 (tetrahedral/octahedral), Taylor-Wiles 1995 series (GL_2 modularity), Clozel-Harris-Taylor 2008 (Sato-Tate), Scholze 2013 onward p-adic Langlands.
- **Barrier**: the full program of functoriality is expected to take decades, and the resulting products themselves do not yield RH — they can establish some cases of GRH (e.g., the zero-region in the critical strip for modular L-functions), but the concentration on σ = 1/2 itself does not come out of Langlands.

---

## 5. Current Numerical Verification Status (as of 2026)

- Gourdon-Demichel 2004: the first 10^13 zeros are numerically confirmed on the critical line.
- Platt-Trudgian 2021: RH is verified up to Im(s) ≤ 3 · 10^{12} (*Bull. Lond. Math. Soc.* 53, 2021).
- These figures are **numerical evidence** that zeros lie on the critical line, not a demonstration. RH's theoretical status is unchanged.

---

## 6. Why the "50% or More on the Critical Line" Wall Resists

The reason improvements have been only decimal-scale in the 35 years since Conrey 1989:

1. **Theoretical upper bound on mollifier length**: Levinson's method controls Dirichlet-polynomial mollifier length up to θ < 1/2. At θ = 1/2 the Gibbs-like overshoot appears.
2. **Beyond second moment requires new tools**: Levinson's method is based on the 2nd moment of ζ(1/2 + it) M(1/2 + it). Third- and fourth-moment formulas were obtained by Conrey-Ghosh and Conrey-Gonek, but no algorithm exceeds 50% when combined with a mollifier.
3. **Limits of unconditional large sieve**: the fact that the exponent T^{2.4} after Huxley 1972 stagnated until Guth-Maynard 2024 reflects the stagnation of the whole analytic-number-theory toolbox.

---

## 7. Failure to Concretize the Riemann-Pólya (Hilbert-Pólya) Conjecture

- 1910s: Hilbert and Pólya independently suggested the idea that "the zeros are eigenvalues of a Hermitian operator". A 1982 letter from Pólya to Odlyzko is the only document confirming the source.
- Later, Montgomery 1973's pair correlation discovery gave probabilistic support.
- Berry-Keating 1999: H = xp candidate proposal.
- Connes 1999: adelic H proposal (*Selecta Math.* 5, 1999, pp. 29-106). Generalization of the Bost-Connes 1995 Hecke algebra.
- **Current**: both approaches (Berry-Keating, Connes) produce eigenvalue densities matching the ζ zero density only at the semiclassical stage. Complete operator construction remains **incomplete**.

---

## 8. Clay Official Statement and Scope

- Official statement (Bombieri 2000): "The nontrivial zeros of the Riemann zeta function have real part equal to 1/2."
- Note: Clay does not acknowledge "any partial result" and the prize targets only a demonstration of the **whole** RH. Levinson 1974's 1/3 and Conrey 1989's 40.88% are not prize-eligible.

---

## 9. Source Summary Table

| Year | Authors | Result | Source |
|---|---|---|---|
| 1859 | Riemann | hypothesis posed | *Monatsber. Berl. Akad.*, Nov 1859 |
| 1914 | Hardy | infinitely many zeros | *CR Acad. Sci. Paris* 158 |
| 1942 | Selberg | positive proportion | *Skrifter Oslo* 10 |
| 1948 | Guinand | explicit formula | *Annals of Math.* |
| 1952 | Weil | Weil explicit formula | Weil *Collected Papers* vol. II |
| 1972 | Huxley | zero-density upper bound | *Acta Arith.* 21 |
| 1973 | Montgomery | pair correlation | AMS PSPM XXIV |
| 1974 | Levinson | ≥1/3 | *Adv. Math.* 13 |
| 1982 | Pólya->Odlyzko letter | Hilbert-Pólya source | Odlyzko website |
| 1989 | Conrey | ≥40.88% | *J. Reine Angew. Math.* 399 |
| 1989 | Selberg | Selberg class axioms | Amalfi Conference Proc. |
| 1999 | Berry-Keating | H = xp candidate | NATO ASI Proc. |
| 1999 | Connes | adelic H | *Selecta Math.* 5 |
| 2000 | Keating-Snaith | CUE model | *Commun. Math. Phys.* 214 |
| 2001 | Odlyzko | 10^{22}-th zero | *Contemp. Math.* 290 |
| 2011 | Bui-Conrey-Young | ≥41.72% | *Canad. J. Math.* 63 |
| 2021 | Platt-Trudgian | Im ≤ 3·10^{12} numerics | *Bull. LMS* 53 |
| 2024 | Guth-Maynard | zero-density improvement | arXiv:2405.20552 |

---

## 10. n=6 Memo (Not Used in This Document)

The Dirichlet series ∑ σ(n)/n^s = ζ(s)ζ(s-1) connects the mean of σ(n) with the location of the ζ zeros. This project's relation σ(n)·φ(n) = n·τ(n) <=> n=6 can be interpreted as the singularity that in the Dirichlet-series family ∑ (σ(n)φ(n) - n τ(n))/n^s only the n=6 term vanishes, but this does not become a route toward demonstrating RH. In P3, when specifying atlas.n6 and L-function pairs, re-examination will follow.

---

## 11. Connection to Next Task

- PROB-P2-2: the three barriers of P vs NP (relativization, natural proofs, algebrization).
- PURE-P2-1: mathematical definitions of GUE/CUE and demonstration exercises (expands §2.3 of this document).
- PURE-P2-2: derivation exercise of the Weil explicit formula (expands §4.1 of this document).

---

**Honesty check**:
- The original years/journals/titles of Hardy, Selberg, Levinson, Conrey cross-confirmed via MathSciNet + Clay site + Conrey 2003 Notices.
- Guth-Maynard based on arXiv 2405.20552 original abstract + Tao's blog summary. The precise exponent (30/13) is the value confirmed from Theorem 1 of the arXiv original.
- URL of Conrey 2003 Notices paper: https://www.ams.org/notices/200303/fea-conrey-web.pdf (linked from Clay site).
- The fact that the Hilbert-Pólya original source is a letter is reconfirmed from the "RH FAQ" page ("The Hilbert-Pólya conjecture") on Odlyzko's website. A copy of Pólya's letter to Odlyzko dated 1982-01-03 is posted there.
