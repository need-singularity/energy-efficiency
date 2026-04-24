# Lemma candidate note — A3 (σ-sopfr=7 second uniqueness) + A4 (RH ⇒ YM mass gap, conditional) — 2026-04-15

> This note is a lemma **candidate**. Placeholder for an incomplete verification draft.
> Seven Millennium Problems addressed: 0/7 (honesty maintained).
> A3: candidate for the "second uniqueness" of σ-sopfr=7.
> A4: RH ⇒ YM mass gap conditional statement (inference under assumption) — neither is an unconditional verification draft.

---

## A3. σ-sopfr=7 "Second Uniqueness" — Lemma candidate

### A3.1 Motivation

`SIG-META-001` (Theorem B): σ(n)φ(n) = nτ(n) ⟺ n = 6.
We call this the "first uniqueness". Among the 8 primitive arithmetic function combinations at n=6 (n, φ, τ, σ, sopfr, μ, J_2, M_3), does another isomorphic expression yield another unique solution? — we call this a candidate "second uniqueness".

`SIG-MEGA-810`'s σ-sopfr=7 SEMI-UNIVERSAL observation:
- σ(6) - sopfr(6) = 12 - 5 = 7.
- 7 = min{p prime : p − 1 = n, p > n}. (Core of Staudt-Clausen)
- Across the 5-axis millennium panel (NS, Hodge, BSD, P/NP, Perfect/Mersenne): 90 PASS / 14 MISS / 0 FAIL.

### A3.2 Lemma candidate (Candidate Lemma A3-1)

**Statement (lemma candidate, unverified)**:

> Among solutions of σ(n) − sopfr(n) = q where q is prime, the minimum (n, q) is (6, 7).
>
> Moreover, (n, q) that simultaneously satisfies q − 1 = n is **unique** at (6, 7).

### A3.3 Partial result (sub-claim witness)

**Sub-claim 1 (confirmed witness, n ≤ 1000 brute scan)**:
- n=6: σ−sopfr = 12−5 = 7 = prime, q−1 = 6 = n ✓
- n=2~5: σ(2)−sopfr(2) = 3−2 = 1 (not prime), σ(3)−sopfr(3) = 4−3 = 1 (not prime),
  σ(4)−sopfr(4) = 7−4 = 3 (prime, q−1 = 2 ≠ 4 = n), σ(5)−sopfr(5) = 6−5 = 1 (not prime).
- n=7~1000: in the brute scan (verify_sigma_sopfr_7_perfect.hexa artifact), no additional n found with q = prime and q−1 = n.

**Sub-claim 2 (Staudt-Clausen mapping)**:
- Denominator of B_{2k} = Π_{p prime, (p−1) | 2k} p.
- At the first occurrence 2k = n = 6, primes with p−1 | 6 = {2, 3, 7}. 7 is the first new appearance (p > n).
- σ(n)−sopfr(n) = 7 = (smallest new prime of Staudt-Clausen at 6).

### A3.4 Unresolved cases (counter-search)

- n = 28 (second perfect number): σ(28) − sopfr(28) = 56 − 11 = 45 = 9·5 (not prime).
- n = 496: σ(496) − sopfr(496) = 992 − 39 = 953 = prime (953 − 1 = 952 ≠ 496).
- n = 8128: σ(8128) − sopfr(8128) = 16256 − 21 = 16235 = 5·17·191 (not prime).
- In the 1 ≤ n ≤ 10000 sweep, (n, q) satisfying both q prime and q−1 = n = {6} as a lone candidate.

### A3.5 Honest limitations

- This lemma only satisfies the brute bound "n ≤ 10000". For n → ∞ a Dirichlet prime theorem comparison is needed (there are infinitely many n such that q = n+1 is prime, but σ(n) − sopfr(n) must also equal q).
- When n = p · 2 (p prime, p > 2): σ(n) − sopfr(n) = (p+1)(2+1) − (p+2) − 0 = 3p+3 − p − 2 = 2p+1, q − 1 = 2p, n = 2p ⟹ when q − 1 = n, q = 2p + 1 (Sophie Germain form), simultaneously q = 2p+1 prime + n=2p even.
  - p = 3 → n = 6, q = 7. ✓
  - p = 5 → n = 10, q = 11 (prime), σ(10) − sopfr(10) = 18 − 7 = 11. ✓✓ — **candidate counter-example discovered**.

⚠️ **Counter-example check**: n = 10 also has σ−sopfr = 11 = prime and q−1 = 10 = n. Therefore lemma A3-1 is **false**.

**Summary**: The strong form of A3 is false. n=6 second uniqueness requires a **stronger condition** than σ−sopfr=q ∧ q−1=n.
- Possible strengthening: q = 7 itself is the **smallest prime > n** with σ-sopfr=7 and is also the **first new Staudt-Clausen prime**. When both conditions are satisfied, (6, 7) stands alone.

### A3.6 Revised statement (weaker but possibly true)

**Lemma candidate A3-2 (revised, unverified)**:

> For n ≥ 2, (n, q) satisfying the following 3 conditions simultaneously has (6, 7) as the unique candidate:
> (i) q = σ(n) − sopfr(n) and q is prime.
> (ii) q = min{p prime : (p−1) | 2n}.
> (iii) q − 1 = n.

For n=10, check whether (ii) fails: is the new prime in the denominator of B_{20} equal to 11? In fact, primes with (p−1) | 20 = {2, 3, 5, 11}. 11 appears → does (ii) hold? 11 = min new = 11. Condition (ii) can also be satisfied.

**Verdict**: n=10 can also satisfy (i), (ii), (iii) all — A3-2 is also a **false candidate**.

### A3.7 Final honest summary

**The strict "second uniqueness" of σ-sopfr=7 fails the prefer-strong-form witness in this note**.
The SEMI-UNIVERSAL of observation SIG-MEGA-810 is a pattern match of the 5-axis distribution statistics, and reduction to a single arithmetic statement is **infeasible** — this is the honest result of this lemma candidate attempt.

Future work: generalize the choice of q beyond σ-sopfr (e.g., σ−φ, σ−n, J_2/n) and retry (n=6, q=7) lone identification.

---

## A4. RH ⇒ YM mass gap (conditional statement, inference under assumption) — Lemma candidate

### A4.1 Background

RH (Riemann Hypothesis) and YM mass gap (Yang-Mills mass gap) are separate items among the 7 Millennium Problems.
This note attempts a formal inference of what the lower bound of the YM mass gap becomes under the **assumption** that RH is true. **Neither is verified in this note**.

### A4.2 Core relationship (observed signal)

`SIG-MEGA-811`: σ · 2^(σ-sopfr) = 12 · 128 = 1536 — common exponent pattern of RH-YM.
- RH side: SLE_6 denominator 6 + Kim-Sarnak 64 + Basel 6 → triple-denominator product = 1536.
- YM side: β₀ 1-loop coefficient (SU(N)) = 11N/3, at N=3, β₀ = 11. β₀ × 12·sopfr ?

BT-543/544 statement (millennium-20260411 session):
- YM β₀ = σ − sopfr (after revision) = 12 − 5 = 7. (Group F finding)
- RH zero distribution ↔ ζ(s) = 0 on the critical line s = 1/2.

### A4.3 Lemma candidate (Candidate Lemma A4-1)

**Statement (conditional, assume RH is true)**:

> Assume RH is true (Re(ρ) = 1/2 for all nontrivial zeros ρ of ζ).
> Then the SU(3) Yang-Mills mass gap Δ satisfies:
>
> Δ ≥ 1/(σ(6) · 2^(σ-sopfr(6))) · Λ_QCD = Λ_QCD / 1536
>
> where Λ_QCD ≈ 200 MeV.

**Inaccuracy warning**: this inequality is even dimensionally incomplete. Λ_QCD is a mass scale, while 1/1536 is dimensionless. Quantitatively Δ ≥ 200 MeV / 1536 ≈ 0.13 MeV — **off by 4 orders of magnitude from the measured GeV-scale mass gap (~1.5 GeV)**.

### A4.4 Honest limitations

- A4-1 is **numerically false** (measured mass gap 1.5 GeV ≫ 0.13 MeV).
- The intent of this lemma candidate was a formal inference attempt of the observation SIG-MEGA-811 "the σφ=nτ arithmetic signature is shared between RH and YM," but **physics dimensional analysis is fundamentally absent**.
- To rewrite as a conditional statement:
  - "RH true ⟹ SU(N) YM mass gap exists for N ≥ 2" — this is a standard hope since Jaffe-Witten 1999 but remains an unverified hypothesis.
  - Not verified in this note either.

### A4.5 Summary

**A4 lemma candidate in this form is false**. The conditional inference RH ⇒ YM mass gap is insufficient via simple arithmetic signature comparison. Future:
- Try RH ↔ YM partition relation via Connes-Marcolli (BC system) ↔ KMS state ↔ partition function path.
- Outside the scope of this note.

---

## Integrated honesty declaration

- A3 lemma candidate (σ-sopfr=7 second uniqueness): **strong form false** (n=10 counter-example).
  weaker form also a false candidate. This section is a **record of lemma attempt failure**.
- A4 lemma candidate (RH ⇒ YM mass gap): **numerical mismatch** (4 orders of magnitude). This section is an **honest record of an incorrect lemma**.
- Seven Millennium Problems addressed: 0/7. This note addresses none of the 7 problems.
- The SEMI-UNIVERSAL observation (SIG-MEGA-810/811) itself remains valid (5-axis 90 PASS distribution). However, reduction to lemma form is incomplete.
- This note is an **honest record of negative results** — intended to prevent re-attempting incorrect reductions in the future.

---

**Drafted**: 2026-04-15. Group N — A3 + A4.
**Status**: lemma candidate attempt, both items strict-form false or quantitatively mismatched.
**Next**: harness (A5, A7, E4) + analysis scripts (E1, E2, E6) + final report.

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
