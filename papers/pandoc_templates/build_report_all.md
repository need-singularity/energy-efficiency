---
task: PAPER-P5-3
date: 2026-04-14
phase: P5 Mk.III-α
status: partial
env:
  pandoc: 3.9.0.2
  xelatex: XeTeX 3.141592653-2.6-0.999998 (TeX Live 2026)
  os: darwin 24.6.0
---

# PAPER-P5-3 pandoc PDF 전량 빌드 리포트

## 요약

| 항목 | 값 |
|---|---|
| 대상 논문 수 | 127 편 (papers/n6-*-paper.md) |
| 빌드 성공 | 16 편 |
| 빌드 시도 | 최소 13 편 (_build_logs/*.log) |
| 성공률 | 12.6% |
| gate_exit criterion | 100편+ (FAIL) |
| fail_action | 정직 기록 + 다음 phase 이월 (P6 포함) |

## 스크립트

- `papers/pandoc_templates/build_all.sh` 완성 (142줄)
- xargs -P 병렬, venue_template 매핑, bash 3.2 호환
- **결함**: pandoc 에 개별 timeout 미적용 → 일부 편 무한 hang 가능

## 환경

정상. `pandoc 3.9.0.2` + `xelatex TeX Live 2026` 확인.

## 빌드된 논문 16편

```
n6-acoustics / n6-advanced-packaging / n6-aerospace-transport / n6-agi-architecture
n6-ai-17-techniques-experimental / n6-ai-ethics-governance / n6-ai-techniques-68-integrated
n6-anima-soc / n6-aquaculture / n6-arch-adaptive-evolution / n6-arch-adaptive-homeostasis
n6-arch-evolution-ouroboros / n6-arch-quantum-design / n6-arch-selforg-design / ...
```

(정확한 16편 목록: `ls papers/pandoc_templates/output/*.pdf`)

## 중단 원인 추정

1. 첫 실행 (23:58:40): 9편 tee 기록 + 13편 log + 16편 PDF 산출 후 중단. 특정 편 xelatex hang.
2. 재실행: macOS `timeout` 명령 미지원 → 즉시 실패.

## 개선 방안 (후속 P6 이월)

- [ ] `build_one()` 에 `gtimeout 30s pandoc ...` 적용 (brew install coreutils)
- [ ] 실패 편 재시도 로직 (재귀 호출)
- [ ] hang 원인 조사: xelatex 로그 `_build_logs/` 개별 확인
- [ ] 127편 중 미빌드 111편 식별 후 incremental 재빌드

## 정직한 한계 (n=6 원칙)

이 task는 gate criterion (100+ 성공) 미달. 스크립트는 완성되었으나 **실행 환경의 timeout 도구 부재**로 hang 방지 불가. 거짓 성공 주장 대신 "12.6% 부분 빌드 + 재실행 가이드 제공" 으로 공시.

Gate exit fail_action 적용: **실패 항목(111편 미빌드) 정직 기록 → P6 에서 재시도.**
