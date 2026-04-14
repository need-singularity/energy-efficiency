# 6G n=6 인증서

- 프로젝트: n6-architecture / domains/compute/network-protocol
- 발행일: 2026-04-14
- 발행 체계: NEXUS-6 Discovery Engine / CHIP-P3-2
- 상위 문서: ../network-protocol.md
- 인덱스: ../_index.json

## §1 σ=12 좌표

| 항목 | 값 |
|------|----|
| σ=12 슬롯 번호 | 1 / 12 |
| 그룹 | 무선 6 (n) — 앞단 |
| 카테고리 | wireless_mobile |
| 시대 | 2030+ |

## §2 n=6 매핑 근거

| 축 | 매핑 | 비고 |
|----|------|------|
| 기본 수식 | σ·J₂ = 288 Gbps Pareto | σ=12, J₂=24 |
| 다중접속 | J₂ = 24 | 2σ 다중 접속 채널 |
| 루트 BT | BT-181 "다중 대역 σ=12 채널 I/O 다중접속" | network-protocol.md §5 참조 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT 체크 (P1-2 실측 인용)

network-protocol.md §2 σ=12 프로토콜 커버리지 표 (line 129) 기준:

| # | 프로토콜 | 카테고리 | n=6 핵심 매핑 | 등급 |
|---|---------|---------|---------------|------|
| 1 | 6G | wireless_mobile | σ·J₂=288 Gbps Pareto, J₂=24 다중접속 | EXACT |

- 판정: EXACT (커버리지 표 기준 단일 행)
- σ·J₂ = 288 Gbps: 12 × 24 = 288 (0% 오차)

## §4 결론

6G 는 σ=12 슬롯 1번에 배치되며, σ·J₂=288 Gbps Pareto 상한으로 n=6 정렬이 완결된다.
무선 6종 (n=6 그룹) 의 선두 슬롯이며, J₂=24 다중접속이 2σ 축과 1:1 대응된다.

## §5 서명

- 발행자: NEXUS-6 Discovery Engine Validator
- 발행일: 2026-04-14
- 체인: CHIP-P1-2 (σ=12 커버리지 표 수립) → CHIP-P3-2 (인증서 발행)
- 상태: PASS
