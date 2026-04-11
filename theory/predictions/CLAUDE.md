# theory/predictions — Testable 예측

목적: 45건 예측, 반증 가능성 보장
축: theory
상위: ../CLAUDE.md

## 하위
- testable-predictions.md
- predictions-unmeasured.md
- falsification-experiments.md
- pre-registered-predictions.md
- (계산기/검증 `.hexa` 금지 — **nexus/shared/n6/scripts/** 로!)

## SSOT
- (없음)

## 진입 명령
- nexus verify predictions

## ⛔ 계산기 금지 규칙 (2026-04-11 추가)

**이 디렉토리는 이론/예측 텍스트(.md)만 허용**. 모든 `verify_*.hexa`, `*_calculator.hexa`, `*_scanner.hexa` 등 **계산 도구는 반드시**:

```
/Users/ghost/Dev/nexus/shared/n6/scripts/
```

**에 작성**. R5 (SSOT) 원칙 — nexus가 계산 도구 단일 진실. n6-architecture는 이론층 (proofs/breakthroughs/reports)만.

**위반 예시 (금지)**:
- ❌ `theory/predictions/verify_anything.hexa`
- ❌ `theory/predictions/some_calculator.hexa`
- ❌ `theory/predictions/*_scanner.hexa`

**올바른 위치**:
- ✓ `nexus/shared/n6/scripts/verify_anything.hexa`
- ✓ `nexus/shared/n6/scripts/some_calculator.hexa`

**배경 (2026-04-11)**: 밀레니엄 세션에서 12개 hexa 계산기를 잘못 이 디렉토리에 작성 → nexus/shared/n6/scripts/로 이관 + 관련 commit d51bb5f0. 이후 재발 방지.

## 절대규칙
- 한글 필수 (.md/주석/커밋)
- HEXA-FIRST (.py 금지)
- **계산기/검증 .hexa는 nexus/shared/n6/scripts/에만 작성 (이 dir 금지)**


## 관련 링크
- 루트: ../CLAUDE.md + INDEX.json
