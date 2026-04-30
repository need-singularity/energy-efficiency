#!/bin/sh
# raw-9-exemption: git pre-commit-style staged-content scanner — invoked
# from git pre-commit hook via core.hooksPath, which expects an executable
# script (not a hexa wrapper that double-spawns). Reviewed 2026-04-28.
# hive safety gate — staged-content scanner (L3 shared core)
# Exit 0  = all staged files pass
# Exit 1  = at least one violation; reasons printed to stderr
# Bypass:  HIVE_SAFETY_ALLOW='<reason>' …   (logged, not silent)

set -eu

if [ -n "${HIVE_SAFETY_ALLOW:-}" ]; then
  # raw 15 strengthening 2026-04-30 personal-path-leak-ban-iter7: bypass
  # logged to state/safety_bypass_audit/audit.jsonl per raw 77 schema so
  # repeated bypass usage is auditable. Skip audit on missing repo root
  # (hook may run outside hive).
  REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "")"
  if [ -n "$REPO_ROOT" ] && [ -d "$REPO_ROOT/state" ]; then
    AUDIT_DIR="$REPO_ROOT/state/safety_bypass_audit"
    mkdir -p "$AUDIT_DIR" 2>/dev/null || true
    TS="$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
    USR="$(id -un 2>/dev/null || echo unknown)"
    SLUG="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo detached)"
    printf '{"ts":"%s","actor":"staged-scan","kind":"bypass","reason":"%s","branch":"%s","scanner_user":"%s"}\n' \
      "$TS" "$(printf '%s' "$HIVE_SAFETY_ALLOW" | sed 's/"/\\"/g')" "$SLUG" "$USR" \
      >> "$AUDIT_DIR/audit.jsonl" 2>/dev/null || true
  fi
  echo "[safety] staged-scan bypassed: $HIVE_SAFETY_ALLOW" >&2
  exit 0
fi

# Filename patterns that indicate a secret-bearing file
SECRET_PATH_RE='(^|/)(\.env(\.[^/]+)?|\.aws/credentials|id_rsa|id_ed25519|id_ecdsa|credentials\.json)$|\.(pem|key|p12|pfx)$'
# Templates that match SECRET_PATH_RE but are intentionally committed
SAFE_PATH_RE='\.env\.(example|sample|template)$'
# Build artefacts / junk that should never be staged
JUNK_PATH_RE='(^|/)(node_modules|dist|build|coverage)/|\.log$|\.tsbuildinfo$'
# Per-file size ceiling (5 MiB)
MAX_BYTES=$((5 * 1024 * 1024))
# High-confidence secret content fingerprints
SECRET_CONTENT_RE='AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{36,}|sk-ant-api[0-9]{2}-[A-Za-z0-9_-]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----'
# raw 15 strengthening 2026-04-30 personal-path-leak-ban-iter4: block staged
# content with operator-username path leaks. Matches Mac /Users/<name>/ and
# Linux /home/<name>/ literals where <name> is a real OS account on the
# inventory hosts. Whitelist <user>/<username>/<remote-user> placeholder
# forms + state/* audit ledgers (per raw 77 operational record).
PERSONAL_CONTENT_RE='/Users/[a-z][a-z0-9_-]+/|/home/[a-z][a-z0-9_-]+/'
PERSONAL_PATH_EXEMPT_RE='^state/|^archive/|^exports/|^\.git/|\.hexa-cache/|^tool/no_hardcode_lint\.hexa$|^scripts/safety/staged-scan\.sh$|^scripts/safety/commit-msg-scan\.sh$|^scripts/safety/git-hooks/|^scripts/safety/safe-git\.sh$'
PERSONAL_PLACEHOLDER_RE='<user>|<username>|<remote-user>'

staged=$(git diff --cached --name-only --diff-filter=AM 2>/dev/null || true)
[ -z "$staged" ] && exit 0

TMP=$(mktemp)
trap 'rm -f "$TMP"' EXIT

printf '%s\n' "$staged" | while IFS= read -r f; do
  [ -z "$f" ] && continue

  if printf '%s' "$f" | grep -Eq "$SECRET_PATH_RE"; then
    if ! printf '%s' "$f" | grep -Eq "$SAFE_PATH_RE"; then
      printf '  SECRET_PATH    %s\n' "$f" >> "$TMP"
    fi
  fi

  if printf '%s' "$f" | grep -Eq "$JUNK_PATH_RE"; then
    printf '  JUNK_PATH      %s\n' "$f" >> "$TMP"
  fi

  # raw 15 strengthening 2026-04-30 personal-path-leak-ban-iter6: filename
  # itself MUST NOT embed operator-username path segments (e.g. aiden_log.txt
  # under tool/ — content scan catches usage but filename leaks the name to
  # ls/find/git log surfaces). Only flag when filename has a `/<user>/` or
  # _<user>_ pattern that matches an actual OS account in inventory. Conservative
  # match: explicit /Users/<name>/ or /home/<name>/ in path. Filename-side
  # hardcoded usernames need explicit operator declaration; out-of-scope here
  # (raw 247 placeholder for operator-name-token catalog when needed).
  if ! printf '%s' "$f" | grep -Eq "$PERSONAL_PATH_EXEMPT_RE"; then
    if printf '%s' "$f" | grep -Eq "$PERSONAL_CONTENT_RE"; then
      printf '  PERSONAL_NAME  %s   (raw 15 personal-path-leak-ban-iter6 filename match; HIVE_SAFETY_ALLOW=intent reason to bypass)\n' "$f" >> "$TMP"
    fi
  fi

  if [ -f "$f" ]; then
    size=$(wc -c < "$f" 2>/dev/null | tr -d ' ' || echo 0)
    if [ "${size:-0}" -gt "$MAX_BYTES" ]; then
      printf '  OVERSIZE       %s  (%s bytes)\n' "$f" "$size" >> "$TMP"
    fi
    if git show ":$f" 2>/dev/null | grep -Eq "$SECRET_CONTENT_RE"; then
      printf '  SECRET_CONTENT %s\n' "$f" >> "$TMP"
    fi
    # raw 15 strengthening 2026-04-30 personal-path-leak-ban-iter4 enforcement.
    if ! printf '%s' "$f" | grep -Eq "$PERSONAL_PATH_EXEMPT_RE"; then
      if git show ":$f" 2>/dev/null \
           | grep -Ev "$PERSONAL_PLACEHOLDER_RE" \
           | grep -Eq "$PERSONAL_CONTENT_RE"; then
        printf '  PERSONAL_PATH  %s   (raw 15 personal-path-leak-ban; HIVE_SAFETY_ALLOW=intent reason to bypass)\n' "$f" >> "$TMP"
      fi
    fi
  fi
done

if [ -s "$TMP" ]; then
  echo >&2
  echo "✗ hive safety gate — staged files violate policy:" >&2
  cat "$TMP" >&2
  echo >&2
  echo "  unstage offending files, or rerun with HIVE_SAFETY_ALLOW='<reason>' if intentional." >&2
  exit 1
fi
exit 0
