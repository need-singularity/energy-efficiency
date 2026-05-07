# hexa-lang 세션 handoff (2026-04-14)

canon ↔ hexa-lang 당일 양방향 handoff 기록.

## 문서 쌍

| 방향 | 파일 |
|------|------|
| n6 → hexa-lang | `~/Dev/hexa-lang/docs/from-canon-2026-04-14.md` |
| hexa-lang → n6 | `~/Dev/hexa-lang/docs/to-canon-2026-04-14.md` |

## 해소된 체크리스트 (5/5)

| # | 항목 | 결과 | 비고 |
|---|------|------|------|
| 1 | `~/.hx/bin/hexa` 심볼릭 | 완료 | stage0 1.8MB 로 업데이트 |
| 2 | `fn main()` auto-call | 확정 | build-only (T23). interpreter/bridge 는 수동 호출 유지 — n6 패턴 유효 |
| 3 | `.substr()` stdlib | 완료 | JS 스타일 `.substr(start, length)` working tree 적용 (clamp 포함) |
| 4 | `hexa build -I` 경로 | 오정보 정정 | stage0 에서 정상. 구 stage1 바이너리 문제였음 |
| 5 | arch_* bench 등록 | 접수 | T44 후 `arch_selforg.hexa` 50 샘플 bench 타겟. `examples/regressions/n6/` 심볼릭 생성 요청 |

## 정정 (3 커밋에 남은 오정보)

canon 커밋 메시지 3건에 "hexa runtime.c 누락" 문구 포함 — 전부 **오정보**:

- `df783ac1` feat(P1): go — 8 에이전트 병렬 발사
- `6e340386` feat(P2): go — 8 에이전트 병렬 (12 tasks done)
- `d494fac6` feat(P3): go — 8 에이전트 병렬 (9 tasks done)

실제 상황: `self/runtime.c` 3637줄 실존. 문제는 구 stage1 `hexa build` 가 `-I '/Users/ghost/.hx/bin/self'` 를 사용했는데 이 경로에 runtime.c 가 없었던 것. stage0 에서는 해결. 인터프리터 모드(`hexa <file>` / `hexa run`)는 처음부터 정상 동작.

git history 는 불변이나 본 문서가 신호원. 차기 커밋에서는 "parse + run 전수 PASS" 로 기록.

## 역요청 실행 (#5)

hexa-lang 측 요청: `examples/regressions/n6/` 심볼릭 디렉토리 생성 → 완료.

13 .hexa 파일 심볼릭:
- `arch_quantum/selforg/adaptive/unified.hexa` (engine/)
- `ouroboros_5phase/ecosystem_9projects.hexa` (bridge/)
- `rtl_top/rtl_soc_drc_lvs/rtl_tapeout_gate.hexa` (hexa-speak/proto/rtl/)
- `boot_matrix_3x12/verify_anima_soc/sim_noc_bott8_1Mcycle.hexa` (chip-verify/)
- `atlas_promote_7_to_10star.hexa` (scripts/)

canon 원본 변경이 자동으로 hexa-lang regression set 에 반영됨 (심볼릭).

README: `/Users/ghost/core/hexa-lang/examples/regressions/n6/README.md`

## ARENA=1 bench 수락 조건

- 기존 결과 공유 받음: fib -3.7% / struct RSS -30%
- arch_selforg.hexa 50 샘플 별도 wave 예정
- T44 후속 + canon P4 (미정) 시 재만남

## 패턴 확정 (이번 세션 결정)

1. **main() 수동 호출 유지**: n6 13 파일 전부 최하단 `main()` 호출 계속 사용. interpreter 호환성 보장.
2. **`.substr()` 사용 가능 지점 대비**: `bridge/ecosystem_9projects.hexa` `pad_r()` 헬퍼는 차기 hexa-lang stdlib 릴리즈 후 리팩터링 가능.
3. **build 는 stage0 사용 필수**: 구 stage1 은 build 경로 이슈. stage0 심볼릭이 정상화됐으므로 `hexa build <file> -o <bin>` 을 차기 세션부터 사용 가능.

## 역방향 기여 합의

- `arch_unified.hexa` 4-mode dispatch → hexa-lang 공식 multi-mode 프레임워크 사례
- `ecosystem_9projects.hexa` growth_bus append-only → 세션 간 발견 공유 인프라
- blowup Mk.II (`canonshared/blowup/core/blowup.hexa`) 공진화 합의

## 메모리 업데이트 대상

- `feedback_hexa_lang_dse_recheck.md` — stage0 바이너리 확인 추가
- `project_hexa_coevolution.md` — 이번 세션 P1~P3 기여 반영
- 신규: `reference_hexa_build_runtime_fix.md` — build 경로 이슈 해소 기록

## 타임라인

- 2026-04-14 09:00~ canon P1 8 에이전트 발사
- 2026-04-14 ~11:30 P1 12 tasks done + 커밋 push
- 2026-04-14 ~13:00 P2 8 에이전트 발사
- 2026-04-14 ~17:00 P2 12 tasks done
- 2026-04-14 ~18:30 P3 8 에이전트 발사
- 2026-04-14 ~20:30 P3 9 tasks done (47 total)
- 2026-04-14 21:00~ hexa-lang handoff 쌍 교환
- 2026-04-14 21:55 `examples/regressions/n6/` 심볼릭 생성 (역요청 완료)

## 8. stage0 실전 재검증 결과

- 일자: 2026-04-14 (추가 세션)
- 바이너리: `/Users/ghost/core/hexa-lang/build/hexa_stage0` (arm64, 1.8 MB, 21:52 mtime)
- 리포트: `experiments/chip-verify/stage0_rerun_report.md`
- 결과: 13 / 13 파일 stage0 실전 실행 rc=0 성공, stderr 0 건
  - A류 5 파일 (파일 하단 `main()` 호출 포함): 원본 그대로 실행 -> 풍부한 출력 + 검증 통과
    - arch_quantum (EXACT 10/10), arch_selforg (50 SAMPLE), arch_adaptive (EXACT 10/10 승격), ouroboros_5phase (승격 15 건), ecosystem_9projects (9/9)
  - B류 1 파일 (main 내부 println 미사용): arch_unified.hexa — rc=0 이지만 stdout 0 (의도된 무출력, main return total)
  - C류 7 파일 (fn main 은 있으나 하단 `main()` 호출 부재): 임시 복제본 끝에 `main()` 추가 harness 로 재실행 -> 모두 통과
    - top 7/7, soc_integration 6/6, soc_drc_lvs 12/12, tapeout_gate 15/15, verify_chip-3d 5/5, verify_anima_soc 12/12, boot_matrix_3x12 34/36 (94%)
- 정정 사항: 과거 P1~P3 산출물 주석/.md 에서 "runtime.c 누락 -> parse 전용 검증" 이라 기술한 부분은 오판이었다. 원인은 구 stage1 `hexa build` 경로의 버그이며, stage0 인터프리터/run 모드는 처음부터 정상 동작. 이후 기준 문구는 "stage0 실전 실행 결과" 이다.
- 권장: C류 7 파일 원본에 최하단 `main()` 한 줄 추가. arch_unified 는 main 반환값을 println 으로 노출.

문서 끝.
