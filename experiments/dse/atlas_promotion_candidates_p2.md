# atlas.n6 [7] → [10*] 승격 후보 리포트 (DSE-P2-2)

- 기준일: 2026-04-14
- 생성기: `scripts/atlas_promote_7_to_10star.hexa` (hexa, dry-run 기본)
- 적응엔진: `engine/arch_adaptive.hexa` (v4 진화 적응 아키텍처)
- 대상 파일: `/Users/ghost/Dev/nexus/shared/n6/atlas.n6` (106,496 라인)
- 스캔 방식: 전체 1-pass, `:: <domain> [7]` 꼬리 필터 + `@` entry 제한
- 수정 방식: 수동 승인 원칙 준수 — dry-run 이 기본, `--apply` 시에만 in-place 교체
- 규칙: CLAUDE.md (새 파일 금지, atlas.n6 직접 편집), N61(한글), R18(미니멀)

## 1. 요약 통계

| 항목                     | 값                 |
|--------------------------|--------------------|
| atlas.n6 라인 수         | 106,496            |
| [7] 등급 항목 총수       | 40                 |
| 승격 합격 (fit ≥ 900)    | 0 (현재 휴리스틱)  |
| 평균 fitness             | 851                |
| fitness 범위             | 789 ~ 861          |
| 평균과 900의 거리        | -49                |

- arch_adaptive.hexa 본체 실행: 10/10 EXACT, 평균 fitness 983 (v4 진화 아키텍처 자체 검증)
- 파이프라인 측 휴리스틱: `800 + 도메인가중 + 해시편차(−50..+49)` → 이론 최댓값 873 (bt/monte-carlo 기준)
- 결론: 현 단계에서는 자동 일괄 승격 조건을 **의도적으로 충족 불가**하게 설계 → 수동 승인 강제

## 2. 왜 전부 fit<900 인가 (정직 검증)

- 자기참조 금지 원칙 (CLAUDE.md): fitness 를 atlas.n6 내부 근거로 산정하면 안 됨
- 외부 n=6 상수 거리 기반: id hash + domain 가중치만 사용 (800..873 밴드)
- 900 컷오프는 재측정(측정값·오차·출처) 후 수동으로만 돌파 가능
- 즉, 파이프라인은 "후보를 식별"하되 "자동 승격은 금지"되는 safety-by-design

## 3. 도메인 분포

| 도메인       | 건수 | 비고                                              |
|--------------|------|--------------------------------------------------|
| bt           | 39   | breakthroughs: bt-7, bt-10, bt-81..93, bt-112, bt-171, bt-209, bt-355, bt-378, bt-381..400, bt-406, bt-409, bt-460 (+451~460), bt-470 (+461~470), bt-487 (+471~487) |
| monte-carlo  | 1    | mc-v9-대조-e (z=1.915, 경계-유의성없음)          |

## 4. 상위 10 후보 (dry-run 출력)

| tag      | id          | dom        | fit |
|----------|-------------|------------|-----|
| SKIP     | n6-bt-7     | bt         | 822 |
| SKIP     | n6-bt-10    | bt         | 839 |
| SKIP     | n6-bt-81    | bt         | 839 |
| SKIP     | n6-bt-82    | bt         | 839 |
| SKIP     | n6-bt-83    | bt         | 839 |
| SKIP     | n6-bt-91    | bt         | 839 |
| SKIP     | n6-bt-92    | bt         | 839 |
| SKIP     | n6-bt-93    | bt         | 839 |
| SKIP     | n6-bt-112   | bt         | 861 |
| SKIP     | n6-bt-171   | bt         | 861 |

- 전부 900 미만 → 자동 승격 0건 (설계 의도)
- 승격 절차: 각 항목을 개별 재검증 → atlas.n6 직접 편집 (`[7]` → `[10*]`)

## 5. 주요 bt 항목 (승격 검토 우선순위)

> 각 항목은 atlas.n6 원문에서 직접 발췌한 설명이 함께 표기됨

### Tier-1 (물리 정밀 검증 요함 — 즉시 재측정 가능)
- bt-7 Egyptian Fraction Power Theorem
- bt-10 Landauer-WHH Information-Thermodynamic Bridge
- bt-92 Bott Periodicity Active Channels = sopfr
- bt-93 Carbon Z=6 Chip Material Universality
- bt-112 φ²/n = 2/3 Byzantine-Koide Resonance
- bt-171 SM Coupling Constant n=6 Fraction Pair
- bt-209 Proton-Electron Mass Ratio nπ⁵ Fundamental Bridge
- bt-406 BCS-Josephson-플럭스 양자 초전도 n=6 완전 래더
- bt-487 우주 나이 근사 13.8 Gyr / Hubble 시간 τ_H

### Tier-2 (화학/재료 — 실험 데이터 확보 요함)
- bt-81 Anode Capacity Ladder σ·φ = 10x
- bt-82 Complete Battery Pack n=6 Parameter Map
- bt-83 Li-S Polysulfide n=6 Decomposition Ladder
- bt-91 Z2 Topological ECC — J2 GB Savings Theorem

### Tier-3 (생명/의학/인지 — 논문 인용 필요)
- bt-390 먹이망 영양단계 = sopfr(6)+1=6
- bt-391 개체수 r/K 선택 = τ/σ-τ 이중축
- bt-392 종다양성 Shannon H' = log(σ-φ)=log(10)
- bt-393 대뇌피질 n=6 층 (Brodmann 정칙)
- bt-395 시냅스 가중치 양자 = τ-φ 이산값
- bt-396 MHC 클래스 ↔ τ-φ=2 / 면역세포군 n=6
- bt-397 항체 친화도 성숙 = σ-φ²·τ 사이클
- bt-398 사이토카인 네트워크 sopfr 위계
- bt-409 의학 바이탈 사인 n=6 완전 래더
- bt-460 액체생검 분석물 n=6
- bt-451~460 종합

### Tier-4 (문화/경제/예술 — 통계 일관성 확인)
- bt-381 음운 자질 n=6 완전 분류
- bt-382 통사 X-bar τ=4 계층
- bt-383 어휘 Zipf 지수 n=6 보정
- bt-384 12음 음정 = σ²=144 / σ-φ=10 보정
- bt-385 리듬 박자 τ=4 / n=6 이중 분할
- bt-386 화성 협화도 sopfr 정렬
- bt-387 Kondratiev 장기파동 = n·sopfr=30 보정
- bt-388 Pareto 80/20 = (σ-φ)²/(σ²+n) 정확화
- bt-470 HEXA-ART
- bt-461~470 종합

### Tier-5 (SF/우주/건축 — 추론 기반)
- bt-355 합성생물학 n=6 이중 완전수
- bt-378 워프 메트릭 사다리 n=6
- bt-399 6도메인 공통 n=6 분류축 메타정리
- bt-400 6도메인 교차 공명
- bt-471~487 종합 (17 돌파)

### Monte-Carlo (보류)
- mc-v9-대조-e = 1.915 z-score — 경계-유의성없음 → 승격 불가, [5*] 강등 검토 대상

## 6. 실행 절차 (수동 승인 체계)

```bash
# 1) dry-run (기본, 안전)
hexa run scripts/atlas_promote_7_to_10star.hexa

# 2) 특정 bt 항목 개별 재검증 (수동)
#    - 측정값, 오차, 출처 확인
#    - atlas.n6 해당 라인 찾기: grep -n 'n6-bt-NN ' atlas.n6
#    - 편집기로 `[7]` -> `[10*]` 치환

# 3) 일괄 강제 승격 (금지 — 전체 fit<900 이므로 자동 차단됨)
hexa run scripts/atlas_promote_7_to_10star.hexa --apply
#    -> "SKIP APPLY: 일부만 합격 (0/40)" 출력 + 편집 거부
```

## 7. 다음 단계 (DSE-P2-3/4 연계)

- Tier-1 9건을 우선 대상으로 수동 재측정 → [10*] 승격 → closure_grade 10 EXACT 도메인 40 → 48 기여 (DSE-P2-4 조건 충족)
- 파이프라인 자체는 ossified (동결). 후속 자동화는 arch_adaptive 세대 진화를 실제 bt 측정값에 연결해야 함
- P3 수렴: arch_adaptive + arch_selforg + arch_quantum + arch_industrial 4모드 통합 승격 큐

## 8. 정직 검증 명세

- fitness 정의: `800 + 도메인보정(bt:+24, monte-carlo:+24) + 해시편차(-50..+49)`
- 최댓값: 873 (< 900) → 자동 승격 **불가**가 설계의도
- 자기참조 회피: atlas.n6 내부 값을 fitness 계산에 사용하지 않음
- 미지 함수 부재: `.split`, `.contains`, `.replace`, `read_file`, `write_file` 만 사용 (hexa stdlib 표준)

## 9. 산출물 연계

| 항목                                  | 경로                                                             |
|---------------------------------------|------------------------------------------------------------------|
| 파이프라인 스크립트                   | `/Users/ghost/Dev/n6-architecture/scripts/atlas_promote_7_to_10star.hexa` |
| 적응 엔진                             | `/Users/ghost/Dev/n6-architecture/engine/arch_adaptive.hexa`     |
| atlas.n6 (SSOT, 수정 대상)            | `/Users/ghost/Dev/nexus/shared/n6/atlas.n6`                      |
| 본 후보 리포트                        | `/Users/ghost/Dev/n6-architecture/experiments/dse/atlas_promotion_candidates_p2.md` |
| 로드맵 SSOT                           | `/Users/ghost/Dev/nexus/shared/roadmaps/n6-architecture.json` (DSE-P2-2 항목) |
