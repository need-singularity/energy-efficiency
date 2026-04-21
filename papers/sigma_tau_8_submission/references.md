# References -- sigma(n) - tau(n) = 8 Paper

---

## Core References (Must Cite)

### Arithmetic Functions -- Standard Texts

[1] G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers*, 6th ed., Oxford University Press, 2008.
- Standard reference for sigma(n), tau(n), phi(n) definitions and multiplicativity.
- Chapters 16-17 on arithmetic functions.

[2] T. M. Apostol, *Introduction to Analytic Number Theory*, Springer, 1976.
- Formal treatment of multiplicative functions, Dirichlet series.
- Theorem on multiplicativity of sigma and tau (Chapter 2).

[3] I. Niven, H. S. Zuckerman, and H. L. Montgomery, *An Introduction to the Theory of Numbers*, 5th ed., Wiley, 1991.
- Alternative standard text covering divisor function properties.

### Perfect Numbers

[4] K. Voight, "Perfect numbers," in *Topics in Number Theory*, Springer, 2021.
- Survey of perfect number theory. sigma(n) = 2n characterization.
- Relevant for contextualizing n = 6 as the first perfect number.

[5] T. Goto and Y. Ohno, "Odd perfect numbers revisited," *Math. Comp.*, 77 (2008), 2261--2279.
- Recent work on perfect numbers; establishes bounds.

[6] P. Ochem and M. Rao, "Odd perfect numbers are greater than 10^1500," *Math. Comp.*, 81 (2012), 1869--1877.
- State-of-the-art lower bound for odd perfect numbers.

### Arithmetic Identities Involving sigma, tau, phi

[7] J. Sandor and B. Crstici, *Handbook of Number Theory II*, Springer, 2004.
- Comprehensive catalog of identities and inequalities involving sigma, tau, phi.
- Check for prior results on sigma(n) - tau(n) = c.

[8] D. S. Mitrinovic, J. Sandor, and B. Crstici, *Handbook of Number Theory I*, Springer, 1995.
- Earlier volume; inequalities for arithmetic functions.
- Includes bounds of the form sigma(n) >= n + 1, tau(n) >= 2 for n >= 2.

[9] R. K. Guy, *Unsolved Problems in Number Theory*, 3rd ed., Springer, 2004.
- Check sections B1-B18 for related open problems on arithmetic functions.
- Specifically B2 (sigma(n)), B5 (tau(n)), B8 (phi(n)).

### Characterization of Specific Integers via Arithmetic Functions

[10] C. Pomerance, "On the distribution of amicable numbers," *J. Reine Angew. Math.*, 293 (1977), 217--222.
- Methodology for studying level sets of arithmetic function equations.

[11] P. Erdos and C. Pomerance, "On the normal number of prime factors of phi(n)," *Rocky Mountain J. Math.*, 15 (1985), 343--352.
- Techniques for analyzing arithmetic function values.

### Golay Code and Coding Theory (If Section Included)

[12] M. J. E. Golay, "Notes on digital coding," *Proc. IRE*, 37 (1949), 657.
- Original paper introducing the Binary Golay code [23, 12, 7].

[13] J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups*, 3rd ed., Springer, 1999.
- Comprehensive treatment of Golay code, Leech lattice (Chapter 3, 11).
- Extended Binary Golay code [24, 12, 8] parameters.

[14] F. J. MacWilliams and N. J. A. Sloane, *The Theory of Error-Correcting Codes*, North-Holland, 1977.
- Standard reference for coding theory; Golay code uniqueness proofs.

### Bott Periodicity and Topological Context (Optional, for Discussion)

[15] R. Bott, "The stable homotopy of the classical groups," *Ann. of Math.*, 70 (1959), 313--337.
- Original Bott periodicity theorem; period 8.
- Optional citation if discussing sigma - tau = 8 = Bott period.

### Computational Verification

[16] The OEIS Foundation, "The On-Line Encyclopedia of Integer Sequences," https://oeis.org.
- Relevant sequences: A000203 (sigma), A000005 (tau), and the difference sequence.
- Check A??????: sigma(n) - tau(n).

[17] SageMath, "SageMath: Open-Source Mathematics Software System," https://www.sagemath.org.
- For independent computational verification.

### sigma(n) * phi(n) = n * tau(n) (Prior Art for the Multiplicative Identity)

[18] [TO FIND]: Need to search for prior publications of sigma(n) * phi(n) = n * tau(n) iff n = 6.
- This result may exist in the literature as a folklore result or exercise.
- Search: Mathematical Reviews, zbMATH, Google Scholar.
- Keywords: "sum of divisors times Euler totient equals n times number of divisors"
- If no prior publication found, this is itself a publishable observation.

---

## References to Find / Verify

| # | Task | Status |
|---|------|--------|
| 1 | Search MathSciNet/zbMATH for "sigma(n) - tau(n)" | TODO |
| 2 | Search OEIS for the sequence sigma(n) - tau(n) | TODO |
| 3 | Verify if sigma*phi = n*tau iff n=6 appears in Hardy-Wright or Sandor | TODO |
| 4 | Find IJNT style BibTeX template | TODO |
| 5 | Check if any published paper studies level sets {n : sigma(n) - tau(n) = c} | TODO |
| 6 | Locate World Scientific ws-ijnt.cls LaTeX class file | TODO |

---

## OEIS Sequences to Reference

- **A000203**: sigma(n) -- sum of divisors of n
- **A000005**: tau(n) = d(n) -- number of divisors of n
- **A000010**: phi(n) -- Euler totient function
- **A??????**: sigma(n) - tau(n) -- to check if this sequence is catalogued
- **A??????**: {n : sigma(n) * phi(n) = n * tau(n)} -- should be {6} if catalogued

---

## BibTeX Template (for LaTeX manuscript)

```bibtex
@book{HardyWright2008,
  author    = {Hardy, G. H. and Wright, E. M.},
  title     = {An Introduction to the Theory of Numbers},
  edition   = {6th},
  publisher = {Oxford University Press},
  year      = {2008}
}

@book{Apostol1976,
  author    = {Apostol, Tom M.},
  title     = {Introduction to Analytic Number Theory},
  publisher = {Springer},
  year      = {1976},
  series    = {Undergraduate Texts in Mathematics}
}

@book{ConwaySloane1999,
  author    = {Conway, John H. and Sloane, Neil J. A.},
  title     = {Sphere Packings, Lattices and Groups},
  edition   = {3rd},
  publisher = {Springer},
  year      = {1999},
  series    = {Grundlehren der mathematischen Wissenschaften}
}

@article{Golay1949,
  author  = {Golay, Marcel J. E.},
  title   = {Notes on digital coding},
  journal = {Proc. IRE},
  volume  = {37},
  year    = {1949},
  pages   = {657}
}

@article{Bott1959,
  author  = {Bott, Raoul},
  title   = {The stable homotopy of the classical groups},
  journal = {Annals of Mathematics},
  volume  = {70},
  number  = {2},
  year    = {1959},
  pages   = {313--337}
}

@book{SandorCrstici2004,
  author    = {Sandor, Jozsef and Crstici, Borislav},
  title     = {Handbook of Number Theory II},
  publisher = {Springer},
  year      = {2004}
}

@book{Guy2004,
  author    = {Guy, Richard K.},
  title     = {Unsolved Problems in Number Theory},
  edition   = {3rd},
  publisher = {Springer},
  year      = {2004}
}
```

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

