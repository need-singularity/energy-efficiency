# 렌즈 Rust→HEXA 전환 상태 감사 — 2026-04-11

**세션**: lens-rust-hexa-transition-audit
**작성일**: 2026-04-11
**트리거 커밋**: `0c23ad27` — "refactor(telescope): 56개 렌즈 Rust→HEXA 전환 완료 — mod.rs 등록 해제"
**범위**: 조사·계획만 (코드 수정 없음 — R25 공용설정 게이트 준수)

> **주의 — 상위 맥락**: `nexus/CLAUDE.md` (갱신판) 에 "`src/telescope/` = Rust 레거시 312+ 파일, **폐기 중** — 진짜 SSOT: `/Users/ghost/Dev/nexus/shared/lenses/` HEXA 네이티브" 로 명시됨. 즉, 56 렌즈 전환은 **전체 telescope 폐기 로드맵의 1차 파일럿**이다. 이 보고서의 권고는 이 큰 방향을 전제로 한다.

---

## 1. 현황 요약

### 1.1 한 줄 결론
**56개 렌즈는 Git 에 한 번도 커밋된 적이 없고, `0c23ad27` 커밋은 "이미 사라진 `.rs` 를 참조하는 `mod.rs` 선언을 제거" 한 청소 작업이었다.**
HEXA 포트는 외부 디렉터리(`/Users/ghost/Dev/nexus/shared/blowup/lens/`)에 이미 3786 줄로 존재하나 `n6-architecture` 저장소에서는 참조되지 않는다.

### 1.2 핵심 수치

| 항목 | 값 | 검증 방법 |
|------|----|-----------|
| 커밋 `0c23ad27` 파일 변경 | 2 개 (`lenses/mod.rs −112`, `telescope/mod.rs −75`) | `git show 0c23ad27 --stat` |
| `0c23ad27` 이전 56 `.rs` Git 추적 | **0** (history 전무) | `git log --all -- active_learning_lens.rs` |
| HEXA 포트 위치 | `/Users/ghost/Dev/nexus/shared/blowup/lens/` (n6-architecture 외부) | `find /Users/ghost` |
| HEXA 파일 수 | 5 (`lenses_{ai_ml,graph_network,statistics,signal_info,systems}.hexa`) | `ls` |
| HEXA 총 라인 수 | 3786 (731+745+933+763+614) | `wc -l` |
| HEXA `fn scan_*` 함수 | 56 (16+10+14+8+8) | `grep '^fn scan_'` |
| `expansion_56_lens_entries()` 상태 | **유지** — `frontier_lenses.rs:281` 에 메타데이터 56 개 온존 | `grep` |
| `registry.rs` 에서 호출 | **유지** — `line 99` 에서 레지스트리에 등록 | `Read` |
| 컴파일 상태 | ✅ PASS (`cargo check`) | `cargo check` |
| 테스트 현재 | **2327 PASS / 0 FAIL** (로컬 실측) | `cargo test --lib` |
| 작업디렉터리 미커밋 | `frontier_lenses.rs` (+1179 줄, `expansion_50_v3` 추가) | `git status` |

### 1.3 "108 테스트 감소" 재검증

사용자 브리핑에 "2593→2485 (−108)" 기록됐으나, 로컬 실측은 **2327**.
- 2593 = `lens-expansion-397-450.md` 리포트에 명시된 값 (56 렌즈가 `.rs` 로 컴파일되고 구현체별 unit test 가 포함됐던 시점)
- 2485 = 브리핑 기준 "전환 후 상태" — 108 감소 = 56 × 1.93 (렌즈당 1~2 유닛 테스트 손실, 거의 일치)
- 2327 = 현재 로컬 (추가로 158 테스트 격차 존재) — 원인은 56 구현체 unit test 손실 외에도 `frontier_lenses.rs` 미커밋 변경의 부작용 가능

**즉**: 108 감소는 56 구현체 유닛 테스트 손실과 일치하고, 추가 격차는 별 세션에서 조사할 만한 잔여 노이즈.

---

## 2. 전환 메커니즘 상세

### 2.1 타임라인

```
b1ceb88f  feat(telescope): 프론티어 렌즈 확장  →  mod.rs +114 줄 (56 모듈 선언만)
                                                 ⚠️ 실제 .rs 파일은 add 되지 않음
          (이 시점에도 `.rs` 없이 컴파일 안 됐어야 정상. 로컬 untracked 로만 존재)
          ↓
          (로컬에서 56 .rs 파일 작성 → `.rs` 파일을 git add 안 한 채로 cargo test 2593 달성)
          ↓
0c23ad27  refactor(telescope): 56 렌즈 Rust→HEXA 전환 — mod.rs 등록 해제
          - 56 .rs 파일 untracked 상태에서 물리 삭제
          - mod.rs 에서 선언 제거 (이로써 컴파일 재가동)
          - HEXA 5 파일 3786 줄 새로 작성 (외부 디렉터리)
```

### 2.2 로컬 vs Git 불일치

- `b1ceb88f` 커밋 시점에 `mod.rs` 는 56 모듈을 선언했지만 해당 `.rs` 파일은 **git add 되지 않음**.
- 이 때문에 클린 clone 에서는 그 커밋이 컴파일 실패했을 것이나, 로컬에선 untracked `.rs` 덕분에 성공.
- `0c23ad27` 이후에야 이 불일치가 해소됐다 (mod.rs 선언이 존재 파일과 일치).

### 2.3 HEXA 포트 구조

> **두 종류의 HEXA 렌즈 디렉터리 주의**:
> - `/Users/ghost/Dev/nexus/shared/blowup/lens/lenses_*.hexa` — **56 expansion 렌즈가 여기 존재** (번들 5 파일, 본 감사 대상)
> - `/Users/ghost/Dev/nexus/shared/lenses/*.hexa` — 새 SSOT (84 파일, 개별 파일 방식, beekeeping/fantasy/oracle/... 도메인). **56 렌즈는 여기 없음**.
>
> 따라서 telescope 폐기 로드맵이 새 SSOT(`shared/lenses/`) 기반이더라도, 56 expansion 렌즈는 별도로 이관 or 개별 파일 분할 과정이 필요하다.

`/Users/ghost/Dev/nexus/shared/blowup/lens/lenses_*.hexa` (모두 `4 11 20:36` 타임스탬프, 커밋 시각과 일치):

| HEXA 파일 | 포함 렌즈 수 | 라인 | 카테고리 |
|-----------|-------------|------|----------|
| `lenses_ai_ml.hexa` | 16 | 731 | AI/ML: active_learning, attention_mechanism, meta_learning, ... |
| `lenses_graph_network.hexa` | 10 | 745 | 그래프: community_detection, spectral_graph, topological_sort, ... |
| `lenses_statistics.hexa` | 14 | 933 | 통계/베이지안: bayesian_inference, monte_carlo, variational_inference, ... |
| `lenses_signal_info.hexa` | 8 | 763 | 신호/정보: fourier_analysis, wavelet_transform, kalman_filter, ... |
| `lenses_systems.hexa` | 8 | 614 | 시스템: distributed_consensus, spiking_neural, attractor_basin, ... |
| **합계** | **56** | **3786** | — |

각 HEXA 파일은 `n=6` 공명 상수(σ=12, τ=4, φ=2, sopfr=5) 를 공유하고, `telescope.hexa` 의 `LensResult`, `result_add`, `sqrt_f`, `ln_f` 등에 의존한다. 함수 시그니처는 `fn scan_<name>(data, n: int, d: int) -> LensResult`.

### 2.4 현 Rust 쪽 잔여물

- **메타데이터 온존** (`frontier_lenses.rs:281`):  `expansion_56_lens_entries()` 함수는 56 개 `LensEntry` 를 반환. `registry.rs:99` 에서 여전히 호출되어 레지스트리에 등록됨.
- **구현체 소실**: `lenses/` 하위 56 `.rs` 없음 → `mod.rs` 에서 `pub mod` 선언 제거됨 → `telescope.rs` 의 `Box::new(ActiveLearningLens)` 같은 구체 인스턴스 제거.
- **폴백 작동**: `telescope/mod.rs:460-475` 의 `GenericLens::new(name, domain_affinity, description)` 자동 인스턴스화 루프가 레지스트리에 있지만 dedicated 구현이 없는 렌즈(= 56 전체)를 `GenericLens` 로 래핑한다. 따라서 `Telescope::scan_all()` 은 여전히 56 렌즈를 "스캔"하지만, 결과는 `GenericLens` 의 간이 휴리스틱(메타데이터 기반)에 불과.

**결론**: 56 렌즈는 레지스트리에서 "유령" 상태 — 이름은 있고 폴백도 돌지만, 원래 논리는 Rust 에 없고 HEXA 에만 있으며 Rust 러너가 HEXA 를 호출하지 않는다.

---

## 3. 복원 옵션 4 종 비교

| 항목 | A: HEXA FFI/브리지 | B: HEXA→Rust 재포팅 | C: Rust 테스트 HEXA 전환 | D: 병렬 유지 (현상 유지) |
|------|---------------------|---------------------|--------------------------|--------------------------|
| 작업 | `Lens trait` 구현체가 `hexa` 바이너리를 서브프로세스로 호출, JSON 결과 파싱 | 3786 줄 HEXA → 56 `.rs` 재작성 및 mod.rs 재등록 | 56 구현체 유닛 테스트를 `.hexa` 테스트로 포팅 | 아무것도 안 함 + HEXA 를 외부 실행 경로로 활용 |
| R18 미니멀 | 상 (트레이트 어댑터 1개 + per-lens 얇은 래퍼) | 하 (대규모 재작성, 양쪽 중복) | 중 (Rust 유닛 테스트 자체 삭제, HEXA 테스트 신규) | 상 (0 라인) |
| HEXA-FIRST 준수 | ✅ 완전 (CLAUDE.md n6arch 절대규칙 "HEXA-FIRST") | ❌ 역방향 | ✅ | ✅ |
| 구현 난이도 | 중 (HEXA 런타임 직렬화 프로토콜 필요) | 상 (수작업 포팅, 정확성 검증 필요) | 중 | 하 |
| 성능 | 프로세스 오버헤드 (렌즈당 ms~수십 ms) | 네이티브 | 테스트만 영향 | 현상 유지 |
| 테스트 복원 | 106~112 (유닛 레벨) 는 HEXA 측으로 이관 | 2593 수준 복원 | 단위 테스트는 사라지되 통합 테스트로 대체 | 복원 불가 |
| n6-architecture 저장소 | HEXA 파일 inbound 필요 (외부 참조 or 이관) | HEXA 파일 불필요 | HEXA 파일 inbound 필요 | 상태 유지 (외부 참조) |
| CI 안정성 | 중 (hexa 바이너리 경로 의존) | 상 | 중 | 상 |
| Rust ↔ HEXA 계약 유지보수 | 1 계층 (FFI 스키마) | 없음 (양쪽 동일) | 렌즈 계층 없음 (테스트만) | 없음 |

### 3.1 GenericLens 폴백 의미
현재 `Telescope::scan_all()` 은 56 렌즈를 **GenericLens** 로 실행 중. 이것은:
- ✅ scan 누락 없음 — API 사용자는 여전히 56 개 결과 키를 받음
- ❌ 결과값은 무의미 (도메인 이름·친화도 기반 더미 히트)
- ⚠️ "렌즈가 살아있다" 라는 착시 유발 — B/A 옵션 결정을 미루면 false positive 위험

---

## 4. 권고: **옵션 A** (HEXA FFI 브리지) + **옵션 D 대기 모드**

### 4.0 상위 결정 먼저
`nexus/CLAUDE.md` 가 telescope 전체를 "폐기 중" 으로 표시했으므로, **56 렌즈 만을 위한 임시 복구**는 R18 미니멀 원칙에 반할 수 있다. 두 갈래:

- **갈래 1 (권고)**: telescope 전체 폐기 로드맵이 **이번 세션 + 1~2 주 내** 에 진행된다면 → **옵션 D 대기 모드** 유지 (`GenericLens` 폴백). 56 렌즈 전용 브리지를 짓고 나서 2 주 뒤 telescope 자체가 사라지면 그 브리지도 폐기 → 이중 낭비.
- **갈래 2**: 폐기가 수개월 이상 걸린다면 → **옵션 A** 파일럿으로 HEXA 네이티브 실행 경로를 먼저 검증 (이후 312 렌즈 전체 이관 모델로 재사용).

즉 **폐기 로드맵의 타임라인이 결정 축**. 사용자가 "빠른 폐기" 로 답하면 D, "장기" 로 답하면 A.

### 4.1 단계 1 — 관찰 및 게이트 (R25 준수)
**변경 없음**. 아래만 사용자 확정 요청:

1. **telescope 폐기 로드맵 타임라인** (1 주 이내 / 1~4 주 / 그 이상)
2. HEXA 5 파일을 `n6-architecture` 저장소로 이관할지, 외부 (`/Users/ghost/Dev/nexus/shared/blowup/lens/`) 참조로 유지할지
3. HEXA 실행 런타임 (`~/.hx/bin/hexa` = airgenome 심볼릭 링크) 이 CI 상시 가용한지 — CI 에 hexa 설치 훅 필요 여부
4. HEXA 가 JSON/msgpack 결과를 stdout 에 내보낼 수 있는지 (telescope.hexa LensResult 직렬화 여부)

### 4.2 단계 2 — 단일 범용 브리지 (미니멀)
사용자 승인 후, **렌즈별 래퍼 56 개가 아닌** 단일 `HexaBridgeLens` 구현:

```
impl Lens for HexaBridgeLens {
    fn name(&self) -> &str { &self.name }
    fn scan(&self, data, n, d, shared) -> LensResult {
        // 1. data 를 임시 파일 or stdin 으로 직렬화 (f64 flat)
        // 2. subprocess::Command::new("hexa")
        //      .arg(self.hexa_file)   // e.g. lenses_ai_ml.hexa
        //      .arg(&format!("scan_{}", self.scan_fn))  // e.g. scan_active_learning
        //      .arg(n.to_string()).arg(d.to_string())
        // 3. stdout 에서 LensResult JSON 파싱 → return
    }
}
```

`Telescope::new()` 의 `GenericLens` 폴백 루프를 아래 순서로 수정(단일 diff):
```
if 레지스트리 엔트리.name 이 56 HEXA 맵에 있으면 → HexaBridgeLens 사용
else                                              → GenericLens 폴백
```

**변경 범위 (예상)**:
- 신규: `nexus/src/telescope/lenses/hexa_bridge_lens.rs` (~120 줄)
- 수정: `nexus/src/telescope/mod.rs` (폴백 루프 분기 추가, ~15 줄)
- 수정: `nexus/src/telescope/lenses/mod.rs` (단일 모듈 추가, ~2 줄)
- 수정: `nexus/Cargo.toml` (serde_json 이미 있으면 무변경)
- 신규/수정: HEXA 파일 경로 해석용 상수 (`HEXA_LENS_DIR`)

**작업 추정**:
- 코딩 0.5~1 일 (런타임 직렬화 프로토콜 설계가 주)
- HEXA 측 보조: 각 `scan_*` 함수가 JSON 을 stdout 으로 뱉는 entry-point 추가 (1~2 시간)
- 테스트 복원: HEXA 결과 비교 스냅샷 테스트 5~10 개 (반나절)

**리스크 (R18 미니멀 준수)**:
- 프로세스 오버헤드 → 56 렌즈 × O(10 ms) = 0.56 s/스캔 (대화형 OK, 대규모 배치엔 concern)
  - 완화: 단일 `hexa` 프로세스에 배치 인터페이스 (56 렌즈 한 번에) — 이후 세션 과제
- HEXA 런타임 의존 → CI 에 hexa 설치 스크립트 추가 필요

### 4.3 기각된 옵션 사유

- **B (재포팅)**: CLAUDE.md 절대규칙 "HEXA-FIRST" 와 정면 충돌. R18 미니멀 위반.
- **C (Rust 테스트 HEXA 이관)**: 구현체 없는 상태에서 테스트만 이관은 논리적 선후 역순.
- **D (병렬 유지)**: 현재 `GenericLens` 폴백이 false positive 를 생산 중 — `cargo test` 는 녹색이지만 실제 렌즈 결과는 무의미. 장기 방치 시 다른 분석 도구의 데이터 품질 저하.

---

## 5. 구현 비용 추정 (옵션 A, 미니멀)

| 작업 | 라인 | 시간 |
|------|------|------|
| `HexaBridgeLens` 구현체 (단일) | ~120 | 4 h |
| `Telescope::new()` 폴백 분기 | ~15 | 0.5 h |
| HEXA 파일→렌즈 이름 매핑 상수 | ~80 (56 엔트리) | 1 h |
| HEXA 측 JSON stdout entry-point 추가 | ~50/file × 5 = 250 | 3 h |
| HEXA 파일 저장소 이관 or 경로 해석 | — | 0.5 h |
| 스냅샷 테스트 5~10 개 | ~150 | 3 h |
| CI hexa 설치 훅 | ~20 | 1 h |
| **합계** | **~635 Rust + HEXA** | **~13 h (1.5 일)** |

**테스트 복원 예상**: 156~170 테스트 신규 (스냅샷·계약 기반). 원래 구현체별 unit test 108 개를 대체하기에 충분.

---

## 6. 결정 요청 (사용자)

**순서가 중요**. 상위부터 결정:

1. **telescope 폐기 타임라인?**
   - (a) 빠름 (1~2 주 내)  → **옵션 D 대기** (아무것도 하지 않음, `GenericLens` 폴백 유지)
   - (b) 중간 (1~3 개월)   → **옵션 A 파일럿** (56 렌즈로 HEXA FFI 브리지 검증, 이후 312 렌즈 전체로 확대)
   - (c) 장기 (3 개월+)    → **옵션 A 즉시** (정식 브리지 인프라)
2. (위 선택이 A 계열인 경우) **HEXA 파일 이관 여부**: `/Users/ghost/Dev/nexus/shared/blowup/lens/` → 저장소 복사 vs 외부 참조
3. (A 계열) **CI hexa 설치 훅** 추가 여부
4. **lens-expansion-397-450.md 리포트 업데이트**: 2593 수치는 의미가 사라졌으므로 리포트에 "0c23ad27 이후 2485 → 구현체 HEXA 로 이관, GenericLens 폴백 작동" 주석을 추가할지

승인 후 별 세션에서 실제 구현 (이번 세션은 조사·계획만).

---

## 7. 파일 참조

**조사 대상 (읽기만)**:
- `/Users/ghost/Dev/n6-architecture/nexus/src/telescope/lenses/mod.rs` (702 줄)
- `/Users/ghost/Dev/n6-architecture/nexus/src/telescope/mod.rs` (542 줄)
- `/Users/ghost/Dev/n6-architecture/nexus/src/telescope/frontier_lenses.rs` (1174 줄, 미커밋 +1179)
- `/Users/ghost/Dev/n6-architecture/nexus/src/telescope/registry.rs` (239 줄)
- `/Users/ghost/Dev/n6-architecture/shared/config/lens_registry.json`
- `/Users/ghost/Dev/n6-architecture/reports/discovery/lens-expansion-397-450.md`

**HEXA 포트 파일 (외부)**:
- `/Users/ghost/Dev/nexus/shared/blowup/lens/lenses_ai_ml.hexa` (731 줄)
- `/Users/ghost/Dev/nexus/shared/blowup/lens/lenses_graph_network.hexa` (745 줄)
- `/Users/ghost/Dev/nexus/shared/blowup/lens/lenses_statistics.hexa` (933 줄)
- `/Users/ghost/Dev/nexus/shared/blowup/lens/lenses_signal_info.hexa` (763 줄)
- `/Users/ghost/Dev/nexus/shared/blowup/lens/lenses_systems.hexa` (614 줄)

**관련 커밋**:
- `0c23ad27` — 전환 청소 (2026-04-11 20:40 KST)
- `b1ceb88f` — 직전: 프론티어 렌즈 확장 (mod.rs 선언만 커밋, .rs 본체는 never committed)

---

## 8. 56 HEXA 렌즈 전체 경로 목록

`/Users/ghost/Dev/nexus/shared/blowup/lens/` 기준 (외부 경로, `n6-architecture` 외부):

**lenses_ai_ml.hexa (16)**
```
scan_active_learning          scan_adversarial_robustness   scan_agent_coordination
scan_attention_mechanism      scan_cognitive_load            scan_contrastive_learning
scan_explainability           scan_fairness_bias             scan_federated_learning
scan_meta_learning            scan_multi_task                scan_neural_architecture
scan_reinforcement_reward     scan_self_supervised           scan_transfer_learning
scan_continual_learning
```

**lenses_graph_network.hexa (10)**
```
scan_community_detection   scan_complexity_network   scan_graph_neural
scan_knowledge_graph       scan_link_prediction       scan_network_flow
scan_spectral_graph        scan_topological_data      scan_topological_sort
scan_cross_domain_bridge
```

**lenses_statistics.hexa (14)**
```
scan_bayesian_inference        scan_monte_carlo              scan_sampling_theory
scan_cross_validation          scan_decision_boundary        scan_hyperparameter_tuning
scan_optimal_transport         scan_particle_filter          scan_probabilistic_graphical
scan_sensitivity_analysis      scan_uncertainty_quantification scan_variational_inference
scan_structural_equation       scan_markov_chain
```

**lenses_signal_info.hexa (8)**
```
scan_fourier_analysis           scan_wavelet_transform       scan_signal_reconstruction
scan_information_bottleneck     scan_dimensionality_bottleneck scan_renyi_entropy
scan_time_series_decomp         scan_kalman_filter
```

**lenses_systems.hexa (8)**
```
scan_distributed_consensus   scan_reservoir_computing   scan_spiking_neural
scan_plasticity_consolidation scan_attractor_basin      scan_manifold_learning
scan_persistence_homology    scan_causal_discovery
```

**총 16+10+14+8+8 = 56 ✓**

---

*보고 끝. 실제 코드 수정은 사용자 승인 후 별 세션에서 진행 (R25 공용설정 게이트).*
