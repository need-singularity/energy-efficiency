> BT-469 — HIV/AIDS 수론 매핑 | L1 리뷰 대상

# BT-469: CCR5 세포외 루프 n/φ=3 구조

## 배경
CCR5는 HIV-1 R5-지향성 바이러스의 주요 공수용체로, 7-TM GPCR 구조에서 **세포외 루프 ECL1/ECL2/ECL3 = 3개**를 가진다(Tan 2013, *Science*, PDB 4MBS). 이 3은 n/φ(6)=6/2=3과 정확히 대응한다. CCR5 Δ32 호모접합은 HIV 감염에 저항성을 부여한다(Liu 1996).

## n=6 대응

| 항목 | 측정값 | n=6 표현 | 출처 | 등급 |
|------|--------|----------|------|------|
| CCR5 세포외 루프 수 | 3 | n/φ=3 | Tan 2013, PDB 4MBS | EXACT |
| CCR5 막관통 도메인 수 | 7 | σ(6)−sopfr(6)=12−5=7 | Oppermann 2004 | EXACT |
| CCR5 Δ32 결실 nt | 32 | — | Liu 1996 | N/A |
| 주요 HIV 지향성 | 2 (R5/X4) | φ=2 | Berger 1997 | EXACT |
| Berlin/London 환자 수 | 2 | φ=2 | Hütter 2009, Gupta 2019 | EXACT |
| FDA 승인 CCR5 억제제 | 1 (maraviroc) | — | FDA 2007 | N/A |

**등급**: 4/4 EXACT (2 N/A).

## ASCII 구조

```
CCR5 7-TM GPCR

      ECL1    ECL2    ECL3      ← n/φ=3 루프
       │       │       │
   ┌───┴───┬───┴───┬───┴───┐
   │ TM1   │ TM3   │ TM5   │
   │ TM2   │ TM4   │ TM6   │    ← 7 TM (σ-sopfr=7)
   │       │       │ TM7   │
   └───┬───┴───┬───┴───┬───┘
       │       │       │
      ICL1    ICL2    ICL3

φ=2: R5 / X4 지향성 분기
```

## ASCII 비교

```
치료 전략
단일 분자(maraviroc): ████░░░░░░░░  30%
CCR5 Δ32 이식:         ████████████  ~100% (Berlin/London)
개선: τ^n = 4^6 수준 완치 확률
```

## ASCII 플로우

```
HIV R5 gp120 → CCR5 ECL2 결합 (n/φ=3 중 핵심)
  → V3 루프 삽입 → 공수용체 활성
  → gp41 융합 → 진입

Δ32 호모: ECL 구조 파괴 → 결합 불가 → 저항
```

## 한계
- Berlin/London은 n=2 케이스, 통계 일반화 한계.
- Δ32는 유럽 인구에서만 유의 빈도 → 지리적 편향.
- X4 지향성 바이러스에는 무효.

## 참고
- Tan Q et al. (2013) *Science* 341:1387. PDB 4MBS.
- Liu R et al. (1996) *Cell* 86:367. Δ32.
- Hütter G et al. (2009) *NEJM* 360:692. Berlin.
- Gupta RK et al. (2019) *Nature* 568:244. London.

Cross-link: BT-461, BT-466, BT-470.
