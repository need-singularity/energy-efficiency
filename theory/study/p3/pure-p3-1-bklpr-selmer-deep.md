# PURE P3-1 — BKLPR Selmer Model Deep Dive

This study note is the 1st output of the P3 PURE track in the canon millennium-learning roadmap. It organizes, from primary sources, the BKLPR Selmer model — the theoretical backbone of the σ(n)·φ(n)=n·τ(n) iff n=6 theorem and the BT-546 BSD conditional Corollary.

## Honesty declaration

- This document handles **conditional (CONDITIONAL)** results. The BKLPR model itself is a heuristic, and BSD is open.
- This project drafts neither BSD nor BKLPR. 7-problem draft-candidate count is 0/7.
- Among the theorems below, only Lemma 1 (CRT direct decomposition) is unconditional; Theorem 1 and Corollary are conditional under the BKLPR assumption.
- Primary sources: Poonen-Rains 2012 J. AMS 25, BKLPR 2015 J. AMS, Cohen-Lenstra 1984 Springer LNM 1068. The narrative here rests on the public summaries of these papers (arXiv abstracts · author lecture notes) and memory/reference_bklpr_model.md.
- No numerical experiment / self-check in this document. Only methodology / logical-path writing. The no-self-reference rule is observed.

## 0. Background — why a random-matrix Selmer model

The Mordell-Weil group E(Q) of an elliptic curve E/Q is a finitely generated abelian group.
E(Q) ≅ Z^r ⊕ E(Q)_tors, r = rank.
BSD expresses r as the order of vanishing of the L-function L(E,s) at s=1. Weak form:
  ord_{s=1} L(E,s) = rank E(Q).

But rank itself is hard to compute effectively. What is actually computable is the Selmer group:
  Sel_n(E) := ker( H^1(G_Q, E[n]) → ∏_v H^1(G_{Q_v}, E) ).

From the exact sequence
  0 → E(Q)/nE(Q) → Sel_n(E) → Ш(E)[n] → 0
|Sel_n(E)| is computable and |Ш| is conjecturally finite (part of BSD). So knowing the distribution of Sel_n gives statistical information about rank and Ш.

## 1. Cohen-Lenstra heuristics (1984)

Source: H. Cohen, H.W. Lenstra Jr., "Heuristics on class groups of number fields", Springer LNM 1068 (1984).

**Core idea**: the p-Sylow part Cl(K)_p of the ideal class group Cl(K) of a number field K can be modeled as a "random finite abelian p-group". Its distribution is the cokernel model:
  n→∞ limit of the distribution of coker(M) over random integer matrices M: Z_p^n → Z_p^n (Haar measure).

Theorem (Cohen-Lenstra): in this limit, a finite abelian p-group G appears with probability proportional to 1/|Aut(G)|:
  Prob(Cl_p ≅ G) ∝ 1/|Aut(G)|.

From this model, several number-theoretic averages (e.g., E[|Cl_p|^k]) are computed in closed form. This is the beginning of predicting distributions of arithmetic objects via "random-matrix cokernels".

## 2. Poonen-Rains 2012 — Selmer random-matrix model

Source: B. Poonen, E. Rains, "Random maximal isotropic subspaces and Selmer groups", J. AMS 25 (2012), 245–269.

Poonen and Rains transplanted Cohen-Lenstra to Selmer groups.

**Model (intuition)**:
1. E[p] is a G_Q-representation. By the Weil pairing, E[p] carries an alternating non-degenerate form.
2. Hence a symmetric or alternating quadratic form naturally exists on relevant subspaces of H^1(G_Q, E[p]).
3. The **Selmer group** Sel_p(E) is described as an intersection of **maximal isotropic subspaces** inside H^1.
4. This intersection is modeled as "intersection of random maximal isotropic subspaces".

**Main results (summary)**:
- A p-adic distribution for the size |Sel_p(E)| of Sel_p(E) is computed.
- Mean E[|Sel_p|] = p + 1 (model prediction).
- This gives 3 at p=2, 4 at p=3, 6 at p=5, 8 at p=7, etc. — matches observational statistics well.

**Core formula (outline)**:
  V = H^1 quadratic-form space, W₁ = maximal isotropic subspace describing Sel.
  Sel_p(E) = V_{E,p} ∩ W_{E,p} form.
  Under randomization, moments of |Sel_p| are computed in closed form.

## 3. Bhargava-Kane-Lenstra-Poonen-Rains 2015 — refinement and CRT extension

Source: M. Bhargava, D. Kane, H.W. Lenstra Jr., B. Poonen, E. Rains, "Modeling the distribution of ranks, Selmer groups, and Shafarevich-Tate groups of elliptic curves", Cambridge J. Math. 3 (2015), 275–321 (via J. AMS channel).

Bhargava's elliptic-curve averaging result (Annals 2015) is fused with the Poonen-Rains model.

**Extension points**:
1. **Composite n generalization**: a model not just for Sel_p but for Sel_n in general.
2. **CRT direct decomposition**: when gcd(m,n)=1, Sel_{mn}(E) ≅ Sel_m(E) × Sel_n(E). This is unconditional — arithmetically it follows directly from the exact sequence.
3. **Squarefree-n mean formula**: under the model
    **E[|Sel_n(E)|] = σ(n)**    (squarefree n, averaged over equivalence-class elliptic-curve set)
   where σ(n) = sum of divisors. Derivation:
    σ(n) = ∏_{p | n} (p+1)  (since squarefree)
    = ∏_{p | n} E[|Sel_p|]
    = E[∏_{p | n} |Sel_p|]   (under independence assumption A3)
    = E[|Sel_n|]            (CRT direct decomposition).
4. **Rank-distribution prediction**: a statistical prediction that the ratios of ranks 0 or 1 are each 1/2 (summing to 1). Under BSD, a prediction on the distribution of L(E,1) zeros.
5. **Ш distribution**: a Delaunay-Cohen-Lenstra-style prediction modification for Ш.

## 4. Contribution of this project — n=6 specialization (CONDITIONAL)

The σφ=nτ iff n=6 theorem is uniqueness at the natural-number level. Plugging this uniqueness into the BKLPR model, a special status for n=6 appears at the Selmer level.

### Lemma 1 (unconditional)
When gcd(m,n)=1:
  |Sel_{mn}(E)| = |Sel_m(E)| · |Sel_n(E)|.

Draft sketch: from E[mn] ≅ E[m] ⊕ E[n] (CRT), the Galois cohomology exact sequence splits as a direct sum. The maximal isotropic subspace also decomposes. Hence Sel also splits. Each factor being finite, the size multiplies.

This Lemma holds without the BKLPR model assumption. It is the starting point of this project's BT-546 roadmap.

### Theorem 1 (BKLPR conditional)
For squarefree n:
  E[|Sel_n(E)|] = σ(n)   (average over the equivalence-class elliptic-curve set, under the BKLPR model).

Draft route:
1. From the Poonen-Rains model, E[|Sel_p|] = p + 1.
2. Under the BKLPR model, for distinct primes p, q, |Sel_p| and |Sel_q| are independent (assumption A3 — see §7).
3. Apply expectations to Lemma 1 (unconditional CRT).
4. Re-arrange as σ(n) = ∏_{p|n} (p+1).

### Corollary (n=6)
n=6 is squarefree (6 = 2·3), so Theorem 1 applies:
  **E[|Sel_6(E)|] = σ(6) = 12**    (BKLPR conditional).

How this value interlocks with n=6, σ=12, φ=2, τ=4 in the σφ=nτ theorem:
- σ(6)=12 is the mean size of Sel_6 (BKLPR).
- σφ=12·2=24=6·4=nτ is on a different numerical level, but **the number 12 shows up identically in both contexts**.
- This project's BT-546 treats this coincidence as a "structural knot" — a conditional observation.

### Universal perfect-number prediction
If n is a perfect number then σ(n) = 2n. Under the BKLPR model:
  **E[|Sel_n(E)|] = 2n** for perfect n.
Same universal formula for n = 6, 28, 496, 8128, ….
Caveat: n = 28 = 2²·7 is not squarefree. Theorem 1 has a squarefree assumption, so it does not apply directly to 28. Among perfect numbers, 6 is the only squarefree one (conjectural — existence of odd perfect numbers is open).

## 5. The BKLPR path (5 steps)

1. **Poonen-Rains random-matrix model assumption**:
   quadratic form on H^1(G_Q, E[p]), randomization of maximal isotropic subspaces.
2. **Compute Sel_n distribution in this model**:
   moment formula for |Sel_n| for squarefree n.
3. **Derive the expectation formula σ(n)**:
   E[|Sel_p|] = p + 1 → independence (A3) → E[|Sel_n|] = ∏(p+1) = σ(n).
4. **Apply CRT to squarefree 6**:
   by Lemma 1, |Sel_6| = |Sel_2|·|Sel_3| (direct decomposition).
5. **Conclude E[|Sel_6|] = σ(6) = 12**:
   E[|Sel_6|] = E[|Sel_2|]·E[|Sel_3|] = 3·4 = 12.
   σ(6) = 1+2+3+6 = 12. They agree.

## 6. The unique bottleneck A3 — independence assumption

The core non-trivial assumption of Theorem 1:
  **(A3) Under the BKLPR model, for distinct primes p, q, |Sel_p(E)| and |Sel_q(E)| are modeled as independent random variables.**

Status of this assumption:
- Unconditional CRT (Lemma 1) guarantees, for a **single elliptic curve** E, that Sel_p and Sel_q split as a direct decomposition (so their sizes multiply).
- A3 is the stronger claim, when taking **averages over an elliptic-curve family**, that the p-part and q-part are probabilistically independent.
- In the BKLPR paper, this is presented as an **axiom** of the model. There is partial agreement with data (compatible with Bhargava-Shankar's average-rank bound), but it is not itself a draft theorem.
- Hence Theorem 1 is conditional "if the BKLPR model is correct", and A3 is the weakest link of that model.

## 7. Sources

1. B. Poonen, E. Rains, "Random maximal isotropic subspaces and Selmer groups", J. AMS 25 (2012), 245–269. DOI: 10.1090/S0894-0347-2011-00710-8.
2. M. Bhargava, D. Kane, H.W. Lenstra Jr., B. Poonen, E. Rains, "Modeling the distribution of ranks, Selmer groups, and Shafarevich-Tate groups of elliptic curves", Cambridge J. Math. 3 (2015), 275–321.
3. H. Cohen, H.W. Lenstra Jr., "Heuristics on class groups of number fields", in: Number Theory Noordwijkerhout 1983, Springer LNM 1068 (1984), 33–62.
4. M. Bhargava, A. Shankar, "Binary quartic forms having bounded invariants, and the boundedness of the average rank of elliptic curves", Annals of Math. 181 (2015), 191–242. (background on average rank)
5. J. Silverman, "The Arithmetic of Elliptic Curves", GTM 106, Springer (2009), ch. X (Selmer groups).
6. memory/reference_bklpr_model.md (internal reference note of this project).

## 8. Follow-up

- P3-2: research methodology — how to observe E[|Sel_n|] statistics via LMFDB · Sage.
- P3-3: arithmetic-geometry frontier — possibility of geometric reinterpretation of the Selmer distribution via prismatic cohomology.
- In this project's BT-546, Theorem 1's Corollary is recorded as roadmap EMPIRICAL tier. Without breaking A3, it cannot be promoted past [7].
