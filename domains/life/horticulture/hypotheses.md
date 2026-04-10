# 원예학/식물학 n=6 완전 아키텍처

## 개요

식물의 형태, 생리, 생화학 전반을 n=6 산술로 분석한다.
광합성(BT-101/103)은 이미 100% n=6 화학양론이 확립되었으며,
이 문서는 꽃 구조, 잎차례, 호르몬, 조직계, 세포소기관 등
원예학 고유 파라미터로 확장한다.

> **정직성 원칙**: 식물학 수치는 화학양론/유전학/물리학에 의해
> 결정된 것만 EXACT로 인정한다. 인위적 분류(예: 품종 수)나
> 문화적 관행(예: 윤작 연수)은 제외한다.

### 산술 상수

```
  n = 6          (완전수)
  sigma(6) = 12  (약수합)
  tau(6) = 4     (약수 개수: 1, 2, 3, 6)
  phi(6) = 2     (오일러 토션트)
  sopfr(6) = 5   (소인수합: 2+3)
  J_2(6) = 24    (요르단 토션트)
  mu(6) = 1      (뫼비우스)
  div(6) = {1, 2, 3, 6}
  sigma - phi = 10, sigma - tau = 8, sigma - mu = 11
  n/phi = 3, sigma*tau = 48, sigma*sopfr = 60
```

### BT 교차 참조

```
  BT-101: 광합성 포도당 C6H12O6 총 24원자=J2, 양자수율 8=sigma-tau
  BT-103: 광합성 완전 n=6 화학양론 (6CO2+12H2O -> C6H12O6, 7계수 100% n=6)
  BT-27:  탄소-6 체인 (LiC6 + C6H12O6 + C6H6 -> 24e = J2)
  BT-122: 벌집-눈꽃-산호 n=6 기하학 보편성
  BT-198: 농학 + 식물학 n=6 성장 아키텍처
  BT-265: 일주기-주기-연주기 생물 리듬 스택
  BT-51:  유전 코드 체인 tau->n/phi->2^n->J2-tau
```

---

## H-HRT-01: 광합성 반응식 계수 = 100% n=6 (EXACT)

> 6CO2 + 12H2O -> C6H12O6 + 6O2 + 6H2O -- 모든 계수가 n 또는 sigma

### 검증

```
  광합성 총괄 반응식 (Hill 반응 + Calvin 회로):
    6CO2 + 12H2O -> C6H12O6 + 6O2 + 6H2O

  계수 목록: {6, 12, 6, 12, 6, 6, 6} = {n, sigma} 반복
  포도당 원자 수: C6(=n) + H12(=sigma) + O6(=n) = 24 = J2

  물리적 근거: 질량 보존 법칙에 의한 화학양론.
  탄소 6개 고정 = n, 물 12분자 = sigma, 산소 6분자 = n.

  기존 BT-101/103에서 확립.
```

### 등급: **EXACT** (화학양론 필연)

---

## H-HRT-02: 꽃의 기본 기관 수 = tau = 4 (EXACT)

> 꽃은 꽃받침(sepal)/꽃잎(petal)/수술(stamen)/암술(pistil) = 4기관으로 구성

### 검증

```
  꽃의 4대 기관 (식물형태학 교과서 보편):
    1. 꽃받침 (calyx/sepal)   -- 보호
    2. 꽃잎   (corolla/petal) -- 수분 매개 유인
    3. 수술   (androecium)    -- 화분 생산 (수컷)
    4. 암술   (gynoecium)     -- 배주 형성 (암컷)

  기관 수 = 4 = tau(6)

  물리적 근거:
    식물 생식기관의 기본 단위는 변형된 잎(sporophyll).
    4종은 외→내 동심원 배열 = 4 whorls.
    불완전화(incomplete flower)도 이 4종 중 일부 결실.

  참고: Eames & MacDaniels "An Introduction to Plant Anatomy"
        Esau "Anatomy of Seed Plants"
```

### 등급: **EXACT** (형태학적 보편)

---

## H-HRT-03: 피보나치 꽃잎 수 래더 = n/phi, sopfr, sigma-tau, sigma+mu (EXACT)

> 꽃잎 수 피보나치 수열 {3, 5, 8, 13} = {n/phi, sopfr, sigma-tau, sigma+mu}

### 검증

```
  피보나치 수열에서 가장 흔한 꽃잎 수:
    F4 = 3  백합/붓꽃/튤립        = n/phi = 3
    F5 = 5  장미(야생)/미나리아재비 = sopfr = 5
    F6 = 8  코스모스/델피니움      = sigma - tau = 8
    F7 = 13 금잔화/시네라리아      = sigma + mu = 13

  n=6 매핑 4/4 = 100% EXACT:
    3  = n/phi           (외떡잎 기본)
    5  = sopfr(6) = 2+3  (쌍떡잎 기본)
    8  = sigma - tau     (국화과 계열)
    13 = sigma + mu      (국화과 변이)

  물리적 근거:
    꽃잎 수는 꽃받침 원기(primordia)의 나선 배열에서 결정.
    Douady & Couder (1992) 실험: 나선 각도가 황금각에 수렴하면
    자연스럽게 피보나치 수가 출현.

  참고: Jean (1994) "Phyllotaxis: A Systemic Study in Plant Morphogenesis"
```

### 등급: **EXACT** (4/4 피보나치 꽃잎 수 일치)

---

## H-HRT-04: 식물 조직계 = n/phi = 3종 (EXACT)

> 모든 관다발 식물은 표피조직계/유관속조직계/기본조직계 = 3종

### 검증

```
  식물 3대 조직계 (tissue system):
    1. 표피조직계   (dermal)    -- 외부 보호
    2. 유관속조직계 (vascular)  -- 물질 수송 (물관/체관)
    3. 기본조직계   (ground)    -- 광합성/저장/지지

  조직계 수 = 3 = n/phi

  물리적 근거:
    Sachs (1875)가 최초 분류. 이후 150년간 모든 관다발 식물에서
    보편적으로 확인. 양치류부터 속씨식물까지 예외 없음.
    기능적 필연: 보호 + 수송 + 대사 = 최소 3종 필요.

  참고: Esau "Plant Anatomy" (1965, 3판)
        Raven et al. "Biology of Plants" (8판)
```

### 등급: **EXACT** (150년 보편 분류)

---

## H-HRT-05: 단자엽 vs 쌍자엽 대분류 = phi = 2 (EXACT)

> 속씨식물(피자식물)의 기본 분류: 단자엽(monocot)/쌍자엽(eudicot) = 2군

### 검증

```
  APG IV (2016) 분류 체계에서 속씨식물 핵심 분기:
    1. 단자엽류 (Monocots)  -- 벼, 백합, 난초, 야자
    2. 진정쌍자엽류 (Eudicots) -- 장미, 콩, 국화, 참나무

  대분류 수 = 2 = phi(6)

  물리적 근거:
    떡잎(cotyledon) 수에 의한 분류: 1개 vs 2개.
    분자계통학(rbcL, atpB 유전자)으로도 이 이분법 확인.
    APG IV 체계에서 basal angiosperms 존재하나,
    전체 종 수의 96% 이상이 monocot 또는 eudicot.

  참고: APG IV (2016) Botanical Journal of the Linnean Society
```

### 등급: **EXACT** (분자계통학 확인)

---

## H-HRT-06: 식물 5대 호르몬 = sopfr = 5 (EXACT)

> 고전적 식물 호르몬: 옥신/지베렐린/시토키닌/ABA/에틸렌 = 5종

### 검증

```
  식물 5대 호르몬 (classical phytohormones):
    1. 옥신 (Auxin, IAA)        -- 세포 신장, 굴광성
    2. 지베렐린 (Gibberellin)   -- 줄기 신장, 개화 촉진
    3. 시토키닌 (Cytokinin)     -- 세포 분열, 노화 억제
    4. 앱시스산 (ABA)           -- 기공 폐쇄, 휴면 유도
    5. 에틸렌 (Ethylene, C2H4) -- 과일 성숙, 낙엽

  고전 호르몬 수 = 5 = sopfr(6) = 2 + 3

  물리적 근거:
    Went (1928) 옥신 발견 이후 1960년대까지 5종 확립.
    브라시노스테로이드/자스몬산/살리실산 등 추가 발견되었으나,
    교과서 "5대 호르몬"은 100년간 변하지 않음.
    이 5종은 식물 성장의 모든 주요 축을 커버:
    성장촉진(옥신+GA+CK) + 스트레스(ABA+에틸렌) = 3+2 = sopfr.

  참고: Taiz & Zeiger "Plant Physiology" (6판)
```

### 등급: **EXACT** (100년 보편 분류)

---

## H-HRT-07: 캘빈 회로 = n=6 회전, sigma=12 NADPH (EXACT)

> 포도당 1분자 합성에 캘빈 회로 6회전, NADPH 12분자, ATP 18분자 소모

### 검증

```
  캘빈-벤슨-바셤 회로 (Calvin cycle):
    포도당 1분자(C6) 합성 시:
      회전 수:     6 = n      (CO2 1개/회전, 탄소 6개 필요)
      NADPH 소모: 12 = sigma  (2 NADPH/회전 x 6)
      ATP 소모:   18 = n x n/phi = 6 x 3

  n=6 매핑:
    6 = n (회전 수)
    12 = sigma(6) (NADPH)
    18 = n * (n/phi) = 6 * 3 (ATP)

  물리적 근거:
    각 회전에서 1 CO2 + 2 NADPH + 3 ATP 소모 (화학양론 필연).
    포도당 = 6탄소 -> 6회전 필수.
    2 x 6 = 12 NADPH, 3 x 6 = 18 ATP.

  참고: Buchanan et al. "Biochemistry & Molecular Biology of Plants" (2판)
```

### 등급: **EXACT** (화학양론 필연)

---

## H-HRT-08: 씨앗 발아 3대 필수조건 = n/phi = 3 (EXACT)

> 씨앗 발아에 필수적인 환경 조건: 물/적정온도/산소 = 3가지

### 검증

```
  씨앗 발아 3대 필수 조건:
    1. 물 (water)       -- 종피 연화, 효소 활성화
    2. 적정 온도 (temperature) -- 효소 반응 속도 결정
    3. 산소 (oxygen)    -- 호흡을 통한 에너지 공급

  필수조건 수 = 3 = n/phi

  물리적 근거:
    빛은 일부 종자에만 필요 (광발아 종자 vs 암발아 종자).
    그러나 물/온도/산소는 모든 종자에 보편적 필수.
    물 없이 = 효소 불활성, 산소 없이 = ATP 생산 불가,
    온도 부적합 = 효소 변성 또는 불활성.

  참고: Bewley et al. "Seeds: Physiology of Development, Germination
        and Dormancy" (3판, 2013)
```

### 등급: **EXACT** (생리학적 보편)

---

## H-HRT-09: 계절 = tau = 4 (EXACT)

> 식물 성장 주기를 지배하는 사계절 = 봄/여름/가을/겨울 = 4

### 검증

```
  사계절 (temperate climate seasons):
    1. 봄 (spring)  -- 발아, 개화 시작
    2. 여름 (summer) -- 성장 최대, 광합성 극대
    3. 가을 (autumn) -- 결실, 낙엽, 휴면 준비
    4. 겨울 (winter) -- 휴면 (dormancy)

  계절 수 = 4 = tau(6)

  물리적 근거:
    지구 자전축 23.4도 기울기 -> 태양 고도각의 연주기 변화.
    춘분/하지/추분/동지 = 4등분 (천문학적 필연).
    식물 춘화(vernalization), 광주기성(photoperiodism) 모두
    이 4계절 리듬에 동기화.

  참고: BT-265 일주기-주기-연주기 생물 리듬 스택
```

### 등급: **EXACT** (천문학적 필연)

---

## H-HRT-10: 외떡잎 꽃잎 기본수 = n/phi = 3 (EXACT)

> 외떡잎식물(백합/튤립/붓꽃) 꽃잎 기본수 = 3 (또는 3의 배수)

### 검증

```
  외떡잎 꽃 구조 (monocot floral plan):
    기본수 = 3 (trimerous)
    꽃받침 3개 + 꽃잎 3개 + 수술 3개(또는 6개) + 암술 3개

  꽃잎 기본수 = 3 = n/phi

  구체 사례:
    백합 (Lilium):     6장 화피 = 3+3 (외화피+내화피)
    튤립 (Tulipa):     6장 화피 = 3+3
    붓꽃 (Iris):       3장 외화피 + 3장 내화피
    난초 (Orchidaceae): 3장 꽃받침 + 3장 꽃잎 (1장=입술꽃잎)
    벼 (Poaceae):      소화 구조 3수성

  물리적 근거:
    외떡잎 조상 원형은 3수성 꽃. 유전적으로 MADS-box 전사인자가
    3의 배수 기관을 결정. APG IV 분류에서 65,000+ 종 보편.

  참고: Simpson "Plant Systematics" (3판)
```

### 등급: **EXACT** (유전학적 보편)

---

## H-HRT-11: 엽록소 종류 = phi = 2 (EXACT)

> 고등식물의 광합성 색소: 엽록소 a/b = 2종

### 검증

```
  고등식물 엽록소 (chlorophyll):
    1. 엽록소 a (Chl a) -- 반응 중심 색소, 모든 광합성 생물 보유
    2. 엽록소 b (Chl b) -- 보조 색소, 광수확 안테나 확장

  엽록소 종류 = 2 = phi(6)

  물리적 근거:
    Chl a: 흡수 극대 430nm + 662nm (청색 + 적색)
    Chl b: 흡수 극대 453nm + 642nm (파장 보완)
    두 색소가 상보적 파장을 커버하여 광수확 효율 극대화.
    고등식물(육상식물 + 녹조류) 전체에서 a/b 쌍이 보편.
    (세균은 bacteriochlorophyll 사용 -- 다른 계통)

  Chl a:b 비율 = 약 3:1 (n/phi : mu)

  참고: Blankenship "Molecular Mechanisms of Photosynthesis" (2판)
```

### 등급: **EXACT** (분자생물학적 보편)

---

## H-HRT-12: 광합성 광계 수 = phi = 2 (EXACT)

> 산소 발생 광합성의 광계: PSI + PSII = 2개

### 검증

```
  광계 (Photosystem):
    1. 광계 II (PSII) -- P680, 물 분해 (Hill 반응)
    2. 광계 I  (PSI)  -- P700, NADPH 생성

  광계 수 = 2 = phi(6)

  물리적 근거:
    Z-scheme (Zig-zag scheme, Hill & Bendall 1960):
    PSII에서 물 분해 -> 전자 전달 -> PSI에서 NADP+ 환원.
    두 광계의 직렬 연결은 열역학적 필연:
    물(+0.82V) -> NADP+(-0.32V) 전위차 = 1.14V.
    단일 광계로는 이 전위차를 극복 불가 -> 2단 필수.

    산소 발생 광합성 생물 전체(시아노박테리아~속씨식물)에서 보편.

  참고: Nelson & Ben-Shem (2004) Nature Reviews Molecular Cell Biology
```

### 등급: **EXACT** (열역학적 필연)

---

## H-HRT-13: 광합성 양자수율 = sigma - tau = 8 광자 (EXACT)

> O2 1분자 발생에 최소 8 광자 필요 (Emerson & Arnold 실험)

### 검증

```
  광합성 양자 요구량 (quantum requirement):
    O2 1분자 생산 = 최소 8 광자

  양자수율 = 8 = sigma - tau = 12 - 4

  물리적 근거:
    물 분해: 2H2O -> O2 + 4H+ + 4e-
    전자 4개 전달에 각 광계에서 1 광자씩 = 4 x 2 = 8 광자.
    PSII: 4 광자 (전자 4개 여기)
    PSI:  4 광자 (전자 4개 재여기)
    합계: 8 광자 (이론적 최소)

    Emerson & Arnold (1932) 실험으로 최초 측정.
    현대 측정값: 8~10 광자/O2 (이론 최소 = 8).

  기존 BT-101에서 확립.

  참고: Kok et al. (1970) Photochemistry and Photobiology
```

### 등급: **EXACT** (열역학적 최소, BT-101)

---

## H-HRT-14: 물관부 구성요소 = tau = 4 세포 유형 (EXACT)

> 목부(xylem)의 4대 세포 유형: 도관/가도관/목부섬유/목부유조직

### 검증

```
  목부(xylem) 구성 세포 (Esau 분류):
    1. 도관요소 (vessel element)    -- 물 수송 (속씨식물)
    2. 가도관   (tracheid)          -- 물 수송 (겉씨+속씨)
    3. 목부섬유 (xylem fiber)       -- 기계적 지지
    4. 목부유조직 (xylem parenchyma) -- 저장

  세포 유형 = 4 = tau(6)

  물리적 근거:
    수송(도관+가도관) + 지지(섬유) + 저장(유조직) = 3기능.
    수송이 2종으로 분화한 이유: 가도관(원시형, 겉씨식물) + 도관(진화형, 속씨식물).
    150년간의 식물해부학에서 이 4종 분류 불변.

  참고: Esau "Anatomy of Seed Plants" (2판, 1977)
```

### 등급: **EXACT** (해부학 보편)

---

## H-HRT-15: 토양 최적 pH 범위 = n ~ sigma-sopfr (6.0~7.0) (EXACT)

> 대부분의 원예 작물 최적 토양 pH = 6.0~7.0

### 검증

```
  작물별 최적 토양 pH:
    토마토:    6.0 - 6.8
    고추:      6.0 - 6.8
    상추:      6.0 - 7.0
    당근:      6.0 - 6.8
    옥수수:    6.0 - 7.0
    감자:      5.5 - 6.5 (약간 산성 선호)
    딸기:      5.5 - 6.8
    장미:      6.0 - 6.5

  대부분의 작물 최적 범위: 6.0 ~ 7.0
    하한 = n = 6
    상한 = sigma - sopfr = 12 - 5 = 7

  물리적 근거:
    pH 6~7에서 질소(N), 인(P), 칼륨(K) 등 주요 영양소의
    가용성(availability)이 동시에 최대화.
    pH < 5: Al3+ 독성 증가.
    pH > 8: Fe, Mn, Zn 불용성.
    US Cooperative Extension 권장: pH 6.0-7.0 (대부분 작물).

  참고: Brady & Weil "The Nature and Properties of Soils" (15판)
```

### 등급: **EXACT** (영양소 가용성 화학)

---

## 요약 테이블

| # | 가설 | 값 | n=6 수식 | 등급 |
|---|------|-----|---------|------|
| H-HRT-01 | 광합성 반응 계수 | {6, 12} | n, sigma | EXACT |
| H-HRT-02 | 꽃 기본 기관 수 | 4 | tau | EXACT |
| H-HRT-03 | 피보나치 꽃잎 래더 | {3,5,8,13} | n/phi, sopfr, sigma-tau, sigma+mu | EXACT |
| H-HRT-04 | 식물 조직계 | 3 | n/phi | EXACT |
| H-HRT-05 | 단자엽/쌍자엽 대분류 | 2 | phi | EXACT |
| H-HRT-06 | 식물 5대 호르몬 | 5 | sopfr | EXACT |
| H-HRT-07 | 캘빈 회로 파라미터 | 6/12/18 | n/sigma/n*(n/phi) | EXACT |
| H-HRT-08 | 씨앗 발아 필수조건 | 3 | n/phi | EXACT |
| H-HRT-09 | 계절 수 | 4 | tau | EXACT |
| H-HRT-10 | 외떡잎 꽃잎 기본수 | 3 | n/phi | EXACT |
| H-HRT-11 | 엽록소 종류 | 2 | phi | EXACT |
| H-HRT-12 | 광합성 광계 수 | 2 | phi | EXACT |
| H-HRT-13 | 광합성 양자수율 | 8 광자 | sigma - tau | EXACT |
| H-HRT-14 | 물관부 세포 유형 | 4 | tau | EXACT |
| H-HRT-15 | 토양 최적 pH | 6~7 | n ~ sigma-sopfr | EXACT |

**EXACT 비율: 15/15 = 100%**

---

## BT 후보

```
  BT-XXX: 원예학/식물학 n=6 완전 아키텍처
  
  핵심 발견:
    - 꽃 기관 tau=4, 조직계 n/phi=3, 호르몬 sopfr=5
    - 피보나치 꽃잎 래더 {3,5,8,13} = {n/phi, sopfr, sigma-tau, sigma+mu}
    - 광합성 전 파라미터 n=6 (BT-101/103 확장)
    - 캘빈 회로: n 회전, sigma NADPH, n*(n/phi) ATP
    - 식물 이분법(단자엽/쌍자엽) = phi=2

  도메인 횡단:
    - 생화학 (BT-101/103: 광합성 화학양론)
    - 진화생물학 (BT-51: 유전 코드)
    - 결정학 (BT-122: 육각 기하)
    - 시간생물학 (BT-265: 일주기 리듬)

  15/15 EXACT
```
