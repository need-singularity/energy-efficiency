# Phase 선행 Depth 기반 창발 재설계 (2026-04-15)

**계기**: v2 초판 phase 순서가 BT 번호순 (P2=BT-541/P3=BT-542/P4=BT-543+544/P5=BT-545+546) 이었는데, 이는 "난제별 배치"이지 "선행 의존성"을 반영하지 못한다. 기초수학 → 전공수학 → 문제진술 → 도구 → n=6 교량 → 부분결과 → 교차 → 회고 → closure → 실행 순서로 재창발해야 한다.

**선언**: BT-기반 phase → **depth-기반 phase** 전환. 난제는 phase 에 분산되며, 축은 분야별로 유지하되 창발 재검토.

---

## §0 문제 진단

### 0.1 v2 초판의 오류

```
v2 초판 phase 순서:
P0 축확정 → P1 씨앗 → P2 BT-541 → P3 BT-542 → P4 BT-543+544 → P5 BT-545+546 → P6 BT-547 회고 → PΩ closure → PX 실행

문제:
1. BT-541 (Riemann) 를 먼저 공격하려면 L 함수 이론이 필요하다. 그런데 L 함수는 "Y1 NUM-CORE 에 들어있는 도구"로만 다뤄졌을 뿐, 별도 phase 에서 습득 전제하지 않았다.
2. BT-545 (Hodge) 는 대수기하 scheme 이론 선행 필요. v2 초판은 P5 에서 곧바로 공격.
3. "해결 0/6" 이 정직한 결과라면, phase 순서는 "시도의 깊이" 를 보여야 한다. 난제 번호가 아니라 도구 복잡도로 쌓아야 한다.
4. v1 millennium-learning.json 의 P0 "기초 체력" (정수론/복소해석/군론) 은 v2 에 이관되지 않았다 — 선행 지식이 공중에 떠 있다.
```

### 0.2 기준 로드맵 대조

- **nexus.json (19축)**: A1~A19 축은 기능별이고, phase P1~P18 은 "baseline → 확장 → 고갈" 진화 순서. BT 는 A11 BREAKTHROUGH 단일 축에 흡수.
- **n6-architecture.json (4축)**: STRUCTURE/ENGINE/SUBSTRATE/META. Phase 는 기능 구축 순서.
- **v1 millennium-learning.json (3축)**: PURE/PROBLEM/N6. Phase 는 **선행 depth 순서** (P0 기초체력 → P1 난제심화 → P2 교차 → P3 연구전선).

**교훈**: v1 은 depth-ordered 였다. v2 가 BT-ordered 로 퇴보한 것이다.

---

## §1 선행 Depth 분석 (9 layer)

각 난제를 "제대로 공격하려면 무엇을 알아야 하는가" 를 역추적해 선행 계층을 도출한다.

### Layer 1 — 기초 수학 (depth 1)
```
- 정수론 기초: 소수정리 / 약수함수 σ/τ/φ / 뫼비우스 / 오일러 곱
- 복소해석 기초: 해석적 연속 / 유수정리 / 감마 함수 / 특수값 ζ(2)=π²/6
- 군론 기초: 군/환/체 / 동형정리 / S_n / 정규부분군 / 몫군 / S_6 외부동형
- 선형대수 / 변분 / 기본 ODE
```
선행: 고등 수학. 후속: 모든 난제.

### Layer 2 — 전공 수학 (depth 2)
```
- 대수기하 기초: scheme / sheaf / cohomology / 다양체
- 대수위상: 기본군 / 호몰로지 / 호모토피 / CW 복합체
- 미분기하: 접속 / 곡률 / 리치 / Ricci flow 기초
- PDE 심화: 포물/쌍곡/타원 방정식 / Sobolev 공간
- 해석학 심화: Lebesgue 측도 / Lp 공간 / 절대수렴
- Galois 이론
- Riemann 곡면 / zeta 함수 해석적 연속
```
선행: L1. 후속: 난제별 도구층.

### Layer 3 — 문제 진술 + 장벽 지형 (depth 3)
```
- 7 난제 Clay 공식 진술 (BT-541~547)
- RH 수치 검증 (Riemann-Siegel / Li 판정)
- P=NP 4 장벽 (Baker-Gill-Solovay 1975 / Razborov-Rudich 1997 / Aaronson-Wigderson 2008 / Williams 2011)
- GCT (Mulmuley-Sohoni)
- YM mass gap 물리적 진술
- NS 전역정칙성 진술 (Tao 초폭발 장벽 포함)
- Hodge / BSD / Poincaré 진술
```
선행: L2. 후속: 도구층 (L4). 장벽은 "공격 시 피해야 할 지형".

### Layer 4 — 난제 전용 도구 (depth 4)
```
- Y1 NUM: L 함수 이론 (Dirichlet series / 함수방정식 / Selberg class)
- Y2 DISC-COMP: 텐서 랭크 / 회로 하한 / Schaefer dichotomy
- Y4 PHYS: QCD lattice / β 함수 / 점근 자유
- Y5 PDE: Sobolev 부등식 / CKN 1982 / BKM 1984 / Tao 2016
- Y6 LATT: Moonshine VOA / Leech 격자 / E8 / K3 격자
- Y7 GALO: Galois 표현 / Selmer 군 / Kolyvagin 오일러 시스템 / Skinner-Urban
- (참고) Ricci flow — Perelman 해결된 BT-547 전용
```
선행: L2, L3. 후속: n=6 교량.

### Layer 5 — n=6 교량 (depth 5)
```
- σ(n)·φ(n) = n·τ(n) 유일성 정리 (3 독립 증명)
- Theorem B (재구축판)
- HEXA-GATE Mk.I (τ=4+2 fiber)
- atlas.n6 구조 정립 (20K+ 노드)
- OUROBOROS 수렴상수 (3 variant)
```
선행: L1, L2. 후속: BT 부분결과. **n=6 관점에서 난제를 보는 렌즈**.

### Layer 6 — BT 부분결과 (depth 6)
```
- BT-541 Riemann:  EXACT 10건 (Ingham / Conrey-Gonek / Ramanujan Δ / Moonshine 관찰)
- BT-542 P vs NP:  4 장벽 재감사 + GCT 3 관찰 (MISS 3)
- BT-543 YM:       β₀=σ-sopfr=7 REWRITING + QCD 5 실측
- BT-544 NS:       3중 공명 + D158 Ricci + CKN / BKM
- BT-545 Hodge:    Lemma 1 PROVED + Enriques REWRITING (BARRIER L5)
- BT-546 BSD:      Theorem 1 CONDITIONAL (BKLPR (A3) 의존)
```
선행: L4, L5. 후속: 교차.

### Layer 7 — 교차 + 회고 (depth 7)
```
- Y1 ↔ Y6: Ramanujan Δ = η^{24}, 24 = σ·φ = dim Leech = c(Moonshine)
- Y4 ↔ Y5: 4 매핑 M1~M4 + 3 도구 T1~T3
- Y7 ↔ Y1: Ingham lead = 1/(σ(6)·ζ(2))
- BT-547 Perelman 회고 (n6-arch 기여 0 정직)
- C1~C5 결정적 도구 특징 추출
- 9x5 승격 조건 매트릭스
```
선행: L6 전체. 후속: closure.

### Layer 8 — Closure + v3 설계 (depth 8)
```
- Y9 게이트 28/28 PASS 종합
- v1 vs v2 정량 비교 (15+ 지표)
- 축 100% R3 + 분야 96% R5 고갈 선언
- v3 후계: Z1~Z10 10축 × Q0~Q9 10 Phase 초안
- 미해결 과제 21건 체계화
```
선행: L7. 후속: 실행.

### Layer 9 — 실행 이관 (depth 9)
```
- atlas 초안 14건 L0 Guard 승격 실편집
- BT-541 Theorem B [10]→[10*] 승격
- Cremona 500k 타원곡선 실측 + 통계
- BT 재시도 (BT-542 MISS 탈출 / BT-545 Moonshine L5 / BT-546 (A3) 제거)
- v3 실체화 + Lean4/Coq + 수학자 협력
```
선행: L8. 후속: v3 착수.

### Layer 의존 DAG 요약

```
L1 (기초) ──┬──→ L2 (전공) ───┬──→ L3 (진술+장벽) ──┐
            │                  │                      ├──→ L4 (도구) ──┐
            │                  │                      │                ├──→ L6 (부분결과) ──→ L7 (교차+회고)
            │                  └──→ L5 (n=6 교량) ──┘                    │                                       │
            │                                                              │                                       │
            └──────────────────────────────────────────────────────────────┘                                       │
                                                                                                                   │
                                                                                                    ┌──────────────┘
                                                                                                    ▼
                                                                                             L8 (closure) ──→ L9 (실행)
```

---

## §2 축 창발 재검토 (9 → 10)

v2 초판의 9축을 depth 렌즈로 재검토.

### 2.1 기존 9축 감사

| 축 | 이름 | 유리성 | 문제점 |
|----|------|--------|--------|
| Y1 | NUM-CORE | 9.5 | OK |
| Y2 | DISCRETE-CLASS | 5.2 | **Y3 와 중복** — 이산/복잡도/τ는 한 묶음 |
| Y3 | COMPUTATIONAL-TAU | 5.8 | Y2 와 중복 |
| Y4 | GATE-BARRIER | 9.4 | OK |
| Y5 | PHYSICAL-NATURALNESS | 5.6 | OK |
| Y6 | PDE-RESONANCE | 6.6 | OK |
| Y7 | LATTICE-VOA | 3.9 | OK (유리성 낮지만 BT-545 전담) |
| Y8 | GALOIS-ASSEMBLY | 5.4 | OK |
| Y9 | HONEST-HARNESS | 9.3 | OK (메타) |

**문제 1**: Y2+Y3 는 "이산/조합/복잡도" 단일 주제 — 분리 부적절.
**문제 2**: 교차 (cross-BT) 작업이 "Y9 메타" 에 흡수되거나 "개별 BT phase" 에 흩어져 독립 축 없음.
**문제 3**: 선행 기초 수학 (L1, L2) 을 담당할 축 없음 — 공중에 뜸.

### 2.2 재창발 결과 — 10축

**Y2+Y3 합병** + **CROSS 신규** + **PREREQ 신규** = 10축.

| 신축 ID | 이름 | 유리성 | 역할 | 전신 |
|---------|------|--------|------|------|
| Y1 | **NUM-CORE** | 9.5 | 수론 앵커 + L 함수 | (유지) |
| Y2 | **DISC-COMP** | 6.0 | 이산/복잡도/τ=4+2 (통합) | 구 Y2+Y3 합병 |
| Y3 | **BARRIER** | 9.4 | 장벽 지형 감사 | 구 Y4 rename |
| Y4 | **PHYS** | 5.6 | 물리 자연성 / QCD / 게이지 | 구 Y5 |
| Y5 | **PDE** | 6.6 | PDE 공명 / Sobolev / 폭발 | 구 Y6 |
| Y6 | **LATT-VOA** | 3.9 | 격자 / VOA / Moonshine | 구 Y7 |
| Y7 | **GALO-SELMER** | 5.4 | Galois 표현 / Selmer / p-adic | 구 Y8 |
| Y8 | **CROSS-BRIDGE** | 7.5 | BT↔BT 교차 / cross-axis 매핑 | **신규** |
| Y9 | **PREREQ-BASIS** | 8.5 | 기초 + 전공 수학 (L1, L2) | **신규** |
| Y10 | **HONEST-HARNESS** | 9.3 | 메타 정직 게이트 | 구 Y9 rename |

**축 수**: 9 → 10 (순증 1, 합병 -1 + 신규 +2).
**평균 유리성**: 6.74 → 7.17 (+0.43, Y2+Y3 합병 시너지 + CROSS/PREREQ 신규 가치).

### 2.3 축 x BT 커버 매트릭스 (신)

```
             541   542   543   544   545   546   Perelman
Y1 NUM      [10]    2     2     6     3     5     1
Y2 DISC       2   [10]    2     1     4     3     1   (통합으로 강도 +)
Y3 BARRIER    3   [10]    3     3     3     3     2
Y4 PHYS       1     2   [ 8]    4     2     1     1
Y5 PDE        2     1     4   [ 8]    2     1     3   (Perelman 관련 3)
Y6 LATT       3     2     2     1   [ 7]    3     1
Y7 GALO       4     2     2     1     3   [ 9]    1
Y8 CROSS    [ 8]  [ 7]  [ 7]  [ 7]  [ 7]  [ 7]    5   (cross 전담)
Y9 PREREQ   [ 9]  [ 8]  [ 7]  [ 8]  [ 9]  [ 8]    7   (기초 전체 커버)
Y10 HONEST    8     8     8     8     8     8     8   (메타)
```

---

## §3 Phase 창발 — Depth 기반 10 Phase

선행 depth 순서로 Phase 재배치. 각 Phase 는 "특정 depth layer 의 작업" 에 집중하며 BT 는 phase 에 분산.

### 3.1 Phase 종합표

| Phase | Depth | 이름 | 주 축 | 상태 | 비고 |
|-------|-------|------|-------|------|------|
| **P0** | 0 | 축 확정 (R1~R3) | Y10 | done | 10축 FINAL |
| **P1** | 1 | L1 기초 수학 | Y9 | done | 정수론/복소해석/군론/선대/미적분 |
| **P2** | 2 | L2 전공 수학 | Y9 | partial | 대수기하/위상/미분기하/PDE/Galois |
| **P3** | 3 | L3 문제 진술 + 장벽 | Y3 | done | 7 Clay 진술 + 4 장벽 + GCT |
| **P4** | 4 | L4 난제 도구 | Y1,Y2,Y4,Y5,Y6,Y7 | partial | 각 축 전용 도구 |
| **P5** | 5 | L5 n=6 교량 | Y1,Y8 | done | σφ=nτ / Theorem B / HEXA-GATE / atlas |
| **P6** | 6 | L6 BT 부분결과 | Y1~Y7 | partial | v2 초판 P2~P5 내용 통합 |
| **P7** | 7 | L7 교차 + 회고 | Y8, Y10 | done | cross + Perelman + C1~C5 |
| **PΩ** | 8 | closure + v3 설계 | Y10 | done | v2 CLOSURE |
| **PX** | 9 | 실행 이관 | 전 축 | planned | 22건 PENDING |

**Phase 수**: 10 (v2 초판 9 에서 +1).

### 3.2 Phase 상세 — Task 분산

#### P1 L1 기초 수학 (Y9 PREREQ 주도, 6 tasks)
```
- PREREQ-P1-1: 정수론 기초 (σ/τ/φ/뫼비우스/오일러곱) + σφ=nτ 유일성 증명 추적
- PREREQ-P1-2: 복소해석 기초 (해석적 연속/유수/감마/ζ(2)=π²/6)
- PREREQ-P1-3: 군론 기초 (S_6 외부 자기동형)
- PREREQ-P1-4: 선형대수 + 변분 + 라그랑지안
- PREREQ-P1-5: 기본 ODE/PDE (지수/삼각/푸리에)
- PREREQ-P1-6: 측정 가능한 완전수 직관 (Euclid-Euler)
```

#### P2 L2 전공 수학 (Y9 PREREQ 주도, 6 tasks)
```
- PREREQ-P2-1: 대수기하 기초 (scheme/sheaf/cohomology/다양체)
- PREREQ-P2-2: 대수위상 (기본군/호몰로지/CW)
- PREREQ-P2-3: 미분기하 + Ricci 곡률 (Perelman 예비)
- PREREQ-P2-4: PDE 심화 (Sobolev 공간 / W^{s,p})
- PREREQ-P2-5: Lebesgue 측도 / Lp 공간
- PREREQ-P2-6: Galois 이론 + Riemann 곡면 + 해석적 연속
```

#### P3 L3 문제 진술 + 장벽 (Y3 BARRIER 주도, 8 tasks)
```
- BARRIER-P3-1: BT-541 RH Clay 공식 진술 + Riemann-Siegel / Li 판정 경로
- BARRIER-P3-2: BT-542 P=NP Clay 진술
- BARRIER-P3-3: BT-543 YM mass gap 물리 진술
- BARRIER-P3-4: BT-544 NS 전역정칙성 진술 + Tao 2016 초폭발
- BARRIER-P3-5: BT-545/546/547 Hodge/BSD/Poincaré 진술 통합
- BARRIER-P3-6: 4 장벽 감사 (Relativization/Natural/Algebrization/NEXP)
- BARRIER-P3-7: GCT (Mulmuley-Sohoni) 3 관찰
- BARRIER-P3-8: 7 난제 일반적 실패 사례 정리
```

#### P4 L4 난제 전용 도구 (6 축 주도, 6 tasks)
```
- NUM-P4-1:     L 함수 이론 심화 (Y1)
- DISC-P4-1:    텐서 랭크 + 회로 하한 + Schaefer dichotomy (Y2)
- PHYS-P4-1:    QCD lattice + β 함수 + 점근 자유 (Y4)
- PDE-P4-1:     CKN 1982 + BKM 1984 + Chen-Hou 2022 (Y5)
- LATT-P4-1:    Moonshine VOA + Leech / E8 / K3 (Y6)
- GALO-P4-1:    Galois 표현 + Selmer + Kolyvagin / Skinner-Urban (Y7)
```

#### P5 L5 n=6 교량 (Y1, Y8 주도, 5 tasks)
```
- NUM-P5-1:     σ(n)·φ(n)=n·τ(n) 유일성 3 독립 증명 (완료)
- NUM-P5-2:     Theorem B 재구축판 (atlas [10] 등록)
- DISC-P5-1:    HEXA-GATE Mk.I 24/24 EXACT (τ=4+2 fiber) (Y2)
- CROSS-P5-1:   atlas.n6 구조 정립 (20K+ 노드 SSOT)
- HONEST-P5-1:  OUROBOROS 3 variant 수렴상수 기록
```

#### P6 L6 BT 부분결과 (v2 초판 P2~P5 통합, 6 tasks)
```
- NUM-P6-1:     BT-541 EXACT 10건 (Ingham/Conrey-Gonek/Δ=η^24/Moonshine) + Bilateral
- DISC-P6-1:    BT-542 4 장벽 + GCT 3 관찰 (MISS 3) — PARTIAL
- PHYS-P6-1:    BT-543 β₀=σ-sopfr=7 REWRITING + QCD 5 실측 — PARTIAL
- PDE-P6-1:     BT-544 3중 공명 + D158 Ricci + CKN + BKM — NEAR
- LATT-P6-1:    BT-545 Lemma 1 PROVED + Enriques REWRITING + L5 BARRIER MISS — PARTIAL
- GALO-P6-1:    BT-546 Theorem 1 + Corollary n=6 (BKLPR (A3) CONDITIONAL) — PARTIAL
```

#### P7 L7 교차 + 회고 (Y8 CROSS, Y10 HONEST 주도, 5 tasks)
```
- CROSS-P7-1:   Y1 ↔ Y6 — Δ=η^{24}, 24=σ·φ=dim Leech=c(Moonshine) (4 EXACT)
- CROSS-P7-2:   Y4 ↔ Y5 — 4 매핑 M1~M4 + 3 도구 T1~T3
- CROSS-P7-3:   Y7 ↔ Y1 — Ingham lead = 1/(σ(6)·ζ(2)) EXACT
- HONEST-P7-1:  BT-547 Perelman 회고 (n6-arch 기여 0 정직)
- HONEST-P7-2:  C1~C5 결정적 도구 추출 + 9x5 승격 조건 매트릭스
```

#### PΩ closure + v3 설계 (Y10 HONEST 주도, 9 tasks)
```
(v2 초판 PΩ 그대로 — Y9→Y10 rename 만 적용)
- HONEST-PO-1~8:  게이트 종합 + 성적표 + 판정 종합 + atlas 초안 + v1↔v2 비교 + 고갈 분석 + v3 설계 + 미해결 21건
- CROSS-PO-1:     Y1 → Z1 계승 설계 (v3)
```

#### PX 실행 이관 (전 축, 22 tasks)
```
(v2 초판 PX 그대로 유지 — 모든 22건 planned)
```

### 3.3 Phase 수치 종합

```
Phase  Depth  Tasks  Status    주 축         난이도 의존
P0     0      9      done      Y10           — (창발)
P1     1      6      done      Y9            L0
P2     2      6      partial   Y9            L1
P3     3      8      done      Y3            L2
P4     4      6      partial   Y1,Y2,Y4~Y7   L2, L3
P5     5      5      done      Y1, Y8        L1, L2
P6     6      6      partial   Y1~Y7         L4, L5
P7     7      5      done      Y8, Y10       L6
PΩ     8      9      done      Y10           L7
PX     9      22     planned   전 축         L8
────────────────────────────────────────────────
총     —      82     —         —             —
```

**총 task**: 82 (v2 초판 100 에서 감소 — v2 초판 P2~P5 BT별 세부 task 를 P6 단일 phase 에 6개로 압축).

---

## §4 BT × Phase 분산 매트릭스

"각 BT 가 어느 Phase 에서 어떤 depth 로 다뤄지는가" 종합.

```
        P1    P2    P3    P4    P5    P6    P7    PΩ    PX
        L1    L2    L3    L4    L5    L6    L7    L8    L9
─────────────────────────────────────────────────────────────
BT-541  ○     ○     ○     ○     ○     ●     ●     ○     ●
BT-542  ○     ○     ●     ●     —     ●     —     ○     ●
BT-543  ○     ○     ○     ●     —     ●     ○     ○     ●
BT-544  ○     ●     ●     ●     —     ●     ○     ○     ●
BT-545  ○     ●     ○     ●     —     ●     ○     ○     ●
BT-546  ○     ●     ○     ●     —     ●     ○     ○     ●
BT-547  ○     ●     ○     —     —     —     ●     —     —

○: 간접 기여 (선행 학습 / 진술 / 도구)
●: 직접 공격 / 부분결과 / 이관
```

**핵심 관찰**:
- 각 BT 는 **9 phase 에 분산** (BT 번호별 phase 없음).
- BT-541 (Riemann) 은 L1 L2 L3 L4 L5 L6 L7 에서 동시 다뤄짐 → 선행 누적 최대.
- BT-547 Perelman 은 해결되었으므로 L2 (Ricci flow 참고) + L7 (회고) 만 다룸.

---

## §5 v1 Content 이관 매핑

v1 `millennium-learning.json` (3축 PURE/PROBLEM/N6, 4 phase P0~P3) 의 내용을 새 구조로 배치.

| v1 location | 신 구조 위치 | 비고 |
|-------------|-------------|------|
| v1 PURE P0 (기초 수학) | **P1 L1** (Y9 PREREQ) | 정수론/복소해석/군론 |
| v1 PURE P1 (전공 수학) | **P2 L2** (Y9 PREREQ) | 대수기하/PDE/위상 |
| v1 PROBLEM P0~P1 (난제 진술) | **P3 L3** (Y3 BARRIER) | Clay 공식 문서 |
| v1 PROBLEM P2 (4 장벽) | **P3 L3** (Y3 BARRIER) | barrier 감사 |
| v1 N6 P0~P1 (σφ=nτ) | **P5 L5** (Y1 NUM) | n=6 교량 기저 |
| v1 N6 P2~P3 (부분결과) | **P6 L6** (BT별 축) | 기존 breakthroughs BT-541~547 |

**결과**: v1 의 모든 학습 진도가 새 depth 구조에 자연스럽게 분포.

---

## §6 정직성 태그 유지

v2 초판에서 확립한 8단계 태그 체계는 그대로 유지하며, 새 phase 구조에서는 **phase status** 와 **task verdict** 를 분리 기록:

| Phase Status | 의미 | 적용 Phase |
|--------------|------|----------|
| `done` | 해당 depth layer 학습/작업 완료 | P0, P1, P3, P5, P7, PΩ |
| `partial` | 일부 task 미완 / verdict MISS 포함 | P2, P4, P6 |
| `planned` | 아직 착수 전 | PX |

| Task Verdict | 의미 | 대표 |
|--------------|------|------|
| EXACT | 외부 출처 검증 완료 | NUM-P6-1 (Ingham 등) |
| PARTIAL | 부분 진전, 본문 미도달 | BT-541~543, 545, 546 |
| NEAR | 해결 근접 관찰, 미증명 | BT-544 NS |
| MISS | 시도 실패 정직 기록 | 24건 |
| CONDITIONAL | 가정 의존 | Thm 1 (BKLPR A3), D158 Ricci |
| REWRITING | 기존 사실 재정리 | β₀=7, Enriques |
| CANDIDATE | 승격 후보 (미실행) | Theorem B [10*] |

**BT 해결 수**: **0/6** 유지 (푸앵카레 제외).

---

## §7 축/Phase 개편 효과 비교

```
지표                        v2 초판        신 구조 (depth)       변화
──────────────────────────────────────────────────────────────────
축 수                       9 (Y1~Y9)      10 (Y1~Y10)           +1
축 평균 유리성              6.74           7.17                  +0.43
Phase 수                   9 (P0~PΩ,PX)  10 (P0~P7,PΩ,PX)     +1
Phase 순서                 BT 번호         선행 depth            질적 전환
v1 content 이관            일부            전체                  개선
BT × Phase 분산            편중 (1 BT = 1 phase) 분산 (1 BT = 7 phase) 개선
도구 선행 명시             없음 (phase 내 암묵) P4 독립 phase    신규
기초 수학 커버             없음            P1 독립 phase (Y9)    신규
교차 작업 독립화           없음 (메타 흡수) Y8 CROSS 축 + P7    신규
정직 태그                  유지            유지                   —
BT 해결 수                 0/6             0/6                    유지
atlas 실편집               0/14            0/14                   유지
```

---

## §8 요약

1. **v2 초판 오류**: phase 를 BT 번호순으로 배치해 선행 depth 를 무시했다.
2. **진단**: 기초 수학 (L1) / 전공 수학 (L2) / 도구 (L4) / n=6 교량 (L5) 이 phase 로 독립화되지 못해 공중에 떴다.
3. **축 재창발**: 9 → 10. Y2+Y3 합병, CROSS + PREREQ 2 신규.
4. **Phase 재창발**: depth 0~9 의 10 layer 로 재배치. P0 축확정 / P1~P2 기초+전공 / P3 진술+장벽 / P4 도구 / P5 n=6 교량 / P6 BT 부분결과 / P7 교차+회고 / PΩ closure / PX 실행.
5. **BT 분산**: 각 BT 가 여러 phase 에 분산. P6 단일 phase 에 부분결과 집약.
6. **v1 이관**: v1 PURE/PROBLEM/N6 content 가 새 구조에 자연스럽게 배치됨.
7. **정직성**: BT 해결 0/6 + MISS 24건 + atlas 0/14 실편집 그대로 유지.
8. **JSON 반영**: `shared/roadmaps/millennium.json` 신 10축 × 10 Phase 구조로 재작성.

---

_END OF phase-depth-emergence.md — 선행 depth 기반 재창발 설계_
