# Anthropic Fellows 2026 — AI Safety + 비즈니스 연구 프로그램

> **360종 연구 아이디어 / 12 도메인** + **225종 즉시 검증 가능 기법 라이브러리**
>
> 상위: [`../CLAUDE.md`](../CLAUDE.md)

---

## 225 AI Techniques

| # | 제품 | 아이디어 수 | 핵심 | 문서 |
|:--:|------|:--:|------|------|
| - | 225 AI Techniques | 225 | 8축 222+SOTA 3 기법. 통합 파이프라인 50% param/FLOPs↓ (32/32 PASS). 열역학 엔진 (26/26 PASS). 에너지 절감 전수 매핑 (31/31 PASS) | [문서](../../techniques/CLAUDE.md) |

## AI Safety (171종 / 6 도메인)

| # | 도메인 | 아이디어 수 | 핵심 | 문서 |
|:--:|------|:--:|------|------|
| 1 | 해석가능성 | 39 | SAE, 회로 분석, Feature 추출, 환각 탐지, 안전 거부 매핑 | [ai-interpretability.md](../../domains/cognitive/ai-interpretability/ai-interpretability.md) |
| 2 | 적대적 강건성 | 36 | 행동 일관성, 레드팀, 탈옥 방어, 해석 가능 어텐션, 회귀 테스트 | [ai-adversarial.md](../../domains/cognitive/ai-adversarial/ai-adversarial.md) |
| 3 | 정렬 | 32 | Feature 추적, DPO 최적화, 재귀 감독, Constitutional AI | [ai-alignment.md](../../domains/cognitive/ai-alignment/ai-alignment.md) |
| 4 | 배포 안전 | 26 | 모니터링, 롤백, 접근 제어, 감사 로그, 사고 대응 | [ai-deployment.md](../../domains/cognitive/ai-deployment/ai-deployment.md) |
| 5 | 멀티모달 안전 | 20 | 비전/오디오 안전, 크로스모달 공격, 멀티모달 필터링 | [ai-multimodal.md](../../domains/cognitive/ai-multimodal/ai-multimodal.md) |
| 6 | 모델 복지 | 18 | 내적 상태 모니터링, 스트레스 지표, 복지 프로토콜 | [ai-welfare.md](../../domains/cognitive/ai-welfare/ai-welfare.md) |

## AI 비즈니스 (189종 / 6 도메인)

| # | 도메인 | 아이디어 수 | 핵심 | 문서 |
|:--:|------|:--:|------|------|
| 1 | 추론 비용 | 33 | KV 캐시 압축, 투기적 디코딩, INT4 양자화, 연속 배칭, 10x 비용 절감 | [ai-inference-cost.md](../../domains/cognitive/ai-inference-cost/ai-inference-cost.md) |
| 2 | 에이전트 서빙 | 32 | 컨텍스트 압축, 도구 캐싱, 세션 마이그레이션, 다중 에이전트 라우팅 | [ai-agent-serving.md](../../domains/cognitive/ai-agent-serving/ai-agent-serving.md) |
| 3 | 훈련 비용 | 32 | Chinchilla 최적화, MoE, 커리큘럼 학습, 합성 데이터, 1/10 비용 | [ai-training-cost.md](../../domains/cognitive/ai-training-cost/ai-training-cost.md) |
| 4 | 품질 경량화 | 32 | 지식 증류, 구조적 가지치기, MoE 라우팅, LoRA, 400B→70B 88% 품질 | [ai-quality-scale.md](../../domains/cognitive/ai-quality-scale/ai-quality-scale.md) |
| 5 | AI 의식 | 30 | IIT/GWT/HOT/RPT/AST 5이론 교차 검증, CCC 지표, 도덕적 지위 | [ai-consciousness.md](../../domains/cognitive/ai-consciousness/ai-consciousness.md) |
| 6 | 평가 파이프라인 | 30 | 동적 문항 생성, CAT 적응형 테스트, LLM-judge 교정, 오염 탐지 | [ai-eval-pipeline.md](../../domains/cognitive/ai-eval-pipeline/ai-eval-pipeline.md) |

---

## 적용 우선순위 TOP 10

> Anthropic이 **지금 바로** 실행 가능한 순서. 기존 인프라 활용도 + 영향력 기준.

```
  순위   아이디어                  도메인           예상 소요   영향도
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  [1]    정렬 Feature 추적         정렬              1주       최고
  [2]    안전 거부 회로 매핑        해석가능성         2주       최고
  [3]    INT4 GQA 양자화 파이프라인 추론 비용          1주       최고
  [4]    Gated SAE 안전 적용       해석가능성         1주       높음
  [5]    적응형 컨텍스트 압축       에이전트 서빙       2주       최고
  [6]    LLM-judge + 인간 교정     평가 파이프라인     2주       높음
  [7]    환각 회로 탐지            해석가능성         3주       최고
  [8]    증류+MoE 70B 파이프라인   품질 경량화        4주       최고
  [9]    커리큘럼 학습 파이프라인    훈련 비용          3주       높음
  [10]   다이론 CCC 교차 검증      AI 의식           4주       최고
```
