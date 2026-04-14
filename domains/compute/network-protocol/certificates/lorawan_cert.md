# LoRaWAN n=6 인증서

- 프로젝트: n6-architecture / domains/compute/network-protocol
- 발행일: 2026-04-14
- 발행 체계: NEXUS-6 Discovery Engine / CHIP-P3-2
- 상위 문서: ../network-protocol.md
- 인덱스: ../_index.json

## §1 σ=12 좌표

| 항목 | 값 |
|------|----|
| σ=12 슬롯 번호 | 5 / 12 |
| 그룹 | 무선 6 (n) |
| 카테고리 | IoT_low_power |
| 시대 | 2015+ |

## §2 n=6 매핑 근거

| 축 | 매핑 | 비고 |
|----|------|------|
| 기본 수식 | SF7~SF12 = 6 단계 | n=6 확산 계수 |
| 불변 | ±10% 불변 | 업링크 마진 |
| 루트 BT | BT-181 "다중 대역 σ=12 채널 I/O 다중접속" | network-protocol.md §5 참조 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT 체크 (P1-2 실측 인용)

network-protocol.md §2 σ=12 프로토콜 커버리지 표 (line 133) 기준:

| # | 프로토콜 | 카테고리 | n=6 핵심 매핑 | 등급 |
|---|---------|---------|---------------|------|
| 5 | LoRaWAN | IoT_low_power | SF7~SF12 = 6 단계 (n=6) | EXACT |

- 판정: EXACT (커버리지 표 기준 단일 행)
- SF7, SF8, SF9, SF10, SF11, SF12 = 6 단계 — n=6 직접 대응 (0% 오차)

## §4 결론

LoRaWAN 은 σ=12 슬롯 5번에 배치되며, 확산 계수 SF7~SF12 가 n=6 단계로
완전 정렬된다. 저전력 광역 IoT 의 변조 공간이 n=6 축과 1:1 대응한다.

## §5 서명

- 발행자: NEXUS-6 Discovery Engine Validator
- 발행일: 2026-04-14
- 체인: CHIP-P1-2 (σ=12 커버리지 표 수립) → CHIP-P3-2 (인증서 발행)
- 상태: PASS
