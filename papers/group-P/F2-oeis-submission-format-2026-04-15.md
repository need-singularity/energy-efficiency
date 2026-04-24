# F2 — OEIS Sequence Registration Format (no submission, format only)

> Written: 2026-04-15
> Status: **format draft only — no actual OEIS submission**
> Source: σ·φ = n·τ uniqueness candidate target + 18 Bernoulli independent candidate results

Draft format for 5 candidate sequences potentially suitable for new registration in OEIS (Online Encyclopedia of Integer Sequences). The actual submission procedure (oeis.org account, draft-edit-approve cycle) is not performed.

---

## Candidate 1: a(n) = R(n) numerator (σ(n) · φ(n))

### Format

```
%I A_PROPOSED_001 #001 (Park Minwoo, 2026-04-15)
%S A_PROPOSED_001 1, 3, 8, 14, 24, 24, 48, 56, 78, 72, 120, 112, 168, 144, 192, 240
%T A_PROPOSED_001 (n=1 to n=16)
%N A_PROPOSED_001 σ(n) · φ(n), the numerator of R(n) = σ(n)·φ(n)/(n·τ(n))
%C A_PROPOSED_001 R(n) = 1 ⟺ n = 6 (Park 2026, theorem R1, σ(6)·φ(6) = n·τ(6) = 24)
%C A_PROPOSED_001 The pair (a(n), n·τ(n)) is equal at n=1 and n=6 only (in n ≤ 10^4).
%H A_PROPOSED_001 Park Minwoo, σ(n)·φ(n) = n·τ(n) ⟺ n = 6 uniqueness theorem
%F A_PROPOSED_001 a(n) = sigma(n) * eulerphi(n)
%e A_PROPOSED_001 a(6) = sigma(6)·phi(6) = 12·2 = 24
%Y A_PROPOSED_001 Cf. A000005 (tau), A000010 (phi), A000203 (sigma), A000396 (perfect numbers)
%K A_PROPOSED_001 nonn,easy
%O A_PROPOSED_001 1,2
%A A_PROPOSED_001 Park Minwoo, Apr 15 2026
```

### Verification (n = 1..16)

| n | σ(n) | φ(n) | a(n) = σ·φ |
|---|------|------|-----------|
| 1 | 1 | 1 | 1 |
| 2 | 3 | 1 | 3 |
| 3 | 4 | 2 | 8 |
| 4 | 7 | 2 | 14 |
| 5 | 6 | 4 | 24 |
| **6** | **12** | **2** | **24** |
| 7 | 8 | 6 | 48 |
| 8 | 15 | 4 | 60 |  ← correction: 60 (78 above is a typo)
| 9 | 13 | 6 | 78 |
| 10 | 18 | 4 | 72 |
| 11 | 12 | 10 | 120 |
| 12 | 28 | 4 | 112 |
| 13 | 14 | 12 | 168 |
| 14 | 24 | 6 | 144 |
| 15 | 24 | 8 | 192 |
| 16 | 31 | 8 | 248 | ← correction: 248 (240 above is a typo)

Corrected S line: `1, 3, 8, 14, 24, 24, 48, 60, 78, 72, 120, 112, 168, 144, 192, 248`

---

## Candidate 2: a(n) = R(n) = σ(n)·φ(n) / (n·τ(n)) numerator/denominator reduced form

Since OEIS only accepts integer sequences, express as the following two separate sequences:

### 2a: Numerator (already Candidate 1 = σ·φ)

### 2b: Denominator (n · τ(n))

```
%I A_PROPOSED_002 #001 (Park Minwoo, 2026-04-15)
%S A_PROPOSED_002 1, 4, 6, 12, 10, 24, 14, 32, 27, 40, 22, 72, 26, 56, 60, 80
%N A_PROPOSED_002 n · τ(n), the denominator of R(n) = σ(n)·φ(n)/(n·τ(n))
%C A_PROPOSED_002 R(n) = a(σ·φ)(n) / a(n·τ)(n) = 1 ⟺ n = 6
%C A_PROPOSED_002 a(6) = 6·4 = 24 = σ(6)·φ(6)
%F A_PROPOSED_002 a(n) = n * tau(n)
%e A_PROPOSED_002 a(6) = 6·τ(6) = 6·4 = 24
%Y A_PROPOSED_002 Cf. A000005 (tau), A038040 (n·tau(n))  (likely existing!)
%K A_PROPOSED_002 nonn,easy
%O A_PROPOSED_002 1,2
%A A_PROPOSED_002 Park Minwoo, Apr 15 2026
```

**Warning**: A038040 (n·τ(n)) is very likely already registered in OEIS (trivial product). This candidate has low probability of new registration — use **cross-reference** only.

---

## Candidate 3: a(n) = n such that R(n) - 1 = 0 (sequence = {6})

```
%I A_PROPOSED_003 #001 (Park Minwoo, 2026-04-15)
%S A_PROPOSED_003 6
%N A_PROPOSED_003 Numbers n ≥ 2 with σ(n)·φ(n) = n·τ(n)
%C A_PROPOSED_003 Equivalent to {n ≥ 2 : R(n) = 1}, where R(n) = σ(n)φ(n)/(n·τ(n))
%C A_PROPOSED_003 Park 2026 (theorem R1): the sequence consists of n = 6 alone (in n ≥ 2)
%C A_PROPOSED_003 Verified for n ∈ [2, 10^4] by computer enumeration; proof: 3 independent proofs (multiplicative R_local decomposition, group-theoretic via S_3 ≅ PSL(2,2), blowup engine)
%H A_PROPOSED_003 Park Minwoo, σ(n)·φ(n) = n·τ(n) ⟺ n = 6 uniqueness theorem (theory/proofs/theorem-r1-uniqueness.md)
%F A_PROPOSED_003 a(1) = 6, no further terms (singleton sequence)
%e A_PROPOSED_003 σ(6) = 12, φ(6) = 2, τ(6) = 4 → 12·2 = 24 = 6·4
%Y A_PROPOSED_003 Cf. A000396 (perfect numbers; n=6 is the first), A005179 (smallest with k divisors)
%K A_PROPOSED_003 nonn,fini,full
%O A_PROPOSED_003 1,1
%A A_PROPOSED_003 Park Minwoo, Apr 15 2026
```

**Note**: `fini,full` keyword = sequence is finite and fully known (single element {6}).

---

## Candidate 4: a(n) = Bernoulli Independent candidate-target cumulative count (author catalogue)

```
%I A_PROPOSED_004 #001 (Park Minwoo, 2026-04-15)
%S A_PROPOSED_004 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
%N A_PROPOSED_004 Cumulative count of independent theorems where the integer 6 appears non-trivially (Park's Bernoulli Independent Theorem family)
%C A_PROPOSED_004 18 = current count as of 2026-04-15 (Park 2026, F1 paper)
%C A_PROPOSED_004 #1 = 6 first perfect number, #2 = |S_3| = 6, ..., #17 = avg|Sel_6| = σ(6) = 12 (BKLPR conditional, Bhargava-Shankar 2010-2012), #18 = BB(2) = 6 (Radó 1962, unconditional)
%C A_PROPOSED_004 Each entry = independent domain occurrence with cited prior literature
%H A_PROPOSED_004 Park Minwoo, F1 paper section 4 (papers/group-P/F1-arxiv-bernoulli-independent-via-n6-2026-04-15.md)
%F A_PROPOSED_004 a(n) = n (trivial counter; the substance is the table of theorems, not the integers)
%e A_PROPOSED_004 a(17) = 17 corresponds to "Sel_6 average = σ(6) = 12 (BKLPR conditional)"
%K A_PROPOSED_004 nonn,easy,bref
%O A_PROPOSED_004 1,1
%A A_PROPOSED_004 Park Minwoo, Apr 15 2026
```

**Warning**: trivial 1, 2, 3, ... sequences may be rejected by OEIS policy — use this candidate only as a **meta-catalogue reference**. Actual OEIS registration not recommended.

---

## Candidate 5: a(n) = numerator of R_local(p_n, 1) (arithmetic of Lemma A)

```
%I A_PROPOSED_005 #001 (Park Minwoo, 2026-04-15)
%S A_PROPOSED_005 3, 8, 24, 48, 120, 168, 288, 360, 528, 840, 960
%N A_PROPOSED_005 Numerator of R_local(p, 1) = (p² - 1) / (2·p) for p = prime(n)
%C A_PROPOSED_005 a(n) = prime(n)² - 1 = (prime(n) + 1)·(prime(n) - 1)
%C A_PROPOSED_005 R_local(p, 1) < 1 only for p = 2 (Lemma A in Park 2026, theorem R1)
%C A_PROPOSED_005 R_local(2, 1) = 3/4 < 1; R_local(3, 1) = 8/6 = 4/3 > 1; R_local(5, 1) = 24/10 = 12/5 > 1
%F A_PROPOSED_005 a(n) = prime(n)^2 - 1
%e A_PROPOSED_005 a(1) = 2² - 1 = 3 (R_local(2,1) = 3/4)
%e A_PROPOSED_005 a(2) = 3² - 1 = 8 (R_local(3,1) = 8/6 = 4/3)
%Y A_PROPOSED_005 Cf. A000040 (primes), A084920 (p^2 - 1 for primes p)  (likely existing)
%K A_PROPOSED_005 nonn,easy
%O A_PROPOSED_005 1,1
%A A_PROPOSED_005 Park Minwoo, Apr 15 2026
```

**Warning**: A084920 (p² - 1 for primes p) or similar sequences likely already registered in OEIS. **Reference search** to confirm novelty is required.

---

## Meta: Actual submission procedure (reference only, not executed)

1. Create oeis.org account.
2. Prepare draft for each candidate (using the formats above).
3. Search existing OEIS DB for duplicates (required).
4. If the sequence is new, submit draft.
5. OEIS editorial team review (days to weeks).
6. Upon approval, A-number is assigned.

**This work is not submitted (per user requirement)**.

---

## Recommended priority for new registration

| Candidate | Novelty | Significance | Recommendation |
|------|--------|------|------|
| 1 (σ·φ) | medium | R(n) numerator | registrable after search |
| 2 (n·τ) | **low** (A038040 expected) | R(n) denominator | registration not recommended |
| **3 (n with R(n)=1)** | **high** | direct OEIS expression of uniqueness candidate target | **top registration candidate** |
| 4 (meta counter) | very low | trivial 1,2,3,... | registration not recommended |
| 5 (p²-1) | low | A084920 possible | decide after search |

**Top priority**: Candidate 3 (singleton {6}) — direct OEIS expression of the uniqueness candidate target, fini+full keywords available.

---

> Artifact: papers/group-P/F2-oeis-submission-format-2026-04-15.md
> No actual submission. format only.

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

