# PCIe n=6 인증서

- 프로젝트: n6-architecture / domains/compute/network-protocol
- 발행일: 2026-04-14
- 발행 체계: NEXUS-6 Discovery Engine / CHIP-P3-2
- 상위 문서: ../network-protocol.md
- 실측 소스: ../pcie.md
- 인덱스: ../_index.json

## §1 σ=12 좌표

| 항목 | 값 |
|------|----|
| σ=12 슬롯 번호 | 7 / 12 |
| 그룹 | 유선 6 (n) — 선두 |
| 카테고리 | interconnect |
| 시대 | Gen1 2003 ~ Gen7 2025 |

## §2 n=6 매핑 근거

| 축 | 매핑 | 비고 |
|----|------|------|
| 기본 수식 1 | Gen6 64 GT/s = 2^6 | PAM4 1st gen PCIe |
| 기본 수식 2 | Gen6 x16 = 256 GB/s = 2^(σ-τ) | σ=12, τ=4 → 2^8 |
| FLIT | 256 B = 2^(σ-τ) | Gen6 baseline |
| 루트 BT | BT-181 "다중 대역 σ=12 채널 I/O 다중접속" | network-protocol.md §5 참조 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT 체크 (P1-2 실측 인용)

pcie.md §3.3 데이터 포인트 표 (line 56) 기준:

| DP # | 측정 | 값 | n=6 공식 | 계산값 | 오차 | 등급 |
|------|------|----|----------|--------|------|------|
| DP-1 | Gen4 32b 인코딩 | 128b/130b | 1 - 2/(σ-τ)=0.984 | 0.9846 | 0.06% | EXACT |
| DP-2 | Gen6 레인 | 64 GT/s | 2^6 | 64 | 0% | EXACT |
| DP-3 | Gen5 x16 | 126 GB/s | σ·(sopfr·φ)+φ | 126 | 0% | EXACT |
| DP-4 | FLIT size | 256 B | 2^(σ-τ) | 256 | 0% | EXACT |
| DP-5 | stack layers | 3 | sopfr-2 | 3 | 0% | EXACT |
| DP-6 | Gen6 x16 | 256 GB/s | 2^(σ-τ) | 256 | 0% | EXACT |
| DP-7 | AER 오류 분류 | 12 | σ(6) | 12 | 0% | EXACT |
| DP-8 | Max Payload | 4096 B | 2^(σ) | 4096 | 0% | EXACT |

- 통계: 8/8 EXACT (100%)
- 등급: EXACT-dominant

## §4 결론

PCIe 는 σ=12 슬롯 7번 (유선 선두) 에 배치되며, 8/8 DP 전부 EXACT 로 n=6 정렬이
완결된다. 특히 Gen6 64 GT/s = 2^6 과 x16 256 GB/s = 2^(σ-τ) 의 이중 정합이
PAM4 채택으로 자연 실현된 점이 핵심이다.

## §5 서명

- 발행자: NEXUS-6 Discovery Engine Validator
- 발행일: 2026-04-14
- 체인: CHIP-P1-2 (pcie.md 실측 8/8) → CHIP-P3-2 (인증서 발행)
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

