# PROB-P0-1 — Clay 수학연구소 + 7대 난제 역사 개관

**트랙**: millennium-learning P0-PROBLEM
**문서 유형**: 학습 노트 (pure history & context)
**범위**: 힐베르트 23문제(1900) → Clay 7문제(2000) 제도사적 맥락 + 7문제 요약 + 현재 상태표
**정직성 선언**: 본 문서는 학습 노트이다. 어떤 밀레니엄 난제도 여기서 해결하지 않는다. 7대 난제 중 실제로 해결된 것은 푸앵카레 추측(2003, Grigori Perelman)뿐이다. 해결 현황은 0 해결 미 인증 + 1 해결(페렐만) = 1/7.

**1차 출처**
- Clay Mathematics Institute 공식 사이트, "Millennium Problems", https://www.claymath.org/millennium-problems/
- Keith Devlin, *The Millennium Problems: The Seven Greatest Unsolved Mathematical Puzzles of Our Time*, Basic Books, 2002
- Jeremy Gray, *The Hilbert Challenge*, Oxford University Press, 2000 (힐베르트 23문제 전체 역사)
- Arthur Jaffe, "The Millennium Grand Challenge in Mathematics", Notices of the AMS 53(6), 2006, pp. 652-660

---

## 1. 힐베르트 23문제(1900) — 20세기 수학의 지도

### 1.1 선포 배경
- 독일 수학자 **David Hilbert**(1862-1943)가 1900년 8월 8일 파리에서 열린 제2회 국제수학자대회(ICM Paris 1900)의 강연 "Mathematische Probleme"에서 미해결 수학 문제 목록을 발표했다.
- 강연에서는 10개 문제를 직접 소개했고, 인쇄된 강연록(*Göttinger Nachrichten*, 1900; *Archiv der Mathematik und Physik*, 1901)에는 23개 전체가 실렸다.
- 힐베르트의 의도: 20세기 수학의 방향 제시, 국제 수학 공동체의 문제 의식 공유. 강연의 유명한 구호 "우리는 알아야 한다, 우리는 알게 될 것이다"(Wir müssen wissen, wir werden wissen)는 훗날 그의 묘비명이 되었다.

### 1.2 100년간 진전 — 일부 해결 사례
힐베르트 23문제는 분야가 매우 다양하고, 100년에 걸쳐 진전 양상도 제각각이다. 대표적인 해결/부분 해결 사례는 다음과 같다.

- **제1문제(연속체 가설)**: Kurt Gödel(1940, 연속체 가설이 ZFC와 무모순) + Paul Cohen(1963, 연속체 가설의 부정도 ZFC와 무모순, 강제법) = **ZFC에서 독립**. 고전적 의미에서는 "해결"이라기보다 "결정불능 입증".
- **제2문제(산술의 무모순성)**: Gödel 불완전성 정리(1931)에 의해 원래 힐베르트 프로그램의 꿈(엄밀히 유한적 방법으로의 증명)은 깨짐. Gentzen(1936)이 초한 귀납을 허용하면 PA 무모순성 증명 가능함을 보임.
- **제3문제(부피 분해 문제)**: Max Dehn(1900)이 같은 해에 Dehn 불변량을 이용해 **해결**(음의 답). 3차원 다면체는 일반적으로 유한 조각 분해로 합동 변환될 수 없음.
- **제5문제(리 군의 해석적 구조)**: Gleason, Montgomery, Zippin (1952년경) **해결**. 연속군은 자동으로 해석적임(국소 유클리드 위상군은 리 군).
- **제7문제(초월수)**: Gelfond-Schneider(1934) **해결**. a ≠ 0,1 이 대수적이고 b가 무리수 대수적이면 a^b 는 초월수.
- **제10문제(디오판틴 방정식 결정 알고리즘)**: Yuri Matiyasevich(1970) **해결**(음의 답). MRDP 정리(Matiyasevich-Robinson-Davis-Putnam) — 일반 디오판틴 해결 알고리즘은 존재하지 않음.
- **제13문제(7차 방정식 해의 2변수 연속 함수 분해)**: Kolmogorov-Arnold(1957) **해결**(연속 함수 의미에서 긍정적). 원래 질문의 미묘함(연속 vs 해석)에 따라 답이 달라짐.
- **제14문제(불변량 환의 유한 생성)**: Nagata(1958) — 특정 경우 **음의 답** (반례 구성).
- **제17문제(양의 유리함수의 제곱합 표현)**: Artin(1927) **해결**(긍정적).
- **제18문제(공간 채움 문제, Kepler 추측)**: Hales(1998 발표, 공식 형식화 완료 2014) — Kepler 추측 증명. 원래 18문제에는 결정체 군 분류 등 여러 하위 질문이 포함되어 있었고, 이들 중 일부는 Bieberbach(1910)가 해결.
- **제19, 20문제(변분 문제의 해의 해석성, 존재성)**: De Giorgi, Nash(1957~1958) **해결**. 선형 타원형 PDE 정규성 이론.

- **여전히 열려 있는 대표 문제**:
  - **제6문제**(물리학의 공리화) — 범위가 너무 넓어 현재도 진행 중. 양-밀스 질량갭은 사실상 제6문제의 현대 후속 문제로 간주되기도 함.
  - **제8문제**(리만 가설 + Goldbach + Twin prime) — 미해결.
  - **제12문제**(Kronecker Jugendtraum, 대수적 수체 위의 아벨 확장) — 허수 이차수체는 CM 이론으로 해결되었으나 일반 체는 미해결. Langlands 프로그램의 원류.
  - **제16문제**(대수 곡선·벡터장의 위상) — 미해결.

### 1.3 힐베르트 23문제의 유산
- 20세기 수학 전체 분야 지도를 그리는 역할을 했다. 많은 수학자들이 "힐베르트 문제 중 하나를 해결했다"를 경력의 정점으로 삼았다.
- 2000년 Clay의 7문제 선정은 명시적으로 힐베르트 100주년을 겨냥했다.

---

## 2. Clay Mathematics Institute 설립

### 2.1 Landon T. Clay와 CMI
- **Landon T. Clay**(1926-2017)는 미국 보스턴의 뮤추얼 펀드 매니저·사업가. 수학 분야 전공은 아니지만 하버드 재학 시절 수학에 흥미를 가졌고, 장년기 이후 수학 진흥에 사재를 출연했다.
- **Clay Mathematics Institute (CMI)**: 1998년 9월, Landon T. Clay와 그의 아내 Lavinia D. Clay가 미국 매사추세츠주 케임브리지(Cambridge, MA)에 설립한 비영리 민간 재단. 현재는 공식 주소가 미국 뉴햄프셔주 피터버러(Peterborough, NH).
- 설립 목적(공식): "to increase and disseminate mathematical knowledge" — 수학 지식의 증가와 보급. 장학생(Clay Research Fellows) 지원, 공개 강연, 출판 사업 등을 운영.

### 2.2 자문위원회(Scientific Advisory Board)
- CMI 설립 시점의 자문위원회는 당시 세계 정상급 수학자들로 구성되었다.
- **Arthur Jaffe**(하버드, 수리물리학, 초대 CMI 총재 역할), **Andrew Wiles**(프린스턴, 페르마 정리 증명자), **Alain Connes**(IHÉS/콜레주 드 프랑스, 비가환 기하), **Edward Witten**(IAS, 수리물리학/끈 이론), **John Tate**(하버드/텍사스, 대수적 정수론) 등이 공식 자문위원으로 참여했다.
- 2년간(1998~2000)의 논의 끝에 "7대 난제"의 최종 목록이 확정되었다.

### 2.3 선정 기준(Clay 공식 진술)
CMI 공식 발표문과 Jaffe(2006)의 회고에 따르면, 선정 기준은 대략 다음 세 가지다.
1. **오래되고 근본적일 것**: 이미 수십 년 이상 최정상 수학자들의 시도를 버텨 왔으며, 해답이 해당 분과의 중심에 서 있는 문제.
2. **분과 전체를 대표할 것**: 해결이 단발성 결과에 머무르지 않고, 그 분과의 방향을 결정지을 것.
3. **분야 간 연결이 있을 것**: 순수 수학 내부에만 머무르지 않고 다른 과학 분야(물리학, 전산학 등)에도 파급력을 가질 것.

### 2.4 2000년 5월 24일 파리 콜레주 드 프랑스 선포식
- **일시**: 2000년 5월 24일
- **장소**: 파리 콜레주 드 프랑스(Collège de France)
- **형식**: 힐베르트 100주년을 명시적으로 겨냥한 공개 강연. John Tate(리만 가설, BSD), Michael Atiyah(다른 문제들) 등이 각 문제를 해설.
- **상금**: 문제당 100만 달러(US$ 1,000,000), 총 700만 달러(US$ 7,000,000).
- **수여 규정**: 공인된 학술지에 출판된 뒤 2년간 국제 수학계의 검증을 거쳐야 함. 이 규정이 있었기 때문에 페렐만의 2002~2003 arXiv 프리프린트에도 불구하고 2010년에야 상금 수여 결정이 내려졌다(그마저도 페렐만은 거부).

---

## 3. 7문제 각 1문단 요약 + 현재 상태표

### 3.1 요약표

| # | 난제 | 1차 분야 | 제기 연도 | 상금(USD) | 현재 상태 |
|---|------|---------|----------|-----------|---------|
| 1 | 리만 가설(Riemann Hypothesis) | 해석적 정수론 | 1859 | 1,000,000 | OPEN |
| 2 | P vs NP | 계산 복잡도 | 1971 (Cook) | 1,000,000 | OPEN |
| 3 | 양-밀스 존재성과 질량 갭(Yang-Mills Existence & Mass Gap) | 수학적 양자장론 | 1954 (Yang-Mills), 2000 (Clay 정식 질문) | 1,000,000 | OPEN |
| 4 | 나비에-스토크스 존재성·매끄러움(Navier-Stokes Existence & Smoothness) | 편미분방정식 | 1822(NS 도출) / 1934 (Leray 약해) / 2000 (Clay 정식 질문) | 1,000,000 | OPEN |
| 5 | 호지 추측(Hodge Conjecture) | 복소대수기하 | 1950 (ICM Cambridge) | 1,000,000 | OPEN |
| 6 | 버치-스위너턴다이어 추측(Birch–Swinnerton-Dyer) | 산술기하 | 1965 | 1,000,000 | OPEN |
| 7 | 푸앵카레 추측(Poincaré Conjecture) | 기하학적 위상수학 | 1904 | 1,000,000 | **해결**(Perelman 2002-2003, 2010 Clay 상금 제안 → 거부) |

**합계**: 7문제 중 **1개(푸앵카레) 해결, 6개 열림**.

### 3.2 각 문제 1문단 요약

**(1) 리만 가설 (Riemann Hypothesis, 1859)**
- **출처**: Bernhard Riemann, "Über die Anzahl der Primzahlen unter einer gegebenen Grösse"(주어진 크기 이하의 소수의 개수에 관하여), Monatsberichte der Berliner Akademie, November 1859.
- **질문**: 리만 제타 함수 ζ(s) = Σ_{n≥1} n^{-s}(해석적 연속을 통해 s ∈ ℂ로 확장)의 모든 **비자명 영점**(s = -2, -4, -6, ... 이 아닌 영점)은 실수부가 정확히 1/2인 임계선 위에 놓이는가?
- **중요성**: 소수 계수 함수 π(x) 와 로그 적분 Li(x) 의 오차항 O(x^{1/2+ε}) 를 함의. 해석적 정수론 전체의 기둥.
- **현재 상태**: 수치적으로 최초 10^{13}개 이상의 비자명 영점이 임계선 위에 있음이 확인(Odlyzko, Platt 등). 이론적으로는 **미해결**.

**(2) P vs NP (1971)**
- **출처**: Stephen Cook, "The complexity of theorem-proving procedures", Proceedings of the 3rd Annual ACM Symposium on Theory of Computing (STOC 1971); Leonid Levin(1973, 독립 제안, 러시아어); Richard Karp(1972, 21개 NP-완전 문제).
- **질문**: 다항 시간에 해의 **검증**이 가능한 모든 결정 문제는, 다항 시간에 **해결**도 가능한가? 즉 P = NP 인가?
- **중요성**: 현대 암호(공개키), 최적화, AI/ML의 한계, 수학 증명 자동화 등 대부분의 계산 세계가 이 질문의 답에 달려 있다. 대부분 P ≠ NP 를 예상하지만 증명 도구가 부족.
- **현재 상태**: **미해결**. 주요 하한 기법(대각선화, 자연 증명 장벽 Razborov-Rudich 1997, 대수적 장벽 등)이 알려진 단순 접근을 모두 차단.

**(3) 양-밀스 존재성과 질량 갭 (2000 Clay 정식 질문)**
- **출처**: C. N. Yang · R. L. Mills, "Conservation of Isotopic Spin and Isotopic Gauge Invariance", Physical Review 96, 191(1954). Clay 공식 문제 정식화: Arthur Jaffe · Edward Witten, "Quantum Yang-Mills Theory", 2000(Clay 공식 문서).
- **질문**: 4차원 유클리드 공간 ℝ^4 위의 임의의 콤팩트 단순 게이지군 G(예: SU(2), SU(3))에 대한 **양자 양-밀스 이론**이 Wightman 공리 혹은 Osterwalder-Schrader 공리를 만족하는 양자장론으로 **수학적으로 엄밀하게 존재**함을 증명하고, **질량 갭 Δ > 0**(즉 진공 상태 위의 최소 여기 에너지가 0과 분리됨)을 보여라.
- **중요성**: 강한 상호작용(QCD)의 색가둠(confinement)의 수학적 설명. 현대 입자물리학 표준 모형의 수학적 기초.
- **현재 상태**: **미해결**. 격자 게이지 이론, Osterwalder-Schrader, 2차원·3차원 부분 결과(Glimm-Jaffe 등)는 있으나 4차원 엄밀 존재성은 아직.

**(4) 나비에-스토크스 존재성·매끄러움 (Clay 2000)**
- **출처**: 방정식 자체는 Claude-Louis Navier(1822) · George Gabriel Stokes(1845). Clay 공식 문서: Charles Fefferman, "Existence and Smoothness of the Navier-Stokes Equation", 2000.
- **질문**: 초기 속도장이 매끄럽고(ℝ^3 전체에서 정의) 무한대에서 충분히 빨리 감쇠할 때, 3차원 비압축성 나비에-스토크스 방정식에 대해 모든 시간에 걸쳐 존재하고 매끄러운 해가 있음을 증명하라. 혹은 유한 시간 내에 특이점이 발생하는 반례를 구성하라.
- **중요성**: 유체 동역학(대기, 해양, 공기역학)의 기초. Leray(1934)의 약해(weak solution)는 존재성을 부분적으로 해결했으나 정규성(smoothness)과 유일성이 미해결.
- **현재 상태**: **미해결**. Leray-Hopf 약해 존재, Scheffer(1976)·Caffarelli-Kohn-Nirenberg(1982) 부분 정규성, Tao의 평균장 근사 폭발 구성(2016) 등 부분 결과.

**(5) 호지 추측 (Hodge Conjecture, 1950)**
- **출처**: William V. D. Hodge, "The topological invariants of algebraic varieties", Proceedings of the International Congress of Mathematicians(ICM Cambridge, Mass.) 1950, vol 1, 182-192.
- **질문**: 사영 복소 비특이 대수다양체 X 위에서, 유리 계수 호지 부류(rational Hodge classes)가 모두 X의 복소 부분 대수다양체의 유리 선형 결합으로 표현되는가? 즉 Hdg^k(X, ℚ) = (대수적 사이클의 이미지) 인가?
- **중요성**: 위상수학·복소해석·대수기하의 교차점. 대수적 사이클 이론의 핵심.
- **현재 상태**: **미해결**. k=1(Lefschetz (1,1) 정리) 이미 증명. 일반 k는 미해결. Grothendieck이 "일반화된 Hodge 추측"의 원판 버전이 틀렸음을 보였음(1969).

**(6) 버치-스위너턴다이어 추측 (Birch–Swinnerton-Dyer, 1965)**
- **출처**: Bryan Birch · Peter Swinnerton-Dyer, "Notes on elliptic curves I, II", Journal für die reine und angewandte Mathematik 212(1963), 218(1965). 1960년대 초 EDSAC 컴퓨터 계산 기반.
- **질문**: 유리수체 ℚ 위의 타원 곡선 E의 Mordell-Weil 군 E(ℚ) 의 계수(rank)는 Hasse-Weil L-함수 L(E, s) 의 s = 1 에서의 영점의 차수(order of vanishing)와 같은가? 더 나아가 L(E, s) 의 s = 1 근방 Taylor 전개의 주도 계수는 E의 산술적 불변량(regulator, Shafarevich-Tate 군 크기, Tamagawa 수 등)의 명시적 공식으로 주어지는가?
- **중요성**: 타원 곡선의 유리점 구조와 L-함수 해석적 행동을 연결. 산술기하학 중심.
- **현재 상태**: **미해결**. Gross-Zagier(1986) + Kolyvagin(1988~1991)로 rank ≤ 1 인 경우 약형 BSD 일부 증명. 일반 rank는 미해결.

**(7) 푸앵카레 추측 (Poincaré Conjecture, 1904) — 해결**
- **출처**: Henri Poincaré, "Cinquième complément à l'Analysis Situs", Rendiconti del Circolo Matematico di Palermo 18(1904), 45-110. 원래 질문은 "단순 연결 닫힌 3-다양체는 3차원 구 S^3 에 위상동형인가?"
- **중요성**: 3차원 다양체 분류의 기초. 20세기 위상수학의 중심 문제.
- **해결**: **Grigori Perelman**이 2002-2003년 arXiv에 3편의 preprint를 공개함으로써 해결. Hamilton의 Ricci flow 프로그램에 surgery 기법을 추가하여 Thurston의 기하화 추측을 완전히 증명, 그 부산물로 푸앵카레 추측 해결. 페렐만은 2006 필즈상과 2010 Clay Millennium Prize(US$ 1,000,000) 모두 거부. 상세는 PROB-P0-2 참조.

---

## 4. 해결 현황 집계

- **해결**: 1개 — 푸앵카레(페렐만 2002-2003, 2006 필즈상 거부, 2010 Clay 상금 거부)
- **열림**: 6개 — 리만, P vs NP, 양-밀스, 나비에-스토크스, 호지, BSD
- **진전(부분 결과 존재)**: 전부. 다만 "해결"의 공식 인증은 푸앵카레만.

**본 프로젝트(n6-architecture)의 밀레니엄 난제 해결 현황은 0/7**이다. 즉 본 프로젝트에서 독자적으로 해결한 난제는 없으며, 푸앵카레 역시 외부(페렐만)의 해결을 참조할 뿐이다.

---

## 5. 정직성 선언 (재확인)

- 본 PROB-P0-1 문서는 **학습 노트**이다.
- 본 문서는 **어떤 밀레니엄 난제도 해결하지 않는다**.
- 7대 난제 중 실제로 해결된 것은 **푸앵카레 추측**(Perelman 2002-2003)뿐이다.
- 본 프로젝트(n6-architecture)의 독자적 해결 건수는 **0/7**이다.
- 모든 역사적 사실은 Clay 공식 문서, Devlin(2002), Jaffe(2006) 등 외부 1차 자료에 근거한다. 기입 오류가 있으면 출처를 재확인하여 수정할 것.

---

## 6. 다음 학습 노트

- **PROB-P0-2**: 푸앵카레 추측 해결 과정 상세 (Hamilton의 Ricci flow → Perelman 3편 논문 → 필즈상 거부 → Clay 상금 거부)
- **PROB-P0-3**: 7대 난제 선정 기준 + 수학 분과 매핑 (각 문제가 대표하는 분과, 상호 연결, Langlands 프로그램 등)
