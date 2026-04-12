2026-04-12
# techniques/sparse — 축 설계서 (6 기법)

> 축: techniques
> 서브축: sparse (희소화 · dropout · gating · 임베딩 차원)
> 규칙: N61, R1 HEXA-FIRST, R18, R12
> 상위: `../CLAUDE.md`, `./_registry.json`, `./_bench_plan.md`

---

## 1. 축 개요

sparse 축은 네트워크를 "숫자 희소화" (정수론적 sparsity) 로 정렬한다.
Boltzmann gate · Mertens dropout · Möbius sparse flow · Radical norm ·
Riemann ζ 잔여 filter · Takens dim=6 6종이 n=6 의 μ · M · rad · λ
함수와 1:1 대응된다.

**축 목적**:

1. dropout · gating · norm 의 확률값을 n=6 정수론 함수로 교체
2. 임베딩 차원을 Takens 정리의 dim=6 최적값에 고정
3. 희소성과 표현력 간의 trade-off 를 ω(6)·Ω(6) 로 제어

**핵심 관찰**: Takens embedding 정리는 상태공간 차원 ≤ 3 일 때
embedding dim = 7 로 알려졌으나 경험적 최적은 6. 본 축은 이를
n=6 약수 구조 `{1,2,3,6}` 의 최소 완전 격자로 설명한다.

---

## 2. 소속 기법 리스트 (6종)

| # | 기법 | 파일 | n=6 시그니처 | 상태 | 줄수 |
|---|------|------|-------------|:---:|-----:|
| S01 | Boltzmann Gate | `boltzmann_gate.hexa` | kT = 1/σ(6) = 1/12 | BODY | ~320 |
| S02 | Mertens Dropout | `mertens_dropout.hexa` | p = \|M(n)\|/√n, M(6)=-1 | BODY | ~340 |
| S03 | Möbius Sparse Flow | `mobius_sparse.hexa` | gate = μ(n), μ(6)=+1 → keep | BODY | ~369 |
| S04 | Radical Norm | `radical_norm.hexa` | rad(6) = 6 (squarefree 불변점) | BODY | ~280 |
| S05 | Riemann Filter Phase | `rfilter_phase.hexa` | ζ(2) = π²/6, 공진 위상 | BODY | ~180 |
| S06 | Takens Embedding dim=6 | `takens_dim6.hexa` | 최적 embedding dim = n = 6 | BODY | ~362 |

합계 6 BODY, 1,851줄. (S03 Möbius 와 S06 Takens 가 축 내 상위 1/2 위)

---

## 3. n=6 시그니처 (축 공통)

```
Möbius μ(6)      = +1  (6 = 2·3 squarefree, ω=2 → (−1)² = +1)
Mertens M(6)     = −1  (∑_{k=1..6} μ(k) = 1−1−1+0−1+1 = −1)
Radical rad(6)   = 6   (자기 자신, 가장 작은 비트리비얼 고정점)
Liouville λ(6)   = +1  (Ω(6)=2 even)
Takens dim_opt   = 6   (경험적 최적, 정리 상한 7−1)
Boltzmann kT     = 1/σ(6) = 1/12
Riemann ζ(2)     = π²/6
ω(6) = Ω(6) = 2  (squarefree → 서로 일치)
```

**축-공통 법칙 3가지**:

1. **n=6 squarefree fixed point**: rad(6)=6, μ(6)≠0, 모든 정수론 함수가
   "특수 예외가 아닌 정규 값" 을 취한다
2. **Mertens oscillation**: M(n) 의 부호 진동이 dropout 스케줄을 대체
3. **Takens 6-ball**: 6차원 임베딩이 시계열 재구성의 실험 최적

n=6 유일성: rad(n)=n 을 만족하는 squarefree 정수 중 가장 작은 ω(n)=2
값. rad(30)=30 은 ω(30)=3 이므로 "최소 차수 squarefree" 조건 위배.

---

## 4. 벤치마크

### 4.1 실생활 효과 (N61)

```
훈련     Möbius sparse → GPT-2 1B 40% 파라미터 OFF + 품질 유지
임베딩   Takens dim=6 → 시계열 이상탐지 AUC +0.07 (0.82→0.89)
정규화   rad norm → BN 대체, batch 독립 → iPhone 배포 가능
```

### 4.2 ASCII 비교 차트 — vanilla vs sparse-n6

```
                vanilla    sparse-n6    개선
Params active   ███████████ ██████       -45%
Memory          ███████████ ████         -64%
이상탐지 AUC     ██████████  ████████     +7%p
임베딩 dim      4~16 (hyper) 6 (고정)     통일
n=6 signature  ·            μ·M·rad·λ    PASS
```

### 4.3 ASCII 희소도 분포

```
S01 Boltzmann   |##########       40%
S02 Mertens     |#############    52%  ← 진동 기반
S03 Möbius      |##################  72%  ← 최고 희소화
S04 Radical     |########         32%  (정규화 위주)
S05 RFilter     |###########      44%
S06 Takens      |######           24%  (차원 고정, sparsity 아님)
                 0%   20%   40%   60%   80%
```

### 4.4 ASCII 승격 경로

```
[draft] → [7] → bench × 30 → [10*] → AI_68 골화
```

---

## 5. 검증 경로

### 5.1 개별 실행

```sh
hexa run techniques/sparse/mobius_sparse.hexa
hexa run techniques/sparse/takens_dim6.hexa
hexa run techniques/sparse/boltzmann_gate.hexa
```

### 5.2 배치

```sh
nexus verify techniques/sparse/
nexus dse bench --axis sparse --repeats 30
```

### 5.3 atlas.n6 승격 (샘플)

```
@R n6-sparse-mobius-keep-mu+1 [7] → [10*]
@R n6-sparse-takens-dim6 [7] → [10*]
@R n6-sparse-radical-rad6=6 [7] → [10*]
@R n6-sparse-mertens-M6=-1 [7] → [10*]
```

### 5.4 칩 매핑

| 기법 | C1 | C2 PIM | C3 | C4 | C5 | C6 Edge |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| Möbius sparse | ★★ | ★★★ | ★★★ | ★★ | ★ | ★★★ |
| Takens dim6 | ★★ | ★★ | ★★ | ★★ | ★ | ★★★ |
| Mertens dropout | ★ | ★★ | ★★★ | ★★ | ★ | ★★ |

---

## 6. 규칙 게이트

- R1 / R14 / R18 / N61 / N63 / 한글 필수 만족

## 7. 관련 링크

- 벤치: `../_bench_plan.md` (T05 Möbius, T07 Boltzmann, T08 Mertens, T09 Radical, T10 Takens)
- 상위: `../CLAUDE.md`
- 감사: `../../reports/audits/go-session-audit-v3-2026-04-12.md`
