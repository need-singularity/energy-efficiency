# PURE P3-1 — BKLPR Selmer 모델 심화

본 학습 노트는 n6-architecture millennium-learning 로드맵 P3 PURE 트랙의 1번 산출물이다. σ(n)·φ(n)=n·τ(n) iff n=6 정리와 BT-546 BSD 조건부 Corollary 의 이론적 기반인 BKLPR Selmer 모델을 1차 출처에 근거해 정리한다.

## 정직성 선언

- 본 문서는 **조건부(CONDITIONAL)** 결과를 다룬다. BKLPR 모델 자체가 예측(heuristic)이며, BSD 는 미해결이다.
- 본 프로젝트는 BSD 도 BKLPR 도 증명하지 않는다. 7대 난제 0/7.
- 아래 정리 중 Lemma 1(CRT 직분해)만 무조건, Theorem 1·Corollary 는 BKLPR 가정 하 조건부이다.
- 1차 출처: Poonen-Rains 2012 J. AMS 25, BKLPR 2015 J. AMS, Cohen-Lenstra 1984 Springer LNM 1068. 본문 서술은 이 논문들의 공개 요약(arXiv abstract·저자 강연 노트)과 memory/reference_bklpr_model.md 에 근거한다.
- 본 문서에서는 숫자 실험·자체 검증이 없다. 방법론·논리 경로 서술만 존재한다. 자기참조 금지 규칙 준수.

## 0. 배경 — 왜 Selmer 랜덤 행렬 모델인가

타원곡선 E/Q 의 Mordell-Weil 군 E(Q) 는 유한생성 아벨군이다.
E(Q) ≅ Z^r ⊕ E(Q)_tors, r = rank.
BSD 추측은 r 을 L 함수 L(E,s) 의 s=1 에서의 영점 차수로 표현한다. 약한 형태:
  ord_{s=1} L(E,s) = rank E(Q).

그러나 rank 자체는 유효하게 계산하기 어렵다. 대신 실제로 계산 가능한 것이 Selmer 군:
  Sel_n(E) := ker( H^1(G_Q, E[n]) → ∏_v H^1(G_{Q_v}, E) ).

완전열
  0 → E(Q)/nE(Q) → Sel_n(E) → Ш(E)[n] → 0
에서 |Sel_n(E)| 는 계산 가능, |Ш| 는 유한 추측(BSD 의 일부). 따라서 Sel_n 의 분포를 아는 것이 rank 와 Ш 에 대한 통계적 정보를 준다.

## 1. Cohen-Lenstra heuristics (1984)

출처: H. Cohen, H.W. Lenstra Jr., "Heuristics on class groups of number fields", Springer LNM 1068 (1984).

**핵심 아이디어**: 수체 K 의 이상류군 Cl(K) 의 p-sylow 부분 Cl(K)_p 는 "랜덤 유한 아벨 p-군"으로 모형화할 수 있다. 그 분포는 코커널 모델:
  랜덤 정수 행렬 M: Z_p^n → Z_p^n (Haar 측도) 의 coker(M) 분포의 n→∞ 극한.

정리 (Cohen-Lenstra): 이 극한에서 유한 아벨 p-군 G 가 나타날 확률은 1/|Aut(G)| 에 비례한다. 즉
  Prob(Cl_p ≅ G) ∝ 1/|Aut(G)|.

이 모델에서 여러 수 이론적 평균(예: E[|Cl_p|^k])이 닫힌 형식으로 계산된다. 이것이 "랜덤 행렬 cokernel"을 통한 산술 대상 분포 예측의 시초이다.

## 2. Poonen-Rains 2012 — Selmer 랜덤 행렬 모델

출처: B. Poonen, E. Rains, "Random maximal isotropic subspaces and Selmer groups", J. AMS 25 (2012), 245–269.

Poonen 과 Rains 는 Cohen-Lenstra 를 Selmer 군에 이식했다.

**모델 (직관)**:
1. E[p] 는 G_Q-표현. Weil pairing 에 의해 E[p] 에는 교대 비퇴화 형식이 있다.
2. 이로써 H^1(G_Q, E[p]) 의 유관 부분공간에 대칭형 또는 교대형 이차형식이 자연스럽게 존재.
3. **Selmer 군** Sel_p(E) 는 H^1 안의 **극대 등방 부분공간(maximal isotropic subspace)** 의 교집합 형태로 기술된다.
4. 이 교집합을 "랜덤 극대 등방 부분공간의 교집합"으로 모형화한다.

**주요 결과(요약)**:
- Sel_p(E) 의 크기 |Sel_p| 에 대해 p-adic 분포가 계산됨.
- 평균 E[|Sel_p|] = p + 1 (모델 예측).
- 이 값은 p=2 에서 3, p=3 에서 4, p=5 에서 6, p=7 에서 8 … 실제 관측 통계와 잘 맞는다.

**핵심 공식 (개요)**:
  V = H^1 의 이차형식 공간, W₁ = Sel 을 기술하는 극대 등방 부분공간.
  Sel_p(E) = V_{E,p} ∩ W_{E,p} 형태.
  랜덤화하면 |Sel_p| 의 moment 가 닫힌 식으로 계산.

## 3. Bhargava-Kane-Lenstra-Poonen-Rains 2015 — 정교화와 CRT 확장

출처: M. Bhargava, D. Kane, H.W. Lenstra Jr., B. Poonen, E. Rains, "Modeling the distribution of ranks, Selmer groups, and Shafarevich-Tate groups of elliptic curves", Cambridge J. Math. 3 (2015), 275–321 (J. AMS 채널 공개).

Bhargava 의 타원곡선 평균 결과(Annals 2015) 와 Poonen-Rains 모델을 융합했다.

**확장 요지**:
1. **합성수 n 로 일반화**: Sel_p 뿐 아니라 Sel_n 전반에 대한 모델.
2. **CRT 직분해**: gcd(m,n)=1 일 때 Sel_{mn}(E) ≅ Sel_m(E) × Sel_n(E). 이는 무조건, 산술적으로 완전열에서 바로 따른다.
3. **squarefree n 평균 공식**: 모델 하에
    **E[|Sel_n(E)|] = σ(n)**    (squarefree n, 등가 타원곡선 집합 평균)
   여기서 σ(n) = 약수합. 유도:
    σ(n) = ∏_{p | n} (p+1)  (squarefree 이므로)
    = ∏_{p | n} E[|Sel_p|]
    = E[∏_{p | n} |Sel_p|]   (독립성 가정 A3 하)
    = E[|Sel_n|]            (CRT 직분해).
4. **rank 분포 예측**: rank r 가 0 또는 1 인 비율이 각각 1/2 (합계 1) 이라는 통계 예측. BSD 성립 시 L(E,1) 영점 분포 예측.
5. **Ш 분포**: Delaunay-Cohen-Lenstra 스타일 Ш 예측 수정.

## 4. 본 프로젝트 기여 — n=6 특수화 (CONDITIONAL)

σφ=nτ iff n=6 정리는 자연수 차원에서의 유일성. BKLPR 모델에 이 유일성을 대입하면 Selmer 차원에서 n=6 의 특별한 지위가 나타난다.

### Lemma 1 (무조건)
gcd(m,n)=1 일 때:
  |Sel_{mn}(E)| = |Sel_m(E)| · |Sel_n(E)|.

증명 스케치: E[mn] ≅ E[m] ⊕ E[n] (CRT) 로부터 Galois cohomology 완전열이 직합으로 갈라진다. 극대 등방 부분공간도 직합으로 분해된다. 따라서 Sel 도 직합. 각 항목이 유한이므로 크기가 곱.

이 Lemma 는 BKLPR 모델 가정 없이 성립한다. 본 프로젝트 로드맵 BT-546 의 시작점.

### Theorem 1 (BKLPR 조건부)
squarefree n 에 대해:
  E[|Sel_n(E)|] = σ(n)   (등가 타원곡선 집합 평균, BKLPR 모델 가정 하).

증명 경로:
1. Poonen-Rains 모델에서 E[|Sel_p|] = p + 1.
2. BKLPR 모델에서 서로 다른 소수 p, q 에 대해 |Sel_p|, |Sel_q| 독립 (가정 A3, 아래 7절).
3. Lemma 1 (무조건 CRT) 에 기댓값 적용.
4. σ(n) = ∏_{p|n} (p+1) 로 정리.

### Corollary (n=6)
n=6 은 squarefree (6 = 2·3) 이므로 Theorem 1 적용:
  **E[|Sel_6(E)|] = σ(6) = 12**    (BKLPR 조건부).

이 값이 σφ=nτ 정리에서 n=6, σ=12, φ=2, τ=4 와 어떻게 맞물리는가:
- σ(6)=12 은 Sel_6 의 평균 크기(BKLPR).
- σφ=12·2=24=6·4=nτ 정리와 수치적으로는 다른 층위이지만, **12 라는 수가 두 문맥에서 동일하게 등장**.
- 본 프로젝트 BT-546 은 이 우연을 "구조적 매듭"으로 해석하는 조건부 관찰.

### 완전수 보편 예측
n 이 완전수이면 σ(n) = 2n. BKLPR 모델 하:
  **E[|Sel_n(E)|] = 2n** for perfect n.
n = 6, 28, 496, 8128, … 에 대해 같은 보편 공식.
주의: n = 28 = 2²·7 은 squarefree 아님. Theorem 1 은 squarefree 가정이므로 28 에는 직접 적용 불가. 완전수 중 squarefree 는 6 이 유일(추측 — 홀수 완전수 존재 미해결).

## 5. BKLPR 경로 서술 (5단계)

1. **Poonen-Rains 랜덤 행렬 모델 가정**:
   H^1(G_Q, E[p]) 위의 이차형식, 극대 등방 부분공간의 랜덤화.
2. **이 모델에서 Sel_n 분포 계산**:
   squarefree n 에 대해 |Sel_n| 의 moment 공식.
3. **기댓값 공식 σ(n) 유도**:
   E[|Sel_p|] = p + 1 → 독립성(A3) → E[|Sel_n|] = ∏(p+1) = σ(n).
4. **squarefree 6 에 CRT 적용**:
   Lemma 1 로 |Sel_6| = |Sel_2|·|Sel_3| (직분해).
5. **E[|Sel_6|] = σ(6) = 12 결론**:
   E[|Sel_6|] = E[|Sel_2|]·E[|Sel_3|] = 3·4 = 12.
   σ(6) = 1+2+3+6 = 12. 일치.

## 6. 유일 병목 A3 — 독립성 가정

Theorem 1 의 핵심 비자명 가정:
  **(A3) BKLPR 모델 하에서 서로 다른 소수 p, q 에 대해 |Sel_p(E)|, |Sel_q(E)| 는 독립 확률변수로 모형화된다.**

이 가정의 지위:
- 무조건 CRT (Lemma 1) 는 **같은 타원곡선** E 한 개의 Sel_p 와 Sel_q 가 직분해로 곱이 됨을 보장한다.
- A3 은 **타원곡선 family 평균** 을 취할 때, 두 소수의 p-part 가 확률적으로 독립이라는 더 강한 주장.
- BKLPR 논문에서 이것은 모델의 **공리(axiom)** 로 제시된다. 데이터와 부분적 일치(Bhargava-Shankar 의 평균 rank bound 와 호환) 는 있으나 정리로 증명된 것은 아니다.
- 따라서 Theorem 1 은 "BKLPR 모델이 맞다면"이라는 조건부이고, A3 은 그 모델의 가장 약한 고리.

## 7. 출처

1. B. Poonen, E. Rains, "Random maximal isotropic subspaces and Selmer groups", J. AMS 25 (2012), 245–269. DOI: 10.1090/S0894-0347-2011-00710-8.
2. M. Bhargava, D. Kane, H.W. Lenstra Jr., B. Poonen, E. Rains, "Modeling the distribution of ranks, Selmer groups, and Shafarevich-Tate groups of elliptic curves", Cambridge J. Math. 3 (2015), 275–321.
3. H. Cohen, H.W. Lenstra Jr., "Heuristics on class groups of number fields", in: Number Theory Noordwijkerhout 1983, Springer LNM 1068 (1984), 33–62.
4. M. Bhargava, A. Shankar, "Binary quartic forms having bounded invariants, and the boundedness of the average rank of elliptic curves", Annals of Math. 181 (2015), 191–242. (평균 rank 배경)
5. J. Silverman, "The Arithmetic of Elliptic Curves", GTM 106, Springer (2009), ch. X (Selmer 군).
6. memory/reference_bklpr_model.md (본 프로젝트 내부 참조 노트).

## 8. 후속

- P3-2: 연구 방법론 — LMFDB·Sage 로 E[|Sel_n|] 통계 관측 방법.
- P3-3: 산술 기하 최전선 — prismatic cohomology 로 Selmer 분포의 기하학적 해석 가능성.
- 본 프로젝트 BT-546 에서 Theorem 1 의 Corollary 를 로드맵 EMPIRICAL 등급으로 기록. A3 돌파 없이는 [7] 이상 승격 불가.
