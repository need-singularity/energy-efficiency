---
task: PAPER-P5-3 (P6 이월 해소)
date: 2026-04-14
phase: P5 Mk.III-α (이월 해소) → P6 Mk.III-β
status: success
env:
  pandoc: 3.9.0.2
  xelatex: XeTeX 3.141592653-2.6-0.999998 (TeX Live 2026)
  timeout: perl alarm 45s (macOS gtimeout 부재 대응)
---

# PAPER-P5-3 pandoc 전량 빌드 리포트 (최종)

## 요약

| 항목 | 값 |
|---|---|
| 대상 논문 수 | 129 편 |
| 빌드 성공 | **129 편 (100%)** |
| 총 경과 | 156s (4-way 병렬) |
| gate criterion | 100편+ → **PASS** |

## 해소 경과

1. **1차 시도** (16/127): macOS `timeout` 미지원 → 일부 편 xelatex hang
2. **2차 시도** (128/129): `perl -e 'alarm 45; exec @ARGV'` wrapper 도입 → 1편만 실패
3. **실패 1편 수정**: n6-boundary-metatheory-paper `\sopfr` → `\mathrm{sopfr}` (TeX 미정의 매크로)
4. **3차 시도** (129/129): 완전 성공

## 기술 개선

- `build_all.sh` line 94: `perl -e 'alarm 45; exec @ARGV' pandoc ...` 적용
- macOS/Linux 공통 호환 (gtimeout 의존성 제거)
- LaTeX 사용자 정의 매크로는 `\mathrm{name}` 형식 권장

## 환경 경고

CJK 폰트 fallback 경고 발생 (Menlo 한글 미지원) — 렌더링은 성공, Apple SD Gothic Neo 적용됨.
