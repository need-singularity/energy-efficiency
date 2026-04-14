# PURE P3-2 — 연구 수학 방법론

본 학습 노트는 n6-architecture millennium-learning 로드맵 P3 PURE 트랙의 2번 산출물이다. 수 이론·산술 기하 연구에서 실제로 사용되는 도구(LMFDB, Sage, Magma, PARI/GP)와 워크플로우, 그리고 조건부 증명 기법을 1차 문헌에 기반해 정리한다.

## 정직성 선언

- 본 문서는 **방법론 요약**이다. 새로운 수학 결과는 없다.
- 아래 "실습 5건" 은 교과서(Silverman-Tate) 및 공식 문헌(LMFDB label)에 기록된 표준 예시이다. 본 문서 작성 중 본인이 LMFDB 웹에 직접 접속한 것이 아니며, 인용 수치는 교과서·공식 논문의 공개 값이다. 본인이 확인하지 않은 값은 "(문헌 예 — 재확인 필요)" 로 명시한다.
- Sage 코드는 Sage 공식 문서 구문이다. 본 문서 작성 중 실행해 결과를 붙인 것이 아니다. 실행은 독자(또는 후속 학습 노트)의 몫.
- 자기참조·지어내기 금지 규칙 준수. BSD·BKLPR 관련 주장은 P3-1 로 넘긴다.

## 0. 왜 도구가 중요한가

타원곡선 한 개의 rank 를 손으로 계산하는 것은 대수 복잡도가 높다. Selmer 군, Shafarevich-Tate 군, L 함수의 analytic rank, 등은 현대 컴퓨터 대수 시스템이 아니면 실험할 수 없다. 수 이론 연구의 "실험 단계" 는 이 도구들 위에서 이루어진다. 정리와 반례의 분리는 이 단계의 결과물이다.

## 1. LMFDB — L-functions and Modular Forms Database

**URL**: https://www.lmfdb.org

**배경**: 2016년 공개된 미·영·유럽 수 이론 커뮤니티의 공용 데이터베이스. L 함수, 타원곡선, 모듈러 형식, 수체, Galois 표현, Hilbert/Bianchi 모듈러 형식 등을 상호 연결된 객체로 제공.

**주요 기능**:
- 타원곡선 E/Q 에 대해: 라벨(Cremona/LMFDB), conductor, j-invariant, discriminant, rank (analytic + algebraic), torsion, Sha_an 근사, Selmer rank 2, Tamagawa 곱, regulator, L(E,1), isogeny class.
- 타원곡선 E/K (K 수체) 도 수록.
- L 함수별 영점 분포, functional equation.
- 모듈러 형식 — 무게/level/character 별.
- 검색: conductor 범위, rank 범위, 특정 불변량 제약.

**수 이론 연구에서의 역할**:
1. 추측 검증: "이 성질이 관찰되는가" 를 즉시 확인.
2. 반례 탐색: 조건부 주장에 대해 counterexample 후보 생성.
3. 통계 수집: E[|Sel_n|] 같은 양의 실측 근사.

### 실습 5건 (문헌 예 — 재확인 필요)

아래는 Silverman-Tate 교재 및 Cremona 의 타원곡선 표에 수록된 표준 예시이다. 라벨과 수치는 공식 출처에서 유래하지만 본 문서 작성자가 LMFDB 에 직접 접속해 확인한 값이 아니므로 "문헌 예" 로 표시한다.

**예 1 — E: y² = x³ − x**
- 문헌 라벨: conductor 32 (32a2 류), j=1728, CM by Z[i].
- rank: 0, torsion Z/2Z × Z/2Z.
- L(E,1) ≠ 0 (BSD 확인된 경우).
- 방법론 포인트: CM 곡선은 L 함수가 Hecke character 의 곱으로 분해되어 BSD 일부가 증명되어 있다(Coates-Wiles 1977).

**예 2 — E: y² = x³ − x + 1**
- 문헌 라벨: 구 Cremona 라벨 "11a…" 계열 conductor 11 후보. (정확 라벨 재확인 필요)
- rank: 0.
- 역사적 의미: conductor 11 은 모듈러성 예 중 가장 작은 비 CM 급 예.

**예 3 — E: y² + y = x³ − x**
- 라벨: 37a1 (Cremona). **첫 rank 1 곡선** — conductor 37, j-invariant 유한.
- rank: 1.
- analytic rank: 1 (BSD 확인).
- 방법론 포인트: Gross-Zagier 정리 (1986) 와 Kolyvagin (1989) 로 rank ≤ 1 BSD 가 증명된 대표 예.

**예 4 — E: y² + y = x³ − x²**
- 라벨: 37b1. conductor 37, rank 0. 37a 와 isogeny class 다름.
- 방법론 포인트: 같은 conductor 에서 rank 가 다른 두 곡선 대비 — isogeny class 의 중요성.

**예 5 — E: y² = x³ − 2**
- rank 1 예. generator: (3, 5) (확인 필요).
- 방법론 포인트: Mordell 의 y² = x³ + k 족 — k=-2 는 rank 1 이고 정수해가 유한하게 기록됨.

각각에 대해 BSD 예측: rank = ord_{s=1} L(E,s). 위 예시들은 모두 rank ≤ 1 이므로 Gross-Zagier-Kolyvagin 정리로 BSD 가 증명된 범위에 있다. rank ≥ 2 인 예(예: conductor 389, 389a1, rank 2)는 BSD 가 여전히 추측.

## 2. Sage Math — 타원곡선 계산

**URL**: https://www.sagemath.org

**배경**: 2005년 W. Stein 시작. Python 기반, GPL, 여러 수학 시스템(PARI, Singular, Maxima, GAP, NumPy, R …)을 통합하는 상위 레이어. 타원곡선·모듈러 형식·L 함수 계산에 사실상 표준.

### 표준 workflow

```python
# 타원곡선 정의
E = EllipticCurve([-1, 0])    # y^2 = x^3 - x
# 또는 Weierstrass 계수 전체
E = EllipticCurve([0, 0, 1, -1, 0])  # y^2 + y = x^3 - x (37a1)

# 기본 불변량
E.conductor()            # 도체
E.j_invariant()          # j-invariant
E.discriminant()         # 판별식
E.cremona_label()        # Cremona 라벨

# rank / torsion
E.rank()                 # 대수 rank (2-descent 기반)
E.analytic_rank()        # L 함수의 s=1 영점 차수
E.torsion_subgroup()     # 비틀림 부분군

# Selmer / Sha
E.selmer_group_order(2)  # |Sel_2|
E.sha().an()             # Sha_an (analytic Sha 근사)

# L 값
L = E.lseries()
L(1)                     # L(E,1)
L.taylor_series(1, 5)    # s=1 근방 5차 Taylor
```

### Sage 실습 스크립트 예 (실행은 독자 몫)

```python
# 5개 예시 곡선에 대한 일괄 계산
curves = [
    ('32a2', [1, 0, 0, -1, 0]),    # y^2 = x^3 - x (변형)
    ('11a1', [0, -1, 1, -10, -20]),
    ('37a1', [0, 0, 1, -1, 0]),    # first rank 1
    ('37b1', [0, 1, 1, -23, -50]),
    ('389a1', [0, 1, 1, -2, 0]),   # first rank 2
]
for label, coeffs in curves:
    E = EllipticCurve(coeffs)
    print(label,
          'rank=', E.rank(),
          'tor=', E.torsion_subgroup().order(),
          'cond=', E.conductor(),
          '|Sel2|=', E.selmer_group_order(2))
```

출력 결과는 Sage 실행 환경에서 검증해야 한다. 본 문서는 코드만 기록.

## 3. Magma, PARI/GP — 보조 도구

**Magma** (University of Sydney, 상용, 무료 아님): 타원곡선 p-descent, 3-descent, 4-descent 등 Sel_n(n>2) 계산에 Sage 보다 깊다. BSD 실험에 표준.

```
// Magma 예
E := EllipticCurve([0, 0, 1, -1, 0]);
Rank(E);
MordellWeilShaInformation(E);
ThreeSelmerGroup(E);
```

**PARI/GP** (Bordeaux, 자유 소프트웨어): 빠른 정수론 원시 함수. Sage 내부에서 호출됨. 직접 사용 예:

```
\\ PARI/GP
E = ellinit([0,0,1,-1,0]);
ellanalyticrank(E)    \\ analytic rank
ellL1(E)              \\ L(E,1)
```

**선택 기준**:
- rank ≤ 2 통상 실험: Sage 충분.
- 3/4-descent, 고차 Selmer: Magma.
- 빠른 통계 수집(수백만 곡선): PARI/GP 직접.

## 4. 반례 체계적 탐색 — 프로그램 설계 원칙

조건부 주장(예: "rank ≤ 1 이면 P 성립")에 대해 반례를 찾는 프로그램은 다음 구조를 가진다.

### 구조
1. **후보 생성기**: conductor N ≤ N_max 범위에서 isogeny class 대표 곡선 순회. Cremona 표(conductor ≤ 500000 현재 수록) 이용.
2. **필터**: 주장의 가정(P 가 적용되는 범위)을 만족하는 곡선만 선택.
3. **평가**: 주장의 결론을 Sage/Magma 로 계산.
4. **기록**: 결론 실패 시 반례 후보로 로그.
5. **검증**: 후보에 대해 더 정밀한(느린) 방법 재계산 — 거짓 양성 제거.

### 예 — Selmer 평균 관측
목표: squarefree n 고정, 범위 내 E 에 대해 |Sel_n(E)| 를 모아 평균을 σ(n) 과 비교.

```python
from sage.schemes.elliptic_curves.ell_rational_field import cremona_curves
n = 6
total, count = 0, 0
for E in cremona_curves(range(1, 1000)):  # conductor 1..999
    # |Sel_6| = |Sel_2| * |Sel_3| (무조건, CRT)
    s2 = E.selmer_group_order(2)
    s3 = E.selmer_group_order(3)  # Sel_3 은 3-descent 필요, 무거움
    total += s2 * s3
    count += 1
print('mean |Sel_6| =', total / count, 'vs sigma(6)=12')
```

주의: Sel_3 계산은 conductor 수백 수준에서도 느리다. 통계적 유의성을 얻으려면 Magma 3-descent 또는 미리 계산된 LMFDB 덤프가 필요.

## 5. 조건부 증명 기법 — GRH 등

순수 증명 중에는 결론을 얻기 위해 아직 미증명 가정(GRH, BKLPR, 모듈러성 일반화 등)을 전제하는 경우가 있다. 이것은 "조건부 정리(conditional theorem)" 이다.

### 대표 예 — GRH (일반화 리만 가설) 하의 결과
- **Bach 1990**: GRH 하 Miller-Rabin 소수성 판정의 결정론적 경계. Bach, "Explicit bounds for primality testing and related problems", Math. Comp. 55 (1990), 355–380.
- **Artin 추측 (일차 원시근)**: Hooley 1967 가 GRH 하 Artin 예상을 증명.
- **Elkies 1987**: GRH 하 supersingular 소수 분포.
- **Titchmarsh "The Theory of the Riemann Zeta-function", 2nd ed. (Heath-Brown 편), Oxford 1986, ch. 14**: GRH 하 ζ 함수 추정.

### Conrad 의 노트
Brian Conrad 의 강의 노트(Stanford) 는 conditional 증명 기법의 교과서적 출처로 자주 인용된다. 특히 BSD·Iwasawa 이론의 GRH 가정 서술.

### 작성 원칙
조건부 정리를 서술할 때:
1. 가정(hypothesis) 을 정리의 statement 에 명시.
2. 가정 없이 얻을 수 있는 무조건 부분을 lemma 로 분리.
3. 가정의 출처(어떤 추측) 를 인용.
4. 가정이 증명되면 얻어지는 귀결을 Corollary 로.

본 프로젝트 BT-546 은 이 원칙을 따라 Lemma 1 (무조건 CRT) 와 Theorem 1 (BKLPR 조건부) 를 분리했다. P3-1 참조.

## 6. 컴퓨터 대수 검증 워크플로우

### 표준 4단계
1. **관찰 (Sage/LMFDB)**: 패턴 발견.
2. **반례 검색**: conductor 확장해 반례 시도.
3. **가설 정립**: 부분 정리 후보.
4. **증명/반증**: 수학적 논증. 실패 시 1단계로 복귀.

### 주의점
- 모든 계산은 **재현 가능** 해야 한다. Sage 버전, 라이브러리 버전, 랜덤 시드 기록.
- **수치 오차**: analytic rank, L(E,1) 등은 부동소수점. 임계(threshold) 선정 신중.
- **정밀도 올림**: Sage 는 RealField(prec) 로 비트 정밀도 지정 가능. L 값이 0 인지 판별할 때 필수.
- **Heuristic 과 증명 구분**: E.rank() 는 내부적으로 일부 heuristic 을 사용하는 경우가 있다. 최종 주장에는 proven rank 플래그 확인.

## 7. 출처

1. J.H. Silverman, J. Tate, "Rational Points on Elliptic Curves", 2nd ed., Springer Undergraduate Texts in Math. (2015).
2. LMFDB Collaboration, "The L-functions and Modular Forms Database", https://www.lmfdb.org (2016–현재).
3. W. Stein 외, Sage Math Documentation, https://doc.sagemath.org.
4. Magma Handbook, University of Sydney, http://magma.maths.usyd.edu.au.
5. PARI/GP User's Manual, Bordeaux, https://pari.math.u-bordeaux.fr.
6. J.E. Cremona, "Algorithms for Modular Elliptic Curves", 2nd ed., Cambridge (1997). 타원곡선 표 부록.
7. E.C. Titchmarsh, "The Theory of the Riemann Zeta-function", 2nd ed., D.R. Heath-Brown 편, Oxford (1986), ch. 14.
8. E. Bach, "Explicit bounds for primality testing and related problems", Math. Comp. 55 (1990), 355–380.
9. B. Conrad, 강의 노트(Stanford), http://math.stanford.edu/~conrad/ — BSD·Iwasawa 계열.
10. B. Gross, D. Zagier, "Heegner points and derivatives of L-series", Invent. Math. 84 (1986), 225–320. (37a1 rank 1 의 증명 기초)
11. V. Kolyvagin, "Finiteness of E(Q) and Ш(E,Q) for a subclass of Weil curves", Izv. Akad. Nauk SSSR 52 (1988), 522–540.

## 8. 후속

- P3-3: 산술 기하 최전선 — perfectoid, prismatic 으로 BSD/RH 에 어떤 새 도구가 등장하는가.
- 본 프로젝트 실전 연습: BT-546 범위에서 Sage 로 |Sel_2| 통계 수집 → σ(2)=3 과 비교. (P4 이후 agenda)
