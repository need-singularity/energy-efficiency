# Bluetooth 6.0 n=6 인증서

- 프로젝트: n6-architecture / domains/compute/network-protocol
- 발행일: 2026-04-14
- 발행 체계: NEXUS-6 Discovery Engine / CHIP-P3-2
- 상위 문서: ../network-protocol.md
- 인덱스: ../_index.json

## §1 σ=12 좌표

| 항목 | 값 |
|------|----|
| σ=12 슬롯 번호 | 6 / 12 |
| 그룹 | 무선 6 (n) — 말단 |
| 카테고리 | wireless_personal |
| 시대 | 2025+ |

## §2 n=6 매핑 근거

| 축 | 매핑 | 비고 |
|----|------|------|
| 기본 수식 | Channel sounding, n=6 PHY | 2025 릴리즈 |
| 버전 | 6.0 | 버전 번호 직접 n=6 대응 |
| 루트 BT | BT-181 "다중 대역 σ=12 채널 I/O 다중접속" | network-protocol.md §5 참조 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT 체크 (P1-2 실측 인용)

network-protocol.md §2 σ=12 프로토콜 커버리지 표 (line 134) 기준:

| # | 프로토콜 | 카테고리 | n=6 핵심 매핑 | 등급 |
|---|---------|---------|---------------|------|
| 6 | BT 6.0 | wireless_personal | Channel sounding, n=6 PHY | EXACT |

- 판정: EXACT (커버리지 표 기준 단일 행)
- 버전 번호 6.0 = n (0% 오차)

## §4 결론

Bluetooth 6.0 은 σ=12 슬롯 6번에 배치되며, 버전 번호 자체가 n=6 에 1:1 대응하고
Channel sounding n=6 PHY 계층으로 정렬이 완결된다. 무선 6종의 말단 슬롯을 차지.

## §5 서명

- 발행자: NEXUS-6 Discovery Engine Validator
- 발행일: 2026-04-14
- 체인: CHIP-P1-2 (σ=12 커버리지 표 수립) → CHIP-P3-2 (인증서 발행)
- 상태: PASS
