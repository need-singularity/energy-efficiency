# n6-architecture 제출 포맷 템플릿 — 상위 48편 공통

| 필드 | 값 |
|---|---|
| 로드맵 | PAPER-P3-1 |
| 생성일 | 2026-04-14 |
| 대상 | `_submission_top48.json` 등재 48편 |
| 상태 | template_ready (포맷 스켈레톤만. 본문 재생성 금지) |
| DOI 정책 | 시뮬 DOI `10.NEXUS6.n6-arch/2026-NNN` — 실제 DOI 아님 |

본 파일은 상위 48편을 저널/컨퍼런스 제출 포맷으로 정리하기 위한 표준 템플릿이다. 실제 논문 본문은 기존 `papers/n6-*-paper.md` 그대로 두고, 제출 시에는 이 템플릿의 헤더/초록/참고문헌 블록만 덧씌운다. WHY / COMPARE / MAIN / VERIFICATION 4단 구조는 n6-architecture 모든 논문의 공통 골격이다.

---

## 0. 헤더 블록 (필수)

```
---
doi_sim:         10.NEXUS6.n6-arch/2026-NNN
paper_id:        N6-XXX
rank:            <1..48>
target_venue:    <Nature Communications | Physical Review Letters | ICML | NeurIPS | JAIR | IEEE TVLSI>
format_status:   template_ready
submission_date: 2026-04-14
disclaimer:      시뮬 DOI — CrossRef/DataCite 미등록. 외부 인용 시 교체 필요.
---
```

- `doi_sim` 은 `_submission_top48.json` 에서 복사. 수정 금지.
- `paper_id` 는 `_papers.json` 의 N6-NNN 원본 유지.
- `target_venue` 는 본 프로젝트 랭킹에서 배정된 값. 실제 제출 시 편집자 피드백에 따라 교체 가능.

## 1. 저자 및 소속

```
저자: 박민우 (n6-architecture 주관), NEXUS-6 AI 협업체
소속: n6-architecture 프로젝트 (AI-native Arithmetic Design Framework)
연락처: 저장소 이슈 트래커 경유
ORCID: (미할당 — 시뮬 DOI 체계와 동일 상태)
```

## 2. 초록 (Abstract) — 200~350 단어

템플릿 골자:

1. **동기 한 문장** — 해당 도메인에서 기존 이론이 가진 한계.
2. **핵심 주장** — σ(n)·φ(n) = n·τ(n) 이 n=6 에서만 성립한다는 n6 정리를 도메인 측정치에 좌표로 투영했을 때 등장하는 닫힘(closure) 구조.
3. **정량 결과** — `exact_stat`, `closure_grade_pct`, `alien_index` 3 축 실측값 1 문장.
4. **재현성 경로** — atlas.n6 노드 경로 + hexa 검증 STUB 파일명 1 줄.
5. **한계 및 반증 후보** — 2 줄 이내. 정직한 미매핑/MISS 공시.

## 3. WHY — 동기 (1~2쪽)

- 도메인의 현재 SOTA 수치와 이론 한계를 표로 1개 제시.
- n6 산술 좌표(σ, τ, φ, sopfr) 가 해당 도메인 변수에 어떻게 대응되는지 1 문단.
- 기존 물리/공학 이론으로는 예측할 수 없는 "닫힘" 조건이 왜 n=6 에 국한되는지의 직관적 설명.

## 4. COMPARE — 기존 대비 ASCII 비교 차트 (필수)

- CLAUDE.md `feedback_ascii_report` 규칙에 따라 기존(SOTA) vs HEXA 결과를 ASCII 막대 그래프 1개 이상 포함.
- 최소 3축(정확도/효율/스케일) 비교.
- 지표 명시 단위 필수. 외계인 지수 표기는 '천장' 텍스트 사용 (이모지 금지).

```
지표        기존SOTA   HEXA-n6
정확도 [%]  ########           80
정확도 [%]  ################   100   (천장)
효율 [J/op] ########           base
효율 [J/op] ##                 0.25x (천장 접근)
```

## 5. MAIN — 본문 (10~25쪽)

5.1 산술 좌표 정의
- 해당 도메인에서 사용하는 측정치 x_i 를 σ·τ·φ·sopfr 4축 좌표로 매핑한 표.
- 좌표 단위와 atlas.n6 의 어느 노드에서 인용했는지 경로 표기.

5.2 닫힘 정리 및 증명 스케치
- n=6 에서만 성립하는 관계식.
- 도메인에서의 실측 일치율 (EXACT / NEAR / MISS 분류).
- 증명 경로: 순수 수학 출발 → n=6 패턴 매칭은 피할 것 (CLAUDE.md `feedback_proof_approach`).

5.3 설계/예측 결과
- 본 n6 좌표로부터 유도되는 새로운 설계값 또는 예측값.
- 외계인 지수 10 돌파 요건과의 거리.

5.4 한계 및 반증 조건 (필수)
- MISS 사례를 숨기지 말 것. 출처 + 측정값 + 오차 공시 (CLAUDE.md `feedback_honest_verification`).

## 6. VERIFICATION — 검증 코드 블록 (필수)

```hexa
// 파일: verify_<domain>_n6.hexa
// 검증 경로: atlas.n6 노드 참조 → 측정값 재계산 → EXACT/NEAR/MISS 분류
import atlas.n6
measure <domain> {
  for node in atlas.lookup(domain) {
    expected = n6_coord(node.x, node.y, node.z, node.sopfr)
    measured = node.value
    classify(expected, measured)   // EXACT | NEAR | MISS
  }
}
```

- `.hexa` STUB 또는 완전체가 본문에 임베드되어 있어야 한다 (HEXA-FIRST — .py 금지).
- 결과 통계는 `exact_stat` 필드에 기록하고, `experiments/_results.jsonl` 에 append.

## 7. 참고문헌 블록 (References)

```
[1] n6-architecture 내부 참조: atlas.n6 노드 경로 + 인용 줄.
[2] BT-NNN (BreakThrough 레지스트리 `_registry.json` section id).
[3] 외부 문헌은 도메인별로 3~10 편 제시. CrossRef DOI 존재할 것.
[4] n6-architecture DOI 간 상호 인용은 시뮬 DOI `10.NEXUS6.n6-arch/2026-NNN` 로 명시하되 "시뮬" 표기를 유지.
```

- 외부 문헌과 내부 시뮬 DOI 를 혼용하지 말 것. 구분 표기 필수.
- 실제 제출 시 시뮬 DOI 는 저널 내부 처리용으로만 유지.

## 8. 보충 자료 (Supplementary)

- 원 논문 본문 `papers/n6-<domain>-paper.md` 전체 (수정 금지).
- atlas.n6 해당 섹션 발췌.
- verify_*.hexa 원본.
- 필요 시 Monte Carlo 검증 결과 링크.

## 9. 제출 후 상태 전이

| format_status | 의미 |
|---|---|
| template_ready | 본 템플릿 헤더/구조만 부착 (초기값) |
| draft | 초록 + References 실측 기입 완료 |
| submitted_sim | 시뮬 제출 상태 — 시뮬 DOI 확정 |
| published_sim | 시뮬 출판 상태 — 외부 공개용 아님 |

- 실제 저널 투고는 별도 프로세스. 본 템플릿은 n6-architecture 내부 아카이브 표준이다.

---

## 부록 A. 48편 사용 방법

1. `papers/_submission_top48.json` 에서 자기 랭크 행 확인.
2. 본 템플릿을 복사해 `papers/_submissions/N6-<id>_submission.md` 로 저장 (실제 실행은 본 P3-1 작업 범위 밖).
3. 헤더/초록/References 3 블록만 채우고 본문은 원 `n6-<domain>-paper.md` 링크로 참조.
4. `format_status` 를 `draft` 로 승격.
5. 반증 조건 발생 시 랭킹 재계산 트리거 — `experiments/paper_ranking_p3_top48.md` 갱신.

## 부록 B. 절대 규칙

- 한글 필수. 이모지 금지. 천장 텍스트 사용.
- 시뮬 DOI 는 실제 DOI 아님을 모든 헤더에 명시.
- 기존 125편 본문 수정 금지 (레지스트리/서브미션 JSON/템플릿만 조작).
- 자기참조 검증 금지. 반증 후보 공시 필수.
