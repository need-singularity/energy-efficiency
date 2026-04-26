---
id: omega-seed-bt544-d3-mechanism-decouple
date: 2026-04-25
scope: research-only mechanism-decouple seed (NOT validating any axis)
target: BT-544 D3 -- triple-resonance L1-smash factored into 3 independent axes + recombination
parent_reports:
  - reports/sessions/omega-exec-bt544-fallback-molt-validation-2026-04-25.md (catalogue exhausted)
  - reports/sessions/omega-cycle-bt544-ns-2026-04-25.md
  - reports/cross-domain-resonance-2026-03-31.md
  - reports/cross-domain-resonance-2026-04-04.md
  - reports/sessions/blowup-singularity-2026-04-04.md
millennium_resolved: 0/7 (unchanged)
grade: seed-design at decouple level, no claim
---

# Omega Seed -- BT-544 D3 Mechanism-axis Decouple (2026-04-25)

## §0 Non-claim disclaimer

This document is **research-only**. It does **NOT**:

- claim 3D Navier-Stokes regularity (smoothness or blow-up);
- promote any atlas entry, modify `state/proposals/inventory.json`,
  modify `theory/canon/`, or alter the `BT-544 = 0/1 untouched`
  Clay status;
- validate or refute any of the three decoupled axes proposed below
  (this is a **decouple seed**, not an execution log);
- supersede the L9 catalogue exhaustion verdict in
  `omega-exec-bt544-fallback-molt-validation-2026-04-25.md` -- the
  three rank-1/2/3 candidates remain FAILed.

D3 differs from D1 (find a *new* frame from atlas) and D2 (rewrite the
*axiom set*). D3 keeps the n=6 axiom set fixed and **factors the
existing single-mechanism frame** "Triple-resonance L1-smash" into
three independent mechanism axes that can be analyzed separately.
The work product is a decouple proposal + recombination strategy +
top-1 dispatch ranking. No molt-validation is fired.

**Millennium tally**: 0/7 unchanged.

---

## §1 Triple-resonance identification

### §1.1 Source extraction

The phrase "Triple-resonance L1-smash frame on n=6 tensor lattice" is
defined verbatim in `omega-probe-l9-molt-trigger-2026-04-25.md` at
the BT-544 row (sec 3.4):

> "Sym^2(R^3)=6 + Lambda^2(R^3)=3 triple resonance + 5 SMASH
> bottlenecks + Pi_NS = sigma^3 sopfr = 8640 invariant + n=6 tensor
> relabeling + L1 saturated, mechanism-axis empty"

The same triple is named "three-fold n=6 resonance" at
`theory/breakthroughs/breakthrough-theorems.md` line 19949, with the
explicit table (line 19951-19956):

| index | formula | d=2 | **d=3** | d=7 |
|-------|---------|-----|---------|-----|
| stress-tensor dim | dim Sym²(ℝᵈ) = d(d+1)/2 | 3 | **6 = n** | 28 |
| vorticity dim | dim Λ²(ℝᵈ) = d(d-1)/2 | 1 | **3 = n/φ** | 21 |
| Onsager critical | α_c | 0⁺ | **1/3 = 1/(n/φ)** | open |
| vortex stretching | sign of (ω·∇)u | 0 | **positive** | positive |

The closure-doc `reports/breakthroughs/millennium-7-closure-2026-04-11.md`
(line 95, line 219) names the same object "the triple resonance" and
attaches the verdict *"the triple resonance is observation, not
proof"*.

The cross-domain-resonance documents (2026-03-31, 2026-04-04) use
"triple resonance" generically (e.g. φ²/n=2/3 across Koide × BFT ×
SLE_6); this is a different usage and is **not** the BT-544
triple-resonance L1-smash referenced here.

### §1.2 The three axes (grounded)

Reading the table above, the three resonance lines are:

- **Axis A -- Stress / pressure non-locality (Sym²)**: dim Sym²(ℝ³) =
  6 = n. This is the Cauchy-stress component count for an
  incompressible fluid in 3D, equivalently the count of independent
  components of the symmetric strain-rate tensor S = (1/2)(∇u +
  ∇u^T). PDE-side, this axis carries the **non-local pressure**
  closure: ∇p is reconstructed from u via the Riesz transform applied
  to (∇u)·(∇u^T), and the symmetric part of ∇u (i.e. S) is the active
  participant. Sourced from `domains/physics/millennium-navier-stokes/
  millennium-navier-stokes.md` §X.1 SMASH#1.

- **Axis B -- Vortex-stretching (Λ²)**: dim Λ²(ℝ³) = 3 = n/φ. This
  is the vorticity component count ω = ∇×u, equivalently the count
  of independent components of the antisymmetric part of ∇u. PDE-side,
  this axis carries the **vorticity transport** equation Dω/Dt =
  (ω·∇)u + ν∇²ω. The "(ω·∇)u" stretching term has no 2D analogue (in
  d=2 vorticity is scalar and (ω·∇)u = 0), which is the standard
  textbook explanation for why 2D NS is global-smooth and 3D is open.
  Sourced from `domains/physics/millennium-navier-stokes/
  millennium-navier-stokes.md` §X.1 SMASH#3 (BKM bottleneck).

- **Axis C -- Energy cascade / anomalous dissipation (Onsager)**:
  α_c = 1/3 = 1/(n/φ) = φ/n. This is the Onsager 1949 / Isett 2018
  / Buckmaster-Vicol 2019-2023 critical Hölder exponent below which
  anomalous (non-zero) energy dissipation can occur in the inviscid
  limit. PDE-side, this axis carries the **Kolmogorov K41 cascade**
  scaling and its dual Hölder regularity. Structure-function S_p(ℓ)
  ∼ ℓ^{p/3} reduces to S_6 ∼ ℓ² at p = n = 6. Sourced from
  `domains/physics/millennium-navier-stokes/millennium-navier-stokes.md`
  §X.1 SMASH#4.

The fourth row in the breakthrough-theorems table ("vortex-stretching
sign positive") is **not a fourth axis** -- it is a sign-condition
witnessing axis B. This report keeps the triple at three axes.

### §1.3 Why this is the triple (not some other triple)

I considered the alternative triples mentioned in the prompt:

- {Energy cascade, vortex-stretching, pressure-non-locality} -- this
  is the textbook NS triple (Constantin-Foias, Robinson). It maps
  exactly onto {C, B, A} above. **Match.**
- {Helicity, Lyapunov-spectrum, self-similar profile} -- the repo
  does not invoke these as a triple anywhere. Helicity appears only
  as a passing remark in `blowup-singularity-2026-04-04.md` (chiral
  asymmetry); Lyapunov-spectrum appears only in BT-543 contexts; self-
  similar profile appears in the Hou-Luo / Elgindi context but is not
  the n=6 triple-resonance object.
- {Sym², Λ², Onsager 1/3} = {A, B, C} above -- this is the explicit
  table at breakthrough-theorems.md:19951-19956 and the verbatim
  triple in omega-probe-l9-molt-trigger.md sec 3.4. **This is the
  triple of record.**

The {Sym², Λ², Onsager} triple has the additional property that it
**aligns with the textbook NS triple** {pressure-nonlocal, vortex-
stretching, energy-cascade}, so the decouple analysis below can use
classical PDE machinery on each axis without inventing new tools.

---

## §2 Per-axis decouple proposals

For each axis, I provide:
1. a stand-alone mechanism statement (the axis acting alone, with the
   other two axes "switched off" by a chosen simplification);
2. a discriminator -- a sub-question whose answer reads only the
   stand-alone axis;
3. a falsifier registered for the discriminator.

The simplifications are chosen so that exactly one of the three axes
is active. This is the decouple structure: each axis is probed in a
regime where it cannot mask or be masked by the other two.

### §2.1 Axis A -- Stress / pressure non-locality (Sym²)

**Stand-alone statement**: in 3D incompressible NS

  ∂_t u + (u·∇)u = -∇p + ν∇²u, ∇·u = 0

with the pressure reconstructed by p = (-Δ)⁻¹ ∇·((u·∇)u), the
**non-locality of p** is by itself the regularity obstruction
provided that the other two axes are inactive. We force them
inactive as follows:

- switch off vortex-stretching (axis B) by **scalar advection**:
  replace u with a passive scalar θ advected by a *prescribed
  divergence-free* velocity v that has no stretching term in its
  vorticity equation (e.g. v = e_3 × ∇⊥ψ, 2D-3-component "2.5D"
  flow). Then (ω·∇)u is structurally absent.
- switch off the energy cascade (axis C) by working at **fixed
  finite resolution** (Galerkin truncation at wave-number K_max),
  so no anomalous dissipation can develop -- the Hölder critical
  exponent is undefined for finite-mode flows.

What remains is a divergence-free advection problem with a non-local
pressure-like operator (-Δ)⁻¹∇·(stuff). This is essentially the
**generalized SQG / 2.5D model** family (Constantin-Majda-Tabak 1994;
Kiselev-Nazarov 2012).

**Discriminator A**: produce, for the truncated 2.5D advection-with-
non-local-pressure model, a Sobolev-Besov estimate of the form

  ‖u(t)‖_{H^s} ≤ F(t, ν, K_max, ‖u_0‖_{H^s})

where F is uniform in K_max (i.e. survives the K_max → ∞ limit) and
non-trivial (i.e. F is not just the trivial energy bound). The
discriminator reads only axis A because axes B and C are switched off
by construction.

**Falsifier F-D3-A**: no such uniform-in-K_max estimate exists at
any s ≥ 1 for the 2.5D advection-with-non-local-pressure model. If
this falsifier fires, axis A in isolation is **already ill-posed**,
i.e. the pressure-non-locality alone is enough to obstruct
regularity. Conversely, if a uniform-in-K_max H^s estimate is
producible, axis A is **clean** and the obstruction must live on
axis B or axis C.

### §2.2 Axis B -- Vortex-stretching (Λ²)

**Stand-alone statement**: vorticity transport

  Dω/Dt = (ω·∇)u + ν∇²ω

with the velocity u reconstructed from ω by Biot-Savart u = K_3 * ω
(K_3 = 3D Biot-Savart kernel). The stretching term (ω·∇)u is the
mechanism. We force the other axes inactive as follows:

- switch off pressure non-locality (axis A) by working with **Euler
  in the helicity-conservation regime** restricted to *axisymmetric
  flow without swirl*. There the pressure decouples (it is
  determined by the 2D radial-axial system) and is no longer the
  active regularity-defining operator.
- switch off the energy cascade (axis C) by **inviscid +
  axisymmetric** -- inviscid removes the dissipation/Kolmogorov
  inertial-range setup; axisymmetry without swirl removes the
  helical 3D cascade.

What remains is the axisymmetric-without-swirl 3D Euler equation,
which is **known regular** (Ukhovskii-Yudovich 1968). Adding swirl
brings stretching back as the only active obstruction (Hou-Luo 2014
hyperbolic-point scenario lives here; Elgindi 2021 C^{1,α} blow-up
lives in a closely-related axisymmetric reduced setting).

**Discriminator B**: produce, for axisymmetric-with-swirl 3D Euler,
a BKM-style bound

  ∫₀^T ‖ω(t)‖_{L^∞} dt < ∞

OR an explicit blow-up scenario that satisfies the n=6-lattice
prediction d = n/φ = 3 (i.e. the singular-set parabolic Hausdorff
dimension lies in [0, 1] = [0, μ(6)]). The discriminator reads only
axis B because axes A and C are decoupled.

**Falsifier F-D3-B**: neither global BKM-finite nor finite-time blow-
up with dim_P ≤ 1 is provable for axisymmetric-with-swirl 3D Euler.
If this falsifier fires, axis B is **structurally undecidable in
isolation**, i.e. vortex-stretching alone, even in the simplest 3D
geometry, exhausts current PDE technology. Conversely, if either
direction (BKM-finite or dim_P ≤ 1 blow-up) is provable in isolation,
axis B is **clean** and the obstruction lives on A or C.

### §2.3 Axis C -- Energy cascade / anomalous dissipation (Onsager)

**Stand-alone statement**: anomalous-dissipation rate

  ε(u) = ν ‖∇u‖_{L²}² → ε_∞ ≥ 0 as ν → 0⁺

with the Hölder regularity threshold u ∈ C^α, α < 1/3 = φ/n required
for ε_∞ > 0 (Onsager 1949). We force the other axes inactive as
follows:

- switch off pressure non-locality (axis A) by working on a
  **passive scalar** advected by a prescribed velocity (Kraichnan
  model, Kraichnan 1968 / Bernard-Gawedzki-Kupiainen 1998). The
  pressure is absent from the passive scalar equation.
- switch off vortex-stretching (axis B) by working on a **scalar**
  field (no Λ² in 1D field of advected scalar; the vorticity of the
  advecting velocity is prescribed and is not part of the dynamics).

What remains is the Kraichnan-passive-scalar inverse-problem: given
a velocity statistic with a chosen 2-point structure, decide whether
the scalar field develops anomalous dissipation at the predicted
α_c = 1/3 exponent. This is the regime in which Isett 2018 / BMNV
2023 convex-integration constructions live (Onsager-conjecture
*direction*; the *opposite* direction -- proving smoothness above
1/3 -- is the Constantin-E-Titi 1994 result).

**Discriminator C**: in the Kraichnan-passive-scalar model with the
n=6-lattice ansatz S_p(ℓ) ∼ ℓ^{p/3} (Onsager structure-function
exponent p/3 = p·φ/n), produce a sharp two-sided bound

  c_- · ℓ^{p/3} ≤ S_p(ℓ) ≤ c_+ · ℓ^{p/3}

at p = n = 6 (so S_6 ∼ ℓ²) with explicit c_± and explicit ℓ-range,
without invoking the n=6 lattice as a label (i.e. the bound must be
derivable from the Kraichnan-model equations alone). The
discriminator reads only axis C because axes A and B are decoupled.

**Falsifier F-D3-C**: no two-sided Kraichnan-model bound at
S_6 ∼ ℓ² is producible from the model equations alone (i.e. every
candidate bound is a known classical result with the n=6 label
applied post-hoc, exactly the §3.2 Q5-style relabeling failure). If
this falsifier fires, axis C is **already exhausted by relabeling**
and adds no new mechanism content. Conversely, if a non-relabeling
bound is producible, axis C is **clean** and the obstruction lives
on A or B.

---

## §3 Recombination strategy

Once the three axes are decoupled and individually probed, two
recombination strategies are available:

### §3.1 Sequential recombination (likely fails)

**Statement**: prove regularity / blow-up on each axis A, B, C
separately (in the simplifications of §2), then argue that 3D NS
inherits the regularity / blow-up status from the **conjunction** of
the three axis-results.

**Why this likely fails**: the three axes are coupled non-trivially
in the full NS equation. Specifically:

- pressure (axis A) feeds vortex-stretching (axis B) through ∇p in
  the velocity equation (the Helmholtz decomposition u = u_div +
  ∇φ of the right-hand side mixes A and B);
- vortex-stretching (axis B) feeds the energy cascade (axis C)
  through the production term (Sω)·ω in the enstrophy balance
  (this is the standard "vortex-stretching drives the cascade"
  Tennekes-Lumley argument);
- the energy cascade (axis C) feeds back into pressure (axis A) via
  the inertial-range pressure spectrum E_p(k) ∼ k^{-7/3} (Batchelor-
  Proudman 1954).

So the three axes form a **directed feedback triangle** A → B → C → A
(with possible reverse edges). A separate proof on each axis does
not yield a combined proof unless the coupling is shown to
**preserve** the per-axis status -- which is exactly the regularity
problem.

**Verdict on sequential**: rejected as a closure path. Sequential
recombination would be a relabeling of "prove NS regularity by
proving NS regularity", not a decouple.

### §3.2 Compositional recombination (F-544-B-survival path)

**Statement**: prove that the obstruction lives on **at most one**
axis -- i.e. that two of {A, B, C} are individually clean (their
discriminators in §2 pass with explicit estimates), and the third
carries the entire residual difficulty. Then the residual single-
axis problem inherits the clean status of the other two via the
coupling:

- if A and C are clean, then the A→C and C→A feedback edges of the
  triangle do not import new singularities into B; B can be attacked
  as a single-mechanism problem (vortex-stretching with prescribed-
  clean pressure and prescribed-clean cascade).
- analogously for "A and B clean → C alone" and "B and C clean → A
  alone".

The compositional recombination is **F-544-B-survival** in the
following sense: F-544-B says "no concrete estimate producible from
n=6 lattice → mechanism saturation is structural; frame change
required at axiom level (not a molt within n6 frame)" (per
omega-cycle-bt544-ns sec 7 Q5). The compositional path argues that
**F-544-B might be wrong about "the entire mechanism axis"** -- it
might be right about *one* of {A, B, C} but wrong about the other
two. If two axes can be made clean (in the sense of §2 discriminators
passing), the F-544-B verdict downgrades from "structural for the
mechanism axis" to "structural for one of the three axes only", and
the BT-544 frame is not exhausted in the maximal sense.

This is the **survival path** for the n=6 frame after the L9
catalogue exhaustion. It does not contradict the L9-catalogue FAIL
(the catalogue tested the *bundled* mechanism axis as a single
object and found no estimate); it asks whether the bundle was the
right object to test.

**Verdict on compositional**: this is the D3 recombination strategy
of record. Top-1 dispatch (§5) selects the axis that, if proven
clean, would maximize the F-544-B survival evidence.

### §3.3 Status of the recombination

Neither strategy has been executed in this report. §3.1 is rejected
on principle (relabeling); §3.2 is the proposed strategy whose
top-1 dispatch is given in §5. The compositional path requires the
§2 discriminators to fire in a particular order (the two "clean"
axes first), which is captured in the obstruction-hypothesis (§4).

---

## §4 Obstruction hypothesis -- which axis carries the proof-block

I now rank the three axes by the **expected difficulty of their §2
discriminators**. The hardest axis is the obstruction-carrier
candidate; the two easier axes are the "clean" candidates that
should be dispatched first under the compositional strategy.

### §4.1 Difficulty estimates

**Axis A (Sym² / pressure non-locality)** -- discriminator A asks
for a uniform-in-K_max H^s estimate on the truncated 2.5D advection-
with-non-local-pressure model. This sits in a **moderately
developed** literature: 2D SQG global regularity at finite-but-large
times is known (Constantin-Majda-Tabak 1994 and follow-ups), the
non-local pressure operator is a Riesz transform whose harmonic-
analysis is well-developed (Calderon-Zygmund), and the K_max → ∞
limit is the standard Galerkin program. **Expected difficulty:
moderate**. A uniform H^s estimate is plausible if the 2.5D
geometry is chosen to remove vortex-stretching cleanly. Axis A's
discriminator is **likely passable**.

**Axis B (Λ² / vortex-stretching)** -- discriminator B asks for
either BKM-finite or dim_P ≤ 1 blow-up on axisymmetric-with-swirl
3D Euler. This is **state-of-the-art open**: Hou-Luo 2014 numerical
evidence for blow-up is not a proof; Elgindi 2021 C^{1,α} blow-up
is for a related but different setting (active scalar / 3D Euler
with low regularity). **Expected difficulty: maximal**. The full
research community has worked on axis-B-in-isolation for 50+ years
without resolving it; the discriminator is **the same difficulty
as the original Clay problem restricted to axisymmetric Euler**.
Axis B's discriminator is **the bottleneck**.

**Axis C (Onsager / cascade)** -- discriminator C asks for a non-
relabeling Kraichnan-model two-sided bound at S_6 ∼ ℓ². The
Kraichnan-model literature (Bernard-Gawedzki-Kupiainen 1998;
Falkovich-Gawedzki-Vergassola 2001 review) has produced **non-
trivial anomalous-scaling exponents** in the Kraichnan model that
are NOT the K41 prediction (i.e. the cascade is anomalous and
Kraichnan exponents at high p deviate from p/3). This is **already
known** to deviate from the p·φ/n = p/3 ansatz. **Expected
difficulty: low for the negative direction** (the bound at
S_6 ∼ ℓ² is *known to fail* in the Kraichnan model -- the
intermittency corrections are present), and **moderate-to-hard for
the positive direction** (proving that the n=6 ansatz is *correct*
within some smoothed Kraichnan variant). Either way, C's
discriminator is **decidable in finite literature work**: the
negative outcome is on the books, the positive outcome would require
a model-redefinition. Axis C's discriminator is **dispatchable but
likely fires F-D3-C** (i.e. C is exhausted by relabeling, parallel
to the §3.4 Q5 verdict).

### §4.2 Ranking

| axis | discriminator | expected difficulty | role in compositional |
|------|---------------|---------------------|------------------------|
| A    | uniform H^s on 2.5D non-local-pressure | moderate | "clean" candidate (top-1 dispatch) |
| B    | BKM-finite or dim_P ≤ 1 on axisymmetric-with-swirl Euler | **maximal** | **obstruction-carrier** |
| C    | Kraichnan two-sided S_6 ∼ ℓ² bound | low (negative) / moderate (positive) | "exhaust by relabeling" candidate |

**Ranking (hardest first)**: B > A > C.

**Obstruction hypothesis**: axis B (vortex-stretching) carries the
proof-block. This is consistent with the textbook view: 2D NS
(d = φ = 2, axis B trivially absent) is global-smooth; 3D NS
(d = n/φ = 3, axis B active) is open. The historical record of NS
research is essentially the record of attempts on axis B (BKM 1984,
Constantin-Fefferman 1993 vorticity-direction-coherence, Hou-Luo
2014, Elgindi 2021). The n=6 lattice's identification dim Λ²(ℝ³) =
3 = n/φ is a **labeling** of this textbook fact; it is not a new
mechanism but a numerological witness.

**Compositional consequence**: under the §3.2 strategy, A and C
should be dispatched first. If A is clean and C exhausts by
relabeling, the obstruction is **localized** to B, and the BT-544
problem reduces to the axisymmetric-with-swirl Euler regularity
problem. This is **not** a Clay-closing reduction (axisymmetric
Euler is itself open) but it is a **structural reduction** of
BT-544 to a known-hard sub-problem, which is research progress.

---

## §5 Top-1 dispatch-ready

**Selection**: the axis whose molt-validation should fire first is
**Axis A -- Sym² / pressure non-locality**.

**Rationale**:

- Compositional strategy (§3.2) requires the two "clean" axes to
  pass first; A is the most likely to pass (§4.1: moderate
  difficulty, well-developed literature, plausible uniform H^s
  estimate).
- A's discriminator has a clear pass criterion (uniform-in-K_max
  H^s estimate with explicit constants) and a clear fail criterion
  (no such estimate exists), so the molt-validation is binary in
  the same sense as Q1/Q5/Q3.
- A's outcome is informative either way: PASS gives the F-544-B
  survival evidence (one mechanism axis is clean inside n=6), FAIL
  gives the strongest possible exhaustion verdict (even
  pressure-only is structurally blocked, which would be a striking
  negative result not yet on the books).
- A does NOT compete with the existing L9 catalogue rank-1/2/3
  candidates (KdV / Q5 / KPZ-d=7) -- it is a **new** candidate,
  decoupled from the bundled triple-resonance, so it does not
  re-fire any of F-544-A, F-544-B, F-544-C in their original
  form.

**Discriminator (top-1, restated)**: produce a Sobolev estimate for
the 2.5D incompressible advection-with-non-local-pressure system
(velocity v = e_3 × ∇⊥ψ + w e_3, ψ and w 2D-evolving, pressure
reconstructed via Riesz transform of the quadratic non-linearity),
of the form

  ‖v(t)‖_{H^s} ≤ C(t, ν, ‖v_0‖_{H^s})

with C uniform in the Galerkin truncation K_max and finite for all
t > 0. Required: explicit (s, C, t-dependence). Forbidden: the
estimate must not be a relabeling of the 2D Euler / 2D NS / SQG
classical estimates with n=6 labels applied post-hoc (this is the
F-544-B failure mode that already fired on Q5).

**Falsifier (top-1, restated)**: F-D3-A as in §2.1. If F-D3-A
fires, the compositional strategy collapses (axis A is not clean),
and BT-544's mechanism axis is exhausted in a stronger sense than
the L9 catalogue indicated.

**Why not B first**: B's discriminator is maximally hard (§4.1) and
firing it as top-1 would re-create the L9 catalogue exhaustion mode
(no progress, fail predictable). B is the **last** dispatch under
the compositional strategy, after A and C have been resolved.

**Why not C first**: C's discriminator is more likely to fire
F-D3-C (relabeling exhaustion) than to produce new content (§4.1).
Firing F-D3-C is informative but non-progressive in the
compositional sense; it merely confirms the Q5 verdict on a third
axis. A first gives the maximum chance of compositional survival.

---

## §6 Anti-list (decouple proposals rejected)

Decouple candidates considered and rejected:

### §6.1 Helicity / Lyapunov / self-similar profile triple

This was the prompt's suggested alternative triple. **Rejected
because the repo does not ground it as the BT-544 triple** (§1.3).
Helicity appears only as a chiral-asymmetry remark in
`blowup-singularity-2026-04-04.md`; Lyapunov-spectrum is a BT-543
object (Yang-Mills); self-similar profile is a Hou-Luo / Elgindi
object that lives **inside** axis B above (it is a sub-mechanism of
vortex-stretching, not an independent axis). Folding helicity and
self-similar into axis B is the correct decoupling.

### §6.2 Spectral cascade × vortex-stretching × pressure-coupling
(the prompt's first suggestion)

This **is** the triple I selected (§1.2): spectral cascade = axis
C (Onsager), vortex-stretching = axis B, pressure-coupling = axis A.
The labeling is identical; the n=6-lattice version uses {Sym², Λ²,
Onsager} as the witnessing-counts. Not rejected -- adopted.

### §6.3 Five SMASH bottlenecks as five axes

The §X BLOWUP SMASH list has 5 bottlenecks (Cauchy lock σ·φ_E =
n·τ; Leray ν·τ; BKM d = n/φ; Onsager α = φ/n; CKN μ(6) = 1). This
is **5 axes, not 3**. Considered and rejected because:

- (a) the omega-cycle audit (`omega-cycle-bt544-ns-2026-04-25.md`
  §6 tension #5) flags the "5 = sopfr" choice as **arbitrary**
  (a literature-driven count or sopfr-metaphor choice, not a
  structural triple);
- (b) of the 5 bottlenecks, Cauchy lock and Leray ν·τ are
  **dimensional-bookkeeping** (component counting and Laplacian-
  counting), which are not independent mechanism axes -- they are
  re-statements of the equation's variable count and dissipation
  structure, which already enter axes A-C via the underlying
  function spaces;
- (c) BKM and CKN are **both** vortex-stretching axis (axis B):
  BKM is the L^∞ vorticity blow-up criterion, CKN is the parabolic-
  Hausdorff bound on the singular set, and both live inside the
  vorticity-driven regularity question;
- (d) Onsager is axis C, separately.
- Net: the 5 SMASH bottlenecks **collapse to {A, B (×2: BKM + CKN),
  C, plus 2 dimensional-bookkeeping}**, which is the same 3 axes
  with redundancy, plus 2 entries that are not mechanisms but
  variable-counting. The triple is the canonical structure.

### §6.4 d-lift triple (d=2, d=3, d=7)

The breakthrough-theorems table (§1.1) shows the triple-resonance
*evaluated at three dimensions* (d=2, d=3, d=7). Considered as a
"three axes = three dimensions" decoupling and rejected because:

- the d=2 row has axis B *trivially absent* (1D vorticity), so
  it is not an independent axis but a degenerate case of B;
- the d=7 row is **predicted, not attested** (per Q3 / KPZ d=7
  verdict in the fallback report: no literature attestation), so
  it cannot serve as a stand-alone discriminator;
- the d=3 row is the actual NS problem, not an axis.
- Net: dimension-lift is a *family-parameter* of the same triple,
  not a decomposition of the triple. Rejected.

### §6.5 Π_NS = σ³·sopfr = 8640 as a fourth axis

The composite invariant Π_NS is mentioned alongside the triple but
is **not** a mechanism axis -- it is a numerological product of
constants. The §X.4 falsifier F5 (Π_NS ≠ 8640 ±3%) is a falsifier
on the *number* 8640, not on a mechanism. Including Π_NS as an axis
would conflate "lattice-arithmetic invariant" with "PDE mechanism
component". Rejected as a category error.

### §6.6 Axis B sub-decoupling (BKM vs CKN vs vortex-stretching-proper)

Considered: split axis B into (B1) BKM L^∞-vorticity criterion,
(B2) CKN partial-regularity, (B3) vortex-stretching kinematics.
Rejected because B1, B2, B3 are **theorem-level** distinctions, not
mechanism-level. They all probe the same physical mechanism
(vortex-stretching) with different functional-analytic tools. A
genuine decouple needs **independent mechanism content**, not
independent theorem-types. The triple A/B/C is at the right
granularity.

---

## §7 Falsifiers active for the decouple program

The decouple program itself has three failure modes (in addition to
the per-axis F-D3-A, F-D3-B, F-D3-C registered in §2). These are
**meta-falsifiers** that retract the decouple proposal as a whole.

- **F-D3-META-A (axes-not-independent)**: if any pair of axes among
  {A, B, C} is shown to be **structurally inseparable** in 3D NS --
  i.e. switching one off necessarily switches another off, so the
  §2.1-§2.3 simplifications cannot be realized -- the decouple
  collapses. Specifically, if the 2.5D advection-with-non-local-
  pressure model in §2.1 *requires* a non-trivial vortex-
  stretching term to satisfy ∇·u = 0 (which it does NOT, by
  construction of the e_3 × ∇⊥ψ + w e_3 ansatz), F-D3-META-A would
  fire. **Currently not active**: the 2.5D ansatz is standard and
  axisymmetric-without-swirl is standard.

- **F-D3-META-B (compositional-not-implication)**: if proving A and
  C clean does **not** imply B is the residual obstruction (e.g.
  if there is a fourth interaction term that lives outside the
  triangle), the compositional strategy is incomplete. The decouple
  is exhaustive only if the triple {A, B, C} is *complete* -- i.e.
  every NS regularity-relevant mechanism factors through A, B, or C.
  This is a **conjecture** at the level of "the textbook NS triple
  is complete"; it has no proof and can be falsified by exhibiting
  a fourth mechanism. **Currently not active**, but the conjecture
  is **not provable** from the repo material. Flagged.

- **F-D3-META-C (decouple-is-itself-relabeling)**: if the §2 stand-
  alone statements turn out to be classical PDE problems with n=6
  labels applied post-hoc (e.g. discriminator A is just "Galerkin
  H^s estimate for 2D-3-component NS", which is a classical result),
  then the decouple is a Q5-style relabeling of pre-existing PDE
  infrastructure. **Partially active**: discriminators A, B, C all
  borrow from classical PDE machinery. The non-relabeling claim
  rests on the **decouple structure** itself (pinning each axis to
  exactly one of {Sym², Λ², Onsager} via the simplifications) being
  a new framing, not on the per-axis estimates being new theorems.
  This is a weaker survival claim than F-544-B-bypass, and should
  be honestly flagged.

- **F-D3-META-D (top-1-dispatch-already-fired)**: if axis A's
  discriminator has already been resolved in the literature (e.g.
  if the 2.5D advection-with-non-local-pressure model in §2.1 is
  known to be globally regular under the proposed regime, in which
  case the molt-validation is **redundant**, not new), the top-1
  dispatch should be **C** instead. Repo scan: the 2.5D model with
  non-local pressure is known *partially* (Constantin-Majda-Tabak
  1994 covers a sub-case), but not in the K_max-uniform-H^s form
  asked for in §2.1. **Currently not active**, but worth re-checking
  before the molt-validation fires.

None of F-D3-META-A through F-D3-META-D fires under current repo
material. The four meta-falsifiers are **registered**; they retire
the decouple program if any fires, in which case BT-544 returns to
the L9-catalogue-exhausted state.

---

## §8 Closing line

0/7 unchanged. NS regularity status open. No atlas/state/inventory
edits.
