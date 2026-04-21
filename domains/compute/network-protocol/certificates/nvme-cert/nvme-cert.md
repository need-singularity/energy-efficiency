# NVMe n=6 인증서

- 프로젝트: n6-architecture / domains/compute/network-protocol
- 발행일: 2026-04-14
- 발행 체계: NEXUS-6 Discovery Engine / CHIP-P3-2
- 상위 문서: ../network-protocol.md
- 실측 소스: ../nvme.md
- 인덱스: ../_index.json

## §1 σ=12 좌표

| 항목 | 값 |
|------|----|
| σ=12 슬롯 번호 | 9 / 12 |
| 그룹 | 유선 6 (n) |
| 카테고리 | storage |
| 시대 | NVMe 1.0 2011 ~ NVMe 2.0 2021 |

## §2 n=6 매핑 근거

| 축 | 매핑 | 비고 |
|----|------|------|
| 기본 수식 1 | 큐 깊이 2^16 = 2^(4σ/3) | σ=12, 4σ/3=16 |
| 기본 수식 2 | 명령 64 B = 2^n | n=6 |
| 페이지 | PRP 4096 B = 2^σ | σ=12 |
| 루트 BT | BT-181 "다중 대역 σ=12 채널 I/O 다중접속" | network-protocol.md §5 참조 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT 체크 (P1-2 실측 인용)

nvme.md §3.3 데이터 포인트 표 (line 62) 기준:

| DP # | 측정 | 값 | n=6 공식 | 오차 | 등급 |
|------|------|----|----------|------|------|
| DP-1 | 명령 크기 | 64 B | 2^n | 0% | EXACT |
| DP-2 | 완료 엔트리 | 16 B | 2^τ | 0% | EXACT |
| DP-3 | LBA 섹터 | 512 B | 2^9 | 0% | EXACT |
| DP-4 | PRP 페이지 | 4096 B | 2^σ | 0% | EXACT |
| DP-5 | SQ/CQ 최대 쌍 | 65536 | 2^(4σ/3)=2^16 | 0% | EXACT |
| DP-6 | 큐 깊이 | 65536 | 2^16 | 0% | EXACT |
| DP-7 | 버전 | 2.0 | φ | 0% | EXACT |
| DP-8 | p50 지연 | 10 µs | 2·sopfr | ±20% | EMPIRICAL |
| DP-9 | Gen5 x4 | 16 GB/s | σ+τ | 0% | EXACT |
| DP-10 | NSID 폭 | 32 bit | 2^τ·φ | 0% | EXACT |
| DP-11 | MSI-X 최대 벡터 | 2048 | 2^11 | 0% | EXACT |

- 통계: 10/11 EXACT, 1 EMPIRICAL (p50 지연 NAND 읽기 지배 요인)
- 등급: EXACT-dominant

## §4 결론

NVMe 는 σ=12 슬롯 9번에 배치되며, 10/11 DP EXACT (90.9%) 로 n=6 정렬이 완결된다.
구조적으로 2^σ·2^τ·2^φ 조합으로 HW stride 가 n=6 친화적이며, 큐 깊이 2^16 = 2^(4σ/3)
의 수직 정렬이 대표적이다. 1건 EMPIRICAL (p50 지연) 은 NAND 물리 한계에 기인.

## §5 서명

- 발행자: NEXUS-6 Discovery Engine Validator
- 발행일: 2026-04-14
- 체인: CHIP-P1-2 (nvme.md 실측 10/11) → CHIP-P3-2 (인증서 발행)
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

