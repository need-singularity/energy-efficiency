# atlas.n6 [7] -> [10*] manual promotion checklist (40 candidates)

- Reference date: 2026-04-14
- Source: `scripts/atlas_promote_7_to_10star.hexa` dry-run (DSE-P2-2)
- Input statistics: 40 candidates / average fitness 851 / range 789~873 / all below the 900 cutoff -> 0 automatic promotions (safety-by-design)
- Target SSOT: `/Users/ghost/Dev/nexus/shared/n6/atlas.n6` (106,496 lines)
- Derived report: `experiments/dse/atlas_promotion_candidates_p2.md`
- Principles (CLAUDE.md + R0~R27 + N61~N65):
  - Only direct edits on atlas.n6 are allowed (no new files)
  - No automatic replacement before manual approval
  - Every promotion must pass all 5 items of the honest-verification specification

## 0. Promotion-procedure overview

Each candidate must pass the following 5-step verification before a manual `[7]` -> `[10*]` edit is performed.

1. Verify measured-value source — is it from paper / experiment / simulation? Record link, DOI, experiments ID.
2. Record error range — record the +/- value, unit, confidence interval, sigma level.
3. Attempt at least 1 counterexample — try to violate sigma*phi = n*tau in an n!=6 case (test the BT converse).
4. Confirm the sigma*phi = n*tau derivation path — explicitly spell out the formula deriving the measured value from the n=6 constants (sigma=12, tau=4, phi=2, sopfr=5, omega=2).
5. Manual approval signature — final approval by user Park Min-woo (signature checkbox).

Only after all 5 items are complete may the bt's atlas.n6 line be modified directly. Editing in a partially-complete state violates R5/N62.

## 1. Combined table of the 40 candidates

| # | id | Current grade | Line | Tier | Description (atlas source) | fitness* |
|---|----|--------|------|------|------------------|----------|
| 1 | n6-bt-7 | [7] | 14306 | Tier-1 | Egyptian Fraction Power Theorem | 822 |
| 2 | n6-bt-10 | [7] | 14312 | Tier-1 | Landauer-WHH Information-Thermodynamic Bridge | 839 |
| 3 | n6-bt-81 | [7] | 14454 | Tier-2 | Anode Capacity Ladder sigma-phi = 10x | 839 |
| 4 | n6-bt-82 | [7] | 14456 | Tier-2 | Complete Battery Pack n=6 Parameter Map | 839 |
| 5 | n6-bt-83 | [7] | 14458 | Tier-2 | Li-S Polysulfide n=6 Decomposition Ladder | 839 |
| 6 | n6-bt-91 | [7] | 14474 | Tier-2 | Z2 Topological ECC — J2 GB Savings Theorem | 839 |
| 7 | n6-bt-92 | [7] | 14476 | Tier-1 | Bott Periodicity Active Channels = sopfr | 839 |
| 8 | n6-bt-93 | [7] | 14478 | Tier-1 | Carbon Z=6 Chip Material Universality | 839 |
| 9 | n6-bt-112 | [7] | 14516 | Tier-1 | phi^2/n = 2/3 Byzantine-Koide Resonance | 861 |
| 10 | n6-bt-171 | [7] | 14633 | Tier-1 | SM Coupling Constant n=6 Fraction Pair | 861 |
| 11 | n6-bt-209 | [7] | 14709 | Tier-1 | Proton-Electron Mass Ratio n*pi^5 Fundamental Bridge | 861 |
| 12 | n6-bt-355 | [7] | 15011 | Tier-5 | Synthetic biology n=6 double perfect number | 789 |
| 13 | n6-bt-378 | [7] | 15047 | Tier-5 | Warp-metric ladder n=6 | 789 |
| 14 | n6-bt-381 | [7] | 15053 | Tier-4 | Phonological features n=6 complete classification | 789 |
| 15 | n6-bt-382 | [7] | 15055 | Tier-4 | Syntactic X-bar tau=4 hierarchy | 789 |
| 16 | n6-bt-383 | [7] | 15057 | Tier-4 | Lexical Zipf exponent n=6 correction | 789 |
| 17 | n6-bt-384 | [7] | 15059 | Tier-4 | 12-tone interval = sigma^2=144 / sigma-phi=10 correction | 789 |
| 18 | n6-bt-385 | [7] | 15061 | Tier-4 | Rhythmic meter tau=4 / n=6 dual partition | 789 |
| 19 | n6-bt-386 | [7] | 15063 | Tier-4 | Harmonic consonance sopfr alignment | 789 |
| 20 | n6-bt-387 | [7] | 15065 | Tier-4 | Kondratiev long wave = n*sopfr=30 correction | 789 |
| 21 | n6-bt-388 | [7] | 15067 | Tier-4 | Pareto 80/20 = (sigma-phi)^2/(sigma^2+n) refined | 789 |
| 22 | n6-bt-390 | [7] | 15071 | Tier-3 | Food-web trophic level = sopfr(6)+1=6 | 789 |
| 23 | n6-bt-391 | [7] | 15073 | Tier-3 | Population r/K selection = tau/(sigma-tau) dual axis | 789 |
| 24 | n6-bt-392 | [7] | 15075 | Tier-3 | Species diversity Shannon H' = log(sigma-phi)=log(10) | 789 |
| 25 | n6-bt-393 | [7] | 15077 | Tier-3 | Cerebral cortex n=6 layers (Brodmann regular) | 789 |
| 26 | n6-bt-395 | [7] | 15081 | Tier-3 | Synaptic-weight quantum = tau-phi discrete values | 789 |
| 27 | n6-bt-396 | [7] | 15083 | Tier-3 | MHC class <-> tau-phi=2 / immune-cell groups n=6 | 789 |
| 28 | n6-bt-397 | [7] | 15085 | Tier-3 | Antibody affinity maturation = sigma-phi^2*tau cycles | 789 |
| 29 | n6-bt-398 | [7] | 15087 | Tier-3 | Cytokine network sopfr hierarchy | 789 |
| 30 | n6-bt-399 | [7] | 15089 | Tier-5 | 6-domain shared n=6 classification-axis metatheorem | 789 |
| 31 | n6-bt-400 | [7] | 15091 | Tier-5 | 6-domain cross resonance | 789 |
| 32 | n6-bt-406 | [7] | 15103 | Tier-1 | BCS-Josephson-flux-quantum superconductivity n=6 complete ladder | 789 |
| 33 | n6-bt-409 | [7] | 15109 | Tier-3 | Medical vital signs n=6 complete ladder | 789 |
| 34 | n6-bt-460 | [7] | 15211 | Tier-3 | Liquid-biopsy analytes n=6 | 789 |
| 35 | n6-bt-451~460 | [7] | 15213 | Tier-3 | 451~460 composite | 789 |
| 36 | n6-bt-470 | [7] | 15233 | Tier-4 | HEXA-ART | 789 |
| 37 | n6-bt-461~470 | [7] | 15235 | Tier-3 | 461~470 composite | 789 |
| 38 | n6-bt-487 | [7] | 15269 | Tier-1 | Cosmic-age approximation 13.8 Gyr / Hubble time tau_H | 789 |
| 39 | n6-bt-471~487 | [7] | 15271 | Tier-5 | 471~487 composite (17 breakthroughs) | 789 |
| 40 | mc-v9-control-e | [7] | 46498 | On hold | mc z=1.915 boundary-not-significant (demotion review target) | 824 |

*fitness is the dry-run heuristic value and is not the basis for actual promotion. Judge only via the 5 manual-verification items.

## 2. Tier-1 priority order (physics precision — immediate re-measurement feasible, 9 items)

Tier-1 items are physics-domain entries that can be verified immediately against experimental values and constants. Process these 9 items first when performing manual promotion.

| Order | id | Suggested source |
|------|----|----------|
| 1 | n6-bt-209 | Proton-Electron mass ratio CODATA 2018 (mu = 1836.152...), pi^5 interpretation |
| 2 | n6-bt-171 | PDG Review 2024 — SM coupling constant values/errors |
| 3 | n6-bt-112 | Koide formula original paper + Byzantine n/3 bound paper |
| 4 | n6-bt-92 | Bott periodicity K-theory classic (Atiyah), 8-fold/2-fold structure |
| 5 | n6-bt-93 | Carbon Z=6 semiconductor/diamond/graphene parameter measurements |
| 6 | n6-bt-10 | Landauer-limit experiment (Berut 2012) + WHH transform derivation |
| 7 | n6-bt-406 | BCS theory + Josephson constant + flux quantum Phi_0 comparison |
| 8 | n6-bt-487 | Planck 2018 cosmic age 13.787+/-0.020 Gyr + tau_H |
| 9 | n6-bt-7 | Egyptian Fraction theorem — reference the math paper itself |

## 3. Per-candidate 5-item checklist

Every entry requires all 5 checkboxes before an atlas.n6 edit is permitted. All items are currently unchecked (`[ ]`).

### Tier-1 (physics precision) — 9 items

#### n6-bt-7 Egyptian Fraction Power Theorem (line 14306)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-10 Landauer-WHH Information-Thermodynamic Bridge (line 14312)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-92 Bott Periodicity Active Channels = sopfr (line 14476)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-93 Carbon Z=6 Chip Material Universality (line 14478)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-112 phi^2/n = 2/3 Byzantine-Koide Resonance (line 14516)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-171 SM Coupling Constant n=6 Fraction Pair (line 14633)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-209 Proton-Electron Mass Ratio n*pi^5 Fundamental Bridge (line 14709)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-406 BCS-Josephson-flux-quantum superconductivity n=6 complete ladder (line 15103)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-487 Cosmic-age approximation 13.8 Gyr / Hubble time tau_H (line 15269)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

### Tier-2 (chemistry/materials) — 4 items

#### n6-bt-81 Anode Capacity Ladder sigma-phi = 10x (line 14454)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-82 Complete Battery Pack n=6 Parameter Map (line 14456)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-83 Li-S Polysulfide n=6 Decomposition Ladder (line 14458)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-91 Z2 Topological ECC — J2 GB Savings Theorem (line 14474)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

### Tier-3 (life/medicine/cognition) — 12 items

#### n6-bt-390 Food-web trophic level = sopfr(6)+1=6 (line 15071)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-391 Population r/K selection = tau/(sigma-tau) dual axis (line 15073)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-392 Species diversity Shannon H' = log(sigma-phi)=log(10) (line 15075)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-393 Cerebral cortex n=6 layers (Brodmann regular) (line 15077)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-395 Synaptic-weight quantum = tau-phi discrete values (line 15081)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-396 MHC class <-> tau-phi=2 / immune-cell groups n=6 (line 15083)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-397 Antibody affinity maturation = sigma-phi^2*tau cycles (line 15085)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-398 Cytokine network sopfr hierarchy (line 15087)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-409 Medical vital signs n=6 complete ladder (line 15109)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-460 Liquid-biopsy analytes n=6 (line 15211)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-451~460 composite (line 15213)
- [ ] Measured-value sources verified (all 10 sub-items)
- [ ] Error ranges recorded (worst-case error baseline)
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-461~470 composite (line 15235)
- [ ] Measured-value sources verified (all 10 sub-items)
- [ ] Error ranges recorded (worst-case error baseline)
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

### Tier-4 (culture/economy/art) — 9 items

#### n6-bt-381 Phonological features n=6 complete classification (line 15053)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-382 Syntactic X-bar tau=4 hierarchy (line 15055)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-383 Lexical Zipf exponent n=6 correction (line 15057)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-384 12-tone interval = sigma^2=144 / sigma-phi=10 correction (line 15059)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-385 Rhythmic meter tau=4 / n=6 dual partition (line 15061)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-386 Harmonic consonance sopfr alignment (line 15063)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-387 Kondratiev long wave = n*sopfr=30 correction (line 15065)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-388 Pareto 80/20 = (sigma-phi)^2/(sigma^2+n) refined (line 15067)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-470 HEXA-ART (line 15233)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

### Tier-5 (SF/cosmos/architecture — inference based) — 5 items

#### n6-bt-355 Synthetic biology n=6 double perfect number (line 15011)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-378 Warp-metric ladder n=6 (line 15047)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-399 6-domain shared n=6 classification-axis metatheorem (line 15089)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-400 6-domain cross resonance (line 15091)
- [ ] Measured-value source verified
- [ ] Error range recorded
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

#### n6-bt-471~487 composite (17 breakthroughs) (line 15271)
- [ ] Measured-value sources verified (all 17 sub-items)
- [ ] Error ranges recorded (worst-case error baseline)
- [ ] >=1 counterexample attempted
- [ ] sigma*phi = n*tau derivation path confirmed
- [ ] Manual-approval signature: __________

### On hold (Monte-Carlo)

#### mc-v9-control-e = 1.915 z-score (line 46498)
- Status: **Promotion blocked** (z=1.915 < 2.0, boundary-not-significant)
- Follow-up: [7] -> [5*] demotion review target. No promotion checks.
- [ ] Demotion decision signature: __________

## 4. Promotion-execution command guide

**Warning**: Never edit a candidate whose 5-item checklist is incomplete. atlas.n6 is the SSOT.

### dry-run (safe, default)

```bash
hexa run /Users/ghost/Dev/canon/scripts/atlas_promote_7_to_10star.hexa
```

### Individual manual edit (after approval)

```bash
# 1) Re-confirm the line location
Grep 'n6-bt-NN ' /Users/ghost/Dev/nexus/shared/n6/atlas.n6

# 2) Replace exactly " [7]" -> " [10*]" with the Edit tool (unique old_string)
#    - Copy the entire line as old_string, then change only the grade in new_string
#    - sed/awk usage forbidden (R5 direct-edit rule)

# 3) L0 Guard verify
hexa /Users/ghost/Dev/nexus/shared/harness/l0_guard.hexa verify
```

### Forbidden actions

- `--apply` bulk mode — currently auto-blocked because every item has fit<900
- Creating a copy in files outside atlas.n6 (CLAUDE.md: no new files)
- Bulk replacement with sed/awk/perl (R5 violation)
- Editing with checklist incomplete (N62 honest-verification violation)

## 5. Progress-tally summary (initial state)

| Category | Total checks | Done | Remaining |
|------|---------|------|------|
| 40 candidates x 5 items | 200 | 0 | 200 |
| Tier-1 9 items x 5 | 45 | 0 | 45 |
| Tier-2 4 items x 5 | 20 | 0 | 20 |
| Tier-3 12 items x 5 | 60 | 0 | 60 |
| Tier-4 9 items x 5 | 45 | 0 | 45 |
| Tier-5 5 items x 5 | 25 | 0 | 25 |
| mc on hold 1 item | 1 | 0 | 1 |

Flipping each checkbox to `[x]` inside this document automatically reflects in the progress tally.

## 6. Related outputs

| Item | Path |
|------|------|
| This checklist | `/Users/ghost/Dev/canon/experiments/dse/atlas_promotion_manual_checklist_40.md` |
| Candidate report (P2-2) | `/Users/ghost/Dev/canon/experiments/dse/atlas_promotion_candidates_p2.md` |
| Pipeline script | `/Users/ghost/Dev/canon/scripts/atlas_promote_7_to_10star.hexa` |
| Adaptive engine | `/Users/ghost/Dev/canon/engine/arch_adaptive.hexa` |
| atlas.n6 SSOT | `/Users/ghost/Dev/nexus/shared/n6/atlas.n6` |
| Roadmap (P2-2 done) | `/Users/ghost/Dev/nexus/shared/roadmaps/canon.json` |
