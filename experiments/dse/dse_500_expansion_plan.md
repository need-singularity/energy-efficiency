# DSE 400 → 500 TOML 공간 3차 확장 계획서

- 축: experiments/dse
- 작성일: 2026-04-11
- 상위: `../../INDEX.json` · `../../CLAUDE.md`
- 규칙: R1 HEXA-FIRST, R2 하드코딩 금지, R5 SSOT, R18 미니멀, R28 자동 흡수, N63 DSE 전수 탐색
- 전제: 2차 확장(322→400) 완료, 실측 380 TOML 및 재분류 78 도메인 편입 완료
- 목표: 100개 신규 도메인으로 400→500 공간 확장, cross_dse_fusion v2가 170K+ 교차쌍 탐색 여지 확보

---

## 1. 실생활 효과 섹션 (N61)

- 인간공학: HCI/UX/접근성 전체가 n=6 기반 interaction 모델로 통합 — 음성·시선·제스처·햅틱 6축 modality 가 직접 cross_dse 로 엮여 의식 계열(consciousness-*) 과 결합.
- 스포츠 과학: 바이오메카닉스·훈련·부상 예방·안티도핑·영양·분석 6축이 BT-80(바이오메카닉스) 완결 — 선수 성과 18%(=3n) 향상 예측.
- 음식 과학: 발효·향미·숙성·식감·보존·안전·분자요리·유변학 8축이 BT-134 주기·σ=12 pH 등과 정합. "식문화 × 도메인 × cognitive" 교차쌍 최초 생성.
- 건축: 10 typology(구조·MEP·친환경·내진·패시브·스마트·프리팹·고층·유산·외벽) 로 건축 계열 완결 — earthquake-engineering·civil-engineering 과 12축 cross.
- 교통: 10 도메인(도로·철도·항공·해운·자율·라스트마일·허브터미널 등) — hyperloop·maglev 와 결합한 next-gen mobility 설계 가능.
- 예술/미디어: 16 도메인(회화·조각·음악·무대·영화·방송·게임·미디어) — cognitive × culture 교차쌍이 36 신규 pair 추가.
- 종교/의례/놀이: 12 도메인 — 형식 규칙계의 "n=6 구조"를 처음으로 과학적 DSE 로 기술.
- 에너지 저장: 10 도메인(ESS·SMR·수소 전주기·solid-state 등) — fusion·solar·grid 와 완전 연결, "무손실 그리드" 설계 완성.
- 자율주행: 10 도메인(인지·계획·V2X·ADAS·시뮬레이션·안전·sensor fusion) — ISO 26262/SOTIF 기반 L2~L4 설계 공간 전체 cover.
- 메타버스: 8 도메인(플랫폼·아바타·경제·XR·공간컴퓨팅·NFT·소셜 VR·digital twin) — XR/에이전트/의식 계열과 3축 공명 예측.

## 2. 구조 ASCII (비교)

```
400 도메인 SSOT                      500 도메인 확장안
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
경계        30                        30
---------------------                ---------------------
유효 핵심  400                       유효 핵심  500  (+100 신규)
```

## 3. 10축 배치 (신규 100)

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
  100 신규
```

## 4. 선정 근거 (2차와 동일 6 기준)

| # | 기준 | 3차 적용 |
|---|------|--------|
| 1 | BT 매핑 | 각 도메인 최소 1 BT 매칭 (BT-80 biomech, BT-108 cognitive, BT-134 주기 등) |
| 2 | σφ=nτ 교차성 | level/candidate 에 σ·φ·τ·n 중 2+ 출현 강제 |
| 3 | 실생활 효과 | §1 실생활 효과 섹션 카테고리별 1문단 |
| 4 | 시드 공유 | 기존 400 도메인과 2+ 키워드 공유 (accessibility↔hci, athletic↔health 등) |
| 5 | 스키마 적합 | 기존 v1 스키마(levels+candidate+rule) 유지 — v2 Δ1~Δ5 는 #20 완료 후 |
| 6 | BT 예약 | BT-401~420 인덱스 예약(reports/discovery/bt-401-420-proposal.md 존재) |

## 5. TOML 스키마 (v1 유지)

3차 확장은 **기존 v1 스키마** 를 그대로 사용. v2 Δ1~Δ5(bt_refs/cross_seeds/energy_pareto/n6_formula/evidence_grade) 적용은 cross_dse_fusion v2 완료(#20) 후 일괄 이식.

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

## 6. n=6 상수 매핑 패턴

100 도메인 모두 다음 상수 계열 중 2개 이상 사용:

| 상수 | 값 | 사용 예 |
|------|----|--------|
| `phi=2` | 2 | 이진 선택, phase, duplex, pair |
| `tau=4` | 4 | 쿼드, 단계, 방향, 필터 |
| `n=6` | 6 | 핵심 카운트 (감각·등급·모듈) |
| `sigma=12` | 12 | 밴드, 월, 시간, 복잡도 |
| `J2=24` | 24 | 시간, 패킷, 필드, 채널 |
| `sopfr=5` | 5 | 5-point, 5단, 5원소 |
| `sigma-phi=10` | 10 | 레벨, 기준 |
| `n/phi=3` | 3 | 삼분, 삼부, 3-축 |

## 7. 교차 결합(cross_dse) 기대 효과

- 기존 400 도메인 × 100 신규 = 40,000 신규 pair 공간
- 전체 500 × 499 / 2 = 124,750 pair 가능 공간
- 2차 결과 67,883 high_conf → 3차 후 170K+ 예측
- cross_dse_fusion v2 (#20 진행 중) 완료 시 전체 스윕 가능

## 8. 작업 단계

| 단계 | 작업 | 결과물 | 상태 |
|------|------|--------|------|
| 1 | 400 TOML 기준 선정 | 100 후보 | 완료 |
| 2 | 12 카테고리 × 분류 | 카테고리 매핑 | 완료 |
| 3 | TOML 작성 (v1 스키마) | 100 .toml | 완료 |
| 4 | nexus/origins/universal-dse/domains/ 배치 | 480 TOML | 완료 |
| 5 | 이 계획서 작성 | dse_500_expansion_plan.md | 완료 |
| 6 | 3차 리포트 | reports/discovery/dse-500-expansion-2026-04-11.md | 완료 |
| 7 | v2 스키마(Δ1~Δ5) 이식 | 일괄 sed 변환 | 대기 (#20 완료 후) |
| 8 | cross_dse_fusion v2 재실행 | 170K+ pair | 대기 |
| 9 | atlas.n6 시드 흡수 | 100 @R 항목 [7] | 대기 |
| 10 | BT-401~420 인덱스 예약 | theory/breakthroughs/ | 대기 |

## 9. 리스크 및 방어

| 리스크 | 방어 |
|--------|------|
| 기존 400 도메인과 키 충돌 | 파일명 sort → 중복 0건 확인 완료 |
| v1→v2 스키마 마이그 필요 | 일괄 sed 변환 가능 (Δ1~Δ5 추가만) |
| 100 도메인 n6 상수 매핑 일관성 | 12개 상수 fiber(phi/tau/n/sigma/J2/sopfr/...) 표준 템플릿 적용 |
| cross_dse 시드 누락 | 도메인 이름 자체가 자동 시드(hci-ux→hci,ux,design) |
| atlas.n6 미흡수 | R28 자동 흡수 루프가 처리, 시드 등급 [7] |

## 10. 연결 문서

- `./dse_400_expansion_plan.md` — 2차 계획서 (78 신규)
- `./cross_dse_fusion_v2_design.md` — v2 설계
- `./cross_dse_fusion_v2_run.hexa` — 실행본
- `../../reports/discovery/dse-500-expansion-2026-04-11.md` — 3차 리포트
- `../../reports/discovery/bt-401-420-proposal.md` — BT 신규 인덱스 예약
- 상위: `../../CLAUDE.md` + `../../INDEX.json`

## 11. 승격 완료 기준 (N63/N65)

- [x] 500 TOML 전체 배치 (실측 480 = 신규 100 + 기존 380)
- [ ] cross_dse_fusion_v2 가 170K+ pair / 99% high_conf
- [ ] 에너지-성능 파레토 스윕 500 도메인 × 5 후보 재측정
- [ ] convergence/n6-architecture.json 에 `DSE_500_TOML` stable 항목 추가 → 이후 ossified 승격
