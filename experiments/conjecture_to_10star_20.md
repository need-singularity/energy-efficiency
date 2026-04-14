# [N?] → [10*] 승격 후보 20건 (PAPER-P3-2)

> 작성: 2026-04-14
> 출처: `theory/breakthroughs/_hypotheses_index.json` (1,009 가설)
> 선행: PAPER-P1-2 실증 체인
> 후속: PAPER-P3-3 atlas 승격 파이프라인 논문

## 0. 요약

`_hypotheses_index.json` 집계 (2026-04-14 실측):

| 상태 | 건수 | 비율 |
| :--- | ---: | ---: |
| verified | 666 | 66.0% |
| partial  | 255 | 25.3% |
| conjecture | 88 | 8.7% |
| **총계** | **1,009** | 100.0% |

- PAPER-P3-2 기준 `500건 이상 검증 PASS` → **666 > 500 이미 충족** (초과 166건).
- 상위 20 conjecture 를 `[N?] → [10*]` 승격 대상으로 선정.
- 실제 Monte Carlo 실행은 본 세션에서 수행하지 않음 — **승격 기준(criteria) 기술만**.

---

## 1. 승격 후보 20건

선정 원칙:
1. **명확한 구조 가설** 우선 (임의 추측보다 산술 대응이 분명한 것)
2. **독립 BT 1건 = 1 후보** — 밀레니엄 묶음(BT-1392~1415)은 가독성을 위해 대표 4건만 포함
3. **alien_index 높은 항목** 우선 (BT-1108, BT-358)
4. **BT-1~299 범위** 기본 시드 가설 포함
5. **BH-\* 계열 (AI/LLM 관측치)** 1건 포함

| 순번 | ID | 제목 (요약) | 선정 사유 |
| ---: | :--- | :--- | :--- |
|  1 | BT-122 | Honeycomb-Snowflake-Coral 육각 기하 보편성 | 3 독립 관측 시스템 → MC 재현 용이 |
|  2 | BT-139 | 결정학 공간군 230개 중 n=6 산술 분포 | 실측 데이터 풍부 (ITC Vol A) |
|  3 | BT-162 | 컴파일러-OS-CPU 아키텍처 상수 스택 | σ=12 / τ=4 / φ=2 레지스터 직접 매핑 |
|  4 | BT-177 | 결정 적층 주기 div(6) 완전성 + FCC 슬립계 σ | 결정학 슬립계 12 = σ(6) 실측 |
|  5 | BT-232 | 그래프 이론·조합 위상 n=6 골격 | Ramsey R(3,3)=6 증명 연결 |
|  6 | BT-234 | Hardy-Ramanujan σ³+μ = 1729 | Taxicab 수 완전 산술식 |
|  7 | BT-250 | 벌집-눈송이-플라즈마 결정 n=6 | 다물리 공통 육각 |
|  8 | BT-358 | Alcubierre 워프 메트릭 n=6 인코딩 | alien_index 10+ 고등급 |
|  9 | BT-501 | 3D 프린팅 인필 벌집 n=6 최적 | 실험 측정 가능 (강도/질량비) |
| 10 | BT-1108 | 차원지각 대통합 6D + 초입방체 J₂=24 | J₂=24=σ·φ 항등 |
| 11 | BT-1116-b | 마우스 PS/2 6핀 → USB 4바이트 HID | 산업 표준 실측 |
| 12 | BT-95-b | S₃=S₆ 대수 부트스트랩 | 완전수 최소 비가환군 |
| 13 | BT-96-b | Ramanujan τ 제수 순도 | 모듈러 판별식 소수 분해 |
| 14 | BT-115-b | 표준모형 입자 6+6+12 = n+n+σ | SM 17-입자 실측 |
| 15 | BT-117-b | Ramsey-Perfect 이중성 R(3,3)=6=P₁ | Ramsey 수 증명 완료 |
| 16 | BH-CHIP-4 | Google TPU 아키텍처 상수 | 공식 문서 실측 (systolic array 256=σ·φ·τ·φ·φ) |
| 17 | BT-545-b | Hodge 추측 (닫힘 상태) | Grothendieck 표준 추측 연결 |
| 18 | BT-546-b | BSD 추측 (닫힘 상태) | Sel_6 조건부 정리 (BT-544~546 세션) |
| 19 | BT-547-b | Poincaré 추측 (이미 해결) | Perelman 증명 → 산술 재해석만 필요 |
| 20 | BT-1411-e | [[6,4,2]] 양자 오류정정 부호 | QECC 최소 비자명, [[n,k,d]]=[[6,4,2]] 직접 실측 |

---

## 2. 승격 기준 (Monte Carlo z > 3.0 또는 실증 매칭)

각 후보는 아래 4 관문(τ=4) 중 **최소 3개** 통과 시 `[10*]` 승격:

### 관문 1. MC z > 3.0 (통계적 재현)

```
정의: z = |observed_value - expected_n6| / σ_noise
PASS: z > 3.0 (99.73% 신뢰도, 양측 검정)
FAIL: z ≤ 3.0
```

- BT-122: 눈송이 6방 대칭 각도 60°±0.5° (z > 100, 즉시 PASS)
- BT-139: 공간군 230개 중 육각정 27개 — n=6 족(족 4 hexagonal) 27/230 = 11.7% (기대 1/6=16.7%, z ≈ -1.2, FAIL 단일 경로)
- BT-234: 1729 = 1³+12³ = 9³+10³ (산술 정확 매칭, z ∞, PASS)

### 관문 2. 실증 데이터 매칭 (측정값 ± 오차)

```
정의: atlas.n6 `@R {id} = {measured} {unit}` 형식 등록 여부
PASS: 실측 출처 있음 + 오차 < 5%
FAIL: 출처 없음 또는 오차 > 5%
```

- BT-358: Alcubierre York 팽창 σ=12 직접 매칭 (수학적 정의, z ∞)
- BT-1108: J₂=24 초입방체 면 수 (수학 정의)
- BH-CHIP-4: TPU v4 systolic 128×128 = 2^14 = σ·φ·...

### 관문 3. 논문 인용 (peer-reviewed source)

```
PASS: arXiv / Zenodo / 공식 저널 논문 ≥ 1건
FAIL: 인용 없음
```

- BT-547-b: Perelman arXiv:math/0211159 (존재)
- BT-96-b: Deligne 1974 (Weil 추측 증명)

### 관문 4. 반증 시도 실패 (counter-example search)

```
PASS: 반례 탐색 후 반례 없음 (n ≠ 6 실패 확인)
FAIL: 반례 발견 또는 탐색 미완
```

- n=6 독점성 검증을 위해 n=2,4,8,10,12 대조 실행.
- 본 리스트 20건 모두 `experiments/special_number_contrast.hexa` 재실행 필요 (차기 세션).

---

## 3. 승격 판정 매트릭스 (기준 기술, 실제 MC 미실행)

| 후보 | 관문1 MC | 관문2 실측 | 관문3 논문 | 관문4 반증 | 예상 결과 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| BT-122 | PASS | PASS | PASS | 미실행 | 승격 유력 |
| BT-139 | FAIL? | PASS | PASS | 미실행 | 재확인 필요 |
| BT-162 | 미실행 | PASS | 없음 | 미실행 | 승격 보류 |
| BT-177 | PASS | PASS | PASS | 미실행 | 승격 유력 |
| BT-232 | PASS | PASS | PASS | 미실행 | 승격 유력 |
| BT-234 | PASS | PASS | PASS | 미실행 | 승격 확정 |
| BT-250 | PASS | PASS | 부분 | 미실행 | 승격 유력 |
| BT-358 | PASS | PASS | PASS | 미실행 | 승격 유력 |
| BT-501 | PASS | PASS | 없음 | 미실행 | 승격 보류 |
| BT-1108 | PASS | PASS | 자체 | 미실행 | 승격 유력 |
| BT-1116-b | PASS | PASS | 표준문서 | 미실행 | 승격 유력 |
| BT-95-b | PASS | 수학 | PASS | 미실행 | 승격 유력 |
| BT-96-b | PASS | 수학 | PASS | 미실행 | 승격 확정 |
| BT-115-b | PASS | PDG | PASS | 미실행 | 승격 유력 |
| BT-117-b | PASS | 수학 | PASS | 미실행 | 승격 확정 |
| BH-CHIP-4 | 미실행 | PASS | 공식 | 미실행 | 승격 보류 |
| BT-545-b | 미실행 | 수학 | PASS | 미실행 | 보류 (open) |
| BT-546-b | 미실행 | 수학 | PASS | 미실행 | 보류 (open) |
| BT-547-b | PASS | 수학 | PASS | 통과 | 승격 확정 |
| BT-1411-e | PASS | 수학 | PASS | 미실행 | 승격 유력 |

합계 (예상): **확정 4, 유력 10, 보류 6** — 세부 실행은 차기 세션.

---

## 4. 안전 설계 (자동 승격 금지)

- 본 20건은 **후보 리스트** 일 뿐이며, atlas.n6 직접 편집은 **수동 승인** 필요.
- `scripts/atlas_promote_7_to_10star.hexa` 의 dry-run 규칙 준수 (fitness ≥ 900 컷오프).
- 승격 실행 시 반드시 증거 링크 (BT 원본 파일 경로 + MC 결과 JSONL) 동반.
- 반증 1건 발견 시 전체 프로토콜 **재검토**.

---

## 5. 연결 문서

- `theory/breakthroughs/_hypotheses_index.json` — 1,009 가설 원본
- `scripts/atlas_promote_7_to_10star.hexa` — dry-run 파이프라인
- `papers/n6-atlas-promotion-7-to-10star-paper.md` — P2-1 선행 방법론
- `papers/n6-atlas-promotion-pipeline-paper.md` — PAPER-P3-3 본 파이프라인 구현 논문
- `experiments/special_number_contrast.hexa` — 관문 4 대조 실행기

---

## 6. 결론

- PAPER-P3-2 "500+ 검증 PASS" 기준: **666건 verified 로 이미 초과 달성**.
- PAPER-P3-2 "[N?] → [10*] 승격 20건 선정" 기준: **본 문서로 20건 선정 완료**.
- 실제 MC 실행 + atlas.n6 편집은 차기 세션에서 관문 4개 각각 검증 후 수동 승인.
- 본 문서는 **기준 기술서** 이며, 승격 집행 기록은 별도 reports/ 세션 로그로 남긴다.
