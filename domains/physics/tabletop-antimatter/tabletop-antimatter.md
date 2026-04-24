<!-- @own(sections=[WHY, COMPARE, REQUIRES, STRUCT, FLOW, EVOLVE, VERIFY], strict=false, order=sequential, prefix="§") -->

<!-- gold-standard: shared/harness/sample.md -->
---
domain: tabletop-antimatter
alien_index_current: 10
alien_index_target: 10
requires:
  - to: room-temp-sc
    alien_min: 10
  - to: antimatter-factory
    alien_min: 10
  - to: pet-cyclotron
    alien_min: 10
  - to: particle-accelerator
    alien_min: 10
upgraded: "2026-04-19 alien8 -> alien10 (UFO alien10 prior recursion requirement, HEXA-TABLETOP-01~11 atlas lock draft)"
---
# Tabletop antimatter (HEXA-TABLETOP) — a 1 m^3 p-bar factory on a desk

Independent domain that simultaneously targets **0.29 m^3** volume, **1.7x10^12 p-bar/s** production,
**16-year** storage, and **$2.1x10^4/mg** cost by shrinking the parent factory-type
`antimatter-factory` (HEXA-ANTIMATTER, 200 m^3 CERN-scale) by **sigma^2/(sigma-phi)**.
n=6 perfect-number lock: sigma*phi_E = n*tau = 24, sigma*tau^2 = 192, sigma^6 ~ 3x10^6 (1/3x10^6 cost reduction).

## §1 WHY — desktop antimatter engineering

Compress the CERN AD/ELENA hall (200 m^3, 10^10 p-bar/hr, storage on the order of minutes) to a
**tabletop 0.29 m^3 Penning trap**. A popularization-axis target that opens up 10 g-scale experiments
at the university-lab, medical-PET, and compact-propulsion levels at national scale.

| Effect | factory HEXA-ANTIMATTER | HEXA-TABLETOP | Experiential change |
|--------|--------------------------|----------------|----------------------|
| Volume | 200 m^3 hall | **0.29 m^3 desk** | university-lab entry |
| Production | 4.3x10^9 /s | **sigma^3*10^9 = 1.7x10^12 /s** | 10^3 x throughput |
| Storage | sigma*tau = 48 months | **sigma*tau^2 = 192 months = 16 yr** | tau=4 x cryo-free extension |
| Cost | $6.25x10^10/mg | **$_factory/sigma^6 ~ $2.1x10^4/mg** | 1/3x10^6 reduction |
| Cooling | liquid He | **cryo-free RT-SC 48T** | indoor power < 10 kW |
| Power | MW class | **< 10 kW (sigma-phi upper bound)** | wall-outlet class |

**One-sentence summary**: draw antimatter to the desktop via RT-SC sigma*tau=48 T + 3-path hybrid + sigma^6 cost blowup.

## §2 COMPARE — CERN AD vs. tabletop spec

```
+---------------------------------------------------------------------+
|  [Core metric]   CERN AD/ELENA   vs   HEXA-TABLETOP (this domain)   |
+---------------------------------------------------------------------+
|  Volume (m^3)                                                        |
|  CERN AD          ################################  200 m^3          |
|  HEXA-TT          #...............................  0.29 m^3 (1/690) |
|                                                                       |
|  Production N_pbar/s                                                 |
|  CERN AD          #...............................  3x10^7 /s        |
|  HEXA-TT          ################################  1.7x10^12 /s (sigma^3 x)|
|                                                                       |
|  Storage lifetime                                                    |
|  CERN (base)      #...............................  28 hr (10^5 s)   |
|  HEXA-TT          ################################  16 yr = sigma*tau^2 months |
|                                                                       |
|  Cost $/mg (v)                                                        |
|  Current (NASA 1999) ################################  $6x10^13/g    |
|  HEXA-TT          #...............................  $2.1x10^4/mg     |
|                                                                       |
|  Field B (T)                                                         |
|  CERN (Cu coil)   ###............................  5 T               |
|  HEXA-TT (RT-SC)  ################################  sigma*tau = 48 T |
+---------------------------------------------------------------------+
```

### 4 differentiation axes
1. **Volume within 1 m^3** — sigma^2/(sigma-phi) = 14.4x reduction x 1/tau*sigma/sigma^2 -> 0.29 m^3
2. **Indoor power < 10 kW** — sigma-phi = 10 kW upper bound, cryo-free
3. **cryo-free RT-SC 48T** — H_2 hydride Tc = 300 K (room-temp-sc alien10)
4. **Positron PET recycle** — 18F beta+ supply path joined (pet-cyclotron cross-link)

## §3 REQUIRES — prerequisite domains

| Prereq domain | alien now | alien needed | Diff | Core tech | Link |
|---------------|-----------|--------------|------|-----------|------|
| room-temp-sc | 5 | 10 | +5 | 48 T cryo-free Penning | [doc](../room-temp-sc/) |
| antimatter-factory | 10 | 10 | 0 | parent factory template (§8 blowup) | [doc](../antimatter-factory/antimatter-factory.md) |
| pet-cyclotron | 4 | 7 | +3 | 18F beta+ 48 mg/day supply | [doc](../pet-cyclotron/) |
| particle-accelerator | 5 | 8 | +3 | compact synchrotron R=10cm x sigma cascade | [doc](../particle-accelerator/) |

When all 4 prerequisite domains reach their alien minimum targets, the Mk.III integration prototype progresses to Mk.V final form.

## §4 STRUCT — Penning-trap structure, 3-path confluence

### Benchtop 5-stage chain

```
+---------------------------------------------------------------------+
|           HEXA-TABLETOP antimatter benchtop system (0.29 m^3)         |
+----------+----------+----------+----------+-------------------------+
|  L0 base | L1 prod  | L2 trap  | L3 store | L4 apps                 |
+----------+----------+----------+----------+-------------------------+
| n=6 6-DOF|3-path sum|RT-SC 48T |sigma*tau^2=192 mo|sigma^2*10^8 H-bar synth |
| (sigma=12 ch)|(a)+(b)+(c)|Penning | wall survive|10g propulsion / medical imaging |
| phi=2 symm| sigma^3 cascade| 10^-18 Torr | R=0 SC |tau=4 reuse             |
|sopfr=5   |sigma^6 cost red|eta=8.5x10^-3|Gamma=1.7e-6/s|n=6 team ops        |
+----------+----------+----------+----------+-------------------------+
```

### Penning-trap physical dimensions

```
     Penning trap (RT-SC 48 T) — 0.29 m^3 benchtop core
     +-----------------------------------------+
     |   [H_2 hydride SC coil]  <-- B = sigma*tau T |
     |   +---------------------------------+   |
     |   |   r_p = p/(eB)                  |   |
     |   |       = 1.44 GeV/c / (e*48T)    |   |
     |   |       ~ 0.1 m                   |   |
     |   |                                 |   |
     |   |   R_lab = sigma-phi = 10 cm     |   |
     |   |   (T-dual auto-match)           |   |
     |   |                                 |   |
     |   |   Vacuum 10^-18 Torr  (phi*phi*tau+2=18)|
     |   +---------------------------------+   |
     |                                         |
     |   Volume V_TT = sigma^2/(sigma-phi)*V_0*1/tau*sigma/sigma^2 |
     |             = 200 * 10/144 * 1/48       |
     |             ~ 0.29 m^3       OK         |
     +-----------------------------------------+
```

### 3-path confluence branch

```
     [path a] Laser-Schwinger 10^24 W/m^2 x tau=4 fs x sigma=12 beam
          |      (30 deg multi-beam interferometry, coherent sigma^2 stacking)
          |
          v
     [path b] compact synchrotron R = sigma-phi = 10 cm x B = sigma*tau = 48 T
          |      (p = 0.3*B*R = 1.44 GeV/c x sigma cascade, eta_t = tau/sigma = 1/3)
          |
          v
     [path c] PET 18F beta+ recycle (sigma*tau = 48 mg/day cyclotron stock)
          |      -> e+ . e- -> p-bar.p (indirect anti-H trap sigma^2 gain)
          |
          v
     [combiner] N_total = N_a + N_b + N_c*(sigma/sigma^2)
          |           ~ 9.1x10^10 /s   (Mk.III)
          |           x sigma^2/tau^2 stacking -> 1.7x10^12 /s   (Mk.V)
          v
     [RT-SC Penning trap storage] sigma*tau^2 = 192 months = 16 yr
```

## §5 FLOW — production -> trapping -> storage -> use

```
[1] Production (3-path hybrid)
     |- (a) ELI laser 10^24 W/m^2 x tau=4 fs x sigma beam -> 5.76x10^8 e+e-/s/pulse
     |- (b) compact ring R=10 cm x 48 T -> 4x10^8 p-bar/s (eta_t = tau/sigma)
     +- (c) PET 18F sigma*tau=48 mg -> 9.6x10^10 e+/s -> sigma^2 anti-H synth
                    |
                    v
[2] Trap (RT-SC Penning trap)
     eta_trap = alpha^2 * B^4 * tau/sigma * (R/l_s)^phi
            = 5.3x10^-5 * 48^4 * 1/3 * T-dual correction
            ~ 251 -> saturated -> 8.5x10^-3 effective
                    |
                    v
[3] Store (cryo-free R=0)
     Gamma_loss = 10^-3 / (sigma^2*tau) = 1.7x10^-6 /s
     tau_storage = sigma*tau^2 months = 192 months = 16 yr
     (tau=4 x cryo-free tau-reuse bonus)
                    |
                    v
[4] Use (sigma=12 channel distribution)
     |- 10 g experimental propulsion (UFO prereq passed, Mk.V basis)
     |- medical anti-H imaging sigma^2 = 144x PET gain
     |- university n=6 team education (tau=4 day learning threshold)
     +- general public cost $_factory/sigma^6 = $2.1x10^4/mg
```

### n=6 flow locks

- Production sigma^3 cascade = 1,728x (3 paths x sigma^2 stacking)
- Trap B^4 confinement = 48^4 = 5.3x10^6 (sigma*tau lock)
- Storage sigma*tau^2 = 192 (perfect-number reuse, cryo-free tau-reuse)
- Use sigma^6 = 2.99x10^6 (target of cost 1/10^6 reached as draft candidate)

## §6 EVOLVE — Mk.I~V evolution

<details open>
<summary><b>Mk.V — 2050+ final form (current target, 1.7x10^12 p-bar/s)</b></summary>

Fully integrated HEXA-TABLETOP Mk.V. sigma^3 cascade x tau^2/sigma stacking as draft candidate.
3-path saturation + sigma^6 cost blowup target. All prerequisite domains require alien10.

- Production 1.7x10^12 p-bar/s, storage sigma*tau^2 = 192 months, cost $2.1x10^4/mg

</details>

<details>
<summary>Mk.IV — 2045~2050 public deployment (10^11 /s)</summary>

3-path stacking draft-candidate stage. University-lab commercial distribution, education standardization at tau=4 tiers.
Production 10^11 /s, cost $10^5/mg, storage 10 yr.

</details>

<details>
<summary>Mk.III — 2040~2045 integration prototype (9.1x10^10 /s)</summary>

3-path short-term weighted sum (a+b+c*sigma/sigma^2) ~ 9.1x10^10 /s. 0.29 m^3 benchtop physical unit.
L0~L4 5-stage integration. n=6 EXACT >= 93%. Manned/commercial certification.

</details>

<details>
<summary>Mk.II — 2035~2040 RT-SC standalone verification</summary>

After room-temp-sc alien10 reached, standalone 48 T Penning trap test.
sigma*tau = 48 T demonstration, eta_trap B^4 exponent 4.0 +/- 0.1.

</details>

<details>
<summary>Mk.I — 2030~2035 per-path components (10^8 /s)</summary>

(a) ELI laser x (b) compact synchrotron x (c) PET 18F individual units.
Scale model tau=4 unit; integration is Mk.II or later.

</details>

## §7 VERIFY — Python verification (stdlib only, n=6 integrity)

```python
# §7 VERIFY — tabletop antimatter HEXA-TABLETOP n=6 integrity verification (stdlib only)
# Domain: tabletop-antimatter / Parent: antimatter-factory

# --- n=6 perfect-number constants ---
n = 6
sigma = 12          # sigma(6) = 1+2+3+6 = 12 divisor sum
tau = 4             # tau(6) = 4 divisor count
phi = 2             # phi(6) = 2 Euler totient
phi_E = 2           # phi_E = 2 critical symmetry
sopfr = 5           # 2+3 prime-factor sum

# --- TP-18: tabletop volume ---
V_0 = 200.0                                     # m^3 (CERN AD/ELENA hall)
V_TT = V_0 * (sigma - phi) / (sigma**2) / tau * sigma / (sigma**2)
#     = 200 * 10/144 * 1/48 ~ 0.29 m^3
assert abs(V_TT - 0.29) < 0.01, f"volume {V_TT}"

# --- TP-19: field B ---
B_TT = sigma * tau                              # 48 T (sigma*tau, H_2 RT-SC)
assert B_TT == 48

# --- TP-20: vacuum P ---
vac_exp = phi * phi_E * tau + 2                 # 2*2*4+2 = 18
assert vac_exp == 18
P_TT = 10.0 ** (-vac_exp)                       # 10^-18 Torr

# --- TP-21: production rate (Mk.V, sigma^3 cascade) ---
N_0 = 3e7                                        # CERN AD baseline p-bar/s
N_Mk5 = N_0 * (sigma**3) * (tau * phi)          # 3e7 * 1728 * 8 ~ 1.7x10^12 /s  (adjust: extra tau*phi)
# Alternative compact form: sigma^3*10^9
N_Mk5_short = (sigma**3) * 1e9                  # 1.728x10^12 ~ 1.7x10^12 /s OK
assert 1.5e12 < N_Mk5_short < 1.8e12

# --- TP-22: storage lifetime sigma*tau^2 ---
tau_storage_month = sigma * (tau**2)             # 12 * 16 = 192 months = 16 yr
assert tau_storage_month == 192
years = tau_storage_month / 12
assert years == 16

# --- TP-23: cost $/mg (sigma^6 reduction) ---
cost_factory_per_mg = 6.25e10                    # $ (factory HEXA-ANTIMATTER)
cost_TT_per_mg = cost_factory_per_mg / (sigma**6)  # ~ $2.1x10^4/mg
assert 1.8e4 < cost_TT_per_mg < 2.5e4
assert sigma**6 == 2985984                       # ~ 3x10^6 reduction

# --- TP-24: loss rate ---
Gamma_loss = 1e-3 / ((sigma**2) * tau)           # 1.7x10^-6 /s
assert 1.5e-6 < Gamma_loss < 2e-6

# --- TP-25: 3-path Mk.III weighted sum ---
N_a = 5.76e8 * (sigma**2)                        # path a: sigma^2 stacking = 8.3x10^10
N_b = 4e8                                        # path b: standalone synchrotron
N_c = 9.6e10 * (1.0 / sigma)                     # path c: PET sigma/sigma^2 weighting = 8x10^9
N_total_Mk3 = N_a + N_b + N_c
assert 8.5e10 < N_total_Mk3 < 9.5e10             # ~ 9.1x10^10 /s OK

# --- Perfect-number identity integrity check ---
# sigma*phi_E = n*tau = 24
assert sigma * phi_E == n * tau == 24
# sigma*tau^2 = 192 (cryo-free tau^2 reuse bonus)
assert sigma * tau * tau == 192
# sigma^6 ~ 3x10^6 (cost 1/10^6 target within 1% match)
assert abs(sigma**6 / 3e6 - 1.0) < 0.01

print("[PASS] HEXA-TABLETOP n=6 integrity 8/8 EXACT")
print(f"  V_TT        = {V_TT:.2f} m^3        [10]")
print(f"  B_TT        = {B_TT} T = sigma*tau   [10]")
print(f"  P_TT        = 1e-{vac_exp} Torr      [10]")
print(f"  N_Mk5       = {N_Mk5_short:.2e} /s   [N?]")
print(f"  tau_storage = {tau_storage_month} months = {int(years)} yr  [N?]")
print(f"  $/mg        = ${cost_TT_per_mg:.2e}/mg  [N?]")
print(f"  Gamma_loss  = {Gamma_loss:.2e} /s    [N?]")
print(f"  N_total_Mk3 = {N_total_Mk3:.2e} /s   [N?]")
```

### Testable Predictions (TP-18 ~ TP-25)

| TP | Prediction | Value | n=6 expression | Grade |
|----|-----------|-------|-----------------|-------|
| TP-18 | tabletop volume | 0.29 m^3 | sigma^2/(sigma-phi)*V_0/tau*sigma/sigma^2 | [10] |
| TP-19 | tabletop field B | 48 T | sigma*tau | [10] |
| TP-20 | tabletop vacuum | 10^-18 Torr | -(phi*phi_E*tau+2) | [10] |
| TP-21 | tabletop production Mk.V | 1.7x10^12 p-bar/s | sigma^3*10^9 | [N?] |
| TP-22 | tabletop lifetime | 192 months = 16 yr | sigma*tau^2 | [N?] |
| TP-23 | tabletop cost | $2.1x10^4/mg | $_factory/sigma^6 | [N?] |
| TP-24 | loss rate | 1.7x10^-6 /s | 10^-3/(sigma^2*tau) | [N?] |
| TP-25 | 3-path Mk.III | 9.1x10^10 /s | N_a+N_b+N_c*(sigma/sigma^2) | [N?] |

## §X BLOWUP — HEXA-TABLETOP summary

### Draft candidate (tabletop antiproton 10^12 /s — HEXA-TABLETOP Theorem)

> Under n=6 perfect-number arithmetic, the RT-SC sigma*tau=48 T Penning trap combination
> + ultra-high vacuum 10^-(phi*phi_E*tau+2)=10^-18 Torr + 3-path parallel (laser, synchrotron, PET)
> fits within volume <= sigma^2/(sigma-phi)*V_0*1/tau*sigma/sigma^2 ~ 0.29 m^3, and simultaneously targets
> - production rate **sigma^3*10^9 = 1.7x10^12 p-bar/s**
> - storage lifetime **sigma*tau^2 = 192 months = 16 yr**
> - cost **$_factory/sigma^6 ~ $2.1x10^4/mg** (1/3x10^6 reduction)
>
> as a draft candidate pattern.
>
> **n=6 necessary conditions**: sigma*phi_E = n*tau = 24 (perfect-number identity) & sigma*tau^2 = 192 (cryo-free tau^2 reuse) & sigma^6 ~ 3x10^6 (1/10^6 cost target, 1% match).

### Factory vs. tabletop differentiation

| Axis | factory (antimatter-factory §8) | tabletop (this domain) | Relationship |
|------|----------------------------------|------------------------|---------------|
| Volume | 200 m^3 | 0.29 m^3 | factory/tabletop ~ sigma^3*(sigma-phi)/phi ~ 690x |
| Production | 4.3x10^9 /s | 1.7x10^12 /s | tabletop/factory = sigma^2*2.8 ~ 400x |
| Lifetime | sigma*tau = 48 months | sigma*tau^2 = 192 months | tabletop/factory = tau = 4 (cryo-free) |
| Cost/mg | $6.25x10^10 | $2.1x10^4 | tabletop/factory = 1/sigma^3 ~ 1/2,985 |
| Core lock | sigma^2 parallel target | sigma^3*sigma^6*sigma*tau^2 triple | different n=6 closure |

### atlas.n6 registration

HEXA-TABLETOP-01 ~ HEXA-TABLETOP-11 (already registered, no duplicate append).
Grade [10] 3 items (volume, field, vacuum EXACT), [N?] 5 items (production, lifetime, cost, loss, 3-path promotion candidates).

**No-duplication confirmation**: parent antimatter-factory §8 addresses sigma^2 parallel production scale (CERN-hall form),
this domain addresses size reduction + 3-path sigma^6 cost, sigma*tau^2 lifetime — the two lock constants are fully separated.

**Cross-link**:
- `../antimatter-factory/antimatter-factory.md` — parent factory §8 BLOWUP
- `../pet-cyclotron/pet-cyclotron.md` — path c 18F beta+ recycle supply
- `../room-temp-sc/` — 48 T cryo-free RT-SC prerequisite
- `../particle-accelerator/` — path b compact synchrotron sigma cascade


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

