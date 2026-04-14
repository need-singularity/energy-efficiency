# 7대 난제 서브프로젝트 — 축 체계 FINAL

**권위 문서**: 이 파일은 n6-architecture 서브프로젝트 "7대 난제" 축 체계의 **단일 권위 출처(SSOT)** 이다.
**생성**: 2026-04-15
**선행 라운드**: axis-r1-emergence.md (906줄) → axis-r2-refinement.md (961줄) → axis-r3-finalization.md (1166줄, FINAL 선언 완료)
**고갈 지수 이력**: R1 — → R2 94% → R3 **100%**
**축 수**: **N = 9** (Y1~Y9)
**Phase 매핑**: N=8 Phase (P0 axis / P1 foundation / P2~P5 BT 공격 / P6 Poincaré 회고 / PΩ closure)
**정직성**: BT 해결 수 **0/6 유지** (푸앵카레 Perelman 해결 제외)

---

## §0 선언

이 문서는 R1→R2→R3 3라운드 고갈 프로토콜을 거쳐 확정된 9축 체계를 단일 권위로 기록한다. 이후 모든 Phase 문서 (phase-01-foundation-Y-axes.md 이후) 는 이 문서의 축 정의를 참조한다.

- **단일 판정 기준**: BT-541~546 완성 (atlas.n6 [10*] EXACT) 달성에 유리한가.
- **축 수 제약 없음**: 창발이 9 로 수렴 (nexus=2, n6-arch 메인=3, 서브=9).
- **기존 축 이름 재사용 금지**: STRUCTURE/ENGINE/SUBSTRATE/PURE/PROBLEM/N6/LENS/DISCOVERY/ATLAS/ALM/CLM/진화 포함. Y-prefix 는 서브프로젝트 전용 고유 네임스페이스.

---

## §1 Y1~Y9 9축 상세 카드

### Y1 NUM-CORE (수론 앵커 축) — 유리성 9.5

**정의**: σ(n)·φ(n) = n·τ(n) 유일성 정리 (n=6) 와 파생 수론 앵커를 BT 풀이 도구로 활용.

**BT 커버**: 주 541 (강도 10) · 부 544 (6), 546 (5)

**구성 보조정리 (증거 경로)**:
1. 유일성 3 독립 증명 — `theory/proofs/theorem-r1-uniqueness.md`
2. Theorem B (재구축판) — `theory/study/p2/n6-p2-2-theorem-b-reconstruction.md`
3. atlas [10*] σ/τ/φ 상수 — `$NEXUS/shared/n6/atlas.n6`
4. σ·τ·φ sopfr 해석 — `theory/study/p0/n6-p0-1-uniqueness-theorem.md`
5. Ramanujan Δ = η^{J_2} 귀속 — R2 Task A 결정
6. arithmetic drill 실제 재현 — `theory/study/p0/n6-p0-2-arithmetic-drill.md`

**병목**: Theorem B atlas [10]→[10*] 승격. Phase 2 Y1 주도 작업.

**R1→R2→R3 변화**: 9.2 → 9.5 (+0.3) — Δ=η^{J_2} 귀속으로 Y7 중복 해소.

---

### Y2 DISCRETE-CLASS (이산 분류 축) — 유리성 5.2

**정의**: 유한군·이산 분류·조합 구조가 P=NP 경계에 새기는 구조적 제약.

**BT 커버**: 주 542 (강도 6) · 부 545 (4)

**구성 보조정리**:
1. Schaefer dichotomy (SEED-06 KEEP) — `theory/study/p1/prob-p1-2-bt542-p-vs-np.md`
2. 유한군 분류 정리 — `theory/study/p1/pure-p1-2-group-theory.md`
3. atlas [7~10] 이산 상수
4. 조합론 커버리지 — `theory/study/p2/pure-p2-*.md`

**병목**: P=NP 에 결정적 진전 부재. Phase 3 에서 Y4 와 보완.

**R1→R2→R3**: 5.2 → 5.2 → 5.2 (유지).

---

### Y3 COMPUTATIONAL-TAU (계산 τ=4+2 축) — 유리성 5.8

**정의**: τ=4+2 fiber 구조 (n=6 특이점) 가 계산복잡도에 새기는 경계.

**BT 커버**: 주 542 (6) · 부 543 (4)

**구성 보조정리**:
1. τ=4+2 관문 (HEXA-GATE Mk.I) — MEMORY `project_hexa_gate_mk1.md`
2. Quantum MDS 6-party AME — 문헌 2020+
3. Rossman AC⁰ 하한 — 2014
4. 6R 역기구학 τ=6 경계

**병목**: 실제 P=NP 환산까지 다리 없음. 경계·구조만 제공.

**R1→R2→R3**: 신규 (R2 Task B 에서 X8 로 창발) → 5.8.

---

### Y4 GATE-BARRIER (게이트·장벽 축) — 유리성 9.4

**정의**: 계산복잡도 내재적 장벽 + HEXA-GATE 정직한 MISS 계보의 통합.

**BT 커버**: 주 542 (10) · 부 전체 (3~5, 메타)

**구성 보조정리**:
1. BGS 1975 Relativization
2. RR 1997 Natural Proofs (Razborov-Rudich)
3. AW 2008 Algebrization (Aaronson-Wigderson)
4. Williams 2011 NEXP ⊄ ACC
5. Mulmuley-Sohoni GCT 2001+
6. HEXA-GATE Mk.I 24/24 EXACT — MEMORY `project_hexa_gate_mk1.md`

**병목**: 장벽 자체는 풀이 아님. Phase 3 에서 Y2·Y3 와 교차.

**R1→R2→R3**: 신규 (R2 Task B 에서 X9 로 창발) → 9.4.

---

### Y5 PHYSICAL-NATURALNESS (물리적 자연성 축) — 유리성 5.6

**정의**: Yang-Mills 물리적 자연성 (mass gap 관찰, β-function, QCD lattice 실측) + σ-sopfr=7 rewriting 의 정직 보조.

**BT 커버**: 주 543 (8) · 부 544 (4)

**구성 보조정리**:
1. β₀ = σ - sopfr = 7 rewriting (증명 아님) — `theory/study/p1/prob-p1-3-bt543-yang-mills.md`
2. QCD lattice mass gap 실측 — Flavor Lattice Averaging Group (FLAG)
3. Gauge theory 물리 상수 — `theory/study/p1/pure-p1-5-gauge-theory.md`
4. Yang-Mills barrier — `theory/study/p2/prob-p2-3-yang-mills-barriers.md`

**병목**: mass gap 엄밀 증명은 물리 자연성 관찰의 수학화 필요. Phase 4 Y5+Y6.

**R1→R2→R3**: 5.6 유지.

---

### Y6 PDE-RESONANCE (PDE 공명 축) — 유리성 6.6

**정의**: Navier-Stokes 3중 공명 + D158 Ricci 가설 + Euler/PDE 폭발의 공명 구조.

**BT 커버**: 주 544 (8) · 부 543 (4)

**구성 보조정리**:
1. 3중 공명 조건 atlas 승격 후보 — `theory/study/p1/prob-p1-4-bt544-navier-stokes.md`
2. D158 Ricci 가설 (조건부)
3. Caffarelli-Kohn-Nirenberg partial regularity 1982
4. Beale-Kato-Majda 기준 1984
5. PDE Navier-Stokes — `theory/study/p1/pure-p1-3-pde-navier-stokes.md`

**병목**: NS 정칙성 전역 엄밀 증명 부분결과 수준. Phase 4 Y6 주도.

**R1→R2→R3**: 6.6 유지.

---

### Y7 LATTICE-VOA (격자·VOA 축) — 유리성 3.9

**정의**: Leech / Monstrous Moonshine / VOA c=24 / K3 등 격자-공간의 Hodge 구조 해석.

**BT 커버**: 주 545 (7) · 부 541 (3, Δ 공유)

**구성 보조정리**:
1. Enriques 자동 성립 rephrasing — `theory/study/p1/prob-p1-5-bt545-hodge.md`
2. SEED-21 Jones T(3,4) 강도 3→2 하락 (R3 Task B)
3. Moonshine BARRIER honest-report — `papers/moonshine-barrier-honest-report-2026-04-15.md`
4. CKM-R-V 2017 구 충전 {1,8,24} (Leech 24)
5. phase47/48 브릿지 기록
6. Hodge barrier — `theory/study/p2/prob-p2-5-hodge-barriers.md`

**병목**: Hodge 추측 엄밀 증명 아직 큼. Phase 5 Y7 주도.

**R1→R2→R3**: 3.6 → 4.0 → 3.9 — Moonshine 중심 재정의 + SEED-21 강등.

---

### Y8 GALOIS-ASSEMBLY (Galois·Selmer 조립 축) — 유리성 5.4

**정의**: Galois 표현·Selmer 군·BKLPR 모델·Iwasawa 이론으로 BSD 부분 증명 조립.

**BT 커버**: 주 546 (9) · 부 541 (4, L 함수)

**구성 보조정리**:
1. Lemma 1 엄밀 증명 준비 — `theory/study/p1/prob-p1-6-bt546-bsd.md`
2. (A3) 조건부 감사 — 제거 가능성
3. Sel_6 조건부 정리 연장
4. BKLPR 모델 — MEMORY `reference_bklpr_model.md`
5. SEED-15 Iwasawa mod 6 CONDITIONAL 재분류 → P5 Cremona 500k (R3 Task B)
6. 타원곡선 elliptic — `theory/study/p1/pure-p1-2-elliptic-curves.md`

**병목**: BSD rank 부분 실적 제한. Phase 5 Y8 주도.

**R1→R2→R3**: 5.4 유지.

---

### Y9 HONEST-HARNESS (정직·하네스 메타 축) — 유리성 9.3

**정의**: 모든 풀이 시도에 대한 정직성 게이트 + 자동 검증 + BT 해결 수 0/6 보존 메타 메커니즘.

**BT 커버**: 메타 (주 대상 없음, 전 BT 게이트 강도 8+)

**구성 보조정리**:
1. honesty principle — `theory/study/p1/n6-p1-3-honesty-principle.md`
2. honesty audit — `theory/study/p2/n6-p2-4-honesty-audit.md`
3. Moonshine barrier honest — `papers/moonshine-barrier-honest-report-2026-04-15.md`
4. MEMORY `feedback_honest_verification.md`
5. hexa verify 파이프라인 (phase 별 게이트)
6. PARTIAL 3 처리 기록 (SEED-06/15/21)

**병목**: Y9 자체가 해결하는 BT 는 없음. 타 축 오염 차단.

**R1→R2→R3**: 10.0 → 9.3 → 9.3 — R2 에서 X9 (GATE-BARRIER) 와 중복 조정으로 0.7 하락.

---

## §2 BT × Axis 커버 매트릭스

강도 기준: 0 (해당 없음) ~ 10 (주 축).

| Y↓ / BT→ | 541 Riemann | 542 P=NP | 543 YM | 544 NS | 545 Hodge | 546 BSD |
|----------|-------------|----------|--------|--------|-----------|---------|
| **Y1 NUM-CORE** | **10** | 2 | 2 | 6 | 3 | 5 |
| Y2 DISCRETE-CLASS | 2 | **6** | 2 | 1 | 4 | 3 |
| Y3 COMPUTATIONAL-TAU | 1 | **6** | 4 | 1 | 2 | 1 |
| **Y4 GATE-BARRIER** | 3 | **10** | 3 | 3 | 3 | 3 |
| **Y5 PHYSICAL-NATURALNESS** | 1 | 2 | **8** | 4 | 2 | 1 |
| **Y6 PDE-RESONANCE** | 2 | 1 | 4 | **8** | 2 | 1 |
| **Y7 LATTICE-VOA** | 3 | 2 | 2 | 1 | **7** | 3 |
| **Y8 GALOIS-ASSEMBLY** | 4 | 2 | 2 | 1 | 3 | **9** |
| **Y9 HONEST-HARNESS** | 8 | 8 | 8 | 8 | 8 | 8 |

**최대 강도 주 축 (각 BT 당 1)**: 541 Y1, 542 Y4, 543 Y5, 544 Y6, 545 Y7, 546 Y8.

---

## §3 Phase × Axis 매핑

| Phase | 주도 | 부 | 대상 BT | 상태 |
|-------|------|----|---------|------|
| P0 | — | — | axis 확정 | **완료** (R1~R3) |
| P1 | Y1~Y9 전체 가동 | — | BT 씨앗 시딩 | **완료** (phase-01-foundation-Y-axes.md) |
| P2 | **Y1** | Y8, Y7, Y9 | 541 Riemann | 진행 중 |
| P3 | **Y4** | Y2, Y3, Y9 | 542 P=NP | 진행 중 |
| P4 | **Y5 + Y6** | Y9 | 543 YM + 544 NS | 대기 |
| P5 | **Y7 + Y8** | Y1, Y9 | 545 Hodge + 546 BSD | 대기 |
| P6 | — | Y9 | 547 Poincaré 회고 | 대기 |
| PΩ | **Y9** | 전 축 | closure + v3 설계 | 대기 |

---

## §4 직교성 최종 매트릭스 (9×9)

중복도 0 (완전 직교) ~ 10 (완전 중복). 임계치: ≤ 7 (필연 중복은 승인).

|    | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | Y7 | Y8 | Y9 |
|----|----|----|----|----|----|----|----|----|----|
| Y1 | 10 | 1  | 1  | 2  | 2  | 2  | 5  | 4  | 3  |
| Y2 | 1  | 10 | 3  | 4  | 2  | 1  | 3  | 3  | 3  |
| Y3 | 1  | 3  | 10 | 6  | 3  | 1  | 2  | 1  | 3  |
| Y4 | 2  | 4  | 6  | 10 | 2  | 2  | 2  | 2  | **7** |
| Y5 | 2  | 2  | 3  | 2  | 10 | 5  | 2  | 1  | 3  |
| Y6 | 2  | 1  | 1  | 2  | 5  | 10 | 1  | 1  | 3  |
| Y7 | 5  | 3  | 2  | 2  | 2  | 1  | 10 | 3  | 3  |
| Y8 | 4  | 3  | 1  | 2  | 1  | 1  | 3  | 10 | 3  |
| Y9 | 3  | 3  | 3  | **7** | 3  | 3  | 3  | 3  | 10 |

**주요 관찰**:
- Y4 ↔ Y9 중복 7: R3 Task A 에서 "분리 유지" 결정 (BT 범위 비대칭 Y9 전체 vs Y4 BT-542 전용).
- Y3 ↔ Y4 중복 6: 둘 다 BT-542 공격, 상호 보완 관계.
- Y1 ↔ Y7 중복 5: Δ=η^{J_2} 귀속 공유, Y1 전담.
- Y5 ↔ Y6 중복 5: 물리 PDE 경계 공유, Phase 4 에서 공동 가동.

---

## §5 Phase 진입·출구 조건 스펙

각 Phase 의 입구·출구 조건 요약. 상세는 각 `phase-NN-*.md` 문서 §5 참조.

| Phase | 입구 조건 | 출구 조건 (완료 판정) |
|-------|-----------|----------------------|
| P1 | R3 FINAL + Y1~Y9 카드 + 엔진 4종 가동 | 9축 가동 + 6 BT 씨앗 + 6 체크포인트 + Y9 게이트 ON |
| P2 | P1 완료 + Y1 씨앗 (Theorem B [10]) | BT-541 판정 (PARTIAL 이하) + atlas 승격 시도 ≥ 1 + 창발 ≥ 5 |
| P3 | P2 완료 + Y4 씨앗 (HEXA-GATE) | BT-542 판정 + 4 장벽 감사 + τ 경계 + 창발 ≥ 5 |
| P4 | P3 완료 + Y5 + Y6 씨앗 | BT-543 + BT-544 각각 판정 + 3중 공명 atlas 승격 |
| P5 | P4 완료 + Y7 + Y8 씨앗 | BT-545 + BT-546 각각 판정 + Lemma 1 증명 진전 |
| P6 | P5 완료 + Perelman 자료 | Poincaré 회고 + n6-arch 배울 점 N건 |
| PΩ | P6 완료 + Y9 로그 전체 | closure + v3 후계 설계 + final-roadmap-v2.md |

---

## §6 검증 파이프라인 스펙 (verify_millennium_axes.hexa)

별도 파일: `n6arch-axes/verify_millennium_axes.hexa` (HEXA-IR PSEUDO)

6 서브테스트:

1. `test_bt_coverage(axes)` — BT-541~546 각각 최소 1 축 강도 ≥ 8. 판정: 6/6 PASS.
2. `test_evidence_integrity(axes)` — 모든 증거 경로 실존. 판정: 파일 존재 rate ≥ 95%.
3. `test_orthogonality(axes)` — 9×9 중복도 임계치 ≤ 7 (필연 중복 승인 제외). 판정: ≤ 2 건 승인.
4. `test_honesty(axes)` — BT 해결 수 == 0. PARTIAL 3 표기 유지.
5. `test_phase_consistency(axes, phases)` — N=8 Phase 주도 축 매핑 완결.
6. `test_r3_final(axes)` — 신규 축 수 == 0, 흡수율 == 100%.

**메인**: `verify_all(axes) -> Map[str, bool] + summary_string`

---

## §7 정직성 선언

- **BT 해결 수 0/6 유지** (BT-547 Poincaré 는 Perelman 해결로 회고 전용)
- **PARTIAL 3건 처리 기록**:
  - SEED-06 Schaefer dichotomy — KEEP (Y2 에 유지)
  - SEED-15 Iwasawa mod 6 — CONDITIONAL 재분류, P5 Cremona 500k 실측 과제로 편입
  - SEED-21 Jones T(3,4) — 강도 3→2 하락, Y7 내 순위 6→7
- **새 수학 증명 미추가** (R3 는 내부 재정리만, Phase 2~5 에서만 부분결과 채굴)
- **자기참조 금지** (OUROBOROS 변경 예외)

---

## §8 이관 완료 체크리스트

- [x] 9축 모두 카드 작성됨 (Y1~Y9)
- [x] 6 BT 모두 최소 1축 강도 8+ (최대 강도 주 축 배정 완료)
- [x] Phase 8개 모두 주도 축 명시 (P0 axis / P1 전체 / P2 Y1 / P3 Y4 / P4 Y5+Y6 / P5 Y7+Y8 / P6 — / PΩ Y9)
- [x] 직교성 매트릭스 9×9 완결
- [x] 증거 경로 실존 (R1~R3 에서 이미 재검증)
- [x] 정직성 선언
- [x] verify 파이프라인 스펙 명시

**본 문서 = 7대 난제 서브프로젝트 축 체계 SSOT.** 이후 Phase 문서는 본 문서 참조.
