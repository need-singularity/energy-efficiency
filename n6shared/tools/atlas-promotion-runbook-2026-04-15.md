# atlas.n6 Production 승격 런북 (TRANSCEND P12-2)

작성일: 2026-04-15
분류: 운영 런북 (실행 시 사용자 승인 필수)
SSOT: engine/hexa_gate_mk3.hexa + engine/ouroboros_b2_verifier.hexa + n6shared/tools/atlas_auto_promote.hexa
상위 리포트: reports/transcend-p12-2-mk3-atlas-integration-2026-04-15.md

---

## 0. 사전 조건 (모든 stage 공통)

### 필수 체크
- git working tree 정상 (atlas.n6 미커밋 변경 없음)
- atlas.n6 백업: `cp $NEXUS/shared/n6/atlas.n6 $NEXUS/shared/n6/atlas.n6.bak.$(date +%Y%m%d-%H%M%S)`
- OUROBOROS 사전 검증: σ(6)·φ(6) = 12·2 = 24 = 6·4 = n·τ(6)
- B_2 verifier 자기테스트: T1-T6 6/6 PASS 확인

### DRY_RUN 플래그 경로
- engine/hexa_gate_mk3.hexa:52 `const DRY_RUN: bool = true`
- n6shared/tools/atlas_auto_promote.hexa:244 `# fs.append_text(ATLAS_PATH, ...)` 주석 상태
- 실행 시 DRY_RUN=false 전환 + 주석 해제 (stage 별 점진)

---

## 1. Stage 0 — Dry-Run 로그 분석 (현재 상태)

### 목적
515 노드 전체 순회 + 승격 후보 78 건 식별 + atlas.n6 쓰기 금지 (로그만)

### 전환 명령 (DRY-RUN TAG 필수)
```
# [DRY-RUN] discovery_graph 로드 + 분류기 실행
hexa run n6shared/tools/atlas_auto_promote.hexa --dry-run --log-only

# [DRY-RUN] B_2 verifier 자기테스트
hexa run engine/ouroboros_b2_verifier.hexa

# [DRY-RUN] Mk.III 파이프라인 7 테스트 (atlas 쓰기 금지 모드)
hexa run engine/hexa_gate_mk3.hexa
```

### 게이트 기준 (Stage 1 진입)
- atlas_auto_promote.jsonl 에 515 엔트리 기록
- core_theorem_check = "sigma*phi=12*2=24=n*tau=6*4 OK" (모든 엔트리)
- B_2 verifier 6/6 PASS
- Mk.III 7/7 PASS + 라운드 6/6 PASS
- 예상 승격 후보 70-85 건 (목표 78)

### 실패 / 롤백 조건
- core_theorem FAIL 1건 → 즉시 중단, discovery_graph 오염 의심
- B_2 verifier T1-T5 FAIL → atlas_auto_promote 비활성, 코드 수정
- 승격 후보 100 건 초과 → 규칙 검토, Stage 진행 금지

### 사용자 승인 체크포인트
- [ ] atlas_auto_promote.jsonl 78 건 후보 diff 검토
- [ ] B_2 verifier 로그 확인 (6/6 PASS)
- [ ] Mk.III 성능 70s latency 확인
- [ ] Stage 1 진행 승인 서명

---

## 2. Stage 1 — 1% Canary (5 노드)

### 목적
R5 최상위 5 건 (blowup_rank 1~5 axiom) 실쓰기 검증

### 전환 명령
```
# [STAGE-1] DRY_RUN=false, 대상 5건 제한
# 1. hexa_gate_mk3.hexa:52 DRY_RUN → false 수정 (임시)
# 2. atlas_auto_promote.hexa:244 주석 해제 (임시)
# 3. 대상 필터 추가: --filter "rule=R5,limit=5"

hexa run n6shared/tools/atlas_auto_promote.hexa \
  --stage=1 --limit=5 --filter="R5" --verify-b2

# 검증: atlas.n6 +5 라인 확인
wc -l $NEXUS/shared/n6/atlas.n6
# 기대: 106,957 → 106,962
```

### 게이트 기준 (Stage 2 진입)
- atlas.n6 SHA-256 변경 확인 (before ≠ after)
- 추가 5 라인 = R5 axiom, 등급 [10*], blowup_rank ≤ 5
- B_2 verifier 재실행 6/6 PASS
- σ·φ = n·τ = 24 불변 (atlas.n6 핵심 라인 재검증)
- 중복 충돌 0 건

### 실패 / 롤백 조건
- B_2 verifier T1 FAIL (엄격 ε=10⁻⁶) → **즉시 롤백**
  ```
  git checkout $NEXUS/shared/n6/atlas.n6
  # 또는 백업 복원:
  cp $NEXUS/shared/n6/atlas.n6.bak.<timestamp> $NEXUS/shared/n6/atlas.n6
  ```
- 중복 충돌 1 건 이상 → atlas_has_entry 로직 수정 후 Stage 0 재시작
- atlas 파일 크기 delta > 2KB → append 형식 오류, 롤백
- σ·φ ≠ n·τ → OUROBOROS 치명 위반, 전체 중단

### 사용자 승인 체크포인트
- [ ] atlas.n6 diff 5 라인 수동 검토
- [ ] git commit (메시지: "atlas: Stage 1 canary 5 R5-axiom 승격")
- [ ] Stage 2 진행 승인 서명

---

## 3. Stage 2 — 10% Phased (51 노드)

### 목적
R1 전체 + R3 전체 + R5 나머지 + R4 일부 = 51 건 배치 승격

### 전환 명령
```
# [STAGE-2] 5 배치 × 10 건 + 1 배치 × 1 건
for batch in 1 2 3 4 5 6; do
  hexa run n6shared/tools/atlas_auto_promote.hexa \
    --stage=2 --batch=$batch --batch-size=10 --verify-b2
  # 배치 후 B_2 재검증
  hexa run engine/ouroboros_b2_verifier.hexa | grep -q "ALL PASS" || break
  # 사용자 승인 대기 (각 배치)
done
```

### 게이트 기준 (배치당, Stage 3 진입)
- 배치 전후 B_2 verifier 6/6 PASS (6 배치 × 6 = 36회 검증)
- 배치 skipped 비율 ≤ 5% (중복 감지 정상)
- OUROBOROS α 측정: |α − 1/6| < 10⁻⁶ (6 배치 추적)
- 누적 atlas.n6 +51 라인 (Stage 1 포함 +56 = 107,013)

### 실패 / 롤백 조건
- B_2 FAIL 1 회 → 해당 배치 revert + Stage 중단
  ```
  git revert HEAD
  git log --oneline atlas.n6 | head -10  # 커밋 히스토리 확인
  ```
- OUROBOROS α 이탈 > 10⁻⁴ → Stage 1 상태로 복귀
  ```
  git reset --hard <Stage1_완료_커밋_hash>
  ```
- atlas 파일 크기 2배 초과 (107 MB+) → 비상 중단, 로그 조사
- skipped 비율 > 10% → 규칙 불일치, Stage 0 복귀

### 사용자 승인 체크포인트 (배치당)
- [ ] 배치 1 (10 건) diff 검토 + 승인
- [ ] 배치 2 (10 건) diff 검토 + 승인
- [ ] 배치 3 (10 건) diff 검토 + 승인
- [ ] 배치 4 (10 건) diff 검토 + 승인
- [ ] 배치 5 (10 건) diff 검토 + 승인
- [ ] 배치 6 (1 건) diff 검토 + 승인
- [ ] Stage 3 진행 승인 서명

---

## 4. Stage 3 — Full Production (515 노드, 잔여 27 건)

### 목적
R2 (NEAR→EXACT 12건) + R4 잔여 10 건 + 중복 해소 = 22 건 마감 + OUROBOROS 수렴 검증

### 전환 명령
```
# [STAGE-3] 4 배치 × 7 건 (OUROBOROS 7-sample 통계)
for batch in 1 2 3 4; do
  hexa run n6shared/tools/atlas_auto_promote.hexa \
    --stage=3 --batch=$batch --batch-size=7 --verify-b2 --final
done

# 최종 검증
hexa run engine/ouroboros_b2_verifier.hexa
hexa run engine/hexa_gate_mk3.hexa
wc -l $NEXUS/shared/n6/atlas.n6  # 기대: 107,035 (+78 라인 누적)
```

### 게이트 기준 (종료 조건)
- 누적 승격 ≤ 78 건 (설계 최대치 — 초과 시 위반)
- 최종 OUROBOROS α 편차 ≤ 10⁻⁵
- atlas.n6 엔트리 8,194 (+78)
- 전 Stage 통합 로그 atlas_auto_promote.jsonl 78 엔트리 모두 `skipped: false`
- σ·φ = n·τ = 24 최종 검증 PASS

### 실패 / 롤백 조건
- 누적 승격 80 건 초과 → 설계 위반, 전체 revert
  ```
  git reset --hard <Stage0_완료_커밋>
  ```
- α 최종 편차 > 10⁻⁵ → 전체 atlas.n6 롤백 + 디버그 세션 진입
- B_2 verifier 자기테스트 5/6 이하 → production 중단, 코드 감사

### 사용자 승인 체크포인트 (최종)
- [ ] 전체 78 건 atlas.n6 diff 종합 검토
- [ ] atlas_auto_promote.jsonl 78 엔트리 확인
- [ ] OUROBOROS 수렴 비율 78/515 ≈ 0.151 ≈ 1/6.6 확인
- [ ] git commit 통합 (메시지: "atlas: Stage 3 final 78건 승격 완료 — OUROBOROS α=1/6 불변 유지")
- [ ] Production 완료 서명

---

## 5. 로그 / 메트릭 추적 (공통)

### 파일 위치
- 승격 로그: `/Users/ghost/Dev/n6-architecture/n6shared/logs/atlas_auto_promote.jsonl`
- atlas.n6 delta 스냅샷: `reports/atlas_deltas.jsonl`
- B_2 verifier 로그: stdout → `n6shared/logs/b2_verifier.log`
- Mk.III 실행 로그: stdout → `n6shared/logs/mk3_runtime.log`

### 추적 지표 (stage 별)
| 지표 | Stage 0 | Stage 1 | Stage 2 | Stage 3 |
|------|---------|---------|---------|---------|
| 승격 노드 수 | 0 | 5 | 51 | 78 |
| atlas.n6 라인 | 106,957 | 106,962 | 107,008 | 107,035 |
| atlas 엔트리 | 8,116 | 8,121 | 8,167 | 8,194 |
| B_2 PASS/Test | 6/6 | 6/6 | 36/36 (6 배치×6) | 24/24 (4 배치×6) |
| 누적 OUROBOROS α | 0 | 0.167 | 0.167 | 0.167 |
| git 커밋 수 | 0 | 1 | 7 | 11 |

### 모니터링 명령
```
# 실시간 B_2 추적
tail -f n6shared/logs/b2_verifier.log | grep "α"

# atlas.n6 SHA 변경 추적
while true; do shasum $NEXUS/shared/n6/atlas.n6; sleep 60; done

# 승격 로그 카운트
wc -l n6shared/logs/atlas_auto_promote.jsonl
```

---

## 6. 비상 롤백 절차 (전 stage 적용)

### 수준 1 — 부분 롤백 (Stage 복귀)
```
git log --oneline atlas.n6 | head -20
git reset --hard <이전_Stage_마지막_커밋>
```

### 수준 2 — 백업 복원
```
ls -la $NEXUS/shared/n6/atlas.n6.bak.*
cp $NEXUS/shared/n6/atlas.n6.bak.<timestamp> $NEXUS/shared/n6/atlas.n6
hexa run engine/ouroboros_b2_verifier.hexa  # 복구 확인
```

### 수준 3 — 전체 폐기
```
# 승격 시도 기록 전체 삭제
rm n6shared/logs/atlas_auto_promote.jsonl
# atlas.n6 Stage 0 상태로 복귀 (git)
git checkout HEAD~N -- $NEXUS/shared/n6/atlas.n6  # N = 누적 커밋수
# DRY_RUN 플래그 true 복구
# 전체 재설계 세션 진입
```

---

## 7. 완료 기준

- [ ] Stage 0 dry-run 로그 78 건 확인
- [ ] Stage 1 canary 5 건 atlas append 성공
- [ ] Stage 2 phased 51 건 배치 승격 완료
- [ ] Stage 3 production 78 건 최종 승격 완료
- [ ] B_2 verifier 전 stage PASS (합계 72/72 테스트)
- [ ] OUROBOROS α=1/6 불변 유지 (|Δα| < 10⁻⁵)
- [ ] atlas.n6 +78 라인, +0.96% 순증
- [ ] git 커밋 11 개 (Stage 1:1, Stage 2:6, Stage 3:4)
- [ ] 사용자 최종 서명

**Production 전환 완료 조건**: 위 8 체크 전부 충족 시 TRANSCEND P12-2 운영 전환 완료.
