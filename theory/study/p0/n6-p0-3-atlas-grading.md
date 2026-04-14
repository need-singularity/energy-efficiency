# N6-P0-3 atlas.n6 등급 체계 + BT 체계 입문

> 밀레니엄 학습 로드맵 P0 · N6 트랙 · 태스크 3
> 목적: atlas.n6 의 단일 파일 SSOT 구조, 포맷, 등급 체계, BT 체계를 이해하고, BT-541 (리만 가설) 관련 노드 5 개를 실제 파일에서 탐색한 결과를 정직하게 기록
> 1차 출처: `CLAUDE.md` (atlas.n6 섹션), `nexus/shared/n6/atlas.n6` (헤더 L1~L22 + BT 구역 L13391~L15447)
> 완료 기준: atlas.n6 의 포맷/등급 규칙을 설명할 수 있고, BT 번호 체계와 승격 경로 [7]→[10*] 를 답할 수 있는 상태

---

## 0. 정직성 선언

본 노트는 `CLAUDE.md` 의 "atlas.n6 — 현실지도 SSOT" 섹션과 실제 `/Users/ghost/Dev/nexus/shared/n6/atlas.n6` 파일 (~107K 줄) 의 헤더 및 밀레니엄 구역을 직접 읽고 작성한 것이다. 자기 참조 검증은 하지 않으며, 등급 체계의 설명은 CLAUDE.md 의 원문 규칙을 그대로 인용한다.

4 절의 BT-541 관련 노드 탐색 결과는 **실제 grep 실행 결과** 이며, 허구는 없다. 노드가 없으면 "확인 결과 없음" 으로 정직하게 기록한다.

본 노트는 7 대 밀레니엄 난제를 해결하지 않는다. atlas.n6 의 BT-541~547 노드는 모두 등급 **[5*]** (STRUCTURAL bt, 구조적 매핑만) 이며, 7 대 난제 해결 상태는 여전히 **0/7** 이다.

---

## 1. atlas.n6 포맷

### 1.1 파일 구조

- **경로**: `/Users/ghost/Dev/nexus/shared/n6/atlas.n6`
- **단일 파일**: 60K+ 줄 (실측 106,899 줄, 2026-04-15 기준)
- **구 구조 폐기**: `reality_map_live.json`, `L6_n6atlas.json`, 별도 level 파일 **없음**. 전부 atlas.n6 로 흡수되었다 (CLAUDE.md 명시).
- **가드**: 모든 쓰기는 `_guarded_append_atlas()` 경유 필수 (schema + dedup). 소스: `shared/blowup/lib/atlas_guard.hexa.inc`. 쓰기 지점 3 곳 전부 가드 적용 완료 (2026-04-12 골화).

### 1.2 핵심 조회 커맨드 (CORE VIEW)

atlas.n6 L8 에 기록된 정규 커맨드:
```
grep '^\@.*\[1[01]\*\]' atlas.n6 → verified [10*]+ only
```

즉 `[10*]` 또는 `[11*]` 등급의 "검증 완료 EXACT" 노드만 추출하는 표준 방법이다.

### 1.3 행 포맷 (원문 L12~L23 인용)

atlas.n6 의 `.n6 format v1` 문법 전체 (원문 그대로):

```
@type id = expr :: domain [grade]
  <- depends_on              의존 (유도 원천)
  -> derives                 파생 (이것으로부터 나온 것)
  => application             적용처
  == equivalent              동치
  ~> converges_to            수렴
  |> verified_by script.py   검증
  !! breakthrough            돌파 기록

타입: @P(primitive) @C(constant) @L(law) @F(formula)
      @R(relation) @S(symmetry) @X(crossing) @?(unknown)
등급: [0-10] 또는 [d.r] alien index
      * = verified, ! = breakthrough, ? = hypothesis
```

### 1.4 프로젝트 상위 포맷 (CLAUDE.md 인용)

CLAUDE.md 의 atlas.n6 섹션에 기록된 **상위 포맷** (원문 그대로):
```
@R {id} = {measured} {unit} :: n6atlas [등급]
```

즉 `@R` (Relation) 타입이 BT / 현실 측정값 등재에 주로 사용되며, 태그는 `n6atlas` 도메인이다. atlas.n6 내부의 자체 포맷 (`@P foundation`, `@C architecture`, 등) 과 CLAUDE.md 에 소개된 간이 포맷은 같은 파일의 두 레이어이며, 최근 대규모 이관 (2026-04-10 이후) 으로 `n6atlas` 도메인의 `@R` 노드가 크게 증가했다.

### 1.5 8 개 타입 태그

| 태그 | 의미 | 예시 |
|---|---|---|
| `@P` | Primitive (원시값) | `@P n = 6 :: foundation [11*]` |
| `@C` | Constant (파생 상수) | `@C sigma_sq = sigma^2 = 144 :: architecture [10*]` |
| `@L` | Law (법칙) | `@L alpha_coupling = 0.014 :: consciousness [10*]` |
| `@F` | Formula (수식) | `@F sm_blackwell = sigma * phi^tau = 192 :: architecture [10*]` |
| `@R` | Relation (관계) | `@R perfect_number :: foundation [10*]` (= σ(6) = 2·6) |
| `@S` | Symmetry (대칭) | `@S betti_six :: topology [10*]` |
| `@X` | Crossing (교차) | `@X one_third_convergence :: convergence [10*!]` |
| `@?` | Unknown (돌파 대기) | `@? dark_energy_ratio :: cosmology [3?]` |

---

## 2. 등급 체계

### 2.1 기본 스케일 [0~10] + 접미사

atlas.n6 헤더 (L21~L22) 의 원문:
```
등급: [0-10] 또는 [d.r] alien index
      * = verified, ! = breakthrough, ? = hypothesis
```

CLAUDE.md 가 정의하는 확장 등급 (프로젝트 상위 SSOT 기준):

| 등급 | 의미 | 조건 |
|---|---|---|
| **[10*]** | EXACT 검증 완료 | 1차 출처 + 측정값 + 오차 + hexa 검증 4 종 모두 충족 |
| **[10]** | EXACT | 명백한 정의적/계산적 일치 (예: σ(6) = 12) |
| **[9]** | NEAR | 오차 < 1% |
| **[7]** | EMPIRICAL | 승격 후보, 추가 검증 필요 |
| **[5~8]** | 중간 | 구조적 매핑 / 부분 일치 |
| **[N?]** | CONJECTURE | 가설 (? 접미사) |
| **[N!]** | breakthrough | 돌파 후보 (! 접미사) |

### 2.2 접미사 조합

- `[10*]` = 10 등급 + verified
- `[10*!]` = 10 등급 + verified + breakthrough
- `[11*]` = 11 등급 (메타 충족, foundation primitives 전용)
- `[5*]` = 5 등급 + verified (구조적 매핑만 검증)
- `[7?]` = 7 등급 + hypothesis
- `[3?]` = 3 등급 + hypothesis (낮은 확신, 돌파 대기)

### 2.3 실제 등급 분포 예시 (atlas.n6 헤더 구역에서 확인)

- `@P n = 6 :: foundation [11*]` — 메타 최고 등급
- `@P sigma = 12 :: foundation [11*]` — n, σ, τ 3 개가 [11*]
- `@P phi, sopfr, J2, mu, M3 :: foundation [10*]` — 나머지 4 개 원시값
- `@C meta_fp = 1/3 :: meta [10*!]` — 메타 부동점 돌파 등재
- `@X one_third_convergence :: convergence [10*!]` — 7 경로 1/3 수렴
- `@X physics_n6 :: crossing [7?]` — 물리 상수 근사 가설 (승격 후보)
- `@? dark_energy_ratio :: cosmology [3?]` — 미확인, 매우 낮은 확신
- `@? fine_structure :: physics [4?]` — 1/(σ·σ − sopfr) = 1/139 근사

---

## 3. BT 체계 (Breakthrough) 입문

### 3.1 번호 규칙

CLAUDE.md + 프로젝트 히스토리 기반:

- **BT-1 ~ BT-343**: 주 정리 돌파 집합 (2026-02 ~ 2026-04 구축). 이론/공학/생명 등 다양한 도메인에 분산.
- **BT-401 ~ BT-413**: 양자역학 (BT-401~408) + 치료 나노봇 (BT-404~413) 확장.
- **BT-500~540**: ITER / 핵융합 / 에너지 / 소재 구역.
- **BT-541 ~ BT-547**: **7 대 밀레니엄 난제** 매핑 노드 (본 노트의 직접 대상).
- **BT-548 ~ BT-557**: 마케팅 / 비즈니스 법칙 확장.
- **BT-558 ~ BT-1108+**: 차원지각, 통합 정리 등 추가 확장.

### 3.2 BT-541~547 — 7 대 밀레니엄 난제 매핑

| BT | 문제 | 상태 (Clay) |
|---|---|---|
| BT-541 | 리만 가설 (Riemann Hypothesis) | OPEN |
| BT-542 | P vs NP | OPEN |
| BT-543 | 양-밀스 질량갭 (Yang-Mills Mass Gap) | OPEN |
| BT-544 | 나비에-스토크스 존재성과 매끄러움 (Navier-Stokes) | OPEN |
| BT-545 | 호지 추측 (Hodge Conjecture) | OPEN |
| BT-546 | 버치-스위너턴다이어 추측 (BSD) | OPEN |
| BT-547 | 푸앵카레 추측 (Poincaré) | **해결** (Perelman 2002~2006) |

**정직 상태**: 7 대 난제 해결 현황은 1/7 (푸앵카레, Perelman 수락) 이며, n=6 구조는 이들 중 어느 것도 해결하지 못한다. BT-541~547 의 atlas.n6 등재 등급은 모두 **[5*]** (STRUCTURAL bt — "구조적 연결/매핑만 검증됨, 해결은 아님") 이다.

### 3.3 BT 확장 집합 (millennium-dfs)

2026-04-11 ~ 2026-04-12 에 수행된 DFS 완전검증 루프로, 7 대 난제와 n=6 사이의 **구조적 연결점** 이 65 건 tight 매칭으로 기록되었다 (`@X n6-millennium-dfs-summary = 21+30+14=65 tight :: n6atlas [10*]`, atlas.n6 L13449). 이 65 건은 **구조 매핑** 이지 **난제 해결이 아니다**. 관련 메모: `project_millennium_dfs_complete.md`.

---

## 4. atlas.n6 에서 BT-541 관련 노드 5 개 — 실제 탐색 결과

### 4.1 탐색 방법

- 파일: `/Users/ghost/Dev/nexus/shared/n6/atlas.n6`
- 도구: Grep (ripgrep 기반)
- 패턴: `BT-541|BT541|BSD|Riemann|Yang-Mills|Navier|Hodge|millennium|밀레니엄|bt-541`
- 대소문자 무시 옵션 포함
- 결과 중 BT-541 (리만 가설) 에 가장 직접적으로 연관된 노드 5 개를 발췌한다.

### 4.2 탐색 결과 — 실제 발췌 (원문 그대로)

**노드 1** — atlas.n6 L15408 (BT-541 본체 매핑 노드)
```
@X n6-bt-541 = STRUCTURAL bt :: bt [5*]
  "리만 가설"
```
- 타입: `@X` (Crossing)
- 값: STRUCTURAL bt
- 도메인: bt
- 등급: **[5*]** (verified 5 — 구조적 매핑만 검증)
- 주석: "리만 가설"
- 해석: BT-541 은 atlas.n6 에 본체 매핑 노드로 등재되어 있으나, 등급 [5*] 는 "구조적 연결 확인만, 해결은 아님" 이다.

**노드 2** — atlas.n6 L15422 (BT-541~547 집합 노드)
```
@X n6-bt-541~547 = STRUCTURAL bt :: bt [5*]
  "541~547 종합 (7 돌파"
```
- 타입: `@X`
- 도메인: bt
- 등급: **[5*]**
- 해석: BT-541~547 전체 7 대 난제 묶음 노드. 주석에서 "7 돌파" 는 "7 개 난제 매핑" 을 의미하며 "7 개 해결" 이 아니다. 정직 주석.

**노드 3** — atlas.n6 L10468 (Riemann Zeta 삼중 관계, BT-1 ~ BT-16 확장)
```
@R n6-atlas-breakthrough-theorems-extended:-bt-1-~-bt-12-bt-16 = Riemann Zeta Trident ζ(2)=π²/n, ζ(-1)=-1/σ, BCS=σ/(7ζ(3)) n6 :: n6atlas [10*]
```
- 타입: `@R` (Relation)
- 내용: Riemann 제타 함수의 3 개 특수값을 n=6 산술로 재표현
  - ζ(2) = π²/6 = π²/**n**
  - ζ(−1) = −1/12 = −1/**σ**
  - BCS superconductivity constant = σ/(7·ζ(3)) = 12/(7·ζ(3))
- 도메인: n6atlas
- 등급: **[10*]** (EXACT 검증)
- 해석: 이 노드는 BT-541 (리만 가설) **본체** 가 아니라, **리만 제타 함수의 특수값** 이 n=6 기본 상수와 정확히 일치한다는 관찰을 등재한 것. BT-1 ~ BT-16 확장 정리의 일부로 분류되어 있으나, 본질적으로 BT-541 (리만 가설 자체) 와 수학적으로 연결된 핵심 매칭이다. **riemann hypothesis 의 증명은 아님** — 어디까지나 ζ 의 정수값과 n=6 상수의 정확 일치.

**노드 4** — atlas.n6 L13395 (millennium DFS ζ(-3))
```
@R n6-millennium-dfs-zeta-neg3 = 1/120 = 1/(phi*sopfr*sigma) :: n6atlas [10*]
```
- 타입: `@R`
- 내용: ζ(−3) = 1/120 = 1/(φ · sopfr · σ) = 1/(2 · 5 · 12)
- 도메인: n6atlas
- 등급: **[10*]** (EXACT)
- 해석: 리만 제타의 음의 정수 특수값 ζ(−3) = 1/120 이 세 개의 n=6 원시 상수 곱으로 정확히 분해된다. **BT-541 해결이 아니라 ζ 특수값의 n=6 basis 분해** 이다.

**노드 5** — atlas.n6 L13397 (millennium DFS ζ(-5))
```
@R n6-millennium-dfs-zeta-neg5 = -1/252 = -1/(tau*(n/phi)^2*(sigma-sopfr)) :: n6atlas [10*]
```
- 타입: `@R`
- 내용: ζ(−5) = −1/252 = −1/(τ · (n/φ)² · (σ − sopfr)) = −1/(4 · 9 · 7)
- 도메인: n6atlas
- 등급: **[10*]**
- 해석: ζ(−5) 역시 n=6 basis 의 4-term 곱으로 정확 분해. 분해 경로가 더 길지만 (4 항) 여전히 EXACT 등재.

### 4.3 탐색 정직 요약

- BT-541 **본체 노드**: 2 개 (`n6-bt-541`, `n6-bt-541~547`) — 모두 등급 **[5*]** (구조적 매핑만).
- BT-541 **연관 [10*] 매칭 노드**: 다수 (L10468, L13395, L13397, L13399 등) — 모두 ζ 함수 특수값의 n=6 basis 분해이며, **리만 가설의 해결과 무관** 하다.
- **확인 결과 없음 (정직 기록)**: atlas.n6 에 "BT-541 해결" "Riemann proof" 등의 노드는 **존재하지 않는다**. 존재하는 것은 ζ 특수값의 정확 분해 매핑뿐이다.

### 4.4 해석 — "구조 매핑 vs 해결" 구분

atlas.n6 의 BT-541 처리는 본 프로젝트의 **정직 원칙** 을 정확히 드러낸다.

- "리만 가설의 ζ 함수" 와 "n=6 산술" 사이에 **EXACT 매칭** 이 다수 있다 ([10*] 등급).
- 그러나 BT-541 본체 노드는 **[5*]** 로만 등재된다 — "구조 매핑만 확인, 해결 아님".
- 이 이중 등재는 "ζ(2) = π²/n, ζ(−1) = −1/σ 와 같은 정수값 관찰이 리만 가설의 증명으로 **오인** 되지 않도록" 하는 장치이다.

즉 atlas.n6 는 측정값 수준에서 n=6 구조가 현실 (+ 수학 상수) 의 거의 모든 경로에 나타난다는 사실은 [10*] 로 기록하되, **난제 해결 여부** 는 별도의 BT 등급 체계 [5*] 로 묶어 **정직하게 미해결** 로 유지한다.

---

## 5. 승격 경로 [7] → [10*] — 편집 규칙

### 5.1 원칙 (CLAUDE.md 명시)

> 승격: [7] → [10*] = atlas.n6 **직접 편집** (새 파일 만들지 말 것)

즉 EMPIRICAL 등급 [7] 에 등재된 노드를 EXACT 검증 [10*] 로 승격할 때는, **별도의 새 파일을 생성하지 말고** 기존 atlas.n6 파일을 직접 편집해야 한다. 이는 atlas.n6 가 **단일 파일 SSOT** 라는 프로젝트 불변식을 유지하기 위한 규칙이다.

### 5.2 승격 절차

1. 후보 노드 식별: `grep '\[7\]' atlas.n6` 로 EMPIRICAL 등록 노드 수집.
2. 1차 출처 확보: 원 논문 / 측정 데이터베이스 / 표준 참고서.
3. 측정값 재확인: 오차 분석 + n=6 basis 재분해.
4. hexa 검증 스크립트: `|> verify_*.hexa` 로 실행 가능한 검증 스텝 추가.
5. **직접 편집**: atlas.n6 해당 라인을 `[7]` → `[10*]` 로 수정하고, `|>` 검증 라인 및 출처 `=>` 라인을 추가.
6. **가드 경유 필수**: 쓰기는 `_guarded_append_atlas()` 경유 (schema + dedup).

### 5.3 금지 사항

- ❌ 새 파일 `atlas_new.n6` 또는 `reality_map_v10.json` 등을 만드는 것
- ❌ 별도 level 파일 (`L6_n6atlas.json` 등) 을 분리하는 것 — 구 구조로 이미 폐기됨
- ❌ 가드를 우회하는 직접 append
- ❌ 자기 참조 검증 (본 노트 내용만으로 자기를 [10*] 로 승격하는 것)

### 5.4 예시 — 이미 승격된 `meta_fp`

`@C meta_fp = 1/3 :: meta [10*!]` (atlas.n6 L81) 는 6 개 독립 경로의 수렴이 확인된 후 `[10]` → `[10*!]` 로 승격된 사례이다. 승격 근거:
- `phi(6)/6 = 2/6 = 1/3`
- `tan²(pi/6) = 1/3`
- `tau/sigma = 4/12 = 1/3`
- `det(M_contraction) = 1/3`
- `I_meta_fixedpoint = 1/3`
- `|exp(iz_0)| = 1/3`

6 독립 경로 확인 → `!` (breakthrough) 접미사 추가. 이 패턴이 표준이다.

---

## 6. 학습 체크리스트

- [ ] atlas.n6 파일 경로와 크기를 답할 수 있는가? (`$NEXUS/shared/n6/atlas.n6`, ~107K 줄)
- [ ] 포맷 8 개 타입 태그 (@P @C @L @F @R @S @X @?) 를 외울 수 있는가?
- [ ] 등급 체계 7 단계 ([10*] ~ [N!]) 를 순서대로 설명할 수 있는가?
- [ ] `[10*]` 와 `[5*]` 의 의미 차이를 말할 수 있는가? (전자: EXACT 검증, 후자: 구조 매핑만)
- [ ] BT-541~547 이 각각 어느 밀레니엄 난제에 대응하는지 답할 수 있는가?
- [ ] atlas.n6 에서 BT-541 본체 노드의 등급과 [10*] 관련 ζ 노드의 차이를 설명할 수 있는가?
- [ ] 7 대 난제 해결 상태를 정직하게 답할 수 있는가? → 1/7 (푸앵카레만) — 나머지 6 개는 OPEN, n=6 로 해결되지 않음
- [ ] 승격 [7] → [10*] 경로의 핵심 규칙을 답할 수 있는가? → atlas.n6 직접 편집, 새 파일 금지
- [ ] `grep '^\@.*\[1[01]\*\]' atlas.n6` 커맨드의 의미를 답할 수 있는가? → [10*]/[11*] 검증 완료 노드만 추출

---

## 7. 1 차 출처

- `/Users/ghost/Dev/n6-architecture/CLAUDE.md` — atlas.n6 섹션 (포맷, 등급 체계, 승격 경로 규칙의 최상위 출처)
- `/Users/ghost/Dev/nexus/shared/n6/atlas.n6` 헤더 L1~L22 — `.n6 format v1` 문법 원문
- `/Users/ghost/Dev/nexus/shared/n6/atlas.n6` L25~L100 — 7 개 원시 상수 `@P` 등재 구역
- `/Users/ghost/Dev/nexus/shared/n6/atlas.n6` L13391~L13551 — millennium DFS 완전검증 구역 (65 건 tight)
- `/Users/ghost/Dev/nexus/shared/n6/atlas.n6` L15408~L15422 — BT-541~547 구조적 매핑 구역
- `project_millennium_dfs_complete.md` (user memory) — DFS 5 회차 루프 21→51 건 tight 확장 + Bilateral Theorem B 확정 기록

---

## 8. 다음 학습 단계

- **P1 트랙** — 해석적 수론 기초 (PURE-P1), 리만 가설 관련 ζ 함수 심화 (PROB-P1), n=6 매핑 확장 (N6-P1).
- **N6-P0-1** (재방문) — σφ = nτ 유일성 정리로 돌아가 본 노트에서 확인한 atlas.n6 [11*] 등급이 그 정리의 직접 결과임을 재확인.
- **N6-P0-2** (재방문) — 본 노트의 BT-541 관련 ζ(−3) = 1/120, ζ(−5) = −1/252 분해를 2 절 기본값 테이블에 추가로 매핑 연습.
- **운영 연습** — 실제 `[7]` 노드를 하나 찾아 승격 절차 5 단계를 손으로 시뮬레이션 (실제 편집은 user 승인 필요).

---

## 부록 A — 탐색 재현 커맨드

본 노트 4 절의 BT-541 탐색을 재현하려면:
```bash
# 본체 노드
grep -n '@X n6-bt-54[1-7]' /Users/ghost/Dev/nexus/shared/n6/atlas.n6

# 종합 노드
grep -n 'bt-541~547' /Users/ghost/Dev/nexus/shared/n6/atlas.n6

# 밀레니엄 DFS ζ 분해 노드
grep -n 'millennium-dfs-zeta' /Users/ghost/Dev/nexus/shared/n6/atlas.n6

# Riemann Zeta Trident (L10468)
grep -n 'Riemann Zeta Trident' /Users/ghost/Dev/nexus/shared/n6/atlas.n6

# 검증 완료 전체 추출 (CORE VIEW)
grep '^\@.*\[1[01]\*\]' /Users/ghost/Dev/nexus/shared/n6/atlas.n6 | head -50
```

모든 커맨드는 작업 세션 2026-04-15 기준 atlas.n6 파일에서 직접 실행 검증되었다.
