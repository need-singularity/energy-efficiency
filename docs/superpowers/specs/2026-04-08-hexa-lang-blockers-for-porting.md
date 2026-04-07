# hexa-lang 누락 기능 — n6-architecture 포팅 차단 항목

작성일: 2026-04-08
상태: **포팅 보류** (hexa-lang 성장 대기)
관련 스펙: `2026-04-08-py-rs-sh-to-hexa-porting-design.md`
관련 계획: `docs/superpowers/plans/2026-04-08-py-rs-sh-to-hexa-porting.md`

## 결정

n6-architecture의 `.py` / `.rs` / `.sh` → `.hexa` 전면 포팅은 **현재 hexa-lang Phase 5 능력으로 수행 불가**. 아래 차단 항목이 해소될 때까지 보류한다.

## 검증된 도구체인 (Pilot-A 통과)

- 빌드 cwd: `~/Dev/hexa-lang` (필수)
- 명령: `./ready/self/hexa_bootstrap <src.hexa> -o <out>`
- 산출물: `<out>.c` + native binary
- 통과 기능: `let`, 정수 산술, 문자열 `+`, `to_string()`, **단일인수** `println()`

## 차단 항목 (Blockers)

### B-1. 다중 인수 `println` 미지원 (codegen_c2)

**증상:** `println("fib(", i, ") =", fib(i))` 컴파일 실패
**영향:** 거의 모든 .rs 계산기 (`println!("...{}...", x)` 형태가 표준)
**필요:** 가변 인수 println 또는 포맷 문자열 지원

### B-2. CLI argv 미지원

**증상:** `hexa_build.hexa`조차 `source_file = "examples/fibonacci.hexa"` 하드코딩 사용
**영향:**
- L1 `scripts/*.sh` 13개 — 거의 전부 `$1 $2` 사용
- L2 `tools/*calc/*.rs` ~30개 — 일부 argv 사용
**필요:** `args()` 또는 `argv` 표준 함수

### B-3. 포맷 스펙 부재

**증상:** Rust `{:<8}`, `{:>2}`, `{:.4}` 같은 정렬·정밀도 지정자 등가물 없음
**영향:** 거의 모든 L2 계산기의 표 출력
**필요:** `format!` / `printf` 류 또는 폭/정밀도 헬퍼 함수

### B-4. 부동소수 수학 함수

**증상:** `f64::powi`, `sqrt`, `sin`, `cos`, `ln`, `exp` 등 표준 라이브러리 함수 미확인
**영향:** 모든 물리/광학/핵융합 계산기 (L2 다수)
**필요:** `math` 모듈 또는 `extern` libm 바인딩

### B-5. 유니코드 리터럴 안정성 미확인

**증상:** `═`, `✓`, `✗`, 한글 등 비-ASCII 출력. 토큰화·C 코드 생성 시 escape 처리 미검증
**영향:** 거의 모든 리포 출력 (CLAUDE.md 한글 강제 규칙)
**필요:** UTF-8 안전 문자열 처리 명시

### B-6. for/range 루프와 destructuring

**증상:** Rust `for (name, rank, val, expr) in &gut_groups` 같은 구조분해 미확인
**영향:** L2 계산기 다수
**필요:** for-in, range, tuple destructuring

### B-7. 외부 명령 호출 (shell 대체용)

**증상:** `runtime.c`에 `exec()`은 있으나 stdout 캡처 / 종료코드 / 환경변수 / pipe 미확인
**영향:** L1 .sh 전부 (git/find/jq 호출이 본질)
**필요:** `Command::new` 또는 `exec_capture(cmd) → {stdout, stderr, code}` API

### B-8. 파일 시스템 / 디렉토리 순회

**증상:** `read_file`, `write_file`은 있으나 `glob`, `read_dir`, `exists`, `mkdir -p` 미확인
**영향:** L1 .sh 다수 (`find ... -name "*.json"`)
**필요:** `fs` 모듈

### B-9. JSON 파싱

**영향:** L1 .sh가 jq로 nexus/shared/*.json을 읽음. .hexa 포팅본도 동일 동작 필요
**필요:** `json::parse(str) → Value` 또는 외부 jq 호출 패턴 안정화

### B-10. ML 수치 스택 (L3/L4 차단)

**증상:** numpy/torch/scipy/matplotlib 상응 0
**영향:** L3 `techniques/*.py` 23개, L4 `experiments/*.py` 전부
**필요:** 별도 결정 — (a) HEXA용 ML 스택 신규 작성 / (b) Python FFI / (c) L3/L4 포팅 영구 보류

### B-11. 빌드 산출물 cleanup / 출력 경로

**증상:** `.c` 중간 파일이 소스 옆에 남음. `-I` 플래그가 `ready/self` 상대경로로 하드코딩 → cwd 의존
**영향:** 본격 sweep 시 빌드 디렉토리 오염, 비-hexa-lang cwd에서 빌드 불가
**필요:** `--include-dir` 옵션 또는 절대경로 / `--temp-dir` 분리

## 우선순위

| 우선 | 차단 항목 | 해소되면 가능해지는 것 |
|---|---|---|
| **P0** | B-1, B-2, B-11 | 기본 sweep 진입 |
| **P0** | B-3, B-4 | L2 sweep 가능 |
| P1 | B-5, B-6 | L2 품질 유지 |
| P1 | B-7, B-8, B-9 | L1 sweep 가능 |
| P2 | B-10 | L3/L4 — 별도 결정 사안 |

## 재개 조건

- **L2 sweep 재개:** P0 5건(B-1, B-2, B-3, B-4, B-11) 해소
- **L1 sweep 재개:** P0 + P1 3건(B-7, B-8, B-9) 해소
- **L3/L4 사안:** B-10에 대한 별도 사용자 결정 필요

## 잠정 조치

1. CLAUDE.md R1(HEXA-FIRST)은 **신규 코드 .hexa 강제** 규칙으로만 운영. 기존 자산은 동결.
2. 이 worktree(`/Users/ghost/Dev/n6-architecture-porting`, 브랜치 `porting/pilot-2026-04-08`)는 재개 시까지 보존. 파일럿 산출물 `.porting-pilot/hello.{hexa,c,exe}` 포함.
3. hexa-lang 측에 본 문서 링크 또는 issue로 전달 (사용자 결정).
