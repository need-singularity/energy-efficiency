# PROB-P2-4 — Navier-Stokes Modern Barriers + Recent Progress

**Track**: millennium-learning P2-PROBLEM / Task 4
**Document type**: study note (modern barriers + progress overview)
**Scope**: from Leray 1934 to Tao 2016 finite-time blowup for averaged NS, Chen-Hou 2022-2023, 90 years of progress toward global existence + uniqueness of smooth solutions of 3D Navier-Stokes, and the walls
**Honesty declaration**:
- This document is a study note. The 3D Navier-Stokes problem is not resolved here. As of 2026-04-15 NS remains an open Clay problem.
- Historical years/authors/journals from primary sources. Numerical evidence from Chen-Hou 2023 transcribed from figures/tables of the original, not recomputed.
- BT-544's **triple resonance** (Sym^2(R^3) = 6, Λ^2(R^3) = 3, Onsager α_c = 1/3) is an observation, not a demonstration (compliance with millennium-7-closure-2026-04-11.md §BT-544).

**Primary sources**
- Jean Leray, "Sur le mouvement d'un liquide visqueux emplissant l'espace", *Acta Mathematica* 63, 1934, pp. 193-248.
- Eberhard Hopf, "Über die Anfangswertaufgabe für die hydrodynamischen Grundgleichungen", *Mathematische Nachrichten* 4, 1951, pp. 213-231.
- Olga A. Ladyzhenskaya, *The Mathematical Theory of Viscous Incompressible Flow*, 2nd ed. (English), Gordon and Breach, 1969 (Russian 1st ed. 1961).
- Luis Caffarelli, Robert Kohn, Louis Nirenberg, "Partial regularity of suitable weak solutions of the Navier-Stokes equations", *Communications on Pure and Applied Mathematics* 35(6), 1982, pp. 771-831.
- Charles L. Fefferman, "Existence and smoothness of the Navier-Stokes equation — Official problem description", Clay Mathematics Institute, 2000. https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf
- Terence Tao, "Finite time blowup for an averaged three-dimensional Navier-Stokes equation", *Journal of the American Mathematical Society* 29, 2016, pp. 601-674.
- Terence Tao, "Quantitative bounds for critically bounded solutions to the Navier-Stokes equations", *arXiv:1908.04958*, 2019.
- Jiajie Chen, Thomas Y. Hou, "Stable nearly self-similar blowup of the 2D Boussinesq and 3D Euler equations with smooth data", arXiv:2210.07191, 2022.
- Jiajie Chen, Thomas Y. Hou, "Finite time blowup of 2D Boussinesq and 3D Euler equations with smooth data", *Communications on Mathematical Physics* 383, 2021, pp. 1559-1667.
- Tristan Buckmaster, Vlad Vicol, "Nonuniqueness of weak solutions to the Navier-Stokes equation", *Annals of Mathematics* 189(1), 2019, pp. 101-144.
- Peter Constantin, Ciprian Foias, *Navier-Stokes Equations*, Chicago Lectures in Math., University of Chicago Press, 1988.
- Pierre-Gilles Lemarié-Rieusset, *Recent Developments in the Navier-Stokes Problem*, Chapman & Hall/CRC, 2002.
- Lars Onsager, "Statistical hydrodynamics", *Il Nuovo Cimento* 6(Supp. 2), 1949, pp. 279-287.
- Philip Isett, "A proof of Onsager's conjecture", *Annals of Mathematics* 188(3), 2018, pp. 871-963.

---

## 0. Why "Modern Barriers"

Global existence of smooth solutions to 3D Navier-Stokes is open for more than 90 years. This is often evaluated as **"the deepest single PDE problem"**. Three threads compete:

1. **Weak/strong regularity thread**: CKN 1982, Escauriaza-Seregin-Šverák 2003, Tao 2019.
2. **Blow-up scenario thread**: Tao 2016 (averaged), Chen-Hou 2022-2023 (Euler/Boussinesq).
3. **Weak-solution non-uniqueness thread**: Buckmaster-Vicol 2019.

---

## 1. Leray 1934 — Start of Weak-Solution Construction

### 1.1 Definition

- 3D Navier-Stokes equation:
  \[
  \partial_t u + (u \cdot \nabla) u - \nu \Delta u + \nabla p = 0, \quad \nabla \cdot u = 0, \quad u(0, x) = u_0(x)
  \]
  ν > 0 kinematic viscosity, u: R^4 -> R^3 velocity, p pressure.
- **Leray 1934 theorem**: for u_0 ∈ L^2(R^3), ∇·u_0 = 0, at least one **weak solution** u ∈ L^∞_t L^2_x ∩ L^2_t H^1_x exists.
- Method: Galerkin + compactness.
- Source: *Acta Mathematica* 63, 1934, pp. 193-248.

### 1.2 Energy Inequality

Leray weak solutions satisfy:
\[
\frac{1}{2} \|u(t)\|_{L^2}^2 + \nu \int_0^t \|\nabla u(s)\|_{L^2}^2 \, ds \leq \frac{1}{2} \|u_0\|_{L^2}^2
\]
Non-increasing energy. Inequality (not equality) due to possible energy loss in Galerkin limit (anomalous-dissipation possibility).

### 1.3 Hopf 1951 — Bounded Domain Extension

- Hopf extended Leray's method to bounded Ω ⊂ R^3 with no-slip u|_{∂Ω} = 0.
- Source: *Math. Nachr.* 4, 1951, pp. 213-231.

### 1.4 **Current Barrier 1 — Weak-Solution Uniqueness**

- Uniqueness of Leray-Hopf weak solutions in 3D is unresolved.
- Unresolved uniqueness is a main obstacle to smoothness demonstration.

---

## 2. Ladyzhenskaya 1963 — 2D Global Regularity

### 2.1 2D Result

- 2D NS smooth solutions globally exist and are unique.
- Key: in 2D vorticity ω is scalar, transport $\partial_t ω + (u \cdot \nabla) ω = \nu \Delta ω$ bounds ω^∞.

### 2.2 **Decisive Difference in 3D**

- In 3D, ω ∈ R^3 vector, vortex stretching $(ω \cdot \nabla) u$ appears:
  \[
  \partial_t ω + (u \cdot \nabla) ω = (ω \cdot \nabla) u + \nu \Delta ω
  \]
- Stretching may amplify ω arbitrarily — primary blowup-mechanism candidate.

### 2.3 Source

- Ladyzhenskaya, Gordon and Breach, 1969, ch. 6.

---

## 3. Caffarelli-Kohn-Nirenberg 1982 — Partial Regularity

### 3.1 CKN Theorem

- *Comm. Pure Appl. Math.* 35, 1982, pp. 771-831.
- **Theorem**: for suitable weak solutions, singular set Σ ⊂ R^4 has 1D parabolic Hausdorff measure 0: $\mathcal{P}^1(\Sigma) = 0$.
- Demonstration: local energy inequality + scaling + iterative improvement.

### 3.2 **Limitation**

- Partial result. Not full smoothness.
- Whether singularities exist remains unresolved.
- Improvement over Scheffer 1976 *Pacific J. Math.* 66.

### 3.3 **Current Barrier 2 — Gap Between Suitable and Leray-Hopf**

- CKN applies only to suitable weak solutions.
- Whether general Leray-Hopf are suitable is unknown.

---

## 4. Serrin Conditions and Critical Spaces

### 4.1 Serrin Condition (1962)

- u ∈ $L^p_t L^q_x$, $2/p + 3/q \leq 1$, $q \geq 3$ => u locally smooth.
- Source: *ARMA* 9, 1962, pp. 187-195.

### 4.2 Critical Spaces

- $2/p + 3/q = 1$ boundary is critical.
- Weakest critical: $L^\infty_t L^3_x$.

### 4.3 Escauriaza-Seregin-Šverák 2003

- **Theorem**: $u \in L^\infty_t L^3_x$ => smooth.
- Source: *Russian Math. Surveys* 58, 2003, pp. 211-250.

### 4.4 **Current Barrier 3 — No Control Below Critical**

- Unknown whether Leray-Hopf is in $L^\infty_t L^3_x$.
- Energy inequality secures only $L^\infty_t L^2_x$.
- 3D NS is supercritical from Serrin scaling perspective.

---

## 5. Tao 2016 — Averaged NS Finite-Time Blow-Up

### 5.1 Tao's Result

- *J. Amer. Math. Soc.* 29, 2016, pp. 601-674.
- **Theorem**: replacing NS's nonlinear term with an **averaged form**, Tao constructs smooth solutions with finite-time blowup.
- This is blowup in a **related model**, not real NS.

### 5.2 Construction — Self-Similar Computational Mechanism

- Tao models NS nonlinear cascade as a Turing-machine energy-transport model.
- Tao conjectures "real NS also blows up in finite time" (2016 introduction).

### 5.3 **Limitation**

- Averaged, not real. Structural differences exist.
- Tao's blog explains intuitively: https://terrytao.wordpress.com/ 2014-2016.

### 5.4 Tao 2019 — Quantitative Bound

- arXiv:1908.04958.
- Quantitative higher-norm bounds if weak solution is in $L^\infty_t L^3_x$.

---

## 6. Chen-Hou 2022-2023 — Boussinesq/Euler Blowup

### 6.1 Chen-Hou (2022)

- arXiv:2210.07191.
- **Result**: computer-assisted demonstration of finite-time blowup for 2D Boussinesq and 3D axisymmetric Euler from smooth initial data.

### 6.2 **Importance**

- Euler, not NS (no viscosity).
- However suggests "near blowup" at small ν.

### 6.3 **Limitation**

- Chen-Hou is Euler, not NS. Viscosity may prevent blowup.
- Boussinesq coupled with temperature, separate from NS.
- Computer-assisted demonstration needs independent verification.

### 6.4 Onsager Conjecture Connection

- Onsager 1949: Hölder exponent α > 1/3 -> energy conservation; α < 1/3 -> anomalous dissipation possible.
- Isett 2018: anomalous dissipation at α < 1/3 constructed.
- Critical α_c = 1/3 is one of BT-544's triple resonances (§10).

---

## 7. Buckmaster-Vicol 2019 — Weak Non-Uniqueness

### 7.1 Result

- *Annals of Math.* 189(1), 2019, pp. 101-144.
- **Theorem**: 3D NS weak solutions **are not unique** — distinct Hölder weak solutions from same initial data.
- Technique: convex integration (extending De Lellis-Székelyhidi 2013).

### 7.2 Weak vs Leray-Hopf

- Important: Buckmaster-Vicol's are **not Leray-Hopf** — distributional, do not satisfy energy inequality.
- Uniqueness of Leray-Hopf is still open.

### 7.3 **Meaning**

- "Weak-uniqueness program" re-evaluated.
- Community now focuses on Leray-Hopf class.

### 7.4 **Current Barrier 4 — Leray-Hopf Uniqueness**

- Central post-Buckmaster-Vicol problem.
- Open as of 2024.

---

## 8. Five Approaches and Each Barrier

### 8.1 Energy-Based (Leray-Hopf)

- Route: energy inequality + Galerkin.
- Barrier: $L^2$ is supercritical.

### 8.2 Higher Sobolev (Local Smooth)

- Route: smoothness for small data or short times (Fujita-Kato 1964).
- Barrier: cannot exclude blowup at large data + long times.

### 8.3 Vorticity (Beale-Kato-Majda 1984)

- BKM criterion: $\int_0^T \|\omega(t)\|_{L^\infty} dt < \infty$ => smooth.
- Source: *CMP* 94, 1984, pp. 61-66.
- Barrier: no direct tool to demonstrate condition.

### 8.4 Symmetric (Axisymmetric, No Swirl)

- Route: axisymmetric + no-swirl -> 2D, global regularity.
- Barrier: with-swirl equivalent to 3D. Hou-Luo 2013 formal blowup; Chen-Hou 2022 rigorous.

### 8.5 Self-Similar

- Leray 1934 conjectured self-similar blowup possibility.
- Nečas-Růžička-Šverák 1996 excluded Leray's specific scenario.
- Barrier: general self-similar blowup open.

---

## 9. Current Numerical Evidence (as of 2026)

- Kida-Murakami 1987, 1989: DNS of Taylor-Green vortex, no blowup suggestion at high resolution.
- Hou-Luo 2013: axisymmetric + no-swirl blowup numerics; rigorous in Chen-Hou 2022.
- Brachet-Meiron-Orszag: Euler debated.

Numerics suggest possibilities but not demonstration. Viscosity in NS may make blowup harder than in Euler.

---

## 10. n=6 Connection (Reference Memo)

### 10.1 Triple Resonance (BT-544)

BT-544 records:

1. **Sym^2(R^3) = 6 = n**: stress tensor 3x3 symmetric, $\binom{3+1}{2} = 6$ independent components at $d=3$.
2. **Λ^2(R^3) = 3 = n/φ(6)**: vorticity = dual of 2-form, $\binom{3}{2} = 3$ components. Why vorticity is a vector in 3D.
3. **Onsager α_c = 1/3 = 1/(n/φ)**: Onsager 1949 critical Hölder exponent; Isett 2018 rigorous.

### 10.2 **Honesty Declaration** (millennium-7-closure §BT-544)

> "n=6 arithmetic parameterizes the dimension-analytic environment of NS. d=3 being the first perfect-number dimension gives a structural hint to 'why 3D is hard'. But actual PDE demonstration path is 0."

### 10.3 d=7 Prediction (NOT DEMONSTRATED)

- Sym^2(R^7) = 28 = second perfect number. Observational only.
- Reynolds stress 6 = n independent components. Kolmogorov −5/3 = −sopfr(6)/(n/φ(6)).

### 10.4 **Scope Declaration**

- This project does not provide a path to demonstrate NS global smoothness. §10 records arithmetic rewritings only.

---

## 11. Clay Official Statement and Scope

- Fefferman 2000 (prize for any one of 4):
  - (A) Global smoothness on R^3.
  - (B) Finite-time blowup on R^3.
  - (C) Global smoothness on T^3.
  - (D) Finite-time blowup on T^3.

---

## 12. Source Summary Table

| Year | Authors | Result | Source |
|---|---|---|---|
| 1934 | Leray | 3D weak solution | *Acta Math.* 63 |
| 1949 | Onsager | α_c = 1/3 conjecture | *Nuovo Cim.* 6 Supp. |
| 1951 | Hopf | bounded-domain weak solution | *Math. Nachr.* 4 |
| 1961/69 | Ladyzhenskaya | 2D global smoothness | book |
| 1962 | Serrin | Serrin condition | *ARMA* 9 |
| 1964 | Fujita-Kato | local smooth | *ARMA* 16 |
| 1976 | Scheffer | pioneering partial regularity | *Pacific J. Math.* 66 |
| 1982 | CKN | partial regularity | *CPAM* 35 |
| 1984 | Beale-Kato-Majda | blowup criterion | *CMP* 94 |
| 2000 | Fefferman | Clay official | Clay |
| 2003 | Escauriaza-Seregin-Šverák | $L^\infty_t L^3_x$ smooth | *RMS* 58 |
| 2013 | Hou-Luo | axisymmetric blowup | *PNAS* 111 |
| 2013 | De Lellis-Székelyhidi | Euler convex integration | *Ann. Math.* 170 |
| 2016 | Tao | averaged NS blowup | *JAMS* 29 |
| 2018 | Isett | Onsager α<1/3 | *Ann. Math.* 188 |
| 2019 | Buckmaster-Vicol | weak non-uniqueness | *Ann. Math.* 189 |
| 2021 | Chen-Hou | Boussinesq blowup | *CMP* 383 |
| 2022 | Chen-Hou | 3D Euler blowup | arXiv:2210.07191 |

---

## 13. Connection to Next Task

- PROB-P2-5: Hodge conjecture modern barriers.
- PURE-P1-3: PDE derivation + weak/strong distinction.
- BT-544: triple resonance + d=7 prediction.

---

## 14. Next Steps

### 14.1 Learning

- CKN 1982 local-energy-inequality derivation reproduction.
- Buckmaster-Vicol 2019 convex-integration structure follow-through.
- Chen-Hou 2022 computer-assisted verification.
- Tao 2016 averaged scaling identification.

### 14.2 n=6 Project

- Expand PDE meaning of BT-544 triple resonance.
- Test d=7 prediction numerically.
- Organize physical interpretation of Kolmogorov −5/3.

### 14.3 Conditions for Bypass

Must resolve four barriers (§1.4, §3.3, §4.4, §7.4) simultaneously or chain-solve. Candidates:

- Leray-Hopf extension of convex integration.
- Quantitative critical regularity (Tao 2019).
- Systematic self-similar classification (Chen-Hou -> NS).

No chain as of April 2026.

---

## 15. Appendix — Scaling and Supercriticality

### 15.1 NS Scaling

- $u(x, t) \to \lambda u(\lambda x, \lambda^2 t)$.
- Norms under scaling:
  - $\|u\|_{L^2}^2 \to \lambda^{-1} \|u\|_{L^2}^2$ (subcritical)
  - $\|u\|_{L^3}^3 \to \|u\|_{L^3}^3$ (critical)
  - $\|u\|_{L^\infty}$ scale-invariant.
  - $\|\nabla u\|_{L^2}^2 \to \lambda \|\nabla u\|_{L^2}^2$ (supercritical in 3D)

### 15.2 Critical Meaning

- Critical: norm invariant. Local existence time depends only on initial norm.
- Supercritical: scaling decreases norm.
- Subcritical: scaling increases norm — natural control.

### 15.3 3D NS Supercriticality

- $L^2$ energy norm supercritical.
- Critical $L^3$ requires stronger control.
- Cannot control critical norms in time with current methods. Core difficulty.

### 15.4 2D Decisive Difference

- 2D energy $L^2$ is critical under its scaling.
- Energy inequality controls naturally. 3D dim analysis supercritical — new tools needed.

### 15.5 Source

- Cannone 2004 Handbook of Math. Fluid Dynamics Vol. 3, §2.

---

## 16. Appendix — Besov Spaces and Vorticity Stretching

### 16.1 Definition

- $\dot{B}^s_{p,q}(\mathbb{R}^3)$: homogeneous Besov via Littlewood-Paley.

### 16.2 Kato 1984

- *Math. Z.* 187, 1984, pp. 471-480.
- Local existence in critical Besov $\dot{B}^{-1+3/p}_{p, \infty}$.

### 16.3 Koch-Tataru 2001 — $BMO^{-1}$

- *Adv. Math.* 157, 2001, pp. 22-35.
- NS local solution in $BMO^{-1}$.

### 16.4 Vorticity Stretching / Besov

- Attempts to control Besov norm of $(\omega \cdot \nabla) u$.
- Planchon 2003 Besov $\dot{B}^0_{\infty, \infty}$ blowup criterion.

### 16.5 **Barrier G**

- Exponential growth in critical Besov uncontrolled.
- Modern approaches conditional.

---

**Honesty check**:
- Leray 1934 *Acta Math.* 63 confirmed via Ladyzhenskaya 1969 + Lemarié-Rieusset 2002.
- CKN 1982 $\mathcal{P}^1(\Sigma) = 0$ verbatim from *CPAM* 35 Theorem A.
- Tao 2016 averaged model equation (2.3) *JAMS* 29 §2; differs from real NS per §1 remarks.
- Chen-Hou 2022 arXiv:2210.07191 Theorems 1.1, 1.2 directly confirmed in §1.1.
- Buckmaster-Vicol 2019 Theorem 1 class is distributional per §1 Remark 1.3.
- Onsager 1949 original *Nuovo Cimento* Italian. Isett 2018 reconstructs history.
- BT-544 triple resonance strictly complies with millennium-7-closure §BT-544.
- Koch-Tataru 2001 $BMO^{-1}$ Theorem 1 confirmed.
- Kato 1984 Theorem 1 Besov-space solution existence.
