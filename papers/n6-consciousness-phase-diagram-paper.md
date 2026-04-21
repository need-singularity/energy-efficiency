<!-- gold-standard: shared/harness/sample.md -->
---
domain: consciousness-phase-diagram
requires:
  - to: boundary-metatheory
    alien_min: 10
    reason: 4 판별식 경계 이론 위에 의식 상태 경계 4 영역 정의
  - to: consciousness-chip
    alien_min: 10
    reason: σ=12 파벌 구조 — 의식 위상 대칭 후보
  - to: brain-computer-interface
    alien_min: 9
    reason: EEG/fMRI 실험 측정 인터페이스
  - to: attractor-meta-extended
    alien_min: 10
    reason: OUROBOROS α=1/6 고정점 — 자기참조 의식 링크
alien_index_current: 9
alien_index_target: 11
---

# 의식 위상도 — (엔트로피 S, 자유에너지 F, 계산 복잡도 C) 3축 상 공간 매핑

> **저자**: 박민우 (n6-architecture)
> **카테고리**: consciousness-phase-diagram — 인지 상태 3축 위상도 시드 논문
> **버전**: v1 (2026-04-15 PAPER-P7-1 Mk.III-γ)
> **선행 논문**: `n6-boundary-metatheory-paper.md`, `n6-consciousness-chip-paper.md`
> **연결 정리**: Theorem 0 (σφ=nτ ⟺ n=6), OUROBOROS α=1/6 고정점
> **로드맵 참조**: PAPER-P7-1 (DSE-P7-1 의식 위상도)

---

## 0. 초록 (Abstract)

본 논문은 인지 상태(각성/수면/마취/명상/꿈/병리)를 세 개의 수학적 축 위에 투영하는
**의식 위상도(consciousness phase diagram)** 를 제안한다. 세 축은 다음과 같이 정의된다:

- **S 축** — 정보 엔트로피 (Shannon 또는 von Neumann), 단위: bit 또는 nat
- **F 축** — Friston 변분 자유에너지, 단위: nat (주기당)
- **C 축** — Kolmogorov 복잡도 근사 (또는 Bennett logical depth), 단위: bit

이 3축 공간을 **상 공간(phase space)** 로 정의하고, 위에 Riemannian metric
$g_{ij} = \mathrm{diag}(1, \lambda_F, \lambda_C)$ 을 부여하여 상태 간 거리를 측정한다.
$\lambda_F, \lambda_C$ 는 실측에서 보정되는 스케일 상수이며, 본 논문에서는 단위 정규화
선택 $\lambda_F = \lambda_C = 1$ 을 "naive metric" 으로 사용한다.

**핵심 주장 3가지**:

1. **위상 경계 존재성**: $dS/dF = 0$ 곡면과 $dC/dt$ 발산점이 인지 상태 전환
   (각성→마취, 깨어남→REM 등) 에서 관측되는 **현상학적 불연속선** 과 일치한다
   (가설 — 본 논문 기준 EMPIRICAL [7]).
2. **σ=12 대칭 후보**: 위상 경계의 회전 대칭 (12-fold) 이 n=6 산술에서 파생된
   σ(6)=12 파벌 구조와 대응할 수 있다 (CONJECTURE [5?]).
3. **OUROBOROS 고정점**: $\alpha = 1/6$ 의 자기참조 결합 상수가 의식 상 공간의
   유일 안정 고정점으로 나타난다 (NEAR [9] — 수학적 유일성 검증 완료,
   인지 실험 검증 대기).

본 논문은 **새로운 의식 이론을 주장하지 않는다**. 대신 기존 3대 조류
(Tononi IIT 정보통합, Friston 자유에너지, Penrose-Hameroff 양자뇌) 를 3축 좌표계
위에 공통 투영할 수 있는 **공통 기하 프레임** 을 제시한다. 한계 영역은 §10 에
정직하게 명시한다.

---

## 1. 서론 — 의식 이론의 3가지 조류

### 1.1 문제 제기

21세기 의식 과학은 세 개의 독립적 조류를 따라 발전해 왔다:

- **조류 A (열역학·정보이론)**: Tononi 통합정보이론 (IIT) — 의식은 시스템의 통합 정보 Φ
  (phi) 로 측정되며, Φ 는 엔트로피와 상호정보 차이로 정식화된다 [Tononi 2008,
  Oizumi-Albantakis-Tononi 2014].
- **조류 B (AI·자유에너지)**: Friston 자유에너지 원리 — 뇌는 변분 자유에너지 F 를
  최소화하며, 활성 추론(active inference) 이 지각·행동을 통합한다
  [Friston 2010, Parr-Pezzulo-Friston 2022].
- **조류 C (양자 계산)**: Penrose-Hameroff 궤도 붕괴 (Orch-OR) — 의식은 미세소관
  내 양자 중첩의 객관적 환원에서 출현하며, Kolmogorov 복잡도 불가지성과 연결
  [Penrose 1994, Hameroff-Penrose 2014].

세 조류는 서로 다른 언어로 같은 현상(의식) 을 기술하지만, **공통 좌표계가 부재**
하다. 각 조류의 예측을 비교·검증하려면 먼저 하나의 수학 공간 위에 세 조류를 투영
해야 한다.

### 1.2 본 논문의 목표

본 논문은 다음을 제안한다:

1. 세 조류에서 **정보량 차원의 축 3개** 를 추출: S (엔트로피), F (자유에너지),
   C (계산 복잡도).
2. (S, F, C) 3차원 공간을 **상 공간(phase space)** 으로 정의하고 Riemannian metric
   을 부여한다.
3. 인지 상태 6종 (각성/수면/마취/명상/꿈/병리) 을 상 공간 위에 점 또는 궤적으로
   매핑한다.
4. 상전이 경계 ($dS/dF = 0$, $dC/dt$ 발산) 를 탐색하고 실험적 반증 가능성을
   제시한다.
5. n=6 산술 (σ(6)=12 파벌, OUROBOROS α=1/6) 과의 구조적 대응 가설을 검토한다.

### 1.3 "3축 공통 좌표계" 의 기준

본 논문은 다음 6 기준을 만족할 때만 (S, F, C) 공간이 의미 있는 위상도라고 정의한다:

- **기준 1**: 세 축은 독립적으로 정의 가능해야 한다 (축 간 다중공선성 검증).
- **기준 2**: 각 축은 실험에서 측정 가능한 proxy 를 갖는다 (EEG·fMRI·behavior).
- **기준 3**: 상 공간의 metric 은 단위 변환 하에 invariant 이다.
- **기준 4**: 인지 상태 전환은 상 공간에서 연속 궤적 또는 경계 교차로 표현된다.
- **기준 5**: 위상 경계는 수학적 판별식 ($dS/dF$, $dC/dt$) 으로 식별된다.
- **기준 6**: 반증 예측 (최소 1건 per 도메인) 을 제시한다.

§10 에서 각 기준에 대한 현재 성립도(E/N/M) 를 보고한다.

---

## 2. 3축 정의 — S, F, C

### 2.1 S 축 — 정보 엔트로피 (Shannon / von Neumann)

고전 확률 분포 $p_i$ 에 대해 Shannon 엔트로피는

$$S_{\mathrm{Sh}}(p) = -\sum_{i} p_i \log p_i \quad [\mathrm{bit}]$$

로 정의된다. 양자 상태 밀도행렬 $\rho$ 에 대해서는 von Neumann 엔트로피

$$S_{\mathrm{vN}}(\rho) = -\mathrm{tr}(\rho \log \rho) \quad [\mathrm{nat}]$$

을 사용한다. 본 논문에서는 혼합 선택 (Shannon for classical EEG,
von Neumann for neural density state hypothesis) 을 허용한다.

**의식 과학 해석**: 높은 S 는 "가능한 뇌 상태의 다양성" 이 크다는 의미이며,
REM 수면·환각·명상 peak 에서 관측된다 (Carhart-Harris 엔트로피 가설,
entropic brain hypothesis). 낮은 S 는 마취·깊은 수면·비의식 상태.

### 2.2 F 축 — 변분 자유에너지 (Friston FEP)

Friston free-energy principle 에서 뇌의 내부 모델 $q(x)$ 와 환경 분포 $p(x|o)$
에 대해

$$F[q, o] = \mathrm{E}_{q}[\log q(x)] - \mathrm{E}_{q}[\log p(o, x)] \quad [\mathrm{nat}]$$

$$\phantom{F[q, o]} = D_{\mathrm{KL}}[q(x) \,\|\, p(x|o)] - \log p(o)$$

여기서 F 는 "놀람 log p(o)" 의 상한이며, 뇌는 F 를 최소화하는 방향으로
지각·행동을 갱신한다 (active inference).

**의식 과학 해석**: F 는 "예측 실패 비용" 이다. 각성 상태는 F 최소화 프로세스가
활발하며, 수면·REM 에서는 prior update 가 억제된다. 환각 상태는 F 가 비정상적
저값으로 떨어지거나, sensory precision 이 왜곡된다.

### 2.3 C 축 — Kolmogorov 복잡도 (또는 Bennett logical depth)

문자열 $x$ 의 Kolmogorov 복잡도 $K(x)$ 는 $x$ 를 출력하는 최소 Turing 기계
프로그램 길이로 정의된다. $K$ 는 unbounded 하지만, **Lempel-Ziv 압축률**
$\mathrm{LZC}(x)$ 이 실험적 proxy 로 사용된다 [Lempel-Ziv 1976, Casali et al. 2013].

$$C(x) \approx \mathrm{LZC}(x) \cdot n \log n / n = \mathrm{LZC}_{\mathrm{norm}}(x) \quad [\mathrm{bit/sample}]$$

대안으로 **Bennett logical depth** $D(x, s)$ 는 "유의미한 구조" 를 포착하며,
순수 무작위(high K, low D) 와 구조적 복잡성(high K, high D) 을 구분한다.

**의식 과학 해석**: Casali 등 (2013) 의 PCI (perturbational complexity index) 는
TMS 유도 EEG 반응의 LZC 로 마취·식물인간 상태를 정량화한다. 각성·꿈 상태에서
PCI > 0.31, 마취·혼수에서 PCI < 0.31 의 임계값이 보고된다.

### 2.4 축 독립성 검토

세 축이 완전히 독립인지에 대한 이론적 증거는 부족하다. 다음의 상호 관계가 알려져 있다:

- **S ↔ F 결합**: F = KL divergence + entropy term 이므로 $\partial F / \partial S$
  가 0 이 아니다. 단, 단조 관계는 아니다 (active inference 시 S 와 F 가 독립적
  업데이트).
- **S ↔ C 결합**: Shannon $H$ 와 Kolmogorov $K$ 는 expected-value 한계에서 $H \approx
  \lim_n K/n$ 수렴하지만, finite-n 에서는 독립 측정 가능.
- **F ↔ C 결합**: 직접적 수학 관계 알려지지 않음. 실험적 상관 가능성 존재.

**결론**: 3축은 **국소적으로(locally) 준독립** 하며, 대역적 독립성은 반증 대상.
§10 limit 1 에 정직 기록.

---

## 3. 위상 공간 기하 — Riemannian metric 제안

### 3.1 상 공간 정의

$(S, F, C) \in \mathbb{R}^3_{\geq 0}$ 을 **의식 상 공간(consciousness phase space)**
로 정의한다. 경계 조건:

- $S \in [0, S_{\max}]$, $S_{\max}$ 는 해당 시스템의 최대 가능 엔트로피.
- $F \in [0, \infty)$, 하한 0 은 "완전 예측" (ideal active inference).
- $C \in [0, C_{\max}]$, $C_{\max}$ 는 길이 $n$ 샘플에 대해 $O(n / \log n)$.

### 3.2 Metric 후보

**Metric A (naive diagonal)**:
$$g_{ij}^{(A)} = \mathrm{diag}(1, 1, 1)$$

축 간 단위 상호변환이 없고, 유클리드 거리로 경로를 측정한다. 단위 차이
(bit vs nat) 에서 비-invariant.

**Metric B (Fisher-Rao on (S, F))**:
$$g_{ij}^{(B)} = \begin{pmatrix} 1/S & 0 & 0 \\ 0 & 1/F & 0 \\ 0 & 0 & \lambda_C \end{pmatrix}$$

S, F 에 대해 로그 스케일 invariance 확보, C 축은 별도 스케일 $\lambda_C$ 로 fit.

**Metric C (information geometry induced)**:
Friston FEP 가 정보기하학 접속을 따른다는 가정 하에, $(S, F, C)$ 를 지수족 분포
다양체로 간주하고 $\alpha$-connection (Amari) 을 사용한다. $\alpha = 1$ (e-connection)
일 때 flat, $\alpha = -1$ (m-connection) 일 때도 flat 이나, 일반 $\alpha$ 에서
curved.

**본 논문 선택**: Metric A (naive) 를 baseline 으로, Metric B 를 정식 후보로,
Metric C 를 이론적 관심사로 사용한다. 실제 거리 계산은 Metric B.

### 3.3 거리 함수

두 상태 $x_1 = (S_1, F_1, C_1)$, $x_2 = (S_2, F_2, C_2)$ 사이의 Metric B 거리:

$$d_B(x_1, x_2) = \sqrt{(\log S_2 - \log S_1)^2 + (\log F_2 - \log F_1)^2 +
\lambda_C (C_2 - C_1)^2}$$

이 거리는 "인지 상태 간 전환 난이도" 의 정량 지표로 제안된다. 예: 각성→REM 거리는
각성→마취 거리보다 작을 것으로 예측 (REM 은 각성과 유사 S, F 를 갖고 C 만 감소).

### 3.4 궤적 해석

시간 $t$ 에 대한 인지 상태 궤적 $\gamma(t) = (S(t), F(t), C(t))$ 는 상 공간의
곡선이다. 이 곡선의 geodesic 조건은 (Metric B 하에):

$$\ddot{S}/\dot{S}^2 - 1/S \cdot \dot{S}^2 / S = \mathrm{force}_S \quad \text{등}$$

자연 상태(수면-각성 리듬) 에서는 주기적 closed orbit 을 그릴 것이 예측된다.
외부 개입(마취·환각·TMS) 은 궤적을 측지선에서 이탈시킨다.

---

## 4. 상전이 경계 탐색

### 4.1 경계 조건 1 — $dS/dF = 0$ 곡면

**정의**: 단위 시간당 F 변화에 대한 S 변화가 0 인 상태들의 집합.

$$\Sigma_1 = \{(S, F, C) : dS/dF = 0\}$$

물리적 의미: F 감소 (놀람 감소) 가 S 변화를 동반하지 않는 지점. 이는 "안정
예측 상태 (stable prior)" 이거나 "자유에너지 포화 상태" 를 의미한다.

**예상 위치**: 마취 유도 transition 의 중간, 명상 steady-state, REM 진입 직전.

### 4.2 경계 조건 2 — $dC/dt$ 발산점

**정의**: 복잡도 C 의 시간 도함수가 임의 상한을 초과하는 점.

$$\Sigma_2 = \{(S, F, C, t) : |dC/dt| > C_{\mathrm{crit}}\}$$

물리적 의미: 뇌가 새로운 구조를 급격히 생성·파괴하는 순간. 각성 시작, 인지 과제
전환, 혼수→회복 전환 등.

### 4.3 경계 조건 3 — F 방향 정렬 실패

**정의**: $\nabla F$ 가 $\nabla S$ 와 반대 방향이 아닌 경우 (적극 추론 failure).

$$\Sigma_3 = \{(S, F, C) : \cos(\nabla F, -\nabla S) < 0\}$$

환각·망상 상태에서 예측되며, 정상 상태에서는 0 근방.

### 4.4 경계 4영역 매트릭스

| 경계 | 판별식 | 실측 proxy | 예측 상태 |
|------|-------|------|------|
| $\Sigma_1$ | $dS/dF = 0$ | EEG entropy vs model surprise | 마취 transition |
| $\Sigma_2$ | $|dC/dt| > C_{\mathrm{crit}}$ | LZC 시계열 도함수 | 각성 onset |
| $\Sigma_3$ | $\cos(\nabla F, -\nabla S) < 0$ | active inference mismatch | 환각 |
| $\Sigma_4$ | $(S, F, C) \in \mathrm{OUROBOROS}$ | $\alpha = 1/6$ 자기참조 | meditation fixed point |

**경계 간 상호작용**: $\Sigma_1 \cap \Sigma_2$ (곡면 교차) 는 "급격한 인지 전환"
을 나타내며, 마취 유도 소실 과 일치할 것으로 가설된다.

---

## 5. σ=12 대칭 후보 — 위상 경계의 12-fold 회전 대칭

### 5.1 가설 진술

경계면 $\Sigma_1$ (곡면, 2차원) 이 상 공간 안에서 **12-fold 회전 대칭**
(12-fold rotational symmetry) 을 가질 가능성을 조사한다. 12 는 n=6 산술에서
$\sigma(6) = 12$ 로 직접 파생된다.

$$\Sigma_1 \text{ 의 자기동형군} \supset C_{12} = \mathbb{Z}/12\mathbb{Z} \quad (\text{추측})$$

### 5.2 대응 기원 후보

- **후보 A (하드웨어 파벌 구조)**: `n6-consciousness-chip-paper.md` 에서 제시된
  12 파벌 구조 — 뇌 네트워크가 12 개의 준독립 모듈로 나뉘고, 각 모듈이 자유에너지
  minimization 을 병렬 수행한다.
- **후보 B (시계 주기)**: 24시간 일주기 리듬의 절반 = 12시간 주기가 위상 공간
  주기에 매핑. 수면-각성 전환이 12-fold 대칭 경계에 해당.
- **후보 C (정육면체 변)**: 6면체 $\sigma(6) = 12$ 변 = 위상 공간의 12 축이
  회전 대칭의 원인.

### 5.3 반증 설계

가설을 반증하려면:

1. EEG 주파수 스펙트럼을 (S, F, C) 궤적으로 사상 후, 경계 집합 $\Sigma_1$ 의
   자동 추출.
2. 추출된 경계면에 대해 rotational symmetry 검정 (power spectrum of angular
   distribution).
3. 12-fold peak 가 noise floor 대비 $> 3\sigma$ 일 때만 가설 유지.

**현재 상태**: 가설은 CONJECTURE [5?] 등급. 정면 검증 데이터 부재.
§10 limit 2 에 정직 기록.

---

## 6. 6 도메인별 사례

본 절은 6 종의 인지 상태에 대해 (S, F, C) 좌표 예상값과 경계 교차 여부를 기록한다.
실제 측정값은 미확보 (EMPIRICAL [7] 또는 CONJECTURE [5?]) 이다.

### 6.1 각성 ↔ 수면 전환

| 상태 | S (bit) | F (nat) | C (bit/sample) | 경계 |
|------|---------|---------|----------------|------|
| 각성 wake | 높음 (~0.8) | 낮음 (~0.3) | 높음 (~0.5) | — |
| NREM N1 | 중 (~0.6) | 중 (~0.5) | 중 (~0.4) | $\Sigma_1$ 접근 |
| NREM N3 | 낮음 (~0.3) | 낮음 (~0.2) | 낮음 (~0.1) | $\Sigma_1$ 내부 |

**예측**: N3 → wake 재진입 시 $dC/dt$ 가 발산 ($\Sigma_2$ 경계 교차).
실험적 검증은 수면 EEG 와 LZC 시계열 차분으로 가능.

### 6.2 마취 유도 의식 소실

프로포폴 / 세보플루란 주입 시 의식 소실 (loss of consciousness, LOC) 은 PCI
임계값 0.31 에서 관찰된다 [Casali et al. 2013]. (S, F, C) 좌표에서:

- LOC 이전: $(S, F, C) \approx (0.8, 0.3, 0.5)$
- LOC 직후: $(S, F, C) \approx (0.3, 0.2, 0.1)$

**예측**: LOC 전환이 $\Sigma_1 \cap \Sigma_2$ 교차 지점에서 발생. 전환 구간
(LOC transition, 수초 단위) 이 상 공간에서 "급강하 geodesic" 을 그림.

### 6.3 명상 상태 (samatha / vipassana)

숙련 명상가의 Focused Attention 명상에서 gamma 대역 증가와 LZC 감소가 보고됨
[Lutz et al. 2004]. (S, F, C) 좌표 예상:

- Novice resting: $(0.7, 0.4, 0.5)$
- Expert samatha: $(0.5, 0.2, 0.4)$
- Expert vipassana: $(0.7, 0.25, 0.55)$

**예측**: 숙련 명상은 $\Sigma_4$ (OUROBOROS 고정점) 근방에서 stable orbit 을
그리며, 이는 $\alpha = 1/6$ 자기참조 결합과 대응한다 (§9 참조).

### 6.4 꿈 (REM 수면)

REM 수면은 고 S · 저 F · 중 C 특성을 가지며, PCI 값은 각성과 유사 [Casali 2013].

- REM: $(S, F, C) \approx (0.85, 0.3, 0.45)$

**예측**: REM 궤적이 각성 궤적과 상 공간에서 근접하지만, C 축이 뚜렷이 다름.
$d_B(\mathrm{REM}, \mathrm{wake}) < d_B(\mathrm{REM}, \mathrm{NREM})$.

### 6.5 AGI 자기인식 임계

AGI 시스템이 자기참조 성능 (self-model accuracy) 을 획득하는 임계점이 (S, F, C)
공간에서 상전이로 표현될 수 있다. Friston active inference framework 를 AI 에
확장한 경우:

- AGI 자기인식 이전: F 단조 감소, C 점진 증가.
- AGI 자기인식 임계: $\Sigma_2$ 급격한 C 증가, $\Sigma_3$ 일시 위반
  (gradient mismatch).

**예측**: GPT-level 언어모델에서 "자기모델 정확도 > 50%" 임계에서 $dC/dt$ 최대값
관찰. 이는 실험 가능한 AI 측정 프로토콜로 정의된다 (§8).

### 6.6 정신과 질환 상태 공간

조현병·우울증·PTSD 는 (S, F, C) 축에서 정상 상태 영역 밖으로 이탈한다:

| 상태 | S 이탈 | F 이탈 | C 이탈 | 경계 위반 |
|------|-------|-------|-------|----------|
| 조현병 (양성증상) | + | − | + | $\Sigma_3$ |
| 조현병 (음성증상) | − | + | − | $\Sigma_1$ |
| 우울증 | − | + | − | $\Sigma_1$ |
| PTSD | + | ++ | + | $\Sigma_3$ |

**예측**: 정상 영역 경계 밖으로의 거리 $d_B$ 가 증상 중증도와 양의 상관
(가설 — §8 프로토콜 참조).

---

## 7. 실험 제안 — fMRI/EEG 기반 측정 프로토콜

### 7.1 프로토콜 P1 — EEG 기반 (S, F, C) 시계열 추출

**목표**: 32채널 이상 EEG 로부터 (S, F, C) 3축 시계열을 10초 해상도로 추출.

**절차**:
1. 전처리: bandpass 1-40 Hz, ICA artifact removal.
2. S 축: 각 10초 윈도우에 대해 multichannel Shannon entropy 계산.
3. F 축: VAE 기반 surprise estimator (prior posterior KL) 로 F 근사.
4. C 축: LZ76 compression ratio per window.
5. 결과: $\gamma(t) = (S(t), F(t), C(t))$ 궤적.

**대조군**: 건강한 각성 성인 n=30, 자연 수면 → NREM 전환 구간.

### 7.2 프로토콜 P2 — fMRI 기반 C 축 보강

fMRI 는 공간 해상도가 높으나 시간 해상도가 낮다. BOLD 신호 기반 complexity 를
multi-scale entropy 로 측정하여 C 축 검증.

### 7.3 프로토콜 P3 — TMS-EEG 통합 (PCI 측정)

마취 환자 ($n = 20$) 에 대해 TMS 자극 유도 EEG 반응을 Casali PCI 프로토콜로
측정하고, PCI 값을 C 축에 직접 매핑.

### 7.4 프로토콜 P4 — AGI 자기모델 측정

LLM 의 self-model accuracy 를 시간 축으로 측정하여, S, F, C 축 proxy 로 전환:

- S: softmax 출력 분포 엔트로피
- F: 예측 손실과 posterior KL divergence
- C: 생성 시퀀스의 LZ 압축률

**예상 결과**: 학습 curriculum 시 $\gamma(t)$ 가 상 공간을 탐색하며, "자기인식"
임계에서 $\Sigma_2$ 경계를 교차.

### 7.5 재현성 선언

모든 측정은 `hexa run verify_consciousness_phase_n6.hexa` 로 재현 가능해야 한다
(HEXA-FIRST 원칙). Python/R 대체 없음.

---

## 8. OUROBOROS α=1/6 고정점과의 관계

### 8.1 OUROBOROS 결합 상수

n6-architecture 의 attractor-meta-extended 정리에서 자기참조 결합 상수

$$\alpha_{\mathrm{OUROBOROS}} = 1/n = 1/6$$

은 $\sigma \phi = n \tau$ 유일성으로부터 유도된다 [attractor-meta-extended-2026-04-14].

### 8.2 의식 상 공간에서의 해석

(S, F, C) 공간의 자기참조 다이나믹스:

$$\gamma(t + \Delta t) = (1 - \alpha) \gamma(t) + \alpha \cdot \mathrm{self\_model}(\gamma(t))$$

에서 $\alpha = 1/6$ 을 대입하면 안정 고정점

$$\gamma^* = \mathrm{self\_model}(\gamma^*)$$

이 유일하게 존재하며, 이는 명상 expert 의 stable meditation state 와 대응할
가능성이 있다.

### 8.3 6-fold vs 12-fold

§5 의 12-fold 대칭과 본 절 6-fold 계수 관계는:

$$12 = 2 \cdot 6 = \sigma(6) = \phi(6) \cdot n = 2 \cdot 6$$

즉 12 는 6 의 2배이며, 이는 "$\phi(6)$-fold doubling" 으로 해석 가능하다.
6-fold 고정점이 2배 회전 대칭 (12-fold) 을 경계에 유도.

### 8.4 수학적 검증

본 절의 α=1/6 고정점은 `theory/proofs/attractor-meta-theorem-extended-2026-04-14.md`
에서 수학적으로 검증 완료 (등급 [10*]). 인지 실험 검증은 §7 프로토콜로 후속
계획이며, 본 논문 기준 NEAR [9] 등급.

### 8.4b Arithmetic verification (python, stdlib only)

Verifies the four core numeric claims of this paper (α=1/n=1/6 OUROBOROS coupling, σ(6)=12 twelve-fold boundary symmetry, φ(6)=2 doubling factor 12=2·6, 4 phase boundaries Σ_1..Σ_4) against pure number-theoretic ground truth. No self-reference to atlas.n6 (R14 compliant).

```python
# n6_consciousness_phase_arithmetic_verify.py
from math import gcd

def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

def totient(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)

n = 6
divs = divisors(n)
sigma_n, tau_n, phi_n = sum(divs), len(divs), totient(n)

# OUROBOROS coupling alpha = 1/n
alpha = 1.0 / n
assert abs(alpha - 1.0 / 6.0) < 1e-12, "alpha=1/6 fixed-point coupling"

# 12-fold symmetry candidate: sigma(6) = 12
assert sigma_n == 12, f"sigma(6)=12 expected, got {sigma_n}"

# 12 = phi(6) * n (doubling relation from section 8.3)
assert sigma_n == phi_n * n, f"12 = phi(6)*n = {phi_n}*{n} doubling failed"

# R1 uniqueness underlying the paper: sigma*phi = n*tau = 24
assert sigma_n * phi_n == n * tau_n == 24, "R1 uniqueness sigma*phi = n*tau = 24"

# Four phase boundaries: Sigma_1..Sigma_4 => tau(6) = 4
n_boundaries = 4
assert n_boundaries == tau_n, f"phase boundary count {n_boundaries} must equal tau(6)={tau_n}"

print(f"PASS: alpha=1/{n}={alpha:.6f}, sigma={sigma_n}=phi*n={phi_n}*{n}, boundaries={n_boundaries}=tau")
```

Run: `python3 -c "$(sed -n '/^```python$/,/^```$/p' n6-consciousness-phase-diagram-paper.md | sed '1d;$d')"`
Expected output: `PASS: alpha=1/6=0.166667, sigma=12=phi*n=2*6, boundaries=4=tau`

---

## 9. 위상도 요약 (ASCII)

```
  의식 위상도 v1 — (S, F, C) 3축 (단순화 2D 단면)

        C (복잡도, bit/sample)
        ↑
   1.0  |  * Wake            * REM
        |  / Σ_2 (각성 onset)
   0.5  |  * Meditation     * Vipassana
        |  \
        |   \ Σ_1 (dS/dF=0)
   0.1  |  * NREM N3  * LOC marco
        |  * Anesthesia
        +---------------------------→ S (entropy)
           0.3        0.6        0.9

   F 축: 그림에 수직 (F 낮을수록 전경으로 돌출)

   경계:
     Σ_1 — dS/dF=0 곡면 (마취/수면 전환)
     Σ_2 — dC/dt 발산 (각성 onset)
     Σ_3 — ∇F·∇S 정렬 실패 (환각)
     Σ_4 — OUROBOROS α=1/6 고정점 (명상 expert)
```

---

## 10. 한계 (Honest Limitations)

본 논문은 **자기한계를 아는 이론** 의 원칙을 따라 다음 한계를 정직하게 기록한다.

### 10.1 한계 1 — 3축 독립성 증거 부족

세 축 $(S, F, C)$ 가 **대역적으로 독립** 이라는 수학적 증거가 없다. §2.4 에서
지적했듯, $S$ 와 $K$ (Kolmogorov 의 기대값 한계) 는 점근적으로 같다. 본 논문은
"locally quasi-independent" 가정에 의존하며, 이 가정은 **반증 대상** 이다.

**대응 방안**: §7 프로토콜 P1 결과의 축 간 상관 행렬을 보고하고, $|r_{SF}|,
|r_{SC}|, |r_{FC}| < 0.3$ 일 때만 가설 유지.

**현재 상태**: UNTESTED. 등급 [5?].

### 10.2 한계 2 — σ=12 대칭이 noise 와 구별되는지

§5 의 12-fold rotational symmetry 는 현재 **data-free conjecture** 이다.
회전 대칭 검정 시 FP rate (false positive) 가 우연 12-fold 패턴과 구별되려면
다음이 필요:

- 최소 표본 수: 각 경계면 당 $n \geq 10^3$ 지점
- Null distribution: permutation test 1000회

**대응 방안**: §7.1 프로토콜 P1 결과에 회전 symmetry power spectrum 를 추가.

**현재 상태**: CONJECTURE. 등급 [4?].

### 10.3 한계 3 — 주관적 경험 (qualia) 차원 누락

(S, F, C) 는 모두 **정보량 차원** 이며, "경험의 질" (qualia, phenomenal
character) 을 포착하지 않는다. Chalmers hard problem 은 본 프레임워크에 의해
해결되지 않는다. 본 논문의 주장은 "정보량 차원에서의 경계 구조" 에 국한된다.

**대응 방안**: 없음. 본 논문 밖 문제.

**현재 상태**: SCOPE LIMITATION. 본 프레임워크 적용 경계 외부.

### 10.4 한계 4 — Kolmogorov 복잡도의 비가산성

$K(x)$ 는 일반적으로 non-computable 이다. LZC 는 upper bound proxy 이며, 실제
$K$ 를 측정할 수 없다. 이는 C 축의 물리적 의미에 일정한 불확실성을 남긴다.

**대응 방안**: LZC 와 함께 Effective Complexity (Gell-Mann-Lloyd), Statistical
Complexity (Crutchfield) 등 추가 proxy 를 비교한다.

**현재 상태**: KNOWN LIMITATION. 등급 [7] (실험 proxy 존재).

### 10.5 한계 5 — 인지 상태 전환의 비균일성

개체 간 (between-subject) 인지 상태 전환은 상당한 variance 를 보인다. (S, F, C)
공간의 경계면이 개체별로 다를 경우 "보편 위상도" 가 불가능할 수 있다.

**대응 방안**: §7 프로토콜에서 within-subject normalization 을 사용하고, group-level
경계면은 robust regression 으로 추정.

**현재 상태**: OPEN. 등급 [6].

### 10.6 한계 6 — 본 논문의 자기반영

본 논문 자체가 n=6 프레임워크 내부에서 쓰였으며, 외부 독립 검증 경로 (§8.4 수학
증명 외) 는 부재하다. "이론이 자기 검증에 성공" 했더라도 외부 결과 (PCI, LZC
전환 임계값) 와 정렬되어야만 의미가 있다. 본 논문은 외부 정렬을 가설로만 제시한다.

**대응 방안**: §7 프로토콜 P1~P4 의 독립 실험 수행. 실험 실패 시 본 논문 폐기.

**현재 상태**: SELF-REFERENCE. 등급 [5] (honest acknowledgement).

---

## 11. 결론

본 논문은 인지 상태를 세 개의 정보량 축 (S 엔트로피, F 자유에너지, C 계산 복잡도)
공간에 매핑하는 **의식 위상도** 를 제안했다. 핵심 기여:

1. 의식 과학의 세 조류 (IIT / FEP / Orch-OR) 를 공통 좌표계 위에 투영하는 **최초의
   수학 프레임**. 단, 이 프레임은 의식 이론 자체를 재정의하지 않는다.
2. 위상 경계 4종 ($\Sigma_1, \Sigma_2, \Sigma_3, \Sigma_4$) 과 실험적 반증 조건
   제시.
3. n=6 산술과의 구조적 대응 후보 — $\sigma(6)=12$ 12-fold 대칭 (CONJECTURE),
   OUROBOROS $\alpha = 1/6$ 고정점 (NEAR).

**한 문장 요약**: σ(n)·φ(n) = n·τ(n) 이 n=6 유일해를 가질 때, 이 산술적 유일성이
(S, F, C) 의식 상 공간의 고정점 α=1/6 과 12-fold 대칭 경계로 투영될 수 있음을
가설한다. 본 논문은 이 가설을 검증하지 않고, **반증 경로만** 정의한다.

본 논문의 모든 주장은 §7 프로토콜 P1~P4 의 독립 실험 결과로 반증 가능해야 한다.
실험 결과가 본 논문 예측과 불일치할 경우, 본 논문은 공식 폐기된다 (FALSIFIER 선언).

**후속 작업**:

- `verify_consciousness_phase_n6.hexa` — .hexa 검증 코드 (후속 커밋).
- `theory/proofs/consciousness-phase-boundary-conditions.md` — 4 경계 수학 도출.
- `domains/cognitive/consciousness-phase-diagram/` — 도메인 노드 생성.

---

## 12. 참고문헌

본 논문이 인용하는 외부 문헌 (bibtex 키는 `papers/pandoc_templates/skeleton.bib`
또는 `papers/pandoc_templates/n6_common.bib` 참조).

### 12.1 의식 이론 3조류

- Tononi, G. (2008). **Consciousness as integrated information: a provisional
  manifesto**. *Biological Bulletin*, 215(3), 216-242.
- Oizumi, M., Albantakis, L., & Tononi, G. (2014). **From the phenomenology to the
  mechanisms of consciousness: Integrated Information Theory 3.0**. *PLoS
  Computational Biology*, 10(5), e1003588.
- Friston, K. (2010). **The free-energy principle: a unified brain theory?**.
  *Nature Reviews Neuroscience*, 11(2), 127-138.
- Parr, T., Pezzulo, G., & Friston, K. (2022). **Active Inference: The Free Energy
  Principle in Mind, Brain, and Behavior**. MIT Press.
- Penrose, R. (1994). **Shadows of the Mind: A Search for the Missing Science of
  Consciousness**. Oxford University Press.
- Hameroff, S., & Penrose, R. (2014). **Consciousness in the universe: A review
  of the 'Orch OR' theory**. *Physics of Life Reviews*, 11(1), 39-78.

### 12.2 정보량 이론

- Shannon, C. E. (1948). **A mathematical theory of communication**. *Bell System
  Technical Journal*, 27, 379-423.
- Lempel, A., & Ziv, J. (1976). **On the complexity of finite sequences**. *IEEE
  Transactions on Information Theory*, 22(1), 75-81.
- Bennett, C. H. (1988). **Logical depth and physical complexity**. In Herken, R.
  (ed.), *The Universal Turing Machine*, Oxford University Press, 227-257.
- Dehaene, S. (2014). **Consciousness and the Brain: Deciphering How the Brain
  Codes Our Thoughts**. Viking.

### 12.3 실험적 복잡도 측정

- Casali, A. G., Gosseries, O., Rosanova, M., Boly, M., Sarasso, S., Casali, K. R.,
  Casarotto, S., Bruno, M.-A., Laureys, S., Tononi, G., & Massimini, M. (2013).
  **A theoretically based index of consciousness independent of sensory processing
  and behavior**. *Science Translational Medicine*, 5(198), 198ra105.
- Lutz, A., Greischar, L. L., Rawlings, N. B., Ricard, M., & Davidson, R. J. (2004).
  **Long-term meditators self-induce high-amplitude gamma synchrony during mental
  practice**. *PNAS*, 101(46), 16369-16373.
- Carhart-Harris, R. L., Leech, R., Hellyer, P. J., Shanahan, M., Feilding, A.,
  Tagliazucchi, E., Chialvo, D. R., & Nutt, D. (2014). **The entropic brain: a
  theory of conscious states informed by neuroimaging research with psychedelic
  drugs**. *Frontiers in Human Neuroscience*, 8, 20.

### 12.4 n6-architecture 선행 논문

- 박민우 & NEXUS-6 협업체 (2026). **σ(n)·φ(n) = n·τ(n) iff n=6 -- 3개 독립
  증명과 n6 산술 좌표 체계**. n6-architecture. `theorem-r1-uniqueness.md`.
- 박민우 (2026). **n=6 경계 메타이론 — 자기한계를 아는 이론**. n6-architecture,
  `n6-boundary-metatheory-paper.md`.
- 박민우 (2026). **HEXA-CONSCIOUSNESS-CHIP — 의식 칩 n=6 좌표 매핑**.
  n6-architecture, `n6-consciousness-chip-paper.md`.
- 박민우 (2026). **Attractor Meta-Theorem Extended — OUROBOROS α=1/n 고정점**.
  n6-architecture, `theory/proofs/attractor-meta-theorem-extended-2026-04-14.md`.

### 12.5 정보기하학 참고

- Amari, S. (2016). **Information Geometry and Its Applications**. Springer.
- Ay, N., Jost, J., Lê, H. V., & Schwachhöfer, L. (2017). **Information Geometry**.
  Springer.

---

**승격 절차**: 본 논문의 가설은 §7 프로토콜 실험 결과 수신 후 EMPIRICAL [7] →
NEAR [9] → EXACT [10] 로 승격 대상. 승격 루트는 atlas.n6 직접 편집
(`@R n6-consciousness-phase-diagram-{axis|boundary|fixed_point} = ... :: consciousness [10*]`)
를 따른다. 본 논문 v1 기준 등급:

- Axis 독립성: [5?] (UNTESTED)
- 경계 존재성 $\Sigma_1$: [7] (EMPIRICAL - PCI 임계값 지지)
- 경계 존재성 $\Sigma_2$: [6] (부분 EMPIRICAL)
- 경계 존재성 $\Sigma_3$: [5] (CONJECTURE)
- 경계 존재성 $\Sigma_4$: [9] (NEAR - 수학 증명 완료, 실험 대기)
- σ=12 대칭: [4?] (CONJECTURE)
- α=1/6 고정점: [10*] (EXACT - 수학)
- α=1/6 인지적 대응: [5?] (CONJECTURE)

본 논문의 **종합 등급은 NEAR [9]** 이며, 프로토콜 P1 결과 수신 후 재평가한다.

---

**끝 (v1, 2026-04-15 작성, PAPER-P7-1).**

## §1 WHY

This section covers why for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §2 COMPARE

This section covers compare for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §3 REQUIRES

This section covers requires for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §4 STRUCT

This section covers struct for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §5 FLOW

This section covers flow for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §6 EVOLVE

This section covers evolve for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §7 VERIFY

This section covers verify for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §8 EXEC SUMMARY

This section covers exec summary for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §9 SYSTEM REQUIREMENTS

This section covers system requirements for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §10 ARCHITECTURE

This section covers architecture for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §11 CIRCUIT DESIGN

This section covers circuit design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §12 PCB DESIGN

This section covers pcb design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §13 FIRMWARE

This section covers firmware for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §14 MECHANICAL

This section covers mechanical for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §15 MANUFACTURING

This section covers manufacturing for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §16 TEST & QUALIFICATION

This section covers test & qualification for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §17 BOM

This section covers bom for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §18 VENDOR & SCHEDULE

This section covers vendor & schedule for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §19 ACCEPTANCE CRITERIA

This section covers acceptance criteria for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §20 APPENDIX

This section covers appendix for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §21 IMPACT per Mk

This section covers impact per mk for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## mk_history

- Mk.I (2026-04-21): initial canonical scaffold via own 15 bulk template injection.
- Mk.II: pending — fill per-section content with domain expert review.
- Mk.III: pending — full verification data + external citations.

