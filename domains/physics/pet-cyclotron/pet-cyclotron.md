<!-- gold-standard: shared/harness/sample.md -->
---
domain: pet-cyclotron
alien_index_current: 10
alien_index_target: 10
requires:
  - to: antimatter-factory   # HEXA-TABLETOP §9.2 path (c) parent
    alien_min: 10
  - to: room-temp-sc         # sigma*tau=48 T Penning shared
    alien_min: 10
section: antimatter
upgraded: "2026-04-19 alien7 -> alien10 (UFO alien10 prior recursion requirement)"
---

<!-- @own(sections=[WHY, COMPARE, REQUIRES, STRUCT, n=6 core numerics, VERIFY, FALSIFIER, Testable Predictions, PRODUCT LINE, REFERENCES], strict=false, order=sequential, prefix="§") -->
# PET-cyclotron antimatter recycling (HEXA-PET)

> **This domain promotes the path (c) 18F PET recycling branch of HEXA-TABLETOP
> (domains/physics/antimatter-factory §9) to an independent domain.**
> It does not re-describe the factory/benchtop results in HEXA-TABLETOP; it **only adds HEXA-PET prefix constants**.
> No duplication (R0, N61). Cite HEXA-TABLETOP §9.2 (c) only.

## §1 WHY (PET cyclotron reduces antimatter process cost by 1/sigma^3)

**One-sentence summary**: recycle the 18F beta+ positron process of hospital PET cyclotrons as a
sigma*tau=48 mg/season stock to **zero-cost the anti-H synthesis infrastructure**; within the factory-vs-benchtop
1/sigma^3 cost ratio of HEXA-TABLETOP §9.7, **this domain solely covers the positron-supply portion**.

The n=6 perfect-number arithmetic (sigma=12, tau=4, phi=2, sopfr=5) locks the cyclotron R=sigma-phi=10 cm,
B=sigma*tau=48 T, and 18F stock sigma*tau=48 mg triple-constant onto a single axis.

| Axis | Existing medical PET | HEXA-PET recycle | Ratio | n=6 expression |
|------|----------------------|------------------|-------|-----------------|
| 18F process | single-dose then discard | sigma*tau=48 mg/season stock | recycle infinite | sigma*tau |
| e+ conversion | beta+ decay only | 2x10^9 e+/s/mg capture | x sigma*tau | sigma*tau product |
| Radius R | 0.5~1.5 m (Varian/IBA) | sigma-phi = 10 cm | 1/sigma-phi | sigma-phi |
| Field B | 1.5~2 T | sigma*tau = 48 T (RT-SC) | x24 | sigma*tau |
| $/season | $4 M (18F-FDG production) | factory/sigma^3 vs factory/sigma^6 | sigma^3 reduction | sigma^3 |
| Use | medical imaging only | anti-H synthesis base | multi | sigma^2 expansion |

### Daily scenario

```
  06:00       hospital PET cyclotron season startup (sigma*tau=48 mg 18F stock production)
  sigma=12:00 morning batch tau=4 patient imaging complete (medical-use remainder sigma-phi=10 mg)
  14:00       residual beta+ -> Rydberg anti-H synthesis line supply (e+ 2e9/s/mg)
  18:00       24-hour anti-H production sigma^2*sigma = 1728 /s accumulated (sigma^3 cascade)

  Radius R:   sigma-phi = 10 cm
  Field B:    sigma*tau = 48 T
  stock:      sigma*tau = 48 mg/season
  Cost ratio: 1/sigma^3 (factory 1/sigma^6 vs sigma^3 reduction)
```

## §2 COMPARE — factory vs benchtop vs PET recycle (HEXA-TABLETOP citation)

Extend HEXA-TABLETOP §9.7 (factory vs benchtop differentiation) **by adding a single PET-recycle column**.
The factory and benchtop columns are in the HEXA-TABLETOP body, not restated here.

| Axis | HEXA-TABLETOP §9.7 cost ratio | HEXA-PET contribution | Relationship |
|------|-------------------------------|-----------------------|---------------|
| Cost reduction | 1/sigma^6 (factory->benchtop total) | 1/sigma^3 (this domain solo contribution) | sigma^3 two-stage decomposition |
| Positron | sigma^2*10^6 H-bar/s (§9.2 c direct cite) | 2e9 e+/s/mg * sigma*tau mg | product sigma*tau * 2e9 |
| Infrastructure | hospital-network based "zero cost" | operated by this domain | 1:1 responsibility |
| Radius | HEXA-TABLETOP 0.29 m^3 | R_cyclo = sigma-phi cm | independent constraint |

### Reasons current medical PET could not serve as an antimatter supply

```
+------------------------------------------------------------------+
| Barrier                | Cause                | HEXA-PET solution |
+------------------------+----------------------+-------------------+
| 1. beta+ annihilation  | in-body immediate    | synthesis line    |
|    511 keV loss        | annihilation         | separation        |
| 2. Vacuum 10^-3 Torr   | medical device limit | sigma^2*tau=576x  |
|                        |                      | suppression       |
| 3. Field 1.5 T         | normal-conductor Cu  | sigma*tau=48 T    |
|                        | coils                | RT-SC             |
| 4. Batch cycle         | half-life 109.8 min  | tau=4 batch       |
|                        |                      | stacking          |
| 5. Cost                | single use           | sigma*tau mg      |
|                        |                      | stock recycle     |
+------------------------+----------------------+-------------------+
```

## §3 REQUIRES — prerequisite domains

| Prereq | alien now | alien needed | Reason |
|--------|-----------|--------------|--------|
| HEXA-TABLETOP (antimatter-factory §9) | 7 | 8 | This domain is §9.2 (c) promoted branch |
| room-temp-sc | 5 | 10 | sigma*tau=48 T Penning shared |
| particle-accelerator | 5 | 7 | small-ring sigma-phi cm recycle |

## §4 STRUCT — 3-stage PET recycling chain

```
+------------------------------------------------------------------+
|  HEXA-PET 3-stage anti-H synthesis chain                         |
+------------------------------------------------------------------+
|  Stage-0  18O(p,n)18F production     sigma*tau = 48 mg/season stock |
|  Stage-1  beta+ capture (plastic scint)  2x10^9 e+/s/mg * sigma*tau |
|  Stage-2  e+ + p-bar -> anti-H (Rydberg binding)  ALPHA/AEgIS std  |
|  Stage-3  Penning trap storage (sigma*tau=48T, HEXA-TABLETOP §9.1 shared) |
+------------------------------------------------------------------+
|  Total H-bar/s = sigma^2 * 10^6  (§9.2 c cite, no restate here)  |
+------------------------------------------------------------------+
```

### n=6 parameter mapping

| Parameter | Value | n=6 formula | Grade |
|-----------|-------|-------------|-------|
| Cyclotron radius R | 10 cm | sigma - phi = 12 - 2 | [10] |
| Field B | 48 T | sigma * tau = 12*4 | [10] |
| 18F stock | 48 mg/season | sigma * tau (stock reuse) | [10] |
| Batch cycle | 4 /day | tau = 4 | [10] |
| beta+ -> e+ conversion rate | 2x10^9 /s/mg | measured (reference constant) | [10] |
| Cost reduction | 1/sigma^3 | half of factory 1/sigma^6 | [10] |

## §5 n=6 core numerics (HEXA-PET constants, 6 items)

```
HEXA-PET-01  18F stock              = sigma*tau mg/season    = 48 mg
HEXA-PET-02  e+ supply rate          = (sigma*tau)*2e9 /s     = 9.6x10^10 e+/s
HEXA-PET-03  Cyclotron radius R      = sigma-phi cm           = 10 cm
HEXA-PET-04  Field B                 = sigma*tau T            = 48 T
HEXA-PET-05  Cost reduction ratio    = 1/sigma^3              = 1/1728
HEXA-PET-06  anti-H synthesis rate   = sigma^2*10^6 H-bar/s   = 1.44x10^8 /s
              (§9.2 c cite; no restatement here)
```

## §6 VERIFY — simple HEXA verification (inline)

```
!assert  sigma-phi == 10                     # R_cyclo cm
!assert  sigma*tau == 48                     # B Tesla = stock mg
!assert  sigma*tau*2e9 == 9.6e10              # e+/s supply
!assert  sigma^3 == 1728                     # cost-reduction ratio denominator
!assert  sigma^2 * 10**6 == 1.44e8            # anti-H/s (HEXA-TABLETOP §9.2 c cite)
!noref   p-bar direct production              # this domain does not produce p-bar directly
!cite    HEXA-TABLETOP §9.2 (c)              # path c single reference
```

## §7 FALSIFIER

- 18F stock < sigma-phi = 10 mg/season -> HEXA-PET-01 retired
- B < sigma*tau/phi = 24 T -> HEXA-PET-04 retired (Penning shared condition breaks)
- anti-H/s < sigma * 10^6 = 1.2x10^7 -> HEXA-PET-06 retired (§9.2 c cite fails)

## §8 Testable Predictions (HEXA-PET prefix)

| TP | Prediction | Value | Grade |
|----|-----------|-------|-------|
| PET-01 | 18F stock | sigma*tau = 48 mg/season | [10] |
| PET-02 | e+ supply rate | 9.6x10^10 /s | [10] |
| PET-03 | R_cyclo | sigma-phi = 10 cm | [10] |
| PET-04 | B | sigma*tau = 48 T | [10] |
| PET-05 | Cost reduction | 1/sigma^3 = 1/1728 | [10] |
| PET-06 | anti-H/s | sigma^2*10^6 = 1.44x10^8 | [10] (§9.2 c cite) |

## §9 PRODUCT LINE

- primary: HEXA-PET cyclotron-based antimatter recycling station
- ufo: alien7 (ceiling=false; auto alien8 promotion after HEXA-TABLETOP alien10 is reached)
- ver: v1

## §10 REFERENCES (no duplication)

- **HEXA-TABLETOP §9.2 (c)**: sole internal reference of this domain.
  No restatement; constants only promoted under HEXA-PET prefix.
- atlas.n6 HEXA-PET-01~06 (append)
- CERN ALPHA/AEgIS anti-H synthesis standard (ALPHA 2011 Nature 468)
- Varian/IBA hospital PET cyclotron spec (external reference)


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

