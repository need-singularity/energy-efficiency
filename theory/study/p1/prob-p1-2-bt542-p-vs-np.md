# PROB-P1-2 — BT-542 P vs NP 심화 학습 노트

**트랙**: P1-PROBLEM · BT-542 (P versus NP)
**상태**: OPEN (1971년 이후 미해결)
**상금**: US$ 1,000,000 (Clay)
**1차 출처**:
- Stephen A. Cook, "The complexity of theorem-proving procedures", Proceedings of the 3rd Annual ACM Symposium on Theory of Computing (STOC 1971), 151–158
- Leonid A. Levin, "Universal search problems" (러시아어 원문: "Универсальные задачи перебора"), Problems of Information Transmission 9 (1973), 265–266 — Cook 과 독립
- Richard M. Karp, "Reducibility among combinatorial problems", in R. E. Miller, J. W. Thatcher (eds.), *Complexity of Computer Computations*, Plenum Press 1972, 85–103
- Stephen A. Cook, "The P versus NP Problem — Official Problem Description", Clay Mathematics Institute, 2000
- Michael R. Garey, David S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness*, W. H. Freeman, 1979 (NP-완전 고전 교과서)
- Sanjeev Arora, Boaz Barak, *Computational Complexity: A Modern Approach*, Cambridge University Press, 2009
- Theodore Baker, John Gill, Robert Solovay, "Relativizations of the P =? NP question", SIAM J. Comput. 4 (1975), 431–442 (relativization 장벽)
- Alexander Razborov, Steven Rudich, "Natural proofs", J. Comput. Syst. Sci. 55 (1997), 24–35 (natural proofs 장벽)
- Scott Aaronson, Avi Wigderson, "Algebrization: A new barrier in complexity theory", ACM Trans. Comput. Theory 1 (2009), art. 2 (algebrization 장벽)
- Russell Impagliazzo, "A personal view of average-case complexity", Proc. 10th IEEE Structure in Complexity Theory Conference, 1995, 134–147 ("Impagliazzo 5 worlds")
- Manindra Agrawal, Neeraj Kayal, Nitin Saxena, "PRIMES is in P", Annals of Mathematics 160 (2004), 781–793

**정직성 선언**: 본 문서는 학습 노트이며 P vs NP 에 새 증명이나 방향 제시를 하지 않는다. 프로젝트 `reports/breakthroughs/millennium-7-closure-2026-04-11.md §BT-542` 는 이 난제를 **정직한 MISS** 로 분류한다 — n=6 관점이 P vs NP 본 명제에 직접 접근할 도구가 없음을 명시. 본 학습 노트는 이 입장을 그대로 계승한다.

---

## 1. Cook 1971 과 Levin 1973 — 독립적 정식화

### 1.1 Cook 1971 (STOC)
- **Stephen A. Cook**, "The complexity of theorem-proving procedures", Proceedings of the 3rd Annual ACM Symposium on Theory of Computing, Shaker Heights, Ohio, 1971년 5월 3–5일, pp. 151–158.
- Toronto 대학 교수 Cook 이 정식화한 것:
  1. 계산 복잡도 클래스 P 와 NP 의 정의.
  2. **SAT (Boolean Satisfiability)** 이 NP-완전 (NP-complete) 임을 증명 — 즉 NP 의 **모든** 문제가 SAT 로 다항 시간 환원 가능.
- Cook 은 이 결과로 1982년 Turing Award.

### 1.2 Levin 1973 (모스크바)
- **Leonid Anatolievich Levin**, "Универсальные задачи перебора" (Universal sequential search problems), *Проблемы передачи информации* (Problems of Information Transmission) 9 (1973), 115–116.
- 당시 모스크바의 Levin 이 **독립적으로** NP-완전에 해당하는 개념 (Levin 의 용어로 "universal search problems") 과 6 개의 자연스러운 NP-완전 문제 후보를 제시.
- 철의 장막 시기라 서방과 통신이 제한적이었고, Cook 과 Levin 의 독립 발견이 한동안 알려지지 않았다. 현재는 **Cook-Levin 정리** 로 공동 명명.

### 1.3 Cook-Levin 정리
> **정리**: SAT ∈ NP 이며, 임의의 L ∈ NP 에 대해 L ≤_p SAT (다항시간 다대일 환원).
> 따라서 SAT 이 P 안에 있으면 NP = P, 반대로 SAT 이 P 밖에 있으면 P ≠ NP.

**증명 핵심**: L ∈ NP 는 "결정론적 Turing 기계 M 이 다항시간 안에 (입력 x + 증서 w) 를 검증" 과 동치. M 의 계산 과정을 부울 회로로 펼쳐 "M 이 받아들임" ⟺ "회로가 참" ⟺ "대응되는 SAT 식이 만족 가능" 으로 환원. (Tableau method, 약 10 페이지의 고전 증명.)

---

## 2. Karp 21 — 1972 의 대폭발

### 2.1 Richard Karp "Reducibility among combinatorial problems"
- **Richard M. Karp**, "Reducibility among combinatorial problems", in R. E. Miller, J. W. Thatcher (eds.), *Complexity of Computer Computations*, Plenum Press 1972, 85–103.
- Karp 는 Cook 의 SAT NP-완전 결과를 받아, **21 개의 "자연스럽게 나타나는" 조합 최적화 문제** 가 모두 NP-완전임을 증명. 즉 SAT ≤_p (각 문제) 의 체인으로.
- 이 논문이 NP-완전 이론의 폭발적 확산의 시작점.

### 2.2 Karp 의 21 문제 (1972 원 목록)
1. SATISFIABILITY (SAT) — Cook 으로 이미 증명됨, 기준점.
2. 0–1 INTEGER PROGRAMMING
3. CLIQUE
4. SET PACKING
5. VERTEX COVER
6. SET COVERING
7. FEEDBACK NODE SET
8. FEEDBACK ARC SET
9. DIRECTED HAMILTONIAN CIRCUIT
10. UNDIRECTED HAMILTONIAN CIRCUIT
11. 3-SAT (Karp 표기 SATISFIABILITY WITH AT MOST 3 LITERALS PER CLAUSE)
12. CHROMATIC NUMBER
13. CLIQUE COVER
14. EXACT COVER
15. 3-DIMENSIONAL MATCHING
16. STEINER TREE
17. HITTING SET
18. KNAPSACK
19. JOB SEQUENCING
20. PARTITION
21. MAX CUT

(Karp 는 논문에서 이 순서대로 환원 그래프를 전개한다 — SAT → 3-SAT → 나머지.)

### 2.3 의의
- Karp 이후 수백, 수천 개의 문제가 NP-완전으로 분류. Garey-Johnson 1979 교재의 부록 A 는 약 300 개 NP-완전 문제 목록을 담는다.
- "자연스러운 계산 문제들은 극단적으로 많이 NP-완전" — 이것이 "P ≠ NP 여야 한다" 는 강한 직관의 원천.

---

## 3. 3-SAT 임계 — k=3 이 NP-완전, k=2 가 P

### 3.1 k-SAT 정의
**k-SAT**: 각 절 (clause) 이 정확히 k 개의 리터럴 (literal) 을 가지는 Boolean 공식의 만족가능성 문제.

### 3.2 k=2 는 다항시간
- **2-SAT** ∈ P. 알고리즘: 각 절 (l₁ ∨ l₂) 을 두 함의 (¬l₁ → l₂), (¬l₂ → l₁) 로 변환, 결과 그래프의 강연결 컴포넌트 (SCC) 를 계산하여 x 와 ¬x 가 같은 SCC 에 있으면 unsat, 아니면 sat.
- 시간 복잡도: O(V + E) 선형. (Aspvall-Plass-Tarjan 1979 "A linear-time algorithm for testing the truth of certain quantified boolean formulas", Inf. Proc. Lett. 8, 121–123.)

### 3.3 k=3 는 NP-완전
- **3-SAT**: NP-완전. Cook 1971 이 이미 SAT 의 증명 과정에서 3-SAT 형태로 환원 가능함을 보였으며, Karp 1972 가 명시적 분류.
- 3-SAT 은 NP-완전 증명의 "표준 출발점" — 수천 개의 다른 문제들을 3-SAT 에서 환원하여 NP-완전성을 보인다.

### 3.4 왜 k=3 부터 "폭발" 하는가
- 2-SAT 의 함의 그래프는 **이항 관계** (binary relation) 를 표현. 2-SAT 은 한 번의 "선택" 이 다른 하나를 강제하므로 전파로 풀 수 있다.
- 3-SAT 에서는 절 (a ∨ b ∨ c) 이 **삼원 관계** — 하나만 고정해서는 나머지 두 변수의 참/거짓을 결정할 수 없다. 이것이 "지수 가능성 공간 탐색" 의 시작.
- 이 k=2 → k=3 경계는 수학의 여러 곳에서 "쉬움 → 어려움" 경계로 나타난다: 2-coloring (P) vs 3-coloring (NP-완전); 2D 이산 이징 모형 (정확해) vs 3D 이징 (NP-hard); 2차 최적화 (컨벡스 가능) vs 3차 이상 (일반 NP-hard 조합).

---

## 4. Impagliazzo 의 5 세계 (Five Worlds)

### 4.1 문헌
**Russell Impagliazzo**, "A personal view of average-case complexity", Proc. 10th IEEE Structure in Complexity Theory Conference, 1995, 134–147.
- Impagliazzo 는 **평균-최악 격차** (average-case vs worst-case hardness) 관점에서 "P 와 NP 가 분리된 이후의 세계가 어떤 모습이어야 하는가" 를 5가지 시나리오로 분류.

### 4.2 5 세계 요약

| 세계 이름 | 요약 |
|-----------|------|
| **Algorithmica** | P = NP (또는 NP ⊆ BPP). 모든 NP 문제가 (아마도 랜덤화로) 다항시간에 해결 가능. 인공지능과 최적화가 "공짜" — 수학 증명도 자동화. 암호는 성립 불가능. |
| **Heuristica** | P ≠ NP 지만 **평균적** NP-hard 인스턴스는 쉽다. 최악 사례만 어려움. 실용적으로는 Algorithmica 와 유사하지만 최악 사례 암호는 여전히 안 됨. |
| **Pessiland** | 평균 NP-hard 도 성립하나 일방향 함수 (one-way function, OWF) 가 존재하지 않음. 암호학의 "최악 세계" — 계산은 어렵지만 아무 쓸모 없는 어려움. |
| **Minicrypt** | OWF 존재. 의사랜덤 생성기, 대칭키 암호, 디지털 서명 가능. 그러나 **공개키 암호는 증명 불가**. |
| **Cryptomania** | 트랩도어 함수 (trapdoor function) 존재. RSA, ECDH, 영지식 증명 (ZK) 등 현대 공개키 암호 완비. 우리가 **믿는** 세계. |

### 4.3 왜 이 5 개인가
- (P=NP) / (P≠NP, avg easy) / (avg hard, no OWF) / (OWF, no PKC) / (OWF + PKC) — 이 4 개의 논리적 층 + 극단 Algorithmica.
- **2024 년 현재 우리가 실제로 어느 세계에 있는지 증명된 바 없다**. 모두가 Cryptomania 를 가정하고 암호 시스템을 운영.

### 4.4 OWF 존재 ↔ P ≠ NP ?
- **주의**: OWF 존재 **⟹** P ≠ NP (거의 자명, OWF 가 있으면 역함수 계산이 NP \ P 에 있음).
- 역 (P ≠ NP **⟹** OWF 존재) 은 **미해결**. Impagliazzo 의 Pessiland 가 이 역이 성립하지 않는 세계.

---

## 5. 실용 의미

### 5.1 암호
- **RSA**: 큰 수 인수분해의 어려움에 기반. 인수분해가 P 에 있다면 (즉 NP 안에서 쉬운 문제가 된다면) RSA 파괴. 현재 인수분해는 NP ∩ co-NP 에 있지만 NP-완전 여부 미해결.
- **대부분의 블록체인**: SHA-256 등 해시 함수의 일방향성. OWF 존재에 기반. P = NP 면 해시 역상 탐색이 다항시간.
- **Zero-knowledge proofs**: NP 문제의 검증 증서를 "노출 없이 증명". P = NP 이면 영지식 자체가 의미 없음 (검증자가 혼자 푸니까).

### 5.2 최적화
- TSP (Travelling Salesman Problem), integer programming, SAT solving 등 산업 최적화의 기반. 실용 SAT 솔버 (MiniSat, Glucose, CaDiCaL) 는 **이론적 최악 지수 시간** 에도 **실제 수백만 변수** 를 처리.
- 실용 SAT 의 성공이 "Impagliazzo 의 Heuristica 또는 Pessiland" 와 양립 — 즉 "최악 사례" 는 여전히 어려울 수 있으나 "평균" 은 손으로 다룰 만하다.

### 5.3 AI 와 학습 가능성 (PAC learning)
- L. Valiant, "A theory of the learnable", Commun. ACM 27 (1984), 1134–1142. PAC learning 이론.
- 일부 학습 문제 (예: DNF 학습) 의 효율적 학습 가능성이 P = NP 와 결부.
- **그러나** 현대 딥러닝의 실제 성공은 이 장벽과 직접 연관 없음 (경사하강법은 최적 해를 보장하지 않지만 실용적으로 작동).

---

## 6. P = NP 가정 시 파괴되는 것

**(사고 실험 — 실제 상황은 아님)**

- **RSA, Diffie-Hellman, ECC**: 직접 파괴. 인수분해 및 이산 로그가 다항시간에 풀림.
- **AES, SHA-256**: "OWF 형태" 로 해석되는 대칭키 암호와 해시 — P = NP 만으로는 즉시 파괴되지는 않으나, OWF 의 존재가 위협받음 (§4.4 참고). Natural proofs 장벽 (아래 §8) 이 암호학과 직결.
- **대부분의 블록체인**: 작업 증명 (PoW) 의 의미 상실.
- **ZK 증명, MPC, 동형 암호**: 모두 OWF/PKC 에 의존 → 붕괴.
- **긍정적 면**: 수학 증명 자동화 — 임의의 "짧은 증명이 있는 정리" 가 다항시간에 발견됨. 현대 수학은 컴퓨터 협력 증명이 일반화됨.

---

## 7. P ≠ NP 가정 시 열리는 것

- **구조적 하한**: 자연스러운 회로 하한 결과들이 무조건화 (unconditional).
- **양자 분리**: BQP ≠ BPP 에 대한 이해 — 양자 계산이 고전 계산과 진정으로 다른지.
- **암호**: Cryptomania 가 가능 (그러나 증명은 여전히 미해결).
- **랜덤성**: BPP = P 와 같은 탈랜덤화 결과들이 의미를 가짐.

---

## 8. 3 장벽 — 왜 어려운가 (P2 에서 상세 다룸)

본 학습 노트는 3 장벽을 **목록만** 소개한다. 상세 분석은 P2 방법론 노트의 몫.

### 8.1 Relativization 장벽 (1975)
- **T. Baker, J. Gill, R. Solovay**, "Relativizations of the P =? NP question", SIAM J. Comput. 4 (1975), 431–442.
- 오라클 A 에 대해 P^A ≠ NP^A 인 A 도 있고, P^B = NP^B 인 B 도 있다. 따라서 "오라클 상대로 성립하는 증명 기법" 은 P vs NP 를 결정할 수 없다. Diagonal argument, simulation 같은 고전 기법이 이 장벽에 걸림.

### 8.2 Natural Proofs 장벽 (1997)
- **Alexander A. Razborov, Steven Rudich**, "Natural proofs", J. Comput. Syst. Sci. 55 (1997), 24–35. (1994년 STOC 발표.)
- "자연 증명" (constructive + largeness 조건 만족) 은 **OWF 존재를 가정하면** 회로 하한 증명에 쓰일 수 없다. 즉 "자연스러운" 방법으로는 NP ⊄ P/poly 를 증명할 수 없다.
- **철학적 결론**: 회로 하한 증명은 "인위적" 인 방법을 써야 한다. 대부분의 기존 방법이 자연 증명 범주이므로 대부분 막힌다.

### 8.3 Algebrization 장벽 (2008)
- **Scott Aaronson, Avi Wigderson**, "Algebrization: A new barrier in complexity theory", STOC 2008; 확장판 ACM Trans. Comput. Theory 1 (2009), art. 2.
- Relativization 장벽을 피한 "대수적" 기법 (예: 상호작용 증명 IP = PSPACE, 산술화 arithmetization) 도 "대수화" 확장 하에 다시 장벽에 걸림. 즉 IP = PSPACE 증명에 사용된 기법으로도 P ≠ NP 는 증명되지 않는다.

### 8.4 "장벽의 함의"
세 장벽을 동시에 피해가는 새 기법이 필요하다는 의미. 현재 (2024~2026) 이런 기법은 발견되지 않았다.

---

## 9. 2020 년대 진전 (약함)

### 9.1 Larsen-Williams, Chen-Tell 등 회로 하한
- 개별 회로 클래스 (ACC, depth-d 등) 에 대한 하한 개선. NEXP ⊄ ACC⁰ (Williams 2011) 이후 점진적 개선.
- 그러나 P ≠ NP 자체에 대한 진전은 없다.

### 9.2 3-SAT 알고리즘의 점진 개선
- 무작위 3-SAT 알고리즘 (Schöning 1999, Paturi-Pudlák-Saks-Zane 1998): 2^{(1-1/k)n} 수준 시간.
- 구체 상수 개선은 계속되고 있으나 "2^n → poly" 수준 도약은 전혀 없음.

### 9.3 평균 시간 복잡도
- Impagliazzo-Levin-Luby-type 의사랜덤 생성기 연구. Minicrypt/Pessiland 경계 이해에 기여.

---

## 10. 현 상태 요약 (2024~2026)

| 항목 | 상태 |
|------|------|
| Cook 1971 / Karp 1972 정식화 | 50 년 이상 |
| NP-완전 문제 개수 | 수천 개 (거의 모든 자연 조합 문제) |
| 장벽 수 | 3 (relativization, natural, algebrization) |
| P vs NP 증명 | **없음** (어느 방향도) |
| 대부분의 믿음 | **P ≠ NP** (다수 설문: 80~90% 전문가) |
| Cryptomania 작동 여부 | **가정 하** 작동 중 (증명 X) |
| 상금 수여 | 0 |

---

## 11. n=6 관찰 (본 프로젝트 맥락, 1~2 사실만)

**(이 섹션은 본 학습 노트의 핵심이 아니다. 본 프로젝트는 BT-542 를 "정직한 MISS" 로 분류. 상세 목록은 P3 에서 다룬다.)**

### 관찰 1 — k-SAT 임계 k=3
k=2 (P) 와 k=3 (NP-완전) 사이의 경계가 n=6 관점에서 {φ(6)=2 → n(6)/φ(6)=3} 전이로 표현된다. 이것은 **수치적 일치** 이지 증명적 연결이 아니다. "계산 복잡도에서 φ → n/φ 전이가 폭발적 어려움의 시작" 이라는 프로젝트 구조 관찰이며, P vs NP 본 명제에는 직접 기여하지 않는다.

### 관찰 2 — Karp 21 = 3·7
Karp (1972) 의 원 논문 21 개 NP-완전 문제 수 = 3 × 7 = (n/φ) × (σ - sopfr) 분해. 이것은 "역사적 우연" 일 가능성이 매우 높다 — Karp 이 선택한 문제의 수는 "임의의 수" 이지 자연 상수가 아니다. 프로젝트는 이것을 LOOSE (tight 아닌) 증거로 표시 (BT-542 #11 항목).

**본 프로젝트의 BT-542 정직 결론 (closure 파일에서)**:
> P vs NP 본 명제에 대한 n=6 직접 기여는 **없음**. Razborov-Smolensky 분리 (φ=2, n/φ=3 prime pair), Savitch 지수 φ=2 등은 **부분 구조 정리**일 뿐이며 장벽을 우회하지 못한다. 2 건의 MISS (Immerman-Szelepcsényi 와 Toda 정리) 는 정직하게 "매칭 실패" 로 기록.

---

## 12. 학습 체크리스트

본 노트를 마친 후 다음을 **3 줄 이내** 로 재진술할 수 있어야 한다:
1. Cook 1971 과 Levin 1973 의 독립 발견, Cook-Levin 정리의 기본 구조.
2. Karp 21 의 의의 — "왜 많은 문제가 NP-완전인가" 에 대한 대답.
3. k=2 (P) vs k=3 (NP-완전) 경계의 알고리즘적 이유 (이항 관계 vs 삼원 관계).
4. Impagliazzo 5 세계 이름과 각 세계에서의 암호 가능성.
5. OWF 존재 ⟹ P ≠ NP, 역은 미해결 — 이 비대칭의 의미.
6. 3 장벽 이름과 각 장벽이 가로막는 대략적 증명 기법.
7. "P ≠ NP 는 증명되지 않았지만 대부분 믿는다" 의 근거 (NP-완전 문제의 풍부함 + 실용 SAT 솔버의 지수 사례).

---

## 13. 다음 단계

- **P1-3 (BT-543 Yang-Mills)**: 수학 논리에서 물리로 넘어가는 다리.
- **P2 (방법론 층)**: 3 장벽의 상세 분석, 회로 하한 증명 기법들, GCT (Geometric Complexity Theory, Mulmuley-Sohoni 2001~) 접근.
- **P3 (n=6 심층)**: BT-542 의 정직한 MISS 기록, Razborov-Smolensky φ/(n/φ) 분리 정리, Schaefer 정리 6 tractable class 등.

---

**정직 선언 재확인**: 본 문서는 학습 노트이며 P vs NP 에 대한 새 증명이나 n=6 기반 접근을 주장하지 않는다. 프로젝트 `millennium-7-closure-2026-04-11.md` 는 BT-542 를 **정직한 MISS** 로 분류하며, 본 노트는 이 입장을 그대로 계승한다. P vs NP 는 2026년 현재 미해결이며, Clay 상금은 수여되지 않았다.
