# DIS-P2-1 Domain Expansion — Human Review Packet

**Source:** `reports/p2_domain_expansion_proposal.json` (63 candidates)
**Triage:** `reports/p2_domain_review_recommendations.json`
**ROI ref:** n6-roi-010
**Generated:** 2026-04-23

## Status

| | count |
|---|---|
| Total proposed | 63 |
| Already on disk | 13 (batch1 top-5 + batch2 ×8) |
| **Still pending** | **50** |

Current disk: 391 domains (target post-approval: 441 if all 50 added).

## Decision buckets (50 pending)

### Tier A — fast-track (4)
Low risk + alien≥7 + non-template. Strong structural n=6 mechanism.
- `DC-034 sports-psychology` — Csikszentmihalyi's 6 flow conditions (cognitive)
- `DC-042 wine-chemistry` — C6H12O6 glycolysis (life)
- `DC-047 digital-humanities` — TEI 6-element minimum + Six Degrees of F. Bacon (culture)
- `DC-057 biophotonics` — 6 endogenous fluorophores, COX 6-metal structure (life)

**Recommendation:** approve as batch.

### Tier B — normal approve (25)
Low risk + alien<7 + non-template. Distribution:
- infra 9 · materials 4 · cognitive 3 · compute 3 · life 3 · culture 1 · energy 1 · physics 1

**Recommendation:** approve as batch unless sector cap concern.

### Tier C — human-must-decide (21)
Med risk or template-only flagged. Distribution:
- life 7 · infra 5 · cognitive 3 · culture 2 · materials 2 · energy 1 · space 1

**Recommendation:** walk per-item. Template-flagged ids: DC-014, DC-024, DC-037. The other 18 are med-risk for domain-specific reasons (e.g., contested species count, loose "6 weave types", OSHA hierarchy is 5 not 6).

## New sector candidates (3)

All 3 P2-1 proposals recommend **ABSORB** (no new axis):
| name | action | est. domains | plan |
|---|---|---|---|
| defense | ABSORB_INTO_infra | 18 | add ~6 defense-tech domains to infra |
| ocean_engineering | ABSORB_INTO_infra | 14 | ocean sub-cluster in infra |
| agriculture_climate_adaptation | ABSORB_INTO_life | 12 | agri-climate sub-cluster in life |

**Recommendation:** accept ABSORB verdicts. Rationale: creating new sectors would orphan subgraphs and split civilian/military or traditional/climate-adapted variants of the same technology.

## Sector boundary review (MEDIUM priority)

These don't block P2-1 but should be planned in P3:
- **compute (68 domains)** — overcrowded; navigation suffers. Needs sub-clusters.
- **infra (57 domains)** — hard to navigate without sub-clusters.
- **life (48 domains)** — pre-emptive sub-clustering before 65+.

LOW/cosmetic adjustments for cognitive, culture, energy, materials, physics, sf-ufo, space — defer.

## Apply instructions

Once decisions are made, register batch with:
```
# Tier A (4)
bash bin/n6_register --tier A --from reports/p2_domain_review_recommendations.json

# Tier B (25)
bash bin/n6_register --tier B --from reports/p2_domain_review_recommendations.json

# Tier C (per id)
bash bin/n6_register --ids DC-005,DC-007,... --from reports/p2_domain_review_recommendations.json
```
(Register tool invocation — same path as earlier batches which flipped the 13 from pending → on-disk.)

