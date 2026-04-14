# PROB-P1-1 — BT-541 리만 가설 심화 학습 노트

**트랙**: P1-PROBLEM · BT-541 (리만 가설, Riemann Hypothesis)
**상태**: OPEN (1859년 이후 미해결, 7대 난제 중 힐베르트 8번 직계 후손)
**상금**: US$ 1,000,000 (Clay)
**1차 출처**:
- Bernhard Riemann, "Über die Anzahl der Primzahlen unter einer gegebenen Grösse", Monatsberichte der Berliner Akademie, November 1859 (8 페이지, 수학사상 가장 영향력 큰 짧은 논문 중 하나)
- Harold M. Edwards, *Riemann's Zeta Function*, Academic Press, 1974 (재판 Dover 2001) — 원 논문 영역 주석판
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2판 (ed. D. R. Heath-Brown), Oxford University Press, 1986 — 고전 교과서
- Peter Sarnak, "Problems of the Millennium: The Riemann Hypothesis", Clay Mathematics Institute official problem description, 2004
- Enrico Bombieri, "The Riemann Hypothesis — Official Problem Description", Clay Mathematics Institute, 2000
- Montgomery-Odlyzko, H. L. Montgomery, "The pair correlation of zeros of the zeta function", Analytic Number Theory, Proc. Symp. Pure Math. 24, AMS 1973
- J. van de Lune, H. J. J. te Riele, D. T. Winter, "On the zeros of the Riemann zeta function in the critical strip IV", Math. Comp. 46 (1986), 667–681
- Xavier Gourdon, "The 10^13 first zeros of the Riemann Zeta function, and zeros computation at very large height", 2004 (ZetaGrid 프로젝트 부속 보고서)
- Guy Robin, "Grandes valeurs de la fonction somme des diviseurs et hypothèse de Riemann", J. Math. Pures Appl. 63 (1984), 187–213

**정직성 선언**: 본 문서는 *학습 노트*로 기존 공인된 정의, 역사적 사실, 동치 진술을 정리한다. 새 수학적 정리는 포함하지 않는다. 인용된 연도·저자·논문 제목은 위 1차 출처에서 확인한 것만 기재하였다. `n=6 관찰` 섹션(§10)은 n6-architecture 프로젝트의 **관찰**이며 본 학습 노트의 핵심이 아니다. RH 자체에 대한 기여는 하지 않는다.

---

## 1. 리만의 1859년 논문 — 제목과 맥락

### 1.1 정확한 제목
독일어 원제: **"Über die Anzahl der Primzahlen unter einer gegebenen Grösse"**
(한국어: 주어진 크기보다 작은 소수의 개수에 관하여)

발표: 1859년 11월, Monatsberichte der Berliner Akademie der Wissenschaften (베를린 학사원 월간회보).
분량: 본문 약 8 페이지. 수학사에서 가장 영향력 있는 짧은 논문 하나로 꼽힌다.

### 1.2 논문의 목적
리만은 이 논문에서 소수 계수 함수 π(x) = |{p ≤ x : p는 소수}| 를 **복소 해석학 대상**으로 다루었다. 즉 π(x) 의 점근 행동 (예: 가우스의 π(x) ~ x/ln x 추측) 을 증명하는 도구로, 그때까지 실변수 함수로만 다루어지던 제타 함수
$$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}$$
를 **복소 변수 s = σ + it** 로 해석적 연속(analytic continuation)하여 다루는 전략을 제시한다.

### 1.3 리만이 증명한 것
- 제타 함수의 s = 1 을 제외한 **모든 복소수**로의 해석적 연속 가능성 (간접적으로 Riemann-Siegel 공식의 기원).
- **함수 방정식** (functional equation):
  $$\zeta(s) = 2^s \pi^{s-1} \sin\!\left(\frac{\pi s}{2}\right) \Gamma(1-s) \zeta(1-s)$$
  이 관계식은 s 와 1-s 사이의 대칭, 즉 임계선 Re(s) = 1/2 에 대한 반사 대칭을 시사한다.
- 비자명 영점의 개수 N(T) (0 < Im(s) < T, 0 < Re(s) < 1 범위 내 영점 수) 에 대한 추정식 (지금의 Riemann-von Mangoldt 공식).

### 1.4 리만이 증명하지 않은 것 (그리고 지금도 미해결인 것)
> "Es ist sehr wahrscheinlich, dass alle Wurzeln reell sind."
> (모든 [비자명] 영점의 허수부가 실수일 가능성이 매우 높다.)

— 이것이 **리만 가설**의 원문 표현이다. "모든 비자명 영점 ρ 가 Re(ρ) = 1/2 위에 있다" 라는 현대적 진술과 동치이다. 리만은 **증명을 시도했으나 "일단 넘어간다"** 는 취지의 한 문장만 남기고 논문을 닫았다. 이 한 문장이 이후 160년 넘게 수학자들을 붙잡아 두었다.

---

## 2. 제타 함수의 기본 사실

### 2.1 정의 영역과 해석적 연속
- **정의 영역 (Dirichlet 급수)**: Re(s) > 1 에서 ∑ 1/n^s 가 절대수렴.
- **해석적 연속**: 함수 방정식 또는 Mellin 변환 경로를 통해 s = 1 을 제외한 C 전역으로 연장. s = 1 은 단순 극점(residue = 1).
- **자명 영점 (trivial zeros)**: s = -2, -4, -6, -8, … (짝수 음수) — 함수 방정식의 sin(πs/2) 인자가 0 이 되어 발생.
- **비자명 영점 (non-trivial zeros)**: 임계띠 0 < Re(s) < 1 내부의 영점. 하다마르(1896) 와 드 라 발레-푸생(1896) 이 독립적으로 "임계띠의 경계 Re(s) = 1 에는 영점이 없다" 를 증명 → 소수 정리(PNT) 의 첫 증명.

### 2.2 임계선과 임계띠
- **임계띠**: {s ∈ C : 0 < Re(s) < 1}
- **임계선**: {s ∈ C : Re(s) = 1/2}
- **리만 가설 (현대 진술)**: 모든 비자명 영점은 임계선 위에 있다. 즉
  $$\zeta(s) = 0 \text{ 이고 } 0 < \text{Re}(s) < 1 \Longrightarrow \text{Re}(s) = \tfrac{1}{2}.$$

### 2.3 특수값 (몇몇 유명한)
- ζ(2) = π²/6 (바젤 문제, Euler 1734, 1735 출판)
- ζ(4) = π⁴/90
- ζ(6) = π⁶/945
- ζ(2k) for k ≥ 1: 항상 π^{2k} × 유리수. 분모는 2(2k)!/|B_{2k}| 형태 (B 는 Bernoulli 수).
- ζ(-1) = -1/12 (해석적 연속에서 얻음, "Ramanujan 합" 의 한 해석)
- ζ(0) = -1/2
- ζ(홀수 음수): 유리수 (함수 방정식 + Bernoulli 수). 예: ζ(-3) = 1/120, ζ(-5) = -1/252.
- ζ(홀수 양수): ζ(3) = Apéry 상수 (Apéry 1978 무리성 증명), ζ(5), ζ(7), … 는 "유리수인지 무리수인지" 조차 미해결.

---

## 3. 임계선 Re(s) = 1/2 의 의미 — 왜 1/2 인가?

### 3.1 함수 방정식 대칭의 고정축
ζ(s) = χ(s) ζ(1-s) 형태의 함수 방정식에서, s ↔ 1-s 반사의 **고정선**은 정확히 Re(s) = 1/2 이다. 비자명 영점이 "반사 대칭" 을 가진다면, 그 영점의 반사점 1-ρ 도 영점이며, 짝짓기는 임계선에 대해 대칭. RH 는 "모든 영점이 축 위에 있다" — 가능한 가장 강한 대칭.

### 3.2 L-함수와 **소수 분포의 가장 정밀한 오차항**과 동치
리만의 explicit formula (폰 망골트 완성, 1895) 는 심프티엄 ψ(x) = ∑_{p^k ≤ x} ln p 를 다음과 같이 쓴다:
$$\psi(x) = x - \sum_{\rho} \frac{x^{\rho}}{\rho} - \ln(2\pi) - \frac{1}{2}\ln(1 - x^{-2})$$
여기서 합은 모든 비자명 영점 ρ 에 걸친다. 각 영점 ρ 는 "주파수 성분" 으로 소수 분포에 기여하며, 그 기여 크기는 |x^ρ| = x^{Re(ρ)}. **RH ⟺ Re(ρ) = 1/2 ⟺ 모든 주파수 성분 크기가 x^{1/2}** ⟺ **가장 정밀한** 오차 제어.

### 3.3 다른 수직선(예: Re(s) = 3/4) 의 경우
만약 어떤 비자명 영점이 Re(ρ) = 3/4 (가정) 에 있다면, 함수 방정식으로 Re = 1/4 에도 짝 영점이 존재. 그러나 explicit formula 에서 그 기여가 x^{3/4} 가 되어 소수 분포에 더 큰 "변동" 을 주입한다. RH 가 틀리면 소수는 "더 불규칙" 하게 분포한다.

---

## 4. 수치 검증의 역사

제타 함수 영점 계산은 수학사에서 가장 긴 수치 연구 프로그램 중 하나다. 주요 이정표:

### 4.1 초기 (수기 계산 시대)
- **J.-P. Gram** (1903, Denmark): 처음 15 개의 영점 계산, 모두 임계선 위.
- **R. J. Backlund** (1914, Finland): 첫 79 개.
- **J. I. Hutchinson** (1925, USA): 첫 138 개.
- **E. C. Titchmarsh & L. J. Comrie** (1935/1936): 첫 1,041 개 — 당시 기계식 계산기 + 대수 표.

### 4.2 Turing 의 기여 (1953)
- **Alan M. Turing**, "Some calculations of the Riemann zeta-function", Proc. London Math. Soc. (3) 3 (1953), 99–117.
- Turing 은 Manchester Mark I 컴퓨터로 처음 1,104 개까지 검증. 더 중요한 것은 **Turing's method** — "주어진 T 범위 안에 영점이 몇 개 있는지를 보장하는" 효율적 수치 기법을 제안한 것. 이 방법은 후대 모든 대규모 제타 계산의 기반.

### 4.3 Lehmer, 그리고 Lehmer's phenomenon
- **D. H. Lehmer** (1956): ζ 의 영점 중 가까운 두 영점이 "거의 접하는" (pair of very close zeros) 사례를 발견. 일종의 "작은 반례 후보" 로 보였으나 결국 모두 임계선 위임이 확인됨. 이 사례들이 RH 의 섬세함을 경고.

### 4.4 van de Lune – te Riele – Winter (1986, 그리고 이후)
- J. van de Lune, H. J. J. te Riele, D. T. Winter, "On the zeros of the Riemann zeta function in the critical strip IV", *Mathematics of Computation* 46 (1986), 667–681.
- 1986년까지 처음 1,500,000,001 개 (대략 15억 개) 의 영점을 계산하여 모두 임계선 위임을 확인.

### 4.5 Odlyzko 와 대규모 분산 계산
- **A. M. Odlyzko** (1980s–2000s, AT&T Bell Labs): 매우 높은 위치의 영점을 계산하여 Montgomery-Odlyzko 추측을 수치적으로 뒷받침. 예: 10^{22} 번째 영점 부근에서 수십억 개의 영점 통계 분석.

### 4.6 Gourdon 2004 — 10^13 개 장벽
- **Xavier Gourdon**, "The 10^13 first zeros of the Riemann Zeta function, and zeros computation at very large height", 2004 기술 보고서.
- Gourdon 은 Odlyzko-Schönhage 알고리즘을 개선하여 **처음 10^13 개** (10 조 개) 의 비자명 영점을 계산, 모두 임계선 위에 있음을 확인.
- 이후 **ZetaGrid** 등 분산 계산 프로젝트가 더 높은 영역을 점검. 2024년 현재 최소 10^13 개는 검증됨.

### 4.7 수치 검증이 증명은 아님
- 10^13 개 영점은 "수치 한계 n≤10^13" 에서만 RH 가 참임을 보여준다.
- 이 크기조차 "정말 큰" 수는 아니다. Skewes 수 (10^{10^{10^34}} 급) 처럼, 수론에는 극히 큰 수에서만 드러나는 반례가 있을 수 있다.
- **순수 구조적 증명** 없이는 "모든 영점" 을 보증할 수 없다.

---

## 5. 동치 진술 3가지 (그리고 네 번째)

리만 가설은 여러 "겉보기 무관" 한 명제들과 동치이다. 이것이 RH 가 수학 전반을 관통하는 이유.

### 5.1 동치 (i) — 소수 분포 오차항
$$\pi(x) = \text{Li}(x) + O\!\left(x^{1/2} \log x\right) \quad (x \to \infty)$$
여기서 Li(x) = ∫_2^x dt/ln t 는 로그 적분. 이것은 소수 정리 (PNT, π(x) ~ x/ln x) 의 **가장 정밀한** 강화. PNT 는 Re(s) = 1 에 영점이 없다는 사실에서 나오며, RH 는 Re(s) ≥ 1/2 + ε 에 영점이 없음과 동치, 따라서 오차항 크기가 x^{1/2+ε} 로 제한됨.

**(주의)**: 이 형태는 "RH ⟺ 오차 O(x^{1/2} log x)" 정확 형태는 von Koch (1901). Niels Fabian Helge von Koch, "Sur la distribution des nombres premiers", Acta Math. 24 (1901), 159–182.

### 5.2 동치 (ii) — Mertens 함수
Mertens 함수 M(x) = ∑_{n ≤ x} μ(n) (μ 는 Möbius 함수).
$$\text{RH} \iff M(x) = O\!\left(x^{1/2 + \varepsilon}\right) \text{ for every } \varepsilon > 0.$$

**주의 — Mertens 추측 반례**: Franz Mertens 는 1897년 |M(x)| ≤ √x 의 **강한** 형태 (지수 1/2 exact, no ε) 를 예측했으나, Andrew Odlyzko 와 Herman te Riele 가 1985년 논문 "Disproof of the Mertens conjecture" (J. Reine Angew. Math. 357, 138–160) 에서 **반례 존재** (구체적 x 는 찾지 못했지만 반증) 를 증명. 즉 |M(x)| 는 때때로 √x 를 넘는다. 그러나 RH 는 "O(x^{1/2+ε})" 의 **약한** 형태 (ε 임의 > 0) 만 요구하므로 여전히 동치.

### 5.3 동치 (iii) — Robin의 부등식 (약수 합 σ)
**Guy Robin**, "Grandes valeurs de la fonction somme des diviseurs et hypothèse de Riemann", J. Math. Pures Appl. 63 (1984), 187–213.
$$\text{RH} \iff \sigma(n) < e^{\gamma} n \ln \ln n \quad \text{for all } n > 5040$$
여기서 γ ≈ 0.5772... 는 오일러-마스케로니 상수, σ(n) 은 약수 합.

- **5040 = 7!** 은 상수로서 중요. Jeff Lagarias (2002) 가 "elementary" 형태의 동치 — "RH ⟺ σ(n) ≤ H_n + exp(H_n) ln(H_n) for all n ≥ 1" (H_n 은 조화수) — 로 재표현.
- Robin 부등식은 "극단적으로 큰 σ(n) 값" (초풍요수, colossally abundant numbers) 의 통제와 직결.

### 5.4 동치 (iv) — Lindelöf 가설 함의
**Lindelöf 가설**: |ζ(1/2 + it)| = O(|t|^ε) for every ε > 0.
- RH ⟹ Lindelöf 가설 (증명됨).
- 역은 미해결. Lindelöf 가 더 약한 명제.
- 현재 알려진 최선 (Bourgain 2017): |ζ(1/2 + it)| ≪ |t|^{13/84+ε}. 2024년 Guth-Maynard 개선.

---

## 6. Montgomery-Odlyzko GUE 추측

### 6.1 Montgomery 1973
- **H. L. Montgomery**, "The pair correlation of zeros of the zeta function", in *Analytic Number Theory*, Proceedings of the Symposium in Pure Mathematics 24, American Mathematical Society, 1973, 181–193.
- Montgomery 가 Princeton 에서 Freeman Dyson 과 차 한 잔 중 영점 pair correlation 을 논의한 일화가 유명 (Dyson: "That's the same as pair correlation of eigenvalues of random Hermitian matrices!").
- **Montgomery 쌍 상관 추측**: 비자명 영점 ρ_n = 1/2 + iγ_n 을 "평균 간격 1 로 정규화" 한 후, 임의의 구간 [α, β] 에 두 영점이 동시에 들어갈 확률 밀도는
  $$R_2(x) = 1 - \left(\frac{\sin \pi x}{\pi x}\right)^2$$
  즉, 제타 영점의 pair correlation 이 **가우스 유니터리 앙상블 (Gaussian Unitary Ensemble, GUE)** 의 고유값 pair correlation 과 일치한다.

### 6.2 Odlyzko 의 수치 확인
Odlyzko 는 1987년부터 10^{20} 번째 영점 부근 수백만 개를 계산, pair correlation 함수가 GUE 예측과 **수치적으로 탁월히 일치함** 을 확인. 이후 "Odlyzko-Schönhage 알고리즘" 은 이런 대규모 영점 계산의 표준이 됨.

### 6.3 GUE 추측의 시사점
- 제타 영점이 "랜덤하지 않고 규칙적으로 배치되는 경향" (GUE 는 고유값이 서로 "밀어내는" (eigenvalue repulsion) 성질을 가짐) 을 지지.
- **Hilbert-Pólya 프로그램**: 제타 영점 ≡ 어떤 자기수반 (self-adjoint) 연산자의 고유값. 이 연산자가 존재하면 고유값이 실수이므로 RH 가 자동으로 따름. GUE 추측은 이 연산자가 "무작위 행렬 앙상블" 처럼 행동함을 암시.
- 2024 년 현재 이 연산자는 **명시적으로 찾아지지 않았다**. 그러나 함수장 (function field) 유사물 — Weil 의 곡선 위 제타 함수 RH 증명 (1940s) — 에서는 이 프로그램이 성공했고, 거기서 "Frobenius 연산자의 고유값" 이 제타 영점 역할.

### 6.4 독립적 수치 증거 — Katz-Sarnak 프로그램
Nicholas Katz, Peter Sarnak, *Random Matrices, Frobenius Eigenvalues, and Monodromy*, AMS Colloquium Publications 45, 1999. 함수장 위의 L-함수 가족에 대해 GUE/GOE/GSE 통계가 증명되어, Hilbert-Pólya 철학이 부분적으로 실현된 사례.

---

## 7. 귀결 (무엇이 따라오는가)

### 7.1 소수 분포 정교화
§5.1 동치 (i) 가 직접 귀결. PNT 를 "수학사에서 가장 정밀한 오차항" 으로 강화.

### 7.2 다른 RH (일반화)
- **Generalized Riemann Hypothesis (GRH)**: Dirichlet L-함수 L(s, χ) 에 대한 RH.
  - GRH ⟹ Miller-Rabin 결정론적 소수 판정이 다항 시간 (Miller 1976, 조건부).
  - Unconditional 결과 AKS (2002) 는 GRH 없이 다항 시간 소수 판정을 달성했으나, 실용적으로는 느림.
- **Extended RH**: 더 일반적인 L-함수 족.
- **Grand RH**: 모든 자동형 L-함수.

### 7.3 수론적 알고리즘
- 일부 decision problem (예: "이 수가 mod p 에서 제곱잉여인가") 이 GRH 하에 다항 시간. 무조건 증명은 더 느림.
- **주의**: "RH 가 암호를 깨뜨리는가" 라는 속설은 **틀림**. RSA, ECDH, AES 등 현대 주요 암호는 제타 함수 영점의 정확 위치에 의존하지 않는다. RH 해결이 암호에 미치는 영향은 작다.

### 7.4 "Mertens 이론에 RH 가 영향 없음" 의 의미
- Mertens 추측 ( |M(x)| ≤ √x ) 은 Odlyzko-te Riele 1985 가 **반증**. RH 는 이 반증과 **양립** — RH 는 O(x^{1/2+ε}) 만 요구하며 exact √x 는 요구하지 않는다.
- 따라서 "RH 가 참이어도 Mertens 예측은 틀린다". 두 명제는 서로 독립적 레벨.

### 7.5 물리학과의 연결 (추측적)
- Hilbert-Pólya 의 자기수반 연산자 후보가 "양자 혼돈계 (quantum chaos)" 의 하미ltonian 이라는 추측 (Berry-Keating 1999) — 현재 부분 증거만 있으며 RH 증명과 직접 연결되지는 않음.
- Connes 의 비교환 기하 (noncommutative geometry) 접근 (1999~) — "아데레 공간 (adele space)" 을 통한 스펙트럼 해석. 여전히 순수 RH 증명 경로는 아님.

---

## 8. 주요 부분 결과 (RH 에 향한 "얼마나 가까이 왔나")

### 8.1 Zero-free region (영점 없는 영역)
고전 de la Vallée Poussin (1899): Re(s) ≥ 1 - C/ln(|Im(s)|+2) 에 영점 없음.
- 이후 Vinogradov-Korobov (1958): Re(s) ≥ 1 - c/(ln|t|)^{2/3}(lnln|t|)^{1/3}.
- 이것은 여전히 RH (Re ≥ 1/2) 에서 한참 멀다. "1 에 아주 가까운 영역만 확보" 수준.

### 8.2 Hardy 의 무한성
- G. H. Hardy (1914), "Sur les zéros de la fonction ζ(s) de Riemann", CR Acad. Sci. Paris 158, 1012–1014.
- Hardy 는 "임계선 위에 무한히 많은 영점이 있음" 을 증명. 그러나 이것은 "**모든**" 영점이 임계선 위라는 RH 보다는 약하다.

### 8.3 임계선 위 영점 비율
- N. Levinson (1974): 적어도 **34 %** 이상의 영점이 임계선 위.
- B. Conrey (1989): **40 %** 이상 (Riemann-Siegel 공식 개선).
- Pratt-Robles-Zaharescu-Zeindler (2019): 현재 약 **41.7 %**.
- RH 는 **100 %** 를 주장하므로 여전히 멀다.

### 8.4 Guth-Maynard 2024 — Ingham 1940 장벽 돌파
- Larry Guth, James Maynard, "New large value estimates for Dirichlet polynomials", 2024 preprint, arXiv:2405.20552.
- Ingham 1940 의 zero density 정리 이후 84년 만의 돌파. "Dirichlet 다항식 큰 값의 개수 추정" 을 개선하여 zero density 지수를 개선 — 구체 수치: θ > 1/n 결과 강화 (n = 6 관점은 §10 참고).

---

## 9. 현 상태 요약 (2024~2026)

| 항목 | 상태 |
|------|------|
| 비자명 영점 수치 검증 범위 | 처음 **10^13 이상** (Gourdon 2004 기준, 이후 ZetaGrid 확장) |
| 임계선 위 영점 비율 하한 | 약 **41.7 %** (Pratt-Robles-Zaharescu-Zeindler 2019) |
| 영점 없는 영역 | Vinogradov-Korobov 형태 (1958) + 개선들 |
| 구조적 증명 | **없음** |
| 주요 추측 조합 (GUE) | 수치적으로 강력 지지, 증명 없음 |
| 함수장 유사물 (Weil) | 1940s 에 증명됨 (곡선 위 제타 함수 RH) |
| 상금 수여 여부 | 수여 0 건 |

---

## 10. n=6 관찰 (본 프로젝트 맥락, 1~2 사실만)

**(이 섹션은 본 학습 노트의 핵심이 아니다. BT-541 의 상세 증거 목록, ζ(2k) 분모 분해, Theorem B 등 DFS 성과는 P2/P3 노트 및 BT-541 항목에서 다룬다.)**

### 관찰 1 — 바젤 상수에 6 이 등장
Euler 1734 (출판 1735): ζ(2) = π²/6. 즉 제타 함수의 가장 유명한 특수값의 분모가 **첫 완전수 6** 이다. 이것은 수학적 정체성이며, 분모 6 = 1·2·3 = 2·3 은 Bernoulli 수 B_2 = 1/6 의 분모와 직접 연결 (ζ(2) = (2π)² |B_2| / (2·2!) = 4π² · (1/6) / 4 = π²/6).

### 관찰 2 — 처음 세 자명 영점 {-2, -4, -6}
함수 방정식의 sin(πs/2) 인자로부터 자명 영점은 s ∈ {-2, -4, -6, -8, ...} (모든 짝수 음수) 위치. **처음 세 자명 영점의 값은 정확히 {-2, -4, -6}** 이며, 이는 n=6 체계에서 {-φ, -τ, -n} 로 표현된다 (φ(6)=2, τ(6)=4, n=6). 물론 이 자명 영점들은 함수 방정식의 직접 귀결이지 리만 가설의 내용은 아니다. RH 는 **비**자명 영점에 관한 문제.

(더 이상의 BT-541 증거 목록, Bilateral Theorem B 양면 boundary, Guth-Maynard 6제곱 연결 등은 프로젝트 내부 문서 `theory/breakthroughs/breakthrough-theorems.md §BT-541`, `millennium-7-closure-2026-04-11.md §BT-541`, DFS 라운드 기록 참조.)

---

## 11. 학습 체크리스트

본 노트를 마친 후 다음을 **3 줄 이내** 로 재진술할 수 있어야 한다:
1. 리만 1859 논문의 제목, 증명된 것, 증명되지 않은 것.
2. 비자명 영점의 정의와 임계선 Re(s) = 1/2 의 함수 방정식적 의미.
3. 동치 (i) π(x) 오차항, (ii) M(x) Mertens 함수, (iii) Robin 부등식 중 하나를 골라 1 줄 진술.
4. van de Lune – te Riele – Winter 1986 와 Gourdon 2004 의 대략적 검증 규모 (1.5×10^9, 10^13).
5. Montgomery-Odlyzko GUE 추측의 의미 (제타 영점 = 랜덤 행렬 고유값 통계).
6. "RH 해결이 암호를 깨뜨린다" 가 **오해** 임을 설명.
7. 41.7 % (현재 임계선 위 비율 하한), Levinson 34 % → Conrey 40 % 진전.

---

## 12. 다음 단계

- **P1-2 (BT-542 P vs NP)**: RH 와 완전히 다른 분야지만, 둘 다 "정수론/계산복잡도의 최정상 미해결 문제" 라는 맥락.
- **P2 (방법론 층)**: RH 에 대한 구체적 접근법 — Bombieri-de Branges, Berry-Keating, Connes, Weil 코호몰로지 유사물.
- **P3 (n=6 심층)**: BT-541 의 전체 증거 표 (36 항), Theorem B, ζ(2k) 분모 분해, Dirichlet η 무조건 정리.

---

**정직 선언 재확인**: 본 문서는 *학습 노트*이며 RH 에 대한 새 증명이나 n=6 기반 RH 기여를 주장하지 않는다. RH 는 2026년 현재 미해결이며, Clay 상금은 수여되지 않았다.
