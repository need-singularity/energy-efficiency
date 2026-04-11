# experiments/dse

목적: DSE 322→400 확장·cross_dse_fusion v2·에너지-성능 파레토 스윕 설계 SSOT
축: experiments
상위: ../CLAUDE.md

## 하위
- dse_400_expansion_plan.md       — 322→400 TOML 공간 확장 계획서 (78 신규 도메인)
- cross_dse_fusion_v2_design.md   — v2 설계 (67,883→100K pair 돌파, diff 분석)
- energy_pareto_sweep_plan.md     — 전 400 도메인 재측정 파이프라인
- cross_dse_fusion_v2.hexa        — v2 구현 초안 (pseudocode, R12/@fuse/@parallel 표기; 현 hexa 파서 미지원)
- cross_dse_fusion_v2_run.hexa    — **실행본** (strset 기반, 5 지표, top-K 온라인, R28 자동 흡수)

## SSOT
- 실행 결과: shared/dse/dse_cross_results_v2.json
- 실행 리포트: reports/discovery/dse-v2-results-<date>.md

## 진입 명령
- hexa run cross_dse_fusion_v2_run.hexa --dir <TOML 디렉토리> --out <json> --atlas <atlas.n6> --report <md>
- hexa run cross_dse_fusion_v2.hexa (설계 초안 — pseudocode)
- nexus dse cross --v2

## 절대규칙
- 한글 필수 (.md/주석/커밋)
- HEXA-FIRST (.py 금지)
- R12 AI-NATIVE FIRST — 저수준 마이크로 최적화 금지
- R28 자동 흡수 — 결과는 atlas.n6 로만 기록

## 관련 링크
- 루트: ../CLAUDE.md + INDEX.json
- cross 실험: ../cross/CLAUDE.md
- 공통 규칙: /Users/ghost/Dev/nexus/shared/rules/common.json
- 프로젝트 규칙: /Users/ghost/Dev/nexus/shared/rules/n6-architecture.json
