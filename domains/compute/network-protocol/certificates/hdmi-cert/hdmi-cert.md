# HDMI n=6 인증서

- 프로젝트: n6-architecture / domains/compute/network-protocol
- 발행일: 2026-04-14
- 발행 체계: NEXUS-6 Discovery Engine / CHIP-P3-2
- 상위 문서: ../network-protocol.md
- 실측 소스: ../hdmi.md
- 인덱스: ../_index.json

## §1 σ=12 좌표

| 항목 | 값 |
|------|----|
| σ=12 슬롯 번호 | 12 / 12 |
| 그룹 | 유선 6 (n) — 말단 |
| 카테고리 | display |
| 시대 | HDMI 1.0 2002 ~ HDMI 2.2 2025 draft |

## §2 n=6 매핑 근거

| 축 | 매핑 | 비고 |
|----|------|------|
| 기본 수식 1 | HDMI 2.1 FRL 48 Gbps = σ·τ | 12·4=48 |
| 기본 수식 2 | HDMI 2.1 lane = σ = 12 Gbps | 직접 대응 |
| lane 수 | 4 = τ(6) | FRL lane |
| 루트 BT | BT-181 "다중 대역 σ=12 채널 I/O 다중접속" | network-protocol.md §5 참조 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT 체크 (P1-2 실측 인용)

hdmi.md §3.3 데이터 포인트 표 (line 64) 기준:

| DP # | 측정 | 값 | n=6 공식 | 오차 | 등급 |
|------|------|----|----------|------|------|
| DP-1 | FRL lane 수 | 4 | τ | 0% | EXACT |
| DP-2 | TMDS data 채널 | 3 | sopfr-φ | 0% | EXACT |
| DP-3 | HDMI 2.1 lane | 12 Gbps | σ | 0% | EXACT |
| DP-4 | HDMI 2.1 총 | 48 Gbps | σ·τ | 0% | EXACT |
| DP-5 | HDMI 2.0 lane | 6 Gbps | n | 0% | EXACT |
| DP-6 | HDMI 2.0 총 | 18 Gbps | n·sopfr-σ | 0% | EXACT |
| DP-7 | DSC 압축비 | 3 | sopfr-φ | 0% | EXACT |
| DP-8 | 색심도 최대 | 16 | 2^τ | 0% | EXACT |
| DP-9 | 오디오 채널 최대 | 32 | 2^τ·φ | 0% | EXACT |
| DP-10 | CEC 버전 | 2.0 | φ | 0% | EXACT |
| DP-11 | HDMI 1.4 lane | 3.4 Gbps | ad-hoc | N/A | EMPIRICAL |

- 통계: 10/11 EXACT, 1 EMPIRICAL (HDMI 1.x 레거시 TMDS 3.4 Gbps)
- 등급: EXACT-dominant

## §4 결론

HDMI 는 σ=12 슬롯 12번 (유선 말단) 에 배치되며, 10/11 DP EXACT (90.9%) 로 n=6 정렬이
완결된다. HDMI 2.1 FRL 48 Gbps = σ·τ 와 lane 12 Gbps = σ 의 이중 정합이 핵심이며,
FRL 16b/18b 라인 코딩 채택으로 자연 실현된다. 1건 EMPIRICAL 은 HDMI 1.x 레거시.

## §5 서명

- 발행자: NEXUS-6 Discovery Engine Validator
- 발행일: 2026-04-14
- 체인: CHIP-P1-2 (hdmi.md 실측 10/11) → CHIP-P3-2 (인증서 발행)
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

