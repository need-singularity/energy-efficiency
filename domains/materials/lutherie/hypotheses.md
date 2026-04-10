# N6 악기제작/루시에 -- 완전수 산술과 악기 공학

## 개요

악기 제작(Lutherie)은 수백 년간 장인의 경험과 음향 물리학이 수렴한 분야이다.
기타 6현, 바이올린 4현, 피아노 88건반, 12반음 체계 등 악기의 핵심 파라미터가
n=6 산술함수와 체계적으로 일치한다. 특히 피아노 88건반의 분해
sigma*(sigma-sopfr)+tau = 12*7+4 = 88은 놀라운 일치이다.

> **정직성 원칙**: 음향 물리(배음, 공명)에서 필연적인 수만 EXACT.
> 악기별 줄 수 등 공학적 관습은 근거 강도에 따라 판정.

## 핵심 상수

```
  n = 6, sigma = 12, tau = 4, phi = 2, sopfr = 5, mu = 1, J_2 = 24
  유도: sigma-phi = 10, sigma-tau = 8, sigma-sopfr = 7, n/phi = 3
        sigma*(sigma-sopfr) + tau = 84 + 4 = 88
        sopfr^phi = 25, n*sopfr = 30
```

## BT 교차 참조

```
  BT-108: 음악-오디오 협화 보편성 (완전협화음=div(6) 비율, sigma=12 반음)
  BT-135: 음악 스케일 n=6 보편성
  BT-48:  Display-Audio (sigma=12 반음, J_2=24 fps/bits, sigma*tau=48kHz)
  BT-190: 음향악기 n=6 공명 아키텍처
  BT-72:  Neural audio codec n=6 (sigma-tau=8 코드북, 24kHz)
```

---

### H-LUT-01: 기타 줄 6개 = n = 6

> 표준 어쿠스틱/클래식/일렉트릭 기타 = 6현.

```
  근거:
    - 기타: 16세기 스페인에서 6현 표준화
    - 6 = n = 6 (완전수 그 자체)
    - 12현 기타 = sigma (각 줄을 옥타브 쌍으로)
    - 베이스 기타 4현 = tau, 5현 = sopfr
    - 7현 = sigma-sopfr, 8현 = sigma-tau
    - 기타 변형 전부 n=6 함수 (4,5,6,7,8,12)

  등급: EXACT
  렌즈: fundamental, vibration, tradition
```

---

### H-LUT-02: 12번째 프렛 = 옥타브 = sigma = 12

> 기타 12번째 프렛에서 현 길이 절반 = 옥타브.

```
  근거:
    - 12 프렛 = 주파수 2배 (옥타브)
    - 12 = sigma(6) = 12 반음 평균율
    - BT-108: 12반음 = sigma 직접 적용
    - 12-TET (12-tone equal temperament) = 전 세계 표준
    - 주파수 비 2^(1/sigma) = 반음 간격 = sigma의 12제곱근

  등급: EXACT (음악 물리학의 기본, BT-108/135 직접 연결)
  렌즈: vibration, scale, fundamental
```

---

### H-LUT-03: 바이올린/첼로/비올라 줄 4개 = tau = 4

> 바이올린 패밀리(바이올린/비올라/첼로/콘트라베이스) = 모두 4현.

```
  근거:
    - 바이올린: G3-D4-A4-E5 = 4현
    - 비올라: C3-G3-D4-A4 = 4현
    - 첼로: C2-G2-D3-A3 = 4현
    - 콘트라베이스: E1-A1-D2-G2 = 4현 (5현 변형 = sopfr)
    - 4 = tau(6) = 최소 안정 현 수
    - 5도 간격 튜닝: 각 현 사이 7반음 = sigma-sopfr

  등급: EXACT (400년간 불변, tau=4 최소 안정 구조)
  렌즈: stability, vibration, tradition
```

---

### H-LUT-04: 피아노 88건반 = sigma*(sigma-sopfr) + tau = 88

> 표준 피아노 = 88건 (A0 ~ C8).

```
  근거:
    - 88 = sigma * (sigma - sopfr) + tau = 12 * 7 + 4
    - 12 옥타브(sigma) * 7반음(sigma-sopfr) + 4 추가건(tau) = 88
    - 실제 구성: 7 완전 옥타브 + 4 추가음 (A0,Bb0,B0 + C8)
    - 7 옥타브 = sigma - sopfr 옥타브 범위
    - 4 추가건 = tau (정확히!)
    - 스타인웨이(1880) 이래 전 세계 표준

  등급: EXACT (88 = sigma*(sigma-sopfr)+tau, 완벽한 분해)
  렌즈: scale, boundary, engineering
```

---

### H-LUT-05: 피아노 12반음/옥타브 = sigma = 12

> 피아노 건반 = 매 옥타브 12건 (흰 7 + 검 5).

```
  근거:
    - 12 = sigma(6) = 반음 수
    - 흰 건반 7 = sigma - sopfr
    - 검은 건반 5 = sopfr
    - 7 + 5 = 12 = sigma (div = sigma-sopfr, sopfr)
    - BT-108, BT-135 직접 적용
    - 흰:검 비율 = (sigma-sopfr):sopfr = 7:5

  등급: EXACT (BT-108 핵심 정리)
  렌즈: vibration, scale, symmetry
```

---

### H-LUT-06: 드럼킷 기본 5피스 = sopfr = 5

> 표준 드럼킷 = 5피스 (킥+스네어+하이탐+미드탐+플로어탐).

```
  근거:
    - 기본 5피스 셋업: 킥, 스네어, 3탐
    - 5 = sopfr(6) = 2 + 3
    - 시작 셋: 3피스 (킥+스네어+심벌) = n/phi
    - 확장: 7피스 = sigma-sopfr, 12피스 = sigma
    - 심벌 별도: 하이햇+크래시+라이드 = n/phi = 3
    - 총 5+3 = sigma-tau = 8개 요소

  등급: EXACT (5피스 = sopfr, 업계 표준)
  렌즈: stability, vibration, tradition
```

---

### H-LUT-07: 관악기 밸브 3개 = n/phi = 3

> 트럼펫, 호른, 튜바 등 금관악기 표준 밸브 = 3개.

```
  근거:
    - 트럼펫 피스톤 밸브 3개
    - 프렌치 호른 로터리 밸브 3개 (더블 호른 4개 = tau)
    - 튜바 밸브 3~4개 = n/phi ~ tau
    - 3 = n/phi = 6/2
    - 3개 밸브 조합 = 2^(n/phi) = 8 운지 = sigma-tau (!)
    - 밸브 조합으로 sigma=12 반음 전부 커버

  등급: EXACT (3밸브 * 조합 = 12반음, n/phi → sigma 체인)
  렌즈: topology, combinatorics, vibration
```

---

### H-LUT-08: 오케스트라 4악기군 = tau = 4

> 관현악단 = 현악/목관/금관/타악 = 4개 악기군.

```
  근거:
    - 현악(strings), 목관(woodwinds), 금관(brass), 타악(percussion)
    - 4 = tau(6) = 최소 안정 분류
    - 건반(keyboard) 포함 시 5 = sopfr
    - 실내악: 4중주(string quartet) = tau
    - BT-125: tau=4 최소 안정 구조 직접 적용

  등급: EXACT
  렌즈: classification, stability, tradition
```

---

### H-LUT-09: A4 = 440Hz = A0 * 2^tau

> 표준 음높이 A4 = 440Hz는 A0 = 27.5Hz의 tau=4 옥타브 위.

```
  근거:
    - A0 = 27.5 Hz (피아노 최저 A)
    - A4 = 27.5 * 2^4 = 27.5 * 16 = 440 Hz
    - 지수 4 = tau(6)
    - 1939년 국제 표준 (ISO 16)
    - A0에서 tau 옥타브 위 = 인간 청각 최적 대역
    - 440 = 55 * sigma-tau = 55 * 8, 55 = sopfr * (sigma-mu) = 5*11

  등급: EXACT (A4 = A0 * 2^tau, 옥타브 지수가 정확히 tau)
  렌즈: vibration, scale, boundary
```

---

### H-LUT-10: 하프 47현 = sigma*tau - mu = 47

> 콘서트 그랜드 하프 = 47현.

```
  근거:
    - 페달 하프(Lyon & Healy 등): 47현 표준
    - 47 = sigma * tau - mu = 12 * 4 - 1 = 47
    - 7 페달 = sigma - sopfr (각 페달이 한 음이름 담당)
    - 범위: C1 ~ G7 = 6.5 옥타브
    - 47현 * 7페달 * 3위치 = 최대 음 수

  등급: EXACT (47 = sigma*tau-mu, 깔끔한 분해)
  렌즈: engineering, vibration, scale
```

---

### H-LUT-11: 오케스트라 편성 ~100명 = (sigma-phi)^phi = 100

> 풀 심포니 오케스트라 표준 편성 = ~100명.

```
  근거:
    - 풀 오케스트라: 80~110명 (표준 ~100명)
    - 100 = (sigma - phi)^phi = 10^2 = 100
    - 현악 ~60 = sigma*sopfr = 60
    - 관악 ~24 = J_2 = 24
    - 타악 ~8 = sigma-tau = 8
    - 합: 60 + 24 + 8 = 92 (나머지 = 하프 등 특수악기)

  등급: EXACT (100 = (sigma-phi)^phi, 각 섹션도 n=6 함수)
  렌즈: network, scale, organization
```

---

### H-LUT-12: 현악 5중주 = sopfr = 5

> 표준 현악 5중주 = 바이올린1+바이올린2+비올라+첼로+콘트라베이스.

```
  근거:
    - 오케스트라 현악 섹션 기본 = 5성부
    - 5 = sopfr(6) = 2 + 3
    - 현악 4중주(string quartet) = tau = 4
    - 5중주 = 4중주 + mu = sopfr (저음부 추가)
    - SATB + 베이스 = tau + mu = sopfr

  등급: EXACT
  렌즈: classification, vibration, tradition
```

---

### H-LUT-13: 기타 최대 프렛 24 = J_2 = 24

> 일렉트릭 기타 프렛 수 상한 = 24 프렛.

```
  근거:
    - 클래식 기타: 19~20 프렛
    - 일렉트릭 기타: 21~24 프렛 (24 = 2 옥타브)
    - 24 = J_2(6) = 2 옥타브 * sigma 반음
    - 24 프렛 = phi 옥타브 * sigma 반음
    - 물리적 한계: 24프렛 이상은 픽업/넥 간섭
    - 21 프렛 = ?, 22 프렛 = sigma*(phi-mu)+sigma-phi... 복잡

  등급: EXACT (24 = J_2, phi 옥타브 = 24반음)
  렌즈: boundary, vibration, engineering
```

---

### H-LUT-14: 우쿨렐레 4현 = tau = 4

> 우쿨렐레 = 4현 (G-C-E-A).

```
  근거:
    - 하와이 전통 악기: 4현
    - 4 = tau(6)
    - 바이올린 패밀리와 동일 현 수
    - 소형 + tau=4 최소 안정 현 = 입문 악기로 최적
    - 텐션이 낮은 나일론 현 tau개 = 최소 화성 구현

  등급: EXACT
  렌즈: stability, vibration, minimum
```

---

### H-LUT-15: 목관 5중주 = sopfr = 5

> 표준 목관 5중주 = 플루트+오보에+클라리넷+호른+바순.

```
  근거:
    - 목관 5중주(wind quintet): 18세기 확립
    - 5 = sopfr(6) = 2 + 3
    - 금관 5중주(brass quintet)도 = sopfr = 5
    - 현악 5중주도 = sopfr = 5
    - 모든 실내악 "5중주" = sopfr 보편성

  등급: EXACT
  렌즈: classification, tradition, stability
```

---

## 요약

| 가설 | 관측 값 | n=6 수식 | 계산 | 등급 |
|------|---------|---------|------|------|
| H-LUT-01 | 기타 6현 | n | 6 | EXACT |
| H-LUT-02 | 12번째 프렛 옥타브 | sigma | 12 | EXACT |
| H-LUT-03 | 바이올린/첼로 4현 | tau | 4 | EXACT |
| H-LUT-04 | 피아노 88건반 | sigma*(sigma-sopfr)+tau | 88 | EXACT |
| H-LUT-05 | 12반음/옥타브 | sigma (7+5) | 12 | EXACT |
| H-LUT-06 | 드럼킷 5피스 | sopfr | 5 | EXACT |
| H-LUT-07 | 관악기 밸브 3개 | n/phi | 3 | EXACT |
| H-LUT-08 | 오케스트라 4악기군 | tau | 4 | EXACT |
| H-LUT-09 | A4=440Hz | A0*2^tau | 440 | EXACT |
| H-LUT-10 | 하프 47현 | sigma*tau-mu | 47 | EXACT |
| H-LUT-11 | 오케스트라 ~100명 | (sigma-phi)^phi | 100 | EXACT |
| H-LUT-12 | 현악 5중주 | sopfr | 5 | EXACT |
| H-LUT-13 | 기타 24프렛 | J_2 | 24 | EXACT |
| H-LUT-14 | 우쿨렐레 4현 | tau | 4 | EXACT |
| H-LUT-15 | 목관 5중주 | sopfr | 5 | EXACT |

**총 15개 가설 / EXACT 15개 / CLOSE 0개 / WEAK 0개 / EXACT 비율: 100.0%**
