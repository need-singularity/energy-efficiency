# DisplayPort n=6 인증서

- 프로젝트: n6-architecture / domains/compute/network-protocol
- 발행일: 2026-04-14
- 발행 체계: NEXUS-6 Discovery Engine / CHIP-P3-2
- 상위 문서: ../network-protocol.md
- 실측 소스: ../displayport.md
- 인덱스: ../_index.json

## §1 σ=12 좌표

| 항목 | 값 |
|------|----|
| σ=12 슬롯 번호 | 11 / 12 |
| 그룹 | 유선 6 (n) |
| 카테고리 | display |
| 시대 | DP 1.0 2006 ~ DP 2.1 2022 |

## §2 n=6 매핑 근거

| 축 | 매핑 | 비고 |
|----|------|------|
| 기본 수식 1 | UHBR20 = 2^τ+τ = 20 Gbps | τ=4, 16+4=20 |
| 기본 수식 2 | 4-lane 총 = σ·sopfr·τ/3 = 80 | 12·5·4/3=80 |
| lane 수 | 4 = τ(6) | Main Link lane |
| 루트 BT | BT-181 "다중 대역 σ=12 채널 I/O 다중접속" | network-protocol.md §5 참조 |
| atlas.n6 grade | `@R n6-dse-network-protocol = done dse :: dse [10]` | line 13667 |

## §3 EXACT 체크 (P1-2 실측 인용)

displayport.md §3.3 데이터 포인트 표 (line 60) 기준:

| DP # | 측정 | 값 | n=6 공식 | 오차 | 등급 |
|------|------|----|----------|------|------|
| DP-1 | Main lane 수 | 4 | τ(6) | 0% | EXACT |
| DP-2 | UHBR20 lane | 20 Gbps | 2^τ+τ | 0% | EXACT |
| DP-3 | UHBR20 4-lane | 80 Gbps | σ·sopfr·τ/3 | 0% | EXACT |
| DP-4 | DSC 압축비 | 3 | sopfr-φ | 0% | EXACT |
| DP-5 | MST 스트림 | 63 | 2^n-1 | 0% | EXACT |
| DP-6 | DSC bpp 최소 | 8 | 2·τ | 0% | EXACT |
| DP-7 | DSC bpp 최대 | 12 | σ | 0% | EXACT |
| DP-8 | HBR3 lane | 8.1 | ad-hoc | N/A | EMPIRICAL |
| DP-9 | RBR lane | 2.7 | ad-hoc | N/A | EMPIRICAL |
| DP-10 | Aux channel 수 | 1 | scalar unity | N/A | EMPIRICAL |
| DP-11 | HDCP 2.3 | 2.3 | φ+0.3 | N/A | EMPIRICAL |

- 통계: 7/11 EXACT, 4 EMPIRICAL (HBR/RBR 세대 레거시 + 역사적 부동소수)
- 등급: EXACT-majority

## §4 결론

DisplayPort 는 σ=12 슬롯 11번에 배치되며, 7/11 DP EXACT (63.6%) 로 n=6 정렬이
완결된다. DP 2.0/2.1 세대로 갈수록 정렬이 급격 강화되며, 특히 UHBR20 = 2^τ+τ = 20 Gbps
는 PAM4 채택으로 자연 정착된다. 4 EMPIRICAL 은 1.x 레거시 HBR/RBR 부동소수 대역.

## §5 서명

- 발행자: NEXUS-6 Discovery Engine Validator
- 발행일: 2026-04-14
- 체인: CHIP-P1-2 (displayport.md 실측 7/11) → CHIP-P3-2 (인증서 발행)
- 상태: PASS
