# Phase 3 Batch Plan — domains/ priority track (200 files, 10 batches)

**Date**: 2026-04-24
**Author**: Phase 3 planner (automated)
**Status**: planning only — no code edits in this proposal
**Scope**: adds only this plan under `reports/sessions/`; allowlist/domains/.md files remain untouched
**Compliance**:
- own#1 (doc-english-hard): this file under `reports/` is in own#1 scope and must be CJK-free. Verified by `python3 tool/own_doc_lint.py --rule 1`.
- own#11 (bt-solution-claim-ban): targets described as "draft/target/candidate" only. No "solved"/"proven" claims.
- own#17 (README English-only): out of scope for this plan.

---

## 1. Priority Criteria

The source roadmap `proposals/own1-hard-english-only-translation-roadmap-2026-04-24.md` describes this wave as its "Phase 2 — domains/ priority track (200/417)" (the roadmap was drafted before Phase 0 completed; real execution order places this as Phase 3 since Phase 0+1+2 are now done).

The roadmap lists exemplar priorities but does not enumerate a precise 200-file set:

> - 4 files in `domains/culture/` (largest debt, 1457 chars)
> - `chip-*` sub-domains (many consistent templates)

Since the roadmap does not enumerate the full 200, the documented fallback rule is applied:

1. Rank all 417 `domains/` allowlist entries by CJK character count ascending (shortest = easiest win).
2. Take the bottom 200 by CJK count.
3. Regroup the selected 200 by first-level subdirectory to keep each batch under a single subtree and minimize cross-batch edit conflicts on the allowlist JSON.
4. Pack into 10 batches of exactly 20 files each, preserving subtree contiguity where possible.

Deviation note vs. roadmap exemplars:
- The roadmap suggested starting with the 4 largest culture/ files. The fallback rule instead schedules them later (batches 5-6) because shortest-first produces more stable early wins and keeps the allowlist-edit contention risk linear. All 26 culture/ files are included in the 200-file set regardless.
- `chip-*` subdomains under `domains/compute/chip-architecture/`, `chip-design/`, etc. are mostly long files (>2277 chars) and therefore fall outside the bottom-200. They are deferred to a later wave. 35 `compute/` entries were selected from other compute sub-trees (network-protocol/certificates/, etc.) because they have lower CJK counts.

## 2. Selection Summary

| Subdirectory | Files in 200-set | CJK Total | Avg CJK |
|---|---:|---:|---:|
| `domains/infra/` | 58 | 73660 | 1270.0 |
| `domains/compute/` | 35 | 29850 | 852.9 |
| `domains/life/` | 30 | 50764 | 1692.1 |
| `domains/culture/` | 26 | 35762 | 1375.5 |
| `domains/materials/` | 17 | 24458 | 1438.7 |
| `domains/physics/` | 11 | 6513 | 592.1 |
| `domains/cognitive/` | 8 | 6525 | 815.6 |
| `domains/energy/` | 6 | 11093 | 1848.8 |
| `domains/sf-ufo/` | 6 | 11977 | 1996.2 |
| `domains/space/` | 3 | 13 | 4.3 |
| **Total** | **200** | **250615** | **1253.1** |

## 3. Batch Overview

| Batch | Label | Files | CJK Total | Primary Subtree |
|---|---|---:|---:|---|
| 1 | `phase-3-1-infra-a` | 20 | 23857 | `domains/infra/` |
| 2 | `phase-3-2-infra-b` | 20 | 25455 | `domains/infra/` |
| 3 | `phase-3-3-infra-c-life-tail` | 20 | 24355 | `domains/infra/` |
| 4 | `phase-3-4-life-a` | 20 | 32580 | `domains/life/` |
| 5 | `phase-3-5-life-b-culture-a` | 20 | 33745 | `domains/culture/` |
| 6 | `phase-3-6-culture-b-physics-top` | 20 | 21551 | `domains/culture/` |
| 7 | `phase-3-7-physics-tail-compute-a` | 20 | 8322 | `domains/compute/` |
| 8 | `phase-3-8-compute-b` | 20 | 26684 | `domains/compute/` |
| 9 | `phase-3-9-materials-cognitive-a` | 20 | 25849 | `domains/materials/` |
| 10 | `phase-3-10-cognitive-tail-energy-sf-space` | 20 | 28217 | `domains/energy/` |
| **Total** | — | **200** | **250615** | — |

Note on CJK-per-batch: the 3,000-CJK target from the kickoff prompt is not feasible for a 200-file/10-batch packing; the minimum achievable average is ~25k/batch (200 files * ~1253 avg CJK). Batches 4 and 5 peak at ~33k CJK due to larger life/ and culture/ files. These are acceptable per the "outliers OK" clause.

## 4. File Lists Per Batch

### Batch 1: `phase-3-1-infra-a` (20 files, CJK=23857)

| # | Path | CJK |
|---:|---|---:|
| 1 | `domains/infra/forensic-science/forensic-science.md` | 3 |
| 2 | `domains/infra/robotics/robotics.md` | 1231 |
| 3 | `domains/infra/transportation/transportation.md` | 1233 |
| 4 | `domains/infra/fun-car/fun-car.md` | 1240 |
| 5 | `domains/infra/marketing/marketing.md` | 1252 |
| 6 | `domains/infra/motorcycle/motorcycle.md` | 1252 |
| 7 | `domains/infra/robotics-transport/robotics-transport.md` | 1253 |
| 8 | `domains/infra/surveying/surveying.md` | 1254 |
| 9 | `domains/infra/environment-thermal/environment-thermal.md` | 1255 |
| 10 | `domains/infra/safety/safety.md` | 1255 |
| 11 | `domains/infra/geology/geology.md` | 1258 |
| 12 | `domains/infra/mining/mining.md` | 1258 |
| 13 | `domains/infra/hexa-weather/hexa-weather.md` | 1259 |
| 14 | `domains/infra/aviation/aviation.md` | 1261 |
| 15 | `domains/infra/oceanography/oceanography.md` | 1261 |
| 16 | `domains/infra/autonomous-driving/autonomous-driving.md` | 1265 |
| 17 | `domains/infra/manufacturing-quality/manufacturing-quality.md` | 1266 |
| 18 | `domains/infra/carbon-capture/carbon-capture.md` | 1267 |
| 19 | `domains/infra/economics-finance/economics-finance.md` | 1267 |
| 20 | `domains/infra/law-justice/law-justice.md` | 1267 |

### Batch 2: `phase-3-2-infra-b` (20 files, CJK=25455)

| # | Path | CJK |
|---:|---|---:|
| 1 | `domains/infra/seabed-grid/seabed-grid.md` | 1267 |
| 2 | `domains/infra/economics/economics.md` | 1268 |
| 3 | `domains/infra/electric-vehicle/electric-vehicle.md` | 1268 |
| 4 | `domains/infra/ocean/ocean.md` | 1268 |
| 5 | `domains/infra/water-treatment/water-treatment.md` | 1268 |
| 6 | `domains/infra/naval-architecture/naval-architecture.md` | 1269 |
| 7 | `domains/infra/desal/desal.md` | 1270 |
| 8 | `domains/infra/meteorology/meteorology.md` | 1270 |
| 9 | `domains/infra/cartography-gis/cartography-gis.md` | 1271 |
| 10 | `domains/infra/desalination/desalination.md` | 1271 |
| 11 | `domains/infra/hexa-exo/hexa-exo.md` | 1272 |
| 12 | `domains/infra/hexa-skyway/hexa-skyway.md` | 1273 |
| 13 | `domains/infra/jurisprudence/jurisprudence.md` | 1273 |
| 14 | `domains/infra/tsunami-shield/tsunami-shield.md` | 1274 |
| 15 | `domains/infra/skyway/skyway.md` | 1276 |
| 16 | `domains/infra/hexa-defense/hexa-defense.md` | 1277 |
| 17 | `domains/infra/hexa-tsunami/hexa-tsunami.md` | 1278 |
| 18 | `domains/infra/printing/printing.md` | 1280 |
| 19 | `domains/infra/earthquake-engineering/earthquake-engineering.md` | 1281 |
| 20 | `domains/infra/fire-science/fire-science.md` | 1281 |

### Batch 3: `phase-3-3-infra-c-life-tail` (20 files, CJK=24355)

| # | Path | CJK |
|---:|---|---:|
| 1 | `domains/infra/environmental-protection/environmental-protection.md` | 1283 |
| 2 | `domains/infra/airbag/airbag.md` | 1285 |
| 3 | `domains/infra/climate/climate.md` | 1285 |
| 4 | `domains/infra/earth-defense/earth-defense.md` | 1290 |
| 5 | `domains/infra/smart-city/smart-city.md` | 1290 |
| 6 | `domains/infra/weather-control/weather-control.md` | 1290 |
| 7 | `domains/infra/ecommerce-fintech/ecommerce-fintech.md` | 1291 |
| 8 | `domains/infra/governance-safety-urban/governance-safety-urban.md` | 1291 |
| 9 | `domains/infra/underground-tunnel/underground-tunnel.md` | 1291 |
| 10 | `domains/infra/civil-engineering/civil-engineering.md` | 1293 |
| 11 | `domains/infra/ultimate-safety/ultimate-safety.md` | 1296 |
| 12 | `domains/infra/insurance/insurance.md` | 1299 |
| 13 | `domains/infra/calendar-time-geography/calendar-time-geography.md` | 1300 |
| 14 | `domains/infra/monetary-history/monetary-history.md` | 1300 |
| 15 | `domains/infra/architecture/architecture.md` | 1309 |
| 16 | `domains/infra/currency-economics/currency-economics.md` | 1318 |
| 17 | `domains/infra/control-automation/control-automation.md` | 1425 |
| 18 | `domains/infra/construction-structural/construction-structural.md` | 2212 |
| 19 | `domains/life/nuclear-medicine/nuclear-medicine.md` | 3 |
| 20 | `domains/life/music-therapy/music-therapy.md` | 4 |

### Batch 4: `phase-3-4-life-a` (20 files, CJK=32580)

| # | Path | CJK |
|---:|---|---:|
| 1 | `domains/life/sleep-medicine/sleep-medicine.md` | 4 |
| 2 | `domains/life/urban-farming/urban-farming.md` | 4 |
| 3 | `domains/life/gastrointestinal-medicine/gastrointestinal-medicine.md` | 5 |
| 4 | `domains/life/radiation-biology/radiation-biology.md` | 6 |
| 5 | `domains/life/tibetan-medicine/tibetan-medicine.md` | 6 |
| 6 | `domains/life/dog-robot-test/dog-robot-test.md` | 1177 |
| 7 | `domains/life/hexa-limb/hexa-limb.md` | 2218 |
| 8 | `domains/life/hiv-treatment/hiv-treatment.md` | 2224 |
| 9 | `domains/life/hiv/hiv.md` | 2227 |
| 10 | `domains/life/viticulture/viticulture.md` | 2230 |
| 11 | `domains/life/neuro/neuro.md` | 2235 |
| 12 | `domains/life/agriculture/agriculture.md` | 2236 |
| 13 | `domains/life/synbio/synbio.md` | 2238 |
| 14 | `domains/life/aquaculture/aquaculture.md` | 2240 |
| 15 | `domains/life/tattoo-removal/tattoo-removal.md` | 2246 |
| 16 | `domains/life/womens-intimate-cleanser/womens-intimate-cleanser.md` | 2249 |
| 17 | `domains/life/neuropharmacology/neuropharmacology.md` | 2253 |
| 18 | `domains/life/virology/virology.md` | 2260 |
| 19 | `domains/life/cancer-therapy/cancer-therapy.md` | 2261 |
| 20 | `domains/life/perfumery/perfumery.md` | 2261 |

### Batch 5: `phase-3-5-life-b-culture-a` (20 files, CJK=33745)

| # | Path | CJK |
|---:|---|---:|
| 1 | `domains/life/mycology/mycology.md` | 2263 |
| 2 | `domains/life/pharmacology/pharmacology.md` | 2270 |
| 3 | `domains/life/hair-regeneration/hair-regeneration.md` | 2272 |
| 4 | `domains/life/medical-device/medical-device.md` | 2272 |
| 5 | `domains/life/entomology/entomology.md` | 2273 |
| 6 | `domains/life/coffee-science/coffee-science.md` | 2275 |
| 7 | `domains/life/ecology-agriculture-food/ecology-agriculture-food.md` | 2275 |
| 8 | `domains/life/wine-enology/wine-enology.md` | 2277 |
| 9 | `domains/culture/ethnomusicology/ethnomusicology.md` | 5 |
| 10 | `domains/culture/ar-vr-xr/ar-vr-xr.md` | 1370 |
| 11 | `domains/culture/music/music.md` | 1409 |
| 12 | `domains/culture/baduk/baduk.md` | 1413 |
| 13 | `domains/culture/mountaineering/mountaineering.md` | 1416 |
| 14 | `domains/culture/yoga/yoga.md` | 1416 |
| 15 | `domains/culture/dance-choreography/dance-choreography.md` | 1420 |
| 16 | `domains/culture/audio/audio.md` | 1423 |
| 17 | `domains/culture/numismatics/numismatics.md` | 1423 |
| 18 | `domains/culture/horology/horology.md` | 1424 |
| 19 | `domains/culture/photography/photography.md` | 1424 |
| 20 | `domains/culture/taekwondo/taekwondo.md` | 1425 |

### Batch 6: `phase-3-6-culture-b-physics-top` (20 files, CJK=21551)

| # | Path | CJK |
|---:|---|---:|
| 1 | `domains/culture/linguistics/linguistics.md` | 1427 |
| 2 | `domains/culture/religion/religion.md` | 1430 |
| 3 | `domains/culture/archaeology/archaeology.md` | 1434 |
| 4 | `domains/culture/writing-systems/writing-systems.md` | 1437 |
| 5 | `domains/culture/biometrics/biometrics.md` | 1438 |
| 6 | `domains/culture/music-mathematics/music-mathematics.md` | 1438 |
| 7 | `domains/culture/hangul-script/hangul-script.md` | 1439 |
| 8 | `domains/culture/library-science/library-science.md` | 1439 |
| 9 | `domains/culture/social-architecture/social-architecture.md` | 1440 |
| 10 | `domains/culture/dice-probability/dice-probability.md` | 1450 |
| 11 | `domains/culture/telecom-linguistics/telecom-linguistics.md` | 1451 |
| 12 | `domains/culture/games-sports/games-sports.md` | 1456 |
| 13 | `domains/culture/bell-clockwork/bell-clockwork.md` | 1457 |
| 14 | `domains/culture/religion-mythology/religion-mythology.md` | 1458 |
| 15 | `domains/physics/computational-fluid-dynamics/computational-fluid-dynamics.md` | 6 |
| 16 | `domains/physics/m-theory-11d/m-theory-11d.md` | 215 |
| 17 | `domains/physics/wormhole/wormhole.md` | 250 |
| 18 | `domains/physics/tabletop-blackhole/tabletop-blackhole.md` | 276 |
| 19 | `domains/physics/calabi-yau-nav/calabi-yau-nav.md` | 296 |
| 20 | `domains/physics/warp-drive/warp-drive.md` | 314 |

### Batch 7: `phase-3-7-physics-tail-compute-a` (20 files, CJK=8322)

| # | Path | CJK |
|---:|---|---:|
| 1 | `domains/physics/multiverse-nav/multiverse-nav.md` | 337 |
| 2 | `domains/physics/pet-cyclotron/pet-cyclotron.md` | 815 |
| 3 | `domains/physics/particle-accelerator/particle-accelerator.md` | 967 |
| 4 | `domains/physics/tabletop-antimatter/tabletop-antimatter.md` | 1094 |
| 5 | `domains/physics/meta-closure-nav/meta-closure-nav.md` | 1943 |
| 6 | `domains/compute/network-protocol/certificates/wifi6-cert/wifi6-cert.md` | 177 |
| 7 | `domains/compute/network-protocol/certificates/ethernet-cert/ethernet-cert.md` | 184 |
| 8 | `domains/compute/network-protocol/certificates/pcie-cert/pcie-cert.md` | 185 |
| 9 | `domains/compute/network-protocol/certificates/usb-cert/usb-cert.md` | 185 |
| 10 | `domains/compute/network-protocol/certificates/starlink-cert/starlink-cert.md` | 192 |
| 11 | `domains/compute/network-protocol/certificates/5g-nr-cert/5g-nr-cert.md` | 197 |
| 12 | `domains/compute/network-protocol/certificates/6g-cert/6g-cert.md` | 197 |
| 13 | `domains/compute/network-protocol/certificates/bt6-0-cert/bt6-0-cert.md` | 200 |
| 14 | `domains/compute/network-protocol/certificates/lorawan-cert/lorawan-cert.md` | 201 |
| 15 | `domains/compute/network-protocol/certificates/displayport-cert/displayport-cert.md` | 205 |
| 16 | `domains/compute/network-protocol/certificates/hdmi-cert/hdmi-cert.md` | 207 |
| 17 | `domains/compute/network-protocol/certificates/nvme-cert/nvme-cert.md` | 226 |
| 18 | `domains/compute/network-protocol/displayport/displayport.md` | 262 |
| 19 | `domains/compute/network-protocol/hdmi/hdmi.md` | 273 |
| 20 | `domains/compute/network-protocol/usb/usb.md` | 275 |

### Batch 8: `phase-3-8-compute-b` (20 files, CJK=26684)

| # | Path | CJK |
|---:|---|---:|
| 1 | `domains/compute/network-protocol/ethernet/ethernet.md` | 292 |
| 2 | `domains/compute/network-protocol/pcie/pcie.md` | 310 |
| 3 | `domains/compute/network-protocol/nvme/nvme.md` | 371 |
| 4 | `domains/compute/hexa-macos/vt-6tier-terminal/vt-6tier-terminal.md` | 555 |
| 5 | `domains/compute/chip-architecture/l7-quantum-hybrid-transmon/l7-quantum-hybrid-transmon.md` | 778 |
| 6 | `domains/compute/chip-architecture/l8-topo-anyon-majorana/l8-topo-anyon-majorana.md` | 831 |
| 7 | `domains/compute/chip-architecture/l9-field-photon-neuro/l9-field-photon-neuro.md` | 900 |
| 8 | `domains/compute/chip-architecture/protocol-bridge-20-rtl/protocol-bridge-20-rtl.md` | 1143 |
| 9 | `domains/compute/chip-interconnect/chip-interconnect.md` | 1420 |
| 10 | `domains/compute/chip-architecture/l11-quantum-dot-6qubit-qec/l11-quantum-dot-6qubit-qec.md` | 1427 |
| 11 | `domains/compute/chip-architecture/l15-meta-integration-closure/l15-meta-integration-closure.md` | 1433 |
| 12 | `domains/compute/chip-yield/chip-yield.md` | 1640 |
| 13 | `domains/compute/chip-packaging/chip-packaging.md` | 1728 |
| 14 | `domains/compute/chip-thermal-power/chip-thermal-power.md` | 1763 |
| 15 | `domains/compute/chip-architecture/mk3-roadmap-l1-l15-audit/mk3-roadmap-l1-l15-audit.md` | 1905 |
| 16 | `domains/compute/chip-verify-test/chip-verify-test.md` | 1933 |
| 17 | `domains/compute/chip-architecture/hexa-consciousness/hexa-consciousness.md` | 1938 |
| 18 | `domains/compute/chip-process/chip-process.md` | 2034 |
| 19 | `domains/compute/chip-architecture/l12-nuclear-isomer-storage/l12-nuclear-isomer-storage.md` | 2064 |
| 20 | `domains/compute/chip-architecture/monster-leech-mapping/monster-leech-mapping.md` | 2219 |

### Batch 9: `phase-3-9-materials-cognitive-a` (20 files, CJK=25849)

| # | Path | CJK |
|---:|---|---:|
| 1 | `domains/materials/hexa-glass/hexa-glass.md` | 1409 |
| 2 | `domains/materials/paper/paper.md` | 1412 |
| 3 | `domains/materials/hexa-fabric/hexa-fabric.md` | 1415 |
| 4 | `domains/materials/pet-film/pet-film.md` | 1422 |
| 5 | `domains/materials/gemology/gemology.md` | 1428 |
| 6 | `domains/materials/epoxy/epoxy.md` | 1430 |
| 7 | `domains/materials/recycling/recycling.md` | 1432 |
| 8 | `domains/materials/swordsmithing/swordsmithing.md` | 1433 |
| 9 | `domains/materials/hexa-recycle/hexa-recycle.md` | 1437 |
| 10 | `domains/materials/nylon/nylon.md` | 1444 |
| 11 | `domains/materials/fashion-textile/fashion-textile.md` | 1447 |
| 12 | `domains/materials/textile-dyeing/textile-dyeing.md` | 1449 |
| 13 | `domains/materials/aramid/aramid.md` | 1451 |
| 14 | `domains/materials/concrete/concrete.md` | 1453 |
| 15 | `domains/materials/tire-cord/tire-cord.md` | 1460 |
| 16 | `domains/materials/lutherie/lutherie.md` | 1467 |
| 17 | `domains/materials/concrete-technology/concrete-technology.md` | 1469 |
| 18 | `domains/cognitive/hexa-speak/proto/README.md` | 186 |
| 19 | `domains/cognitive/hexa-speak/proto/rtl/README.md` | 588 |
| 20 | `domains/cognitive/hexa-speak/proto/n6-speak-v2-spec.md` | 617 |

### Batch 10: `phase-3-10-cognitive-tail-energy-sf-space` (20 files, CJK=28217)

| # | Path | CJK |
|---:|---|---:|
| 1 | `domains/cognitive/hexa-speak/proto/rtl/soc_drc_lvs_report.md` | 682 |
| 2 | `domains/cognitive/hexa-speak/rtl/README.md` | 720 |
| 3 | `domains/cognitive/hexa-speak/proto/rtl/gdsii_signoff.md` | 827 |
| 4 | `domains/cognitive/brain-computer-interface/bci-6ch-n6-mapping/bci-6ch-n6-mapping.md` | 847 |
| 5 | `domains/cognitive/ai-multimodal/ai-multimodal.md` | 2058 |
| 6 | `domains/energy/tabletop-fusion/tabletop-fusion.md` | 1723 |
| 7 | `domains/energy/pemfc/pemfc.md` | 1849 |
| 8 | `domains/energy/energy-efficiency/energy-efficiency.md` | 1870 |
| 9 | `domains/energy/hvac-system/hvac-system.md` | 1875 |
| 10 | `domains/energy/battery-energy/battery-energy.md` | 1881 |
| 11 | `domains/energy/datacenter-reactor/datacenter-reactor.md` | 1895 |
| 12 | `domains/sf-ufo/vampire/vampire.md` | 1871 |
| 13 | `domains/sf-ufo/snowflake-ice/snowflake-ice.md` | 1879 |
| 14 | `domains/sf-ufo/dragon/dragon.md` | 1888 |
| 15 | `domains/sf-ufo/fantasy/fantasy.md` | 1892 |
| 16 | `domains/sf-ufo/hexa-grav/hexa-grav.md` | 2190 |
| 17 | `domains/sf-ufo/rtsc-12-products-evolution/rtsc-12-products-evolution.md` | 2257 |
| 18 | `domains/space/astrodynamics/astrodynamics.md` | 4 |
| 19 | `domains/space/space-medicine/space-medicine.md` | 4 |
| 20 | `domains/space/astrobiology/astrobiology.md` | 5 |

## 5. Parallelism Coordination Notes (allowlist race pattern, proven in Phase 2)

All 10 batch agents will attempt to edit the shared file `tool/own1_legacy_allowlist.json`. The following mitigation pattern, proven in Phase 2, is MANDATORY:

1. **Read-modify-write with mtime check**: capture `os.stat(path).st_mtime_ns` before read; re-check after edit is staged but before commit. If mtime changed, re-pull and re-apply removal set.
2. **Removal set, not index-based edits**: each agent computes the set of paths to remove (their 20 batch files). Re-apply idempotently (`[e for e in allowlist if e not in removal_set]`). Never use positional indices.
3. **`_meta.count` resync**: after editing `allowlist`, set `_meta.count = len(allowlist)` unconditionally.
4. **Rebase-retry loop on push**: `git pull --rebase origin main`, max 3 retries. On rebase conflict in the allowlist JSON, resolve by accepting theirs + re-applying our removal set (our entries are a disjoint subset).
5. **Stash/pop on dirty tree**: if rebase complains about uncommitted changes (e.g., pre-commit hook left artifacts), `git stash push -u`, rebase, `git stash pop`.
6. **Pre-commit hook race**: `--no-verify` is permitted after the agent has locally run `python3 tool/own_doc_lint.py --rule 1` and confirmed pass. This is explicitly authorized.
7. **Staging hygiene**: `git add` only the translated `.md` files + `tool/own1_legacy_allowlist.json`. Never `git add -A` or `git add .`.

## 6. Per-Batch Launch Prompt Templates

Each block below is a paste-ready prompt for a single agent. Do not edit; copy-paste verbatim into a fresh agent session. Replace the `$BATCH_N` files list only if you want to re-split batches.

### Prompt for Batch 1: `phase-3-1-infra-a`

```
You are a Phase 3 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-3-1-infra-a
Batch number: 1 of 10

## Files to translate (20 files, CJK total = 23857)

- domains/infra/forensic-science/forensic-science.md (CJK=3)
- domains/infra/robotics/robotics.md (CJK=1231)
- domains/infra/transportation/transportation.md (CJK=1233)
- domains/infra/fun-car/fun-car.md (CJK=1240)
- domains/infra/marketing/marketing.md (CJK=1252)
- domains/infra/motorcycle/motorcycle.md (CJK=1252)
- domains/infra/robotics-transport/robotics-transport.md (CJK=1253)
- domains/infra/surveying/surveying.md (CJK=1254)
- domains/infra/environment-thermal/environment-thermal.md (CJK=1255)
- domains/infra/safety/safety.md (CJK=1255)
- domains/infra/geology/geology.md (CJK=1258)
- domains/infra/mining/mining.md (CJK=1258)
- domains/infra/hexa-weather/hexa-weather.md (CJK=1259)
- domains/infra/aviation/aviation.md (CJK=1261)
- domains/infra/oceanography/oceanography.md (CJK=1261)
- domains/infra/autonomous-driving/autonomous-driving.md (CJK=1265)
- domains/infra/manufacturing-quality/manufacturing-quality.md (CJK=1266)
- domains/infra/carbon-capture/carbon-capture.md (CJK=1267)
- domains/infra/economics-finance/economics-finance.md (CJK=1267)
- domains/infra/law-justice/law-justice.md (CJK=1267)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all 20 files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the 20 paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the 20 translated `.md` files and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-3-1 phase-3-1-infra-a (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-3-1` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 1015 minus shrinkage from concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 2: `phase-3-2-infra-b`

```
You are a Phase 3 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-3-2-infra-b
Batch number: 2 of 10

## Files to translate (20 files, CJK total = 25455)

- domains/infra/seabed-grid/seabed-grid.md (CJK=1267)
- domains/infra/economics/economics.md (CJK=1268)
- domains/infra/electric-vehicle/electric-vehicle.md (CJK=1268)
- domains/infra/ocean/ocean.md (CJK=1268)
- domains/infra/water-treatment/water-treatment.md (CJK=1268)
- domains/infra/naval-architecture/naval-architecture.md (CJK=1269)
- domains/infra/desal/desal.md (CJK=1270)
- domains/infra/meteorology/meteorology.md (CJK=1270)
- domains/infra/cartography-gis/cartography-gis.md (CJK=1271)
- domains/infra/desalination/desalination.md (CJK=1271)
- domains/infra/hexa-exo/hexa-exo.md (CJK=1272)
- domains/infra/hexa-skyway/hexa-skyway.md (CJK=1273)
- domains/infra/jurisprudence/jurisprudence.md (CJK=1273)
- domains/infra/tsunami-shield/tsunami-shield.md (CJK=1274)
- domains/infra/skyway/skyway.md (CJK=1276)
- domains/infra/hexa-defense/hexa-defense.md (CJK=1277)
- domains/infra/hexa-tsunami/hexa-tsunami.md (CJK=1278)
- domains/infra/printing/printing.md (CJK=1280)
- domains/infra/earthquake-engineering/earthquake-engineering.md (CJK=1281)
- domains/infra/fire-science/fire-science.md (CJK=1281)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all 20 files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the 20 paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the 20 translated `.md` files and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-3-2 phase-3-2-infra-b (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-3-2` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 1015 minus shrinkage from concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 3: `phase-3-3-infra-c-life-tail`

```
You are a Phase 3 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-3-3-infra-c-life-tail
Batch number: 3 of 10

## Files to translate (20 files, CJK total = 24355)

- domains/infra/environmental-protection/environmental-protection.md (CJK=1283)
- domains/infra/airbag/airbag.md (CJK=1285)
- domains/infra/climate/climate.md (CJK=1285)
- domains/infra/earth-defense/earth-defense.md (CJK=1290)
- domains/infra/smart-city/smart-city.md (CJK=1290)
- domains/infra/weather-control/weather-control.md (CJK=1290)
- domains/infra/ecommerce-fintech/ecommerce-fintech.md (CJK=1291)
- domains/infra/governance-safety-urban/governance-safety-urban.md (CJK=1291)
- domains/infra/underground-tunnel/underground-tunnel.md (CJK=1291)
- domains/infra/civil-engineering/civil-engineering.md (CJK=1293)
- domains/infra/ultimate-safety/ultimate-safety.md (CJK=1296)
- domains/infra/insurance/insurance.md (CJK=1299)
- domains/infra/calendar-time-geography/calendar-time-geography.md (CJK=1300)
- domains/infra/monetary-history/monetary-history.md (CJK=1300)
- domains/infra/architecture/architecture.md (CJK=1309)
- domains/infra/currency-economics/currency-economics.md (CJK=1318)
- domains/infra/control-automation/control-automation.md (CJK=1425)
- domains/infra/construction-structural/construction-structural.md (CJK=2212)
- domains/life/nuclear-medicine/nuclear-medicine.md (CJK=3)
- domains/life/music-therapy/music-therapy.md (CJK=4)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all 20 files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the 20 paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the 20 translated `.md` files and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-3-3 phase-3-3-infra-c-life-tail (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-3-3` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 1015 minus shrinkage from concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 4: `phase-3-4-life-a`

```
You are a Phase 3 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-3-4-life-a
Batch number: 4 of 10

## Files to translate (20 files, CJK total = 32580)

- domains/life/sleep-medicine/sleep-medicine.md (CJK=4)
- domains/life/urban-farming/urban-farming.md (CJK=4)
- domains/life/gastrointestinal-medicine/gastrointestinal-medicine.md (CJK=5)
- domains/life/radiation-biology/radiation-biology.md (CJK=6)
- domains/life/tibetan-medicine/tibetan-medicine.md (CJK=6)
- domains/life/dog-robot-test/dog-robot-test.md (CJK=1177)
- domains/life/hexa-limb/hexa-limb.md (CJK=2218)
- domains/life/hiv-treatment/hiv-treatment.md (CJK=2224)
- domains/life/hiv/hiv.md (CJK=2227)
- domains/life/viticulture/viticulture.md (CJK=2230)
- domains/life/neuro/neuro.md (CJK=2235)
- domains/life/agriculture/agriculture.md (CJK=2236)
- domains/life/synbio/synbio.md (CJK=2238)
- domains/life/aquaculture/aquaculture.md (CJK=2240)
- domains/life/tattoo-removal/tattoo-removal.md (CJK=2246)
- domains/life/womens-intimate-cleanser/womens-intimate-cleanser.md (CJK=2249)
- domains/life/neuropharmacology/neuropharmacology.md (CJK=2253)
- domains/life/virology/virology.md (CJK=2260)
- domains/life/cancer-therapy/cancer-therapy.md (CJK=2261)
- domains/life/perfumery/perfumery.md (CJK=2261)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all 20 files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the 20 paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the 20 translated `.md` files and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-3-4 phase-3-4-life-a (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-3-4` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 1015 minus shrinkage from concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 5: `phase-3-5-life-b-culture-a`

```
You are a Phase 3 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-3-5-life-b-culture-a
Batch number: 5 of 10

## Files to translate (20 files, CJK total = 33745)

- domains/life/mycology/mycology.md (CJK=2263)
- domains/life/pharmacology/pharmacology.md (CJK=2270)
- domains/life/hair-regeneration/hair-regeneration.md (CJK=2272)
- domains/life/medical-device/medical-device.md (CJK=2272)
- domains/life/entomology/entomology.md (CJK=2273)
- domains/life/coffee-science/coffee-science.md (CJK=2275)
- domains/life/ecology-agriculture-food/ecology-agriculture-food.md (CJK=2275)
- domains/life/wine-enology/wine-enology.md (CJK=2277)
- domains/culture/ethnomusicology/ethnomusicology.md (CJK=5)
- domains/culture/ar-vr-xr/ar-vr-xr.md (CJK=1370)
- domains/culture/music/music.md (CJK=1409)
- domains/culture/baduk/baduk.md (CJK=1413)
- domains/culture/mountaineering/mountaineering.md (CJK=1416)
- domains/culture/yoga/yoga.md (CJK=1416)
- domains/culture/dance-choreography/dance-choreography.md (CJK=1420)
- domains/culture/audio/audio.md (CJK=1423)
- domains/culture/numismatics/numismatics.md (CJK=1423)
- domains/culture/horology/horology.md (CJK=1424)
- domains/culture/photography/photography.md (CJK=1424)
- domains/culture/taekwondo/taekwondo.md (CJK=1425)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all 20 files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the 20 paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the 20 translated `.md` files and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-3-5 phase-3-5-life-b-culture-a (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-3-5` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 1015 minus shrinkage from concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 6: `phase-3-6-culture-b-physics-top`

```
You are a Phase 3 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-3-6-culture-b-physics-top
Batch number: 6 of 10

## Files to translate (20 files, CJK total = 21551)

- domains/culture/linguistics/linguistics.md (CJK=1427)
- domains/culture/religion/religion.md (CJK=1430)
- domains/culture/archaeology/archaeology.md (CJK=1434)
- domains/culture/writing-systems/writing-systems.md (CJK=1437)
- domains/culture/biometrics/biometrics.md (CJK=1438)
- domains/culture/music-mathematics/music-mathematics.md (CJK=1438)
- domains/culture/hangul-script/hangul-script.md (CJK=1439)
- domains/culture/library-science/library-science.md (CJK=1439)
- domains/culture/social-architecture/social-architecture.md (CJK=1440)
- domains/culture/dice-probability/dice-probability.md (CJK=1450)
- domains/culture/telecom-linguistics/telecom-linguistics.md (CJK=1451)
- domains/culture/games-sports/games-sports.md (CJK=1456)
- domains/culture/bell-clockwork/bell-clockwork.md (CJK=1457)
- domains/culture/religion-mythology/religion-mythology.md (CJK=1458)
- domains/physics/computational-fluid-dynamics/computational-fluid-dynamics.md (CJK=6)
- domains/physics/m-theory-11d/m-theory-11d.md (CJK=215)
- domains/physics/wormhole/wormhole.md (CJK=250)
- domains/physics/tabletop-blackhole/tabletop-blackhole.md (CJK=276)
- domains/physics/calabi-yau-nav/calabi-yau-nav.md (CJK=296)
- domains/physics/warp-drive/warp-drive.md (CJK=314)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all 20 files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the 20 paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the 20 translated `.md` files and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-3-6 phase-3-6-culture-b-physics-top (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-3-6` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 1015 minus shrinkage from concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 7: `phase-3-7-physics-tail-compute-a`

```
You are a Phase 3 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-3-7-physics-tail-compute-a
Batch number: 7 of 10

## Files to translate (20 files, CJK total = 8322)

- domains/physics/multiverse-nav/multiverse-nav.md (CJK=337)
- domains/physics/pet-cyclotron/pet-cyclotron.md (CJK=815)
- domains/physics/particle-accelerator/particle-accelerator.md (CJK=967)
- domains/physics/tabletop-antimatter/tabletop-antimatter.md (CJK=1094)
- domains/physics/meta-closure-nav/meta-closure-nav.md (CJK=1943)
- domains/compute/network-protocol/certificates/wifi6-cert/wifi6-cert.md (CJK=177)
- domains/compute/network-protocol/certificates/ethernet-cert/ethernet-cert.md (CJK=184)
- domains/compute/network-protocol/certificates/pcie-cert/pcie-cert.md (CJK=185)
- domains/compute/network-protocol/certificates/usb-cert/usb-cert.md (CJK=185)
- domains/compute/network-protocol/certificates/starlink-cert/starlink-cert.md (CJK=192)
- domains/compute/network-protocol/certificates/5g-nr-cert/5g-nr-cert.md (CJK=197)
- domains/compute/network-protocol/certificates/6g-cert/6g-cert.md (CJK=197)
- domains/compute/network-protocol/certificates/bt6-0-cert/bt6-0-cert.md (CJK=200)
- domains/compute/network-protocol/certificates/lorawan-cert/lorawan-cert.md (CJK=201)
- domains/compute/network-protocol/certificates/displayport-cert/displayport-cert.md (CJK=205)
- domains/compute/network-protocol/certificates/hdmi-cert/hdmi-cert.md (CJK=207)
- domains/compute/network-protocol/certificates/nvme-cert/nvme-cert.md (CJK=226)
- domains/compute/network-protocol/displayport/displayport.md (CJK=262)
- domains/compute/network-protocol/hdmi/hdmi.md (CJK=273)
- domains/compute/network-protocol/usb/usb.md (CJK=275)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all 20 files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the 20 paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the 20 translated `.md` files and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-3-7 phase-3-7-physics-tail-compute-a (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-3-7` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 1015 minus shrinkage from concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 8: `phase-3-8-compute-b`

```
You are a Phase 3 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-3-8-compute-b
Batch number: 8 of 10

## Files to translate (20 files, CJK total = 26684)

- domains/compute/network-protocol/ethernet/ethernet.md (CJK=292)
- domains/compute/network-protocol/pcie/pcie.md (CJK=310)
- domains/compute/network-protocol/nvme/nvme.md (CJK=371)
- domains/compute/hexa-macos/vt-6tier-terminal/vt-6tier-terminal.md (CJK=555)
- domains/compute/chip-architecture/l7-quantum-hybrid-transmon/l7-quantum-hybrid-transmon.md (CJK=778)
- domains/compute/chip-architecture/l8-topo-anyon-majorana/l8-topo-anyon-majorana.md (CJK=831)
- domains/compute/chip-architecture/l9-field-photon-neuro/l9-field-photon-neuro.md (CJK=900)
- domains/compute/chip-architecture/protocol-bridge-20-rtl/protocol-bridge-20-rtl.md (CJK=1143)
- domains/compute/chip-interconnect/chip-interconnect.md (CJK=1420)
- domains/compute/chip-architecture/l11-quantum-dot-6qubit-qec/l11-quantum-dot-6qubit-qec.md (CJK=1427)
- domains/compute/chip-architecture/l15-meta-integration-closure/l15-meta-integration-closure.md (CJK=1433)
- domains/compute/chip-yield/chip-yield.md (CJK=1640)
- domains/compute/chip-packaging/chip-packaging.md (CJK=1728)
- domains/compute/chip-thermal-power/chip-thermal-power.md (CJK=1763)
- domains/compute/chip-architecture/mk3-roadmap-l1-l15-audit/mk3-roadmap-l1-l15-audit.md (CJK=1905)
- domains/compute/chip-verify-test/chip-verify-test.md (CJK=1933)
- domains/compute/chip-architecture/hexa-consciousness/hexa-consciousness.md (CJK=1938)
- domains/compute/chip-process/chip-process.md (CJK=2034)
- domains/compute/chip-architecture/l12-nuclear-isomer-storage/l12-nuclear-isomer-storage.md (CJK=2064)
- domains/compute/chip-architecture/monster-leech-mapping/monster-leech-mapping.md (CJK=2219)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all 20 files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the 20 paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the 20 translated `.md` files and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-3-8 phase-3-8-compute-b (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-3-8` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 1015 minus shrinkage from concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 9: `phase-3-9-materials-cognitive-a`

```
You are a Phase 3 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-3-9-materials-cognitive-a
Batch number: 9 of 10

## Files to translate (20 files, CJK total = 25849)

- domains/materials/hexa-glass/hexa-glass.md (CJK=1409)
- domains/materials/paper/paper.md (CJK=1412)
- domains/materials/hexa-fabric/hexa-fabric.md (CJK=1415)
- domains/materials/pet-film/pet-film.md (CJK=1422)
- domains/materials/gemology/gemology.md (CJK=1428)
- domains/materials/epoxy/epoxy.md (CJK=1430)
- domains/materials/recycling/recycling.md (CJK=1432)
- domains/materials/swordsmithing/swordsmithing.md (CJK=1433)
- domains/materials/hexa-recycle/hexa-recycle.md (CJK=1437)
- domains/materials/nylon/nylon.md (CJK=1444)
- domains/materials/fashion-textile/fashion-textile.md (CJK=1447)
- domains/materials/textile-dyeing/textile-dyeing.md (CJK=1449)
- domains/materials/aramid/aramid.md (CJK=1451)
- domains/materials/concrete/concrete.md (CJK=1453)
- domains/materials/tire-cord/tire-cord.md (CJK=1460)
- domains/materials/lutherie/lutherie.md (CJK=1467)
- domains/materials/concrete-technology/concrete-technology.md (CJK=1469)
- domains/cognitive/hexa-speak/proto/README.md (CJK=186)
- domains/cognitive/hexa-speak/proto/rtl/README.md (CJK=588)
- domains/cognitive/hexa-speak/proto/n6-speak-v2-spec.md (CJK=617)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all 20 files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the 20 paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the 20 translated `.md` files and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-3-9 phase-3-9-materials-cognitive-a (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-3-9` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 1015 minus shrinkage from concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

### Prompt for Batch 10: `phase-3-10-cognitive-tail-energy-sf-space`

```
You are a Phase 3 translation agent for the n6-architecture own#1 HARD English-only campaign.

Repo: /Users/ghost/core/n6-architecture
Branch: main (rebase against origin/main as needed)
Batch label: phase-3-10-cognitive-tail-energy-sf-space
Batch number: 10 of 10

## Files to translate (20 files, CJK total = 28217)

- domains/cognitive/hexa-speak/proto/rtl/soc_drc_lvs_report.md (CJK=682)
- domains/cognitive/hexa-speak/rtl/README.md (CJK=720)
- domains/cognitive/hexa-speak/proto/rtl/gdsii_signoff.md (CJK=827)
- domains/cognitive/brain-computer-interface/bci-6ch-n6-mapping/bci-6ch-n6-mapping.md (CJK=847)
- domains/cognitive/ai-multimodal/ai-multimodal.md (CJK=2058)
- domains/energy/tabletop-fusion/tabletop-fusion.md (CJK=1723)
- domains/energy/pemfc/pemfc.md (CJK=1849)
- domains/energy/energy-efficiency/energy-efficiency.md (CJK=1870)
- domains/energy/hvac-system/hvac-system.md (CJK=1875)
- domains/energy/battery-energy/battery-energy.md (CJK=1881)
- domains/energy/datacenter-reactor/datacenter-reactor.md (CJK=1895)
- domains/sf-ufo/vampire/vampire.md (CJK=1871)
- domains/sf-ufo/snowflake-ice/snowflake-ice.md (CJK=1879)
- domains/sf-ufo/dragon/dragon.md (CJK=1888)
- domains/sf-ufo/fantasy/fantasy.md (CJK=1892)
- domains/sf-ufo/hexa-grav/hexa-grav.md (CJK=2190)
- domains/sf-ufo/rtsc-12-products-evolution/rtsc-12-products-evolution.md (CJK=2257)
- domains/space/astrodynamics/astrodynamics.md (CJK=4)
- domains/space/space-medicine/space-medicine.md (CJK=4)
- domains/space/astrobiology/astrobiology.md (CJK=5)

## Task

1. For each file, translate all Korean/CJK text to English in-place, preserving:
   - All markdown structure (headers, lists, tables, blockquotes, code fences)
   - All math blocks ($...$, $$...$$) verbatim
   - All code blocks verbatim
   - All frontmatter keys verbatim
   - All hyperlinks and image paths verbatim
   - Technical terms as-is: atlas, ouroboros, sigma, phi, J2, @R/@P/@C/@L, BT-*, M10*, HEXA-*, N6-*, own#N
2. own#11 compliance: describe all results as "draft/candidate/pattern/target". Do NOT write "solved", "proven", "complete", "finished", "confirmed" in a claim-asserting sense. If the source document used such claim words, soften to "draft candidate / pattern target".
3. After all 20 files are translated, edit `tool/own1_legacy_allowlist.json`:
   - Remove exactly the 20 paths in this batch from the `allowlist` array
   - Set `_meta.count = len(allowlist)`
   - Keep JSON formatting style (2-space indent, trailing newline)
4. Allowlist race mitigation (MANDATORY):
   - Read mtime before edit; re-read after edit if mtime changed
   - Use set-based removal (disjoint subset); never positional
   - On push conflict: `git pull --rebase origin main`, max 3 retries
   - On rebase conflict in allowlist JSON: accept theirs, re-apply removal set
   - On dirty tree during rebase: `git stash push -u`, rebase, `git stash pop`
5. Local validation before commit:
   - Run `python3 tool/own_doc_lint.py --rule 1`
   - If non-zero exit, ABORT (do not commit). Fix remaining CJK or re-run translation on the failing file.
6. Staging:
   - `git add` only the 20 translated `.md` files and `tool/own1_legacy_allowlist.json`
   - Never use `git add -A` or `git add .`
7. Commit (two commits, not one):
   - Commit A: `docs(translate): phase-3-10 phase-3-10-cognitive-tail-energy-sf-space (20 files)` — staged .md files only
   - Commit B: `feat(own): shrink own#1 allowlist phase-3-10` — staged allowlist JSON only
   - If pre-commit hook race triggers on sibling files (other batches running), `--no-verify` is permitted ONLY after you have locally verified `python3 tool/own_doc_lint.py --rule 1` passes.
8. Push:
   - `git push origin main`
   - On rejection, `git pull --rebase origin main` then retry (max 3 total attempts)

## Report back

- Commit SHAs for Commit A and Commit B
- Final allowlist count (should be 1015 minus shrinkage from concurrent batches)
- Any files that failed translation and were deferred
- own_doc_lint.py --rule 1 exit code at commit time
```

## 7. Estimated Numbers

- Total files to translate: **200**
- Total CJK characters: **250615**
- Current allowlist count: **1015**
- Post-Phase-3 target allowlist count: **815** (1015 - 200)
- Per-batch avg: 20 files, ~25,062 CJK
- Expected origin/main commit churn: 20 commits (2 per batch x 10 batches)
- Per-file translation effort estimate: 5-10 min human review, 2-3 min automated; total ~16-33 agent-hours if fully parallel

## 8. Verification Checklist (post-all-batches)

- [ ] `python3 tool/own_doc_lint.py --rule 1` passes (exit 0)
- [ ] `python3 -c "import json; d=json.load(open('tool/own1_legacy_allowlist.json')); assert len(d['allowlist']) == d['_meta']['count'] == 815"`
- [ ] `git log --oneline origin/main | head -30` shows 20 new commits (2 per batch)
- [ ] CI own1-doc-english-hard job green
- [ ] No `.md` files in the 200-file set contain CJK bytes (`python3 -c "import re,sys; ..."` spot check)

---

*End of plan. No source .md files were modified during plan generation. The plan file itself is CJK-free.*
