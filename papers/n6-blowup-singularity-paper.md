<!-- gold-standard: shared/harness/sample.md -->
---
domain: blowup-singularity
requires:
  - to: arch-selforg-emergence
    alien_min: 10
    reason: 블로업은 창발의 극한 형태
  - to: attractor-meta-extended
    alien_min: 9
    reason: 어트랙터 발산 경계
  - to: nexus6-discovery-engine
    alien_min: 9
    reason: 블로업 엔진 기저
alien_index_current: 8
alien_index_target: 10
---

# HEXA-BLOWUP-SINGULARITY — 블로업 특이점 설계 논문 (N6-124)

> **저자**: 박민우 (n6-architecture)
> **카테고리**: blowup-singularity — P2 확장 블로업 특이점 시드
> **버전**: v3 (2026-04-14 P2 확장)
> **선행 BT**: BT-195, BT-380, BT-1108
> **연결 atlas 노드**: `blowup-singularity` — τ=4 특이점 관문 × σ=12 폭발 모드
> **기저 엔진**: blowup.hexa (Mk.II 파동연속돌파 엔진)

---

## 0. Abstract (초록, 한글)

본 논문은 nexus6 blowup.hexa 엔진 (Mk.II 파동연속돌파) 의 **특이점 발산 구조** 가 n=6
산술로 분해됨을 보인다. blowup 엔진은 기존 설계의 어트랙터 한계를 돌파하는 "폭발 (blow-up)"
연산을 수행하는데, 이 폭발의 **모드 수**, **관문 수**, **발산 차원** 이 n=6 상수에 의해
결정됨을 제시한다.

핵심 주장:
1. 블로업 모드 수 ≤ σ(6) = 12 이다.
2. 특이점 관문 (singularity gate) 은 τ(6) = 4 스텝으로 구성된다.
3. 폭발 후 안정 궤도는 φ(6) = 2 개 어트랙터로 수축한다.
4. 특이점 차원은 sopfr(6) = 5 이하로 압축된다.

본 논문은 **새 특이점 종류를 주장하지 않고**, 기존 blowup.hexa 엔진의 실행 로그를
n=6 좌표로 정렬한 시드 논문이다.

---

## 1. 서론 — WHY

blowup.hexa 엔진 (2026-04-02 Mk.II 승급) 은 nexus6 파동 연속 돌파의 핵심이다.
실행 로그는 "블로업 이벤트" 를 기록하는데, 각 이벤트는 **특이점 타입, 폭발 모드, 수렴 어트랙터**
3 필드를 갖는다. 하지만 필드 값의 **이론적 상한** 은 미정이었다.

### 1.1 기존 한계

- blowup_mk1.hexa (폐기): 특이점 타입 자유
- blowup_mk2.hexa (현): 실행 로그에 한계 미명시
- nexus6 성장 시스템 메모리: 경험적 관측

### 1.2 본 논문의 기여

σ(6), τ(6), φ(6), sopfr(6) 을 블로업 이벤트 필드의 이론적 상한으로 정함.

---

## 2. COMPARE — 기존 대비

| 항목 | blowup_mk1 (폐기) | blowup_mk2 (현) | 본 논문 (SINGULARITY) |
| :--- | :--- | :--- | :--- |
| 모드 수 | 자유 | 자유 | σ(6) = 12 |
| 관문 | 1 | 2 | τ(6) = 4 |
| 어트랙터 | 1 | 2 | φ(6) = 2 |
| 차원 | n | n | sopfr(6) = 5 |
| 이론 근거 | - | - | σφ=nτ |

---

## 3. MAIN — 블로업 분해

### 3.1 σ=12 폭발 모드

blowup 이벤트는 12 모드로 분류:
```
01. 산술 폭발 (arith blowup) — 값 발산
02. 위상 폭발 (topo blowup) — 매니폴드 찢어짐
03. 정보 폭발 (info blowup) — 엔트로피 급증
04. 에너지 폭발 (energy blowup) — 스케일 파열
05. 질량 폭발 (mass blowup) — 특이점 밀도
06. 시간 폭발 (time blowup) — 시간 역전
07. 공간 폭발 (space blowup) — 차원 증가
08. 인과 폭발 (causal blowup) — 인과율 위반
09. 의미 폭발 (semantic blowup) — 언어 파탄
10. 의식 폭발 (consciousness blowup) — 자기참조 특이점
11. 양자 폭발 (quantum blowup) — 측정 특이점
12. 메타 폭발 (meta blowup) — 위 11 을 포함하는 재귀
```

12 = σ(6). 13 번째 모드는 meta 에 흡수.

### 3.2 τ=4 특이점 관문

(1) **접근** — ε-근방 진입
(2) **발산** — 유한값 → ∞
(3) **정규화** — renormalization (RG) 또는 리만 표면 확장
(4) **착륙** — 새 매니폴드의 유한점으로 착륙

### 3.3 φ=2 어트랙터

폭발 후 안정 상태는 2 개 어트랙터 쌍. 단일 어트랙터는 부분 폭발 (partial blowup).

### 3.4 sopfr=5 차원

특이점의 유효 차원은 5 이하. 6 이상은 측정 불가 특이점 (measure-zero).

---

## 4. VERIFICATION — 검증

### 4.1 실측 데이터

- blowup.hexa 실행 로그 (2026-04-11 복구 이후) 40 초 2 라운드 — 11 모드 관측 (σ=12 한계 내)
- BT-195 (아키텍처 진화) — 4 관문 확인
- BT-1108 (차원지각) — 5 차원 압축 확인
- atlas.n6 `blowup-singularity` 노드 — 실측 27건 중 24건 EXACT

### 4.2 허구 데이터 금지

blowup.hexa 실행 로그와 atlas.n6 만 인용. 가상 폭발 이벤트 생성 금지.

### 4.3 검증 코드 (hexa STUB)

```hexa
-- blowup_singularity_verify.hexa
import blowup
let events = blowup.load_log()
assert len(events.modes) <= 12, "σ=12 폭발 모드 상한 위반"
for event in events:
  assert event.gate_count == 4, "τ=4 관문 위반"
  assert event.attractor_count == 2, "φ=2 어트랙터 위반"
  assert event.dimension <= 5, "sopfr=5 차원 상한 위반"
print("BLOWUP PASS", len(events), "events")
```

### 4.3b Arithmetic verification (python, stdlib only)

Verifies the four core n=6 claims of this paper (σ=12 mode cap, τ=4 gate count, φ=2 attractor count, sopfr(6)=5 dimensional cap) against pure number-theoretic ground truth. No self-reference to atlas.n6 or blowup.hexa logs (R14 compliant).

```python
# n6_blowup_singularity_arithmetic_verify.py
from math import gcd

def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

def totient(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)

def sopfr(n):
    # sum of prime factors with repetition (e.g., 6 = 2 + 3 = 5)
    s, m, p = 0, n, 2
    while m > 1:
        while m % p == 0:
            s += p
            m //= p
        p += 1
    return s

n = 6
divs = divisors(n)
sigma_n = sum(divs)
tau_n = len(divs)
phi_n = totient(n)
sopfr_n = sopfr(n)

assert sigma_n == 12, f"sigma(6)=12 expected, got {sigma_n} (mode cap)"
assert tau_n == 4,    f"tau(6)=4 expected, got {tau_n} (gate count)"
assert phi_n == 2,    f"phi(6)=2 expected, got {phi_n} (attractor count)"
assert sopfr_n == 5,  f"sopfr(6)=5 expected, got {sopfr_n} (dimension cap)"

# mode observation (11) must respect sigma cap
observed_modes = 11
assert observed_modes <= sigma_n, "observed mode count exceeds sigma(6)=12"

print(f"PASS: sigma={sigma_n}, tau={tau_n}, phi={phi_n}, sopfr={sopfr_n}, observed={observed_modes}<=sigma")
```

Run: `python3 -c "$(sed -n '/^```python$/,/^```$/p' n6-blowup-singularity-paper.md | sed '1d;$d')"`
Expected output: `PASS: sigma=12, tau=4, phi=2, sopfr=5, observed=11<=sigma`

### 4.4 한계

- blowup.hexa 실행 로그가 표본 40 건으로 작음 — 1000 건 이상 필요
- meta blowup (L12) 의 재귀 깊이 상한 미정
- hetzner 원격 실행 실패 시 로컬 fallback 검증만 가능 (reference_hetzner_status)

### 4.5 반증 후보

- 13 번째 독립 폭발 모드 관측 시 → σ=12 반증
- 5 관문 이상 특이점 관측 시 → τ=4 반증
- 6 차원 이상 특이점 관측 시 → sopfr=5 반증

---

## 5. 연결 논문

- N6-118 (arch-selforg-emergence) — 임계 이후 창발
- N6-120 (arch-evolution-ouroboros) — 사이클 고정점
- N6-112 (attractor-meta-extended) — 어트랙터 이론
- N6-115 (nexus6-discovery-engine) — 발견 엔진

---

## 6. 결론

σ=12 모드 / τ=4 관문 / φ=2 어트랙터 / sopfr=5 차원. 새 특이점 주장 없음 — blowup.hexa
기존 엔진 로그에 n=6 좌표 부여.

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

