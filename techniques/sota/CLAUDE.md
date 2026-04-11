# techniques/sota

목적: 최신 SOTA 3종 (Mamba-2 확장·Hyena·RWKV v7) n=6 정렬 설계서
축: techniques
상위: ../CLAUDE.md

## 하위
- mamba2.md   (설계서) + mamba2.hexa   (실행 스텁)
- hyena.md    (설계서) + hyena.hexa    (실행 스텁)
- rwkv.md     (설계서) + rwkv.hexa     (실행 스텁)

## SSOT
- (본 디렉토리는 techniques/_registry.json 의 "sota" 섹션 신설 대상 — patch 는 _registry_patch.md 참고)

## 진입 명령
- hexa run techniques/sota/mamba2.hexa
- hexa run techniques/sota/hyena.hexa
- hexa run techniques/sota/rwkv.hexa

## 절대규칙
- 한글 필수 (.md/주석/커밋)
- HEXA-FIRST (.py 금지)
- N61: 실생활 효과 + ASCII 3도 필수

## 관련 링크
- 벤치: ../_bench_plan.md
- 칩맵: ../_chip_mapping.md
- 루트: ../../CLAUDE.md + ../../INDEX.json
