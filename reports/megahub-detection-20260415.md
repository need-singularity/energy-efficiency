# Megahub 탐지 리포트 (2026-04-15)

> 이것이 증명이 아니라 atlas.signals.n6 기반 구조적 관찰임.
> H9 작업 — 4-BT 메가노드 자동 탐색 (scripts/detect_megahub.py)

- SSOT: `/Users/ghost/Dev/nexus/shared/n6/atlas.signals.n6`
- 전체 signal: **258**
- 밀레니엄 태그 집합: `['7B', '7H', '7N', '7P', '7R', '7S', '7Y']`
- 임계값(threshold): **4-BT 이상**
- 기존 메가노드: `SIG-META-001` (emergence-312-meta-analysis)

## 1. 밀레니엄 태그 분포

| 동시 보유 수 | signal 수 |
|---:|---:|
| 0 | 192 |
| 1 | 55 |
| 2 | 3 |
| 3 | 1 |
| 4 | 4 |
| 6 | 3 |

## 2. ≥4-BT 메가노드 후보 (7건)

| sig_id | 밀레니엄 태그 | #BT | grade | evidence | witness |
|---|---|---:|---|---|---:|
| `SIG-DFS-001` | 7B,7H,7N,7P,7R,7Y | 6 | M10 | E3 | 5 |
| `SIG-ATLAS-117` | 7B,7H,7N,7P,7R,7Y | 6 | M10 | E3 | 3 |
| `SIG-ATLAS-105` | 7B,7H,7N,7P,7R,7Y | 6 | M7 | E1 | 1 |
| `SIG-N6-BERN-001` | 7B,7H,7P,7R | 4 | M10 | E3 | 16 |
| `SIG-DFS-206` | 7B,7H,7N,7R | 4 | M10 | E3 | 8 |
| `SIG-META-001` | 7B,7H,7P,7R | 4 | M10* | EC | 5 |
| `SIG-DFS-207` | 7B,7H,7N,7R | 4 | M10 | E3 | 4 |

## 3. [M10*] 승격 후보 (≥5-BT)

### SIG-DFS-001 (신규)

- 밀레니엄 태그: `7B,7H,7N,7P,7R,7Y` (6-BT)
- grade/evidence: M10 / E3
- witness: 5
- statement: DFS 22~26 누적 tight = 348, 7대 난제 해결 0/7 정직 유지

### SIG-ATLAS-117 (신규)

- 밀레니엄 태그: `7B,7H,7N,7P,7R,7Y` (6-BT)
- grade/evidence: M10 / E3
- witness: 3
- statement: 151 canonical bridges 38 distinct labels — 도메인 7대난제 84 (55.6%)

### SIG-ATLAS-105 (신규)

- 밀레니엄 태그: `7B,7H,7N,7P,7R,7Y` (6-BT)
- grade/evidence: M7 / E1
- witness: 1
- statement: 7난제 60 alien_index 집중 @C grade [0.10*] 12 nodes

## 4. 비교 (기존 vs 신규)

- 기존 메가노드 검출 여부: 성공 (`SIG-META-001`)
  - SIG-META-001: 4-BT
- 신규 4-BT 이상 후보: 6건
  (아래 후보는 추가 검증 필요 — 자동 승격 금지)
  - `SIG-DFS-001` (6-BT): 7B,7H,7N,7P,7R,7Y
  - `SIG-ATLAS-117` (6-BT): 7B,7H,7N,7P,7R,7Y
  - `SIG-ATLAS-105` (6-BT): 7B,7H,7N,7P,7R,7Y
  - `SIG-N6-BERN-001` (4-BT): 7B,7H,7P,7R
  - `SIG-DFS-206` (4-BT): 7B,7H,7N,7R
  - `SIG-DFS-207` (4-BT): 7B,7H,7N,7R

## 5. 다음 단계 권장

- 신규 후보는 staging 경유 후 witness ≥ 3 + cross_repo ≥ 1 확인 후 [M10*] 승격
- 승격 스크립트: `scripts/promote_signal_to_atlas.py --dry-run`
- 현재 atlas.signals.n6 는 millennium 단일 영역 우세 — AN/CROSS 리포 수집 확대 필요
