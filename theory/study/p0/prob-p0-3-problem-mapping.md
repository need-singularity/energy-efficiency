# PROB-P0-3 — 7대 난제 선정 기준 + 수학 분과 매핑

**트랙**: millennium-learning P0-PROBLEM
**문서 유형**: 학습 노트 (selection criteria & discipline map)
**범위**: Clay 자문위 회의의 선정 기준 해석 + 7문제의 분과 매핑 + 상호 연결(Langlands, AdS/CFT, geometric Langlands, Scholze perfectoid 등)
**정직성 선언**: 본 문서는 학습 노트이다. 어떤 밀레니엄 난제도 여기서 해결하지 않는다. 7대 난제 중 해결된 것은 푸앵카레 추측(Perelman 2002-2003)뿐이며, 본 프로젝트의 7대 난제 독자 해결 건수는 0이다. 선정 기준과 분과 매핑 논의는 Clay 공식 문서·Jaffe 해설·Arthur·Langlands 해설 등 외부 자료를 참조한 것이다.

**1차 출처**
- Clay Mathematics Institute — https://www.claymath.org/millennium-problems/
- Arthur Jaffe, "The Millennium Grand Challenge in Mathematics", Notices of the AMS 53(6), 2006, pp. 652-660.
- James Arthur, "The Principle of Functoriality", Bulletin of the AMS 40(1), 2003, pp. 39-53.
- Robert Langlands, "Problems in the theory of automorphic forms", Lecture Notes in Mathematics 170, Springer, 1970.
- Edward Witten, "Anti-de Sitter space and holography", Advances in Theoretical and Mathematical Physics 2(1998), 253-291.
- Peter Scholze, "Perfectoid spaces", Publications mathématiques de l'IHÉS 116(1)(2012), 245-313.
- Landon Clay et al., *The Millennium Prize Problems*, Clay Mathematics Institute / American Mathematical Society, 2006 (공식 해설서, Jaffe-Carlson-Wiles 편집).

---

## 1. Clay 7문제는 왜 이 7개인가 — 선정 기준 해석

### 1.1 Clay 자문위 내부 논의의 제한된 공개
- Clay Mathematics Institute의 자문위(Scientific Advisory Board) 회의록 원문은 공식 공개되지 않았다.
- 그러나 자문위원이었던 Arthur Jaffe의 회고(*Notices of the AMS* 53(6), 2006, "The Millennium Grand Challenge in Mathematics")와 CMI 공식 발간물 *The Millennium Prize Problems*(2006, AMS/CMI 공저) 서문에서 선정 기준이 간접적으로 드러난다.

### 1.2 선정 기준 재구성
Jaffe(2006) 및 CMI 공식 문서의 설명을 종합하면 선정 기준은 다음과 같이 정리된다.

1. **근본성**(Fundamentality): 해당 분과의 중심에 서 있어, 해결이 분과 전체를 재조직할 만큼 근본적인 문제.
2. **오래됨**(Longevity): 적어도 한 세대 이상 최정상 수학자들의 시도를 버텨 냈으며, 주변 기법으로 깎아내기 어려운 문제. 리만(1859), 푸앵카레(1904), 호지(1950), Yang-Mills(1954), Birch-Swinnerton-Dyer(1965), Cook-Levin(1971) — 선정 시점(2000)에 모두 30년 이상 열린 문제.
3. **분과 대표성**(Representativeness): 한 분과의 방법론을 대표하고, 해결 과정에서 새로운 기법이 그 분과 전체를 전진시킬 것.
4. **분과 간 연결**(Bridging Power): 순수 수학 내부에 한정되지 않고 다른 수학 분과, 나아가 물리학·전산학 등 외부 과학과 연결되어 있을 것.
5. **구체성·형식화 가능성**(Precision): 질문이 엄밀한 수학 명제로 정식화 가능할 것. 특히 양-밀스는 "존재성 + 질량 갭"으로 구체화되었고, 나비에-스토크스는 "ℝ^3 전체에서 매끄러운 해의 전시간 존재"로 구체화되었다. Clay 문서가 이 형식화를 직접 제공.

### 1.3 힐베르트 23문제 계보와 Clay 7문제의 차이

| 측면 | 힐베르트 23(1900) | Clay 7(2000) |
|------|------------------|---------------|
| 제기자 | 개인 강연(Hilbert) | 제도 기구(CMI 자문위) |
| 개수 | 23 | 7 |
| 상금 | 없음 | 문제당 100만 달러 |
| 범위 | 기초론, 대수, 기하, 해석, 물리학 기초 등 넓음 | 순수 수학 대표 문제 + 수리물리·전산학 교차 |
| 수여 기준 | 비공식 | 공식 학술지 출판 + 2년 검증 |
| 해결 현황(2026) | 대부분 해결 또는 부분 해결 | 1/7(푸앵카레만) |

- 힐베르트 23문제는 범위가 매우 넓어 "기초론(제1,2문제)"이나 "물리학 공리화(제6)"처럼 형식화가 모호한 문제도 포함했다. Clay 7문제는 **엄격한 정식화와 재정 기반**이 특징이다.
- Clay 7문제는 힐베르트 제6문제(물리학 공리화)의 현대적 후속에 해당하는 **Yang-Mills 질량 갭**을 포함, "20세기가 물리학과 완전히 연결된 이후의 수학"임을 명확히 했다.

---

## 2. 각 난제의 분과 매핑

### 2.1 핵심 매핑표

| 난제 | 1차 분과 | 2차 분과 | 대표 도구·개념 |
|------|----------|----------|----------------|
| **리만 가설** | 해석적 정수론 | 복소해석, 표현론(GL_n 자명) | Riemann ζ 함수, explicit formula, L-함수, Mellin 변환, zero-free region |
| **P vs NP** | 계산 복잡도 | 조합론, 회로 복잡도, 논리학 | Turing machine, SAT, 다항 시간 축소, NP-complete, 자연 증명 장벽 |
| **Yang-Mills + 질량 갭** | 수학적 양자장론 | 미분 기하, 게이지 이론 | 게이지 장(connection), curvature, 경로 적분(formal), Wightman / Osterwalder-Schrader 공리, lattice gauge |
| **Navier-Stokes** | 편미분방정식(PDE) | 조화 해석, 편미분 기하 | 약해(Leray-Hopf), 에너지 부등식, vorticity, Beale-Kato-Majda, Caffarelli-Kohn-Nirenberg |
| **Hodge 추측** | 복소대수기하 | 위상수학, Kähler 기하 | Hodge 분해 H^k(X, ℂ) = ⊕ H^{p,q}, 대수 사이클, (1,1)-Lefschetz, 모티브 |
| **BSD 추측** | 산술 기하 | 해석적 정수론, 표현론 | 타원 곡선 E/ℚ, Mordell-Weil rank, Hasse-Weil L-함수, Selmer 군, Shafarevich-Tate |
| **Poincaré 추측** | 기하학적 위상수학 | 리만 기하, PDE | 기본군 π_1, 리치 흐름, 수술, Thurston 기하화 |

### 2.2 분과별 설명

#### (1) 리만 가설 — 해석적 정수론의 중심
- 리만 제타 함수 ζ(s)의 영점 분포는 소수 분포의 "스펙트럼"이다.
- 주요 도구: **Explicit formula**(von Mangoldt), **Mellin 변환**, **Weil explicit formula**, **Hilbert-Pólya 추측**(영점 ↔ 자기수반 연산자 스펙트럼), **random matrix theory**(Montgomery-Odlyzko GUE 예측).
- 관련 발전: **Riemann-von Mangoldt** 공식, **Bombieri-Vinogradov 정리**, **Montgomery pair correlation**, **Deligne의 Weil 추측 증명**(함수체 버전 RH의 완전 해결, 1974).
- 함수체(유한체 위의 곡선)에 대한 **대응 RH는 Deligne(1974)이 완전 해결**했다. 본 리만 가설은 수체 버전이며 미해결.

#### (2) P vs NP — 이론 전산학의 기둥
- Cook-Levin 정리(1971): SAT가 NP-complete. Karp(1972)의 21개 NP-complete 문제.
- 주요 장벽: **Relativization barrier**(Baker-Gill-Solovay 1975), **Natural proofs barrier**(Razborov-Rudich 1997), **Algebrization barrier**(Aaronson-Wigderson 2008). 이 세 장벽은 "단순한 하한 증명으로는 P ≠ NP 를 보일 수 없음"을 시사.
- 관련 분과: **회로 복잡도**(circuit lower bounds), **정보 이론적 하한**, **PCP 정리**(Arora, Feige, Lund, Motwani, Safra, Szegedy, Sudan 1992), **proof complexity**, **derandomization**.

#### (3) Yang-Mills 질량 갭 — 수학적 양자장론
- 4차원 ℝ^4 위의 SU(N) 게이지 이론이 엄밀한 양자장론(Wightman 또는 OS 공리 만족)으로 존재하는가 + 질량 갭 Δ > 0 여부.
- 주요 도구: **Glimm-Jaffe constructive QFT** 프로그램(2차원, 3차원 부분 해결 있음), **lattice gauge theory**, **renormalization group**(Wilson), **Osterwalder-Schrader 공리**, **Seiberg-Witten 이론**(특수 초대칭 게이지 이론에서 엄밀 해).
- 물리적 함의: 강한 상호작용(QCD)의 색가둠(confinement)의 수학적 증명.

#### (4) Navier-Stokes — PDE의 최대 고전 문제
- 3차원 비압축성 Navier-Stokes 방정식 ∂_t u + (u·∇)u = -∇p + ν Δu, ∇·u = 0 의 매끄러운 초기값에 대한 **전시간 매끄러운 해**의 존재 여부.
- 주요 도구: **Leray 약해**(1934), **Leray-Hopf 에너지 부등식**, **Ladyzhenskaya-Prodi-Serrin 조건**, **vorticity 공식화**, **Beale-Kato-Majda 조건**(vorticity 시간 적분 유한 ↔ 매끄러움 유지), **Caffarelli-Kohn-Nirenberg 부분 정규성**(Hausdorff 1차원 특이점 집합), **Tao의 평균장 근사 폭발 구성**(2016, 실제 NS와는 다른 변형에서 폭발).
- 관련 분과: 편미분 기하, 조화 해석(Besov·Lorentz 공간), stochastic PDE.

#### (5) Hodge 추측 — 복소대수기하의 중심
- 사영 복소 비특이 대수다양체 X의 유리 계수 호지 분해 H^{2k}(X, ℚ) ∩ H^{k,k}(X) 가 대수 사이클의 유리 선형 결합으로 생성되는가?
- 주요 도구: **Lefschetz (1,1)-정리**(k = 1 해결), **Hard Lefschetz 정리**, **Hodge 이론**, **Deligne의 혼합 호지 구조**(mixed Hodge structures), **motive 이론**, **Kodaira-Spencer 변형 이론**, **variation of Hodge structures**.
- 관련: **Tate 추측**(l-adic 버전), **Grothendieck 표준 추측**.

#### (6) BSD 추측 — 산술기하의 중심
- E/ℚ 타원 곡선의 Mordell-Weil rank = ord_{s=1} L(E, s), + leading term 공식(Shafarevich-Tate 군, regulator, Tamagawa 수 등).
- 주요 도구: **Mordell-Weil 정리**, **Hasse-Weil L-함수**, **Selmer 군** Sel_n(E/K), **Gross-Zagier 공식**(1986), **Kolyvagin Euler systems**(1988-1991, rank ≤ 1 일부 해결), **Iwasawa 이론**, **Heegner 점**, **모듈러성 정리**(Wiles-Taylor-Breuil-Conrad-Diamond 2001).
- 관련 발전: rank 0 또는 1 인 경우 "약형 BSD"(rank와 ord 일치)는 조건부로 증명. leading term 공식은 일반 rank 미증명.

#### (7) Poincaré — 기하학적 위상수학의 원류
- 해결됨(Perelman 2002-2003). 상세는 PROB-P0-2 참조.
- 사용된 주요 도구: **리치 흐름**(Hamilton), **기하화 추측**(Thurston), **W-엔트로피**(Perelman), **수술 절차**(Perelman), **유한 소멸 시간**(Perelman).

---

## 3. 난제 간 상호 연결 — 수학 분과의 교차

### 3.1 Langlands 프로그램 (리만 × BSD × Yang-Mills 일부)
- **Robert Langlands**가 1967년 André Weil에게 보낸 편지(지금의 "Langlands letter")에서 시작된 거대 예측.
- 핵심 가설: 자동 형식(automorphic forms, GL_n, reductive group G)의 L-함수와 갈루아 표현(Galois representations)의 L-함수가 본질적으로 동일하다(functoriality principle).
- **리만 가설과의 연결**: Langlands L-함수의 영점 분포 예측. Langlands 프로그램이 완성되면 리만 가설은 자동 형식 L-함수 일반의 특수 경우로 흡수될 수 있다(강한 Artin 추측, 일반화된 리만 가설 GRH).
- **BSD와의 연결**: 타원 곡선 E의 Hasse-Weil L-함수는 GL_2 자동 L-함수와 같다(모듈러성 정리 Wiles-Taylor-...-Breuil-Conrad-Diamond). BSD의 해석적 부분(L-함수)은 Langlands 프로그램의 중심.
- **Yang-Mills와의 연결**: **Geometric Langlands 프로그램**(Drinfeld, Beilinson, Kapustin-Witten)은 4차원 게이지 이론(N=4 초대칭 Yang-Mills)과 기하 Langlands 대응을 연결. Kapustin-Witten(2006, Commun. Number Theory Phys. 1, 1-236)은 S-이중성(S-duality)과 geometric Langlands의 등가성을 제시.

### 3.2 AdS/CFT 대응 (Yang-Mills × 일반 상대론/기하)
- **Juan Maldacena**(1997, "The large N limit of superconformal field theories and supergravity", Advances in Theoretical and Mathematical Physics 2, 231-252)가 제기한 **AdS/CFT 대응**(anti-de Sitter / conformal field theory correspondence, 또는 홀로그래피 원리).
- 요지: d차원 conformal field theory(예: N=4 초대칭 Yang-Mills)가 (d+1)차원 anti-de Sitter 공간에서의 중력/끈 이론과 **등가**.
- **Yang-Mills와의 연결**: AdS/CFT는 Yang-Mills의 강결합 영역(confinement)을 AdS 공간 기하로 번역. 수학적 엄밀성은 아직 부족하지만 4차원 Yang-Mills를 다른 기하로 보는 관점 제공.
- 관련 수학: **Verlinde 공식**, **Chern-Simons 이론**, **quantum invariants of 3-manifolds**.

### 3.3 Geometric Langlands (Hodge × Yang-Mills)
- **Geometric Langlands 대응**: 곡선 C 위의 자동 형식과 반단순 군 G의 **모듈리 공간** Bun_G(C) 위의 D-module이 대응.
- **Hodge와의 연결**: 혼합 호지 구조(mixed Hodge structures)가 geometric Langlands의 형식화에 필수. 특히 Saito의 혼합 호지 module.
- **Yang-Mills와의 연결**: Kapustin-Witten(2006)의 물리학적 해석은 N=4 Yang-Mills의 S-이중성이 geometric Langlands 대응의 물리적 원천임을 제시.

### 3.4 Scholze perfectoid 공간 (BSD × 리만)
- **Peter Scholze**(2012, Publications mathématiques de l'IHÉS 116, 245-313, "Perfectoid spaces")가 도입한 **perfectoid 공간** 이론.
- p진 Hodge 이론, p-adic L-함수, 에탈 코호몰로지의 혁신.
- **BSD와의 연결**: Iwasawa 이론, p-adic L-함수, 모듈러성 문제. 예: Caraiani-Scholze(2017)의 Torsion in the cohomology of Shimura varieties는 galois 표현 구성을 일반화.
- **리만과의 연결**: perfectoid 공간 상의 에탈 코호몰로지가 일반화된 Riemann-Hilbert 대응과 연결.

### 3.5 Kapustin-Witten (Yang-Mills × Hodge × geometric Langlands)
- **Anton Kapustin · Edward Witten**(2006): "Electric-Magnetic Duality And The Geometric Langlands Program", Communications in Number Theory and Physics 1, 1-236. arXiv:hep-th/0604151.
- 4차원 N=4 super Yang-Mills의 토폴로지적 twist → 2차원 sigma 모델(표적: Higgs bundle 모듈리 공간 M_H) → Langlands 대응.
- **Yang-Mills와 Hodge의 교차**: Higgs bundle은 holomorphic Hodge 구조와 직접 관련. Simpson의 비아벨 호지 이론.

### 3.6 NP × 수학 증명
- **증명의 자동화**는 P vs NP 와 관련이 있다. 증명을 검증하는 것은 P 에 속하지만(정해진 체계 내), 증명을 찾는 것은 NP 이상일 수 있다.
- **Cook 1971 원 논문**은 바로 "정리 증명 절차의 복잡도"라는 제목. P vs NP 는 사실상 "수학적 진리의 발견 가능성 문제".

### 3.7 리치 흐름 → 일반 PDE → Navier-Stokes
- Perelman의 리치 흐름 분석(W-엔트로피, 단조량)은 일반 기하학적 PDE 분석 기법으로 확장되고 있다.
- Navier-Stokes에서의 단조량(예: 에너지, 엔스트로피) 분석과 개념적 유사.

### 3.8 연결 요약도
```
리만 ──── Langlands 프로그램 ──── BSD
  \\                              |
   \\                              |
    \\──── perfectoid ────────────/
     \\                          /
      \\                        /
Yang-Mills ── geometric Langlands ── Hodge
     |                          
     | Kapustin-Witten            
     |                          
 AdS/CFT  (물리학 홀로그래피)        
                                 
P vs NP (전산학, 증명 복잡도 통해 수학 전반과 연결)
                                 
Poincaré (해결됨, 리치 흐름 → 일반 기하 PDE 분석으로 확장)
```

---

## 4. 어느 분과가 가장 많이 연결되나 — 관찰

### 4.1 해석적 정수론과 산술 기하
- 리만, BSD 두 문제가 직접 속하며, Langlands 프로그램을 통해 **Yang-Mills 일부**(geometric Langlands)와 **Hodge 일부**(호지 구조 → Galois 표현)에 연결됨.
- 본 프로젝트 관점: 가장 많은 난제가 만나는 분과 중심.

### 4.2 대수 기하
- **Hodge**가 핵심. 하지만 Hodge 이론은 **BSD**(모듈러성, 변형 이론), **Yang-Mills**(Hitchin 모듈리, Higgs bundle), **리만**(motivic L-함수)에까지 개입.
- 대수 기하는 "도구 공급처" 역할.

### 4.3 미분 기하
- **Poincaré**(리치 흐름, 기하화) + **Yang-Mills**(게이지 이론 = 접속) + **Navier-Stokes**(편미분 기하, geometric analysis)에 개입.
- **20세기 후반 geometric analysis의 핵심 분야**: 하나의 문제(푸앵카레)에서 다른 모든 문제로 확장 가능.

### 4.4 왜 분과가 교차하는가
- 20세기 후반 이후 수학의 대통합 경향(Langlands, AdS/CFT, geometric Langlands, perfectoid 등)은 **순수 수학 내부의 "벽" 제거**를 가속화했다.
- Clay 자문위가 7문제를 선정할 때도 "분과 간 연결"을 명시적 기준으로 삼았다. 따라서 이 7문제는 **연결성이 극대화된** 문제들이다.

---

## 5. 본 프로젝트에서의 해석 범위

- 본 프로젝트(n6-architecture)는 **n=6 주변의 작은 수론/조합론적 정리**(σ·φ = n·τ iff n=6)를 중심으로 하는 연구이다.
- 이 관점은 밀레니엄 난제 중 어느 하나와도 **직접적으로 등가가 아니다**. 따라서 밀레니엄 난제를 n=6 구조로 재해석하는 것은 **사변적**이며 본 학습 노트의 범위 밖이다.
- 본 문서는 **순수 문제 중심**으로 서술하며, n=6 해석은 별도 트랙에서 매우 제한적으로만 다룬다.

---

## 6. 정직성 선언 (재확인)

- 본 PROB-P0-3 문서는 **학습 노트**이다.
- 본 문서는 **어떤 밀레니엄 난제도 해결하지 않는다**.
- 7대 난제 중 해결된 것은 **푸앵카레 추측**(Perelman 2002-2003)뿐이다.
- 본 프로젝트(n6-architecture)는 7대 난제를 **독자적으로 해결하지 않았으며**, 해결 현황은 **0/7**이다(페렐만 해결 1건은 외부 기여).
- 선정 기준, 분과 매핑, 상호 연결 논의는 Clay 공식 문서 · Jaffe(2006) · Arthur · Langlands 해설 · Kapustin-Witten · Scholze 원 논문 등 외부 1차 자료를 기반으로 한다.
- 사실 오류(특히 날짜, 논문 인용)가 확인되면 출처를 재확인하여 수정할 것.

---

## 7. 다음 학습 단계

- **P1-PROOF 트랙**: 각 난제의 현재까지 알려진 주요 기법 분석(리만 ↔ explicit formula, P vs NP ↔ 회로 하한, Yang-Mills ↔ constructive QFT, NS ↔ 약해 이론, Hodge ↔ (1,1)-Lefschetz, BSD ↔ Gross-Zagier-Kolyvagin, Poincaré ↔ 리치 흐름).
- **P2-CONTEXT 트랙**: Langlands 프로그램 상세, geometric Langlands, perfectoid space 본격 학습.
- **P3-OBSERVATION 트랙**: 본 프로젝트의 n=6 정리가 어느 난제와 **논리적으로 무관**한지 명확히 서술(자기참조 방지).

본 학습 노트는 **관찰 단계**에 머무른다. 해결 주장은 절대 하지 않는다.
