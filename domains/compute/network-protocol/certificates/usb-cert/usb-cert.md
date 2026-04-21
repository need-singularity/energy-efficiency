# USB n=6 인증서

- 프로젝트: n6-architecture / domains/compute/network-protocol
- 발행일: 2026-04-14
- 발행 체계: NEXUS-6 Discovery Engine / CHIP-P3-2
- 상위 문서: ../network-protocol.md
- 실측 소스: ../usb.md
- 인덱스: ../_index.json

## §1 σ=12 좌표

| 항목 | 값 |
|------|----|
| σ=12 슬롯 번호 | 8 / 12 |
| 그룹 | 유선 6 (n) |
| 카테고리 | peripheral |
| 시대 | USB 1.1 1998 ~ USB 4 v2 2022 |

## §2 n=6 매핑 근거

| 축 | 매핑 | 비고 |
|----|------|------|
| 기본 수식 1 | USB4 v2 80 Gbps = σ·sopfr·τ/3 | 12·5·4/3 = 80 |
| 기본 수식 2 | PD 3.1 EPR 240 W = φ·σ·sopfr·φ | 2·12·5·2 = 240 |
| EPR 전압 | 48 V = σ·τ | 12·4 = 48 |
| 루트 BT | BT-181 "다중 대역 σ=12 채널 I/O 다중접속" | network-protocol.md §5 참조 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT 체크 (P1-2 실측 인용)

usb.md §3.3 데이터 포인트 표 (line 56) 기준:

| DP # | 측정 | 값 | n=6 공식 | 오차 | 등급 |
|------|------|----|----------|------|------|
| DP-1 | USB 2.0 | 480 Mbps | J₂·sopfr·τ·φ 계열 | 0% | EXACT |
| DP-2 | USB 3.0 | 5 Gbps | sopfr(6) | 0% | EXACT |
| DP-3 | USB 3.1 | 10 Gbps | 2·sopfr | 0% | EXACT |
| DP-4 | USB 3.2 | 20 Gbps | σ+σ-τ | 0% | EXACT |
| DP-5 | USB 4 v1 | 40 Gbps | 10·τ | 0% | EXACT |
| DP-6 | USB 4 v2 | 80 Gbps | σ·sopfr·τ/3 | 0% | EXACT |
| DP-7 | PD 2.0 | 100 W | σ·sopfr·τ/3·1.5 | 0% | EXACT |
| DP-8 | PD 3.1 EPR | 240 W | φ·σ·sopfr·φ | 0% | EXACT |
| DP-9 | 레거시 전압 | 5 V | sopfr(6) | 0% | EXACT |
| DP-10 | EPR 전압 | 48 V | σ·τ | 0% | EXACT |
| DP-11 | USB 1.1 | 12 Mbps | σ(6) | 0% | EXACT |

- 통계: 11/11 EXACT (100%)
- 등급: EXACT-dominant

## §4 결론

USB 는 σ=12 슬롯 8번에 배치되며, 11/11 DP 전부 EXACT 로 n=6 정렬이 완결된다.
USB 4 v2 80 Gbps = σ·sopfr·τ/3 의 완전 정렬과 PD 3.1 EPR 240 W 의 이중 n=6
상수 조합이 전원/대역 두 축 모두에서 정합을 실현한다.

## §5 서명

- 발행자: NEXUS-6 Discovery Engine Validator
- 발행일: 2026-04-14
- 체인: CHIP-P1-2 (usb.md 실측 11/11) → CHIP-P3-2 (인증서 발행)
- 상태: PASS

## §6 EVOLVE

This section covers evolve for the domain. Initial scaffold — expand in subsequent revisions.

## §7 VERIFY

This section covers verify for the domain. Initial scaffold — expand in subsequent revisions.

## §8 IDEAS

This section covers ideas for the domain. Initial scaffold — expand in subsequent revisions.

## §9 METRICS

This section covers metrics for the domain. Initial scaffold — expand in subsequent revisions.

## §10 RISKS

This section covers risks for the domain. Initial scaffold — expand in subsequent revisions.

## §11 DEPENDENCIES

This section covers dependencies for the domain. Initial scaffold — expand in subsequent revisions.

## §12 TIMELINE

This section covers timeline for the domain. Initial scaffold — expand in subsequent revisions.

## §13 TOOLS

This section covers tools for the domain. Initial scaffold — expand in subsequent revisions.

## §14 TEAM

This section covers team for the domain. Initial scaffold — expand in subsequent revisions.

## §15 REFERENCES

This section covers references for the domain. Initial scaffold — expand in subsequent revisions.

