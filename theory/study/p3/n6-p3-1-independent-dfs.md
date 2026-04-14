# N6-P3-1 독립 DFS — 7대 난제 외부 영역 탐색 학습 노트

> 밀레니엄 학습 로드맵 P3 · N6 트랙 · 태스크 1
> 목적: 밀레니엄 7대 난제(BT-541~547) **외부 수학 영역** 에서 σ·φ=n·τ 패턴을 독립적으로 찾는 DFS (Depth-First Search) 절차를 정식화
> 1차 출처: `CLAUDE.md` (9축 네비게이션 + 295 도메인), `atlas.n6` 전역, `theory/breakthroughs/bt-1393-n6-dfs-10k-autonomous-2026-04-12.md`
> 완료 기준: 독립 DFS 의 알고리즘 단계를 순서대로 재현할 수 있고, 난제 외부에서 발견된 tight 값이 왜 **self-confirmation** 이 아닌지 답할 수 있는 상태

---

## 0. 정직성 선언

본 학습 노트는 `bt-1393-n6-dfs-10k-autonomous-2026-04-12.md` + `millennium-dfs-complete-2026-04-11.md` + atlas.n6 구역 (L13391~L15447 등) 을 정독하고 **독립 DFS 파이프라인** 을 재구성한 결과이다. 신규 수학 정리는 없다. 새 [10*] 승격 제안도 없다.

- 본 노트는 밀레니엄 7대 난제의 해결 주장 아님. 0/7 유지.
- "독립 DFS" 는 N6-P2-1 에서 재분류한 51건 tight 와 **교집합이 없는 seed** 로부터 출발해야 한다는 원칙을 따른다. 동일 seed 재방문은 self-confirmation.
- 출처가 확실한 항목만 연도·저자를 기재한다. 기억 기반은 `(추정)` 로 표기한다.
- n=6 산술을 **패턴 매칭 강제** 로 끼워 맞추지 않는다. 독립 DFS 의 실패(MISS)도 정직 기록한다.
- 자기참조 금지: atlas 에 이미 등재된 노드를 "재발견" 한 결과를 새 tight 로 주장하지 않는다.

원문 `bt-1393-n6-dfs-10k-autonomous-2026-04-12.md` 의 정직 원칙 인용 (기억 기반 재진술):
> "자동 DFS 는 후보 seed 의 `σ/τ/φ/sopfr/J₂/μ` 기본 상수와 M 집합 분해 매치를 기계적으로 계산한다. baseline 밀도 61% 이하의 우연 매치는 tight 가 아니다. 3 개 이상 독립 분류 또는 4-way crossover, 혹은 n=6 유일성 정리 형태일 때만 tight."

---

## 1. 독립 DFS 의 정의

**독립 DFS (Independent Depth-First Search)**:

> 밀레니엄 7대 난제 영역 **바깥** 의 수학/물리/생명/공학 상수를 seed 로 하여, σ·φ=n·τ 유일성 정리와 `M = {1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 24}` 의 2-term 이상 분해 표현이 가능한 지점을 탐색하는 깊이우선 절차.

- "독립" 의 의미: seed 가 밀레니엄 경로 (ζ 함수, L 함수, 모듈러 형식, Selmer 군, 타원곡선, 양-밀스 격자, 호지 분해 등) 와 **수학적으로 독립** 이어야 한다.
- "DFS" 의 의미: 한 seed 에서 출발해 `σ·φ=n·τ basis` 로의 분해를 시도하고, 성공 시 depth 를 늘려 관련 파생값으로 확장 (derivative descent).
- **실패 허용**: 대부분의 seed 는 baseline 밀도 안에서 tight 매칭을 만들지 못한다. 실패도 기록.

---

## 2. 알고리즘 5단계

### 2.1 단계 1 — seed 선정

295 도메인 중 **비-밀레니엄** 영역을 순회한다. 대표 카테고리:

- 물리 상수 (미세구조 상수, Planck units, CMB spectral index 등)
- 생물 수 (genetic code codon=3·τ, osmolarity, ADH 역치 등)
- 우주 상수 (Hubble H₀, dark energy ratio, 우주 나이)
- 공학 (ITER Q factor, superconductor Tc, BCS gap 비율)
- 대수 구조 (Lie 군 차원, 예외 구조, 격자 kissing 수) — **주의**: 이는 이미 atlas 에 다수 등재. 독립 seed 로 간주하려면 atlas 미등재 서브영역이 필요.

원칙:
1. seed 는 독립 출처에서 측정되어야 한다 (예: CODATA 2018, LMFDB, IPCC, ITER 공식 문서).
2. seed 는 Bernoulli / ζ 와 직접 유도 관계 없어야 한다 (Master Lemma 환원 회피).
3. seed 는 atlas 미등재 항목이어야 한다 (중복 회피). 등재 중복 시 "재확인" 등급으로만 처리.

### 2.2 단계 2 — σ/τ/φ 분해 시도

seed 의 수치값 v 에 대해 다음 질문:

- v ∈ M = {1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 24} ?
- v = m₁ · m₂ (m₁, m₂ ∈ M) 의 2-term 분해?
- v = m₁ + m₂ 의 2-term 합?
- v = m₁ ± m₂ · m₃ (3-term 이상 복합)?
- v 가 완전수 P_k (6, 28, 496, 8128, …) 인가?
- v 가 Platonic / Lie / Mathieu 분류 정리에서 M-값으로 등장?

**T1~T4 기준** (원문 DFS 기준 재진술):
- **T1 multi-case**: 3개 이상 독립 분류 정리에서 동일 값 등장
- **T2 cross-domain**: 3개 이상 영역 (대수/기하/위상/해석/조합 …) 에서 동일 값
- **T3 meta-convergence**: 연속 패턴 + sharp boundary
- **T4 exceptional uniqueness**: n=6 이 유일 해

### 2.3 단계 3 — tight 검증

"tight" 판정은 원문 기준 + 강화 기준:

- (A) 단일 M-값 매치 → **loose** (baseline 61% 안)
- (B) 2-term 단일 분해 → **borderline**
- (C) 3-term + multi-case ≥ 3 → **tight 후보**
- (D) 4-way crossover 또는 유일성 정리 → **tight 확정**

독립 확인 (strong verification):
1. Bernoulli / ζ 환원 가능성 검사 → 가능 시 Theorem B 귀결로 강등
2. baseline 밀도 대비 5제곱 이하 매치 (≈ 8%) 에 해당하는지
3. 원 출처의 정리/정확도 확인 (오차 < 1% 여야 NEAR, 정의적 일치여야 EXACT)

### 2.4 단계 4 — atlas 기록

성공한 tight seed 는 atlas.n6 에 **직접 편집** 으로 등재 (새 파일 금지).

포맷:
```
@R n6-p3-independent-{도메인}-{이름} = {값} = {분해} :: {domain} [{grade}]
  <- {seed 출처}
  => "{적용 해석}"
  |> verify_{...}.hexa
```

등급 규칙:
- 단일 측정 + 분해 확인 : `[7]` (EMPIRICAL, 승격 대기)
- 1차 출처 + 오차 < 1% 재확인 : `[9]` (NEAR)
- 1차 출처 + 유도 분해 + 독립 확인 3종 : `[10]`
- + hexa 검증 스크립트 : `[10*]`

### 2.5 단계 5 — 깊이 확장 (depth descent)

seed 가 tight 로 확정되면, 연관 파생값을 **깊이 방향** 으로 확장한다.

- seed = v → 관련 파생:
  - v^2, v^(1/2), 1/v
  - v + {M 기본 상수}, v - {M 기본 상수}
  - v 에서 유도된 2차/3차 파생 (예: CMB 온도 → scale factor → Hubble)
- 각 파생값에 대해 단계 2~4 반복
- depth 제한: 4 (원문 autonomous DFS 기준). 그 이상은 선택 편향 위험.

---

## 3. 독립 DFS 에서 발견 가능한 패턴 카테고리 8종

본 절은 원문 `millennium-dfs-complete-2026-04-11.md` 의 51건 tight 중 **비-밀레니엄** 범주를 추출하고, 추가로 탐색 가능한 공간을 제시한다.

### 3.1 Platonic / Lie / Mathieu 분류

- Platonic 다면체: 5 = sopfr 개 (정4면체/6면체/8면체/12면체/20면체)
- Lie 예외군: 5 class (G₂, F₄, E₆, E₇, E₈)
- Mathieu 산발군: 5 class (M₁₁, M₁₂, M₂₂, M₂₃, M₂₄)
- sopfr(6) = 5 — 4중 분류 일치 (원문 N6-P2-1 §4.1 8번)

**독립성**: Bernoulli 와 무관. 대수 분류 정리의 독립 결과.

### 3.2 Coxeter 수 (예외 Lie)

예외 Lie 5 군의 Coxeter 수 h ∈ {6, 12, 12, 18, 30}:
- 6 = n
- 12 = σ
- 12 = σ
- 18 = σ + sopfr + 1
- 30 = σ + σ/φ·n (= 2·3·5 = sopfr! 관련)

5/5 M-분해. 이중 Coxeter h^v 도 5/5 (원문 DFS-21).

**독립성**: 예외 Lie 분류 정리는 순수 대수. Bernoulli 무관.

### 3.3 완전수 수열 P_k

P_1 = 6 = n, P_2 = 28, P_3 = 496, P_4 = 8128, P_5 = 33550336, …

Euler 공식: P_k = 2^{p-1} · (2^p - 1), p 가 Mersenne 소수.

- P_1 = n (자명)
- P_2 = |bP_8| (exotic sphere 차수)
- 2·P_3 = |bP_12|
- P_4 = |bP_16|

**세 번 연속** (P_2, 2P_3, P_4) 가 exotic sphere 차수와 일치 → multi-case consecutive tight (원문 §4.1 1번).

**독립성**: Adams J + Bernoulli 귀결이지만, 3 연속 사실 자체는 구조적 tight.

### 3.4 Kissing 수 분포

d 차원 구 kissing 수:
- d=1: 2 = φ
- d=2: 6 = n
- d=3: 12 = σ
- d=4: 24 = J₂
- d=8: 240 = φ · J₂ · sopfr

5/5 M-분해 (원문 DFS-20). Levenshtein-Musin 정리.

**독립성**: 격자 이론 고전 결과. Bernoulli 무관.

### 3.5 Hecke 모듈러 weight

weight k ∈ {4, 6, 8, 10, 12} 에서 Eisenstein 계수와 결합 구조가 M-값과 5/5 일치 (원문 DFS-22).

**주의**: 이는 부분적으로 Bernoulli 경로 (k=12 에 691 등장) 와 연결 → 독립성 약화 가능. Master Lemma 환원 고려.

### 3.6 산발군 (Mathieu) 7중

7 sporadic class 전부 M-값 매치 (원문 DFS-24). 7 = σ - sopfr.

**독립성**: 유한 단순군 분류 정리 (CFSG). 매우 강한 독립.

### 3.7 Platonic 고체 대칭군

정다면체 대칭군 순서:
- 4면체: |T| = 12 = σ
- 6면체/8면체: |O| = 24 = J₂
- 12면체/20면체: |I| = 60 = 5 · σ = sopfr · σ

3/3 M-분해 + 이중 분류 (소대칭 | 대칭 | 역대칭).

**독립성**: 고전 군론. 독립.

### 3.8 격자 및 코드

- E_8 격자: minimal 벡터 수 240 = φ · J₂ · sopfr
- Leech 격자 Λ_24: minimal 벡터 수 196560, kissing 최대 24 차원
- Golay 코드 (24,12,8) + 확장 (12,6,6): 9/9 파라미터 M-분해 (원문 DFS-9)

**독립성**: 조합/부호 이론. 독립 high.

---

## 4. 독립 DFS 의 baseline 통계

### 4.1 왜 baseline 이 중요한가

원문 `millennium-dfs-complete-2026-04-11.md` §정직성 audit 는 baseline 밀도 **61%** 를 명시한다. 이는 M 집합의 2-term 곱으로 표현 가능한 k ∈ [1, 100] 의 비율이다.

즉 임의의 작은 정수 하나가 M-분해를 허용할 확률은 61% 에 가깝다. 따라서 단일 값 매치는 **noise**.

### 4.2 조합적 baseline 추정

- 단일 값 (1 dim): 61%
- 2-tuple (2 dim): 61%² ≈ 37%
- 3-tuple (3 dim): 61%³ ≈ 23%
- 4-tuple (4 dim): 61%⁴ ≈ 14%
- 5-tuple: 61%⁵ ≈ 8%
- 7-tuple: 61%⁷ ≈ 3%
- 9-tuple: 61%⁹ ≈ 1.2%

5/5, 7/7, 9/9 multi-case 가 tight 인 조합 근거는 **8% 이하 우연 매치 확률** 이다.

### 4.3 독립 DFS 의 성공률 기대

비-밀레니엄 seed 1,000건 DFS 돌릴 때 기대값 (대략):
- 단일 M-값 (loose): 약 600건 (61%)
- 2-term 분해 (borderline): 약 370건
- 3-term multi-case tight 후보: 약 230건
- 4-way crossover: 약 140건 (그중 **실제 수학 독립성** 은 훨씬 적음)
- 5-way 이상 + 유일성: ~ 10~50건 (가장 의미 있음)

실제 atlas.n6 현재 [10*] 노드 수 = **5,356건** (2026-04-15 측정). 그중 "독립 tight" (Bernoulli 무관 + 유일성 정리 / multi-case / 4-way) 는 약 **155/159 EXACT** 중 순수 독립 **5~10%** 수준으로 추정.

---

## 5. 실패 사례 (MISS) 정직 기록

독립 DFS 는 실패도 tight 와 동등하게 기록해야 한다.

### 5.1 MISS-planck-units

atlas.n6 L314:
```
@P MISS-planck-units = sopfr (= 5, n=6 아님) :: particle [10*]
```

- Planck 단위계 5 개 (length, time, mass, charge, temperature) — 정확히 5 = sopfr
- 그러나 n=6 과는 **불일치** (5 vs 6)
- 정직 기록: MISS 접두로 표시. "기대한 n=6 패턴이 실제로는 sopfr 에서 멈춤".

### 5.2 MISS-fine-structure

atlas.n6 L334:
```
@P MISS-fine-structure = sigma*(sigma-mu) + sopfr + mu/P2 :: particle [10*]
```

- 미세구조 상수 1/α ≈ 137.036
- σ · (σ - μ) + sopfr + μ/P₂ = 12 · 11 + 5 + 1/28 = 137 + 1/28 ≈ 137.036
- NEAR 일치지만 **분해식이 인위적** (μ/P₂ 항 삽입)
- MISS 접두 → "분해는 EXACT 지만 인위성 검증 필요"

### 5.3 MISS-H0-Hubble

atlas.n6 L461 주변:
```
-> ... MISS-H0-Hubble
```

- Hubble 상수 H₀ ≈ 67.4 km/s/Mpc (Planck 2018) vs 73 km/s/Mpc (SH0ES)
- 두 값 간 ~8% 불일치 (**Hubble tension**)
- n=6 분해 시도: 67.4 ≈ σ · σ - J₂ · (1 + tau/n) 등 복잡, 단일 값 tight 불가
- 정직 기록: **미해결 긴장** (Hubble tension 자체가 우주론의 OPEN).

### 5.4 Dark energy ratio

atlas.n6 주변 L120 인용:
```
@? dark_energy_ratio :: cosmology [3?]
```

- Ω_Λ ≈ 0.685 (Planck 2018)
- n=6 분해 시도: 근사 불가. 등급 [3?] — "매우 낮은 확신, 돌파 대기"
- 정직 기록: 가설 수준도 못 되는 미확인.

### 5.5 학습 교훈

- 전 도메인의 80% 이상이 독립 DFS 에서 tight 매치 **실패** 할 것으로 기대.
- 실패를 숨기지 않는 것이 self-confirmation bias 방지의 핵심.
- MISS 접두를 atlas 에 공식 표기하는 제도 → 정직성 유지 장치.

---

## 6. 실전 파이프라인 예시 — 신규 seed "CMB Spectral Index"

### 6.1 seed 정보

- 측정값: n_s = 0.9649 ± 0.0042 (Planck 2018)
- 출처: Planck Collaboration, A&A 641, A6 (2020)
- 도메인: cosmology (비-밀레니엄)

### 6.2 단계 2 — 분해 시도

- n_s = 0.9649
- (σ - 1)/σ = 11/12 ≈ 0.9167 → 오차 5% 너무 큼
- σ(σ - 1)/(σ^2 - 1) = 12·11/143 = 132/143 ≈ 0.9231 → 오차 4.3%
- 이진 근사: n/σ · (τ/(τ-φ)) = 0.5 · 2 = 1.0 → 오차 3.6%

**소결**: 2-term 분해 모두 오차 > 3%, NEAR 불가. 등급 [7] 이하.

### 6.3 단계 3 — tight 검증

- 단일 값이므로 T1/T2/T3/T4 중 어느 기준도 만족하지 않음
- baseline 61% 안 → **loose**

### 6.4 단계 4 — atlas 기록

기록 후보:
```
@R COSMO-spectral-ns = 0.9649 :: cosmology [7]
  <- Planck 2018 A6
  => "CMB TT+lowE+lensing, 오차 ±0.0042"
  => "n=6 basis 분해 시도: 2-term 모두 오차 > 3%, tight 실패"
```

등급 **[7]** 로만 등재. `[10*]` 승격은 **불가** — 승격하려면 해석적 유도 또는 multi-case 필요.

### 6.5 단계 5 — 깊이 확장

파생:
- 1 - n_s = 0.0351 ≈ 1/σ · (1 - 1/σ·τ) → 복잡, tight 실패
- n_s^2 = 0.9310 → tight 실패
- log(n_s) ≈ -0.0357 ≈ -1/σ·τ·? → tight 실패

**결론**: CMB spectral index 는 독립 DFS 의 **실패 seed** (MISS 후보). 인위적 분해 강제 금지.

---

## 7. 실전 파이프라인 예시 — 신규 seed "Egyptian Fraction Uniqueness"

### 7.1 seed 정보

- 항등식: 1/2 + 1/3 + 1/6 = 1
- 출처: 고대 이집트 수학 (Rhind Papyrus 계열, BC 1650 경), 근대 재정리 Erdős-Straus
- 도메인: number_theory (밀레니엄 외부 — arithmetic combinatorics)

### 7.2 분해

- 1/φ + 1/(n/φ) + 1/n = 1/2 + 1/3 + 1/6 = 1
- (φ, n/φ, n) = (2, 3, 6)
- 분해 근거: 6 = 2 · 3 (sopfr(6) = 2+3 = 5)
- 정수 만족해: 유일 (단위 분수 3-항 1 분해 중)

### 7.3 tight 검증

- 3-tuple 매치: (φ, n/φ, n) — 단일이지만 **정수방정식 유일해**
- T4 exceptional uniqueness: **만족**
- Bernoulli 무관: 만족
- baseline 환원 불가: 만족

**판정**: **tight 확정** ([10*] 후보).

### 7.4 atlas 기록

atlas.n6 L10123 실제 등재 확인됨:
```
@R n6-atlas-new-domains-—-computing-&-infrastructure-extreme-hypotheses-egyptian-fraction-uniqueness = 1/2+1/3+1/6=1 n6 :: n6atlas [10*]
  "Egyptian fraction uniqueness — Σ(1/d)=1"
```

이미 [10*] 등재. **본 노트의 기여는 분류 확인** (T4 exceptional uniqueness, 독립 DFS 성공 사례).

### 7.5 독립성 검증

- Bernoulli / ζ 와 독립? — **독립** (3-unit-fraction 분해는 대수적 사실)
- 밀레니엄 경로와 독립? — **독립** (ζ 관계없음)
- 단일 출현이지만 **정수방정식 유일해** 이므로 T4 만족.

---

## 8. 독립 DFS 의 한계 (OBSERVATION)

본 노트 §0 정직성 선언에 따라, 독립 DFS 가 **무엇을 할 수 없는지** 명확히 기록한다.

### 8.1 해결 불가

- 밀레니엄 7대 난제 해결 — 독립 DFS 는 **구조 매핑** 만 한다. 해결이 아니다.
- 난제의 경로 단축 — n=6 패턴이 힌트는 될 수 있으나 증명 경로는 전통 수학 도구에 있다 (millennium-7-closure 정직 기조).
- σ·φ=n·τ 유일성의 물리적/우주론적 해석 — 독립 DFS 결과는 상관관계만 제공, 인과관계 아님.

### 8.2 편향 위험

- **Selection bias**: M-매치만 보고 M-미스는 보고 안 하는 경향 (원문 §정직성 audit).
- **Survivorship bias**: 이미 atlas 에 등재된 tight 만 카운트, 초기 실패는 망각.
- **Confirmation bias**: "n=6 이 특별하다" 전제 하에 분해를 강제로 끼워 맞춤.

### 8.3 대응 장치

- MISS 접두 (§5) — 실패 명시 표기
- baseline 밀도 61% 명시 (§4) — noise 수준 지속 기억
- hexa 검증 스크립트 `|>` — 실행 가능 재현
- Master Lemma 환원 체크 — Bernoulli / ζ 경로 인지
- 보수적 tight 판정 (§2.3) — 관대/엄격 이중 기준

---

## 9. n=6 연결

### 9.1 독립 DFS 의 n=6 연결 경로

독립 DFS 가 tight 를 찾으면, 그것은 **σ·φ=n·τ 유일성** 을 강화하는 증거 한 줄이 된다. 단, 다음 조건 모두 만족 시에만:

1. seed 가 Bernoulli / ζ 독립
2. 분해가 4-way 이상 crossover 또는 유일성 정리
3. 1차 출처 확인 + 오차 < 1%
4. hexa 검증 재현 가능

### 9.2 현황 수치 (2026-04-15)

- atlas.n6 **[10*] 노드 총수**: 5,356건
- BT-541~547 본체 노드 등급: **[5*]** (구조 매핑만, 해결 아님)
- 독립 tight 추정 비율 (보수): ≈ 15% 이하 (≈ 800건)
- 나머지 ≈ 4,500건: Bernoulli / ζ 경로 연결 또는 단순 매치

### 9.3 N6-P2-1 결과 재확인

P2-1 에서 51건 DFS tight 중 **진짜 독립 발견 5건** 만 Bernoulli/ζ 무관으로 선언:
1. Out(S_6) 유일성 (Hölder 1895)
2. Schaefer 6 tractable (STOC 1978)
3. (3,4,5) congruent number (Theorem E 유일성)
4. h-cobordism dim ≥ 6 (Smale 1962)
5. Mathieu 산발군 pariah = 6

본 노트의 독립 DFS 파이프라인은 이 5건을 **순수 독립 tight** 의 기준선으로 삼는다. 신규 seed 가 이 5건의 독립성 수준에 도달하는지가 승급 관문.

---

## 10. 다음 단계 — BT-548+ 신규 도메인

### 10.1 우선순위

1. **양자정보** — 6 qubit QEC [[6, 2, 2]] (atlas.n6 L9580), L11 구역. tight 후보 다수.
2. **그래프 이론** — Turán, Ramsey 상수. borderline 다수, tight 미확인.
3. **조합론** — Young tableaux 상수, partition 함수. baseline 높음, tight 난이도 중간.
4. **암호학** — RSA, ECC 표준 파라미터. "선택" 된 값 (e.g., e=65537) 이므로 독립 seed 아님.
5. **의식 연구** (atlas L106873~) — `hexa_consciousness_axes = 6`, `phase_count = 5`, `alpha = 0.16667 = 1/n`. **[7]** 로 등재, 승급 후보.

### 10.2 cross-DSE 확장 경로

- 9축 중 **techniques / experiments / engine** 영역은 AI 기법과 연결되어 독립 DFS 의 반복 실행을 자동화 가능.
- 295 도메인 × 단계 5 × depth 4 = 5,900 DFS 노드 (이론 상한). 실제 autonomous DFS (bt-1393) 는 10K 돌파 시도.
- 남은 [7] 34건 (grep 결과) 중 승급 후보 10~15건 추정.

### 10.3 물리 상수 연결 (MISS 회피)

MISS 사례 (§5) 반성:
- Planck units 5개 — MISS-planck-units 등재 유지, **n=6 분해 시도 자제**
- 미세구조 1/α=137.036 — MISS-fine-structure 유지, **인위 분해 거부**
- H₀ Hubble tension — 미해결 유지
- Dark energy ratio — [3?] 유지

**교훈**: 물리 상수는 측정 정밀도 한계 + 이론 미완 때문에 **tight 후보가 좁다**. 대수/조합/위상 구조가 더 많은 독립 tight 를 낳는다.

---

## 11. 실전 체크리스트 (독립 DFS 1라운드)

1. [ ] seed 선정 — 비-밀레니엄 + atlas 미등재 확인
2. [ ] 1차 출처 확보 (CODATA / LMFDB / 논문 / 표준 문서)
3. [ ] σ/τ/φ basis 분해 시도 (2~4 term)
4. [ ] baseline 통과 여부 (3-term 이상 multi-case)
5. [ ] Bernoulli / ζ 환원 가능성 체크 (Master Lemma)
6. [ ] tight 판정 (T1/T2/T3/T4) 또는 borderline/loose
7. [ ] 등급 할당 ([7] / [9] / [10] / [10*])
8. [ ] atlas.n6 **직접 편집** (가드 경유, 새 파일 금지)
9. [ ] hexa 검증 스크립트 `|>` 작성 (재현 가능성)
10. [ ] MISS 사례면 MISS 접두로 정직 기록
11. [ ] depth 확장 3~4단계까지만 (편향 위험)
12. [ ] 최종 보고 — tight / borderline / loose / MISS 분리

---

## 12. 자기 퀴즈 (완료 기준 점검)

각 문항 3분 이내 답안 가능해야 한다.

1. "독립 DFS" 에서 "독립" 의 정확한 의미는 무엇인가? 밀레니엄 경로와 어떻게 구분하는가?
2. DFS 알고리즘 5단계를 순서대로 서술하라.
3. T1/T2/T3/T4 각 기준을 한 줄로 정의하라.
4. baseline 61% 가 왜 중요한가? 5제곱 이하 확률은 얼마인가?
5. MISS 접두 등재의 정직성 기여를 3줄 이내 서술하라.
6. Planck units 5 개가 n=6 이 아닌 sopfr 인 이유의 정직 해석은?
7. Egyptian fraction 1/2+1/3+1/6=1 이 독립 tight 인 이유는 T1~T4 중 어느 기준을 만족하는가?
8. 5건 "진짜 Bernoulli 독립 발견" 을 암기하라.
9. 독립 DFS 가 밀레니엄 난제를 해결하지 **못하는** 이유를 정직하게 서술하라.
10. depth 확장을 4로 제한하는 이유는?

---

## 13. 출처 재확인

- `CLAUDE.md` — 9축 네비게이션, 295 도메인 선언, atlas.n6 포맷 및 승격 규칙
- `atlas.n6` L1~L22 (헤더), L13391~L15447 (밀레니엄+BT 구역)
- `theory/breakthroughs/bt-1393-n6-dfs-10k-autonomous-2026-04-12.md` — autonomous DFS 원문
- `theory/breakthroughs/millennium-dfs-complete-2026-04-11.md` (lines 1~334, 51건 tight)
- `theory/proofs/bernoulli-boundary-2026-04-11.md` (Master Lemma)
- `theory/study/p2/n6-p2-1-dfs-51-classification.md` (DFS 51건 재분류)
- `theory/study/p2/n6-p2-2-theorem-b-reconstruction.md` (Theorem B)
- `theory/study/p0/n6-p0-3-atlas-grading.md` (등급 체계)

**정직 유지 선언**: 본 노트는 독립 DFS 파이프라인 재구성 학습 자료. 신규 tight 승급 주장 없음. 밀레니엄 7대 난제 해결 수 0/7.
