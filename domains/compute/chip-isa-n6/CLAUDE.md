# chip-isa-n6 — CLAUDE 가이드

축: **compute**

## 파일
- `chip-isa-n6.md` — 15섹션 통합 본문 (Xn6 RISC-V 확장 명령 제안서)
- `verify.hexa` — J₂=24 명령 슬롯, funct3×variant=24, CSR=4 검증
- `CLAUDE.md` — 본 가이드

## 사용법
- 본문 읽기: 섹션 2 목표 → 5 opcode 공간 → 6 명령어 세트 → 9 툴체인
- 검증 실행: `hexa verify.hexa`
- 진화 단계: 섹션 10 Mk.I~V
- 디코더: `nexus/origins/hexa-rtl/rtl/xn6_decoder.hexa` (Mk.II 이후)

## 연관 도메인
- `chip-rtl-gen` — 원시연산 6종 SSOT 공유
- `chip-npu-n6` — xn6.gemm 이 dispatch 하는 연산 대상
- `chip-architecture` — H-CHIP-23 R-score 모니터와 CSR 연동

## 자원
- RISC-V ISA Manual — custom opcode 0x0B/0x2B/0x5B/0x7B
- 기존 riscv_n6_core.hexa — 별개 24비트 커스텀 ISA (공존)
- 기존 hexalang_decoder.hexa — 53 키워드 CAM (참고)
- SSOT: `shared/config/xn6_isa.json` (신규 예정)

## BT 연결
- BT-28, BT-58 (σ-τ=8), BT-134, BT-380
- 돌파 발생 시: `blowup.hexa chip-isa-n6 3` + `growth_bus.jsonl`

## 규칙
- RISC-V 표준 준수 — custom 영역 외 변경 금지
- 어셈블리 수동 작성 금지 — intrinsic/@xn6 attr 만 (R12)
- 한글 필수 (R-한글) / HEXA-FIRST (R1)
