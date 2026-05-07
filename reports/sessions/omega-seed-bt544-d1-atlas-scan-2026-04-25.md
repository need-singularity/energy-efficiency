---
id: omega-seed-bt544-d1-atlas-scan
date: 2026-04-25
scope: research-only seed-design (NEW frame-shift candidates from atlas scan; NOT validating)
target: BT-544 D1 -- atlas-side scan for new frame-shift candidates after catalogue-exhaustion
parent_reports:
  - reports/sessions/omega-exec-bt544-fallback-molt-validation-2026-04-25.md (catalogue exhausted)
  - reports/sessions/omega-exec-bt544-q1-molt-validation-2026-04-25.md
  - reports/sessions/omega-cycle-bt544-ns-2026-04-25.md
  - reports/sessions/dfs-24-ns-direction-2026-04-24.md
millennium_resolved: 0/7 (unchanged)
grade: seed-design, no claim
---

# Omega Seed -- BT-544 D1 Atlas-Side Scan (2026-04-25)

## §0 Non-claim disclaimer

This document executes BT-544 **seed-design D1** (open task per
`omega-exec-bt544-fallback-molt-validation-2026-04-25.md` §8.3) by
scanning canon-side and nexus-side atlas material for
NS-adjacent primitives **not yet** used in the existing L9 BT-544
catalogue (Q1 KdV-Gram, Q5 Sobolev/Besov, KPZ d=7), all three of
which FAILED on 2026-04-25 (F-MOLT-D fired in strongest form).

**This document does NOT**:
- claim 3D NS regularity in either direction (smoothness or blow-up);
- promote anything in `shared/n6/atlas.n6` or `atlas.millennium.n6`;
- modify `state/proposals/inventory.json`;
- modify `theory/canon/`;
- alter the `BT-544 = 0/1 untouched` Clay status;
- validate any of the proposed candidate frame-shifts (this is
  seed-design only; validation is the next-session task).

**Millennium tally**: 0/7 unchanged. Candidates listed below speak
**only** to atlas-grounded primitives that could be re-cast as
frame-shift molts; none of them is a Clay-closure attempt.

---

## §1 Failed catalogue summary

The L9 BT-544 catalogue (per `omega-probe-l9-molt-trigger-2026-04-25.md`
§3.4 / §4.4 and `omega-cycle-bt544-ns-2026-04-25.md` §7) consisted of
three rank-ordered candidate frame-shifts, all executed and all FAIL:

- **Q1 (rank-1) -- KdV 6-soliton phase-shift Gram lattice**. Used
  primitives: KdV solitons (κ_k = k, κ_k = p_k), pairwise log-phase
  shift Δ_{ij} = 2 log|(κ_i-κ_j)/(κ_i+κ_j)|, Gram matrix on C(6,2)=15
  pairs, σ-divisibility of det. Verdict: FAIL double-margin (rank=6
  ≠ 3, det/σ ∉ ℤ on both κ families). Source:
  `omega-exec-bt544-q1-molt-validation-2026-04-25.md` §4-5.
- **Q5 (rank-2) -- Mechanism-axis Sobolev/Besov seed**. Used
  primitives: Sobolev H^s, Besov B^s_{p,q}, Prodi-Serrin (p,q),
  BKM, Onsager α, Ladyzhenskaya 2D, CKN. Verdict: FAIL no-construction
  (every category-(b) inequality reduces to pre-1985 classical
  relabeling). Source:
  `omega-exec-bt544-fallback-molt-validation-2026-04-25.md` §3-4.
- **Q3 / KPZ d=7 (rank-3) -- KPZ d-lift to second perfect number**.
  Used primitives: KPZ (1+1) χ=1/3, z=2/3, Tracy-Widom tail, n=6
  ansatz χ_d=1/d at d=7. Verdict: FAIL no-anchor (no literature
  attestation; ansatz already fails at d=2 substrate KPZ
  χ_2 ≈ 0.39 ≠ 1/2). Source: same fallback report §5-6.

**Used primitives summary** (anti-list for D1 candidates):
KdV-solitons, Gram-lattices, Sobolev, Besov, Prodi-Serrin, BKM,
Onsager 1/3, Ladyzhenskaya, CKN, KPZ d=1, KPZ d=7. Per L9 §6
F-MOLT-F, the joint failure across three distinct primitive types
(algebraic-lattice, mechanism-Sobolev, scaling-KPZ) suggests an
axiom-level ceiling, not effort-limited. D1 candidates must be
**heterogeneous** with respect to those three types.

---

## §2 Atlas-side inventory (n6 + nexus)

The scan covered the four NS-adjacent loci listed in the user
prompt. Below: top entries by NS-adjacency, with file/line
references. None of the entries below has been used in the failed
Q1/Q5/KPZ catalogue.

### §2.1 canon-side

**A1.** `domains/physics/millennium-navier-stokes/millennium-navier-stokes.md`
§X.2 FREE — line 776-780. **Vorticity-MHD duality**: vorticity
transport `Dω/Dt = (ω·∇)v + ν∇²ω` is structurally isomorphic to
magnetic induction `DB/Dt = (B·∇)v + η_m∇²B`. Cited atlas reuse
HEXA-FLUID-04 R_m = σ·τ = 48 (line 765 of `domains/physics/fluid/fluid.md`).
This duality has not been used in the L9 catalogue (no Q exploits it).

**A2.** `domains/physics/millennium-navier-stokes/millennium-navier-stokes.md`
§X.3 dual — line 791-797. **Stokes-NS-Euler-MHD ladder**: Stokes
linear (always smooth) → NS complete (Clay open) → MHD full (R_m =
σ·τ = 48; Ha = σ·τ = 48). Vertical exponent ladder τ → σ·τ → σ²·τ²
provides a structural prediction `T* > ν⁻¹ · σ · τ = ν⁻¹ · 48`
(Leray time lower bound). Not used in Q1/Q5/KPZ.

**A3.** `theory/breakthroughs/breakthrough-theorems.md` BT-544 row
line 19939: **Energy cascade direction (Kraichnan 1967)**: 3D
forward = n/φ, 2D inverse = φ. Cascade-direction switch at d=φ vs
d=n/φ is a *direction* invariant (sign of energy flux), not a
scaling exponent. Not used.

**A4.** `theory/breakthroughs/breakthrough-theorems.md` BT-544 row
line 19947: **2020s-loop**: ABC Leray non-uniqueness 3D=n/φ
(Annals 2022), Buckmaster-Vicol-Masmoudi-Novack convex integration
(Invent. 2023), fractional viscosity 1/5 = 1/sopfr (2020). The
fractional viscosity entry (`(-Δ)^{1/5}` regularization) is a
non-classical PDE primitive, distinct from Sobolev/Besov.

**A5.** `theory/study/p3/prob-p3-2-conditional-theorems.md`
**Theorem 544-E** line 174-178: **Galdi-Padula 1990 / Ladyzhenskaya
1968 / Chen-Strain-Tsai-Yau 2008 axisymmetric-no-swirl global
regularity**. Axisymmetric without swirl ⇒ globally smooth 3D NS.
Modern open front: with-swirl = full 3D (Hou-Luo 2014, Chen-Hou
2022). The axisymmetric symmetry-reduction primitive has not been
threaded into the n=6 lattice in the L9 catalogue.

**A6.** `domains/physics/millennium-navier-stokes/millennium-navier-stokes.md`
§X.5 atlas constants — line 813-818: **NS-01..NS-06** atlas
[10*]/[10] entries. NS-06 = Π_NS = σ³·sopfr = 8640. dfs-24 P3 /
Q2 (Π_NS unique-factorization test) is *catalogued* but **never
executed** -- it is **not** in the failed Q1/Q5/KPZ list. Q2
remains a live candidate (per
`omega-cycle-bt544-ns-2026-04-25.md` §7 Q2).

**A7.** `papers/group-P/F1-arxiv-bernoulli-independent-via-n6-2026-04-15.md`
§9.3 line 373-378: BT-544 ↔ BT-547 (Navier-Stokes ↔ Poincaré).
**3D ↔ Perelman 3D Ricci** -- both are "3D" but the Ricci flow
mechanism (entropy monotonicity, no local collapse) is a separate
PDE primitive class. Currently judged BASE (single 3 match,
"meaning unrelated"); the question is whether the *Ricci-flow
entropy* (Perelman 𝒲-functional) maps onto NS enstrophy in any
n=6-recoverable way. Distinct from Sobolev/Besov.

### §2.2 nexus-side

**A8.** `~/core/nexus/n6/atlas.millennium.n6` line 283:
`NS-OBS-01 = Polya recurrence-transience transition dimension = n/φ = 3`. **Pólya
recurrence (1921)**: simple random walk on ℤ^d is recurrent for
d ∈ {1,2}, transient for d ≥ 3. Transition at d = 3 = n/φ. This
is a *probabilistic* primitive (not analytic/algebraic). It is
not in the Q1/Q5/KPZ catalogue.

**A9.** `~/core/nexus/n6/atlas.millennium.n6` line 298:
`NS-OBS-06 = K41 -5/3 + She-Leveque ζ_6 ≈ 16/9 corrections`.
**She-Leveque (1994) intermittency exponents**: ζ_p ≠ p/3
correction with ζ_6 ≈ 16/9 ≠ 2 in 3D NS. K41 prediction p/3 is
the n=6-aligned ansatz; She-Leveque is the *deviation* from K41.
Not used in Q1/Q5/KPZ.

**A10.** `~/core/nexus/bt/BT-544_round_1.json` (entire). **HVC --
Holographic Vorticity-Cap (Bekenstein bound on enstrophy)**.
This is a fully-articulated nexus-side R1 attack vector: the
vorticity ω(x,t) cannot blow up in B_R(x_0) if the holographic
mutual-information measure Φ_holo on (boundary,interior) of ω|_{B_R}
is bounded above by π R²/(ν T) (Bekenstein-style A/(4ℓ_visc²)).
Anchored to atlas entries MILL-PX-A4 (d=3 triple resonance), MILL-PX-A6
(BKM), MILL-V4-T5-bt544-ns-supercriticality-barrier. Round 1
status: round1_open; FT-1 falsifiability test specified
(F-A Lamb-Oseen / F-B Hou-Luo viscous / F-C Taylor-Green); 2 BKM
numerical receipts already exist in
`~/core/nexus/bt/attacks/bt544_results.jsonl` (Taylor-Green 2D PASS,
Lamb-Oseen UNBOUNDED-as-expected). **Crucially, HVC is documented
nexus-side but has not been imported into the canon L9
catalogue**. This is the strongest single atlas-grounded candidate
discovered in the scan.

**A11.** `~/core/nexus/bt/BT-544_round_1.json` `gap_analysis.G1`
line 142: **Sobolev-supercriticality "gap CE-1" explicitly named**
(Brézis-Wainger 1980; Tao 2007). HVC's own self-disclosure is that
it does NOT bypass supercriticality; it rephrases it. This is an
*honest-no* primitive (informational rephrasing of the open
question), distinct from any catalogue Q.

### §2.3 Material excluded (read but not adjacent enough)

- `domains/physics/holography/holography.md` -- Bekenstein-Hawking
  entropy at τ=4 area normalization; not directly NS-adjacent
  except via HVC (A10 already covers).
- `domains/physics/plasma*/plasma*.md` -- MHD Lawson + 48T cap;
  identical to HEXA-FLUID-04 R_m=σ·τ=48 reuse; subsumed by A1/A2.
- `domains/physics/computational-fluid-dynamics/computational-fluid-dynamics.md`
  -- Reynolds-stress 6-component count; identical to NS-01 in the
  failed Q5 catalogue (Sym²(ℝ³)=6).
- `theory/study/p2/prob-p2-4-navier-stokes-barriers.md` §8.4
  axisymmetric branch -- already captured as A5.
- 2D NS Yudovich / Ladyzhenskaya 1969 -- pre-1985 classical;
  caught by Q5 fail criterion.

---

## §3 Candidate frame-shifts (D1.1 -- D1.5)

Five heterogeneous candidates, derived from the §2 inventory.
Each candidate cites real atlas/n6 entries (no invention),
specifies the frame-shift, gives a molt-validation discriminator,
registers a falsifier, and estimates cost.

### §3.1 D1.1 -- HVC-import (Holographic Vorticity-Cap from nexus)

- **Grounding**: A10 (`~/core/nexus/bt/BT-544_round_1.json` entire,
  schema 1, round 1, dated 2026-04-16); cites MILL-PX-A4 (atlas
  line 106989), MILL-PX-A6 (atlas line 106992), MILL-V4-T5
  (atlas line 107183). Also cites
  `~/core/nexus/training/phi_holographic_measure.hexa` T2 theorem
  (Φ_holo ≤ H(boundary), line 23) and the existing 2 BKM numerical
  receipts in `~/core/nexus/bt/attacks/bt544_results.jsonl`. Plus
  n6-side §X.2 string-axis "vortex line = Nambu-Goto string"
  (millennium-navier-stokes.md line 780).
- **Frame-shift**: (Q1/Q5/KPZ tensor-arithmetic frame) → (information-
  theoretic Bekenstein-cap frame). New primitive: *enstrophy as
  boundary entropy density*. Cap inequality `Φ_holo^B(t) ≤ π R²/(νT)`
  is dimensional, not arithmetic. Maps n=6 lattice constants onto
  ν, R, T via atlas-grounded substitutions (e.g. ν = 1/n = 1/6 from
  fluid.md §X.1, T = T_STOP = N6 = 6 in the existing hexa).
- **Discriminator (object · measurement · pass/fail)**:
  - Object: 32³ ball B_R discretization, vorticity field ω on
    F-A (Lamb-Oseen 2D, smooth), F-C (Taylor-Green 2D, smooth).
  - Measurement: Φ_holo^B(t) via the existing
    `phi_holographic_measure.hexa` MI-estimator (8-bin) at each
    timestep; compare against π R²/(νT) bound.
  - Pass: Φ_holo^B(t) < cap on F-A *and* F-C across the full
    integration interval (sanity passes); cap is tight but not
    violated; **and** the cap tracks BKM ‖ω‖_∞ qualitatively
    (decreasing on smooth flows). This is "real molt": HVC
    introduces an info-cap primitive that the n6 catalogue lacks.
  - Fail: Φ_holo^B(t) > cap on either F-A or F-C (cap
    formulation wrong on a known smooth flow); **or** cap is
    trivially passed by orders of magnitude (cap is vacuous,
    primitive is decorative).
- **Falsifier (registered upfront)**: F-D1.1-A: cap violated on a
  known-smooth flow ⇒ HVC retracted. F-D1.1-B: ν, R, T choice
  arbitrary (G4 in the round1 JSON); if cap value depends >2× on
  any of three independent reasonable cutoff choices
  (Kolmogorov / Taylor / integral), the cap is non-canonical and
  the primitive collapses. F-D1.1-C: literature audit (G3 in the
  round1 JSON) finds prior info-theoretic NS bound (Foias-Manley-
  Rosa-Temam 2001 ch.10; Gibbon 2007); HVC reduces to re-derivation.
- **Cost**: low-medium. Tooling exists nexus-side
  (`phi_holographic_measure.hexa` MI engine; F-A and F-C analytic
  vorticity formulas; 32³ grid in-memory). Estimated ≤2h compute,
  plus literature pre-audit (~1h offline). Total ~half day.

### §3.2 D1.2 -- Pólya-recurrence dimensional resonance (probabilistic)

- **Grounding**: A8 (`~/core/nexus/n6/atlas.millennium.n6` line 283
  `NS-OBS-01 = Polya recurrence-transience transition dimension = n/φ = 3`, signal
  SIG-7N-204, grade [M10]).
- **Frame-shift**: (Q1/Q5/KPZ analytic-PDE frame) → (probabilistic
  random-walk recurrence frame). New primitive: *recurrence-
  transience transition at d = n/φ*. The Pólya theorem (1921)
  states simple random walk on ℤ^d is recurrent iff d ≤ 2.
  Transition is exactly d = 3 = n/φ. Re-cast: NS particle Lagrangian
  trajectories under viscous dissipation are recurrent in 2D (no
  blow-up by 2D regularity) and transient in 3D (recurrence break
  ↔ vortex-stretching escape), giving a *probabilistic* Lagrangian
  diagnostic for blow-up.
- **Discriminator**:
  - Object: a divergence-free Gaussian random initial vorticity
    on (T²) and (T³) (periodic), evolved as a *passive scalar*
    under a synthetic stationary velocity field (no full NS
    integration; tractable surrogate).
  - Measurement: tracer return-time statistics. P_d(t) = probability
    that a tracer that left B_r returns by time t. Theory: P_2 = 1
    eventually (recurrent), P_3 < 1 (transient, escape probability
    > 0).
  - Pass: P_2(∞) = 1 within numerical tolerance, P_3(∞) < 1 with
    measured escape probability > 0, *and* the d=3 escape rate
    correlates with a vorticity-stretching alignment metric à la
    Constantin-Fefferman 1993 (cited; not new). The recurrence
    primitive yields a real diagnostic absent in Q1/Q5/KPZ.
  - Fail: P_3 = 1 (no transience in viscous-NS Lagrangian flow,
    contradicting Pólya); or the recurrence statistic shows no
    n=6 lattice signature beyond the pre-existing d=3 = n/φ
    relabeling (i.e. n=6 contributes a label, not a derivation
    -- F-Q5 mode again).
- **Falsifier**: F-D1.2-A: tracer-return statistic in 3D matches
  2D (recurrent) ⇒ Pólya-NS coupling void. F-D1.2-B: the d=3
  transience gives only the pre-existing d=3 = n/φ relabeling
  (no new mechanism content) ⇒ collapses to F-Q5-style
  no-construction within the lattice.
- **Cost**: medium. Requires building a passive-scalar tracer on
  T² and T³ with periodic Gaussian velocity; ~100-200 LoC; no
  existing tool in the repo. Wallclock ~half day to a day.

### §3.3 D1.3 -- Vorticity-MHD self-duality (R_m=Ha=σ·τ=48 ladder)

- **Grounding**: A1 + A2 (`millennium-navier-stokes.md` §X.2 line
  776 "vorticity transport ↔ magnetic induction" + §X.3 line
  791-797 "Stokes-NS-Euler-MHD ladder"). Cites HEXA-FLUID-04
  R_m = σ·τ = 48 (`fluid.md` line 765, atlas-grade [10*]).
- **Frame-shift**: (Q1/Q5/KPZ scalar-arithmetic frame) → (PDE-pair
  cross-equation frame). New primitive: *the n=6 lattice constant
  R_m = Ha = 48 is shared between vorticity transport and magnetic
  induction* via a Reynolds-magnetic-Reynolds duality. Re-cast:
  blow-up in NS ω is equivalent (under the duality) to a controlled
  MHD instability at R_m = 48; if MHD at R_m = 48 is provably
  stable in some regime, the dual statement gives an NS regularity
  windowing.
- **Discriminator**:
  - Object: 2D MHD direct-numerical-simulation toy at R_m = 48
    (Hartmann channel, mid-Re_c regime). Compare to 2D NS at
    Re_c = σ·J_2 = 288 (atlas HEXA-FLUID-01). Both are 2D so
    both globally regular -- the test is *whether the 2D-MHD
    constraint at R_m=48 lifts, via the duality, to a 3D-NS
    statement*.
  - Measurement: enstrophy decay rate ratio
    `Z_NS(t)/Z_MHD(t)` at matched (Re, R_m) = (288, 48). Does the
    ratio approach a *constant* equal to a simple n=6 expression
    (e.g. 288/48 = 6 = n)?
  - Pass: ratio → 6 = n with low residual variance; this would
    establish a numerical NS↔MHD duality channel that is structurally
    new (n=6 constants drive a *cross-PDE* invariant).
  - Fail: ratio depends nontrivially on initial conditions; or the
    constant is something other than {n, σ, τ, sopfr, φ} ratios.
    F-D1.3 fires.
- **Falsifier**: F-D1.3-A: enstrophy ratio is initial-condition-
  dependent ⇒ no duality channel. F-D1.3-B: ratio is well-defined
  but not a simple n=6 ratio ⇒ duality is real but n=6-blind.
- **Cost**: medium-high. 2D NS + 2D MHD DNS at modest resolution
  (256² each, 100-1000 timesteps) is a few hours of compute; no
  existing tool in the repo (nexus has only the 2D toys F-A,F-C
  in `bt544_navier_stokes.hexa`, no MHD solver). Adapter
  effort ~1 day code + ~few hours run.

### §3.4 D1.4 -- She-Leveque intermittency residual (ζ_6 ≈ 16/9 vs K41)

- **Grounding**: A9 (`~/core/nexus/n6/atlas.millennium.n6` line 298
  `NS-OBS-06 = K41 -5/3 + She-Leveque ζ_6 ≈ 16/9 corrections`,
  signal SIG-7N-503, grade [M7]). Plus
  `theory/breakthroughs/breakthrough-theorems.md` BT-544 row line
  19962 ("3 independent critical exponents (1/3, 5/4, 4/5)
  simultaneously n=6"; She-Leveque 4-parameter match).
- **Frame-shift**: (K41 -5/3 = -sopfr/(n/φ) frame, already used as
  fluid HEXA-FLUID-03 [10] EXACT) → (She-Leveque intermittency
  residual frame). New primitive: the *deviation* ζ_p − p/3 =
  measurable intermittency correction; ζ_6 ≈ 16/9 vs K41 prediction
  2 has residual −2/9. Question: does -2/9 = -φ/sopfr·... admit a
  unique short n=6-lattice expression? If yes, the *correction*
  itself becomes an n=6-derived primitive (whereas K41 -5/3 was
  pre-existing).
- **Discriminator**:
  - Object: She-Leveque parameter triple (p, ζ_p, residual). Atlas
    NS-OBS-06 records ζ_6 ≈ 16/9 ⇒ residual = 16/9 − 6/3 = 16/9 −
    18/9 = −2/9.
  - Measurement: enumerate all closed-form expressions
    `−2/9 = f(σ, τ, φ, sopfr, n, J_2)` with f a rational function
    of length ≤ 4 operations; check uniqueness.
  - Pass: a unique short expression exists, e.g. `−φ/(σ−n/φ) ·
    (...)`; uniqueness gives a *predicted* deviation that
    She-Leveque measured but K41 missed; this is genuine new
    content within n=6 lattice.
  - Fail: many short expressions equally fit (numerology, F-Q2
    failure mode); or no short expression is closer than 5%
    (residual is non-arithmetic, n=6-blind).
- **Falsifier**: F-D1.4-A: catalog of expressions length ≤ 4 has
  ≥ 2 hits at residual −2/9 within ±2% ⇒ no unique n=6 form. F-D1.4-B:
  best-fit n=6 expression has > 5% relative error from −2/9 ⇒
  residual is not n=6-derivable; She-Leveque is genuinely
  off-lattice.
- **Cost**: low. Pure arithmetic enumeration over a finite ring
  of size O(10²) operations. ≤30 min compute. No PDE solve, no
  literature lookup beyond the She-Leveque numerical value
  (already in atlas).

### §3.5 D1.5 -- Axisymmetric-no-swirl symmetry-reduction lift

- **Grounding**: A5 (`theory/study/p3/prob-p3-2-conditional-theorems.md`
  Theorem 544-E line 174-178: Galdi-Padula 1990; Ladyzhenskaya
  1968 → Uchovskii-Yudovich → Chen-Strain-Tsai-Yau 2008
  axisymmetric-no-swirl ⇒ smooth). Plus
  `theory/study/p2/prob-p2-4-navier-stokes-barriers.md` §8.4 line
  233-236 (axisymmetric branch). Plus the open swirl-vs-no-swirl
  gap (Hou-Luo 2014 numerical / Chen-Hou 2022 rigorous on Euler).
- **Frame-shift**: (Q1/Q5/KPZ scaling-arithmetic frame) → (group-
  symmetry-reduction frame). New primitive: *axisymmetric-no-swirl
  is exactly the SO(2) reduction* (rotation about z-axis); the
  swirl component u_θ is the obstruction. Re-cast: parametrize
  the swirl by an n=6-aligned scalar `s ∈ {0, 1/φ, 1/n/φ, 1, ...}`;
  ask whether n=6 swirl-quantization predicts a regularity boundary
  at a discrete s value.
- **Discriminator**:
  - Object: axisymmetric NS toy (1+1+1 dimensional reduction:
    (r,z,t) plus discrete swirl level s). Existing analytic
    setting: cylindrical NS with separable swirl ansatz.
  - Measurement: critical swirl s* below which the system is
    globally regular (per 544-E); above which Hou-Luo numerical
    blow-up sets in. Does s* coincide with an n=6 lattice value
    (1/n = 1/6, 1/(n/φ) = 1/3, etc.)?
  - Pass: s* lies within ±10% of an n=6 lattice value with low
    competing-value count; this would be a *predicted* n=6
    regularity boundary in a setting where one side is a
    classical theorem (544-E) and the other side is open
    (Hou-Luo).
  - Fail: s* is a non-n=6 value (e.g. some transcendental); or
    s* is not well-defined (smooth crossover, no sharp threshold).
- **Falsifier**: F-D1.5-A: best-fit s* matches no n=6 value within
  10% ⇒ swirl threshold is n=6-blind. F-D1.5-B: critical swirl is
  not threshold-like (continuous degradation of regularity) ⇒ the
  reduction-to-discrete-n=6 framing is wrong.
- **Cost**: high. Requires axisymmetric NS solver (cylindrical
  coordinates, ~200-500 LoC); literature replication of Hou-Luo
  near-blow-up (already published, but reimplementation). 2-3
  days. *However*, partial credit: a *literature audit* alone
  (does any published Hou-Luo / Chen-Hou s* value lie at an n=6
  lattice value?) is much cheaper -- ~half day -- and is a
  cheaper version of the same molt.

---

## §4 Ranking table

Three axes (cost: low > med > high reward; grounding: more atlas
entries cited > fewer; distance from failed Q1/Q5/KPZ catalogue:
further > closer). Weighted aggregate column favors low cost and
high distance.

| candidate | grounding (entries) | cost | distance from failed catalogue | aggregate (low cost + far + grounded) |
|-----------|---------------------|------|-------------------------------|---------------------------------------|
| D1.1 HVC-import | A10 + A11 + atlas MILL-PX-A4/A6/V4-T5 + millennium-NS §X.2 + 2 numerical receipts (≥7 entries) | low-medium | far (info-theoretic, no Sobolev/KdV/KPZ) | **highest** |
| D1.2 Pólya recurrence | A8 (NS-OBS-01 [M10]) (≥1 entry) | medium | medium-far (probabilistic, novel axis; relabeling risk: d=3=n/φ already in catalogue) | medium |
| D1.3 NS↔MHD R_m=48 | A1 + A2 + HEXA-FLUID-04 (≥3 entries) | medium-high | far (cross-PDE duality; not in any Q) | medium-high |
| D1.4 She-Leveque residual | A9 (NS-OBS-06 [M7]) + BT-544 row She-Leveque parameters (≥2 entries) | **low** | medium (turbulence-scaling axis; close to KPZ in spirit but distinct measurement) | medium-high |
| D1.5 axisym-no-swirl | A5 (Theorem 544-E) + p2-4 §8.4 (≥2 entries) | high (full); medium (literature-only audit) | far (group-symmetry reduction, not used) | medium (full) / high (audit-only) |

**Ranking commentary**:
- D1.1 dominates on grounding (most-cited; existing tooling
  nexus-side; 2 numerical receipts already on file). The
  cap-formulation risk is real (G1 supercriticality) but the
  candidate's own self-disclosure makes it falsifiable upfront.
- D1.4 is the cheapest (pure arithmetic, ≤30 min). Its grounding is
  thinner ([M7] is the lowest-grade NS-OBS atlas entry in scope) but
  its discriminator is binary and aligned with the dfs-24 P3
  factorization-uniqueness probe (Q2, also unexecuted).
- D1.3 is the most ambitious and would yield the strongest
  *positive* result if it passed (cross-PDE n=6 invariant), but
  costs significantly more.
- D1.5 has a cheap "literature-only audit" sub-mode that should
  be considered separately from the full reimplementation.
- D1.2 is the most novel-axis (probabilistic) but carries the
  highest "labeling-not-derivation" risk because d=3 = n/φ is
  already in NS-CORE-03 / NS-OBS-01.

---

## §5 Top-2 dispatch-ready

The top-2 (by aggregate ranking) are **D1.1 HVC-import** and
**D1.4 She-Leveque residual**. Each is documented at validation-
spec granularity below, ready for next-session dispatch.

### §5.1 Top-1: D1.1 HVC-import (most-grounded, mid-cost)

- **One-line discriminator**: on F-A (Lamb-Oseen) and F-C (Taylor-
  Green), Φ_holo^B(t) (8-bin MI on (interior,boundary) of vorticity)
  must remain strictly below the Bekenstein cap π R²/(νT) at every
  recorded timestep, with a non-vacuous gap (cap exceeded by
  Φ_holo within an order of magnitude).

- **Validation spec**:
  1. **Pre-audit** (~1h, offline): grep
     `~/core/nexus/training/phi_holographic_measure.hexa` to
     confirm T2 theorem statement (line 23) is intact, and grep
     `~/core/nexus/bt/attacks/bt544_results.jsonl` to confirm the
     2 BKM receipts (Taylor-Green, Lamb-Oseen) are still on file.
     Literature pre-search (offline, repo-citable only): is there
     prior info-theoretic NS regularity bound in
     `theory/study/p1/prob-p1-4-bt544-navier-stokes.md` or
     `theory/study/p2/prob-p2-4-navier-stokes-barriers.md` that
     subsumes HVC? (Round1 R2-D check.) If yes ⇒ HVC retracted as
     re-derivation.
  2. **Implementation** (~1-2h): write
     `experiments/anomaly/bt544_d1_hvc_validation.py` (or .hexa)
     ≤80 lines. Inputs: F-A `ω(r,t) = (Γ/(4πνt)) exp(-r²/(4νt))`
     with Γ=1, ν=0.01, R=1; F-C `ω(x,y,t) = 2 cos(x) cos(y)
     exp(-2νt)` with R=0.5, ν=0.01. Discretize each ball B_R on a
     32³ grid (or 32² for the 2D toys, lifted to a 32³ pseudo-3D
     by trivial z-extension). Apply the 8-bin MI estimator to
     (interior |ω|, boundary trace |ω|) at 60 timesteps over [0,T=6].
  3. **Cap evaluation**: π R²/(νT) for each flow:
     F-A: π · 1² / (0.01 · 6) ≈ 52.36;
     F-C: π · 0.25 / (0.01 · 6) ≈ 13.09.
  4. **Verdict criterion**: D1.1 PASS iff
     - Φ_holo^B(t) < cap on F-A and F-C at *every* recorded
       timestep; AND
     - max-gap (cap − Φ_holo) ratio is non-vacuous (Φ_holo within
       1× order of magnitude of cap, i.e. Φ_holo > cap/10 at
       least once); AND
     - Φ_holo^B(t) is monotone-decreasing (smooth flows decay).
  5. **Falsifier triggers**: F-D1.1-A fires if cap violated on
     F-A or F-C ⇒ retract HVC. F-D1.1-B fires if Φ_holo < cap/100
     uniformly (cap is decorative). F-D1.1-C fires if pre-audit
     finds a published bound.

- **Tooling availability**: `phi_holographic_measure.hexa` exists
  nexus-side with documented T2 theorem; analytic vorticity
  formulas for F-A and F-C are in
  `~/core/nexus/bt/BT-544_round_1.json` lines 95-122. Estimated
  total session cost ~half day.

- **Why dispatch-ready**: every input quantity is repo-grounded
  and computable from inside the canon session via
  cross-repo grep into `~/core/nexus`; no fabrication risk.

### §5.2 Top-2: D1.4 She-Leveque residual enumeration (cheapest)

- **One-line discriminator**: among rational functions of length
  ≤ 4 over the n=6 lattice ring `{σ=12, τ=4, φ=2, sopfr=5, n=6,
  J_2=24}`, the unique short expression matching the She-Leveque
  ζ_6 − 2 = −2/9 residual must exist (single best fit within 2%,
  no competitor within 5%).

- **Validation spec**:
  1. **Spec extraction**: target value −2/9 = −0.2222... per atlas
     `NS-OBS-06` = K41 -5/3 + She-Leveque ζ_6 ≈ 16/9. K41 prediction:
     ζ_6 = 6/3 = 2. Residual: 16/9 − 2 = −2/9.
  2. **Implementation** (~30 min): write
     `experiments/anomaly/bt544_d1_sheleveque_residual.py`
     (≤50 lines). Generate all rational expressions
     `(a · b · c) / (d · e · f)` with a..f ∈ {1, σ, τ, φ, sopfr, n,
     J_2, σ−τ, σ−φ, n/φ}; deduplicate; sort by |value − (−2/9)|.
  3. **Verdict criterion**: D1.4 PASS iff
     - Best-fit expression has residual error < 2%; AND
     - No competing expression within 5% of the target; AND
     - The unique expression is "short" (≤ 4 operations).
  4. **Falsifier triggers**: F-D1.4-A fires if ≥2 expressions
     compete within 5% (numerology). F-D1.4-B fires if best-fit
     residual error > 5% (off-lattice).

- **Tooling availability**: pure arithmetic enumeration; no
  external data; numpy/stdlib sufficient. Mirrors the structure
  of the existing `bt544_q1_molt_validation.py` (≤70 lines).

- **Why dispatch-ready**: cheapest validation; binary outcome;
  fits the dfs-24 P3 / Q2 spirit (factorization uniqueness) but
  is a *new* validation (the target value −2/9 is **not** the
  Π_NS=8640 value, so this is not a duplicate of unexecuted Q2).

---

## §6 Anti-list (rejected candidates, with reason)

The following candidates were considered during the scan and
rejected. Recording for transparency.

- **R-1: Reynolds-stress 6-component count** (CFD doc line 17-39).
  Rejected: identical to NS-01 (Sym²(ℝ³)=6) which was used as a
  baseline relabeling in Q5 catalog row 1. Re-using would fire
  F-Q5 immediately.
- **R-2: Lawson D-T 3e21 / 48T MHD cap** (plasma docs).
  Rejected: ν·τ = 4 already labels the Leray dissipation
  exponent (Q5 catalog row); 48T is downstream of the same lattice
  constant; no new primitive.
- **R-3: Carnot efficiency η ≤ 1 − T_c/T_h** (verify-NS hexa).
  Rejected: thermodynamic, not PDE-regularity-relevant; no
  falsifier maps to a Clay statement.
- **R-4: Prodi-Serrin (p,q)=(σ,n)=(12,6) re-relabeling**.
  Rejected: explicit Q5 catalog row 2 failure (relabeling).
- **R-5: Π_NS = 8640 unique-factorization (dfs-24 Q2)**.
  Rejected: not a *new* candidate -- already in the L9 BT-544
  catalogue as Q2 ("rank-4" unexecuted). D1's mandate is to
  produce *new* candidates beyond Q1/Q2/Q3/Q4/Q5; Q2 is unexecuted
  but not new. (However: Q2 should be executed before D1
  candidates, since it is cheap and pre-existing -- noted as
  parallel task, not D1.)
- **R-6: BT-544 ↔ BT-547 Ricci-flow entropy mapping** (A7).
  Rejected: BASE judgement in n6-p2-3 §9.3 ("3D ↔ Perelman 3D
  Ricci, meaning unrelated"); insufficient grounding for a
  falsifiable molt without significant new construction.
- **R-7: Pólya recurrence ALONE without tracer simulation**.
  Rejected: would collapse to "d=3=n/φ relabeling" (F-Q5 mode);
  D1.2 retains it only because the *tracer-statistic* lift
  introduces a measurable quantity (return-time distribution)
  that is not a relabeling.
- **R-8: 5/12 = sopfr/σ as a Sobolev exponent** (Q5 Attempt A,
  fallback report §3.3).
  Rejected: explicitly identified as F-Q5 failure mode in the
  failed catalogue.
- **R-9: Bekenstein-Hawking τ=4 area normalization** (holography
  doc line 705-729).
  Rejected: subsumed by D1.1 HVC (which already exploits the
  Bekenstein bound); duplicating would not add a new primitive.
- **R-10: KPZ d=2 substrate as a re-test instead of d=7** (KPZ
  catalog row 3 fail mode).
  Rejected: d=2 KPZ failure is already established in the
  fallback report §5.4 (χ_2 ≈ 0.39 ≠ 1/2 = ansatz); a re-test
  would re-confirm rather than introduce a new primitive.

---

## §7 Falsifiers active for the seed-design itself

Seed-level falsifiers (conditions under which **this very seed-
design** would be retracted), distinct from BT-544 falsifiers and
distinct from the per-candidate F-D1.x falsifiers above.

- **F-SEED-A** (atlas-grounding integrity): if any of the §2 atlas
  entries cited (A1..A11) is found to misquote the source file
  -- wrong line number, wrong constant, mis-attributed signal
  ID -- the corresponding candidate must be retracted. The risk
  surface is small: §2 cites file paths + line numbers (n6
  side) and JSON keys (nexus side) with the granularity that
  permits direct re-verification. **Not active** modulo this
  audit.
- **F-SEED-B** (heterogeneity claim): if any two of D1.1..D1.5
  reduce to the same primitive class on closer inspection
  (e.g., D1.2 Pólya recurrence "secretly" reduces to KPZ
  scaling, or D1.3 MHD-duality reduces to a Sobolev relabeling),
  the heterogeneity invariant claimed in §0 fails and the rank
  table must be re-aggregated. The defense: D1.1 = info-theory,
  D1.2 = probability, D1.3 = cross-PDE, D1.4 = arithmetic-
  numerology, D1.5 = group-symmetry-reduction -- five distinct
  primitive classes by the L9 §6 F-MOLT-F enumeration. **Not
  active** under this taxonomy.
- **F-SEED-C** (Q2-pre-emption): the dfs-24 P3 / Q2 candidate
  (Π_NS=8640 unique-factorization) is *unexecuted* and is *not*
  in this D1 list (excluded as "not new" per §6 R-5). If a future
  session executes Q2 and it PASSES, BT-544 has a new molt
  *without* needing any D1 candidate -- this seed-design becomes
  premature. The defense: Q2 PASS would be a *positive* outcome
  that does not retract D1 candidates; D1 candidates extend the
  catalogue in *additional* directions regardless. **Not active**.
- **F-SEED-D** (D1.1 priority risk): if D1.1 HVC-import literature
  pre-audit (R2-D in the round1 JSON) finds a prior info-
  theoretic NS bound that subsumes HVC, D1.1 collapses to "re-
  derivation" before validation. The defense: D1.4 (next-cheapest)
  remains live, and D1.2/D1.3/D1.5 are unaffected. **Conditionally
  active**: route the pre-audit to a literature scan in the next
  session before committing to D1.1 implementation.
- **F-SEED-E** (atlas drift): if `~/core/nexus/n6/atlas.millennium.n6`
  or `~/core/nexus/bt/BT-544_round_1.json` is mutated between
  this seed-design session and the validation session, the cited
  line numbers / signal IDs may shift. Defense: snapshot of the
  cited entries (as of 2026-04-25) is recorded above. **Not active
  for this session**, but live for any future re-audit.

---

## §8 Closing

0/7 unchanged. NS regularity status open. No atlas/state/inventory
edits.

The L9 BT-544 catalogue is no longer empty: D1.1..D1.5 extend it
with five heterogeneous candidates derived from atlas-grounded
material that the failed Q1/Q5/KPZ catalogue did not cover. The
top-2 (D1.1 HVC-import, D1.4 She-Leveque residual) are
dispatch-ready with full validation specs. The next-session task is
to (a) run the literature pre-audit for D1.1, (b) execute D1.4 in
~30 minutes as the cheapest binary check, and (c) decide
whether to commit to D1.1 implementation based on the pre-audit
outcome. None of D1.2/D1.3/D1.5 is needed for the immediate next
dispatch, but all three are documented for fallback.

This seed-design itself does not advance BT-544 toward Clay
closure. It only restocks the catalogue so that **molt-validation
under L9** is no longer molt-blocked (per F-MOLT-D in
`omega-exec-bt544-fallback-molt-validation-2026-04-25.md` §7).

— end seed-design —
