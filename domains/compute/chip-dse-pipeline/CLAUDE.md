# chip-dse-pipeline — CLAUDE 가이드

축: **compute**

## 파일
- `chip-dse-pipeline.md` — 15섹션 통합 본문 (5 DSE 통합 분석 + 확장)
- `verify.hexa` — σ·φ=n·τ + 단계=5 + 조합=7,776/단계 검증
- `CLAUDE.md` — 본 가이드

## 사용법
- 본문 읽기: 섹션 2 목표 → 5 5종 분석 → 6 파이프라인 → 7 확장점
- 검증 실행: `hexa verify.hexa`
- 실제 실행 (Mk.II 이후): `nexus dse universal --pipeline`
- 진화 단계: 섹션 9 Mk.I~V

## 연관 도메인
- `chip-rtl-gen` — Phase 3 에서 템플릿 파라미터 주입 대상
- `chip-isa-n6` — ISA 결정의 하드웨어 근거
- `chip-npu-n6` — NPU 파이프라인 선택 근거
- `chip-architecture` — 상위 칩 아키텍처 가설 컨테이너

## 자원
- 5 DSE TOML: `nexus/origins/universal-dse/domains/chip-*.toml` (dca8f87f)
- 교차 융합: `cross_dse_fusion.hexa` (CROSS_DSE 골화)
- 엔진: `nexus/src/cmd/dse/universal.rs`
- SSOT: `shared/config/dse_pipeline.json` (신규 예정)

## BT 연결
- BT-28, BT-37, BT-55, BT-58, BT-69, BT-89, BT-90, BT-93
- 돌파 발생 시: `blowup.hexa chip-dse-pipeline 3` + `growth_bus.jsonl`

## 규칙
- 원본 섹션 유지, 5 TOML 수정 금지 (R5 SSOT)
- 신규는 해당 섹션 뒤에 추가
- 한글 필수 (R-한글) / HEXA-FIRST (R1)
