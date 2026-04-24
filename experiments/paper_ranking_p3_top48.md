# P3 Paper Ranking Report — Top 48 Candidate Selection

| Field | Value |
|---|---|
| Roadmap | PAPER-P3-1 |
| Created | 2026-04-14 |
| Input pool | 125 candidate drafts registered in `papers/_registry.json` |
| Selected count | Top 48 drafts (P3 gate_exit requirement) |
| Result JSON | `papers/_submission_top48.json` |
| Submission template | `papers/_submission_top48_template.md` |

## 1. Score formula

```
score = alien_index * 0.4 + (closure_grade_pct / 10) * 0.3 + (citation_depth / 3) * 0.3
```

- `alien_index` (0~10): section-level alien index. Map `_registry.json` sections[].alien_index to the draft's domain. If unmapped, default to 7.
- `closure_grade_pct` (0~100): use the EXACT ratio from `_papers.json` exact_stat when available. Otherwise estimate as 70/72/78/82 based on chunk_status.
- `citation_depth` (0~30): number of BT IDs in bt_ref * 2 + body line count / 50. Clamped at 30.
- Each component is normalized to the same scale (0~10) and then weighted-summed. Theoretical maximum 10.0, observed maximum about 9.57.

## 2. Simulated DOI scheme — not a real DOI

```
10.NEXUS6.n6-arch/<YYYY>-<NNN>
  YYYY = 2026 fixed
  NNN  = 001~048 (ranking order)
```

- `10.NEXUS6` is a prefix not registered with CrossRef/DataCite. For internal reference only.
- Replace this number upon actual journal/conference submission.
- This report is used only as a reference for organizing the submission format.

## 3. Target journal/conference mapping rules

| Journal/Conference | Assignment rule | Number selected |
|---|---|---|
| Nature Communications | Natural science/biology/earth/culture/industry general (default for unmapped domains) | 24 |
| Physical Review Letters | Gravity/particles/superconductors/quantum computing/topology/pure math/fluid dynamics/electromagnetism | 6 |
| IEEE TVLSI | Chip architecture/DRAM/V-NAND/packaging/neuromorphic/consciousness chip | 6 |
| NeurIPS | AI techniques 68/17/SSM/network collective intelligence/autonomous driving/AI ethics-governance/neuroscience | 5 |
| ICML | Self-organization/homeostasis/evolutionary ouroboros/blow-up/lens-forge/cycle engine/AGI/attractor | 2 |
| JAIR | Millennium DFS/jurisprudence/atlas promotion protocol/hypothesis MC verification/economics/governance | 5 |

## 4. Top 48 ranking (candidate drafts)

| Rank | Paper ID | File | Domain | Score | alien | closure% | cit-depth | Simulated DOI | Target |
|---:|---|---|---|---:|---:|---:|---:|---|---|
| 1 | N6-032 | `n6-dance-choreography-paper.md` | dance-choreography | 9.57 | 10 | 100.0 | 25.7 | `10.NEXUS6.n6-arch/2026-001` | Nature Communications |
| 2 | N6-108 | `n6-writing-systems-paper.md` | writing-systems | 9.57 | 10 | 100.0 | 25.7 | `10.NEXUS6.n6-arch/2026-002` | Nature Communications |
| 3 | N6-106 | `n6-wine-enology-paper.md` | wine-enology | 9.42 | 10 | 95.2 | 25.7 | `10.NEXUS6.n6-arch/2026-003` | Nature Communications |
| 4 | N6-016 | `n6-carbon-capture-paper.md` | carbon-capture | 9.37 | 10 | 100.0 | 23.7 | `10.NEXUS6.n6-arch/2026-004` | Nature Communications |
| 5 | N6-051 | `n6-gravity-wave-paper.md` | gravity-wave | 9.03 | 10 | 82.0 | 25.7 | `10.NEXUS6.n6-arch/2026-005` | Physical Review Letters |
| 6 | N6-009 | `n6-aquaculture-paper.md` | aquaculture | 8.57 | 10 | 80.0 | 21.7 | `10.NEXUS6.n6-arch/2026-006` | Nature Communications |
| 7 | N6-025 | `n6-consciousness-chip-paper.md` | consciousness-chip | 8.43 | 10 | 82.0 | 19.7 | `10.NEXUS6.n6-arch/2026-007` | IEEE TVLSI |
| 8 | N6-030 | `n6-cryptography-paper.md` | cryptography | 8.37 | 10 | 80.0 | 19.7 | `10.NEXUS6.n6-arch/2026-008` | Nature Communications |
| 9 | N6-068 | `n6-horology-paper.md` | horology | 8.36 | 10 | 86.4 | 17.7 | `10.NEXUS6.n6-arch/2026-009` | Nature Communications |
| 10 | N6-007 | `n6-ai-techniques-68-integrated-paper.md` | ai-techniques-68-integrated | 8.26 | 7 | 82.0 | 30.0 | `10.NEXUS6.n6-arch/2026-010` | NeurIPS |
| 11 | N6-074 | `n6-millennium-dfs-1-12-integrated-paper.md` | millennium-dfs-1-12-integrated | 8.26 | 7 | 82.0 | 30.0 | `10.NEXUS6.n6-arch/2026-011` | JAIR |
| 12 | N6-080 | `n6-particle-cosmology-paper.md` | particle-cosmology | 8.26 | 7 | 82.0 | 30.0 | `10.NEXUS6.n6-arch/2026-012` | Physical Review Letters |
| 13 | N6-020 | `n6-chip-6stages-integrated-paper.md` | chip-6stages-integrated | 8.23 | 7 | 82.0 | 29.7 | `10.NEXUS6.n6-arch/2026-013` | IEEE TVLSI |
| 14 | N6-093 | `n6-superconductor-paper.md` | superconductor | 8.23 | 10 | 82.0 | 17.7 | `10.NEXUS6.n6-arch/2026-014` | Physical Review Letters |
| 15 | N6-027 | `n6-construction-structural-paper.md` | construction-structural | 8.21 | 7 | 88.0 | 27.7 | `10.NEXUS6.n6-arch/2026-015` | Nature Communications |
| 16 | N6-070 | `n6-jurisprudence-paper.md` | jurisprudence | 8.13 | 10 | 85.4 | 15.7 | `10.NEXUS6.n6-arch/2026-016` | JAIR |
| 17 | N6-078 | `n6-oceanography-paper.md` | oceanography | 8.03 | 10 | 82.0 | 15.7 | `10.NEXUS6.n6-arch/2026-017` | Nature Communications |
| 18 | N6-072 | `n6-mechanical-engineering-paper.md` | mechanical-engineering | 7.99 | 7 | 87.5 | 25.7 | `10.NEXUS6.n6-arch/2026-018` | Nature Communications |
| 19 | N6-001 | `n6-acoustics-paper.md` | acoustics | 7.97 | 7 | 86.7 | 25.7 | `10.NEXUS6.n6-arch/2026-019` | Nature Communications |
| 20 | N6-089 | `n6-religion-mythology-paper.md` | religion-mythology | 7.97 | 10 | 66.7 | 19.7 | `10.NEXUS6.n6-arch/2026-020` | JAIR |
| 21 | N6-079 | `n6-optics-paper.md` | optics | 7.96 | 7 | 86.4 | 25.7 | `10.NEXUS6.n6-arch/2026-021` | Nature Communications |
| 22 | N6-076 | `n6-network-collective-paper.md` | network-collective | 7.83 | 10 | 82.0 | 13.7 | `10.NEXUS6.n6-arch/2026-022` | NeurIPS |
| 23 | N6-100 | `n6-topology-paper.md` | topology | 7.83 | 7 | 82.0 | 25.7 | `10.NEXUS6.n6-arch/2026-023` | Physical Review Letters |
| 24 | N6-069 | `n6-hydrology-paper.md` | hydrology | 7.78 | 7 | 87.2 | 23.7 | `10.NEXUS6.n6-arch/2026-024` | Nature Communications |
| 25 | N6-081 | `n6-performance-chip-paper.md` | performance-chip | 7.63 | 7 | 82.0 | 23.7 | `10.NEXUS6.n6-arch/2026-025` | IEEE TVLSI |
| 26 | N6-075 | `n6-music-theory-paper.md` | music-theory | 7.61 | 7 | 88.0 | 21.7 | `10.NEXUS6.n6-arch/2026-026` | Nature Communications |
| 27 | N6-004 | `n6-agi-architecture-paper.md` | agi-architecture | 7.50 | 10 | 70.0 | 14.0 | `10.NEXUS6.n6-arch/2026-027` | ICML |
| 28 | N6-002 | `n6-advanced-packaging-paper.md` | advanced-packaging | 7.47 | 10 | 70.0 | 13.7 | `10.NEXUS6.n6-arch/2026-028` | IEEE TVLSI |
| 29 | N6-003 | `n6-aerospace-transport-paper.md` | aerospace-transport | 7.47 | 10 | 70.0 | 13.7 | `10.NEXUS6.n6-arch/2026-029` | Nature Communications |
| 30 | N6-010 | `n6-archaeology-paper.md` | archaeology | 7.47 | 10 | 70.0 | 13.7 | `10.NEXUS6.n6-arch/2026-030` | Nature Communications |
| 31 | N6-012 | `n6-autonomous-driving-paper.md` | autonomous-driving | 7.47 | 10 | 70.0 | 13.7 | `10.NEXUS6.n6-arch/2026-031` | NeurIPS |
| 32 | N6-013 | `n6-battery-energy-storage-paper.md` | battery-energy-storage | 7.47 | 7 | 83.3 | 21.7 | `10.NEXUS6.n6-arch/2026-032` | Nature Communications |
| 33 | N6-034 | `n6-dolphin-bioacoustics-paper.md` | dolphin-bioacoustics | 7.47 | 10 | 70.0 | 13.7 | `10.NEXUS6.n6-arch/2026-033` | Nature Communications |
| 34 | N6-036 | `n6-ecology-agriculture-food-paper.md` | ecology-agriculture-food | 7.47 | 10 | 70.0 | 13.7 | `10.NEXUS6.n6-arch/2026-034` | Nature Communications |
| 35 | N6-038 | `n6-economics-finance-paper.md` | economics-finance | 7.47 | 10 | 70.0 | 13.7 | `10.NEXUS6.n6-arch/2026-035` | JAIR |
| 36 | N6-043 | `n6-fermentation-paper.md` | fermentation | 7.47 | 10 | 70.0 | 13.7 | `10.NEXUS6.n6-arch/2026-036` | Nature Communications |
| 37 | N6-050 | `n6-governance-safety-urban-paper.md` | governance-safety-urban | 7.47 | 10 | 70.0 | 13.7 | `10.NEXUS6.n6-arch/2026-037` | JAIR |
| 38 | N6-059 | `n6-hexa-neuro-paper.md` | hexa-neuro | 7.47 | 10 | 70.0 | 13.7 | `10.NEXUS6.n6-arch/2026-038` | NeurIPS |
| 39 | N6-065 | `n6-hexa-telepathy-paper.md` | hexa-telepathy | 7.47 | 10 | 70.0 | 13.7 | `10.NEXUS6.n6-arch/2026-039` | ICML |
| 40 | N6-071 | `n6-manufacturing-quality-paper.md` | manufacturing-quality | 7.47 | 10 | 70.0 | 13.7 | `10.NEXUS6.n6-arch/2026-040` | Nature Communications |
| 41 | N6-077 | `n6-neuromorphic-computing-paper.md` | neuromorphic-computing | 7.47 | 10 | 70.0 | 13.7 | `10.NEXUS6.n6-arch/2026-041` | IEEE TVLSI |
| 42 | N6-084 | `n6-pure-mathematics-paper.md` | pure-mathematics | 7.47 | 10 | 70.0 | 13.7 | `10.NEXUS6.n6-arch/2026-042` | Physical Review Letters |
| 43 | N6-085 | `n6-quantum-computing-paper.md` | quantum-computing | 7.47 | 10 | 70.0 | 13.7 | `10.NEXUS6.n6-arch/2026-043` | Physical Review Letters |
| 44 | N6-095 | `n6-synthetic-biology-paper.md` | synthetic-biology | 7.47 | 10 | 70.0 | 13.7 | `10.NEXUS6.n6-arch/2026-044` | Nature Communications |
| 45 | N6-096 | `n6-telecom-linguistics-paper.md` | telecom-linguistics | 7.47 | 10 | 70.0 | 13.7 | `10.NEXUS6.n6-arch/2026-045` | NeurIPS |
| 46 | N6-098 | `n6-therapeutic-nanobot-paper.md` | therapeutic-nanobot | 7.47 | 10 | 70.0 | 13.7 | `10.NEXUS6.n6-arch/2026-046` | Nature Communications |
| 47 | N6-102 | `n6-virology-structure-paper.md` | virology-structure | 7.47 | 10 | 70.0 | 13.7 | `10.NEXUS6.n6-arch/2026-047` | Nature Communications |
| 48 | N6-021 | `n6-chip-design-ladder-paper.md` | chip-design-ladder | 7.43 | 7 | 82.0 | 21.7 | `10.NEXUS6.n6-arch/2026-048` | IEEE TVLSI |

## 5. ASCII comparison chart — top 15 candidate score bars

```
 1 N6-032 ######################################## 9.57
 2 N6-108 ######################################## 9.57
 3 N6-106 #######################################  9.42
 4 N6-016 #######################################  9.37
 5 N6-051 #####################################    9.03
 6 N6-009 ###################################      8.57
 7 N6-025 ###################################      8.43
 8 N6-030 ##################################       8.37
 9 N6-068 ##################################       8.36
10 N6-007 ##################################       8.26
11 N6-074 ##################################       8.26
12 N6-080 ##################################       8.26
13 N6-020 ##################################       8.23
14 N6-093 ##################################       8.23
15 N6-027 ##################################       8.21
```

## 6. Limitations and rebuttal candidates

- **closure_grade estimation accuracy**: only 25 of 125 candidate drafts have measured exact_stat. The other 100 use a discrete estimate based on chunk_status text. Re-ranking needed after a measurement audit.
- **citation_depth bias**: since bt_ref collection is based on chunk metadata, drafts without registered chunks get bt_count=0 and only partial line-count scoring applies. An audit parsing each draft file body is needed.
- **alien_index unmapped**: 118/125 domains are mapped in sections. 7 fall back to the default of 7 — at risk of being pushed to the bottom of the ranking.
- **Simulated DOI**: not actually registered with CrossRef/DataCite. Not resolvable by external citation/search engines.
- **Rebuttal condition**: if this ranking omits, in P3 evaluation, candidate drafts with alien_index 10 outside the top 48, a re-ranking trigger fires.

## 7. Reproduction procedure

```
python3 scripts/rank_papers_p3.py   # (script that generated this report — executed inline)
  Input:  papers/_papers.json, papers/_registry.json
  Output: papers/_submission_top48.json, experiments/paper_ranking_p3_top48.md
```
