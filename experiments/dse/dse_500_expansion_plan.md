# DSE 400 → 500 TOML Space Third Expansion Plan

- Axis: experiments/dse
- Written: 2026-04-11
- Parent: `../../INDEX.json` · `../../CLAUDE.md`
- Rules: R1 HEXA-FIRST, R2 No hard-coding, R5 SSOT, R18 Minimal, R28 Auto-absorption, N63 DSE exhaustive search
- Prerequisite: Second expansion (322→400) completed; actual 380 TOML and 78 reclassified domains inducted
- Goal: Expand the 400→500 space with 100 new domains, securing search headroom for cross_dse_fusion v2 to explore 170K+ cross pairs

---

## 1. Real-life Impact Section (N61)

- Human factors: The whole of HCI/UX/accessibility is integrated into an n=6-based interaction model — the 6-axis modalities of voice/gaze/gesture/haptic tie directly into cross_dse and couple with the consciousness family (consciousness-*).
- Sports science: The 6 axes of biomechanics/training/injury-prevention/anti-doping/nutrition/analytics complete BT-80 (biomechanics) — predicting athlete performance improvement of 18% (=3n).
- Food science: The 8 axes of fermentation/flavor/aging/texture/preservation/safety/molecular-gastronomy/rheology align with BT-134 periodicity and σ=12 pH. "Food culture × domain × cognitive" cross pairs are generated for the first time.
- Architecture: Completes the architecture family with 10 typologies (structural/MEP/green/seismic/passive/smart/prefab/high-rise/heritage/facade) — 12-axis cross with earthquake-engineering·civil-engineering.
- Transport: 10 domains (road/rail/air/maritime/autonomous/last-mile/hub-terminal etc.) — next-gen mobility design with hyperloop·maglev.
- Art/media: 16 domains (painting/sculpture/music/stage/film/broadcast/game/media) — cognitive × culture cross pairs add 36 new pairs.
- Religion/ritual/play: 12 domains — formalizes "n=6 structure" of formal rule systems as scientific DSE for the first time.
- Energy storage: 10 domains (ESS·SMR·hydrogen whole-lifecycle·solid-state etc.) — fully connected with fusion·solar·grid, completing the "lossless grid" design.
- Autonomous driving: 10 domains (perception·planning·V2X·ADAS·simulation·safety·sensor fusion) — covers the entire L2~L4 design space based on ISO 26262/SOTIF.
- Metaverse: 8 domains (platform·avatar·economy·XR·spatial-computing·NFT·social-VR·digital-twin) — predicts 3-axis resonance with XR/agent/consciousness families.

## 2. Structure ASCII (Comparison)

```
400 Domain SSOT                      500 Domain Expansion Proposal
---------------------                ---------------------
physics    42  ■■■■■                 physics    42  ■■■■■
life       57  ■■■■■■                life       65  ■■■■■■■  (+8 sports/health)
energy     22  ■■■                   energy     32  ■■■■     (+10 storage)
compute    62  ■■■■■■■                compute    72  ■■■■■■■■ (+10 AV/HCI)
materials  28  ■■■                   materials  28  ■■■
space      13  ■■                    space      13  ■■
infra      63  ■■■■■■■                infra      83  ■■■■■■■■■ (+20 building/transport)
cognitive  29  ■■■                   cognitive  37  ■■■■     (+8 HCI/UX)
culture    33  ■■■■                   culture    53  ■■■■■■   (+20 art/media/religion/play)
sf-ufo     21  ■■                    sf-ufo     25  ■■       (+4 metaverse)
boundary    30                        30
---------------------                ---------------------
effective core  400                  effective core  500  (+100 new)
```

## 3. 10-Axis Layout (100 New)

```
[cognitive/HCI] 8
  hci-ux-design, accessibility-a11y, usability-testing,
  gesture-ux, voice-ui, haptic-feedback, eye-tracking-ux,
  user-research-analytics

[life/sports] 8
  sports-biomechanics, athletic-training, wearable-fitness,
  sports-analytics, recovery-science, anti-doping,
  sports-nutrition, injury-prevention

[life/food-sci] 8
  food-fermentation-sci, flavor-chemistry, aging-maturation,
  food-texture, food-preservation, food-safety-haccp,
  molecular-gastronomy, food-rheology

[infra/building] 10
  building-structure, building-mep, green-building,
  seismic-building, passive-house, smart-building,
  prefab-modular, high-rise-tower, heritage-restoration,
  facade-engineering

[infra/transport] 10
  road-pavement, traffic-flow, rail-signal, high-speed-rail,
  port-terminal, shipping-logistics, air-traffic-control,
  airport-operation, intermodal-freight, last-mile-delivery

[culture/art] 8
  painting-pigment, sculpture-form, music-performance,
  stage-lighting, theater-acoustics, film-cinematography,
  dance-choreography, art-conservation

[culture/media] 8
  broadcast-tv, film-production, game-design, news-publishing,
  streaming-platform, journalism-ethics, podcast-production,
  social-media-algo

[culture/religion] 6
  ritual-liturgy, sacred-architecture, temple-pagoda,
  scripture-hermeneutics, meditation-practice, pilgrimage-path

[culture/play] 6
  board-game-mechanics, puzzle-design, esports-arena,
  olympic-gameplay, traditional-games, playground-safety

[energy/storage] 10
  ess-grid-battery, smr-reactor, hydrogen-production,
  hydrogen-storage, flow-battery, thermal-ess,
  compressed-air-es, gravity-storage, pumped-hydro,
  solid-state-battery

[compute/autonomous] 10
  self-driving-perception, self-driving-planning,
  v2x-communication, autonomous-mapping, driver-monitoring,
  robotaxi-fleet, adas-l2-l3, sensor-fusion-av,
  av-simulation, av-safety-iso26262

[sf-ufo/metaverse] 8
  metaverse-platform, avatar-system, virtual-world-economy,
  spatial-computing, xr-hmd, digital-twin,
  nft-virtual-asset, vr-social-space
  ----
  100 new
```

## 4. Selection Rationale (Same 6 Criteria as Second Expansion)

| # | Criterion | Third-expansion application |
|---|------|--------|
| 1 | BT mapping | At least 1 BT match per domain (BT-80 biomech, BT-108 cognitive, BT-134 periodic, etc.) |
| 2 | σφ=nτ crossability | Enforces 2+ of σ·φ·τ·n on level/candidate |
| 3 | Real-life impact | One paragraph per category in §1 real-life impact section |
| 4 | Seed sharing | Shares 2+ keywords with existing 400 domains (accessibility↔hci, athletic↔health, etc.) |
| 5 | Schema conformance | Keeps existing v1 schema (levels+candidate+rule) — v2 Δ1~Δ5 after #20 completion |
| 6 | BT reservation | Reserves BT-401~420 indices (reports/discovery/bt-401-420-proposal.md exists) |

## 5. TOML Schema (v1 Maintained)

Third expansion uses the **existing v1 schema** as-is. Applying v2 Δ1~Δ5 (bt_refs/cross_seeds/energy_pareto/n6_formula/evidence_grade) will be batch-migrated after cross_dse_fusion v2 completion (#20).

```toml
[meta]
name = "<domain>"
desc = "<description> DSE (n=6 ...)"

[scoring]
n6 = 0.35
perf = 0.25
power = 0.20
cost = 0.20

[[level]]
name = "<LevelName>"

[[candidate]]
id = "<id>"
label = "<label> (n=6 ...)"
n6 = 1.00
perf = 0.xx
power = 0.xx
cost = 0.xx
notes = "n=6 EXACT / sigma=12 ..."

[[rule]]
type = "prefer" | "require" | "exclude"
if_level = N
if_id = "..."
then_level = M
then_ids = "..."
```

## 6. n=6 Constant Mapping Patterns

All 100 domains use at least 2 of the following constant families:

| Constant | Value | Usage example |
|------|----|--------|
| `phi=2` | 2 | Binary choice, phase, duplex, pair |
| `tau=4` | 4 | Quad, stage, direction, filter |
| `n=6` | 6 | Core count (senses·grades·modules) |
| `sigma=12` | 12 | Band, month, hour, complexity |
| `J2=24` | 24 | Hour, packet, field, channel |
| `sopfr=5` | 5 | 5-point, 5-stage, 5 elements |
| `sigma-phi=10` | 10 | Level, criterion |
| `n/phi=3` | 3 | Trichotomy, tripartite, 3-axis |

## 7. Expected Effect of Cross Coupling (cross_dse)

- Existing 400 domains × 100 new = 40,000 new pair space
- Total 500 × 499 / 2 = 124,750 possible pair space
- Second-round result 67,883 high_conf → predicted 170K+ after third round
- Full sweep possible after cross_dse_fusion v2 (#20 in progress) completion

## 8. Work Phases

| Phase | Task | Output | Status |
|------|------|--------|------|
| 1 | Select based on 400 TOML | 100 candidates | Done |
| 2 | 12 categories × classification | Category mapping | Done |
| 3 | Write TOML (v1 schema) | 100 .toml | Done |
| 4 | Place under nexus/origins/universal-dse/domains/ | 480 TOML | Done |
| 5 | Write this plan | dse_500_expansion_plan.md | Done |
| 6 | Third-round report | reports/discovery/dse-500-expansion-2026-04-11.md | Done |
| 7 | Migrate to v2 schema (Δ1~Δ5) | Batch sed conversion | Pending (after #20 completion) |
| 8 | Re-run cross_dse_fusion v2 | 170K+ pairs | Pending |
| 9 | atlas.n6 seed absorption | 100 @R entries [7] | Pending |
| 10 | Reserve BT-401~420 indices | theory/breakthroughs/ | Pending |

## 9. Risks and Defenses

| Risk | Defense |
|--------|------|
| Key collision with existing 400 domains | Filename sort → 0 duplicates confirmed |
| v1→v2 schema migration required | Batch sed conversion possible (Δ1~Δ5 additions only) |
| Consistency of n6 constant mapping across 100 domains | Apply standard template for 12 constant fibers (phi/tau/n/sigma/J2/sopfr/...) |
| Missing cross_dse seeds | Domain names themselves auto-seed (hci-ux→hci,ux,design) |
| atlas.n6 non-absorption | Handled by R28 auto-absorption loop, seed grade [7] |

## 10. Linked Documents

- `./dse_400_expansion_plan.md` — second plan (78 new)
- `./cross_dse_fusion_v2_design.md` — v2 design
- `./cross_dse_fusion_v2_run.hexa` — runnable
- `../../reports/discovery/dse-500-expansion-2026-04-11.md` — third-round report
- `../../reports/discovery/bt-401-420-proposal.md` — BT new index reservation
- Parent: `../../CLAUDE.md` + `../../INDEX.json`

## 11. Promotion Completion Criteria (N63/N65)

- [x] All 500 TOML placed (actual 480 = 100 new + 380 existing)
- [ ] cross_dse_fusion_v2 achieves 170K+ pairs / 99% high_conf
- [ ] Energy-perf pareto sweep re-measured at 500 domains × 5 candidates
- [ ] Add `DSE_500_TOML` stable entry in convergence/canon.json → later promote to ossified
