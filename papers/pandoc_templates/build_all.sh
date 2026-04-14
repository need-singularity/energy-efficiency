#!/usr/bin/env bash
# ============================================================
# n6-architecture 전량 논문 pandoc PDF 빌드 스크립트 (126편+)
# ============================================================
# 생성일: 2026-04-14
# 태스크: PAPER-P5-3
# 필수 환경: pandoc 3.9+, xelatex (TeX Live 2026), xeCJK, hyperxmp
# 폰트: Apple SD Gothic Neo (macOS 내장), Menlo
# 사용법:
#   bash papers/pandoc_templates/build_all.sh 2>&1 | tee build_log.txt
# 옵션:
#   PARALLEL=N 병렬 수 (기본 4)
#   LIMIT=N   처음 N 편만 빌드 (기본 0 = 전량)
# venue 매핑:
#   1) _top48_pandoc_manifest.json 에 정의된 venue_template 우선
#   2) 미정의 시 default = venue_nature_comms.yaml
# ============================================================

# bash 3.2 (macOS 기본) 호환: mapfile/readarray 사용 금지
# set -u 제거 (배열 빈 참조 허용)

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$PROJECT_ROOT"

OUTDIR="papers/pandoc_templates/output"
HEADER="papers/pandoc_templates/_pandoc_header.yaml"
BIB="papers/pandoc_templates/skeleton.bib"
MANIFEST="papers/pandoc_templates/_top48_pandoc_manifest.json"
DEFAULT_VENUE="papers/pandoc_templates/venue_nature_comms.yaml"
LOGDIR="papers/pandoc_templates/output/_build_logs"

PARALLEL="${PARALLEL:-4}"
LIMIT="${LIMIT:-0}"

mkdir -p "$OUTDIR" "$LOGDIR"

# ---- venue 매핑 사전 추출 (_top48_pandoc_manifest.json) ----
# 파이썬/jq 없이 awk 로 input_md -> venue_template 매핑을 단일 줄로 추출
VENUE_MAP_FILE="$(mktemp -t n6_venue_map.XXXXXX)"

if [ -f "$MANIFEST" ]; then
  awk '
    /"input_md"/      { gsub(/[",]/,"",$2); input=$2 }
    /"venue_template"/{ gsub(/[",]/,"",$2); print input "|" $2 }
  ' "$MANIFEST" > "$VENUE_MAP_FILE"
fi

# venue 조회 함수
lookup_venue() {
  local md="$1"
  local hit
  hit=$(grep -F "${md}|" "$VENUE_MAP_FILE" 2>/dev/null | head -1 | cut -d'|' -f2)
  if [ -n "$hit" ]; then
    echo "$hit"
  else
    echo "$DEFAULT_VENUE"
  fi
}
export -f lookup_venue
export VENUE_MAP_FILE DEFAULT_VENUE

# ---- 빌드 대상 수집 (bash 3.2 호환) ----
PAPERS_LIST="$(mktemp -t n6_papers.XXXXXX)"
trap 'rm -f "$VENUE_MAP_FILE" "$PAPERS_LIST"' EXIT
ls papers/n6-*-paper.md 2>/dev/null | sort > "$PAPERS_LIST"
TOTAL=$(wc -l < "$PAPERS_LIST" | tr -d ' ')

if [ "$LIMIT" -gt 0 ] && [ "$LIMIT" -lt "$TOTAL" ]; then
  head -n "$LIMIT" "$PAPERS_LIST" > "${PAPERS_LIST}.tmp" && mv "${PAPERS_LIST}.tmp" "$PAPERS_LIST"
  TOTAL="$LIMIT"
fi

echo "=============================================="
echo " n6-architecture 전량 빌드 시작"
echo "=============================================="
echo " 시각: $(date '+%Y-%m-%d %H:%M:%S')"
echo " 대상: $TOTAL 편"
echo " 병렬: $PARALLEL"
echo " pandoc: $(pandoc --version | head -1)"
echo " xelatex: $(xelatex --version | head -1)"
echo "----------------------------------------------"

# ---- 단일 논문 빌드 함수 (xargs 에서 실행) ----
build_one() {
  local INPUT="$1"
  local BASENAME OUTPUT VENUE LOG START END ELAPSED PAGES SIZE
  BASENAME=$(basename "$INPUT" .md)
  OUTPUT="papers/pandoc_templates/output/${BASENAME}.pdf"
  LOG="papers/pandoc_templates/output/_build_logs/${BASENAME}.log"
  VENUE=$(lookup_venue "$INPUT")

  START=$(date +%s)
  if pandoc \
      --metadata-file="papers/pandoc_templates/_pandoc_header.yaml" \
      --metadata-file="$VENUE" \
      --bibliography="papers/pandoc_templates/skeleton.bib" \
      --pdf-engine=xelatex \
      -V 'mainfont=Apple SD Gothic Neo' \
      -V 'sansfont=Apple SD Gothic Neo' \
      -V 'monofont=Menlo' \
      -V 'CJKmainfont=Apple SD Gothic Neo' \
      -V 'CJKsansfont=Apple SD Gothic Neo' \
      -V 'CJKmonofont=Menlo' \
      -V 'keywords=' \
      "$INPUT" \
      -o "$OUTPUT" > "$LOG" 2>&1; then
    END=$(date +%s)
    ELAPSED=$((END - START))
    PAGES=$(pdfinfo "$OUTPUT" 2>/dev/null | awk '/^Pages:/{print $2}')
    SIZE=$(ls -l "$OUTPUT" 2>/dev/null | awk '{print $5}')
    echo "[OK ] ${BASENAME} venue=$(basename "$VENUE" .yaml) pages=${PAGES:-?} size=${SIZE:-?}B elapsed=${ELAPSED}s"
  else
    END=$(date +%s)
    ELAPSED=$((END - START))
    echo "[FAIL] ${BASENAME} venue=$(basename "$VENUE" .yaml) elapsed=${ELAPSED}s log=${LOG}"
  fi
}
export -f build_one

# ---- 병렬 실행 (xargs -P) ----
RUN_LOG="$(mktemp -t n6_build_run.XXXXXX)"
BUILD_START=$(date +%s)
cat "$PAPERS_LIST" | xargs -n 1 -P "$PARALLEL" -I {} bash -c 'build_one "$@"' _ {} | tee "$RUN_LOG"
BUILD_END=$(date +%s)
BUILD_ELAPSED=$((BUILD_END - BUILD_START))

# ---- 집계 (이번 실행 기준) ----
BUILT=$(grep -c '^\[OK \]' "$RUN_LOG" | tr -d ' ')
FAILED=$(grep -c '^\[FAIL\]' "$RUN_LOG" | tr -d ' ')
rm -f "$RUN_LOG"

echo "----------------------------------------------"
echo " 빌드 종료"
echo " 총 경과: ${BUILD_ELAPSED}s"
echo " 시도:   $TOTAL"
echo " 성공:   $BUILT"
echo " 실패:   $FAILED"
echo " 출력 디렉토리: $OUTDIR"
echo " 실패 로그: $LOGDIR/*.log"
echo "=============================================="
