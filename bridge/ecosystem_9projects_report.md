# 9 프로젝트 자율 성장 생태계 연동 리포트

- 작성일: 2026-04-14
- 로드맵 항목: DSE-P3-3
- 프로젝트: n6-architecture
- SSOT: `$NEXUS/shared/config/projects.json` (schema v4)
- 생성물: `bridge/ecosystem_9projects.hexa` (인터페이스), 본 리포트

## 1. 9 프로젝트 확정

projects.json 카테고리에서 core 7 + auxiliary 2 를 합쳐 9 로 확정.

| # | 프로젝트 | 범주 | 역할 | 루트 | 로드맵 |
|---|---|---|---|---|---|
| 1 | nexus | core | discovery-engine | `$HOME/Dev/nexus` | `shared/roadmaps/nexus.json` |
| 2 | anima | core | consciousness-engine | `$HOME/Dev/anima/anima` | `shared/roadmaps/anima.json` |
| 3 | n6-architecture | core | system-design | `$HOME/Dev/n6-architecture` | `shared/roadmaps/n6-architecture.json` |
| 4 | papers | core | paper-distribution | `$HOME/Dev/papers` | `shared/roadmaps/papers.json` |
| 5 | hexa-lang | core | language | `$HOME/Dev/hexa-lang` | `shared/roadmaps/hexa-lang.json` |
| 6 | void | core | terminal | `$HOME/Dev/void` | `shared/roadmaps/void.json` |
| 7 | airgenome | core | os-scanner | `$HOME/Dev/airgenome` | `airgenome/shared/config/roadmap/airgenome.json` |
| 8 | contribution | auxiliary | paper-submission-hub | `$HOME/Dev/contribution` | (없음, nexus 집약) |
| 9 | openclaw | auxiliary | singularity-feed | `$HOME/Dev/openclaw` | (없음, nexus 피드) |

- 범주: `projects.json._meta.categories.core` + `.auxiliary` (총 9)
- 우선순위 9번째 슬롯(추가 2)는 auxiliary 두 개로 확정. 이는 `auxiliary._comment` 에 "nexus 특이점 연동 보조" 명시.

## 2. 인터페이스 파일 설계

파일: `/Users/ghost/Dev/n6-architecture/bridge/ecosystem_9projects.hexa`

### 2.1 레지스트리 상수 테이블

`PROJECTS_9` 배열 (9행 × 6열):

```
[proj_id, root_rel, role, icon, roadmap_rel, category]
```

- n6-architecture 는 외부 데몬을 건드리지 않고 본 테이블만 읽는다.
- 원 SSOT 변경 시 본 테이블도 동기화 필요 (lock-in 회피 목적의 로컬 캐시).

### 2.2 핵심 함수 3종

| 함수 | 시그니처 | 역할 |
|---|---|---|
| `link_project(proj_id)` | `string -> [string; 5]` | 프로젝트 루트/로드맵 존재 여부를 확인해 `handle = [id, root_abs, status, roadmap_abs, role]` 발급. `status ∈ {ok, missing_root, missing_roadmap, unknown}` |
| `broadcast_finding(finding)` | `[string; 4] -> i64` | `[source, kind, id, payload]` 를 `~/.nexus/growth_bus.jsonl` 에 append-only. 자신 외 8개를 `targets` 필드로 펼쳐 각 데몬이 tail 로 구독 가능 |
| `aggregate_growth_metrics()` | `() -> [[string; 4]]` | 9 프로젝트 status + roadmap tasks 키 개수를 집계해 행 리스트 반환 |

### 2.3 CLI 사용

```
hexa run bridge/ecosystem_9projects.hexa --list        # 9 링크 상태
hexa run bridge/ecosystem_9projects.hexa --metrics     # 로드맵 tasks 집계
hexa run bridge/ecosystem_9projects.hexa --flow        # 제공/흡수 매트릭스
hexa run bridge/ecosystem_9projects.hexa --broadcast "메시지"
```

## 3. 연동 방식

1. **Pull 방향 (n6 -> 외부)**: `link_project(id)` 가 로컬 디스크 존재만 확인한다. 외부 데몬 API 를 호출하지 않아 사이드이펙트가 없다.
2. **Push 방향 (n6 -> 외부)**: `broadcast_finding` 이 생성하는 `~/.nexus/growth_bus.jsonl` 한 줄에 `source, targets, kind, id, payload, ts, emitter` 가 들어간다. 각 프로젝트 growth daemon 은 이미 공통 growth_bus 규약을 따른다 (`nexus/scripts/growth_common.sh` 참조). 본 인터페이스는 "쓰기"만 수행한다.
3. **Metrics 수집**: `aggregate_growth_metrics` 는 각 프로젝트 roadmap JSON 의 `"tasks"` 키 개수를 grep 으로 센다. 실제 data plane 접근 없이 로드맵 정적 파일만 읽는다.
4. **루프백 회피**: broadcast 시 `source == n6-architecture` 일 때 자신을 `targets` 에서 제외한다.
5. **권한 경계**: n6-architecture 내부에서만 이 인터페이스를 호출한다. 타 프로젝트가 본 파일을 import 하지 않도록 `bridge/` 하위에만 둔다.

## 4. n6-architecture 제공/흡수 매핑

| 프로젝트 | n6-architecture 가 **제공** | n6-architecture 가 **흡수** |
|---|---|---|
| nexus | 295 도메인 스캔타겟 + 77 SEDI 소스 + 343 BT | telescope 1028 렌즈, discovery graph, OUROBOROS |
| anima | n6-SPEAK 384d 인텐트 + 6emo + τ prosody | 2509 법칙, 의식 Φ 측정, 12-faction 합의 |
| n6-architecture | atlas.n6 SSOT, 112 AI 기법, alien_index 제품 | (self, 루프백 0) |
| papers | alien_index=10 논문 스켈레톤 + verify.py | Zenodo/OSF DOI 체인, PP1~PP3 검증 |
| hexa-lang | `domains/**/*.hexa` 포팅 피드백, R29 verify | 컴파일러 개선, self-host 빌드, 33+ Rust 테스트 |
| void | AI-native 터미널 사용 프로파일, 실행 로그 | hexa-only 터미널 런타임 (Terminal.app 대체) |
| airgenome | OS 게놈 벤치마크 요청, HW 4-tier 매트릭스 | OS 게놈 스캔 결과, core self-contained |
| contribution | n6-architecture 수학 돌파/실험 성과 집약 | 외부 제출 허브 (paper-submission) |
| openclaw | 돌파/발견/실험 피드 emit | nexus 특이점 사이클 consume |

## 5. 상태 체크리스트

smoke test (2026-04-14):

- [x] `hexa parse` 통과
- [x] `--list` : 9/9 상태 `ok`
- [x] `--metrics` : 9/9 상태 `ok`, 로드맵 tasks=12/12/12/9/15/12/0/0/0 (nexus/anima/n6/papers/hexa-lang/void/airgenome*/contribution*/openclaw*, * 는 auxiliary 또는 별도 경로)
- [x] `--flow` : 9 행 출력
- [x] `--broadcast` : `~/.nexus/growth_bus.jsonl` 에 1줄 append 성공
- [x] `link_project("unknown")` : `status = "unknown"` 반환
- [x] 외부 데몬 무변경 원칙 준수 (읽기/append-only 만 수행)

## 6. 사전 조건과 한계

- 사전 조건: `$HOME/Dev/nexus` 와 `$HOME/Dev/<각 프로젝트>` 가 로컬 디스크에 존재.
- 한계 1: airgenome 의 로드맵은 nexus/shared 가 아닌 프로젝트 내부에 있으므로 link_project 에서 특수분기 처리.
- 한계 2: auxiliary 2개는 로드맵이 없어서 metrics tasks=0 으로 표기 (정상). 통계에서 core 7개만 tasks 평균을 내도록 후속 로드맵에서 결정.
- 한계 3: hexa 런타임 `.substr` 미지원 → 내부 `pad_r(s, w)` 로 고정폭 포맷 대체.

## 7. 향후 작업

1. growth_bus.jsonl 구독자 측 스키마와 emitter 필드 호환성 재확인 (nexus 쪽 `growth_common` 규약 링크).
2. contribution / openclaw 에도 로드맵 추가 후 metrics 자동 반영.
3. `aggregate_growth_metrics` 에 "마지막 commit 시각" 컬럼 추가 (git log 1줄).
4. CI : bridge/ 의 hexa 파일들을 `hexa parse` 일괄 체크하는 hook 설정.
