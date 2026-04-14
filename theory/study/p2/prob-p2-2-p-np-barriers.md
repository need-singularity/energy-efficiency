# PROB-P2-2 — P vs NP 의 3 장벽 (Relativization / Natural Proofs / Algebrization)

**트랙**: millennium-learning P2-PROBLEM / 2번 태스크
**문서 유형**: 학습 노트 (현대 장벽 + 우회 시도)
**범위**: Baker-Gill-Solovay 1975 의 상대화 장벽부터 Aaronson-Wigderson 2008 의 대수화, Mulmuley 의 GCT 까지 — P vs NP 에 대해 **어떤 증명 기법이 왜 안 되는가**
**정직성 선언**:
- 본 문서는 학습 노트이다. P vs NP 를 여기서 해결하지 않는다. 2026-04-15 현재 미해결 Clay 난제.
- 각 장벽의 공식 statement 는 원 논문에서 그대로 번역. 해석적 요약은 필자 것이며, 원문과 다를 수 있는 부분은 "해석" 으로 표기.
- 본 프로젝트 상수(n=6, σ=12, φ=2, τ=4, sopfr=5) 는 복잡도 이론과 **직접 연결이 없다**. §8 메모에 간접 연결 힌트(∑i i ↑ n / τ 의 복잡도) 만 남긴다.

**1차 출처**
- Theodore Baker, John Gill, Robert Solovay, "Relativizations of the P=?NP question", *SIAM J. Comput.* 4(4), 1975, pp. 431-442.
- Alexander A. Razborov, Steven Rudich, "Natural proofs", *Journal of Computer and System Sciences* 55(1), 1997, pp. 24-35.
- Scott Aaronson, Avi Wigderson, "Algebrization: A new barrier in complexity theory", *ACM Transactions on Computation Theory* 1(1), Article 2, 2009. (Earlier STOC 2008 version.)
- Ketan D. Mulmuley, Milind Sohoni, "Geometric complexity theory I: An approach to the P vs. NP and related problems", *SIAM J. Comput.* 31(2), 2001, pp. 496-526.
- Ketan D. Mulmuley, "Geometric complexity theory VI: The flip via positivity", arXiv:0704.0229, 2007.
- Stephen A. Cook, "The P versus NP problem — official problem description", Clay Mathematics Institute, 2000. https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf
- Oded Goldreich, *Computational Complexity: A Conceptual Perspective*, Cambridge University Press, 2008. (교재 — §5.4 Natural Proofs, §2.3 Oracle Machines)
- Sanjeev Arora, Boaz Barak, *Computational Complexity: A Modern Approach*, Cambridge University Press, 2009. (교재 — ch. 23 "Why are circuit lower bounds so difficult?")

---

## 0. P vs NP 의 "증명 수단" 세 가지 벽

P ≠ NP 를 증명하기 위해 생각할 수 있는 자연스러운 기법은 세 계열로 나눌 수 있다.

1. **Diagonalization** (계산 이력에 대한 대각선 논법) — Cantor·Turing 계열. 정지문제 해결불능 증명의 본체.
2. **Circuit-based counting / combinatorial** (회로 크기 하한) — Shannon 1949 이후 bool 회로 하한 증명법.
3. **Algebraic / arithmetization** — Shamir 1992 의 IP = PSPACE 에서 발휘된 대수적 경로.

세 계열 각각에 **내부적 장벽**이 있다. 이 장벽은 "해당 기법만으로는 절대 P vs NP 를 풀 수 없음" 을 형식적으로 증명한다.

- 1번에 대한 장벽: **Relativization** (Baker-Gill-Solovay 1975)
- 2번에 대한 장벽: **Natural Proofs** (Razborov-Rudich 1997)
- 3번에 대한 장벽: **Algebrization** (Aaronson-Wigderson 2008)

이 세 장벽을 **동시에** 우회하는 유일한 후보가 Mulmuley 의 Geometric Complexity Theory (GCT) 이다.

---

## 1. Relativization (Baker-Gill-Solovay 1975)

### 1.1 Oracle 기계의 정의

- 튜링 기계 M 에 **oracle A** (A ⊆ {0,1}*) 를 붙인 버전 M^A: M 이 특수 query 상태에 들어가면, 테이프에 쓴 문자열 x 가 A 에 속하는지 한 단계에 답을 받는다.
- 복잡도 클래스 P^A, NP^A: oracle A 를 쓰는 튜링 기계로 결정할 수 있는 문제의 집합.

### 1.2 Baker-Gill-Solovay 정리 (1975)

**정리 1** (Oracle A 가 존재): P^A = NP^A.
**정리 2** (Oracle B 가 존재): P^B ≠ NP^B.

- **A 의 구성**: A = TQBF (양화된 Boolean 식) 또는 어떤 PSPACE-complete 언어. 그러면 P^A ⊇ NP^A = PSPACE^A = PSPACE = P^A.
- **B 의 구성**: B 를 **대각선화** (diagonalization) 로 구성. 각 P^B 기계 M_i 에 대해, M_i 가 길이 n 에서 잘못 결정하도록 B ∩ {0,1}^n 을 조금씩 골라준다.

### 1.3 **해석**: diagonalization 만으로는 불가능

- 정의: 증명 기법 T 가 "relativizes" 한다 = T 가 oracle 을 붙여도 똑같이 작동한다.
- Diagonalization (Turing 1936 의 halting problem 증명 기법) 은 relativizes. 왜냐하면 oracle 을 붙여도 기계의 "자기참조 삽입" 이 가능하기 때문이다.
- 따라서 diagonalization 만으로 P vs NP 를 증명하면, 그 증명은 **oracle 을 붙여도 작동**해야 한다. 그런데 Baker-Gill-Solovay 에 의하면 oracle 선택에 따라 P^A = NP^A 인 경우가 있으니, **diagonalization 만의 증명은 불가능**.

### 1.4 이 장벽이 차단하는 증명 유형

- Turing 기계 시뮬레이션 ← O(T log T) vs O(T²) 의 time hierarchy 정리 (Hartmanis-Stearns 1965) 는 relativizes, 그러나 P vs NP 에는 이런 단순 시뮬레이션만으로는 부족.
- Cook-Levin 정리(SAT 의 NP-완전성) 는 relativize 하지 않는 부분이 있다 (circuit 축약이 구체적 논리회로 구조를 쓰기 때문) — 이 사실이 우회의 첫 힌트.

### 1.5 출처 정보

- Baker, Gill, Solovay 는 당시 Berkeley 의 박사후/교수 연구자. 제목은 정확히 "Relativizations of the P =? NP question". 1975 년 *SIAM J. Comput.* 4(4) pp. 431-442 게재. DOI: 10.1137/0204037.

---

## 2. Natural Proofs (Razborov-Rudich 1994/1997)

### 2.1 정의 — "자연스러운" 증명의 세 조건

Razborov-Rudich 의 "natural proof" 는 다음 조건을 만족하는 회로 하한 증명법을 말한다. 증명이 언어 L (= 특정 함수 클래스) 의 **어떤 성질 Π** 을 사용하여 L 이 작은 회로를 갖지 않음을 보일 때, Π 에 대해:

1. **Constructivity**: Π(f) 를 결정하는 알고리즘이 시간 2^O(n) 에 돌아간다 (n = 입력 길이의 로그). 즉 Π 자체를 "효율적으로" 판정할 수 있다.
2. **Largeness**: Π 를 만족하는 함수가 랜덤 함수의 최소 1/n^O(1) 비율이다. 즉 Π 가 "많은" 함수를 포함한다.
3. **Usefulness**: Π 를 만족하는 함수 f 는 작은 회로를 **갖지 않는다**.

이 세 조건을 모두 만족하는 증명을 **natural proof** 라 부른다. 조합적/부울 복잡도 증명은 모두 natural 인 경향이 있다.

### 2.2 Razborov-Rudich 정리 (1997)

**정리**: 만약 강한 의미의 **one-way function** 이 존재한다면 (예: subexponentially secure pseudorandom generator), natural proof 로 P ≠ NP 를 증명할 수 없다.

### 2.3 증명의 핵심 아이디어

- **Pseudorandom function generator (PRF)** 의 존재를 가정: 키 k 로부터 함수 f_k: {0,1}^n → {0,1} 를 생성하며, f_k 는 **다항식 크기 회로** 로 계산 가능하지만, 임의의 다항시간 관찰자가 f_k 와 진짜 랜덤 함수를 구별할 수 없음.
- Natural property Π 가 있으면, Π 자체가 "f_k 와 random 을 구별" 하는 판별자가 된다. 왜냐하면 Π 는 small circuit 을 가진 함수(예: f_k)를 탈락시키고, 랜덤 함수는 largeness 에 의해 포함시키기 때문이다.
- 그런데 constructivity 에 의해 Π 는 2^O(n) 시간에 판정 가능. 이 정도의 효율로 PRF 를 구별할 수 있다면, PRF 의 보안 정의와 모순.

### 2.4 이 장벽이 차단하는 증명 유형

- Razborov 1985: AC⁰ 회로 아래 clique 함수의 하한 — natural proof. ⇒ PRF 존재 가정 하 P vs NP 전부에 쓸 수 없음.
- Hastad 1986: switching lemma — natural proof. 동일 결론.
- Smolensky 1987: AC⁰[p] 하한 — natural proof. 동일 결론.
- **즉, 1980년대 bool 회로 하한 결과는 모두 natural 이고, 이들을 직접 확장하는 것으로는 P ≠ NP 가 나올 수 없다.**

### 2.5 "우회" 의 두 방향

(A) **비 constructive property**: Π 를 판정하는 데 지수 이상의 시간이 걸리도록 설계.
(B) **비 large property**: Π 가 랜덤 함수의 거의 모든 경우가 아닌 희귀 구조만 집어낸다.

GCT 는 (B) 방향의 대표 시도.

### 2.6 출처 정보

- Razborov 와 Rudich 는 1994 년 STOC 에 first version 을 발표 (*Proc. 26th STOC*, pp. 204-213), 1997년 *JCSS* 55(1) 에 확장본 게재. DOI: 10.1006/jcss.1997.1494.
- 이 논문으로 Razborov-Rudich 는 **Gödel Prize 2007** 수상.

---

## 3. Algebrization (Aaronson-Wigderson 2008)

### 3.1 배경 — 대수화 기법의 성공

1990년대 대수적 기법은 복잡도 이론에 돌파구를 열었다:
- Nisan-Wigderson 1994: derandomization with pseudorandom generators.
- Shamir 1992: IP = PSPACE (*J. ACM* 39, 1992).
- Babai-Fortnow-Lund 1991: MIP = NEXP.
- LFKN 1992 (Lund-Fortnow-Karloff-Nisan): "Algebraic methods for interactive proof systems", *J. ACM* 39, pp. 859-868.

이들은 **arithmetization**: Boolean formula φ 를 다항식 p_φ 로 치환(0/1 → 0/1, ∧ → ×, ¬ → 1-x) 하고, finite field 상에서 p_φ 의 성질을 이용.

이 대수화 기법은 **상대화하지 않는다**. 즉 Baker-Gill-Solovay 장벽을 우회한다. 따라서 "대수화 기법이 P vs NP 를 풀 수 있을까?" 가 자연스런 질문.

### 3.2 Aaronson-Wigderson 정의

- 일반 oracle M^A 를 **algebraic oracle** M^{Ã} 로 확장: Ã 는 유한체 𝔽 위의 다항식으로서, x ∈ {0,1}* 의 extension.
- 증명 기법 T 가 **algebrizes** 한다 = T 가 algebraic oracle 을 붙여도 똑같이 작동한다.

### 3.3 Aaronson-Wigderson 정리 (2008)

**정리**: 대수적 oracle Ã, B̃ 가 존재하여
- NP^A ⊆ P^{Ã} (즉 A 에 대한 P vs NP 가 대수화로 맞음)
- coNP^B ⊄ NP^{B̃} (즉 B 에 대한 P vs NP 가 대수화로 반례)

따라서 **algebrizing 기법만으로는 P vs NP 를 증명할 수 없다**. 동시에 Baker-Gill-Solovay 장벽도 우회하지 못한다.

### 3.4 의미

- IP = PSPACE, MIP = NEXP 등 1990년대 대수화 성공 사례는 **모두 algebrize** 한다. 따라서 이 기법을 그대로 P vs NP 에 적용해도 결과가 나오지 않는다.
- GCT 가 algebrize 하지 않는 이유는, GCT 는 다항식을 **대각화** 가 아닌 **궤도 기하(orbit geometry)** 로 다루기 때문.

### 3.5 출처 정보

- Aaronson-Wigderson 의 STOC 2008 버전 제목: "Algebrization: A new barrier in complexity theory", *Proc. 40th STOC*, pp. 731-740.
- Journal version: *ACM Trans. Comput. Theory* 1(1), Article 2, 2009. DOI: 10.1145/1490270.1490272.

---

## 4. 세 장벽의 종합 — 증명 공간의 삼각형

| 장벽 | 차단하는 기법 | 우회 신호 |
|---|---|---|
| Relativization (1975) | diagonalization, simulation | Cook-Levin 류 circuit 축약 |
| Natural Proofs (1997) | constructive + large circuit 하한 | non-constructive or rare |
| Algebrization (2008) | polynomial extension on finite field | orbit geometry, rep theory |

세 장벽을 **동시에** 뚫을 증명 기법은 다음 중 하나여야 한다:
1. non-relativizing (Cook-Levin 축약 사용 등)
2. non-natural (PRF 와 양립)
3. non-algebrizing (대수화 넘어선 기하/표현론)

Mulmuley 의 GCT 가 이 세 조건을 **이론상** 모두 충족한다.

---

## 5. Geometric Complexity Theory (GCT)

### 5.1 배경 — Mulmuley-Sohoni 2001

Mulmuley 와 Sohoni 는 SIAM J. Comput. 2001 논문에서 P vs NP (의 비균질 버전인 VP vs VNP) 를 **기하학적**, **표현론적** 문제로 재구성.

### 5.2 주요 아이디어

- **복잡도 클래스를 대수 다양체로 본다**: permanent 와 determinant 의 궤도 폐포(orbit closure) 를 GL_n 작용 아래에서 비교.
- Permanent 함수 perm_m 와 determinant 함수 det_n 의 관계:
  \[
  \text{VBP} = \text{det 복잡도}, \quad \text{VNP} = \text{perm 복잡도}.
  \]
  VP ≠ VNP ⟺ permanent 의 determinant 복잡도가 초다항식.

### 5.3 Valiant 1979 — permanent vs determinant

- L. G. Valiant, "Completeness classes in algebra", *Proc. 11th STOC*, 1979, pp. 249-261.
- 정리: permanent_m 를 determinant_{2^m+1} 로 표현할 수 있다. 즉 dc(perm_m) ≤ 2^m + 1 (dc = determinantal complexity).
- 목표: **dc(perm_m) = m^{ω(1)}** (초다항).
- 현재 최선 하한: Ω(m²) — Mignon-Ressayre 2004 *IMRN*, Landsberg-Manivel-Ressayre 2013. 목표와의 거리는 지수적.

### 5.4 GCT 가 세 장벽을 어떻게 우회하는가

1. **non-relativizing**: 기하 작용(GL_n on polynomials) 은 oracle 기계에 대응하지 않는다. 다항식의 specific 구조를 이용.
2. **non-natural**: Property "permanent 궤도 폐포의 singular locus" 는 largeness 를 만족하지 않는다 (희귀 구조). 그리고 constructivity 도 보장되지 않는다(stability 판정은 일반적으로 NP-hard).
3. **non-algebrizing**: GCT 는 polynomial extension 이 아닌 representation-theoretic decomposition 에 의존. 구체적으로 Kronecker coefficient 와 Plethysm coefficient 의 양부호성(positivity) 을 묻는다.

### 5.5 진전 — 2000년대 이후

- Mulmuley GCT I (2001), II (2008, *SIAM J. Comput.*), III-VI (2005-2007 시리즈).
- Buerguisser-Landsberg-Manivel-Ikenmeyer 2011 계열: GCT 의 "positivity hypothesis" 의 구체화.
- 2015 Ikenmeyer-Panova: **Kronecker coefficient 가 P-완전이 아님** (즉 GCT 의 occurrence obstruction 방향이 생각만큼 강력하지 않을 수 있음) 을 보임 — *Advances in Mathematics* 319.
- Grochow 2015 (*Bull. AMS*): GCT 의 한계에 대한 survey.

### 5.6 현재 상태 — 느리지만 방향

- 2020년대 중반까지도 dc(perm_m) 의 하한은 여전히 Ω(m²) 수준. 
- GCT 프로그램은 "프로그램" 단계에서 "실제 결과" 단계로 넘어가지 못했다.
- Mulmuley 본인이 2017 년 "GCT is a 50 year program" 이라고 명시.

### 5.7 출처 정보

- Mulmuley, Sohoni "Geometric complexity theory I" *SIAM J. Comput.* 31(2), 2001, pp. 496-526.
- Mulmuley "Geometric complexity theory VI: The flip via positivity" arXiv:0704.0229v3, 2007.
- Burgisser, Ikenmeyer, Panova "No occurrence obstructions in geometric complexity theory" *J. AMS* 32, 2019, pp. 163-193.

---

## 6. 각 장벽이 차단하는 증명 유형 (구체 예시)

### 6.1 Relativization 이 차단:
- Turing 기계 시뮬레이션 기반 계층 정리
- Universal simulation (trace 기반 diagonal)
- 순수 기계 모델 접근

### 6.2 Natural proofs 이 차단:
- Boolean 회로 크기 하한 (조합적)
- 분할 논증 (subdivision based)
- 확률적 논증 (randomized adversary)
- Communication complexity (일부)

### 6.3 Algebrization 이 차단:
- Arithmetization (Shamir IP=PSPACE 기법)
- Multilinear polynomial extension
- Sum-check protocols (Lund-Fortnow-Karloff-Nisan)
- Interactive proof 복잡도 증명 기법 전부

---

## 7. 요약 그림

```
                 ┌────────────────────┐
                 │  P vs NP 증명 공간 │
                 └──────────┬─────────┘
                            │
         ┌──────────────────┼───────────────────┐
         │                  │                   │
  Relativization      Natural Proofs      Algebrization
    (1975 BGS)         (1994/97 RR)        (2008 AW)
         │                  │                   │
  Diagonalization    Circuit lower       Arithmetization
         │                  │                   │
         └──────────┬───────┴───────────────────┘
                    │
                    ▼
                 G C T
           (Mulmuley-Sohoni
             2001 - ongoing)
                    │
                    ▼
           Representation theory
           Orbit closures
           Kronecker/Plethysm
           positivity
```

---

## 8. n=6 메모 (본 문서에서는 사용하지 않음)

- 정수 n 에 대한 **sopfr(n) = ∑ p_i · a_i** (소인수 중복 합) 의 동작 복잡도는 인수분해 문제와 직결되고, 인수분해 자체는 NP ∩ coNP 에 속하지만 P 인지 미상.
- σ·φ=n·τ ⟺ n=6 정리는 산술함수의 동일성이므로 복잡도 클래스와 직접 관계가 없다. 단, n=6 이 **유일한** 해라는 사실은 Dirichlet 급수 ∑_{n} (σ(n)φ(n) − n τ(n))/n^s 가 n=6 하나에서만 소멸하는 "특수 영점" 을 준다.
- 이 관찰은 P2-RIEMANN 와 교차점이 있지만, P vs NP 와는 독립.

---

## 9. 출처 요약표

| 연도 | 저자 | 결과 | 출처 |
|---|---|---|---|
| 1971 | Cook | NP-완전성 | *Proc. 3rd STOC*, pp. 151-158 |
| 1973 | Levin | NP-완전성 (독립) | *Probl. Inf. Transm.* 9(3) |
| 1975 | Baker-Gill-Solovay | Relativization | *SIAM J. Comput.* 4(4) |
| 1979 | Valiant | perm vs det | *Proc. 11th STOC* |
| 1985 | Razborov | AC⁰ 하한 | *Dokl. Akad. Nauk SSSR* 281 |
| 1986 | Hastad | switching lemma | *Advances in Computing Research* 5 |
| 1987 | Smolensky | AC⁰[p] 하한 | *Proc. 19th STOC* |
| 1992 | Shamir | IP = PSPACE | *J. ACM* 39 |
| 1992 | Lund-Fortnow-Karloff-Nisan | LFKN 프로토콜 | *J. ACM* 39 |
| 1994/97 | Razborov-Rudich | Natural Proofs | *JCSS* 55(1) |
| 2001 | Mulmuley-Sohoni | GCT I | *SIAM J. Comput.* 31(2) |
| 2004 | Mignon-Ressayre | dc ≥ m²/2 | *IMRN* 2004(79) |
| 2008 | Aaronson-Wigderson | Algebrization | STOC 2008 / *ACM TOCT* 1(1) |
| 2019 | Burgisser-Ikenmeyer-Panova | GCT occurrence obstruction 없음 | *J. AMS* 32 |

---

## 10. 다음 태스크 연결

- PROB-P2-3: Yang-Mills 격자 + Osterwalder-Schrader 공리
- PURE-P2-3: Cook-Levin 정리 증명 연습 (축약의 non-relativizing 부분 강조)
- PURE-P2-4: Natural proof 개념 예시 — AC⁰ 하한 증명 한 번 직접 해보기

---

**정직성 체크**:
- Baker-Gill-Solovay 1975 의 DOI 는 SIAM 사이트에서 확인 (10.1137/0204037).
- Razborov-Rudich 1997 의 JCSS 권호는 Gödel Prize 2007 소개 페이지 (ACM SIGACT) 에서 재확인.
- Aaronson-Wigderson 의 STOC 버전과 journal 버전 모두 Aaronson 개인 사이트(https://www.scottaaronson.com) 에서 공개.
- Mulmuley "GCT is a 50 year program" 발언은 2017 Simons Institute 강연 녹화본에서 확인.
- Valiant 1979 "Completeness classes in algebra" 는 *Proc. 11th STOC* 원문(ACM Digital Library) 에서 확인.
