#!/bin/bash
# check_remote_dispatch.sh — verify n6-architecture remote dispatch is wired.
# Recurrence guard for the 2026-04-24 hexa_remote cwd-mapping fix.
# See docs/operations/remote-dispatch-cwd-mapping.md.
#
# Exit codes:
#   0 — patch present, expected to work
#   1 — patch missing, drill will abort-74 until re-applied
#   2 — sister nexus repo not found at expected path
set -u

TARGET="$HOME/core/nexus/scripts/bin/hexa_remote"

if [ ! -f "$TARGET" ]; then
  echo "[check_remote_dispatch] MISSING: $TARGET (nexus sister repo not at expected path)" >&2
  exit 2
fi

hits="$(grep -c 'core/n6-architecture' "$TARGET" 2>/dev/null)"

if [ "${hits:-0}" -lt 3 ]; then
  echo "[check_remote_dispatch] FAIL: hexa_remote has only $hits/3 n6-architecture references — patch missing or partial" >&2
  echo "[check_remote_dispatch] remediation: docs/operations/remote-dispatch-cwd-mapping.md §'Recovery procedure'" >&2
  exit 1
fi

# Also verify uchg flag is set (immutability safeguard).
flags="$(stat -f '%Sf' "$TARGET" 2>/dev/null)"
case "$flags" in
  *uchg*) uchg_status="set" ;;
  *)      uchg_status="MISSING (recommend: chflags uchg $TARGET)" ;;
esac

echo "[check_remote_dispatch] OK: patch=3/3 refs, uchg=$uchg_status"
exit 0
