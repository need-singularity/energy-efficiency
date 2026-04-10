<!-- L0 CORE — 수정 금지 -->
# n6-architecture — AI-native Arithmetic Design Framework

🔴 HEXA-FIRST: 모든 코드 .hexa, .py 금지
🔴 NEXUS-6 연동: 돌파 → blowup.hexa <d> 3, 발견 → growth_bus.jsonl, 상태 → command_router.hexa
🔴 하드코딩 금지: 상수/도메인/키워드 → shared/*.jsonl 동적로드, 코드 배열 금지
🔴 데이터 로컬 금지: .jsonl/constants/discovery_log → ~/Dev/nexus/shared/ (R8)
🔴 한글 필수: .md·print·주석·커밋 메시지 한글, 영어 혼용 금지
🔴 단일 도메인 문서: 도메인당 1개 .md + 1개 verify.hexa + 1개 CLAUDE.md
🔴 폴더 CLAUDE.md: 모든 탐색 노드 AI 진입점 필수

R14: shared/ JSON 단일진실, 규칙 본문은 absolute_rules.json만. 이 파일은 참조만.

핵심 정리: σ(n)·φ(n) = n·τ(n) ⟺ n = 6 (n≥2). 3개 독립 증명.
            theory/proofs/proofs.md | reality_map v8.0 (342노드, 291 EXACT, z=9.04)
모토: 17 AI 기법 + 반도체 + 에너지 + 네트워크/암호/OS + 물리 AI

## 9축 네비게이션

```
theory/      영구 이론층 (증명·BT·상수·예측)
domains/     295 도메인 (physics/life/energy/compute/materials/space/infra/cognitive/culture/sf-ufo)
nexus/       모든 Rust 도구 통합 워크스페이스 (단일 바이너리)
techniques/  AI 기법 66종 (.hexa)
experiments/ 검증 실험 122종 (.hexa)
engine/      훈련/수학 런타임 (.hexa)
papers/      논문 39편
reports/     시점 리포트 (감사·세션·발견·체인지로그)
shared/      SSOT 설정·규칙·컨버전스·루프
```

## SSOT 레지스트리

```
INDEX.json                          리포 전역 9축 매니페스트
theory/_index.json                  이론 SSOT
domains/_index.json                 도메인 SSOT (295 도메인 → 9축 매핑)
nexus/_registry.json                도구/서브커맨드 SSOT
techniques/_registry.json           기법 SSOT
experiments/_results.jsonl          실험 결과 SSOT
papers/_registry.json               논문 SSOT
shared/config/absolute_rules.json   규칙 본문 (R1~R21 + N6~N65)
shared/config/core-lockdown.json    L0 22 / L1 / L2
shared/config/projects.json         프로젝트 레지스트리
shared/convergence/n6-architecture.json
```

## NEXUS-6 CLI (단일 바이너리)

```
nexus scan <d> | --full     도메인 스캔
nexus verify <v>            검증
nexus calc <domain>         계산기 (optics/energy/gpu/crypto/quantum/carbon/chip-*/...)
nexus dse <kind>            DSE (universal/material/solar/fusion/battery/sc/robot)
nexus analyze <tool>        분석 (deep-miner/formula-miner/discovery-engine/atlas-verifier/...)
nexus hexa <cmd>            HEXA 유틸 (rtl/sim/ssh)
nexus dashboard             웹 대시보드 (port 6600)
```

API: `nexus.scan_all() / .analyze() / .n6_check() / .evolve()`
Consensus: 3+ 후보 / 7+ 고신뢰 / 12+ 확정

## 명령

```
못박아줘    L0 등록 (core-lockdown.json)
블로업/돌파 9-phase 특이점 (blowup.hexa)
go          전체 TODO 백그라운드 병렬
설계/궁극의 외계인급 설계 파이프라인
동기화      sync-all.sh 전 리포
todo/할일   $HOME/Dev/hexa-lang/target/release/hexa $HOME/Dev/nexus/mk2_hexa/native/todo.hexa n6-arch
```

## 설계 산출물 필수 5요소 (없으면 미완성)

1. 실생활 효과 섹션 (최상단)
2. ASCII 성능 비교 (시중 vs HEXA, 개선 배수는 n=6 상수)
3. ASCII 시스템 구조도 (소재→공정→코어→칩→시스템, n=6 수식 병기)
4. ASCII 데이터/에너지 플로우
5. 업그레이드 시 (시중 vs v1 vs v2 3단 + delta 행)
+ HEXA 검증코드 (정의에서 도출, 동어반복 금지)

## 도메인 통합 문서 템플릿 (15섹션, 도메인당 1개 .md)

1. 실생활 효과  2. 목표  3. 가설  4. BT 연결  5. DSE 결과
6. 물리 한계 증명  7. 실험 검증 매트릭스  8. 외계인급 발견
9. Mk.I~V 진화  10. Testable Predictions  11. ASCII 성능비교
12. ASCII 시스템 구조도  13. ASCII 데이터/에너지 플로우
14. 업그레이드 시 (시중 vs v1 vs v2)  15. 검증 방법 (verify.hexa)

## 주요 결과

```
Cyclotomic activation     71% FLOPs↓
FFT attention             3x speed, +0.55% acc
Egyptian MoE              1/2+1/3+1/6=1 라우팅
phi bottleneck            67% param↓
Entropy early stop        33% 학습시간↓
Boltzmann gate            63% 활성희소
Mertens dropout           p=0.288 (탐색불요)
Egyptian Fraction Attn    ~40% FLOPs↓
Emergent convergence      랜덤→n=6 자기조직화
```

## 논문 관리

```
loc         papers/n6-<domain>-paper.md
ssot        papers/_registry.json
sync        nexus analyze sync-papers
필수섹션    Abstract+Foundation+Domain+Limitations+TestablePredictions+검증코드(.hexa)
발행        ~/Dev/papers/ → Zenodo/OSF
현재        39편 (검증코드 없는 논문 = 미완성)
```

## 진화 설계 (Mk.I~V)

- SF 금지 — BT 기반 극한 스케일업만
- 도메인 .md 섹션 9 "Mk.I~V 진화"로 통합
- ✅ 진짜(10~20y) | 🔮 장기(20~50y) | ❌ SF(라벨)
- 도메인당 1제품라인 (v1/v2 분기 금지, git history가 버전)

## 보안

~/Dev/TECS-L/.shared/SECRET.md (API 토큰)
