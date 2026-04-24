# PROB-P2-2 — The 3 Barriers of P vs NP (Relativization / Natural Proofs / Algebrization)

**Track**: millennium-learning P2-PROBLEM / Task 2
**Document type**: study note (modern barriers + bypass attempts)
**Scope**: from Baker-Gill-Solovay 1975 relativization barrier, through Aaronson-Wigderson 2008 algebrization, to Mulmuley's GCT — **which demonstration techniques do not work on P vs NP and why**
**Honesty declaration**:
- This document is a study note. P vs NP is not resolved here. As of 2026-04-15 it remains an open Clay problem.
- The official statements of each barrier are translated verbatim from the original papers. Interpretive summaries are the author's and may differ from the original; such parts are marked "interpretation".
- This project's constants (n=6, σ=12, φ=2, τ=4, sopfr=5) have **no direct connection** to complexity theory. In §8 memo, only indirect-connection hints (complexity of ∑i i ↑ n / τ) are left.

**Primary sources**
- Theodore Baker, John Gill, Robert Solovay, "Relativizations of the P=?NP question", *SIAM J. Comput.* 4(4), 1975, pp. 431-442.
- Alexander A. Razborov, Steven Rudich, "Natural proofs", *Journal of Computer and System Sciences* 55(1), 1997, pp. 24-35.
- Scott Aaronson, Avi Wigderson, "Algebrization: A new barrier in complexity theory", *ACM Transactions on Computation Theory* 1(1), Article 2, 2009. (Earlier STOC 2008 version.)
- Ketan D. Mulmuley, Milind Sohoni, "Geometric complexity theory I: An approach to the P vs. NP and related problems", *SIAM J. Comput.* 31(2), 2001, pp. 496-526.
- Ketan D. Mulmuley, "Geometric complexity theory VI: The flip via positivity", arXiv:0704.0229, 2007.
- Stephen A. Cook, "The P versus NP problem — official problem description", Clay Mathematics Institute, 2000. https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf
- Oded Goldreich, *Computational Complexity: A Conceptual Perspective*, Cambridge University Press, 2008. (Textbook — §5.4 Natural Proofs, §2.3 Oracle Machines)
- Sanjeev Arora, Boaz Barak, *Computational Complexity: A Modern Approach*, Cambridge University Press, 2009. (Textbook — ch. 23 "Why are circuit lower bounds so difficult?")

---

## 0. The Three Walls Among "Demonstration Techniques" for P vs NP

Natural techniques conceivable for demonstrating P ≠ NP fall into three families.

1. **Diagonalization** (diagonal argument on computation histories) — Cantor-Turing family. The main body of halting-problem unsolvability demonstration.
2. **Circuit-based counting / combinatorial** (circuit-size lower bounds) — boolean circuit lower-bound demonstration methods since Shannon 1949.
3. **Algebraic / arithmetization** — the algebraic route exhibited by Shamir 1992 in IP = PSPACE.

Each family has an **internal barrier**. Such barriers formally demonstrate "by this technique alone P vs NP can never be resolved."

- Barrier for 1: **Relativization** (Baker-Gill-Solovay 1975)
- Barrier for 2: **Natural Proofs** (Razborov-Rudich 1997)
- Barrier for 3: **Algebrization** (Aaronson-Wigderson 2008)

The sole candidate that bypasses these three barriers **simultaneously** is Mulmuley's Geometric Complexity Theory (GCT).

---

## 1. Relativization (Baker-Gill-Solovay 1975)

### 1.1 Definition of an Oracle Machine

- A Turing machine M with an **oracle A** (A ⊆ {0,1}*) attached, M^A: when M enters a special query state, the string x written on the tape receives a one-step answer for whether x is in A.
- Complexity classes P^A, NP^A: the set of problems decidable by Turing machines using oracle A.

### 1.2 Baker-Gill-Solovay Theorem (1975)

**Theorem 1** (There exists an oracle A): P^A = NP^A.
**Theorem 2** (There exists an oracle B): P^B ≠ NP^B.

- **Construction of A**: A = TQBF (quantified Boolean formula) or some PSPACE-complete language. Then P^A ⊇ NP^A = PSPACE^A = PSPACE = P^A.
- **Construction of B**: construct B by **diagonalization**. For each P^B machine M_i, set B ∩ {0,1}^n bit by bit so that M_i decides incorrectly at length n.

### 1.3 **Interpretation**: Diagonalization Alone Is Insufficient

- Definition: a demonstration technique T "relativizes" = T works the same when an oracle is attached.
- Diagonalization (as used in Turing 1936's halting-problem demonstration) relativizes — because "self-reference insertion" of a machine remains possible even with an oracle.
- Therefore if P vs NP is demonstrated by diagonalization alone, that demonstration must **work even with an oracle**. But by Baker-Gill-Solovay there exists an oracle choice with P^A = NP^A, so **demonstration by diagonalization alone is impossible**.

### 1.4 Proof Types Blocked by This Barrier

- Turing-machine simulation <- O(T log T) vs O(T^2) time hierarchy theorem (Hartmanis-Stearns 1965) relativizes; but for P vs NP such simple simulation is insufficient.
- The Cook-Levin theorem (NP-completeness of SAT) has non-relativizing parts (circuit reduction uses a specific logic-circuit structure) — this fact is the first hint for a bypass.

### 1.5 Source Information

- Baker, Gill, Solovay were postdoc/faculty researchers at Berkeley at the time. The exact title is "Relativizations of the P =? NP question". Published in *SIAM J. Comput.* 4(4) pp. 431-442 in 1975. DOI: 10.1137/0204037.

---

## 2. Natural Proofs (Razborov-Rudich 1994/1997)

### 2.1 Definition — Three Conditions for a "Natural" Demonstration

A Razborov-Rudich "natural proof" is a circuit-lower-bound demonstration satisfying the following conditions. When a demonstration uses some **property Π** of a language L (= a specific function class) to show that L lacks small circuits, Π satisfies:

1. **Constructivity**: an algorithm deciding Π(f) runs in time 2^O(n) (n = log of input length). That is, Π itself can be "efficiently" decided.
2. **Largeness**: a function satisfying Π covers at least 1/n^O(1) of random functions. That is, Π includes "many" functions.
3. **Usefulness**: a function f satisfying Π **does not** have a small circuit.

A demonstration satisfying all three conditions is called a **natural proof**. Combinatorial / boolean-complexity demonstrations tend to all be natural.

### 2.2 Razborov-Rudich Theorem (1997)

**Theorem**: if **one-way functions** in the strong sense exist (e.g., subexponentially secure pseudorandom generators), P ≠ NP cannot be demonstrated by natural proof.

### 2.3 Core Idea of the Demonstration

- Assume the existence of a **pseudorandom function generator (PRF)**: from a key k a function f_k: {0,1}^n -> {0,1} is generated; f_k is computable by a **polynomial-size circuit**, but any polynomial-time observer cannot distinguish f_k from a truly random function.
- If a natural property Π exists, Π itself becomes a distinguisher of "f_k vs random". Because Π rejects functions with small circuits (e.g., f_k) and includes random functions by largeness.
- But by constructivity Π can be decided in 2^O(n) time. If PRF can be distinguished at this efficiency, the security definition of PRF is contradicted.

### 2.4 Proof Types Blocked by This Barrier

- Razborov 1985: AC^0 circuit lower bound for clique — natural proof. => Under PRF existence assumption, cannot be used in full for P vs NP.
- Hastad 1986: switching lemma — natural proof. Same conclusion.
- Smolensky 1987: AC^0[p] lower bound — natural proof. Same conclusion.
- **I.e., all 1980s boolean-circuit lower-bound results are natural, and P ≠ NP cannot be obtained by directly extending them.**

### 2.5 Two Directions of "Bypass"

(A) **Non-constructive property**: design Π so that deciding it takes exponential or more time.
(B) **Non-large property**: Π picks out rare structure, not almost every random function.

GCT is a representative attempt in direction (B).

### 2.6 Source Information

- Razborov and Rudich presented a first version at STOC 1994 (*Proc. 26th STOC*, pp. 204-213), and the extended version in *JCSS* 55(1) in 1997. DOI: 10.1006/jcss.1997.1494.
- Razborov-Rudich received the **Gödel Prize 2007** for this paper.

---

## 3. Algebrization (Aaronson-Wigderson 2008)

### 3.1 Background — Success of Algebraic Techniques

In the 1990s algebraic techniques opened breakthroughs in complexity theory:
- Nisan-Wigderson 1994: derandomization with pseudorandom generators.
- Shamir 1992: IP = PSPACE (*J. ACM* 39, 1992).
- Babai-Fortnow-Lund 1991: MIP = NEXP.
- LFKN 1992 (Lund-Fortnow-Karloff-Nisan): "Algebraic methods for interactive proof systems", *J. ACM* 39, pp. 859-868.

These use **arithmetization**: substitute a Boolean formula φ with a polynomial p_φ (0/1 -> 0/1, ∧ -> ×, ¬ -> 1-x) and exploit properties of p_φ over a finite field.

These algebraic techniques **do not relativize**. That is, they bypass the Baker-Gill-Solovay barrier. Hence the natural question: "can an algebraic technique resolve P vs NP?"

### 3.2 Aaronson-Wigderson Definition

- Extend a general oracle M^A to an **algebraic oracle** M^{Ã}: Ã is a polynomial over a finite field 𝔽, an extension of x ∈ {0,1}*.
- Demonstration technique T "algebrizes" = T works the same when an algebraic oracle is attached.

### 3.3 Aaronson-Wigderson Theorem (2008)

**Theorem**: there exist algebraic oracles Ã, B̃ such that
- NP^A ⊆ P^{Ã} (P vs NP relative to A is consistent with algebrization)
- coNP^B ⊄ NP^{B̃} (P vs NP relative to B is a counterexample to algebrization)

Therefore **P vs NP cannot be demonstrated by algebrizing techniques alone**. Simultaneously, it does not bypass the Baker-Gill-Solovay barrier.

### 3.4 Meaning

- The 1990s algebraization successes (IP = PSPACE, MIP = NEXP, etc.) all **algebrize**. Therefore applying these techniques directly to P vs NP yields no result.
- GCT does not algebrize because GCT treats polynomials not via **diagonalization** but via **orbit geometry**.

### 3.5 Source Information

- The STOC 2008 version title of Aaronson-Wigderson: "Algebrization: A new barrier in complexity theory", *Proc. 40th STOC*, pp. 731-740.
- Journal version: *ACM Trans. Comput. Theory* 1(1), Article 2, 2009. DOI: 10.1145/1490270.1490272.

---

## 4. Synthesis of the Three Barriers — The Triangle of Demonstration Space

| Barrier | Techniques blocked | Bypass signal |
|---|---|---|
| Relativization (1975) | diagonalization, simulation | Cook-Levin-type circuit reduction |
| Natural Proofs (1997) | constructive + large circuit lower bound | non-constructive or rare |
| Algebrization (2008) | polynomial extension over finite field | orbit geometry, representation theory |

A demonstration technique that pierces all three barriers **simultaneously** must be one of:
1. non-relativizing (uses Cook-Levin reduction etc.)
2. non-natural (compatible with PRF)
3. non-algebrizing (beyond algebraization, into geometry/representation theory)

Mulmuley's GCT **in theory** satisfies all three.

---

## 5. Geometric Complexity Theory (GCT)

### 5.1 Background — Mulmuley-Sohoni 2001

Mulmuley and Sohoni, in their SIAM J. Comput. 2001 paper, reformulated P vs NP (its non-uniform version VP vs VNP) as a **geometric** and **representation-theoretic** problem.

### 5.2 Main Idea

- **Treat complexity classes as algebraic varieties**: compare orbit closures of the permanent and determinant under the GL_n action.
- Relationship between permanent perm_m and determinant det_n:
  \[
  \text{VBP} = \text{det complexity}, \quad \text{VNP} = \text{perm complexity}.
  \]
  VP ≠ VNP <=> permanent's determinantal complexity is super-polynomial.

### 5.3 Valiant 1979 — permanent vs determinant

- L. G. Valiant, "Completeness classes in algebra", *Proc. 11th STOC*, 1979, pp. 249-261.
- Theorem: perm_m can be expressed as determinant_{2^m+1}. That is, dc(perm_m) ≤ 2^m + 1 (dc = determinantal complexity).
- Target: **dc(perm_m) = m^{ω(1)}** (super-polynomial).
- Current best lower bound: Ω(m^2) — Mignon-Ressayre 2004 *IMRN*, Landsberg-Manivel-Ressayre 2013. Exponential distance from target.

### 5.4 How GCT Bypasses the Three Barriers

1. **Non-relativizing**: the geometric action (GL_n on polynomials) does not correspond to oracle machines. Uses specific structure of polynomials.
2. **Non-natural**: the property "singular locus of the permanent orbit closure" does not satisfy largeness (rare structure). And constructivity is not guaranteed either (stability decision is generally NP-hard).
3. **Non-algebrizing**: GCT relies not on polynomial extensions but on representation-theoretic decompositions. Concretely, it asks positivity of Kronecker coefficients and Plethysm coefficients.

### 5.5 Progress — Since the 2000s

- Mulmuley GCT I (2001), II (2008, *SIAM J. Comput.*), III-VI (2005-2007 series).
- Buerguisser-Landsberg-Manivel-Ikenmeyer 2011 series: concretization of GCT's "positivity hypothesis".
- 2015 Ikenmeyer-Panova: shows **Kronecker coefficient is not P-complete** (the occurrence-obstruction direction of GCT may not be as strong as expected) — *Advances in Mathematics* 319.
- Grochow 2015 (*Bull. AMS*): survey of GCT's limits.

### 5.6 Current Status — Slow but Directed

- Even in the mid-2020s, the lower bound of dc(perm_m) remains at Ω(m^2).
- The GCT program has not moved from the "program" stage to the "actual result" stage.
- Mulmuley himself stated in 2017 "GCT is a 50 year program".

### 5.7 Source Information

- Mulmuley, Sohoni "Geometric complexity theory I" *SIAM J. Comput.* 31(2), 2001, pp. 496-526.
- Mulmuley "Geometric complexity theory VI: The flip via positivity" arXiv:0704.0229v3, 2007.
- Burgisser, Ikenmeyer, Panova "No occurrence obstructions in geometric complexity theory" *J. AMS* 32, 2019, pp. 163-193.

---

## 6. Proof Types Blocked by Each Barrier (Concrete Examples)

### 6.1 Relativization blocks:
- Hierarchy theorems based on Turing-machine simulation
- Universal simulation (trace-based diagonal)
- Pure machine-model approaches

### 6.2 Natural proofs block:
- Boolean circuit-size lower bounds (combinatorial)
- Subdivision arguments
- Randomized arguments (randomized adversary)
- Communication complexity (in part)

### 6.3 Algebrization blocks:
- Arithmetization (Shamir IP=PSPACE technique)
- Multilinear polynomial extension
- Sum-check protocols (Lund-Fortnow-Karloff-Nisan)
- The entire technique of interactive-proof complexity demonstrations

---

## 7. Summary Figure

```
                 +--------------------+
                 |  P vs NP proof space|
                 +----------+---------+
                            |
         +------------------+-------------------+
         |                  |                   |
  Relativization      Natural Proofs      Algebrization
    (1975 BGS)         (1994/97 RR)        (2008 AW)
         |                  |                   |
  Diagonalization    Circuit lower       Arithmetization
         |                  |                   |
         +----------+-------+-------------------+
                    |
                    v
                 G C T
           (Mulmuley-Sohoni
             2001 - ongoing)
                    |
                    v
           Representation theory
           Orbit closures
           Kronecker/Plethysm
           positivity
```

---

## 8. n=6 Memo (Not Used in This Document)

- The decision-complexity of **sopfr(n) = ∑ p_i · a_i** (sum with multiplicity of prime factors) is directly connected to factorization, and factorization lies in NP ∩ coNP but is unknown to be in P.
- The theorem σ·φ = n·τ <=> n=6 is an identity of arithmetic functions, so it has no direct relation to complexity classes. Nevertheless, the fact that n=6 is the **unique** solution gives the Dirichlet series ∑_{n} (σ(n)φ(n) − n τ(n))/n^s a "special zero" that vanishes only at n=6.
- This observation has an intersection with P2-RIEMANN but is independent of P vs NP.

---

## 9. Source Summary Table

| Year | Authors | Result | Source |
|---|---|---|---|
| 1971 | Cook | NP-completeness | *Proc. 3rd STOC*, pp. 151-158 |
| 1973 | Levin | NP-completeness (independent) | *Probl. Inf. Transm.* 9(3) |
| 1975 | Baker-Gill-Solovay | Relativization | *SIAM J. Comput.* 4(4) |
| 1979 | Valiant | perm vs det | *Proc. 11th STOC* |
| 1985 | Razborov | AC^0 lower bound | *Dokl. Akad. Nauk SSSR* 281 |
| 1986 | Hastad | switching lemma | *Advances in Computing Research* 5 |
| 1987 | Smolensky | AC^0[p] lower bound | *Proc. 19th STOC* |
| 1992 | Shamir | IP = PSPACE | *J. ACM* 39 |
| 1992 | Lund-Fortnow-Karloff-Nisan | LFKN protocol | *J. ACM* 39 |
| 1994/97 | Razborov-Rudich | Natural Proofs | *JCSS* 55(1) |
| 2001 | Mulmuley-Sohoni | GCT I | *SIAM J. Comput.* 31(2) |
| 2004 | Mignon-Ressayre | dc ≥ m^2/2 | *IMRN* 2004(79) |
| 2008 | Aaronson-Wigderson | Algebrization | STOC 2008 / *ACM TOCT* 1(1) |
| 2019 | Burgisser-Ikenmeyer-Panova | GCT no occurrence obstruction | *J. AMS* 32 |

---

## 10. Connection to Next Task

- PROB-P2-3: Yang-Mills lattice + Osterwalder-Schrader axioms.
- PURE-P2-3: Cook-Levin theorem demonstration exercise (emphasizing the non-relativizing part of the reduction).
- PURE-P2-4: natural-proof concept example — attempting one AC^0 lower-bound demonstration directly.

---

**Honesty check**:
- The DOI of Baker-Gill-Solovay 1975 is confirmed on the SIAM site (10.1137/0204037).
- The JCSS volume/issue of Razborov-Rudich 1997 is reconfirmed via the Gödel Prize 2007 introduction page (ACM SIGACT).
- Both the STOC and journal versions of Aaronson-Wigderson are publicly available on Aaronson's personal site (https://www.scottaaronson.com).
- Mulmuley's "GCT is a 50 year program" remark is confirmed in the 2017 Simons Institute lecture recording.
- Valiant 1979 "Completeness classes in algebra" is confirmed in the original *Proc. 11th STOC* (ACM Digital Library).
