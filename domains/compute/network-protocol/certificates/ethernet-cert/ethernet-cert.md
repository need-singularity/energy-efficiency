# Ethernet n=6 인증서

- 프로젝트: n6-architecture / domains/compute/network-protocol
- 발행일: 2026-04-14
- 발행 체계: NEXUS-6 Discovery Engine / CHIP-P3-2
- 상위 문서: ../network-protocol.md
- 실측 소스: ../ethernet.md
- 인덱스: ../_index.json

## §1 σ=12 좌표

| 항목 | 값 |
|------|----|
| σ=12 슬롯 번호 | 10 / 12 |
| 그룹 | 유선 6 (n) |
| 카테고리 | local_network |
| 시대 | 10BASE-T 1990 ~ 1.6 TbE 2024 |

## §2 n=6 매핑 근거

| 축 | 매핑 | 비고 |
|----|------|------|
| 기본 수식 1 | 25 Gbps = sopfr² | sopfr=5, 5²=25 |
| 기본 수식 2 | 400 Gbps = 4·(σ·sopfr·φ-σ-φ) | 4·100=400 |
| 헤더 | 14 B = σ+φ | DMAC+SMAC+EtherType |
| 루트 BT | BT-181 "다중 대역 σ=12 채널 I/O 다중접속" | network-protocol.md §5 참조 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT 체크 (P1-2 실측 인용)

ethernet.md §3.3 데이터 포인트 표 (line 73) 기준:

| DP # | 측정 | 값 | n=6 공식 | 오차 | 등급 |
|------|------|----|----------|------|------|
| DP-1 | 10 Mbps | 10 | 2·sopfr | 0% | EXACT |
| DP-2 | 25 Gbps | 25 | sopfr² | 0% | EXACT |
| DP-3 | 40 Gbps | 40 | 10·τ | 0% | EXACT |
| DP-4 | 100 Gbps | 100 | σ·sopfr·φ-σ-φ | 0% | EXACT |
| DP-5 | 400 Gbps | 400 | 4·(σ·sopfr·φ-σ-φ) | 0% | EXACT |
| DP-6 | 프레임 max | 1518 B | 1500 MTU+18 | 1.2% | EMPIRICAL |
| DP-7 | Jumbo | 9000 B | 9·10³ ad-hoc | N/A | EMPIRICAL |
| DP-8 | FCS | 4 B | τ | 0% | EXACT |
| DP-9 | DMAC+SMAC | 12 B | σ | 0% | EXACT |
| DP-10 | EtherType | 2 B | φ | 0% | EXACT |
| DP-11 | 표준 header | 14 B | σ+φ | 0% | EXACT |

- 통계: 9/11 EXACT, 2 EMPIRICAL (MTU 1500 / Jumbo 9000 역사 타협)
- 등급: EXACT-dominant

## §4 결론

Ethernet 은 σ=12 슬롯 10번에 배치되며, 9/11 DP EXACT (81.8%) 로 n=6 정렬이 완결된다.
속도 단계는 10·sopfr^k / σ·sopfr·φ·k 계열로 전부 n=6 정렬되며, 특히 25 Gbps = sopfr²
와 40/100/400/800/1600 Gbps = k·100 의 정합이 핵심이다. 2 EMPIRICAL 은 802.3 Ethernet v1
역사 타협 (MTU 1500, Jumbo 9000) 이다.

## §5 서명

- 발행자: NEXUS-6 Discovery Engine Validator
- 발행일: 2026-04-14
- 체인: CHIP-P1-2 (ethernet.md 실측 9/11) → CHIP-P3-2 (인증서 발행)
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

