# arch_unified.hexa — 4 모드 통합 아키텍처 DSE (P3-1)

## 개요

canon 프로젝트 DSE-P3-1 단계 산출물. 기존 v1(산업실증), v2(양자중첩), v3(자기조직), v4(진화적응) 4개 아키텍처 엔진을 단일 오케스트레이터에서 선택/전환/혼합 가능하도록 통합한 파이프라인 엔진이다.

- 경로: `/Users/ghost/core/canon/engine/arch_unified.hexa`
- 포팅 상태: BODY (외부 import 없음, 순수 정수 연산)
- 검증: stage0 실전 실행 결과 rc=0 (2026-04-14 재검증, main 은 total 반환, println 미사용)
- 규칙: R1 HEXA-FIRST, R18 미니멀, N61 한글

## 4 모드 표

| 코드 | 모드         | 의미             | 원본 엔진                  | 성숙도 | 기반 원리                                             |
| ---- | ------------ | ---------------- | -------------------------- | ------ | ----------------------------------------------------- |
| 1    | INDUSTRIAL   | 산업실증 (v1)    | (P0 220/220 EXACT 골화)    | 7      | 170 chip-architecture + 50 network-protocol 실측      |
| 2    | QUANTUM      | 양자중첩 (v2)    | `arch_quantum.hexa`        | 4      | n_superpose 후보 → n=6 argmax 붕괴 (collapse)         |
| 3    | SELFORG      | 자기조직 (v3)    | `arch_selforg.hexa`        | 5      | 6 부품 국소 규칙 결합 → 집단 창발 gain                |
| 4    | ADAPTIVE     | 진화적응 (v4)    | `arch_adaptive.hexa`       | 6      | G 세대 mutation + fitness 선발, atlas.n6 승격 hook    |

성숙도 수치는 `fuse_modes` 의 weight 가중치로 사용된다 (10 단위 정수).

## 모드 전환 규칙 (select_mode)

환경 입력은 3 필드 정수 팩으로 표현한다 (0~1000 SCALE).

- `env_certainty`: 0=불확실, 1000=확정
- `env_drift`:     0=정적, 1000=동적
- `env_scale`:     0=국소, 1000=대규모

결정 트리:

```
1) env_certainty >= 750 AND env_scale >= 750 -> INDUSTRIAL (v1)
2) env_certainty <  500                      -> QUANTUM    (v2)
3) env_drift     <  400                      -> SELFORG    (v3)
4) 그 외                                      -> ADAPTIVE   (v4)
```

시나리오 예:
- `(900, 200, 900)` 확정대규모 -> `INDUSTRIAL`
- `(300, 500, 500)` 불확실        -> `QUANTUM`
- `(800, 700, 500)` 동적진화      -> `ADAPTIVE`

## Fusion 매트릭스 (fuse_modes)

2 모드 혼합 공식:

```
hybrid = (score_a * weight_a + score_b * (10 - weight_a)) / 10
```

| mode_a \ mode_b | INDUSTRIAL (w=7) | QUANTUM (w=4) | SELFORG (w=5) | ADAPTIVE (w=6) |
| ---------------- | ----------------- | -------------- | -------------- | --------------- |
| INDUSTRIAL (w=7) | 1.0*I             | 0.7*I + 0.3*Q  | 0.7*I + 0.3*S  | 0.7*I + 0.3*A   |
| QUANTUM    (w=4) | 0.4*Q + 0.6*I     | 1.0*Q          | 0.4*Q + 0.6*S  | 0.4*Q + 0.6*A   |
| SELFORG    (w=5) | 0.5*S + 0.5*I     | 0.5*S + 0.5*Q  | 1.0*S          | 0.5*S + 0.5*A   |
| ADAPTIVE   (w=6) | 0.6*A + 0.4*I     | 0.6*A + 0.4*Q  | 0.6*A + 0.4*S  | 1.0*A           |

`main()` 데모에서 2 조합을 실행한다:
1. `fuse_modes(INDUSTRIAL, QUANTUM, 48)` → 0.7 I + 0.3 Q
2. `fuse_modes(SELFORG, ADAPTIVE, 48)`   → 0.5 S + 0.5 A

## 파이프라인 stub 수식 요약

모든 stub 은 n=6 상수(sigma=12, tau=4, phi=2, sopfr=5)에서만 score 를 유도하며 자기참조를 금지한다.

- `pipe_industrial(input)`: `base = sigma(6)*tau(6) = 48`, `score = SCALE - |input-48|*10`
- `pipe_quantum(input)`: 3 후보 `input ± tau(6)` 에서 argmax
- `pipe_selforg(input)`: `group = input*phi(6) + sigma(6)`, `solo = input + sigma(6)/2`, `score = 500 + (group-solo)*5`
- `pipe_adaptive(input)`: `target = sigma(6)+tau(6) = 16`, 3 세대 변이 후 `score = SCALE - |gene-target|*sopfr(6)*10`

## hexa parse 결과

```
$ hexa parse /Users/ghost/core/canon/engine/arch_unified.hexa
OK: /Users/ghost/core/canon/engine/arch_unified.hexa parses cleanly
```

구문 검증 완료. 런타임 검증은 runtime.c 복구 후 후속 단계에서 `hexa run` 으로 수행한다.

## 후속 단계 (P3-2 대기)

- runtime.c 복구 후 `hexa run` 실제 실행 + score 분포 수집
- 4 모드 실측값과 `arch_quantum.hexa` / `arch_selforg.hexa` / `arch_adaptive.hexa` 원본 엔진 score 대조
- INDUSTRIAL 모드는 `chip-architecture` / `network-protocol` 실제 DSE 계산기와 직결
- atlas.n6 `[7]->[10*]` 승격 훅을 통합 파이프에서 일관되게 호출
