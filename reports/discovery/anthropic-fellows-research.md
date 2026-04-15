# Anthropic Fellows 2026 — AI Safety 연구 프로그램

> **171종 연구 아이디어 / 6 도메인** + **즉시 검증 가능한 성능 기법 4종**
>
> 상위: [`../CLAUDE.md`](../CLAUDE.md)

---

# 즉시 검증 가능 — 성능/자원/속도

> 돌려보면 바로 결과가 나오는 것들. Anthropic 인프라에서 즉시 재현 가능.

| 천장확인 | ver | 완성제품 | 핵심 | 문서 |
|:--:|:---:|---------|------|------|
| ✅ | v6 | **225 Techniques** | 8축 222기법+SOTA 3 — arch 72, optim 75, attention 27, compress 18, moe 13, sparse 10, graph 7, sota 3 | [문서](../../techniques/CLAUDE.md) |
| ✅ | v2 | **Full N6 Pipeline** | 17기법 통합: 50% 파라미터↓, 50% FLOPs↓, 46% 희소성 — 32/32 PASS 검증 | [문서](../../experiments/experiment_full_n6_pipeline.py) |
| ✅ | v2 | **N6 Inevitability Engine** | 기법 11~16 + 3-Layer 열역학 (Dedekind+Jordan+Mobius+Carmichael+Boltzmann+Mertens) — 26/26 PASS | [문서](../../domains/compute/ai-efficiency/ai-efficiency.md) |
| ✅ | v2 | **AI Energy Savings Guide** | AdamW 5중쌍+LR+Inference 하이퍼파라미터 전수 매핑 — 31/31 PASS | [문서](../../reports/discovery/ai-energy-savings-guide.md) |

---

# AI Safety 연구 도메인 — 171종

| 천장확인 | ver | 완성제품 | 핵심 | 문서 |
|:--:|:---:|---------|------|------|
| ✅ | v1 | **해석가능성** | SAE 차세대 15 + 회로 매핑 12 + 해석 도구 12 = 39종 | [문서](../../domains/cognitive/ai-interpretability/ai-interpretability.md) |
| ✅ | v1 | **정렬** | 정렬 기법 비교 12 + 모델 유기체 10 + 확장 감독 10 = 32종 | [문서](../../domains/cognitive/ai-alignment/ai-alignment.md) |
| ✅ | v1 | **적대적 강건성** | 안전 평가 12 + 기만 탐지 8 + 에이전트 안전 10 + 아키텍처 6 = 36종 | [문서](../../domains/cognitive/ai-adversarial/ai-adversarial.md) |
| ✅ | v1 | **모델 복지** | 복지 감지 10 + 수학 검증 8 = 18종 | [문서](../../domains/cognitive/ai-welfare/ai-welfare.md) |
| ✅ | v1 | **멀티모달 안전** | 멀티모달 8 + 프라이버시 6 + 공정성 6 = 20종 | [문서](../../domains/cognitive/ai-multimodal/ai-multimodal.md) |
| ✅ | v1 | **배포 안전** | 훈련 4 + 추론 4 + 배포 프로토콜 10 + 프롬프트 방어 8 = 26종 | [문서](../../domains/cognitive/ai-deployment/ai-deployment.md) |

---

# 적용 우선순위 TOP 10

> Anthropic이 **지금 바로** 실행 가능한 순서. 기존 인프라 활용도 + 영향력 기준.

```
  순위   아이디어                  도메인           예상 소요   영향도
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  [1]    정렬 Feature 추적         정렬              1주       최고
  [2]    안전 거부 회로 매핑        해석가능성         2주       최고
  [3]    행동 일관성 테스트         적대적 강건성       1주       높음
  [4]    Gated SAE 안전 적용       해석가능성         1주       높음
  [5]    DPO 하이퍼파라미터 최적    정렬              3일       중간
  [6]    Mini-NEXUS 유기체 실험    정렬              4주       최고
  [7]    환각 회로 탐지            해석가능성         3주       최고
  [8]    안전 회귀 테스트 자동화    적대적 강건성       2주       높음
  [9]    해석 가능 어텐션           적대적 강건성       6주       높음
  [10]   재귀 감독 프로토콜         정렬              4주       최고
```
