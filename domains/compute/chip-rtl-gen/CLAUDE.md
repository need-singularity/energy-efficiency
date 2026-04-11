# chip-rtl-gen — CLAUDE 가이드

축: **compute**

## 파일
- `chip-rtl-gen.md` — 15섹션 통합 본문 (AI-native RTL 자동생성기 설계서)
- `verify.hexa` — σ·φ = n·τ + 원시연산 6종 + 기법 16종 일관성 검증
- `CLAUDE.md` — 본 가이드

## 사용법
- 본문 읽기: 섹션 2 목표 → 5 연산자 추상화 → 6 템플릿 매핑 → 7 파이프라인
- 검증 실행: `hexa verify.hexa`
- 진화 단계: 섹션 9 Mk.I~V
- 예측 추적: 섹션 10

## 연관 도메인
- `chip-dse-pipeline` — DSE 5종 연동 (PIM/3D/Photonic/Wafer/Superconducting)
- `chip-isa-n6` — RISC-V 확장 ISA (생성 RTL 의 대상 ISA)
- `chip-npu-n6` — NPU 스펙 (본 생성기의 소비자)

## 자원
- 기존 RTL: `nexus/origins/hexa-rtl/rtl/` 6 모듈
- 기법 SSOT: `techniques/_registry.json` 66 기법
- 템플릿 SSOT: `shared/config/rtl_templates.json` (설계서 기준, 생성 예정)

## BT 연결
- BT-28 (컴퓨팅 사다리), BT-55 (HBM), BT-58 (σ-τ=8), BT-69 (칩렛), BT-89 (광)
- 돌파 발생 시: `blowup.hexa chip-rtl-gen 3` + `growth_bus.jsonl`

## 규칙
- 원본 섹션 유지, 신규는 해당 섹션 뒤에 추가
- 레거시는 부록 B에만
- 한글 필수 (R-한글) / HEXA-FIRST (R1) / AI-NATIVE (R12)
