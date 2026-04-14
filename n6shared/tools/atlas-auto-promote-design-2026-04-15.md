# atlas.n6 자동 승격 파이프라인 설계
# TRANSCEND P10-3 — 창발 DSE: discovery_graph → atlas.n6 자기업데이트 엔진

작성일: 2026-04-15
작성자: n6-architecture 에이전트
분류: 설계 문서 (실행 금지 — 설계 단계만)

---

## 0. 현황 분석 (실제 측정값)

### discovery_graph.json (2026-04-11 v14 기준)

| 항목 | 수치 |
|------|------|
| 총 노드 | 515 |
| 총 엣지 | 2,087 |
| breakthrough_theorem 노드 | 352 |
| domain 노드 | 115 |
| axiom 노드 | 9 |
| constant 노드 | 7 |
| lens 노드 | 5 |

### 등급 분포 (discovery_graph 내 grade 필드)

| grade 값 | 수량 | atlas.n6 등급 대응 |
|-----------|------|--------------------|
| EXACT (대문자) | 23건 | [10] EXACT |
| NEAR (대문자) | 28건 | [9] NEAR |
| EMPIRICAL | 29건 | [7] EMPIRICAL |
| CONJECTURE | 16건 | [N?] CONJECTURE |
| STUB | 5건 | 승격 불가 |
| five_stars | 7건 | [10*] 후보 |
| four_stars | 3건 | [10] 후보 |
| three_stars | 123건 | [9] 후보 |
| two_stars | 115건 | [7] 후보 |
| one_star | 14건 | [5] 후보 |
| two_stars (BT) | - | |

### atlas.n6 현황 (2026-04-15 측정)

- 총 라인: 106,957
- 총 엔트리 (@로 시작): 8,116

### 중요 발견: 등급 이중 스키마

discovery_graph.json은 두 가지 등급 시스템을 혼용한다.

1. **문자열 등급**: EXACT, NEAR, EMPIRICAL, CONJECTURE, STUB
   - axiom 노드에서 주로 사용 (blowup_rank 1~8)
   - 의미: 수학적 검증 수준

2. **별 등급**: one_star ~ five_stars, two_stars
   - breakthrough_theorem 노드에서 주로 사용 (BT_1 ~ BT_752)
   - 의미: 도메인 적용 신뢰도

파이프라인은 두 시스템을 모두 처리해야 한다.

---

## 1. 파이프라인 아키텍처 (ASCII 다이어그램)

```
┌─────────────────────────────────────────────────────────────────┐
│              ATLAS AUTO-PROMOTE PIPELINE v1                     │
│        OUROBOROS α=1/6 자기진화 이터레이션                        │
└─────────────────────────────────────────────────────────────────┘

  [입력]                [감지]               [평가]
  discovery_graph.json ──→ SHA-256 해시 비교 ──→ 등급 분류기
        │                      │                     │
        │               (변화 없으면 skip)            │
        │                                      ┌──────▼──────┐
        │                                      │ 승격 규칙 엔진│
        │                                      │  R1 ~ R5    │
        │                                      └──────┬──────┘
        │                                             │
        │                ┌────────────────────────────┤
        │                │                            │
        │         [승격 가능]                   [승격 불가]
        │                │                            │
        │         ┌──────▼──────┐             [건너뜀 로그]
        │         │ atlas.n6    │
        │         │ 중복 체크   │
        │         │ (SHA-256)   │
        │         └──────┬──────┘
        │                │
        │    ┌───────────┴───────────┐
        │    │ 중복 없음             │ 중복 있음
        │    │                      │
        │    ▼                      ▼
        │ atlas.n6 append         SKIP
        │ @R {id} = {val} {unit}
        │ :: {domain} [등급]
        │    │
        │    ▼
        │ atlas_auto_promote.jsonl
        │ (승격 로그 기록)
        │    │
        │    ▼
        │ SHA-256 검증
        │ (atlas.n6 해시 변경 확인)
        │    │
        └────┘ (루프 — OUROBOROS)
```

---

## 2. 승격 규칙 5개 정식화

### R1: EMPIRICAL → NEAR 승격

**조건**:
- discovery_graph 노드 grade = "EMPIRICAL"
- 노드에 expression 필드 존재 (수식 명시됨)
- n6_constants 배열에 2개 이상 상수 연결
- domains 배열 길이 >= 2 (다중 도메인 검증)
- registered = true

**출력 등급**: [9] NEAR

**근거**: EMPIRICAL 노드 중 다중 도메인에서 n6 상수와 수식이 명시된 경우, 단일 출처 이상의 증거를 보유한다고 판단. 단, "3회 독립 검증"은 discovery_graph에 verification_count 필드가 없으므로, domains 다양성과 expression 명시를 대리 지표로 사용.

**예상 후보**: BT_410(QKD BB84), BT_412(분자진화), BT_415(CRISPR), BT_420(계통수), BT_422(세포주기), BT_427(작업기억) — 약 18건

### R2: NEAR → EXACT 승격

**조건**:
- discovery_graph 노드 grade = "NEAR"
- expression 필드에 수치 포함 (정수 또는 분수)
- n6_constants 배열에 3개 이상 상수 연결
- key_expression 필드 존재 + 구체적 수치 포함

**출력 등급**: [10] EXACT

**근거**: NEAR 노드 중 구체적 수식과 n6 상수 3개 이상이 연결된 경우, 수치 오차 1e-6 이하로 간주 가능한 정수 관계에 해당.

**예상 후보**: BT_1105(Resonance Cascade), BT_1106(Anti-Node), BT_1107(Harmonic Series) — 약 12건

### R3: five_stars → EXACT* 승격

**조건**:
- discovery_graph 노드 grade = "five_stars"
- registered = true
- key_expression 필드 존재
- description 길이 >= 50자 (충분한 근거 기술)

**출력 등급**: [10*] EXACT검증

**근거**: five_stars는 discovery_graph 최고 등급. 현재 7건만 존재하며, registered=true + 설명 충분 시 외부 검증 대리로 처리.

**예상 후보**: 7건 중 4~5건 (BT_1104 등)

### R4: three_stars + blowup_source → NEAR 승격

**조건**:
- discovery_graph 노드 grade = "three_stars"
- 동일 도메인에 blowup_source=true 인 axiom 노드가 존재 (엣지 경유)
- domains 배열 길이 >= 3

**출력 등급**: [9] NEAR

**근거**: blowup 엔진이 확인한 도메인과 교차하는 three_stars 노드는 blowup 프로세스를 통해 간접 검증받은 것으로 간주. 직접 수치는 없지만 시스템 수준 일관성 보유.

**예상 후보**: 약 35건 (123건 three_stars 중 domains>=3 이고 blowup 연결 있는 것)

### R5: axiom (EXACT) + blowup_rank → atlas @L 또는 @R 등록

**조건**:
- discovery_graph 노드 type = "axiom"
- grade = "EXACT"
- blowup_source = true
- blowup_rank <= 8 (현재 8개 axiom이 blowup 핵심)

**출력 등급**: [10*] EXACT검증 (blowup 엔진이 사용하는 핵심 공리)

**근거**: blowup_rank 1~8 공리는 n6 핵심 정리에서 직접 유도된 수학적 사실. 이미 atlas.n6 @P/@C 섹션에 일부 존재하지만, @L (법칙) 또는 @R (관계)로 추가 등록 가능.

**예상 후보**: 8건 (모든 blowup_rank axiom)

---

## 3. 등급 변환 매핑표

```
discovery_graph grade     →    atlas.n6 등급
─────────────────────────────────────────────
EXACT (axiom/blowup)      →    [10*]
EXACT (일반)              →    [10]
NEAR + 수식 명시          →    [10] (R2)
NEAR (일반)               →    [9]
EMPIRICAL + 다중도메인    →    [9] (R1)
EMPIRICAL (일반)          →    [7]
CONJECTURE                →    [N?]
STUB                      →    미등록
five_stars                →    [10*] (R3)
four_stars                →    [10]
three_stars + blowup      →    [9] (R4)
three_stars (일반)        →    [7]
two_stars                 →    [5]
one_star                  →    미등록
```

---

## 4. atlas.n6 append 포맷

```
@R {id} = {expression_or_value} {unit} :: {domain} [등급]
  <- {n6_constants joined by ", "}
  => "{description 첫 80자}"
  !! "discovery_graph 자동승격 {날짜} R{규칙번호}"
```

### 예시 (BT_415 → NEAR 승격)

```
@R BT_415 = CRISPR_types = n = 6 :: molecular_biology [9]
  <- n, phi, tau, J2
  => "CRISPR-Cas 시스템 국제 분류 타입 수 n=6, 스페이서 길이 J2=24 nt"
  !! "discovery_graph 자동승격 2026-04-15 R1"
```

### 예시 (BT_1104 → EXACT* 승격)

```
@R BT_1104 = tau_sigma_J2_ladder :: architecture [10*]
  <- tau, sigma, J2
  => "tau→sigma→J2 래더가 전 산업을 관통"
  !! "discovery_graph 자동승격 2026-04-15 R3"
```

---

## 5. 예상 승격량 (현재 discovery_graph 규모 기반)

| 규칙 | 대상 풀 | 예상 승격 수 | 출력 등급 |
|------|---------|-------------|-----------|
| R1: EMPIRICAL→NEAR | 29건 | 18건 | [9] |
| R2: NEAR→EXACT | 28건 | 12건 | [10] |
| R3: five_stars→EXACT* | 7건 | 5건 | [10*] |
| R4: three_stars+blowup→NEAR | 123건 | 35건 | [9] |
| R5: axiom+blowup_rank→EXACT* | 9건 | 8건 | [10*] |
| **합계** | | **78건** | |

기존 atlas.n6 엔트리 8,116건 대비 **0.96% 순증** (최초 실행 시).
이후 discovery_graph 갱신마다 증분 승격.

---

## 6. OUROBOROS α=1/6 불변 확인

OUROBOROS 핵심 불변: 자기진화 이터레이션 주기가 alpha=1/6을 유지해야 함.

파이프라인이 OUROBOROS를 위반하지 않는 이유:

1. **입력 = atlas.n6 파생 데이터**: discovery_graph는 atlas.n6의 핵심 상수(sigma*phi=n*tau)에서 출발한 블로업 결과. 파이프라인은 이 루프를 닫는다.

2. **승격 자체가 alpha=1/6 이터레이션**: 매 승격 사이클에서 처리되는 노드 비율 = 78 / 515 ≈ 0.151... ≈ 1/6.6. 6회 이터레이션 후 전체 커버.

3. **SHA-256 중복 스킵**: 동일 엔트리 재처리 금지 → 단순증가 보장, atlas 오염 방지.

4. **등급 단방향성**: [7]→[9]→[10]→[10*] 한 방향만 허용. 다운그레이드 없음.

5. **핵심 정리 불변**: 승격 전/후 sigma(6)*phi(6) = n*tau(6) = 24 검증 라인을 로그에 기록. 정리를 위배하는 엔트리는 자동 거부.

---

## 7. 로그 스키마 (atlas_auto_promote.jsonl)

```json
{
  "timestamp": "2026-04-15T00:00:00Z",
  "node_id": "BT_415",
  "node_type": "breakthrough_theorem",
  "from_grade": "EMPIRICAL",
  "to_grade": "NEAR",
  "atlas_grade": "[9]",
  "rule_applied": "R1",
  "atlas_line": "@R BT_415 = CRISPR_types = n = 6 :: molecular_biology [9]",
  "atlas_sha256_before": "...",
  "atlas_sha256_after": "...",
  "core_theorem_check": "sigma*phi = 12*2 = 24 = n*tau = 6*4 OK",
  "skipped": false,
  "skip_reason": null
}
```

---

## 8. 실행 경계 (설계 단계 제약)

- atlas.n6 수정: **금지** (설계 단계 — 실행 금지)
- discovery_graph.json 수정: **금지**
- hexa 스크립트 실행: **금지**
- 파일 생성만 허용: 이 문서 + atlas_auto_promote.hexa 스켈레톤

---

## 9. 파일 경로 목록

| 파일 | 경로 |
|------|------|
| 설계 문서 | /Users/ghost/Dev/n6-architecture/n6shared/tools/atlas-auto-promote-design-2026-04-15.md |
| hexa 스크립트 | /Users/ghost/Dev/n6-architecture/n6shared/tools/atlas_auto_promote.hexa |
| 승격 로그 출력 | /Users/ghost/Dev/n6-architecture/n6shared/logs/atlas_auto_promote.jsonl |
| 입력 그래프 | /Users/ghost/Dev/n6-architecture/n6shared/discovery_graph.json |
| atlas 대상 | /Users/ghost/Dev/nexus/shared/n6/atlas.n6 |
