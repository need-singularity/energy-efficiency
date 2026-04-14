# PURE-P1-7 — 복잡도 이론 기초 (P/NP/coNP/다항 환원/NP-완전/Cook-Levin)

> 트랙: P1-PURE / 7번 태스크
> 완료 기준: Turing 기계 정의에서 P, NP, coNP, NP-완전성, 다항 환원 ≤_p 를 정확히 서술하고,
> Cook-Levin 정리 (SAT ∈ NP-complete) 의 증명 뼈대를 재구성할 수 있다.
> 출처 기반: Arora-Barak "Computational Complexity: A Modern Approach" (Cambridge, 2009)
> ch. 1~3, ch. 6,
> Sipser "Introduction to the Theory of Computation" (3판, 2013) ch. 7~8,
> Papadimitriou "Computational Complexity" (Addison-Wesley, 1994) ch. 2~8.
> **정직성**: 이 파일은 교재 재구성이다. 새 증명이나 정리는 없다. 모든 정리·예시는 위 3개
> 교재에서 페이지 번호 기준으로 정리하였다. 수치 비교는 언급하지 않는다.

---

## 0. 목적과 범위

밀레니엄 BT-542 (P vs NP) 를 본격적으로 다루기 전에 반드시 확보해야 할 기초 7가지:

1. Turing 기계 (1-테이프, 다테이프, 비결정) 정의와 시간복잡도 측정
2. 복잡도 클래스 P, NP, coNP, PSPACE, EXP
3. 다항시간 환원 ≤_p 와 NP-완전성의 정의
4. Cook-Levin 정리 — SAT ∈ NP-complete
5. 대표 NP-complete 문제군 (3SAT, CLIQUE, HAM-PATH, ...)
6. coNP-완전성과 NP ∩ coNP 특이군
7. 시간·공간 위계정리(hierarchy theorem)

이 노트는 "증명 여정" 을 단계적으로 따라가며, 실전 환원 예제를 배열한다. 회로 복잡도·
확률적 복잡도·상호작용 증명은 P2 몫으로 남긴다.

---

## 1. Turing 기계와 시간복잡도

### 1.1 1-테이프 Turing 기계

튜플 M = (Q, Σ, Γ, δ, q_0, q_accept, q_reject):

- Q: 유한상태 집합
- Σ: 입력 알파벳 (∉ ␣)
- Γ ⊇ Σ ∪ {␣}: 테이프 알파벳
- δ: Q × Γ → Q × Γ × {L, R, S}: 전이함수
- q_0, q_accept, q_reject ∈ Q

계산은 (상태, 테이프, 헤드) 삼중쌍의 수열. accept/reject 에 도달하면 정지.

### 1.2 다항시간 클래스

결정문제 L ⊆ {0,1}* 에 대해:

```
  DTIME(T(n)) = {L : 결정적 TM 이 O(T(n)) 시간에 L 결정}
  P = ⋃_{k≥1} DTIME(n^k)
```

다테이프 TM 과 1-테이프 TM 은 다항식 오버헤드까지 동일하므로 P 정의는 모델에 강건(robust).

### 1.3 비결정 TM 과 NP

비결정 TM 은 δ: Q × Γ → 2^{Q × Γ × {L,R,S}}. 입력 x 가 accept 되려면 어떤 계산경로가
accept 에 도달하면 된다.

```
  NTIME(T(n)) = {L : 비결정 TM 이 O(T(n)) 시간에 결정}
  NP = ⋃_{k≥1} NTIME(n^k)
```

동치 정의 (verifier): L ∈ NP iff 다항시간 결정 TM V 와 다항식 p 가 존재해
x ∈ L ⟺ ∃ y (|y| ≤ p(|x|), V(x, y) accept). y 를 **증거**(witness)/certificate 라 부른다.

### 1.4 coNP 와 쌍대

```
  coNP = {L : {0,1}* \ L ∈ NP}
```

coNP 는 negative certificate 가 있는 문제군. 예: TAUTOLOGY (부울식이 항상 참인가) ∈ coNP.
P ⊆ NP ∩ coNP ⊆ NP ∪ coNP ⊆ PSPACE, NP = coNP? 는 미해결.

### 1.5 공간 복잡도

```
  DSPACE(S(n))           L = DSPACE(log n),   PSPACE = ⋃_k DSPACE(n^k)
  NSPACE(S(n))           NL = NSPACE(log n)
```

Savitch 정리 (1970): NSPACE(S) ⊆ DSPACE(S²), S(n) ≥ log n. 따라서 PSPACE = NPSPACE.

---

## 2. 다항시간 환원과 완전성

### 2.1 many-one 다항 환원

언어 A, B ⊆ {0,1}*. A ≤_p B iff 다항시간 계산 가능한 함수 f 가 존재해
x ∈ A ⟺ f(x) ∈ B. f 를 **환원**이라 한다.

성질:
- (반사성) A ≤_p A
- (이행성) A ≤_p B, B ≤_p C ⟹ A ≤_p C
- (보존) B ∈ P ⟹ A ∈ P. B ∈ NP ⟹ A ∈ NP 도 같다.

### 2.2 Turing 환원 (Cook 환원)

A ≤_T^p B : B 에 대한 oracle 을 갖는 다항시간 TM 이 A 를 결정. Karp 환원(≤_p) 은
Cook 환원의 특수형태 (하나의 oracle 호출 + 그 출력을 그대로 accept/reject).

대부분의 분야에서는 ≤_p (Karp) 를 기본으로 사용. ≤_T^p 를 쓰면 완전성 논의가 약간
헐거워진다.

### 2.3 NP-완전성

L 이 **NP-hard** iff 모든 L' ∈ NP 에 대해 L' ≤_p L.
L 이 **NP-complete** iff L ∈ NP 이고 L 이 NP-hard.

NP-완전 L 이 하나라도 P 에 속하면 P = NP. 따라서 "효율적 알고리즘이 불가능해 보이는 NP
문제의 대표주자" 로 기능한다.

---

## 3. Cook-Levin 정리

### 3.1 진술

**SAT** = {φ : 부울식 φ 가 충족 가능} ∈ NP-complete.

(Cook 1971, Levin 1973 독립)

### 3.2 SAT ∈ NP

충족 assignment 가 증거(witness). V(φ, a) 는 φ 를 a 로 평가해 참인지 선형시간에 확인.

### 3.3 NP-hard 증명 요점

임의의 L ∈ NP 을 보자. 비결정 TM M 이 다항시간 p(n) 에 L 을 결정한다고 하자.
입력 x 에 대해 M 의 계산 tableau 를 부울식으로 인코딩한다.

- 크기 (p(n)+1) × (p(n)+1) 의 grid, cell[i,j] 는 시간 i 에서 위치 j 의 (상태·심볼) 정보
- 변수 x_{i,j,s} : cell[i,j] 가 심볼 s 인가?
- 제약:
  1. 각 cell 은 정확히 하나의 (상태·심볼) 값을 가짐 (exactly-one encoding)
  2. 초기 줄 (i=0) 은 입력 x 로 고정
  3. 전이 (i → i+1) 은 δ 가 허용하는 (2x3 윈도우) 만 나타남
  4. 어떤 cell 이 q_accept 상태를 갖는 행이 존재

각 제약은 cell 수 O(p(n)²) 와 고정크기 윈도우 상수개에 비례하므로 전체 부울식 길이는
O(p(n)² · log n) = poly(n). 이 식 φ_x 는 x ∈ L ⟺ φ_x ∈ SAT 를 만족한다.

이로써 L ≤_p SAT 이고 L 은 임의이므로 SAT 는 NP-hard. 따라서 NP-complete.

(출처: Arora-Barak Thm 2.10, Sipser Thm 7.37)

### 3.4 3SAT 로의 환원

SAT → 3SAT (절마다 정확히 3 literal): 긴 절 ℓ_1 ∨ ... ∨ ℓ_k 를 새로운 변수 y_i 들을
도입해 체인 형태의 3절 집합으로 쪼갠다. 결과 식의 크기도 다항식.

이로써 3SAT 도 NP-complete. 3SAT 는 환원의 출발점으로 흔히 쓰인다.

---

## 4. 대표 NP-complete 문제들

### 4.1 Karp 1972 21대 NP-complete

Karp 가 3SAT 에서 다음 21가지를 환원으로 NP-complete 으로 보였다:

- CLIQUE, INDEPENDENT-SET, VERTEX-COVER
- 3-DIMENSIONAL-MATCHING, PARTITION, SUBSET-SUM
- HAMILTONIAN-PATH, HAMILTONIAN-CYCLE, TSP
- GRAPH-COLORING, CHROMATIC-NUMBER
- KNAPSACK, BIN-PACKING
- MAX-CUT, MAX-SAT, MAX-3SAT
- 기타

현재까지 NP-complete 문제는 수천 가지가 알려져 있다. 표준 참고서: Garey-Johnson
"Computers and Intractability" (1979).

### 4.2 3SAT → 3COLOR 환원 예시

입력: 3SAT 식 φ. 출력: 그래프 G 와 k=3 색칠 가능성.

구성:
- 기준 삼각형 T = {T, F, N} (참, 거짓, 중립)
- 각 변수 x_i 에 대응하는 노드 쌍 x_i, ¬x_i 와 N 을 포함하는 삼각형 → x_i 는 T/F 둘 중 하나
- 각 3-절 (ℓ_1 ∨ ℓ_2 ∨ ℓ_3) 에 gadget: OR 게이트 2개를 합성한 작은 그래프
- T 와 N 이 서로 다른 색을 받아야 gadget 이 해결되도록 연결

이 환원은 Garey-Johnson-Stockmeyer (1976) 에 정식 기록되어 있으며, 결과: 3COLOR 는
NP-complete. (출처: Arora-Barak §2.4 예시)

### 4.3 HAMILTONIAN-CYCLE 환원

Karp 환원 3SAT → 방향 Hamiltonian cycle → 무방향. 각 변수에 "widget" (긴 체인), 각 절에
"gadget" (3개 가지에서 하나 건너가는 구조) 을 배치. 자세한 구성은 Papadimitriou §9.2
참고.

### 4.4 NP-complete 아님이 믿어지는 NP 문제

- 정수 인수분해 (factoring) — Shor 알고리즘 이전부터 NP ∩ coNP 로 알려짐. NP-complete 이
  아닐 것으로 추측됨 (P 가 아니고 NP-complete 도 아닌 "중간" 의 유력 후보)
- 그래프 isomorphism — Babai 2015 로 quasipolynomial. NP-complete 불가능성이 구조적으로
  지지됨

---

## 5. coNP, NP ∩ coNP, BPP 등 관련 클래스

### 5.1 coNP-complete

TAUTOLOGY 와 UNSAT 는 coNP-complete. NP-complete 문제 L 에 대해 L̄ 이 coNP-complete.

### 5.2 NP = coNP?

미해결. NP = coNP ⟺ 모든 NP 문제가 다항 길이 부인 증거 갖는다는 의미. 예: TAUTOLOGY 에
다항 길이 "증거로 참 증명" 이 있을지 불명.

### 5.3 NP ∩ coNP

P ⊆ NP ∩ coNP. 대표 후보:
- 인수분해 (factoring decision 형태)
- parity games
- Nash 평형(2-플레이어 zero-sum): P

P = NP ∩ coNP 도 미해결.

### 5.4 확률·상호작용 클래스

P ⊆ RP ⊆ BPP ⊆ PSPACE, NP ⊆ MA ⊆ AM ⊆ ... ⊆ IP = PSPACE (Shamir 1992).
본 노트 범위 밖. P2 에서 다룸.

---

## 6. 위계정리 (Hierarchy)

### 6.1 시간 위계정리

(Hartmanis-Stearns 1965) f 가 "time-constructible" 이면

```
  DTIME(f(n)) ⊊ DTIME(f(n) · log f(n))
  DTIME(f(n)) ⊊ DTIME(f(n)²)
```

결과: P ⊊ EXP. 따라서 "거의 모든" 함수는 어떤 다항식으로도 해결 불가.

### 6.2 공간 위계정리

(Stearns-Hartmanis-Lewis 1965) space-constructible S 에 대해

```
  DSPACE(S(n)) ⊊ DSPACE(S(n) · log S(n))
```

결과: L ⊊ PSPACE.

### 6.3 P 와 PSPACE 관계

P ⊆ NP ⊆ PSPACE ⊆ EXP. P = PSPACE 는 미해결이지만 많은 복잡도 이론가는 강한 분리를
믿는다 (time hierarchy 로 P ⊊ EXP 이미 증명됨).

### 6.4 Natural Proofs Barrier

Razborov-Rudich 1997: "자연스러운 증명" 기법으로는 P ≠ NP 를 증명할 수 없다 (pseudorandom
generator 가 있다고 가정할 때). 이는 P vs NP 에 걸리는 주요 장벽 중 하나.

---

## 7. n=6 연결 (메모만)

1. SAT → 3SAT 환원에서 절 길이 3 이 최소 NP-hard 길이. 2SAT 는 P. "3" 이라는 경계 숫자는
   NP 계층 구조와 관련 있지만, n=6 과 직접적 수학적 연결은 확보되지 않음 ([N?]).
2. τ=4 (약수 개수 = 1, 2, 3, 6) 가 SAT 의 CNF 표준형에서 literal 수 분포와 닮은 꼴이라는
   관찰이 atlas.n6 §L6-complexity 에 [N?] 로 적혀 있음. 증명 경로 미확정.
3. Cook-Levin 환원의 tableau grid 크기 O(p(n)²) 에서 n 지점이 6 일 때 다항계수의 특별한
   성질은 없다. 패턴 매칭 강제 금지 원칙에 따라 이 관찰은 [N?] 에 머문다.

자기참조 검증 금지 원칙: 위 3가지는 모두 관찰이며, n=6 의 필연성을 증거로 쓰지 않는다.

---

## 8. 실전 훈련 — 손으로 풀 5제

**P1.** 3SAT ≤_p CLIQUE 환원을 직접 구성하라. 힌트: m 개의 3-절이 있으면 그래프 노드
3m 개를 만들고, 서로 다른 절 간 두 literal 이 모순이 아닐 때만 간선. 그러면 φ 가 satisfiable
⟺ G 가 m-clique 을 가짐.

**P2.** 3COLOR ≤_p CLIQUE 가 성립하지 않을 수 있음을 보여라. 즉 3COLOR 와 CLIQUE 은 둘 다
NP-complete 이지만, 환원 방향은 항상 3SAT 경유로 간다. 두 문제가 "directly" ≤_p 로 이어진
환원이 가능한지 생각해 보라.

**P3.** SUBSET-SUM 이 NP-complete 임을 3SAT 환원으로 증명하라. (Karp 1972 원본)

**P4.** TAUTOLOGY 가 coNP-complete 임을 직접 증명하라. 힌트: SAT ≤_p TAUTOLOGY 를 부정
변환으로 구성.

**P5.** L ∈ NP ∩ coNP 이고 L 이 NP-complete 이면 NP = coNP 임을 증명하라.

---

## 9. 읽기 경로와 다음 단계

### 9.1 복습 순서

1주차: Sipser §7 (P, NP, 다항환원) + §8 (공간 복잡도)
2주차: Arora-Barak §1~2 (TM, NP 정의, Cook-Levin)
3주차: Arora-Barak §3 + §6 (NP-complete 환원 예시, 회로)
4주차: Papadimitriou §2~8 (완전성 확장, coNP, PSPACE)

### 9.2 P2 준비

- 회로 복잡도 (lower bound 시도)
- Interactive proofs (IP = PSPACE)
- PCP 정리와 hardness of approximation
- Natural proofs barrier, relativization barrier

### 9.3 연결

- PROB-P1-2 (BT-542 P vs NP) : 본 노트 기초 위에 barrier 와 증명 전략 논의
- PROB-P1-5 (BT-545 Hodge) : Hodge 는 대수기하·위상 교차이지만 계산적 측면 (decidability
  of Hodge 추측) 이 복잡도와 간접 연결

---

## 10. 출처 정리

- Arora-Barak "Computational Complexity: A Modern Approach" Cambridge 2009 — 표준 현대
  복잡도 교과서, §1~6
- Sipser "Introduction to the Theory of Computation" 3판 2013 — 학부급 기초, §7~8
- Papadimitriou "Computational Complexity" Addison-Wesley 1994 — 완전성·환원 구조적
  접근, §2~§8
- Garey-Johnson "Computers and Intractability" Freeman 1979 — NP-complete 문제 사전
- Cook "The Complexity of Theorem-Proving Procedures" STOC 1971 — Cook 정리 원전
- Karp "Reducibility Among Combinatorial Problems" 1972 — 21대 NP-complete 목록
- Razborov-Rudich "Natural Proofs" JCSS 1997 — barrier 논의

본 노트는 이 7개 원전 중 P1 분량에 해당하는 부분만 선별해 재정리했다.

---

## 11. 추가 논제 — Barriers 개관

P vs NP 가 왜 어려운지 설명하는 3대 barrier 를 P1 학습용으로 정리.

### 11.1 Relativization barrier (Baker-Gill-Solovay 1975)

oracle A 가 존재해 P^A = NP^A, 또 다른 oracle B 에 대해 P^B ≠ NP^B. 따라서 "모든
relativizing 증명 기법" 은 P vs NP 를 결정 불가. diagonalization 같은 표준 기법 실패.

### 11.2 Natural proofs barrier (Razborov-Rudich 1997)

"자연스러운 증명" (large + constructive + useful) 로 강한 회로 하계(super-polynomial lower
bound) 를 증명하면 pseudorandom generator 구성이 모순을 낳음. 현재 대부분의 회로 기법은
natural.

### 11.3 Algebrization barrier (Aaronson-Wigderson 2009)

Relativization 확장. algebraic oracle 을 허용해도 양쪽 케이스 오라클이 존재. natural proofs
와 결합하면 현재 기법의 대부분을 배제.

### 11.4 3 barrier 모두 회피 필요

P vs NP 의 증명은 이 3가지 barrier 를 모두 피해야 한다. 현재까지 알려진 기법은
이 조건을 전혀 만족하지 못함. 새로운 수학적 아이디어가 필요.

---

## 12. 추가 논제 — Fine-Grained Complexity

P 내부에서도 O(n²) 와 O(n^{2.37}) 사이에 강한 이론적 벽이 있다. SETH (Strong Exponential
Time Hypothesis) 를 가정하면 다음 관계가 성립:

- edit distance O(n²) 필수
- 3SUM O(n²) 필수
- APSP O(n³) 필수

이들은 P 내부의 "하위 경계" 를 위한 별도 가설 기반 분류. P vs NP 와 독립된 결과.

---

## 13. 추가 논제 — Quantum Complexity 개관

양자 컴퓨터의 복잡도 클래스 BQP. 다음 관계 알려져 있음:

- P ⊆ BPP ⊆ BQP ⊆ PSPACE
- Shor 알고리즘: factoring ∈ BQP (NP 로 믿어지지만 NP-complete 아님)
- BQP vs NP 관계 미결 (양방향 분리 없음)

P1 범위 밖이지만 P vs NP 논의와 직접 연결되므로 간단히 메모.

---

## 14. 부록 — PCP 정리 (참고)

### 14.1 PCP 정리 진술 (Arora-Safra, Arora-Lund-Motwani-Sudan-Szegedy 1992)

```
  NP = PCP[O(log n), O(1)]
```

즉 NP 문제의 "증거" 는 O(log n) 비트 무작위 선택 + O(1) 비트 조회만으로 확률적으로 검증
가능하다. 혁명적 정리.

### 14.2 Hardness of approximation

PCP 정리의 귀결: 많은 최적화 문제의 근사 알고리즘 하계. 예: MAX-3SAT 의 8/7 근사가 NP-hard
(Håstad 2001).

### 14.3 UGC — Unique Games Conjecture

Khot 2002 의 Unique Games Conjecture: Vertex Cover 의 2-ε 근사 NP-hard. 많은 근사 하계가
UGC 에 의존.

---

## 15. 부록 — 주요 복잡도 클래스 도표

| 클래스 | 정의 | 완전문제 대표 | 포함 |
|-------|------|---------------|------|
| L | log-space | - | P |
| NL | log-space 비결정 | s-t reachability | NP |
| P | 다항시간 결정 | circuit value | NP |
| NP | 다항시간 비결정 | SAT | PSPACE |
| coNP | NP 여집합 | TAUTOLOGY | PSPACE |
| BPP | 다항시간 확률 | - | PSPACE |
| PSPACE | 다항공간 | TQBF | EXP |
| EXP | exp(poly) 시간 | - | NEXP |

---

## 16. 다음 문서

- PROB-P1-2 : BT-542 P vs NP 심화 (본 노트 기초 활용)
- PROB-P1-5 : BT-545 Hodge 심화
- N6-P1-3 : n=6 정직성 원칙

본 문서 완료로 P1-PURE 트랙이 마무리된다. P1-PROB 트랙 심화 (BT-543~547) 로 진입한다.
