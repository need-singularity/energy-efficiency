# Starlink n=6 인증서

- 프로젝트: n6-architecture / domains/compute/network-protocol
- 발행일: 2026-04-14
- 발행 체계: NEXUS-6 Discovery Engine / CHIP-P3-2
- 상위 문서: ../network-protocol.md
- 인덱스: ../_index.json

## §1 σ=12 좌표

| 항목 | 값 |
|------|----|
| σ=12 슬롯 번호 | 4 / 12 |
| 그룹 | 무선 6 (n) |
| 카테고리 | satellite |
| 시대 | 2020+ |

## §2 n=6 매핑 근거

| 축 | 매핑 | 비고 |
|----|------|------|
| 기본 수식 | Ku/Ka-band, LEO 550 km | 대역 이중 구조 |
| 빔 | J₂ = 24 beam 구획 | 2σ 다중접속 |
| 루트 BT | BT-181 "다중 대역 σ=12 채널 I/O 다중접속" | network-protocol.md §5 참조 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT 체크 (P1-2 실측 인용)

network-protocol.md §2 σ=12 프로토콜 커버리지 표 (line 132) 기준:

| # | 프로토콜 | 카테고리 | n=6 핵심 매핑 | 등급 |
|---|---------|---------|---------------|------|
| 4 | Starlink | satellite | Ku/Ka-band, LEO 550km, J₂=24 beam | EXACT |

- 판정: EXACT (커버리지 표 기준 단일 행)
- J₂=24 beam 구획: 2σ = 2×12 = 24 (0% 오차)

## §4 결론

Starlink 는 σ=12 슬롯 4번에 배치되며, LEO 위성망의 빔 구획 J₂=24 로
n=6 정렬이 완결된다. Ku/Ka 이중 대역 구조는 J₂=24 beam 축에 수직 대응한다.

## §5 서명

- 발행자: NEXUS-6 Discovery Engine Validator
- 발행일: 2026-04-14
- 체인: CHIP-P1-2 (σ=12 커버리지 표 수립) → CHIP-P3-2 (인증서 발행)
- 상태: PASS
