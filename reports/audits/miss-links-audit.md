# MISS 링크 감사 보고서

**날짜**: 2026-04-12
**범위**: papers/_products.json 전체 링크 + papers/_papers.json ghost 논문
**작성**: ROI #11 + ROI #15 통합 감사

---

## 1. 감사 요약

| 항목 | 수치 |
|------|------|
| _products.json 전체 링크 수 | 248 |
| _products.json MISS 링크 | 6 (기타 파일, 논문 MISS 0) |
| _papers.json 등록 논문 수 | 96 |
| 감사 전 ghost 논문 | 10 |
| 감사 후 ghost 논문 | 0 (전량 해소) |

---

## 2. ghost 논문 해소 (ROI #11)

### 2.1 해소된 10편 (chunk_c, 인체/의료/생물)

| # | 파일명 | 줄수 | EXACT | 분야 |
|---|--------|------|-------|------|
| 1 | n6-hexa-neuro-paper.md | 237 | 15/15 (100%) | 뉴로모픽 칩/BCI |
| 2 | n6-hexa-mind-paper.md | 255 | 36/40 (90%) | 인지과학/심리학 |
| 3 | n6-hexa-telepathy-paper.md | 192 | 10/10 (100%) | 뇌-뇌 통신/BBI |
| 4 | n6-hexa-dream-paper.md | 181 | 20/20 (100%) | 수면과학/자각몽 |
| 5 | n6-hexa-skin-paper.md | 179 | 20/20 (100%) | 전자 피부/햅틱 |
| 6 | n6-hexa-exo-paper.md | 189 | 20/20 (100%) | AI 외골격/SE(3) |
| 7 | n6-hexa-limb-paper.md | 197 | 24/24 (100%) | AI 의수/의족 |
| 8 | n6-hexa-olfact-paper.md | 188 | 20/20 (100%) | 디지털 후각/전자코 |
| 9 | n6-entomology-paper.md | 226 | 23/23 (100%) | 곤충학/Hexapoda |
| 10 | n6-dolphin-bioacoustics-paper.md | 222 | 18/18 (100%) | 돌고래 생체음향 |

합계: 2,066줄, EXACT 비율 평균 97%

### 2.2 각 논문 포함 요소

모든 논문에 포함:
- 제목, 초록, 키워드 (한글)
- Foundation (n=6 핵심 항등식)
- Domain (핵심 상수 표)
- 성능 비교 (ASCII 그래프)
- 검증 가능한 예측 (TP)
- 한계 및 MISS 공시
- n=6 연결 요약
- 교차 도메인 연결
- 부록 A: Python 임베드 검증코드 (N62 준수)
- 참고문헌

---

## 3. _products.json MISS 링크 감사 (ROI #15)

### 3.1 현재 MISS 링크 6건 (전부 기타 파일, 논문 아님)

| # | 경로 | 라벨 | 섹션 | 제품 |
|---|------|------|------|------|
| 1 | experiments/experiment_full_n6_pipeline.py | 기타 | ai | Full N6 Pipeline |
| 2 | domains/energy/hvac-system/verify.hexa | 기타 | tech-industry | HVAC 냉난방 |
| 3 | domains/infra/earthquake-engineering/verify.hexa | 기타 | tech-industry | 내진설계 |
| 4 | domains/materials/concrete-technology/verify.hexa | 기타 | tech-industry | 콘크리트+탄소포집 |
| 5 | domains/infra/smart-city/verify.hexa | 기타 | tech-industry | 스마트시티 |
| 6 | domains/infra/civil-engineering/verify.hexa | 기타 | tech-industry | 토목/구조역학 |

### 3.2 MISS 유형 분석

- 논문 MISS: 0건 (ghost 10편 해소로 논문 MISS 전량 해소)
- 계산기 MISS: 0건
- hexa 검증코드 MISS: 5건 (verify.hexa 미생성)
- 실험 코드 MISS: 1건 (.py 파일 -- N62 규칙상 .py 금지이므로 경로 자체 재검토 필요)

### 3.3 해소 권장 사항

| 우선순위 | MISS 항목 | 해소 방법 |
|----------|-----------|-----------|
| 높음 | experiment_full_n6_pipeline.py | .py -> .hexa 변환 또는 경로 삭제 (N62 규칙 .py 금지) |
| 중간 | hvac-system/verify.hexa | 도메인 폴더에 verify.hexa 스텁 생성 |
| 중간 | earthquake-engineering/verify.hexa | 도메인 폴더에 verify.hexa 스텁 생성 |
| 중간 | concrete-technology/verify.hexa | 도메인 폴더에 verify.hexa 스텁 생성 |
| 중간 | smart-city/verify.hexa | 도메인 폴더에 verify.hexa 스텁 생성 |
| 중간 | civil-engineering/verify.hexa | 도메인 폴더에 verify.hexa 스텁 생성 |

---

## 4. 감사 전후 비교

```
  감사 전 상태:
  ├── ghost 논문: 10편 (chunk_c 전량)
  ├── _products.json MISS: 6건
  └── 총 MISS: 16건 (ghost 10 + 링크 6)

  감사 후 상태:
  ├── ghost 논문: 0편 (전량 해소)
  ├── _products.json MISS: 6건 (논문 외 파일)
  └── 총 MISS: 6건 (논문 MISS 0 + 기타 6)

  해소율: 10/16 = 62.5%
```

---

## 5. 레지스트리 갱신 내역

- _papers.json: ghost_해소 메타데이터 추가
- _registry.json: papers_chunk_c ghost_status 갱신

---

## 6. 다음 단계

1. 잔여 MISS 6건 중 verify.hexa 5건은 별도 ROI로 hexa 스텁 생성
2. experiment_full_n6_pipeline.py는 N62 규칙 위반이므로 경로를 .hexa로 변경하거나 삭제
3. 전체 논문 96편 -> Zenodo/OSF 발행 준비 확인
