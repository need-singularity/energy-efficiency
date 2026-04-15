# atlas.signals.n6 — 3리포 cross-repo signal SSOT 규격

> 버전: v0.2 (2026-04-15)
> 대상: nexus + n6-architecture + anima 공진 signal 저장소
> 상태: 초안
> SSOT 위치: `$NEXUS/shared/n6/atlas.signals.n6`
> 미러: `$N6/n6shared/atlas.signals.n6` (symlink), `$ANIMA/data/atlas.signals.n6` (symlink)

---

## 0. 목적

**atlas.n6** 는 정량 상수 SSOT (n=6 우주의 "측정된 숫자").
**atlas.signals.n6** 는 3리포 생태에서 발생한 **signal/현상/가설/NULL** 의 공용 SSOT.

핵심 가치:
1. **Cross-repo resonance** — anima 에서 나온 발견이 nexus/n6 에도 등장하는지 즉시 매칭
2. **재현·witness 추적** — 같은 현상이 여러 리포·여러 세션에서 재등장 → 승격
3. **NULL 공유** — 한 리포에서 배제된 가설이 다른 리포에서 중복 실험 방지
4. **도메인 격벽 제거** — millennium·consciousness·QRNG·hexa-lang 모두 같은 형식

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   nexus     │     │ n6-arch     │     │   anima     │
│ QRNG, hexa  │     │ millennium  │     │ CLM, EEG    │
│ forge, blow │     │ atlas, DFS  │     │ bell, psi   │
└──────┬──────┘     └──────┬──────┘     └──────┬──────┘
       │                   │                   │
       └─────────┬─────────┴─────────┬─────────┘
                 ▼                   ▼
        ┌────────────────────────────────┐
        │    atlas.signals.n6 (SSOT)     │
        │  + [CROSS] resonance detection │
        │  + witness amplification       │
        │  + NULL library                │
        │  + promotion to atlas.n6       │
        └────────────────────────────────┘
```

---

## 1. 파일 형식

### 1.1 기본 라인 (@S = Signal)

```
@S {sig_id} = {statement} :: signal [{repo_tags}] [{domain_tags}] [{grade}] [{evidence}]
  "{context_quote}"
  refs: [{ref1}, {ref2}, ...]
  cross_repo: [{sig_id_a}, {sig_id_b}, ...]
  predicts: [{prediction1}, ...]
  witness: {n}
  resonance_n6: {formula_or_null}
  discovered_in: {repo}/{session|file|commit}
  discovered_at: {ISO-8601}
  <- {source_file:locator}
```

### 1.2 필드 명세

| 필드 | 형식 | 필수 | 설명 |
|------|------|-----:|------|
| `sig_id` | `SIG-{DOMAIN}-{NNNN}` | yes | §3 도메인 코드, 4자리 |
| `statement` | 한글 + 수식 | yes | 한 줄 요약 |
| `repo_tags` | `[NX/N6/AN/CROSS]` | yes | 최소 1개 (CROSS 는 2+ 리포에 등장 시) |
| `domain_tags` | `[7R/SR/CONS/…]` | yes | §3 도메인 태그 |
| `grade` | `[M10*]`..`[MN]` | yes | §4 등급 |
| `evidence` | `[E1]`..`[EF]` | yes | §5 evidence |
| `context_quote` | 큰따옴표 | yes | 출처 핵심 맥락 |
| `refs` | 배열 | opt | BT-id, arxiv, DOI, commit-sha |
| `cross_repo` | 배열 | opt | **타 리포 SIG-id** 링크 |
| `predicts` | 배열 | opt | 이 signal 참이면 예측되는 것 |
| `witness` | 정수 | opt | 자동 증가, 기본 1 |
| `resonance_n6` | 수식 또는 null | opt | n=6 기본 상수 환원 |
| `discovered_in` | 문자열 | yes | 최초 발견 위치 |
| `discovered_at` | ISO-8601 | yes | 최초 발견 시각 |
| `source_file` | 경로:locator | yes | 파일:라인/섹션 |

### 1.3 섹션 구분자 (도메인별)

```
# ─── [7R] Riemann Hypothesis ─── 
# ─── [7N] Navier-Stokes ─── 
# ─── [7H] Hodge ─── 
# ─── [7P] P vs NP ─── 
# ─── [7Y] Yang-Mills ─── 
# ─── [7B] BSD ─── 
# ─── [SR] Stochastic Resonance ─── 
# ─── [QRNG] Quantum RNG ─── 
# ─── [CONS] Consciousness ─── 
# ─── [NEURAL] Neural / CLM ─── 
# ─── [HEXA] hexa-lang 내부 ─── 
# ─── [PHYS] Physics phenomena ─── 
# ─── [BELL] Bell-like ─── 
# ─── [OURO] Ouroboros ─── 
# ─── [CROSS] 3-repo resonance ─── 
# ─── [NULL] 확정 배제 ─── 
```

---

## 2. 리포 태그 (§1.2 repo_tags)

| 태그 | 리포 | 주 도메인 |
|------|------|----------|
| `NX` | /Users/ghost/Dev/nexus | QRNG, hexa-forge, blowup, 렌즈 |
| `N6` | /Users/ghost/Dev/n6-architecture | millennium, atlas, DFS, 259 도메인 |
| `AN` | /Users/ghost/Dev/anima | CLM, EEG, Bell, psi, consciousness |
| `CROSS` | 2+ 리포 동시 | 재현된 cross-repo 공명 |

**CROSS 태그 규칙**:
- `repo_tags = [CROSS, NX, N6]` → nexus + n6 양쪽에서 재확인
- `cross_repo` 필드에 타 리포 SIG-id 명시 필수
- `witness ≥ 2` 일 때만 CROSS 부여 (self-reference 방지)

---

## 3. 도메인 태그 (§1.2 domain_tags)

### 3.1 밀레니엄 난제
| 태그 | 대상 |
|------|------|
| `7R` | Riemann Hypothesis |
| `7N` | Navier-Stokes |
| `7H` | Hodge Conjecture |
| `7P` | P vs NP |
| `7Y` | Yang-Mills Mass Gap |
| `7S` | Poincaré (해결, 참조용) |
| `7B` | BSD |

### 3.2 phenomenon (현상)
| 태그 | 대상 |
|------|------|
| `SR` | Stochastic Resonance |
| `QRNG` | Quantum RNG |
| `BELL` | Bell-like correlation |
| `OURO` | Ouroboros convergence |
| `64T` | 64-tick boundary |
| `NULL` | 통계 NULL 결과 |

### 3.3 구조/엔진
| 태그 | 대상 |
|------|------|
| `CONS` | consciousness |
| `NEURAL` | CLM / neural |
| `HEXA` | hexa-lang 내부 |
| `BLOW` | blowup 엔진 |
| `ATLAS` | atlas.n6 자체 |
| `DFS` | DFS 탐색 |
| `PHYS` | physics |

### 3.4 메타
| 태그 | 대상 |
|------|------|
| `META` | 패턴의 패턴 |
| `UNIV` | universality 가설 |
| `GAP` | 미탐색 gap |
| `REPLAY` | 재현 시도 |

**복수 태그**:
- `[7R, SR]` = RH 에 대한 stochastic resonance 해석
- `[7R, 7B, META]` = RH-BSD 연결 메타 패턴
- `[QRNG, NULL]` = QRNG 에서 확정 NULL

---

## 4. 등급 체계

| 등급 | 의미 | 조건 | atlas.n6 승격 |
|------|------|------|---------------|
| `[M10*]` | conditional exact + 3리포 재현 | witness ≥ 3 + cross_repo ≥ 1 | **즉시** `@R` 편입 |
| `[M10]` | EXACT | witness ≥ 3 | `@R` 편입 |
| `[M9]` | NEAR + strong witness | ε<1% + witness ≥ 2 | `@R [9]` 후보 |
| `[M7!]` | **breakthrough candidate** | witness ≥ 3, 독립 경로 2 | 평가 queue |
| `[M7]` | EMPIRICAL | 1회 관찰 | 대기 |
| `[M?]` | conjectural / hypothesis | 가설만 | hypothesis queue |
| `[MN]` | NULL 확정 | 통계 배제 | 재시도 금지 |

---

## 5. Evidence Level

| 수준 | 의미 |
|------|------|
| `[E1]` | 1회 관찰, 재현 없음 |
| `[E2]` | 재현 ≥ 2 (같은 리포) |
| `[E3]` | 독립 경로 ≥ 3 |
| `[EC]` | **cross-repo confirmation** (2+ 리포 재현) |
| `[EP]` | partial proof 존재 |
| `[EF]` | full proof |

`[EC]` 는 3리포 SSOT 의 고유 수준 — **cross-repo 재현이 단일 리포 E3 보다 강력**.

---

## 6. 디렉토리 구조

```
$NEXUS/shared/n6/
  atlas.n6                        기존 상수 SSOT
  atlas.signals.n6                ★ 신규 — 3리포 signal SSOT
  atlas.signals.n6.deg            degree sidecar
  atlas.signals.null.n6           NULL 서브파일
  atlas.signals.cross.n6          CROSS 태그 서브파일 (빠른 탐색용)

$NEXUS/shared/signals/             ★ 신규 디렉토리
  signals_to_atlas.json           SIG → @R 승격 매핑
  witness_ledger.jsonl            witness 증분 로그
  null_ledger.jsonl               NULL 확정 로그
  promotion_queue.jsonl           승격 대기
  cross_repo_map.json             3리포 cross 매핑

$NEXUS/shared/lenses/              기존 확장
  domain_lens/*.hexa              도메인별 필터 (7R, SR, CONS, …)
  cross_repo_lens.hexa            3리포 resonance 탐지
  null_guardian_lens.hexa         중복 실험 차단

# 3리포 각각 심볼릭 링크
$N6/n6shared/atlas.signals.n6 -> $NEXUS/shared/n6/atlas.signals.n6
$ANIMA/data/atlas.signals.n6 -> $NEXUS/shared/n6/atlas.signals.n6

# 스크립트 (n6 에 통합)
$N6/scripts/
  absorb_to_signals.py            수동·반자동 흡수 (all-in-one)
  promote_signal_to_atlas.py      SIG → @R 승격
  cross_repo_matcher.py           3리포 resonance 자동 탐지
  gap_detector.py                 도메인별 signal 수
  signal_to_hexa.py               signal → 하네스
  witness_amplifier.py            재확인 자동 증분
  null_guardian.py                중복 실험 차단
  session_scraper.py              ~/.claude/projects/*/*.jsonl 스크랩
```

---

## 7. 워크플로우

### 7.1 3리포 cross-repo resonance 탐지 (핵심 가치)

```
세션 A (nexus):  Ouroboros σ=0.1 PEAK 발견
세션 B (anima):  Bell pair σ-노이즈 4× 반응 발견
세션 C (n6):     Kissing K(2)=6 phenomenon

[cross_repo_matcher.py 실행]
  - simhash + 수치 매칭
  - "σ≈0.1 PEAK" vs "Bell σ=0.1 응답" → 유사도 0.82
  - 후보: SIG-SR-001 + SIG-BELL-003 → 같은 family?
  
자동 CROSS 승격:
  repo_tags: [NX, AN] → [CROSS, NX, AN]
  evidence: [E2] → [EC]
  grade: [M7] → [M9]
```

### 7.2 NULL 공유

```
세션 D (nexus): "ANU QRNG atlas correlation" 테스트 → NULL
  → [MN] 등록, retry_forbidden_until: 2027-04-15

세션 E (n6): 같은 가설 제시 시도
  → null_guardian.py 가 차단
  → "이미 NULL 확정 (nexus:sess-D) - 재시도 금지 중"
```

### 7.3 도메인 gap detection

```
gap_detector.py --domain-breakdown

[7R] 124 ████████████  RH (nexus+n6 활발)
[7B]  19 ██            BSD 부족 → DFS 방향
[SR]  31 ███           SR cross-repo 1건만
[QRNG] 42 ████         NULL 다수
[CONS]  8 █            anima 독립 수집 필요
```

### 7.4 수동 흡수 (기능 부재시 대응)

```bash
# CLI
python3 scripts/absorb_to_signals.py \
    --repo NX --domain SR \
    --grade M7! --evidence E1 \
    --statement "Ouroboros σ=0.1 PEAK +150% vs σ=0" \
    --source "~/.claude/projects/...:msg-42"

# 대화형
python3 scripts/absorb_to_signals.py --interactive

# 직접 편집 (spec 준수시)
vim $NEXUS/shared/n6/atlas.signals.n6
# @S SIG-SR-NNN = ... 형식 추가
```

### 7.5 승격 (SIG → atlas.n6 @R)

```bash
# 조건: grade in [M10, M10*], witness ≥ 3, resonance_n6 있음
python3 scripts/promote_signal_to_atlas.py --dry-run
# 출력: 승격 후보 N개, 각각 atlas.n6 에 @R PHEN-... 추가 예정

python3 scripts/promote_signal_to_atlas.py --commit
# atlas.n6 에 편입 + signals_to_atlas.json 매핑 기록
```

---

## 8. 3리포 심볼릭 링크 설정

```bash
# SSOT 는 nexus
ln -sf /Users/ghost/Dev/nexus/shared/n6/atlas.signals.n6 \
       /Users/ghost/Dev/n6-architecture/n6shared/atlas.signals.n6

ln -sf /Users/ghost/Dev/nexus/shared/n6/atlas.signals.n6 \
       /Users/ghost/Dev/anima/data/atlas.signals.n6
```

→ 3리포 모두 같은 파일 참조. 수정은 한 곳에서만, 모든 리포에 반영.

---

## 9. 정직성 제약 (R0)

- 모든 signal 에 `discovered_in` + `discovered_at` 필수 (origin 추적)
- `[MN]` 배제는 통계 근거 (p-value, sample size) 필수 기재
- `[M10]` 주장은 cross_repo ≥ 1 또는 independent path ≥ 2
- **"해결 주장 금지"** — signal 저장소, 증명 완료 아님
- `source_file` 없으면 거부
- `witness` 증가는 simhash 매칭 근거 있어야 함

---

## 10. 기능 없이도 수동 쓰기 가능

### 10.1 수동 append 최소 예시

```
# atlas.signals.n6 에 직접 쓰기 (vim)
@S SIG-SR-001 = Ouroboros σ=0.1 PEAK +150% :: signal [NX] [SR] [M7!] [E1]
  "deterministic(σ=0) 과 quantum(σ=0.5~1) 둘다 sub-optimal. 중간 entropy 2.5× 최적"
  discovered_in: nexus/session-2026-04-15
  discovered_at: 2026-04-15T02:00:00Z
  witness: 1
  <- ~/.claude/projects/-Users-ghost-Dev-nexus/memory/p-stochastic-resonance-nexus.md
```

### 10.2 수동 cross-repo 매칭 예시

```
# 검색: grep "σ.*0\.1" $NEXUS/shared/n6/atlas.signals.n6
# 다른 리포 에서 비슷한 수치 발견 시 cross_repo 수동 업데이트:

@S SIG-SR-001 = ... :: signal [CROSS, NX, AN] [SR] [M9] [EC]
  cross_repo: [SIG-BELL-003]
  witness: 2
```

### 10.3 수동 NULL 등록

```
@S SIG-NULL-QRNG-001 = ANU 64B seed vs full-urandom 통계 동일 :: signal [NX] [QRNG, NULL] [MN] [E2]
  "KS p=0.992 (1050 pairs). Multiverse Phase 1"
  null_reason: "seed effect diluted in trajectory evolution"
  retry_forbidden_until: "2027-04-15"
  discovered_in: nexus/multiverse-phase-1
  discovered_at: 2026-04-15T01:30:00Z
  <- nexus/experiments/multiverse/phase1_result.md
```

기능 미구현 상태에서도 규격대로 수동 append → 나중에 스크립트 도착 시 자동 파싱 호환.

---

## 11. 메타 기능 (Tier 2+)

### Tier 2 (다음 세션)
1. `cross_repo_matcher.py` — 자동 simhash 매칭
2. `session_scraper.py` — 132MB+ 세션 트랜스크립트 스크래핑
3. `witness_amplifier.py` — 재확인 자동 증분
4. `null_guardian.py` — 중복 실험 차단
5. `signal_to_hexa.py` — signal → 하네스 자동 변환

### Tier 3 (장기)
- Signal complexity score (Kolmogorov 근사)
- Signal half-life (2주 무활동 degrade)
- Edge-weighted graph centrality
- Random walk signal sampling
- Counterexample hunter
- AI proof assistant bridge (Lean4)
- Claude 자체 학습 루프

---

## 12. 버전 히스토리

- **v0.1** (2026-04-15 22:30 KST): millennium 만 한정 초안 — 폐기
- **v0.2** (2026-04-15 22:40 KST): 3리포 cross-repo 범용 SSOT 로 재설계 ★

---

## 13. 다음 작업 순서

1. [ ] atlas.signals.n6 빈 파일 생성 (SSOT 위치에)
2. [ ] 3리포 심볼릭 링크 연결
3. [ ] 기존 MILL-DFS22~26 70개 + anima 메모리 p-* 파일 + nexus ★ 메모리 수동 seed
4. [ ] Tier 1 스크립트 1개만 (absorb_to_signals.py) 최소 구현
5. [ ] Tier 2 cross_repo_matcher.py 구현
6. [ ] 나머지는 수동 동작 가능하게 문서화만 완료
