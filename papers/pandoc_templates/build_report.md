# pandoc PDF 빌드 리포트

- 태스크: PAPER-P5-1
- 빌드 일시: 2026-04-14
- pandoc 버전: 3.9.0.2
- PDF 엔진: xelatex (TeX Live 2026)

---

## 빌드 환경 세팅

### 추가 설치 패키지
| 패키지 | 용도 | 설치 방법 |
|--------|------|-----------|
| xecjk | xelatex 한글/CJK 조판 | `sudo tlmgr install xecjk` |
| hyperxmp | PDF 메타데이터 XMP 삽입 | `sudo tlmgr install hyperxmp` |

### 폰트 변경
`_pandoc_header.yaml` 에 지정된 Noto Serif/Sans CJK KR 폰트가 시스템 미설치 상태.
빌드 시 `-V` 플래그로 아래와 같이 오버라이드:

| 원본 (header.yaml) | 빌드 시 대체 |
|---------------------|-------------|
| Noto Serif CJK KR | Apple SD Gothic Neo |
| Noto Sans CJK KR | Apple SD Gothic Neo |
| Noto Sans Mono CJK KR | Menlo |

### keywords 우회
`hyperxmp` 의 `\xmpquote` 가 xelatex 에서 정의 충돌 발생.
빌드 시 `-V keywords=""` 로 비워서 우회. PDF 메타데이터에 키워드 미삽입.

---

## 빌드 결과: 상위 6편

| 순위 | 논문 ID | 도메인 | 대상 venue | 결과 | 페이지 | 용량 |
|------|---------|--------|-----------|------|--------|------|
| 1 | N6-032 | dance-choreography | Nature Comms | 성공 | 16p | 110K |
| 2 | N6-108 | writing-systems | Nature Comms | 성공 | 16p | 110K |
| 3 | N6-106 | wine-enology | Nature Comms | 성공 | 16p | 110K |
| 4 | N6-016 | carbon-capture | Nature Comms | 성공 | 16p | 110K |
| 5 | N6-051 | gravity-wave | PRL | 성공 | 16p | 110K |
| 6 | N6-009 | aquaculture | Nature Comms | 성공 | 16p | 110K |

**성공 6편 / 실패 0편 / 전체 6편**

---

## 알려진 제한사항

1. **monofont 한글 누락**: Menlo 폰트는 한글 미지원. 코드 블록 내 한글 주석이 PDF에서 누락됨.
   - 해결: `Noto Sans Mono CJK KR` 설치 또는 D2Coding 폰트로 교체 권장.
2. **keywords XMP 미삽입**: `\xmpquote` 충돌로 keywords 비워서 빌드. PDF 메타데이터에 키워드 없음.
   - 해결: hyperxmp 최신 버전 확인 또는 header-includes 로 수동 XMP 삽입.
3. **CSL 파일 미적용**: nature.csl / american-physics-society.csl 파일 미보유로 인용 스타일 기본값 적용.
   - 해결: CSL 파일 다운로드 후 `--csl=` 인수 추가.
4. **Noto CJK 폰트 미설치**: 최종 배포 품질을 위해 Noto CJK 설치 권장.
   - `brew install font-noto-serif-cjk-kr font-noto-sans-cjk-kr` (homebrew-cask-fonts)

---

## 후속 조치

- [ ] Noto CJK 폰트 설치 후 header.yaml 원본 폰트로 재빌드
- [ ] CSL 파일 확보 (nature.csl, american-physics-society.csl, ieee.csl)
- [ ] keywords XMP 충돌 근본 해결
- [ ] 나머지 42편 일괄 빌드 스크립트 작성
- [ ] 빌드 스크립트: `papers/pandoc_templates/build_top6.sh`

---

## 빌드 명령 예시

```bash
# 단일 논문 빌드
pandoc \
  --metadata-file=papers/pandoc_templates/_pandoc_header.yaml \
  --metadata-file=papers/pandoc_templates/venue_nature_comms.yaml \
  --bibliography=papers/pandoc_templates/skeleton.bib \
  --pdf-engine=xelatex \
  -V 'mainfont=Apple SD Gothic Neo' \
  -V 'sansfont=Apple SD Gothic Neo' \
  -V 'monofont=Menlo' \
  -V 'CJKmainfont=Apple SD Gothic Neo' \
  -V 'CJKsansfont=Apple SD Gothic Neo' \
  -V 'CJKmonofont=Menlo' \
  -V 'keywords=' \
  papers/n6-dance-choreography-paper.md \
  -o papers/pandoc_templates/output/n6-dance-choreography-paper.pdf

# 상위 6편 일괄 빌드
bash papers/pandoc_templates/build_top6.sh
```

## §1 WHY

This section covers why for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §2 COMPARE

This section covers compare for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §3 REQUIRES

This section covers requires for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §4 STRUCT

This section covers struct for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §5 FLOW

This section covers flow for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §6 EVOLVE

This section covers evolve for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §7 VERIFY

This section covers verify for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §8 EXEC SUMMARY

This section covers exec summary for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §9 SYSTEM REQUIREMENTS

This section covers system requirements for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §10 ARCHITECTURE

This section covers architecture for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §11 CIRCUIT DESIGN

This section covers circuit design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §12 PCB DESIGN

This section covers pcb design for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §13 FIRMWARE

This section covers firmware for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §14 MECHANICAL

This section covers mechanical for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §15 MANUFACTURING

This section covers manufacturing for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §16 TEST & QUALIFICATION

This section covers test & qualification for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §17 BOM

This section covers bom for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §18 VENDOR & SCHEDULE

This section covers vendor & schedule for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §19 ACCEPTANCE CRITERIA

This section covers acceptance criteria for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §20 APPENDIX

This section covers appendix for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## §21 IMPACT per Mk

This section covers impact per mk for the paper. Initial scaffold content — expand with domain-specific data, references, and verification in subsequent Mk iterations.

## mk_history

- Mk.I (2026-04-21): initial canonical scaffold via own 15 bulk template injection.
- Mk.II: pending — fill per-section content with domain expert review.
- Mk.III: pending — full verification data + external citations.

