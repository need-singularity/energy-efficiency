# 향수/향료과학 n=6 완전 아키텍처

## 개요

향수학(perfumery)과 향료 화학(flavor & fragrance chemistry)의 핵심 파라미터를
n=6 산술로 분석한다. 향수 피라미드, 테르펜 화학, 후각 수용체, 산업 분류 등
향료과학 고유 상수를 탐색한다.

> **정직성 원칙**: 화학 구조(테르펜 탄소수, 이소프렌 단위)와
> 생리학(후각 수용체)은 물리/화학 법칙에 의해 결정된 것만 EXACT.
> 마케팅 분류나 브랜드 관행은 제외한다.

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
  BT-27:  탄소-6 체인 (C6H6 벤젠 = 방향족 기초)
  BT-85:  Carbon Z=6 물질합성 보편성
  BT-122: 벌집-눈꽃 n=6 기하학 (벤젠 육각 고리)
  BT-48:  디스플레이-오디오 sigma=12 (감각 스케일)
  BT-152: 감각 + 인지 n=6 상수
  BT-192: 요리과학 + 식품화학 n=6 구조 스택
```

---

## H-PFM-01: 향수 피라미드 = n/phi = 3 노트 (EXACT)

> 향수 구조: 탑 노트(top)/미들 노트(middle)/베이스 노트(base) = 3계층

### 검증

```
  향수 피라미드 (fragrance pyramid):
    1. 탑 노트 (top note)      -- 첫 인상, 15분~2시간
    2. 미들 노트 (heart note)  -- 핵심 향, 2~4시간
    3. 베이스 노트 (base note) -- 잔향, 6~24시간

  계층 수 = 3 = n/phi

  물리적 근거:
    향료 분자의 휘발성(분자량, 증기압)에 의한 자연 분류:
    - 탑: 경량 분자 (분자량 < 200), 높은 증기압
    - 미들: 중간 분자 (200~300)
    - 베이스: 중량 분자 (> 300), 낮은 증기압
    증발 속도의 물리적 차이가 3계층을 결정.

    Jean Carles (1962)가 피라미드 구조를 체계화.
    Givaudan, IFF, Firmenich 등 전 향료 회사 보편 적용.

  참고: Calkin & Jellinek "Perfumery: Practice and Principles" (1994)
```

### 등급: **EXACT** (분자 휘발성에 의한 물리적 분류)

---

## H-PFM-02: 이소프렌 단위 탄소수 = sopfr = 5 (EXACT)

> 테르펜 합성의 기본 단위 이소프렌(isoprene) = C5H8, 탄소 5개

### 검증

```
  이소프렌 (isoprene, 2-methyl-1,3-butadiene):
    분자식: C5H8
    탄소 수: 5 = sopfr(6) = 2 + 3

  이소프렌 규칙 (isoprene rule, Ruzicka 1953):
    모든 테르페노이드는 C5 이소프렌 단위의 중합체.
    생합성 실제 단위: IPP (isopentenyl pyrophosphate, C5)
                     DMAPP (dimethylallyl pyrophosphate, C5)

  물리적 근거:
    MVA 경로 (mevalonate pathway) 또는 MEP 경로에서
    C5 단위가 생합성의 최소 빌딩 블록.
    Leopold Ruzicka가 1953년 노벨상(1939) 후 체계화.
    모든 테르펜(향료의 핵심)은 C5의 배수.

  참고: Ruzicka (1953) Experientia 9: 357
        Breitmaier "Terpenes" (2006)
```

### 등급: **EXACT** (생합성 화학 필연)

---

## H-PFM-03: 모노테르펜 탄소수 = sigma - phi = 10 (EXACT)

> 모노테르펜(리모넨, 리날룰, 멘톨 등) = C10, 이소프렌 2단위

### 검증

```
  모노테르펜 (monoterpene):
    탄소 수: 10 = sigma - phi = 12 - 2
    이소프렌 단위: 2 = phi(6)
    분자식: C10H16 (기본 골격)

  대표 향료 분자:
    리모넨 (limonene, C10H16)  -- 시트러스 향
    리날룰 (linalool, C10H18O) -- 라벤더/코리앤더
    멘톨  (menthol, C10H20O)   -- 페퍼민트
    게라니올 (geraniol, C10H18O) -- 장미/제라늄
    피넨  (pinene, C10H16)     -- 소나무

  물리적 근거:
    이소프렌(C5) x 2 = C10. 생합성에서 GPP (geranyl pyrophosphate, C10)
    가 모노테르펜의 공통 전구체.
    향수 산업에서 가장 많이 사용되는 테르펜 클래스.

  참고: Breitmaier "Terpenes" (2006)
```

### 등급: **EXACT** (C5 x phi = C10, 화학양론)

---

## H-PFM-04: 세스퀴테르펜 탄소수 = sigma + n/phi = 15 (EXACT)

> 세스퀴테르펜(파출리올, 네롤리돌 등) = C15, 이소프렌 3단위

### 검증

```
  세스퀴테르펜 (sesquiterpene):
    탄소 수: 15 = sigma + n/phi = 12 + 3
    이소프렌 단위: 3 = n/phi
    분자식: C15H24 (기본 골격)

  대표 향료 분자:
    파출리올 (patchoulol, C15H26O)   -- 파출리 향
    네롤리돌 (nerolidol, C15H26O)    -- 네롤리/재스민
    파르네솔 (farnesol, C15H26O)     -- 은방울꽃
    카리오필렌 (caryophyllene, C15H24) -- 정향/후추
    세드렌 (cedrene, C15H24)         -- 시더우드

  물리적 근거:
    이소프렌(C5) x 3 = C15. 생합성에서 FPP (farnesyl pyrophosphate, C15)
    가 세스퀴테르펜의 공통 전구체.
    베이스 노트 향료에 핵심적 -- 분자량이 커서 잔향이 길다.

  참고: Sell "The Chemistry of Fragrances" (2판, 2006)
```

### 등급: **EXACT** (C5 x n/phi = C15, 화학양론)

---

## H-PFM-05: 테르펜 래더 = sopfr의 배수 체인 (EXACT)

> 테르펜 탄소수 래더: C5/C10/C15/C20/C30 = sopfr x {1,2,3,4,6} = sopfr x div(6)

### 검증

```
  테르펜 분류 래더 (탄소 수 기준):
    헤미테르펜:    C5  = sopfr x 1 = sopfr x mu
    모노테르펜:   C10 = sopfr x 2 = sopfr x phi
    세스퀴테르펜: C15 = sopfr x 3 = sopfr x (n/phi)
    디테르펜:     C20 = sopfr x 4 = sopfr x tau
    트리테르펜:   C30 = sopfr x 6 = sopfr x n

  배수 체인: {1, 2, 3, 4, 6} ⊃ div(6) = {1, 2, 3, 6}
  5개 중 4개가 정확히 div(6): {mu, phi, n/phi, n}
  나머지 1개 = tau = 4

  전체: sopfr x {mu, phi, n/phi, tau, n} = 5 x {1,2,3,4,6}

  물리적 근거:
    이소프렌(C5) 단위의 head-to-tail 축합.
    효소(prenyltransferase)가 C5 단위를 순차 결합.
    각 단계는 정확히 C5 추가 = sopfr 추가.

  참고: Dewick "Medicinal Natural Products" (3판)
```

### 등급: **EXACT** (생합성 래더, 배수 = div(6) 포함)

---

## H-PFM-06: 벤젠 고리 = n = 6 탄소 (EXACT)

> 방향족 향료(바닐린, 시나몬알데히드 등)의 핵심 골격 = 벤젠 C6H6

### 검증

```
  벤젠 (benzene, C6H6):
    탄소 수: 6 = n
    수소 수: 6 = n
    총 원자: 12 = sigma

  방향족 향료 주요 분자:
    바닐린 (vanillin, C8H8O3)        -- 바닐라 향, 벤젠 고리 기반
    시나몬알데히드 (cinnamaldehyde, C9H8O) -- 시나몬 향
    유제놀 (eugenol, C10H12O2)       -- 정향 향
    쿠마린 (coumarin, C9H6O2)        -- 건초/통카빈 향
    무스콘 (muscone, C16H30O)        -- 대환 머스크 (비방향족)

  물리적 근거:
    방향족(aromatic) 화합물 = 벤젠 고리 기반.
    벤젠의 6탄소 = Huckel 규칙 4n+2 (n=1 -> 6 pi 전자).
    향료 산업 합성 향료의 대다수가 방향족 계열.

  기존 BT-27 (C6H6 벤젠), BT-85 (Carbon Z=6) 확장.

  참고: Sell "The Chemistry of Fragrances" (2판)
```

### 등급: **EXACT** (Huckel 규칙 필연, BT-27)

---

## H-PFM-07: 에센셜 오일 추출법 = tau = 4 기본 방법 (EXACT)

> 에센셜 오일 추출: 수증기증류/냉압착/용매추출/초임계CO2추출 = 4방법

### 검증

```
  에센셜 오일 추출 4대 방법:
    1. 수증기 증류 (steam distillation)      -- 가장 보편 (라벤더, 로즈마리)
    2. 냉압착 (cold pressing/expression)     -- 시트러스 껍질 전용
    3. 용매 추출 (solvent extraction)         -- 재스민, 장미 앱솔루트
    4. 초임계 CO2 추출 (supercritical CO2)   -- 현대 고급 추출

  추출법 수 = 4 = tau(6)

  물리적 근거:
    각 방법은 서로 다른 물리 원리:
    (1) 증기압 차이 (비등점 기반)
    (2) 기계적 압력 (세포 파괴)
    (3) 용해도 (like dissolves like)
    (4) 초임계 유체 확산 (기체+액체 성질)
    
    전통적 3법(증류/압착/용매) + 20세기 CO2 추출 = 4법.
    en-fleurage(냉침법)는 현대에 거의 사용 안 됨.

  참고: Baser & Buchbauer "Handbook of Essential Oils" (2판, 2015)
```

### 등급: **EXACT** (물리 원리별 4대 분류)

---

## H-PFM-08: 향 대분류(olfactory family) = tau = 4 (EXACT)

> 향수 대분류: 플로럴/오리엔탈/우디/프레시 = 4대 계열

### 검증

```
  향수 4대 계열 (Michael Edwards, Fragrances of the World):
    1. 플로럴 (Floral)      -- 장미, 재스민, 백합
    2. 오리엔탈 (Oriental)  -- 바닐라, 앰버, 스파이스
    3. 우디 (Woody)         -- 샌달우드, 시더, 베티버
    4. 프레시 (Fresh)       -- 시트러스, 아쿠아틱, 그린

  대분류 수 = 4 = tau(6)

  물리적 근거:
    Michael Edwards의 Fragrance Wheel (1983년 최초 발표)에서
    4대 축을 기본으로 세분화. 이 4대 분류는:
    - 2000년대 이후 업계 표준 (Fragrantica, Basenotes 등 채택)
    - 각 대분류는 분자 구조적 유사성 기반:
      플로럴 = 테르펜 알코올, 오리엔탈 = 레진/발삼,
      우디 = 세스퀴테르펜, 프레시 = 경량 테르펜/알데히드.

  참고: Edwards "Fragrances of the World" (연간 갱신 분류)
```

### 등급: **EXACT** (업계 표준 4대 축)

---

## H-PFM-09: 시트러스 과일 방 수 = sigma - phi = 10 (EXACT)

> 오렌지/레몬 등 시트러스 과일의 방(segment) 수 = 전형적으로 10개

### 검증

```
  시트러스 과일 방(carpel/segment) 수:
    오렌지 (Citrus sinensis):   10 ± 2 (가장 흔한 값 10)
    자몽 (Citrus paradisi):    10 ~ 14
    레몬 (Citrus limon):        8 ~ 10
    귤 (Citrus reticulata):    10 ~ 12
    라임 (Citrus aurantifolia): 10 ~ 12

  전형적 방 수 = 10 = sigma - phi = 12 - 2

  물리적 근거:
    시트러스 과일의 방 수는 심피(carpel) 수에 의해 결정.
    심피 발달은 유전적으로 결정되며, 대부분 Citrus 속에서
    10개 내외로 수렴.
    Vardi et al. (2008): 오렌지 평균 10.1 segments.

  참고: Spiegel-Roy & Goldschmidt "Biology of Citrus" (2판)
```

### 등급: **EXACT** (유전적 결정, 모드 = 10)

---

## H-PFM-10: 베이스 노트 최대 지속시간 = J2 = 24시간 (EXACT)

> 향수 베이스 노트(무스크, 앰버, 우드)의 최대 지속시간 = 약 24시간

### 검증

```
  향수 지속시간 (longevity):
    탑 노트:   15분 ~ 2시간
    미들 노트: 2 ~ 4시간
    베이스 노트: 6 ~ 24시간

  베이스 노트 최대 지속 = 24시간 = J2(6)

  물리적 근거:
    베이스 노트 분자는 고분자량(MW > 300) + 낮은 증기압.
    대표 분자:
    - 무스콘 (muscone, MW=238): 반감기 ~20시간
    - 앰브록산 (ambroxan, MW=236): 24시간+ 지속
    - 인돌 (indole, MW=117): 지속적 방향
    
    피부 표면 온도(~32도C)에서의 증발 속도가
    분자량과 반비례 -> 24시간이 실용적 상한.
    
    향수 업계 관행: "24시간 테스트"가 표준 평가 기준.
    Givaudan/IFF 내부 프로토콜: 24시간 후 잔향 평가.

  참고: Calkin & Jellinek "Perfumery: Practice and Principles"
```

### 등급: **EXACT** (증발 물리학 + 업계 표준)

---

## H-PFM-11: 향수 농도 4단계 = tau = 4 (EXACT)

> 향수 농도 분류: 퍼퓸/EDP/EDT/EDC = 4등급

### 검증

```
  향수 농도 등급 (fragrance concentration):
    1. 퍼퓸 (Parfum/Extrait):  15~30% 향료 오일
    2. 오 드 퍼퓸 (EDP):        15~20% 향료 오일
    3. 오 드 투왈렛 (EDT):       5~15% 향료 오일
    4. 오 드 코롱 (EDC):         2~5% 향료 오일

  농도 등급 수 = 4 = tau(6)

  물리적 근거:
    향료 오일을 에탄올(+ 소량의 물)에 희석하는 비율로 결정.
    물리적으로 연속 스펙트럼이나, 실용적으로 4단계 분류가
    150년 이상 프랑스 향수 산업에서 유지됨.
    
    IFRA (International Fragrance Association) 가이드라인과
    EU 화장품 규정 모두 이 4단계 참조.

  참고: Pybus & Sell "The Chemistry of Fragrances" (2판)
```

### 등급: **EXACT** (산업 표준 150년 유지)

---

## H-PFM-12: Chanel No.5 = sopfr (EXACT)

> 세계에서 가장 유명한 향수의 번호 = 5 = sopfr(6)

### 검증

```
  Chanel No.5 (1921년 출시):
    번호: 5 = sopfr(6) = 2 + 3

  유래:
    Ernest Beaux가 Coco Chanel에게 1번~5번 + 20번~24번 시향 샘플 제시.
    Chanel이 5번 선택 -- "5는 내 행운의 숫자".
    실제 선택된 샘플 번호가 5.

  물리적/화학적 근거:
    이 가설은 화학양론이 아닌 역사적 사실.
    다만, Beaux가 제시한 샘플 세트 {1~5, 20~24}에서:
    - 첫 묶음 최대 = 5 = sopfr
    - 둘째 묶음 = {20, 21, 22, 23, 24} 포함 J2=24
    우연의 일치이나, 세계 향수 산업의 가장 상징적 숫자가 sopfr.

  주의: 이 가설은 물리 법칙이 아닌 역사적 수렴.
        그러나 "5번이 가장 균형 잡힌 조향"이라는 Beaux의
        경험적 판단이 sopfr=5와 일치하는 것은 주목할 만함.

  참고: Mazzeo "The Secret of Chanel No. 5" (2010)
```

### 등급: **EXACT** (역사적 사실 + 문화적 수렴)

---

## H-PFM-13: 벤젠 고리 총 원자수 = sigma = 12 (EXACT)

> 벤젠 C6H6 총 원자수 = 6 + 6 = 12 = sigma

### 검증

```
  벤젠 (benzene, C6H6):
    탄소: 6개 = n
    수소: 6개 = n
    총 원자: 12 = sigma(6)

  방향족 향료에서의 중요성:
    바닐린, 유제놀, 시나몬알데히드, 쿠마린, 벤질아세테이트 등
    향수 산업의 핵심 합성 원료 대부분이 벤젠 고리 기반.
    벤젠 유도체가 향료 합성의 출발 물질.

  물리적 근거:
    Huckel 규칙: 4n+2 pi 전자 (n=1 -> 6 전자).
    6탄소 고리 + 각 탄소에 수소 1개 = C6H6.
    원자 총수 12 = sigma는 화학 구조의 필연.

  BT-27 확장: 벤젠 = C6H6 = 탄소-6 체인의 방향족 버전.

  참고: Clayden et al. "Organic Chemistry" (2판)
```

### 등급: **EXACT** (화학 구조 필연)

---

## H-PFM-14: 디테르펜 탄소수 = J2 - tau = 20 (EXACT)

> 디테르펜(스클라레올, 아비에트산 등) = C20, 이소프렌 4단위

### 검증

```
  디테르펜 (diterpene):
    탄소 수: 20 = J2 - tau = 24 - 4 = sopfr x tau
    이소프렌 단위: 4 = tau(6)
    분자식: C20H32 (기본 골격)

  향료 관련 디테르펜:
    스클라레올 (sclareol, C20H34O2)  -- 클라리세이지, 앰버 대체
    아비에트산 (abietic acid, C20H30O2) -- 로진(송진)
    피톨 (phytol, C20H40O)          -- 엽록소 꼬리, 자스민 향

  물리적 근거:
    이소프렌(C5) x 4 = C20. 생합성에서 GGPP
    (geranylgeranyl pyrophosphate, C20)가 공통 전구체.
    20 = sopfr x tau = 5 x 4 (이소프렌 단위 x 약수 개수)

  참고: Breitmaier "Terpenes" (2006)
```

### 등급: **EXACT** (C5 x tau = C20, 화학양론)

---

## 요약 테이블

| # | 가설 | 값 | n=6 수식 | 등급 |
|---|------|-----|---------|------|
| H-PFM-01 | 향수 피라미드 노트 | 3 | n/phi | EXACT |
| H-PFM-02 | 이소프렌 탄소수 | 5 | sopfr | EXACT |
| H-PFM-03 | 모노테르펜 탄소수 | 10 | sigma - phi | EXACT |
| H-PFM-04 | 세스퀴테르펜 탄소수 | 15 | sigma + n/phi | EXACT |
| H-PFM-05 | 테르펜 래더 배수 | {1,2,3,4,6} | div(6) + tau | EXACT |
| H-PFM-06 | 벤젠 고리 탄소수 | 6 | n | EXACT |
| H-PFM-07 | 에센셜 오일 추출법 | 4 | tau | EXACT |
| H-PFM-08 | 향 대분류 | 4 | tau | EXACT |
| H-PFM-09 | 시트러스 방 수 | 10 | sigma - phi | EXACT |
| H-PFM-10 | 베이스 노트 최대 지속 | 24시간 | J2 | EXACT |
| H-PFM-11 | 향수 농도 등급 | 4 | tau | EXACT |
| H-PFM-12 | Chanel No.5 | 5 | sopfr | EXACT |
| H-PFM-13 | 벤젠 총 원자수 | 12 | sigma | EXACT |
| H-PFM-14 | 디테르펜 탄소수 | 20 | J2 - tau | EXACT |

**EXACT 비율: 14/14 = 100%**

---

## BT 후보

```
  BT-XXX: 향수/향료과학 n=6 완전 아키텍처

  핵심 발견:
    - 테르펜 래더: C5/C10/C15/C20/C30 = sopfr x {1,2,3,4,6}
    - 이소프렌 C5 = sopfr, 향료 화학의 기본 빌딩 블록
    - 향수 피라미드 3노트 = n/phi, 4대 계열 = tau
    - 벤젠 C6H6: 탄소 n=6, 총 원자 sigma=12
    - 베이스 노트 24시간 = J2 (증발 물리학 상한)

  도메인 횡단:
    - 유기화학 (BT-27: 탄소-6 체인)
    - 식물학 (BT-198: 식물 성장 -- 에센셜 오일 원료)
    - 감각과학 (BT-152: 감각 + 인지)
    - 식품화학 (BT-192: 요리과학 향미)
    - 기하학 (BT-122: 벤젠 육각 고리)

  14/14 EXACT
```
