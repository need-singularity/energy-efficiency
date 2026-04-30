#!/bin/sh
# raw 15 strengthening 2026-04-30 personal-path-leak-ban-iter5: commit-msg
# hook gate. Blocks commits whose message body contains operator-username
# path leaks (Mac /Users/<name>/ + Linux /home/<name>/) — closes the gap
# left by staged-scan.sh which only scans staged file content.
#
# This hook receives the commit message file path as $1 (per git docs).
# Exit 0 = message clean; Exit 1 = leak detected, abort commit.
# Bypass: HIVE_SAFETY_ALLOW='<reason>' (logged, not silent).

set -eu

if [ -n "${HIVE_SAFETY_ALLOW:-}" ]; then
  # raw 15 strengthening 2026-04-30 personal-path-leak-ban-iter7: bypass
  # audit ledger per raw 77 schema.
  REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "")"
  if [ -n "$REPO_ROOT" ] && [ -d "$REPO_ROOT/state" ]; then
    AUDIT_DIR="$REPO_ROOT/state/safety_bypass_audit"
    mkdir -p "$AUDIT_DIR" 2>/dev/null || true
    TS="$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
    USR="$(id -un 2>/dev/null || echo unknown)"
    SLUG="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo detached)"
    printf '{"ts":"%s","actor":"commit-msg-scan","kind":"bypass","reason":"%s","branch":"%s","scanner_user":"%s"}\n' \
      "$TS" "$(printf '%s' "$HIVE_SAFETY_ALLOW" | sed 's/"/\\"/g')" "$SLUG" "$USR" \
      >> "$AUDIT_DIR/audit.jsonl" 2>/dev/null || true
  fi
  echo "[safety] commit-msg-scan bypassed: $HIVE_SAFETY_ALLOW" >&2
  exit 0
fi

msg_file="${1:-}"
if [ -z "$msg_file" ] || [ ! -f "$msg_file" ]; then
  exit 0
fi

# Same patterns as staged-scan.sh PERSONAL_CONTENT_RE.
PERSONAL_CONTENT_RE='/Users/[a-z][a-z0-9_-]+/|/home/[a-z][a-z0-9_-]+/'
PERSONAL_PLACEHOLDER_RE='<user>|<username>|<remote-user>'

# Strip lines starting with '#' (git commit message comments) before scan.
# Strip placeholder lines.
cleaned=$(grep -v '^#' "$msg_file" 2>/dev/null | grep -Ev "$PERSONAL_PLACEHOLDER_RE" || true)

if printf '%s' "$cleaned" | grep -Eq "$PERSONAL_CONTENT_RE"; then
  echo >&2
  echo "✗ hive safety gate — commit message contains operator-username path leak:" >&2
  printf '%s' "$cleaned" | grep -nE "$PERSONAL_CONTENT_RE" | head -5 >&2
  echo >&2
  echo "  raw 15 strengthening 2026-04-30 personal-path-leak-ban-iter5: replace" >&2
  echo "  /Users/<actual-user>/ or /home/<actual-user>/ with placeholder form" >&2
  echo "  (e.g. \$HOME, ~/, <user>, <username>) before committing." >&2
  echo "  Bypass with HIVE_SAFETY_ALLOW='<reason>' if intentional." >&2
  exit 1
fi

exit 0
