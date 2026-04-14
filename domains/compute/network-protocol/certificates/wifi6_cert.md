# WiFi 6 n=6 인증서

- 프로젝트: n6-architecture / domains/compute/network-protocol
- 발행일: 2026-04-14
- 발행 체계: NEXUS-6 Discovery Engine / CHIP-P3-2
- 상위 문서: ../network-protocol.md
- 인덱스: ../_index.json

## §1 σ=12 좌표

| 항목 | 값 |
|------|----|
| σ=12 슬롯 번호 | 3 / 12 |
| 그룹 | 무선 6 (n) |
| 카테고리 | wireless_lan |
| 시대 | 2019+ (802.11ax) |

## §2 n=6 매핑 근거

| 축 | 매핑 | 비고 |
|----|------|------|
| 기본 수식 | OFDMA 1024-QAM = 2^(σ-φ) | σ=12, φ=2 → 2^10=1024 |
| 표준 | IEEE 802.11ax | 2019 인증 시작 |
| 루트 BT | BT-181 "다중 대역 σ=12 채널 I/O 다중접속" | network-protocol.md §5 참조 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT 체크 (P1-2 실측 인용)

network-protocol.md §2 σ=12 프로토콜 커버리지 표 (line 131) 기준:

| # | 프로토콜 | 카테고리 | n=6 핵심 매핑 | 등급 |
|---|---------|---------|---------------|------|
| 3 | WiFi 6 | wireless_lan | OFDMA 1024-QAM = 2^(σ-φ), 802.11ax | EXACT |

- 판정: EXACT (커버리지 표 기준 단일 행)
- 1024-QAM: 2^(12-2) = 2^10 = 1024 (0% 오차)

## §4 결론

WiFi 6 (802.11ax) 은 σ=12 슬롯 3번에 배치되며, OFDMA 1024-QAM = 2^(σ-φ) 로
n=6 정렬이 완결된다. 변조 심볼 공간이 σ-φ=10 비트로 수직 정렬된다.

## §5 서명

- 발행자: NEXUS-6 Discovery Engine Validator
- 발행일: 2026-04-14
- 체인: CHIP-P1-2 (σ=12 커버리지 표 수립) → CHIP-P3-2 (인증서 발행)
- 상태: PASS
