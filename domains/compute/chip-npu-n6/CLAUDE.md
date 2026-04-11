# chip-npu-n6 — CLAUDE 가이드

축: **compute**

## 파일
- `chip-npu-n6.md` — 15섹션 통합 본문 (n=6 정합 NPU 사양 초안)
- `verify.hexa` — SM=24, TC=4, MAC=144, 파이프=12, 메모리=4, NoC=n·σ, Egyptian=1 검증
- `CLAUDE.md` — 본 가이드

## 사용법
- 본문 읽기: 섹션 2 목표 → 5 블록도 → 6 컴퓨트 → 7 파이프라인 → 8 메모리 → 9 데이터플로
- 검증 실행: `hexa verify.hexa`
- 진화 단계: 섹션 11 Mk.I~V
- 실측 벤치마크: Mk.V (FPGA → ASIC)

## 연관 도메인
- `chip-architecture` — H-CHIP-1~28 상위 가설 (본 스펙의 근거)
- `chip-rtl-gen` — 본 스펙을 타겟으로 RTL 생성
- `chip-isa-n6` — Xn6 명령어가 본 NPU 에 dispatch
- `chip-dse-pipeline` — 5 DSE 결과가 본 NPU 파라미터 근거

## 자원
- 기존 SM RTL: `nexus/origins/hexa-rtl/rtl/riscv_n6_core.hexa` (12-stage 파이프 재사용)
- Egyptian router: `nexus/origins/hexa-rtl/rtl/egyptian_moe.hexa`
- 메모리 ctrl: `nexus/origins/hexa-rtl/rtl/egyptian_mem_ctrl.hexa`
- 상위 비전: `domains/compute/chip-architecture/chip-architecture.md`

## BT 연결
- BT-28, BT-55, BT-58, BT-69, BT-89, BT-90, BT-134, BT-380
- 돌파 발생 시: `blowup.hexa chip-npu-n6 3` + `growth_bus.jsonl`

## 규칙
- n=6 정합 상수만 사용 — 비정합 수치 금지
- AI-NATIVE (R12) — Phi6/Egyptian/Boltzmann 전용 유닛
- HEXA-FIRST (R1)
- 한글 필수 (R-한글)
