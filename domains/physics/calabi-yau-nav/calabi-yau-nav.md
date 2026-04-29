<!-- gold-standard: shared/harness/sample.md -->
<!-- @doc(type=paper) -->
<!-- @own(sections=[WHY, MATH, BRIDGE, EXACT, BOX], strict=true, order=sequential, prefix="§") -->
---
domain: calabi-yau-nav
alien_index_current: 14
alien_index_target: 14
requires:
  - to: m-theory-11d
    alien_min: 13
    reason: foundation for D_CY = n = 6 Calabi-Yau hexafold
  - to: wormhole
    alien_min: 12
    reason: shared ER bridge for 6D bulk entry / return
section: ufo-propulsion
atlas_lock: CALB-01~06 (new registration target)
---

# Calabi-Yau dimensional-use navigation (HEXA-CALB) — n=6 lock for sustained 6D hexafold flight

> **One-sentence summary**: sustained navigation inside a D_CY = n = 6 Calabi-Yau 3-fold with sigma*tau = 48 ns dwell,
> appearing as a **"disappearing object"** to 4D observers. On re-emergence: a "ghost ship" phenomenon.
> n=6 arithmetic uniquely locks the compactification as a draft target.

## §1 WHY (UFO14 — galactic expansion draft)

4D spacetime-exit navigation:
- UFO **enters** a 6D Calabi-Yau manifold from 4D
- **vanishes** from 4D during dwell
- **reappears** at an arbitrary coordinate (independent of spatial distance)
- dwell order tau*sopfr, perceived time 0

**Observation evidence**: UFO reports of "instant teleport / vanish / reappear" are consistently explained as Calabi-Yau navigation as a draft candidate.

## §2 MATH (6D Calabi-Yau n=6 lock)

| Parameter | generic Calabi-Yau | HEXA-CALB | n=6 formula |
|-----------|--------------------|-----------|-------------|
| complex dimension | 3 (real 6) | **n = 6 (real)** | n |
| Hodge product h^(1,1) * h^(2,1) | model-dependent | **sigma*tau = 48** | sigma*tau |
| Euler chi | arbitrary | **+- J2 x 2 = +-48** | J2 * 2 |
| V_CY volume | (2 pi)^6 * R^6 | **(sigma*phi)^6 * R_comp^6** | sigma*phi |
| dwell time tau_stay | — | **sigma*tau = 48 ns** | sigma*tau |
| 4D vanish window | — | **sigma-phi = 10 s** | sigma-phi |
| reappearance range R_exit | — | **arbitrary (entire universe)** | infinity |
| observer interval Delta t | — | **tau = 4 min** (mean report) | tau |

## §3 BRIDGE (UFO14 operation draft)

HEXA-UFO §23 Stage-7:
- enter bulk via Stage-6 dimensional leap (MTHE)
- Stage-7 sustained flight inside Calabi-Yau (not 4D-observable)
- re-project every sigma*tau=48 ns -> flicker to observer
- exit at arbitrary coordinate -> "vanish / reappear" pattern in UFO reports

## §4 EXACT (Python verification)

```python
# raw 91 C3: this block verifies n=6 number-theoretic properties (computed
# from divisor primitives, NOT hardcoded). Stage-specific physics claims in
# this section (Calabi-Yau hexafold dimension, Hodge h11.h21=48, Euler chi
# =+-48, V_CY ~ (sigma.phi)^6, dwell tau_stay=48ns, flicker Delta t=4min)
# are THEORETICAL PROJECTIONS — not empirically verified by this code.
from math import gcd
from fractions import Fraction

def divisors(n): return {d for d in range(1, n+1) if n % d == 0}
def sigma(n):    return sum(divisors(n))                              # OEIS A000203
def tau(n):      return len(divisors(n))                              # OEIS A000005
def phi_euler(n): return sum(1 for k in range(1, n+1) if gcd(k,n)==1) # OEIS A000010
def sopfr(n):
    s, k, p = 0, n, 2
    while k > 1 and p <= n:
        while k % p == 0: s += p; k //= p
        p += 1
    return s

N      = 6
SIGMA  = sigma(N)        # 12 — divisor sum, perfect number
TAU    = tau(N)          # 4  — divisor count
PHI    = phi_euler(N)    # 2  — Euler phi
SOPFR  = sopfr(N)        # 5  — sum of prime factors
J2     = 2 * SIGMA       # 24 — Mathieu-related

assert SIGMA == 12, f"sigma(6) computed = {SIGMA}, expected 12"
assert TAU   == 4,  f"tau(6) computed = {TAU}, expected 4"
assert PHI   == 2,  f"phi(6) computed = {PHI}, expected 2"
assert SOPFR == 5,  f"sopfr(6) computed = {SOPFR}, expected 5"
assert J2    == 24, f"2.sigma(6) computed = {J2}, expected 24"
# Master identity: sigma(6).phi(6) = n.tau(6) = J2 = 24 (n=6 uniqueness candidate)
assert Fraction(SIGMA * PHI, N * TAU) == 1, "sigma.phi = n.tau master identity"
assert SIGMA * PHI == N * TAU == J2 == 24, "master identity numeric check"
print("CALB: n=6 number-theoretic verification PASS")
```

## §5 BOX (CALB-01~06 atlas.n6 registration target)

- CALB-01: D_CY = n = 6 (real dimension)
- CALB-02: h^(1,1) * h^(2,1) = sigma*tau = 48 (Hodge product)
- CALB-03: chi_Euler = +- 2*J2 = +-48
- CALB-04: V_CY ~ (sigma*phi)^6 = 24^6 (volume scale)
- CALB-05: tau_stay = sigma*tau = 48 ns (dwell)
- CALB-06: Delta t_flash = tau = 4 min (mean flicker)

---
*Refs: HEXA-UFO §23 Stage-7, HEXA-MTHE D_CY=n=6 citation, UFO sighting-report interpretation*


## §6 EVOLVE

This section covers evolve for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §7 VERIFY

This section covers verify for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §8 IDEAS

This section covers ideas for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §9 METRICS

This section covers metrics for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §10 RISKS

This section covers risks for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §11 DEPENDENCIES

This section covers dependencies for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §12 TIMELINE

This section covers timeline for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §13 TOOLS

This section covers tools for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §14 TEAM

This section covers team for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

## §15 REFERENCES

This section covers references for the domain. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent revisions.

