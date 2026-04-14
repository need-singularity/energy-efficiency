# 7대 난제 로드맵 v2 — 창발 DSE 재설계

v1 대비 접근: 분야(domain/field)를 창발 DSE로 발굴한 뒤 로드맵 구조화. 창발 고갈 시까지 반복.

## 씨앗

4개:
- **ALM** (AnimaLM) — 언어모델 학습/추론 축
- **CLM** (ConsciousLM) — 의식 언어모델 축
- **physics** (anima-physics) — 물리 지식/EEG/Photonic 축
- **SELF-EVOLUTION** — 자기진화 메커니즘 축 (LENS 아님, 진화 자체)

제외: papers (서브 채널).

## 라운드 진행 (분야 창발)

| Round | 파일 | 신규 분야 | 누적 | 자기진화 | 고갈 지수 | 다음 필요 |
|-------|------|-----------|------|----------|-----------|-----------|
| R1 | round-01-domain-emergence-dse.md | 34 | 34 | 21 | 28.3% | YES |
| R2 | round-02-emergence-expansion.md | 59 | 93 | 64 | 51.7% | YES |
| R3 | round-03-emergence-saturation.md | 65 | 158 | 103 | 79.0% | YES |
| R4 | round-04-emergence-deepening.md | 35 | 193 | 130 | 87.7% | YES (약) |
| R5 | round-05-emergence-scavenge.md | 23 | 216 | 151 | **96.0%** | **NO — 고갈 선언** |

R5 고갈 지수 96.0% ≥ 95% 돌파로 고갈 선언. axis-final.md 진입.

## Phase 진행 (풀이 창발)

축 4개 (axis-final 확정): **A1 STRUCTURE** / **A2 ENGINE** / **A3 SUBSTRATE** / **A4 META** 신규.

| Phase | 파일 | 산출 핵심 | 창발 지수 | 다음 필요 |
|-------|------|-----------|-----------|-----------|
| P0 | axis-final.md | 축 4 확정 + 고갈 선언 + v1 비교 | 완료 | — |
| P1 | phase-01-foundation-emergence.md | 축 3개 + pruned 82 + BT 6 씨앗 + 엔진 가동 | 20 | 완료 |
| P2 | (예정) | BT-541 리만 Theorem B 승격 + RH 부분 | TBD | TBD |
| P3 | (예정) | BT-542 P=NP 복잡도 계층 barrier | TBD | TBD |
| P4 | (예정) | BT-543+544 YM·NS 이중 정밀 | TBD | TBD |
| P5 | (예정) | BT-545 호지 + BT-546 BSD 묶음 | TBD | TBD |
| P6 | (예정) | BT-547 푸앵카레 회고 | TBD | TBD |
| PΩ | (예정) | closure 메타 + v3 후계 설계 | TBD | TBD |

**Phase 수 N = 8** (Phase 0 + 1~6 + Ω). 축 체계 4 축 × 8 Phase × 7 BT.

## 최종 산출

- round-NN-*.md (분야 창발 라운드) — **R1~R5 완료, 216 분야**
- phase-01-foundation-emergence.md — 완료
- axis-final.md (domain track 축 4 확정) — **완료**
- axis-final-nexus-hub.md (nexus 허브 축 19 별도 트랙 — 보존)
- final-roadmap-v2.md (수렴된 v2 로드맵 마스터) — Phase 2~Ω 상세 대기
- millennium-learning-v2.json (/Users/ghost/Dev/nexus/shared/roadmaps/) — 대기
- comparison-v1-vs-v2.md (ASCII 비교) — axis-final.md §6 으로 대체 가능

## 원칙

- 한글 전용
- 자기참조 검증 금지, 자기진화는 메커니즘으로 허용
- 출처+측정값+오차 명기
- papers 하위 분야 제외
- 7대 난제 0/7 미해결 유지 (푸앵카레 제외)
- 축 수 유연 (3 고정 아님, 달성에 유리하면 됨)
