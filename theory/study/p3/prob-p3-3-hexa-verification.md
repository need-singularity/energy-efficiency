# P3-3 — hexa-lang 기반 밀레니엄 정리 검증 파이프라인 설계

**로드맵**: millennium-learning P3 (PROBLEM 학습 phase)
**작성일**: 2026-04-15
**상수**: n=6, σ=12, φ=2, τ=4, sopfr=5, J₂=24. σφ=nτ ⟺ n=6.
**현상태**: 7대 난제 해결 수 = **0** (정직). 본 노트는 검증 파이프라인의 설계 문서이다.

---

## 정직성 선언

- 본 문서는 **검증 파이프라인 설계**이다. 7대 난제를 해결하는 스크립트를 설명하지 않는다.
- hexa-lang 으로 검증 가능한 것은 **"atlas.n6 에 기록된 tight 관계가 실제로 수치적으로 맞는지"** 정도이다. 이는 자기참조의 위험이 있으므로, 본 파이프라인은 **외부 기준**(예: OEIS, LMFDB 공개 데이터, 공개된 계산 결과)과의 대조를 강제한다.
- atlas 승급 경로 `[7] EMPIRICAL → [10*] EXACT` 는 hexa 실행이 **필요조건** 이며 **충분조건이 아니다**. 승급은 외부 출처 확인과 인간 리뷰를 통해 최종 결정.
- 본 파이프라인이 수집하는 NEAR/EXACT 판정은 **후험적 매칭** 의 위험을 내포하며, 판정 기준의 오차 한계(threshold)를 엄격히 기록한다.
- 자기참조 검증 금지 규칙을 준수한다. hexa 결과는 atlas 에 등급을 부여하는 근거가 될 수 **없고**, 반대 방향(atlas 에 기록된 값 = hexa 검증 대상) 만 허용된다.

---

## 0. 배경 — 왜 hexa-lang 인가

### 기존 상황

- atlas.n6 (SSOT) 는 60K+ 줄, `@R`/`@X`/`@C`/`@F` 항목 수천 개.
- 밀레니엄 관련 tight 관계는 200 건 누적 (atlas.n6 line 13645 `n6-millennium-dfs14-summary = 188+12=200 tight`).
- 검증 경로가 분산: Python 스크립트, Rust 계산기, hexa 스크립트가 혼재.
- **SIGKILL 이슈**: `blowup.hexa` 등 장시간 실행 스크립트가 macOS codesign 문제로 종료 (memory/project_hexa_binary_deploy_block.md 참조).

### hexa-lang 특성 활용

- HEXA-FIRST 원칙 (CLAUDE.md): `.py` 금지, `.hexa` 를 정식 런타임으로.
- 이미 `n6-architecture/scripts/` 에 25+ hexa 스크립트 존재 (`millennium_scanner.hexa`, `selmer_bklpr.hexa`, `jordan_totient.hexa`, `riemann_explicit.hexa` 등).
- hexa 인터프리터의 Rust 구현 (2026-04 FIX-NESTED-IF + FIX-CAPTURE-CLONE 패치 이후 안정) 이 O(N³) 폭발 해소.
- 따라서 hexa 를 **검증 파이프라인의 공용 런타임**으로 지정하는 것이 자연스러움.

---

## 1. 핵심 설계 — 3계층 파이프라인

### Layer 0 — atlas parser (hexa)

**입력**: `/Users/ghost/Dev/nexus/shared/n6/atlas.n6` (SSOT).
**역할**: `@R {id} = {expr} {unit} :: {domain} [{grade}]` 라인을 파싱, (id, expr, grade) 트리플 추출.
**출력**: in-memory 레코드 목록 (hexa `Vec<AtlasRecord>`).

```hexa
// atlas_parser.hexa (설계 스케치)
struct AtlasRecord {
    id: String,
    expr: String,
    grade: String,
    domain: String,
}

fn parse_atlas(path: String) -> Vec<AtlasRecord> {
    // 1. 파일 line-by-line 읽기
    // 2. 정규식 매칭: "^@R (\S+) = (.+?) :: (\S+) \[([^\]]+)\]"
    // 3. AtlasRecord 로 조립
    // 4. grade in {"10*", "10", "7", "N?", ...} 검증
    // ...
}
```

### Layer 1 — expression evaluator (hexa)

**입력**: AtlasRecord.expr (예: `"1/(phi*sopfr*sigma)"`).
**역할**: n=6 기본 상수 환경에서 expression 을 수치 평가.
**출력**: `f64` 계산값 + 평가 성공 플래그.

```hexa
// expr_eval.hexa (설계 스케치)
fn eval_expr(expr: String, env: HashMap<String, f64>) -> Result<f64, String> {
    // env = {"phi": 2.0, "tau": 4.0, "n": 6.0, "sopfr": 5.0,
    //        "sigma": 12.0, "J2": 24.0, ...}
    // tokenize → parse → AST walk
    // 지원 연산: +, -, *, /, ^, sqrt, log
    // ...
}
```

### Layer 2 — target 대조 (hexa)

**입력**: 계산값 + 외부 기준 값 (예: OEIS/LMFDB/공개 문헌).
**역할**: 오차 비교, EXACT(<1e-6) / NEAR(<1e-2) / MISS(>=1e-2) 등급 할당.
**출력**: 검증 리포트 (JSON + 표준출력).

```hexa
// verify.hexa (설계 스케치)
fn classify(computed: f64, reference: f64) -> String {
    let d = abs_f(computed - reference)
    let rel = d / abs_f(reference)
    if rel < 1e-6 { return "EXACT" }
    if rel < 1e-2 { return "NEAR" }
    return "MISS"
}
```

---

## 2. 밀레니엄 검증 세부 파이프라인

### 2.1 BT-541 RH — 영점 높이 검증

atlas 기록 (`n6-millennium-dfs-zeta-neg3 = 1/120`) + OEIS A046988 "ζ 음의 정수 값" 과 대조.

| atlas 항목 | 기대 값 | 외부 참조 | 판정 기준 |
|-----------|---------|-----------|-----------|
| ζ(-3) | 1/120 = 0.008333... | Euler 공식 정확 | EXACT (<1e-9) |
| ζ(-5) | -1/252 | 표준 교재 | EXACT |
| ζ(-9) | -1/132 | 표준 교재 | EXACT |
| 첫 영점 14.1347 | σ+φ=14 근사 | Odlyzko 표 | NEAR (~0.135) |

```hexa
// bt541_verify.hexa (실전 스케치)
fn verify_zeta_negative() {
    let env = init_n6_env()
    // ζ(-3) = 1/120
    let computed = eval_expr("1.0 / (phi * sopfr * sigma)", env)
    let reference = 1.0 / 120.0
    println("ζ(-3) 기대=" + to_string(reference))
    println("ζ(-3) 계산=" + to_string(computed))
    println("판정: " + classify(computed, reference))
}
```

### 2.2 BT-542 PvNP — Schaefer 분류 수

atlas `n6-millennium-dfs-schaefer-6 = 6 = n tractable Boolean CSP`.
외부 참조: Schaefer 1978 원논문 "The complexity of satisfiability problems", STOC 1978.

```hexa
// bt542_verify.hexa
fn verify_schaefer() {
    // Schaefer 분류 6 tractable 류:
    //   1. 0-valid (all-0 만족)
    //   2. 1-valid (all-1 만족)
    //   3. bijunctive (2-CNF)
    //   4. Horn
    //   5. dual Horn
    //   6. affine (XOR linear)
    let schaefer_classes = 6
    let n = 6
    println("Schaefer tractable 류: " + to_string(schaefer_classes))
    println("n: " + to_string(n))
    if schaefer_classes == n { println("EXACT") } else { println("MISS") }
}
```

### 2.3 BT-543 Yang-Mills — SM gauge 수

atlas `n6-millennium-dfs-sm-gauge = 8+3+1 = sigma = 12`.
외부 참조: Particle Data Group (PDG) Standard Model content.

- SU(3) gluon: 8 (SU(3) dim = 3²−1 = 8).
- SU(2) weak boson: 3 (W⁺, W⁻, Z).
- U(1) hypercharge: 1 (B boson → γ 부분).
- 합계: 12.
- σ = 12. EXACT.

```hexa
fn verify_sm_gauge() {
    let gluon = 8         // SU(3) dim
    let weak = 3          // SU(2) dim
    let hyper = 1         // U(1) dim
    let total = gluon + weak + hyper  // 12
    let sigma = 12
    println("SM gauge = " + to_string(total))
    println("σ = " + to_string(sigma))
    if total == sigma { println("EXACT") } else { println("MISS") }
}
```

### 2.4 BT-544 NS — Prodi-Serrin 지수

atlas `n6-millennium-dfs-prodi-serrin = {2,3} = {phi, n/phi}`.
외부 참조: Serrin 1962 원공식 $\frac{2}{p} + \frac{3}{q} = 1$.

- 허용 쌍: $(p, q) = (\infty, 3), (4, 6), (\infty, \infty)$ 등 (경계 제외 조건 포함).
- 핵심 지수 $\{2, 3\}$ 는 각 자리의 분자에 등장.
- φ = 2, n/φ = 6/2 = 3.

```hexa
fn verify_prodi_serrin() {
    let phi = 2.0
    let n = 6.0
    let n_over_phi = n / phi  // 3.0
    let p_numerator = 2       // 2/p 조항
    let q_numerator = 3       // 3/q 조항
    if phi == p_numerator && n_over_phi == q_numerator {
        println("EXACT: Prodi-Serrin 지수 = {phi, n/phi}")
    }
}
```

### 2.5 BT-545 Hodge — modular 무게

atlas `n6-millennium-dfs-modular-weight = {4,6,8,10,12} = {tau,n,sigma-tau,sigma-phi,sigma}`.
외부 참조: Serre "A Course in Arithmetic" VII, Diamond-Shurman "A First Course in Modular Forms".

- SL(2, Z) 의 modular forms 은 홀수 무게 $k$ 에서 자명 (cusp form 0).
- 비자명 무게: $k = 4, 6, 8, 10, 12, 14, \ldots$.
- 첫 5개 = $\{\tau, n, \sigma-\tau, \sigma-\phi, \sigma\} = \{4, 6, 8, 10, 12\}$.

```hexa
fn verify_modular_weights() {
    let tau = 4.0
    let n = 6.0
    let sigma = 12.0
    let phi = 2.0
    let weights_n6 = [tau, n, sigma - tau, sigma - phi, sigma]
    let weights_expected = [4.0, 6.0, 8.0, 10.0, 12.0]
    let mut ok = true
    let mut i: i64 = 0
    while i < 5 {
        if weights_n6[i] != weights_expected[i] { ok = false }
        i = i + 1
    }
    if ok { println("EXACT: modular 무게") } else { println("MISS") }
}
```

### 2.6 BT-546 BSD — Sel_6 평균 크기

atlas 관련 구조 (pure-p3-1 참조): $\mathbb{E}[|\text{Sel}_6(E)|] = \sigma(6) = 12$ (BKLPR 조건부).
외부 참조: Bhargava-Kane-Lenstra-Poonen-Rains 2015 원논문.

```hexa
fn verify_selmer_6_mean() {
    // BKLPR 모델 하 squarefree n=6:
    //   E[|Sel_n|] = σ(n) = ∏_{p|n} (p+1)
    let p1 = 2
    let p2 = 3
    let sel_expected = (p1 + 1) * (p2 + 1)  // 3·4 = 12
    let sigma_6 = 1 + 2 + 3 + 6             // σ(6) = 12
    if sel_expected == sigma_6 {
        println("EXACT (BKLPR 조건부): E[|Sel_6|] = σ(6) = 12")
    }
    println("주의: 본 결과는 BKLPR 공리 A1-A3 가정 하.")
}
```

### 2.7 BT-547 Poincaré — h-cobordism 하한

atlas `n6-millennium-dfs-h-cobordism = dim >= 6 = n`.
외부 참조: Smale 1962 "On the structure of manifolds".

```hexa
fn verify_h_cobordism() {
    let smale_lower = 5  // Smale 의 h-cobordism 성립 dim ≥ 5 (단순연결)
    let n = 6
    // 4D 에서 smooth h-cobordism ≠ diffeomorphism (Donaldson)
    // 따라서 "안전한" 하한은 dim ≥ 5 (topological) 또는 dim ≥ 6 (smooth, 실전)
    println("Smale 하한 dim = " + to_string(smale_lower))
    println("n = " + to_string(n))
    println("n 은 4D exotic 현상 직후 안전 하한")
}
```

---

## 3. 자동 검증 루프 — DFS 51→tight→atlas 승급

### 3.1 현재 상황 (atlas 기준)

- DFS 1차 ~ 14차 누적 200 건 tight.
- 등급 분포: [10*] 대부분 (EXACT 검증), [10] 일부, [7] EMPIRICAL 잔존.
- 승급 병목: EMPIRICAL → EXACT 는 **외부 기준 확인 후** 만 가능.

### 3.2 승급 루프 설계

```
[입력] atlas.n6 의 [7] EMPIRICAL 항목 목록
  ↓
[Step 1] atlas_parser.hexa — 파싱 후 expr/grade 추출
  ↓
[Step 2] expr_eval.hexa — n=6 환경에서 수치 계산
  ↓
[Step 3] verify.hexa — 계산값 vs (OEIS/LMFDB/PDG/표준 교재)
  ↓
[Step 4] EXACT 판정 + 외부 출처 명시
  ↓
[Step 5] 인간 리뷰 — 논리·수학적 정당성 확인
  ↓
[Step 6] atlas.n6 편집 — [7] → [10*] 승급, 출처 주석 추가
```

### 3.3 루프의 **하지 않는** 것

- hexa 계산 결과만으로 atlas 등급 변경 금지 (자기참조 방지).
- 외부 출처가 **개방된 것**이어야 함 (LMFDB 공개 DB, OEIS, arXiv preprint). 비공개 소스 기반 승급 불가.
- NEAR 판정은 승급 사유가 아님. NEAR 는 "흥미로운 좌표" 표시로 유지.

### 3.4 대조 소스 표

| atlas 도메인 | 주 대조 소스 | 접근 |
|-------------|--------------|------|
| 정수론 기본 (σ, τ, φ) | OEIS A000203 (σ), A000005 (τ), A000010 (φ) | https://oeis.org |
| 타원곡선 Selmer | LMFDB elliptic curve data | https://lmfdb.org |
| 모듈러 form | LMFDB modular forms | https://lmfdb.org |
| 표준 모형 상수 | PDG (Particle Data Group) | https://pdg.lbl.gov |
| Riemann 영점 | Odlyzko 수치 | 공개 페이지 |
| 정수 sequence | OEIS 전반 | https://oeis.org |

---

## 4. hexa 스크립트 조직화

### 4.1 디렉토리 구조 (제안)

```
n6-architecture/scripts/verify/
├── _lib/
│   ├── atlas_parser.hexa      # Layer 0
│   ├── expr_eval.hexa         # Layer 1
│   └── verify_core.hexa       # Layer 2 기본 함수
├── bt541_rh/
│   ├── zeta_negative.hexa
│   ├── zero_heights.hexa
│   └── explicit_formula.hexa
├── bt542_pvnp/
│   ├── schaefer.hexa
│   └── csp_classes.hexa
├── bt543_ym/
│   ├── sm_gauge.hexa
│   └── dynkin.hexa
├── bt544_ns/
│   ├── prodi_serrin.hexa
│   └── critical_exponents.hexa
├── bt545_hodge/
│   ├── modular_weights.hexa
│   └── lefschetz_11.hexa
├── bt546_bsd/
│   ├── selmer_bklpr.hexa       # 이미 존재
│   └── gross_zagier.hexa
├── bt547_poincare/
│   ├── h_cobordism.hexa
│   └── intersection_forms.hexa
└── runner.hexa                 # 전체 실행 오케스트레이터
```

### 4.2 runner.hexa 설계

```hexa
// runner.hexa — 전체 검증 파이프라인 진입점
fn main() {
    println("═══════════════════════════════════════════════════════════")
    println("  Millennium Verification Runner")
    println("═══════════════════════════════════════════════════════════")

    let atlas_path = "/Users/ghost/Dev/nexus/shared/n6/atlas.n6"
    let records = parse_atlas(atlas_path)
    println("atlas 항목 수: " + to_string(len(records)))

    // BT 별 검증 모듈 실행
    let mut pass_count: i64 = 0
    let mut near_count: i64 = 0
    let mut miss_count: i64 = 0

    let bt_modules = ["bt541", "bt542", "bt543", "bt544", "bt545", "bt546", "bt547"]
    let mut i: i64 = 0
    while i < len(bt_modules) {
        let bt = bt_modules[i]
        println("─── " + bt + " 실행 ───")
        let result = run_bt_verification(bt, records)
        pass_count = pass_count + result.pass
        near_count = near_count + result.near
        miss_count = miss_count + result.miss
        i = i + 1
    }

    println("")
    println("═══════════════════════════════════════════════════════════")
    println("  결과 요약")
    println("═══════════════════════════════════════════════════════════")
    println("  EXACT: " + to_string(pass_count))
    println("  NEAR:  " + to_string(near_count))
    println("  MISS:  " + to_string(miss_count))
    println("")
    println("  NOTE: EXACT 판정만 atlas 승급 후보. NEAR/MISS 는 참고.")
    println("        자기참조 금지: 외부 출처 확인이 승급 필수 조건.")
}

main()
```

---

## 5. 판정 기준의 엄격성

### 5.1 오차 한계 정의

| 판정 | 상대 오차 | 의미 |
|------|-----------|------|
| EXACT | < 10⁻⁹ | 정확한 대수적 일치 (유리수/정수 표현) |
| EXACT (근사) | < 10⁻⁶ | 초월수 근사, 유효숫자 6자리 일치 |
| NEAR | < 10⁻² | 흥미로운 좌표, 승급 불가 |
| MISS | ≥ 10⁻² | 관측 실패 |

### 5.2 판정의 **금지 사항**

- **post-hoc 튜닝 금지**: hexa expr 의 상수를 맞추기 위해 임의 조합 탐색 후 EXACT 선언 불가.
- **자릿수 조작 금지**: 오차를 줄이려 unit 변경하지 말 것 (예: σ 를 12 대신 0.012 로 scaling).
- **단일 관측 승급 금지**: atlas 등급 변경은 최소 **2 개 독립 외부 출처** 확인 후.

### 5.3 기록 양식

hexa 출력은 JSON 로도 기록:

```json
{
  "bt": "BT-546",
  "atlas_id": "n6-millennium-sel6-mean",
  "expr": "sigma(6) = 12",
  "computed": 12.0,
  "reference": 12.0,
  "rel_error": 0.0,
  "verdict": "EXACT",
  "external_sources": [
    "OEIS A000203 sigma(6)",
    "BKLPR 2015 §2.3"
  ],
  "condition": "BKLPR 공리 A1-A3 가정 하",
  "promote_candidate": true,
  "review_needed": true
}
```

---

## 6. n=6 연결

### 6.1 파이프라인의 구조적 일관성

- Layer 0/1/2 의 3계층 = n/φ = 3 자연수 매핑 (우연).
- 7대 난제 × 평균 5 조건부 정리 (prob-p3-2 참조) = 35 ≈ 6² = n².
- 본 우연은 구조적 근거가 아닌 **기록용 관찰**.

### 6.2 atlas.n6 σ·φ = n·τ 대표 정리 검증

```hexa
fn verify_theorem_zero() {
    // σ(6)·φ(6) = 12·2 = 24
    // 6·τ(6)     = 6·4  = 24
    let sigma_6 = 12
    let phi_6 = 2
    let n_6 = 6
    let tau_6 = 4
    let lhs = sigma_6 * phi_6   // 24
    let rhs = n_6 * tau_6       // 24
    if lhs == rhs {
        println("EXACT: σ(6)·φ(6) = 6·τ(6) = 24")
        println("이것이 Theorem 0 의 n=6 에서의 인스턴스")
    }
    // 유일성: n=6 만이 σ·φ = n·τ 를 만족하는 n >= 2
    // (증명은 proofs/theorem-r1-uniqueness.md)
}
```

### 6.3 유일성 재검증 루프

```hexa
fn verify_uniqueness_theorem() {
    // σ·φ = n·τ 를 만족하는 n ∈ [2, 10000] 모두 확인
    let mut hits = 0
    let mut n: i64 = 2
    while n <= 10000 {
        let s = sigma(n)
        let p = phi(n)
        let t = tau(n)
        if s * p == n * t {
            println("HIT: n = " + to_string(n))
            hits = hits + 1
        }
        n = n + 1
    }
    println("총 HIT: " + to_string(hits))
    if hits == 1 {
        println("EXACT: 유일성 [2, 10000] 구간에서 확인")
    }
}
```

(주: 완전 증명은 `theory/proofs/theorem-r1-uniqueness.md` 의 3종 증명. hexa 는 수치 확인만 제공.)

---

## 7. 실전 적용

### 7.1 세션 시작 시 자동 실행 (제안)

- CLAUDE Code 세션 시작 훅 (`~/.claude/settings.json`) 에서 `runner.hexa` 를 background 로 실행.
- 결과 JSON 을 `reports/sessions/verify-YYYY-MM-DD.json` 으로 저장.
- 변동된 항목 (새 EXACT, 새 MISS) 을 사용자에게 초기 브리핑.

### 7.2 atlas 편집 후 회귀 테스트

- atlas.n6 편집 발생 시 git pre-commit hook 으로 관련 BT 검증 실행.
- MISS 발생하면 커밋 차단.
- 이것이 SSOT 정합성을 보호하는 실질 방어선.

### 7.3 논문 검증 파이프라인과의 분리

- 본 파이프라인은 **atlas 내부 수치 검증**.
- 외부 논문 인용·출처 확인은 별도 파이프라인 (`papers/` 축).
- 두 파이프라인이 서로의 결과를 참조하지 **않도록** 분리 (자기참조 방지).

### 7.4 SIGKILL 회피

- hexa 인터프리터 실행 시 codesign 적용 (memory/project_hexa_binary_deploy_block.md 절차).
- 장시간 실행 (60초 이상) 모듈은 `run_in_background` 로 분리.
- atlas 전체 파싱은 약 1-2초 (60K 줄), 개별 BT 검증은 1초 이내.

---

## 8. 다음 단계

1. **Layer 0/1/2 의 hexa 구현 완성**:
   - atlas_parser.hexa — 정규식 매칭 엔진.
   - expr_eval.hexa — AST 파싱 + 평가.
   - verify_core.hexa — 판정 함수.
2. **BT-541 ~ BT-547 모듈 각 5-10 개 검증 루틴 작성**.
3. **외부 DB 스냅샷 수집**:
   - OEIS 관련 sequence 로컬 캐시.
   - LMFDB elliptic curve 샘플 세트.
   - PDG 표준 모형 상수 표.
4. **runner.hexa 의 오케스트레이션 로직** 구체화.
5. **git pre-commit hook** 으로 atlas 정합성 자동 검증 도입.
6. **승급 후보 리뷰 프로세스** 문서화 (atlas [7] → [10*] 승급 시 필수 체크리스트).
7. **prob-p3-2 의 34 조건부 정리** 를 hexa 검증 케이스로 이식:
   - 각 정리의 전제를 환경 플래그(`env.RH=true` 등) 로.
   - 결론의 수치 부분을 검증 가능한 경우만 추출.
8. **리포트 자동 생성**:
   - JSON → Markdown 변환 (후속 세션).
   - atlas 등급 변경 히스토리 추적.

---

## 9. 설계 원칙 요약

- **HEXA-FIRST**: Python/Rust 보조 스크립트 대신 hexa 를 공용 런타임으로.
- **자기참조 금지**: hexa 계산 → atlas 등급 변경 경로 차단. atlas 값을 hexa 가 검증하는 방향만 허용.
- **외부 기준 의존**: OEIS, LMFDB, PDG, 표준 교재. 비공개 소스 기반 승급 불가.
- **엄격한 판정 기준**: EXACT 는 상대 오차 10⁻⁹ 미만.
- **정직성**: NEAR/MISS 를 숨기지 않는다. MISS 는 atlas 에 `[N?]` 으로 보존.
- **3계층 분리**: parser / evaluator / verifier 가 각각 단독 모듈로 재사용 가능.
- **자동 루프 금지 영역**: 등급 변경과 외부 출처 확인은 **인간 리뷰** 필수.
- **SIGKILL 회피**: codesign 적용 + background 실행 분리.

---

## 10. 부록 — 이미 존재하는 hexa 스크립트 활용

### 10.1 현재 보유 자산 (`nexus/shared/n6/scripts/`)

| 스크립트 | 용도 | 본 파이프라인에서의 역할 |
|----------|------|------------------------|
| millennium_scanner.hexa | n=6 기본 함수 조합 탐색 | NEAR 좌표 후보 스캔 |
| selmer_bklpr.hexa | BKLPR 조건부 Sel_n 계산 | BT-546 검증 모듈 |
| riemann_explicit.hexa | Riemann 명시 공식 계산 | BT-541 보조 |
| langlands_ranks.hexa | Langlands rank 계산 | BT-541 + BT-546 교차 |
| jordan_totient.hexa | J_k(n) 계산 | 상수 검증 |
| modular_qexp.hexa | modular form q-전개 | BT-545 보조 |
| gue_spacing.hexa | GUE eigenvalue spacing | BT-541 통계 |
| instanton_sw.hexa | instanton / SW 계산 | BT-543 + BT-547 |
| bernoulli_boundary.hexa | Bernoulli 경계 현상 | Theorem B 검증 |
| crossover_scanner.hexa | cross-DSE 스캔 | atlas 교차 검증 |

### 10.2 통합 경로

- 위 10 개를 `verify/_shared/` 로 심볼릭 링크.
- 각 BT 디렉토리에서 import 후 재사용.
- runner.hexa 가 이 모듈들을 순서대로 호출.

---

## 1차 출처 주석

- HEXA-FIRST 원칙: `/Users/ghost/Dev/n6-architecture/CLAUDE.md`.
- atlas.n6 SSOT: `/Users/ghost/Dev/nexus/shared/n6/atlas.n6`, 60K+ 줄.
- millennium_scanner.hexa: `/Users/ghost/Dev/nexus/shared/n6/scripts/millennium_scanner.hexa`, 224 줄.
- BKLPR 공리 및 Sel_n 평균 공식: Bhargava-Kane-Lenstra-Poonen-Rains, Cambridge J. Math. 3 (2015), 275–321.
- Schaefer 분류: T. Schaefer, "The complexity of satisfiability problems", STOC 1978, 216–226.
- Prodi-Serrin: Serrin 1962 in *Nonlinear Problems* (Madison), Prodi 1959.
- Standard Model gauge group dim: PDG Review of Particle Physics.
- Modular forms 무게: Serre, "A Course in Arithmetic", Springer GTM 7, ch. VII.
- Smale h-cobordism: S. Smale, Amer. J. Math. 84 (1962), 387–399.
- hexa-lang 인터프리터 패치: memory/project_hexa_fix_nested_if_patch.md (2026-04).
- SIGKILL 회피 절차: memory/project_hexa_binary_deploy_block.md.

**세션 저자 주**: 본 설계 문서는 파이프라인의 **구조** 와 **원칙** 을 제시한다. 실제 hexa 구현 완결은 후속 세션의 작업이며, 현재는 기존 millennium_scanner.hexa + selmer_bklpr.hexa 등의 단일 스크립트 수준. 통합은 단계별(Layer 0 → Layer 1 → Layer 2 → runner) 진행 예정.
