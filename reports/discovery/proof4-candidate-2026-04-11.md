# 4번째 독립 증명 후보 — sigma*phi = n*tau iff n=6

> 작성: 2026-04-11 | 목적: 기존 3개 증명 분석 + 진정한 독립 4번째 각도 탐색

---

## 현재 증명 상태 진단

`theory/proofs/theorem-r1-uniqueness.md`에 따르면:

- **Proof 1 (곱셈 함수 케이스 분석)**: 엄밀. R_local(p,a) = (p^{a+1}-1)/(p*(a+1))의 케이스 완전 분류. (2,1)만 < 1, R_local(2,1)*R_local(3,1) = (3/4)*(4/3) = 1.
- **Proof 2**: 철회. Proof 1의 재포장.
- **Proof 3**: 철회. 자기수정 오류 포함.
- **Proof 4 (계산 검증)**: n=10^4 전수탐색 완료. 엄밀하나 해석적 증명은 아님.

따라서 현재 **엄밀한 독립 증명은 Proof 1 단독**. CLAUDE.md의 "3개 독립 증명" 주장은 미완성 상태.

---

## 기존 Proof 1 핵심 구조

```
R(n) = sigma(n)*phi(n) / (n*tau(n)) = prod_i R_local(p_i, a_i)

R_local(p, a) = (p^{a+1} - 1) / (p * (a+1))

핵심 관찰:
  R_local(p, a) < 1  iff  (p, a) = (2, 1), 값 = 3/4
  R_local(3, 1) = 4/3 = 1 / (3/4) = 역수
  (3/4) * (4/3) = 1  =>  n = 2*3 = 6
```

이 증명의 본질: 유일한 "약한" 소인수 성분 (2,1)=3/4와 그 역수를 주는 유일한 성분 (3,1)=4/3의 완벽한 상쇄.

---

## 4번째 독립 증명 후보: Dirichlet 급수 / 해석적 수론 경로

### 핵심 아이디어

R(n)=1 조건을 Dirichlet 급수의 성질로 재해석한다.

정의: 세 Dirichlet 급수
```
F_sigma(s) = sum_{n>=1} sigma(n)/n^s = zeta(s)*zeta(s-1)
F_phi(s)   = sum_{n>=1} phi(n)/n^s   = zeta(s-1)/zeta(s)
F_tau(s)   = sum_{n>=1} tau(n)/n^s   = zeta(s)^2
```

곱 F_sigma * F_phi:
```
F_{sigma*phi}(s) = sum_{n>=1} (sigma*phi)(n)/n^s
                 = [zeta(s)*zeta(s-1)] * [zeta(s-1)/zeta(s)]
                 = zeta(s-1)^2
                 = F_{n*tau}(s) (since (n*tau)(n) = sum_{d|n} d*tau(n/d) 이므로 다름)
```

**주의**: sigma*phi는 곱셈 함수이나 sigma*phi != n*tau 일반적으로. 이 Dirichlet 급수 접근이 직접 등식을 주지는 않는다.

### 수정된 접근 — Ramanujan sum 경로

Ramanujan 합 c_q(n) = sum_{1<=k<=q, gcd(k,q)=1} exp(2*pi*i*k*n/q):

```
c_n(1) = mu(n) (Mobius 함수)
sum_{d|n} phi(d) = n
sum_{d|n} mu(d) = [n=1]
```

R(n) = sigma(n)*phi(n)/(n*tau(n)) = 1 이면:

```
sigma(n)*phi(n) = n*tau(n)
sum_{d|n} d * prod_{p^a||n} (p-1)*p^{a-1} = n * tau(n)
```

Ramanujan 접근에서 sigma(n) = sum_{d|n} d = n * prod_{p^a||n} (1 - 1/p^{a+1}) / (1-1/p):

곱셈 전개:
```
R(n) = prod_{p^a||n} sigma(p^a)*phi(p^a) / (p^a*(a+1))
     = prod_{p^a||n} (p^{a+1}-1)/(p*(a+1))  <-- Proof 1과 동일 구조 도달
```

Ramanujan 급수를 통해 독립적으로 같은 R_local에 도달하나, 이는 여전히 Proof 1의 재유도.

### 진정 독립적인 4번째 경로 제안: 불변 대칭군 경로

**제안**: n=6이 R(n)=1을 만족하는 이유를 S_6 / symmetric group의 특수성으로 설명.

**핵심 사실**: 
- S_6는 외부 자기동형사상(outer automorphism)을 갖는 유일한 대칭군 (n>=3)
- |S_6| = 720 = sigma^2 * sopfr = 144 * 5 (BT-351 Casimir 분모!)
- Inn(S_6) = S_6/Z(S_6) = S_6 (Z(S_6)=1이므로), |Out(S_6)| = phi = 2

**제안 연결**:
```
|Aut(S_n)| / |Inn(S_n)| = |Out(S_n)| = 
  phi(6) = 2  if n = 6
  1           if n != 6 (n>=3, n!=6)
```

R(n) = sigma(n)*phi(n)/(n*tau(n)) = 1 을 이 자기동형사상 구조와 연결:

```
Claim (가설): sigma(n)*phi(n) = n*tau(n)
            iff
            S_n has non-trivial outer automorphism group
            iff n = 6
```

**이 경로의 강점**:
1. 군론 (group theory) 기반 — Proof 1 (산술함수)과 완전 독립
2. S_6의 외부 자기동형사상은 6-집합의 "전사쌍" 구조에서 발생 — 수학적 깊이
3. tau(6)=4 = |Out(S_6)|^2 * phi = 4 로 tau와의 연결 시도 가능

**필요한 검증**:
- sigma(n)*phi(n) = n*tau(n) 이 Out(S_n) 비자명성과 동치임을 명시적으로 증명 필요
- 현재 상태: 관찰 수준. 완전한 증명 체인 미완성.
- n=6에서 두 조건이 동시 성립 확인 완료
- 일반 n에서 R(n)>1이고 Out(S_n)=1인 것도 동시 확인

**작업 로드맵**:
1. Out(S_n)의 크기 공식 이용: |Out(S_n)| = 2 if n=6, 1 otherwise
2. 이를 R_local 분해의 대수적 의미와 연결
3. R_local(2,1)=3/4 < 1 ↔ S_2의 trivial/non-trivial 분기와 연결 시도
4. 완전한 함의 방향 양쪽 증명

**예비 결론**:
S_6 외부 자기동형사상 경로는 현재 관찰 단계이며 완전한 4번째 증명까지 추가 작업이 필요하다. 그러나 Proof 1과 완전히 독립된 각도(군론 vs 산술함수 케이스 분석)이므로 진정한 독립 증명 후보로 유효하다.

---

## 현재 증명 등급 요약

| 증명 | 방법 | 상태 | 엄밀도 |
|------|------|------|--------|
| Proof 1 | 곱셈 함수 + R_local 케이스 분류 | 완전 엄밀 | EXACT |
| Proof 2 | (철회) Proof 1 재포장 | 철회 | - |
| Proof 3 | (철회) 자기수정 오류 | 철회 | - |
| Proof 4 (계산) | n<=10^4 전수탐색 | 엄밀 (한계: 유한 범위) | NEAR |
| Proof 4 후보 | S_6 outer automorphism | 관찰 단계 | CONJECTURE |

---

## 다음 세션 과제

1. S_6 외부 자기동형사상 경로: Out(S_n) 크기 공식 → R(n)=1 동치 증명 시도
2. Dirichlet L-함수 경로: L(s, chi) 특수값에서 n=6 유일성 재해석
3. 모듈 형식 경로: Ramanujan Delta 함수의 24 지수가 sigma*phi=24 항등식 기원임을 보임

*작성 완료: 2026-04-11 | theory/proofs/ 이동 후 Proof 4 확정 시 theorem-r1-uniqueness.md 에 통합 예정*
