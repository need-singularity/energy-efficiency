# DSE 미커버 도메인 스캔 리포트

- 일시: 2026-04-12
- 분석: domains/_index.json (304 도메인) vs nexus/origins/universal-dse/domains/ (490 TOML)

---

## 요약

| 항목 | 수치 |
|------|------|
| 인덱스 도메인 총수 | 304 |
| DSE TOML 총수 | 490 (인덱스 외 186 확장 도메인 포함) |
| 커버된 도메인 | 84 |
| 미커버 도메인 | 220 |
| 커버율 | 27.6% |
| 금회 신규 생성 | 10건 |
| 생성 후 미커버 | 220건 (인덱스 기준) |

---

## 금회 신규 생성 10건

| # | 도메인 | 축 | 핵심 n=6 연결 | 조합수 |
|---|--------|----|---------------|--------|
| 1 | millennium-yang-mills | physics | SU(3) 색 n/phi=3, sigma=12 게이지 보손 | 7,776 |
| 2 | millennium-riemann | physics | phi(6)/tau(6)=1/2 임계선, sigma(6)=12 약수합 | 7,776 |
| 3 | autonomous-driving | infra | n=6 SAE 레벨, sigma=12 센서, tau=4 인지 | 7,776 |
| 4 | cancer-therapy | life | n=6 치료 양식, sigma=12 바이오마커, tau=4 단계 | 7,776 |
| 5 | fusion-powerplant | energy | sigma=12 TF 코일, n=6 가열 빔라인, phi=2 이중 격납 | 7,776 |
| 6 | mind-upload | cognitive | n=6 피질층, sigma=12 브로드만 영역, phi=2 생물/디지털 | 7,776 |
| 7 | aramid | materials | n=6 벤젠 고리, sigma=12 GPa 강도, phi=2 코어-쉘 | 7,776 |
| 8 | taekwondo | culture | n=6 기본 발차기, sigma=12 품새, tau=4 라운드 | 7,776 |
| 9 | cosmology | physics | n=6 BBN 핵종, z_reion=6, sigma=12 CMB 주파수 | 7,776 |
| 10 | baduk | culture | n=6 활로 최대, sigma=12 정석, phi=2 흑백 | 7,776 |

---

## 축별 미커버 현황

| 축 | 미커버 | 주요 미커버 도메인 |
|----|--------|---------------------|
| infra | 43 | architecture, climate, geology, meteorology, transportation, ... |
| compute | 38 | chip-3d/hexa1/sc/wafer, dram, exynos, vnand, hexa-* 시리즈, ... |
| life | 31 | genetics, immunology, pharmacology, synbio, vaccine, ... |
| physics | 26 | millennium-bsd/hodge/ns/p-vs-np/poincare, electromagnetism, ... |
| culture | 18 | hangul-script, music, photography, writing-systems, yoga, ... |
| cognitive | 17 | anima-service/soc, dream-recorder, hexa-dream/mind/neuro, ... |
| materials | 16 | ceramics, epoxy, gemology, nylon, paper, swordsmithing, ... |
| sf-ufo | 16 | cloak, dragon, fantasy, hexa-cloak/grav/hover/sim/teleport, ... |
| energy | 9 | pemfc, smr-datacenter, superconductor, thermal-management, ... |
| space | 6 | astronomy, hexa-cosmic, hexa-starship, observational-astronomy, ... |

---

## 우선순위 추천 (다음 차수)

### 1순위 (밀레니엄 난제 나머지 5건)
- millennium-bsd, millennium-hodge, millennium-navier-stokes, millennium-p-vs-np, millennium-poincare

### 2순위 (산업 핵심)
- genetics, immunology, superconductor, pemfc, chip-3d

### 3순위 (한국 문화/고유)
- hangul-script, music, photography, archaeology

### 4순위 (hexa-* 확장)
- hexa-dream, hexa-mind, hexa-neuro, hexa-cosmic, hexa-starship

---

## TOML 구조 표준

각 TOML 파일 표준:
- `[meta]`: name, desc, levels (5개 레벨), vision
- `[scoring]`: n6=0.35, perf=0.25, power=0.20, cost=0.20
- 5개 `[[level]]` x 6개 `[[candidate]]` = 30 후보 = 7,776 조합
- 각 candidate: level, id, label, n6, perf, power, cost, notes
- n=6 연결: n=6, sigma=12, tau=4, phi=2, n/phi=3, sigma-tau=8 등
- `[[rule]]`: type (require/exclude), if_level, if_id, then_level, then_ids

---

## 핵심 정리 연결

sigma(n) * phi(n) = n * tau(n) iff n = 6

- sigma(6) = 12 (약수합: 1+2+3+6)
- phi(6) = 2 (오일러 함수: 1,5)
- tau(6) = 4 (약수 개수: 1,2,3,6)
- n = 6 (유일 해)
- 검증: 12 * 2 = 24 = 6 * 4

모든 DSE TOML은 이 상수 체계(n=6, sigma=12, tau=4, phi=2)를 설계 공간 파라미터에 매핑.
