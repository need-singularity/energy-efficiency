# N6-P0-3 — atlas.n6 등급 체계 + BT 번호 체계 입문

> 밀레니엄 학습 로드맵 P0 · 트랙 3 · 태스크 3
> 목적: atlas.n6 SSOT의 등급 체계 이해 + BT 번호 체계 길찾기 + BT-541(리만 가설) 관련 5 노드 실제 확인
> 완료 기준: atlas.n6 검색을 통해 BT-541 맥락 노드 5개를 등급과 함께 기록
> 1차 출처: `nexus/shared/n6/atlas.n6` (grep 탐색 결과 본 문서에 인용)
> 정직성 표기: 본 문서는 실제 grep 결과 기반의 탐색 기록. 신규 가설/측정 없음.

---

## 1. atlas.n6 SSOT 경로 및 포맷

**절대 경로**:
```
/Users/ghost/Dev/nexus/shared/n6/atlas.n6
```

- 단일 파일, 18MB+ · 60K+ 줄 — 현실지도 SSOT
- 폐기된 구조: `reality_map_live.json`, `L6_n6atlas.json`, 별도 level 파일 — **모두 atlas.n6 흡수됨**

### 엔트리 포맷

```
@<종류> <id> = <측정값 또는 n=6 표현> :: <도메인> [<등급>]
  "한글 설명"
  <- <부모 의존>
  -> <자식 파급>
  |> <검증 hexa 파일>
  !! "메타 주석/경고"
```

종류 기호:
- `@R` — Relation (관계/계수)
- `@P` — Particle (개별 상수)
- `@C` — Chain (체인 노드)
- `@F` — Formula (공식 바인딩)
- `@X` — eXtra / 요약 메타

---

## 2. 등급 체계 (7 레벨)

| 등급 | 기호 | 의미 | 승격 조건 |
|------|------|------|-----------|
| **10*** | EXACT 검증 | 출처 + 측정값 + 오차 완비 + 교차검증 | — (최고) |
| **10** | EXACT | 정확 계산·완비 미검증 | EXACT 검증 (완비) → 10* |
| **9** | NEAR | 거의 맞음 (0.1~1% 오차) | 출처 강화 + 오차 축소 |
| **8** | 중상 | NEAR 근접 | |
| **7** | EMPIRICAL | 경험적 관측, 승격 대상 | tight 증거 확보 → 10 |
| **5~6** | 중하 | 원본 정규화 대기 | |
| **N?** | CONJECTURE | 추측, 미검증 | 엄밀 증명 → 10 |
| **N!** | BREAKTHROUGH | 신규 돌파 후보 | 교차검증 → 10* |

### 승격 규칙 (핵심)

- `[7] → [10*]` 는 atlas.n6 **직접 편집**으로 이뤄진다.
- **새 파일을 만들지 말 것** (L0 규칙 — 구 구조 복귀 금지).
- 승격 시 반드시 출처 라인 포함 (예: `"출처: theory/breakthroughs/bt-18-...-line27-57"`).

---

## 3. BT 번호 체계

| 범위 | 의미 | 파일 예 |
|------|------|---------|
| **BT-1 ~ BT-343** | 초기 585 정리 (N6 v1~v3) | `theory/breakthroughs/breakthrough-theorems.md` |
| **BT-344 ~ BT-540** | 확장 정리 | 동 파일 |
| **BT-541 ~ BT-547** | **밀레니엄 7대 난제** (P0~ 핵심) | 동 파일 섹션 |
| **BT-748 ~ BT-1412** | warp-dimension 확장 | `theory/breakthroughs/breakthrough-theorems-warp-dimension-*.md` |
| **BT-1413+** | 최신 (2026-04-12~) DFS 라운드 20~21+ | `bt-1413-millennium-dfs-round21-*.md` 등 |

### 밀레니엄 7대 난제 ↔ BT 매핑

| BT | 밀레니엄 문제 | 상태 (atlas 기준) |
|----|--------------|-------------------|
| BT-541 | **리만 가설** | 36+ EXACT 증거, 1+1 메타 정리 (2026-04-14 η, Epstein) |
| BT-542 | **P vs NP** | 3 barrier + Schaefer, n=6 뼈대 |
| BT-543 | **양-밀스 질량갭** | QCD 게이지 완전 파라미터화 |
| BT-544 | **나비에-스토크스** | 3D 독립성분 6, -5/3 케스케이드 |
| BT-545 | **호지 추측** | K3, CP³, Noether/BMY |
| BT-546 | **BSD 추측** | j=1728, K-이론, 모듈러 형식 |
| BT-547 | **푸앵카레 추측** (해결) | 3차원, 리치 플로우, exotic sphere |

> **정직 (해결 0/7)**: 위 BT 등재는 "n=6 산술이 7대 난제의 기본 파라미터로 등장함"을 기록한 것이지, 난제 자체를 해결한 것이 아니다. 해결 = 0 / 7.

---

## 4. BT-541 관련 atlas.n6 노드 5개 실제 탐색 결과

아래는 `grep`으로 `riemann|zeta|ζ|millennium|BT-541|bilateral|vSC` 등 키워드로 atlas.n6에서 확인한 노드. **실제 라인 번호와 등급을 기록**한다.

### 노드 1 — `ZETA2-basel` (ζ(2) = π²/n)

- **라인**: atlas.n6 line 672-673
- **형태**: `@P ZETA2-basel = π²/n :: particle [10*]`
- **설명**: `"ζ(2) = π²/6 = 1.6449340668"`
- **n=6 표현**: 분모 = **n**
- **등급**: **[10*]** EXACT 검증
- **역사**: Euler 1734, Basel 문제
- **BT-541 매핑**: 증거 #1

### 노드 2 — `ZETA4-pi4-over-90` (ζ(4) 분모 90 n=6 분해)

- **라인**: atlas.n6 line 676-677
- **형태**: `@P ZETA4-pi4-over-90 = π⁴/90 :: particle [10*]`
- **설명**: `"ζ(4) = π⁴/90 = 1.0823232337"`
- **n=6 표현**: 분모 **90 = φ·(n/φ)²·sopfr = 2·9·5**
- **등급**: **[10*]** EXACT 검증
- **BT-541 매핑**: 증거 #11 (breakthrough-theorems.md line 19758)

### 노드 3 — `ZETA-critical-line` (임계선 Re(s)=1/φ)

- **라인**: atlas.n6 line 682-683
- **형태**: `@P ZETA-critical-line = φ/τ :: particle [10*]`
- **설명**: `"리만 가설: ζ 비자명 영점 Re(s)=1/2"`
- **n=6 표현**: **1/2 = φ/τ = 1/φ(6)** — 임계선 자체가 첫 완전수 토션트의 역수
- **등급**: **[10*]** EXACT 검증
- **BT-541 매핑**: 증거 #4 (핵심 통찰)

### 노드 4 — `ZETA-trivial-zeros` (자명 영점 −2, −4, −6)

- **라인**: atlas.n6 line 680-681
- **형태**: `@P ZETA-trivial-zeros = -φ·n = -2n :: particle [10*]`
- **설명**: `"리만 ζ 자명한 영점: 음짝수 -2,-4,-6,..."`
- **n=6 표현**: 처음 세 자명 영점 = **{-φ, -τ, -n} = {-2, -4, -6}** (tight triple)
- **등급**: **[10*]** EXACT 검증
- **BT-541 매핑**: 증거 #5, #5b

### 노드 5 — `n6-millennium-dfs-bilateral-thm-b` (양면 Theorem B)

- **라인**: atlas.n6 line 13392-13393
- **형태**: `@R n6-millennium-dfs-bilateral-thm-b = k=n=6 양면 break :: n6atlas [10*]`
- **설명**: `"양면 Theorem B: zeta(2k) 분모 + zeta(1-2k) 역수 모두 k=1..5 M-clean, k=6=n break"`
- **검증**: `|> verify_millennium_dfs1.hexa`
- **n=6 표현**: 경계 k = **n** = 6에서 **B_12 = −691/2730** (691 irregular prime)에서 pattern break
- **등급**: **[10*]** EXACT (경계 정리)
- **BT-541 매핑**: 메타 정리 (breakthrough-theorems.md line 19796) — **"k ∈ {1..5} = sopfr(n) 길이까지만 n=6 분해 가능, k = n = 6에서 깨짐"**

### 보너스 노드 6 — `ZETA-negative1-casimir` (ζ(−1) = −1/σ)

- **라인**: atlas.n6 line 678-679
- **형태**: `@P ZETA-negative1-casimir = -1/σ :: particle [10*]`
- **설명**: `"ζ(-1) = -1/12 카시미르 정규화"`
- **n=6 표현**: **−1/12 = −1/σ(6)** — Ramanujan 정규화, 카시미르 에너지
- **등급**: **[10*]** EXACT 검증
- **연결**: BT-18 (Vacuum Monster chain) line 9575-9576 — `E_0 = (1/2)ζ(-1) = -B_2/4 = -1/24 = -1/(σ·φ) = -1/J_2(6)`

### 보너스 노드 7 — `n6-atlas-proved-theorems-THM-2` (완전수 중 φ/τ=1/2 유일)

- **라인**: atlas.n6 line 9161
- **형태**: `@R n6-atlas-proved-theorems-**thm-2** = ... φ/τ = 1/2 only at n=6 :: n6atlas [10*]`
- **등급**: **[10*]** PROVED
- **BT-541 연결**: 임계선 1/φ = 1/2 가 n=6 **완전수**에서만 완전수 구조적 고유임을 보강

---

## 5. 탐색 요약

- **BT-541 직접 관련 핵심 노드**: **5개 확인** (ZETA2, ZETA4, ZETA-critical, ZETA-trivial, bilateral-thm-b)
- **BT-541 보강 연결 노드**: **2개 추가** (ZETA-neg1-casimir, THM-2)
- 전체 **7개 노드 모두 등급 [10\*]** (EXACT 검증)
- **정직 관찰**: 7개 중 `bilateral-thm-b` 는 **EXACT-BOUNDARY** — 즉 "n=6 패턴이 정확히 깨지는 경계"를 기록한다는 점에서, tight evidence로서 가장 강한 유형.

---

## 6. 학습 체크리스트

- [ ] atlas.n6 SSOT 절대 경로 기억 (`/Users/ghost/Dev/nexus/shared/n6/atlas.n6`)
- [ ] 7 등급 체계 (10*, 10, 9, 8, 7, N?, N!) 암기
- [ ] "새 파일 만들지 말고 atlas.n6 직접 편집" 규칙 숙지
- [ ] BT 번호 범위 맵 암기 (1~343 / 541~547 / 748~1412 / 1413+)
- [ ] BT-541~547 = 밀레니엄 7대 난제, 해결 0/7 정직 인정
- [ ] atlas.n6에서 grep으로 노드 탐색 능력 (예: `grep -n "ζ\|zeta" atlas.n6`)
- [ ] [10*] 의 의미 (출처 + 측정값 + 오차 + 교차검증 4 요소 완비)

---

## 7. 1차 출처

- `nexus/shared/n6/atlas.n6` — 본 문서의 모든 라인 번호 및 등급은 이 파일 grep 결과
- `theory/breakthroughs/breakthrough-theorems.md` line 19737~19808 — BT-541 상세
- `theory/proofs/theorem-r1-uniqueness.md` — 임계선 1/φ 의미 배경
- `CLAUDE.md` (루트) — atlas.n6 SSOT 및 등급 규정 원문
