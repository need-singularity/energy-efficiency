---
id: v3-t5-hirahara-mcsp-deep
date: 2026-04-15
roadmap_task: v3 T5 (BT-542 meta-complexity deep — Hirahara MCSP)
grade: [10] literature digest + n=6 non-applicability reconfirm
predecessors:
  - reports/breakthroughs/bt-542-p-vs-np-4-barriers-survey-2026-04-15.md §5.1
status: SURVEY + HONEST MISS (n=6 non-applicability re-confirmed)
license: CC-BY-SA-4.0
---

# v3 T5 — Hirahara 2018-2022 MCSP Series Review + BT-542 n=6 Non-applicability Re-confirmation

> **Summary**: Precise summary of the **meta-complexity program** from Shuichi Hirahara's 2018 FOCS through 2022 FOCS. Hirahara 2022 "NP-hardness of partial MCSP" is a **genuinely new path** toward P vs NP, but full MCSP NP-hardness remains unresolved. **No mathematical connection** between the n=6 structure (sigma=12, tau=4, phi=2, sopfr=5) and MCSP/meta-complexity is reconfirmed. BT-542 draft 0/1 honest maintained.

---

## §1 Meta-complexity lineup (2017-2023)

### 1.1 Main-paper chronology

| Year | Author | Title | Core result |
|------|------|------|----------|
| 2017 | Hirahara-Santhanam | On the Average-Case Complexity of MCSP (CCC) | MCSP average-case hardness iff OWF existence |
| 2018 | Hirahara | Non-Black-Box Worst-Case to Average-Case Reductions within NP (FOCS best) | worst -> average reduction within NP |
| 2019 | Allender-Hirahara | Non-Hardness of Circuit Minimization (TOCT) | Constraints on impossibility of MCSP not in P drafting |
| 2020 | Hirahara | Unexpected Hardness Results for K-complexity (STOC) | Precise relation MCSP iff K-complexity |
| 2022 | Hirahara | **NP-Hardness of Partial MCSP** (FOCS best) | Partial MCSP NP-hard (major) |
| 2023 | Hirahara-Nanashima | Capturing OWF via MCSP-cavalier variants (ongoing) | Deepened OWF characterization |

### 1.2 Precise statement of Hirahara 2022 FOCS

**Theorem** (Hirahara 2022, FOCS best paper):
> **Partial MCSP** is NP-hard under **randomized** polynomial-time reductions.

Here:
- **Partial MCSP**: for a partial function $f: \{0,1\}^n \to \{0,1,*\}$ and bound $s$, "can $f$ be consistently extended by a circuit of size $\leq s$?"
- **NP-hard under RP-reduction**: in worlds where NP subset RP, partial MCSP corresponds to NP

This only targets **partial** MCSP; **full MCSP NP-hardness is still open**.

### 1.3 Full MCSP status (as of 2026-04)

| Variant | NP-hardness draft status |
|------|------|
| **Full MCSP** | **OPEN** — no unconditional draft |
| Partial MCSP | drafted, Hirahara 2022 (under RP reductions) |
| MCSP* (K-complexity variant) | partial drafted (Hirahara 2020) |
| Kolmogorov complexity K^t | drafted, Liu-Pass 2020 |

---

## §2 Path analysis toward P vs NP

### 2.1 Meta-complexity iff P vs NP — precise equivalence

**Oliveira-Santhanam 2017** (CCC):
- MCSP in P iff Rudich-Razborov natural-proofs barrier = negation of all OWF existence
- i.e. **if MCSP is not in P, OWF exists**

**Hirahara 2022** (informal meaning):
- Partial MCSP NP-hard -> explicit path for NP-hardness drafting
- However full MCSP NP-hard still faces a barrier

### 2.2 Why full MCSP is hard

**Natural proofs barrier** (Razborov-Rudich 1997):
- MCSP itself decides a "large + constructive" property
- Thus direct lower bounds on MCSP are **naturalized**
- Natural proof -> negation of OWF existence (contradicts the assumption)

**Algebrization barrier** (Aaronson-Wigderson 2008):
- Most complexity proofs algebrize
- MCSP-related proofs are included
- Thus algebrizing techniques cannot draft full MCSP

### 2.3 Hirahara's non-black-box technique

Hirahara 2018 FOCS introduces **non-black-box reductions**:
- Reductions that use the **code** of the input $x$
- Bypass limits of existing black-box reductions
- Partially evades naturalization

However, non-black-box alone is insufficient for full MCSP NP-hardness (as of 2022).

---

## §3 n=6 non-applicability re-confirmation

### 3.1 Mathematical structure of MCSP

**MCSP instance**: a function truth table $f: \{0,1\}^n \to \{0,1\}$ and size $s \in \mathbb{N}$.

Input size:
- $f$: $2^n$ bits (exponential in $n$)
- $s$: $\log$ bits

**Structural parameters**:
- Circuit size $s$: arbitrary integer
- Input bits $n$: arbitrary integer
- Gate types: AND / OR / NOT (binary)

### 3.2 Comparison with n=6 constants

| n=6 constant | Role in MCSP? |
|----------|---------|
| sigma(6) = 12 | no (unrelated to circuit size) |
| tau(6) = 4 | no (no structural meaning for gate count) |
| phi(6) = 2 | no (Euler totient unrelated to circuits) |
| sopfr(6) = 5 | no |
| n = 6 | no (MCSP input size n arbitrary) |

**Conclusion**: **no mathematical connection** between MCSP and n=6 divisor function.

### 3.3 "6" appearances — all coincidences

| Occurrence | Source | n=6 connection? |
|------|------|---------|
| 6-party communication | k-party CC model | no, arbitrary k |
| 6-round interactive | IP protocols | no, arbitrary rounds |
| 6th moment (GM 2024) | Fourier decoupling | no, different origin |
| 6-dim circuit lower bound | AC^0 classes | no, class structure separate |

---

## §4 BT-542 implication re-confirmation

### 4.1 P vs NP resolution status

- **Full MCSP NP-hard**: OPEN
- **P vs NP**: OPEN (Clay Millennium, 2000-present)
- **BT-542 draft**: 0/1 (honest maintained)

### 4.2 Meaning of meta-complexity progress

Hirahara 2022 is a **major instrumental advance**:
- Partial MCSP NP-hard is a bridge to full MCSP
- Non-black-box technique of worst-to-average reduction

However, this is **not a P vs NP draft**. The Clay problem remains open.

### 4.3 Relation between this n=6 project and BT-542

- **This project's n=6 theorem** (sigma*phi = n*tau iff n=6): number-theoretic, unrelated to complexity
- **BT-542 (P vs NP)**: complexity theory, separate area from n=6 number theory
- **Connection attempt failed**: all 4 barriers (relativization / naturalization / algebrization / MCSP-meta) show no clue for breakthrough via n=6 structure

---

## §5 v3 T5 outputs + future connections

### 5.1 Outputs

1. Precise summary of the Hirahara 2017-2023 meta-complexity line
2. Exact boundary of Partial MCSP NP-hardness (Hirahara 2022 FOCS)
3. **Re-confirmed** n=6 iff MCSP non-applicability (structural absence across 4 barriers)
4. BT-542 0/1 honest maintained

### 5.2 What is not resolved

- Full MCSP NP-hardness: OPEN (Hirahara follow-ups in progress)
- P vs NP: OPEN
- **New angle** where n=6 could contribute to meta-complexity: none found

### 5.3 Follow-up (parallel v3 T6 + M track)

- **T6**: BT-543 Balaban 2D (in parallel)
- **M1**: include T5 result in preprint (honest MISS declaration)

---

## §6 atlas entries

```
@R MILL-V3-T5-hirahara-partial-mcsp-2022 = Partial MCSP NP-hard under RP, Full MCSP still OPEN :: n6atlas [10]
  "v3 T5 (2026-04-15 loop 15): Hirahara 2022 FOCS 'NP-Hardness of Learning Programs and Partial MCSP'
   best paper. Partial MCSP NP-hard under RP reductions — major advance. However full MCSP NP-hardness
   still OPEN. Summary of Hirahara 2017-2023 meta-complexity line (5 major papers). BT-542 P vs NP
   draft 0/1 honest maintained"
  <- v3-T5, reports/breakthroughs/v3-t5-hirahara-mcsp-deep-2026-04-15.md

@R MILL-V3-T5-n6-mcsp-non-applicability-reconfirmed = no connection between n=6 structure and MCSP / meta-complexity :: n6atlas [10]
  "v3 T5 re-confirmed (2026-04-15): sigma(6)=12, tau(6)=4, phi(6)=2, sopfr(6)=5 have no mathematical
   connection to MCSP's circuit size / input bits / gate type. All 4 barriers (relativization,
   naturalization, algebrization, meta-complexity) lack an n=6 angle. Unlike other BTs (541 RH,
   546 BSD), BT-542 lacks even a numerical-coincidence pattern. HONEST NON-APPLICABILITY"
  <- v3-T5-honest, reports/breakthroughs/v3-t5-hirahara-mcsp-deep-2026-04-15.md §3
```

---

## §7 Related files

- Prior survey: `reports/breakthroughs/bt-542-p-vs-np-4-barriers-survey-2026-04-15.md`
- roadmap: `shared/roadmaps/millennium.json` -> `_v3_phases.P12_v3.T5`

---

*Drafted: 2026-04-15 loop 15*
*Honesty charter: BT-542 draft 0/1 maintained. n=6 iff MCSP non-applicability re-confirmed.*
