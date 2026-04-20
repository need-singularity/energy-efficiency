# chip-materials — compute 도메인

목적: 반도체 소재 돌파 (Si/Diamond/SiC/GaN/InP/SiPh + 포토레지스트·도핑)
축: domains/compute
상위: ../CLAUDE.md

## 하위
- chip-materials.md (§1~§7 + §6, stdlib 검증코드 인라인)

## SSOT
- ../_index.json 의 compute.chip-materials 키 참조

## 진입 명령
- nexus scan chip-materials
- nexus verify chip-materials

## 절대규칙
- 한글 필수 (.md/주석/커밋)
- HEXA-FIRST (.py 금지, 검증은 .md 임베드 Python)
- 도메인당 문서 1개만
- n=6 마스터 항등식 σ·φ = n·τ = J₂ = 24 준수

## 관련 링크
- 선행: chip-process, chip-packaging, chip-yield
- 후속: chip-design, chip-architecture
- 루트: ../CLAUDE.md + INDEX.json
