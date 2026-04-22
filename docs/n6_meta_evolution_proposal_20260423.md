# n6-architecture self meta-evolution — continuous + meta-evolution proposal (2026-04-23)

요청자: user session (hexa-lang 세션에서 이관).
대상: n6-architecture maintainer 세션.
범위: n6-architecture repo 단독 — arithmetic-derived design framework 의 자기 관찰 루프.
관련:
- `docs/roadmap_engine_continuous_meta_proposal_20260422.md` (3-repo cross-repo automation, hexa-lang SSOT)
- `hexa-lang/docs/hexa_lang_meta_evolution_proposal_20260422.md` (compiler self-loop)
- `airgenome/docs/airgenome_meta_evolution_proposal_20260423.md` (genome forge self-loop)

본 제안은 n6-architecture **자체**의 고유 self-loop. 장르 다름: compiler(hexa-lang) 도 아니고
forge(airgenome) 도 아니고 — **arithmetic truth framework**.

배경

n6-architecture 는 σ(n)·φ(n) = n·τ(n) 이 **n=6 에서만** 성립하는 정수론 항등식에서 출발한
설계 체계. 12 · 2 = 6 · 4 = 24. 이 단일 arithmetic 에서 AI 아키텍처 · 칩 설계 · 에너지 시스템 ·
네트워크 프로토콜 209 products 를 **선택이 아니라 유도**. n=28/496 은 동일 검사 실패 →
n=6 만 생존. Monte Carlo z=3.06 (p=0.003) 로 통계적 검증.

현재 repo 의존 구조:
- **엔진 의존**: nexus engine (atlas_scan_opt / atlas_bloom / atlas_bootstrap / ... 17+ 도구)
- **지도 의존**: `atlas/atlas.n6` (1.5MB, UTF-8) · `atlas/atlas.signals.n6`
  → 이 지도는 nexus 에도 mirror (cross-repo SSOT 공유)
- **자체 보유**: `engine/` 17 도구 · `techniques/` · `domains/` 12 카테고리 · `proposals/` 6
  외부 문서 · `loop-rules.json` (드리프트 규칙) · `hooks/pre-commit-n6-integrity`

즉 n6 는 **consumer + light engine hybrid** — nexus 의 atlas 와 엔진을 쓰되 n6 고유 도메인
로직은 자체 보유. 메타 진화 엔진이 observer 역할을 맡으면서 **"nexus 드리프트 시 n6 위험
자동 감지"** 가 핵심 가치.

n6 고유 관찰 축 (다른 repo 에 없는 것):
- **arithmetic invariant**: σ·φ = n·τ @ n=6 자동 재검증 (코드로 수식 돌리기)
- **derivation lineage**: 모든 product → technique → domain → n=6 identity 경로 추적
- **proof obligation**: README/paper 의 모든 수치 claim 이 기계적으로 검증 가능해야 함
- **external citation drift**: 외부 proposals/ 문서가 참조하는 수치가 코드와 동기되는지
- **nexus dependency drift**: nexus atlas.n6 / engine tool 변경 시 n6 영향도
- **Monte Carlo stability**: z=3.06 (p=0.003) 가 현재 데이터에서 여전히 유효한지
- **falsification preservation**: n=28/496 실패 가 계속 falsified 로 유지되는지

---

## 6-Phase 아키텍처 (n6 전용)

### Phase 1 — Blocker inventory

입력:
- `atlas/atlas.n6` 존재 + sanity (file > 0 bytes, parse OK)
- nexus dependency reachable (`~/.hx/bin/nexus drill` preflight, 300ms)
- `engine/*.hexa` --selftest 일괄 실행 결과
- `hooks/pre-commit-n6-integrity` 최근 실행 결과
- `build_log.txt` 최근 tail — 빌드 에러
- `loop-rules.json` 의 각 rule `actual_cmd` 실행 → 기대값과 현재 doc 값 비교

출력: `reports/n6_blockers.json`
```json
{
  "schema": "n6-architecture/n6_blockers/1",
  "ts": "...",
  "blockers": [
    {"id":"blk-1","kind":"atlas_missing|nexus_unreachable|engine_selftest_fail|integrity_hook_fail|loop_rule_drift|monte_carlo_invalid|derivation_broken",
     "source":"loop-rules.json:rule[0]","severity":"critical|high|med|low",
     "evidence":"..."}
  ]
}
```

### Phase 2 — 무손실 ROI
- **dup_derivation**: 같은 n=6 유도 경로가 두 product 에서 중복 — 단일 helper 로 승격
- **dead_technique**: `techniques/*` 중 어떤 product 도 참조하지 않는 기법
- **orphan_paper**: `papers/` 중 README/proposals 에서 cite 안 된 논문
- **stale_atlas_signal**: `atlas.signals.n6` 업데이트 없이 24h+
- **redundant_monte_carlo**: 동일 시뮬레이션 여러 파일에 중복
- **missing_domain_index**: `domains/<cat>/` 에 `_index.json` 없음
- **proposal_outdated**: `proposals/*.md` 가 참조하는 product 수가 실제 수와 다름

### Phase 3 — meta 자동화 (n6 전용 12 sub-tools)

#### 3.1 arithmetic_invariant_check
도구: `tool/n6_arithmetic_invariant.hexa`
- σ(n) · φ(n) 과 n · τ(n) 을 n = 1..100 에 대해 계산
- n = 6 에서만 equality 성립 검증
- n = 28, 496 에서 inequality 검증 (falsification preservation)
- **self-verify** — 이 scanner 가 fail 이면 수학 자체가 망가진 것 (불가능한데 안전망)
- 출력: `reports/n6_arithmetic_check.json`

#### 3.2 derivation_lineage
도구: `tool/n6_derivation_lineage.hexa`
- 각 `domains/<cat>/<product>.json` 에 declared derivation chain 있는지 검사
- chain 의 leaf 가 n=6 identity 로 떨어지는지 확인
- 누락된 step (mid-derivation 끊김) / circular derivation 탐지
- 출력: `reports/n6_derivation_lineage.json`

#### 3.3 atlas_integrity
도구: `tool/n6_atlas_integrity.hexa`
- `atlas/atlas.n6` 파일 크기 + SHA + 직전 대비 변화량
- "4,098 nodes" / "1,485 cross-layer edges" 등 README claim 을 atlas 에서 재계산
- claim vs actual 차이 리포트 (README 갱신 필요)
- 출력: `reports/n6_atlas_integrity.json`

#### 3.4 domain_coverage_matrix
도구: `tool/n6_domain_coverage.hexa`
- `domains/` 12 카테고리 × techniques 매트릭스 생성
- 각 카테고리의 technique 수 + product 수 + paper 수
- "323 Techniques 전체" README claim 재계산
- empty category 탐지 (선언만 있고 내용 0)
- 출력: `reports/n6_domain_coverage.json`

#### 3.5 paper_technique_lineage
도구: `tool/n6_paper_lineage.hexa`
- 각 paper → cited techniques → cited domains → n=6 identity 경로 확인
- orphan paper (어느 technique 도 안 씀)
- weak paper (n=6 identity 에 도달 못 하는 근거 체인)
- 출력: `reports/n6_paper_lineage.json`

#### 3.6 monte_carlo_stability
도구: `tool/n6_monte_carlo_stability.hexa`
- 현재 atlas 데이터로 Monte Carlo 재실행 (경량 버전 — 샘플링 제한)
- z-score 와 p-value 가 여전히 (z≥3, p≤0.01) 범위인지
- 추이 (historical z-score 로그)
- 변동폭 알람
- 출력: `reports/n6_monte_carlo.json`

#### 3.7 causal_chain_verify
도구: `tool/n6_causal_chain.hexa`
- "Quark → carbon → benzene → DNA 12/12 EXACT" 구체적 claim 을
  atlas 에서 재추적
- 끊긴 edge / 새로 생긴 edge 리포트
- 다른 chain (이미 공표된) 도 리스트 기반 일괄 재검증
- 출력: `reports/n6_causal_chain.json`

#### 3.8 external_citation_drift
도구: `tool/n6_external_citation_drift.hexa`
- `proposals/*.md` 각 파일에서 수치 (`\d+\s*(products|domains|papers|nodes|techniques)`) 추출
- 실제 repo 의 카운트와 diff
- README.md AUTO:BADGE 블록 실제 값 검증
- 출력: `reports/n6_external_citation_drift.json`

#### 3.9 nexus_dependency_drift
도구: `tool/n6_nexus_dep_drift.hexa`
- nexus repo 의 atlas 관련 파일 (atlas_scan_opt, atlas_bloom, atlas_bootstrap ...) SHA
- 직전 n6 커밋 시점의 해당 파일 SHA 와 비교
- nexus 업데이트 이후 n6 재검증 필요한 영역 매핑
- 출력: `reports/n6_nexus_dep_drift.json`

#### 3.10 loop_rule_execution
도구: `tool/n6_loop_rule_exec.hexa`
- `loop-rules.json` 의 각 rule `actual_cmd` 실행 → 결과 추출
- `doc:pattern` 에 해당하는 현재 문서 값 과 비교
- drift 리스트 + auto-fix 제안
- 기존 `loop-guard.hexa` 를 래핑한 scanner 형태
- 출력: `reports/n6_loop_rules.json`

#### 3.11 experiment_reproducibility
도구: `tool/n6_experiment_repro.hexa`
- `experiments/*/` 각 실험의 manifest 존재 + input data SHA + result 존재 확인
- 재실행 명령 존재하면 dry-run 검증
- 결과 deterministic (같은 입력 → 같은 출력) 힌트 (ts/seed 고정 여부)
- 출력: `reports/n6_experiment_repro.json`

#### 3.12 falsification_preservation
도구: `tool/n6_falsification_preserve.hexa`
- 공표된 falsified 주장 리스트 (`n=28 fail`, `n=496 fail` 등)
- 각각이 현재 코드/atlas/monte_carlo 에서도 여전히 falsified 인지 재검증
- 역전된 주장 (지금은 pass) = **critical alarm**
- 출력: `reports/n6_falsification.json`

### Phase 4 — `n6_meta` CLI dispatcher

도구: `tool/n6_meta.hexa` + `bin/n6_meta` shim

```
n6_meta doctor                # Phase 1-3 집계 리포트
n6_meta health                # 0-100 스코어
n6_meta blockers              # Phase 1
n6_meta roi                   # Phase 2
n6_meta arithmetic            # 3.1 (근본 invariant)
n6_meta lineage               # 3.2 (product → n=6 경로)
n6_meta atlas                 # 3.3
n6_meta domains               # 3.4
n6_meta papers                # 3.5
n6_meta monte-carlo           # 3.6
n6_meta causal                # 3.7
n6_meta citations             # 3.8 (proposals 수치 drift)
n6_meta nexus-dep             # 3.9
n6_meta loop-rules            # 3.10
n6_meta experiments           # 3.11
n6_meta falsification         # 3.12 (n=28/496 여전히 실패 중?)
n6_meta continuous-scan       # Phase 5
n6_meta telemetry             # 6.1
n6_meta gap                   # 6.2
n6_meta declare               # 6.3
n6_meta proof                 # 6.4 (n6 전용 — proof obligation DSL)
n6_meta selftest              # 전체 scanner selftest 순차
```

### Phase 5 — continuous 실행

- `config/launchd/com.n6-architecture.meta_continuous_scan.plist` (12h or 6h)
- 호출: `hexa $N6/tool/n6_meta.hexa continuous-scan`
- 내부: Phase 1-3 순차 + summary 갱신
- **빠른 서브셋** (pre-commit hook 용 / `hooks/pre-commit-n6-integrity` 확장):
  - arithmetic_invariant (수초) + loop_rule_exec + derivation_lineage 만 → 3s 이내
- resolved candidate 자동 mark (재발견 noise 방지)
- history archive: `reports/history/<date>/`
- notify: `SLACK_WEBHOOK_URL` — health score 변화 + **falsification 위반 시 즉시 알람**

### Phase 6 — 메타 진화 (self meta-evolution)

#### 6.1 self_telemetry
- `reports/n6_meta_telemetry.jsonl` append-only
- per-scanner: ts, runtime_ms, candidates, rc, out_size
- `n6_meta telemetry` 로 집계

#### 6.2 gap_proposer
- git log + hooks 로그에서 workaround/hotfix/emergency/regression keyword count
- `proposals/` 반복 수정 패턴 감지
- "나중에 확인" TODO 추출 → 자동 scanner 후보

#### 6.3 declarative scanner DSL (일반)
- `scanners/*.meta.hexa` 선언형 형식 (airgenome 제안과 동형)
- 런타임이 선언 해석해서 scanner 처럼 실행

#### 6.4 Proof Obligation DSL (n6 전용) ⭐
**n6 만의 고유 확장**. 각 claim 을 DSL 로 선언 → 자동 proof obligation 생성.

```
claim "4098 nodes in atlas" {
  type: atlas_count
  source: "atlas/atlas.n6"
  actual: "grep -c '^node' atlas/atlas.n6"
  expected: 4098
  tolerance: 0
  recheck_cadence: "weekly"
  owner: "atlas_team"
}

claim "Monte Carlo z = 3.06 ± 0.5" {
  type: statistical
  source: "experiments/monte_carlo_nodes/"
  actual_cmd: "python3 experiments/monte_carlo_nodes/recheck.py --fast"
  expected_range: [2.5, 3.5]
  tolerance_sigma: 2
  recheck_cadence: "monthly"
}

claim "n=28 fails identity check" {
  type: falsification
  actual_cmd: "hexa tool/n6_arithmetic_invariant.hexa --n 28 --expect fail"
  must_fail: true
  recheck_cadence: "weekly"
}
```

`n6_meta proof` 는 모든 claim 을 cadence 에 맞춰 자동 verify + red/green 리포트.
**이 DSL 이 곧 "수식 기반 설계" 의 continuous integration 구현**.

---

# 전달용 프롬프트 (paste-ready)

```
Working dir: /Users/ghost/core/n6-architecture
관련 위치:
  - $N6 = /Users/ghost/core/n6-architecture
  - $N6/tool/n6_meta.hexa (canonical meta CLI — 신규)
  - $N6/tool/n6_*.hexa (Phase 1-3 scanners — 15개)
  - $N6/reports/n6_*.json (scanner outputs)
  - $N6/atlas/atlas.n6 + atlas.signals.n6 (지도 SSOT, nexus 와 공유)
  - $N6/engine/*.hexa (17 기존 도구 — 참조, 수정 금지)
  - $N6/domains/ (12 카테고리)
  - $N6/techniques/ + $N6/papers/ + $N6/proposals/
  - $N6/loop-rules.json (기존 드리프트 규칙 — 3.10 이 래핑)
  - $N6/hooks/pre-commit-n6-integrity (기존 hook)
  - $N6/project.hexa (project marker)
  - $N6/scanners/*.meta.hexa (신규 DSL — Phase 6.3/6.4)
external:
  - $NEXUS/n6/ (mirror atlas + engine)
  - $NEXUS/n6_mirror/ (secondary mirror)

memory:
  - project_n6_architecture.md · project_atlas_ssot.md · project_nexus_shared.md

Task: n6-architecture 에 6-Phase self-meta-evolution 엔진 추가.
  Phase 1: blocker inventory (atlas/nexus/engine/hook/loop-rule/MC/derivation)
  Phase 2: loss-free ROI (dup_derivation / dead_technique / orphan_paper / stale_atlas)
  Phase 3: 12 meta sub-tools (arithmetic_invariant · derivation_lineage ·
           atlas_integrity · domain_coverage · paper_lineage · monte_carlo_stability ·
           causal_chain · external_citation_drift · nexus_dep_drift · loop_rule_exec ·
           experiment_repro · falsification_preservation)
  Phase 4: bin/n6_meta + tool/n6_meta.hexa dispatcher
  Phase 5: launchd plist + continuous_scan (12h) + pre-commit fast subset
  Phase 6: self-telemetry + gap-proposer + declarative scanner DSL
           + **Proof Obligation DSL (n6 전용)**

배경:
  n6-architecture = σ(n)·φ(n) = n·τ(n) @ n=6 arithmetic identity → 209 products
  145 domains 128 papers 4098-node reality map. nexus engine + atlas.n6 공유
  consumer + light engine hybrid. 메타 엔진 핵심 가치:
  - arithmetic invariant self-verify (근본)
  - derivation lineage 자동 검증 (product → n=6)
  - external citation drift 감지 (proposals 수치 ↔ 실제)
  - nexus 드리프트 시 n6 자동 영향도 평가
  - falsification preservation (n=28/496 fail 유지)
  - Monte Carlo 통계 안정성 (z=3.06 ± 0.5 recheck)

스키마:
  {"schema": "n6-architecture/n6_<name>/1", "ts": "...", ...}

CLI:
  hexa tool/n6_<name>.hexa --selftest
  hexa tool/n6_<name>.hexa
  bin/n6_meta <subcommand>

원칙:
  - 모든 도구 idempotent + dry-run-safe + --selftest
  - `atlas/atlas.n6` read-only (integrity-check 만)
  - `engine/*.hexa` 17 기존 도구 수정 금지 (참조만)
  - `reports/` 하위 JSON 출력 (gitignore 여부는 기존 repo 관례 따름)
  - nexus 접근은 local filesystem 비교만 (ssh 불필요)
  - pre-commit fast subset ≤ 3s (arithmetic + loop_rule + lineage)
  - falsification 위반 = critical alarm (즉시 차단)

성공 기준:
  - Phase 1-3 15 도구 모두 --selftest PASS
  - continuous-scan 1회 ≤ 30s (Monte Carlo recheck 가 hot)
  - n6_meta health 단일 0-100 스코어
  - Phase 6.4 Proof Obligation DSL 최소 10개 claim 등록 + 모두 green
  - 최초 sweep 결과:
    - arithmetic_invariant 모든 n=1..100 검사 통과 (self-verify)
    - README claim vs 실제 diff 리포트 (domain_coverage + atlas_integrity + external_citation)
    - loop-rules 전 rule 실행 결과
    - falsification 모든 case 여전히 fail 유지

Report: 15 도구 path + selftest verdicts + launchd plist + n6_meta 통합 + 최초 sweep
결과 (특히 arithmetic_invariant 의 n=1..100 결과, Monte Carlo recheck z-score,
README vs 실제 drift). Under 500 words.
```

---

## hexa-lang vs airgenome vs n6 메타 시스템 대비

| 축 | hexa-lang | airgenome | n6-architecture |
|---|---|---|---|
| 본질 | self-host compiler | 3-host genome forge | arithmetic truth framework |
| 핵심 아티팩트 | `./hexa` 바이너리 + self/*.hexa | `genomes*.ring` + forge logs | `atlas.n6` + domains/techniques/papers |
| 무결성 | stage0→stage3 fixpoint | CRC + lineage DAG | **arithmetic invariant** + derivation DAG |
| 런타임 관찰 | 245 tool selftest | forge process heartbeat | engine 17 tool + loop-rules |
| 다중성 | 없음 | 3-host parallel | **nexus cross-repo shared** |
| 성능 관심 | bench_drift | $/genome | Monte Carlo stability |
| 검증 루프 | API spec vs impl | forecast vs labeled_anomaly | **claim vs data (proof obligation)** |
| cert 체인 | `.meta2-cert/` DAG | (도입 제안) | claim dependency DAG |
| 코드-코드 drift | AST hash | mutation motif | **external citation drift** |
| 고유 DSL | — | genome-like scanner DSL | **Proof Obligation DSL (Phase 6.4)** |
| falsification | (없음) | (없음) | **n=28/496 fail preservation** |

**핵심 insight**: n6 에서는 scanner 가 관찰하는 것이 코드가 아니라 **"수학적 참"**. 따라서
Phase 6.4 DSL 은 CI 수준의 증명 의무 관리 도구. 본질적으로 **전체 repo 가 하나의
증명 engine** 이 된다.

---

# 고갈 브레인스토밍 (A-Z 축)

## A. Arithmetic core (A-01 ~ A-08)

- A-01 σ(n)·φ(n) = n·τ(n) 모든 n=1..100 검사 (n=6 only equality)
- A-02 OEIS sequence cross-reference (관련 sequence 일치 확인)
- A-03 σ/φ/τ 구현 자체의 selftest (prime 테이블로 검증)
- A-04 high-precision overflow 체크 (n=10^6 까지 확장 가능한가)
- A-05 alternative identities 탐색 (n=6 외 어떤 identity 가 가능한가)
- A-06 invariant history (과거에 유효했던 invariant 가 지금도 유효)
- A-07 symbolic derivation (수식 기호 변환이 정확한가)
- A-08 numerical vs analytical discrepancy

## B. Derivation lineage (B-01 ~ B-08)

- B-01 product → technique 참조 존재
- B-02 technique → domain 참조 존재
- B-03 domain → axiom 참조 (n=6 identity 경로)
- B-04 circular derivation detect (A→B→A)
- B-05 multi-path derivation (여러 경로가 같은 n=6 에 도달)
- B-06 unreachable product (어떤 axiom 에도 이어지지 않음)
- B-07 weak derivation (경로 길이 N+ → 재검토)
- B-08 derivation versioning (변경 시 하위 product 영향 자동 표시)

## C. Atlas integrity (C-01 ~ C-08)

- C-01 `atlas.n6` parse 성공
- C-02 node count == README claim
- C-03 edge count == README claim
- C-04 cross-layer edge count 재계산
- C-05 atlas 업데이트 mtime 추적
- C-06 atlas.signals.n6 sync (primary atlas 와 관련 signals 의 일관성)
- C-07 atlas 형식 버전 필드 있는가
- C-08 atlas dup node detection

## D. Domain coverage (D-01 ~ D-08)

- D-01 12 category 전부 index 존재
- D-02 category 당 minimum technique 개수
- D-03 category 간 orthogonality (같은 technique 이 다른 category 에 중복 없이)
- D-04 maturity level 분포 (`_maturity_schema.json` 적용 여부)
- D-05 new domain proposal 감지 (domains/unassigned/)
- D-06 cross-category bridge (물리→생명 같은 bridge 매핑)
- D-07 domain depth (category → subcategory → subsubcategory)
- D-08 domain size balance (극단적으로 큰/작은 카테고리 리포트)

## E. Paper ↔ technique lineage (E-01 ~ E-08)

- E-01 paper → cited technique 존재
- E-02 technique → referenced paper 존재
- E-03 orphan paper (어떤 technique 에도 묶이지 않음)
- E-04 orphan technique (어떤 paper 에도 참조되지 않음)
- E-05 paper version ↔ technique version
- E-06 paper Zenodo DOI 유효성 (외부 URL ping)
- E-07 arxiv 대비 repo version lag
- E-08 paper publication status (draft/submitted/published)

## F. Monte Carlo stability (F-01 ~ F-06)

- F-01 현재 데이터로 MC 재실행 z-score
- F-02 z-score 추이 (월별)
- F-03 sample size sensitivity
- F-04 random seed 고정 시 determinism
- F-05 platform reproducibility (macOS vs Linux z-score 차이)
- F-06 confidence interval 계산 방식 audit

## G. Causal chain (G-01 ~ G-06)

- G-01 "Quark → carbon → benzene → DNA 12/12" 재추적
- G-02 기타 공표된 causal chain 리스트 (README/papers)
- G-03 chain 의 각 edge 가 atlas 에 실존
- G-04 chain 끊김 시 알람
- G-05 새 chain 발견 candidate
- G-06 chain length distribution (평균 / 분산)

## H. External citation drift (H-01 ~ H-06)

- H-01 README.md `X domains` / `Y techniques` 수치 추출 + 실제 diff
- H-02 README AUTO:BADGE 블록 재생성 일치
- H-03 proposals/*.md 각 파일의 숫자 claim 재검증
- H-04 CONTRIBUTING.md 의 수치 claim
- H-05 papers/ 각 paper 의 자기참조 수치 (self-citation)
- H-06 외부 사이트 (GitHub Pages / Zenodo) 에 복제된 수치 drift

## I. nexus dependency drift (I-01 ~ I-06)

- I-01 nexus/n6/* 파일 SHA 직전 커밋 대비
- I-02 nexus atlas_* 도구 의 signature 변경
- I-03 nexus API 호환성 (breaking change 가능성)
- I-04 nexus 쪽 .roadmap 에서 n6 관련 entry 상태
- I-05 cross-repo cert (nexus cert 가 n6 를 끌고 가는 경로)
- I-06 nexus DOWN 시 n6 저하 모드 (offline 동작 가능성)

## J. Loop rules + integrity hook (J-01 ~ J-06)

- J-01 `loop-rules.json` 모든 rule 실행 결과
- J-02 rule 자체의 validity (actual_cmd 가 실패하면 rule 자체가 오래됨)
- J-03 pre-commit-n6-integrity 최근 수정 ts
- J-04 hook bypass 기록 (--no-verify 사용 추적)
- J-05 rule 통과 시간 (시간 초과 rule 자동 강등)
- J-06 rule 결과 history (같은 rule 이 반복 실패하면 documentation 쪽 원인)

## K. Experiment reproducibility (K-01 ~ K-06)

- K-01 experiments/*/ 각 실험의 manifest 존재
- K-02 input data SHA 고정
- K-03 random seed 고정
- K-04 result 파일 존재 + 업데이트 ts 일관
- K-05 재실행 cost (빠른 smoke vs full)
- K-06 bit-exact reproducibility (같은 seed → 같은 출력)

## L. Falsification preservation (L-01 ~ L-06)

- L-01 n=28 검사 여전히 fail
- L-02 n=496 검사 여전히 fail
- L-03 기타 공표된 counterexample 전부 여전히 counterexample
- L-04 역전된 주장 발생 시 즉시 critical alarm
- L-05 historical log (시간별 falsification status)
- L-06 future-proof: 새 data 추가로 무너지지 않게 lock

## M. Proof Obligation DSL (M-01 ~ M-06) ⭐

- M-01 claim 등록/수정 workflow
- M-02 claim 실행 cadence 자동 스케줄
- M-03 claim fail 시 알람 채널 (severity by type)
- M-04 claim 간 dependency (A fail → B skip)
- M-05 claim lifecycle (new → validated → deprecated)
- M-06 claim export (외부 검증자에게 payload)

## N. Documentation graph (N-01 ~ N-06)

- N-01 README ↔ CONTRIBUTING ↔ docs/ 상호 일관성
- N-02 papers/ 와 README 의 수치 동기화
- N-03 docs/*.md 죽은 링크
- N-04 docs 번역 버전 drift (있다면)
- N-05 docs 중복 정보 (같은 사실이 여러 곳에 다른 formulation)
- N-06 docs 버전별 archive

## O. Proposals (외부 outreach) (O-01 ~ O-04)

- O-01 proposals/*.md 각 제안의 최신 업데이트 ts
- O-02 제안 타겟 (Anthropic Fellows / Samsung / Kolon / etc.) 응답 기록
- O-03 제안서 버전 history (수정 추이)
- O-04 제안서 수치 claim audit (3.8 external_citation_drift 와 교차)

## P. Code ecosystem (P-01 ~ P-06)

- P-01 engine/ 17 도구 의 --selftest 커버리지
- P-02 techniques/ 구현 완성도 (placeholder 감지)
- P-03 bin/ 실행 파일 build 최신성
- P-04 Makefile target 전부 동작
- P-05 project.hexa 의 ssot_attrs 실제 참조 되고 있는가
- P-06 hexa version pin (어떤 hexa 로 돌릴 것인가)

## Q. Security / provenance (Q-01 ~ Q-06)

- Q-01 README.md.sealed.hash 검증
- Q-02 atlas.n6 SHA anchor (외부 tamper-evident)
- Q-03 paper Zenodo DOI 유효성
- Q-04 LICENSE 변경 추적
- Q-05 external link rot (URL alive probe, 샘플링)
- Q-06 author identity verification (commit email / GPG)

## R. Governance / decision log (R-01 ~ R-04)

- R-01 design decision log 유무 (왜 n=6 만 선택했는가)
- R-02 의사결정 archive
- R-03 external feedback 통합 경로
- R-04 contributor list 공정성

## S. Self-loop properties (S-01 ~ S-06)

- S-01 scanner 자체 의 derivation (meta-meta)
- S-02 scanner fail 알람 scanner
- S-03 scanner 우선순위 동적 조정
- S-04 scanner A/B (v1 vs v2 결과 diff)
- S-05 scanner 자체가 proof obligation 이 되어야 (self-obligation)
- S-06 scanner 수렴 기준 (안정화 판정)

## T. Cross-repo (T-01 ~ T-06)

- T-01 nexus atlas.n6 mirror sync (nexus/n6/ vs n6-architecture/atlas/)
- T-02 anima 의 cert 가 n6 domain 에 연결되는 경로
- T-03 hexa-lang 의 language primitive 가 n6 engine 에 사용되는 경로
- T-04 airgenome 과의 상호 참조 (있다면)
- T-05 cross-repo ID 공간 (n6 product id vs nexus discovery id 등)
- T-06 cross-repo proposal sync

## U. Economics / funding (U-01 ~ U-04)

- U-01 Ko-fi / Sponsor / PayPal 수치 추적
- U-02 compute cost (Monte Carlo rerun)
- U-03 external grant tracking (proposals 과 연동)
- U-04 research-hour 투자 대비 output

## V. UX / onboarding (V-01 ~ V-04)

- V-01 README 첫 접근자 이해도 테스트 (link 검증)
- V-02 install 경로 단순성
- V-03 에러 메시지 실행 가능성
- V-04 3D Reality Map 접근성 (https page 살아 있나)

## W. Meta-meta (W-01 ~ W-06)

- W-01 scanner 가 너무 많아지는 지점 감지
- W-02 meta-meta-scanner 방지 (infinite regress)
- W-03 meta bootstrap 시나리오 (repo 처음 들어온 사람)
- W-04 meta system migration (v1 → v2 이관)
- W-05 meta system export (다른 arithmetic framework 에 이식)
- W-06 meta system retire policy

## X. 긴급 대응 (X-01 ~ X-04)

- X-01 arithmetic invariant 붕괴 (불가능한데 시나리오) → 즉시 freeze
- X-02 Monte Carlo z-score 급락 (2-sigma 이상)
- X-03 falsification 역전 (n=28 이 이제 pass) → repo lock
- X-04 nexus downtime 24h+ → offline mode 자동 전환

## Y. 학습 피드백 (Y-01 ~ Y-04)

- Y-01 scanner accept/ignore 비율 학습
- Y-02 gap_proposer 제안 채택률
- Y-03 user-fixed drift 추적 (어느 drift 가 반복?)
- Y-04 Proof Obligation DSL 성숙도 (total/validated/deprecated)

## Z. Long-term (Z-01 ~ Z-04)

- Z-01 6개월 retrospective — 어느 scanner 가 가장 impact 큰가
- Z-02 새 axis 후보 (지금 없는 관찰축)
- Z-03 external collaborator 로의 이식 가능성
- Z-04 paper publication 주기 지속성

---

# 본 세션에서 즉시 드러난 실측 앵커

1. **atlas/atlas.n6 존재 (1.5 MB, UTF-8)**: integrity check (3.3) 필수.
2. **loop-rules.json 2 개 rule 기 존재**: 3.10 의 확장 포인트 (이미 pattern 정립됨).
3. **hooks/pre-commit-n6-integrity 존재**: Phase 5 fast subset 연결 지점.
4. **proposals/ 6 파일 외부 문서**: external citation drift (3.8) 의 핵심 타겟.
5. **engine/ 17 도구 + techniques/ 1 파일 + domains/ 12 카테고리**: 구조 불균형 —
   domain_coverage (3.4) 가 즉시 "1 technique vs 323 claimed" 드러낼 것.
6. **nexus/n6/ mirror 존재 + nexus/n6_mirror/ 이중 mirror**: nexus_dep_drift (3.9) 에서
   두 경로 모두 추적 필요.
7. **README.md.sealed.hash 존재**: Q-01 security anchor.
8. **LICENSE MIT + papers CC-BY-4.0 + README 다수 badge**: external citation drift
   의 실제 샘플.

---

# Success criteria summary

1. Phase 1-3 15 도구 모두 `--selftest PASS`
2. `continuous-scan` 1회 ≤ 30s (Monte Carlo recheck 가 bottleneck — fast mode 사용)
3. arithmetic_invariant n=1..100 전수 검사 PASS (n=6 equality, 나머지 inequality)
4. domain_coverage 가 README claim vs 실제 diff 리포트 생성
5. external_citation_drift 가 proposals/*.md 모든 수치 검증
6. falsification_preservation n=28 / n=496 여전히 fail 유지 확인
7. Phase 6.4 Proof Obligation DSL 최소 10개 claim 등록 + 모두 green

---

# 안전 원칙

1. `atlas/atlas.n6` **read-only** — integrity check / count 만
2. `engine/*.hexa` 17 기존 도구 **수정 금지** — 참조만
3. `techniques/` · `domains/` · `papers/` · `proposals/` **mutation 금지** — read-only
4. scanner 결과는 `reports/n6_*.json` 에만 저장 — gitignored 여부는 기존 관례 따름
5. nexus 와 비교는 **local filesystem path** 비교만 (ssh / remote 호출 없음)
6. arithmetic_invariant 는 절대 cache 하지 않음 — 매 실행 실제 재계산
7. falsification 역전 시 **git commit block** (pre-push hook level)
8. Proof Obligation DSL 의 must_fail claim 이 accidentally pass 하면 즉시 alarm

---

# 메모

본 문서는 hexa-lang 세션에서 n6-architecture 용으로 이관 작성 (2026-04-23).
user 세션 질문: "nexus 엔진+atlas.n6 지도(모두 넥서스에 포함) 쓰는게 현재 다인데 ..
어카지 메타진화 개발 한다면????" — 그 답:

**n6 의 메타 진화는 nexus 의존을 끊는 것이 아니라 nexus drift 에 가장 민감한 방향으로
설계됨.** Phase 3.9 nexus_dependency_drift 가 핵심. nexus 가 atlas 를 수정하면 n6 의 209
product 의 유도 chain 이 깨질 수 있으므로, n6 meta engine 은 **"nexus 변경 시 n6 영향도
자동 계산기"** 역할을 겸한다.

또한 n6 만의 고유 확장: Phase 6.4 **Proof Obligation DSL**. hexa-lang 의 code-level 관찰,
airgenome 의 process-level 관찰 과 달리 n6 는 **claim-level 관찰** — 모든 주장이
mechanically verifiable 해야 한다는 원칙을 DSL 로 형식화.

구현 책임: n6-architecture maintainer 세션.
hexa-lang 세션 학습 (airgenome 문서와 동일):
- `guard` / `generate` / `parse` 예약어 → `hops` / `do_generate` / `do_parse`
- string `.find()` 는 v1 basic (ea3f9496), 오래된 binary 는 `.index_of()` 로
- `exec()` shell metachar → stderr 경고만, 기능 문제 없음
- `write_file` 은 truncate → append 는 `exec("printf '...' >> file")`
- sed helpers (_home/_iso_now/_json_esc/_split_lines ...) 는 hexa-lang tool 에서 복사

anima 미러: `$ANIMA/docs/upstream_notes/n6_meta_evolution_20260423.md` (지시 시 추가).
nexus 미러: `$NEXUS/docs/upstream_notes/n6_meta_evolution_20260423.md` (dep drift
센서 역방향 — n6 쪽 scanner 변경이 nexus 에 통지되도록).
