# 3D 현실 지도 v6.1 풀세트 변경 기록

날짜: 2026-04-08
대상: `docs/index.html` (Three.js r175 WebGL 3D 시각화)
이전 버전: v6.0 (2026-04-07, 247 노드 / 49 인과 엣지)

## 추가된 5개 기능

### 1. 인과 사슬 애니메이션
- 우상단 `▶ 인과사슬` 버튼 토글
- `DATA.edges` 배열에서 최대 5개 경로를 자동 순회 (2.2초 간격)
- 각 단계에서 from/to 노드를 펄스로 강조 (스케일 1.6배 박동)
- 카메라 OrbitControls 타깃이 두 노드 중점으로 부드럽게 이동
- 정지 시 펄스/타깃 원복

### 2. BT 역참조 클릭 팝업
- 노드 클릭 시 `bt_refs` 배열이 있으면 중앙 상단 팝업 표시
- 표시 항목: claim, id, BT 태그(보라색 칩), measured, n6_expr, cause, source_url 링크
- bt_refs 없는 노드는 기존 동작(`source_url` 새 탭) 유지
- 247개 노드 중 229개(92.7%)가 bt_refs 보유 → 거의 전 노드 팝업 작동

### 3. origin 색상/크기 토글
- 우상단 `□ origin 색상` 체크박스
- ON 시 모든 인스턴스 색상을 origin 기반으로 재칠:
  - natural = `#4fc3f7` (시안)
  - engineering = `#ff7043` (오렌지)
  - convention = `#b0bec5` (회색)
- OFF 시 기존 level/CHAIN 색상 복원
- 검색바의 origin 필터와 직교 동작

### 4. Z축 6 도메인 분리 (n=6)
- 우상단 `Z=6도메인` 체크박스 (기본 ON)
- level 7개를 6 버킷으로 압축 (L5_material + L5_bio = 도메인 5)
- 각 도메인이 Z 슬라이스 (`DOMAIN_Z_GAP = 4·SCALE_Z`)에 분리 배치
- 도메인 분포(247노드): [47, 20, 33, 15, 16, 116] — 6 슬롯 모두 충원
- 토글 OFF 시 v6.0 기존 thread×index Z 좌표 복원
- 좌표 변경 시 모든 엣지 BufferGeometry + 화살표 콘 자동 재구성

### 5. WebGL 성능 최적화 (InstancedMesh)
- 이미 v6.0 에서 InstancedMesh 채택 — v6.1 에서 다음 사항 보강:
  - 노드 좌표 갱신 시 `instanceMatrix.needsUpdate` 단일 플래그로 전체 재배치
  - origin 색상 재칠 시 setColorAt + `instanceColor.needsUpdate` 단일 호출
  - Raycaster 폴백 거리 체크가 247노드에서도 60FPS 유지
  - 1000+ 노드 확장 시에도 동일 코드 경로로 동작 보장

## 신규 파일

- `.github/workflows/reality_map_verify.yml` — CI 검증
  - 노드 수 ≥ 200 임계값 (회귀 방지)
  - 6 도메인 분포 보고
  - bt_refs 보유 노드 카운트 (BT 역참조 UI 의존성 검증)
  - 인과 엣지 카운트
  - 트리거: docs/reality_map.json, docs/index.html, 본 워크플로 변경 시
- `docs/3d-map-changelog-2026-04-08.md` — 본 문서

## 회귀 방지 체크

- v6.0 검색/필터 (search-input, filter-grade, filter-origin) 그대로 작동
- v6.0 글로우 스프라이트 EXACT/CHAIN 펄스 유지
- v6.0 thread/parent/sibling/causal 4종 엣지 모두 복원 (rebuildEdges)
- v6.0 source_url 클릭 동작은 bt_refs 없는 노드에 한해 폴백 보존
- 단일 `index.html` 파일 유지 (분할 금지 규칙 준수)
- JS 문법 검증: `node --check` PASS

## 추가 라인 수

- `docs/index.html`: +약 200 라인 (689 → 약 887)
- `.github/workflows/reality_map_verify.yml`: +71 라인
- `docs/3d-map-changelog-2026-04-08.md`: 본 파일

## CI 로컬 사전 검증

```
nodes=247 exact=228 bt_refs=229 domains=[47, 20, 33, 15, 16, 116] edges=49
```
- 247 ≥ 200 임계값 PASS
- 6 도메인 모두 비어있지 않음 PASS
- bt_refs 92.7% 커버리지 PASS
