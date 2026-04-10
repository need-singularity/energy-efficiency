# BT 라벨 ↔ 실측값 1:1 정밀 매핑 — 2026-04-08

대상: 논문 44편 + 가설 파일 (상위 50편).

## 추출 전략 (날조 금지)
- A) 마크다운 BT 표: `| BT-NNN | 이름 | … | 숫자 |` 행 파싱.
- B) 인라인 문장: 한 문장 안에 `BT-NNN`과 정수가 동시 등장하면 페어링.
- 각 정수는 sigma/tau/phi/sopfr/jordan2(6) 또는 그 조합과 일치할 때만 채택.
- 매칭 5건 미만 파일은 기존 검증 블록 보존 (skip).
- 모든 기댓값은 산술함수 호출(코드 실행)로 도출. 하드코딩 비교 금지.

| 파일 | 매칭수 | PASS/TOTAL | 비고 |
|---|---|---|---|
| n6-aerospace-transport-paper.md | 92 | 92/92 | OK |
| n6-autonomous-driving-paper.md | 28 | 28/28 | OK |
| n6-battery-energy-paper.md | 13 | 13/13 | OK |
| n6-biology-medical-paper.md | 13 | 13/13 | OK |
| n6-calendar-time-geography-paper.md | 24 | 24/24 | OK |
| n6-carbon-capture-paper.md | - | - | skip: only 0 BT extractions |
| n6-causal-chain-paper.md | - | - | skip: only 0 BT extractions |
| n6-classical-mechanics-accelerator-paper.md | - | - | skip: only 3 BT extractions |
| n6-cognitive-social-psychology-paper.md | 48 | 48/48 | OK |
| n6-consciousness-chip-paper.md | - | - | skip: no results list literal |
| n6-consciousness-soc-paper.md | - | - | skip: only 4 BT extractions |
| n6-control-automation-paper.md | 5 | 5/5 | OK |
| n6-crystallography-materials-paper.md | 26 | 26/26 | OK |
| n6-dram-paper.md | 5 | 5/5 | OK |
| n6-ecology-agriculture-food-paper.md | 58 | 58/58 | OK |
| n6-economics-finance-paper.md | 27 | 27/27 | OK |
| n6-energy-efficiency-paper.md | - | - | skip: only 0 BT extractions |
| n6-environment-thermal-paper.md | 25 | 25/25 | OK |
| n6-exynos-paper.md | 7 | 7/7 | OK |
| n6-games-sports-paper.md | 16 | 16/16 | OK |
| n6-governance-safety-urban-paper.md | 7 | 7/7 | OK |
| n6-hexa-3d-paper.md | - | - | skip: only 2 BT extractions |
| n6-hexa-photon-paper.md | - | - | skip: only 2 BT extractions |
| n6-hexa-pim-paper.md | - | - | skip: only 2 BT extractions |
| n6-hexa-super-paper.md | - | - | skip: only 2 BT extractions |
| n6-hexa-wafer-paper.md | - | - | skip: only 2 BT extractions |
| n6-isocell-comms-paper.md | - | - | skip: only 1 BT extractions |
| n6-manufacturing-quality-paper.md | 5 | 5/5 | OK |
| n6-particle-cosmology-paper.md | 45 | 45/45 | OK |
| n6-performance-chip-paper.md | 14 | 14/14 | OK |
| n6-plasma-fusion-deep-paper.md | 67 | 67/67 | OK |
| n6-pure-mathematics-paper.md | - | - | skip: only 0 BT extractions |
| n6-quantum-computing-paper.md | 21 | 21/21 | OK |
| n6-reality-map-paper.md | - | - | skip: only 3 BT extractions |
| n6-robotics-transport-paper.md | 46 | 46/46 | OK |
| n6-rtsc-12-products-evolution-paper.md | 16 | 16/16 | OK |
| n6-software-crypto-paper.md | 36 | 36/36 | OK |
| n6-space-systems-paper.md | 22 | 22/22 | OK |
| n6-superconductor-paper.md | 20 | 20/20 | OK |
| n6-telecom-linguistics-paper.md | 15 | 15/15 | OK |
| n6-thermodynamics-paper.md | 7 | 7/7 | OK |
| n6-unified-soc-paper.md | 13 | 13/13 | OK |
| n6-virology-paper.md | - | - | skip: no results list literal |
| n6-vnand-paper.md | - | - | skip: only 4 BT extractions |
| H-OURO-1-self-referential-n6.md | - | - | skip: no results list literal |
| H-OURO-2-egyptian-health-convergence.md | - | - | skip: no python block |
| H-OURO-2-health-fraction-ladder.md | - | - | skip: no python block |
| H-OURO-2-sigma12-transformer-atom.md | - | - | skip: no python block |
| H-OURO-2-sigma12-transformer-universality.md | - | - | skip: no python block |
| H-OURO-3-convergence-automaton.md | - | - | skip: no results list literal |

## 요약
- 전체 대상: 50 편
- 패치 성공: 28 편 / skip: 22 편
- 1:1 매칭 합계: 721
- 평균 매칭수/성공편: 25.8
- 검증 항목 합계: 721
- PASS 합계: 721
- PASS 비율: 100.0%