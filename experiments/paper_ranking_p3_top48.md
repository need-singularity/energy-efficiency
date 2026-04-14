# P3 논문 랭킹 리포트 — 상위 48편 선정

| 필드 | 값 |
|---|---|
| 로드맵 | PAPER-P3-1 |
| 생성일 | 2026-04-14 |
| 입력 풀 | `papers/_registry.json` 등록 125편 |
| 선정 수 | 상위 48편 (P3 gate_exit 요구치) |
| 결과 JSON | `papers/_submission_top48.json` |
| 제출 템플릿 | `papers/_submission_top48_template.md` |

## 1. 점수 공식

```
score = alien_index * 0.4 + (closure_grade_pct / 10) * 0.3 + (citation_depth / 3) * 0.3
```

- `alien_index` (0~10): 섹션 단위 외계인 지수. `_registry.json` sections[].alien_index 를 논문의 domain 와 매핑. 미매핑 시 기본값 7.
- `closure_grade_pct` (0~100): `_papers.json` exact_stat 의 EXACT 비율을 우선 사용. 미기입 시 chunk_status 에 따라 70/72/78/82 로 추정.
- `citation_depth` (0~30): bt_ref 에 등장하는 BT 번호 개수 * 2 + 본문 줄수 / 50. 30 상한 클램프.
- 각 성분은 동일 스케일(0~10)로 정규화 후 가중합. 이론 최대값 10.0, 실제 최댓값 약 9.57.

## 2. 시뮬 DOI 체계 — 실제 DOI 아님

```
10.NEXUS6.n6-arch/<YYYY>-<NNN>
  YYYY = 2026 고정
  NNN  = 001~048 (랭킹 순서)
```

- `10.NEXUS6` 는 CrossRef/DataCite 미등록 접두사. 내부 참조 전용.
- 실제 저널/콘퍼런스 제출 시 이 번호를 교체할 것.
- 본 리포트는 제출 포맷 정비의 참조용으로만 사용.

## 3. 타겟 저널/컨퍼런스 매핑 규칙

| 저널/컨퍼런스 | 배정 규칙 | 선정 편수 |
|---|---|---|
| Nature Communications | 자연과학/생물/지구/문화/산업 일반 (미매핑 도메인 기본값) | 24 |
| Physical Review Letters | 중력·입자·초전도·양자계산·위상수학·순수수학·유체역학·전자기 | 6 |
| IEEE TVLSI | 칩 아키텍처·DRAM/V-NAND·패키징·뉴로모픽·의식칩 | 6 |
| NeurIPS | AI 기법 68/17·SSM·네트워크 집단지성·자율주행·AI 윤리 거버넌스·뇌과학 | 5 |
| ICML | 자기조직/항상성/진화 오우로보로스/블로우업/렌즈포지/사이클 엔진/AGI/어트랙터 | 2 |
| JAIR | 밀레니엄 DFS·법학·아틀라스 승격 프로토콜·가설 MC 검증·경제·거버넌스 | 5 |

## 4. 상위 48편 랭킹

| 순위 | Paper ID | 파일 | 도메인 | 점수 | alien | closure% | cit-depth | 시뮬 DOI | 타겟 |
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

## 5. ASCII 비교 차트 — 상위 15편 점수 막대

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

## 6. 한계 및 반증 후보

- **closure_grade 추정 정확도**: 125편 중 exact_stat 실측 보유는 25편뿐. 나머지 100편은 chunk_status 텍스트 기반 이산 추정값 사용. 실측 감사 후 재랭킹 필요.
- **citation_depth 편중**: bt_ref 수집이 청크 메타데이터 기반이라 청크 미등록 논문은 bt_count=0 이 되어 줄수 기반 부분 점수만 적용된다. 개별 논문 파일 본문 파싱 감사 필요.
- **alien_index 미매핑**: 118/125 도메인이 sections 에 매핑. 7편은 기본값 7 로 fallback — 랭킹 하위로 밀릴 위험.
- **시뮬 DOI**: CrossRef/DataCite 실등록 아님. 외부 인용/검색 엔진에서 해석 불가.
- **반증 조건**: 본 랭킹이 P3 평가에서 상위 48편 외에 alien_index 10 인 논문을 누락시키면 재랭킹 트리거.

## 7. 재현 절차

```
python3 scripts/rank_papers_p3.py   # (본 리포트 생성 스크립트 — 인라인으로 실행됨)
  입력:  papers/_papers.json, papers/_registry.json
  출력:  papers/_submission_top48.json, experiments/paper_ranking_p3_top48.md
```
