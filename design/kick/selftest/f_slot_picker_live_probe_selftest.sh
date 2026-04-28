#!/usr/bin/env bash
# F-SLOT-PICKER-LIVE-PROBE selftest (2026-04-28)
#
# Exercises the live-API health gate added to
# /Users/ghost/core/hive/tool/claude_slot_pick.hexa.  Uses
# CLAUDE_SLOT_TEST_HOME to redirect slot discovery to an isolated tempdir
# and CLAUDE_SLOT_PICK_PROBE_CMD to inject a deterministic mock probe so
# we can simulate revoked OAuth (401) without touching real Anthropic.
#
# Cases:
#   C1  all-3-revoked-401            → expect picker exit 76, reason
#                                       all-slots-unhealthy-live-probe
#   C2  one-healthy-two-revoked      → expect picker exit 0, picked = healthy
#   C3  cache-hit-skips-fresh-probe  → second pick under same cache
#                                       must NOT re-spawn probe
#   C4  invalidate-cache-rerun       → after --invalidate-cache,
#                                       fresh probe runs again
#
# Sentinel pattern asserted on stderr per case.

set -euo pipefail

HEXA="${HEXA:-/Users/ghost/core/hexa-lang/hexa}"
TOOL="/Users/ghost/core/hive/tool/claude_slot_pick.hexa"
TMP="$(mktemp -d /tmp/f-splp-selftest.XXXXXX)"
trap 'rm -rf "$TMP" /tmp/claude_slot_health' EXIT

mkdir -p "$TMP/.claude-claude1" "$TMP/.claude-claude2" "$TMP/.claude-claude3"
# minimal .claude.json with valid oauthAccount.emailAddress so the static
# pre-gate (probe_one_slot) accepts the slot; the live-API mock decides
# the actual verdict.
for n in 1 2 3; do
  printf '{"oauthAccount":{"emailAddress":"test%s@example.com"}}\n' "$n" \
    > "$TMP/.claude-claude$n/.claude.json"
done

# Mock probe: behavior keyed on slot suffix in CLAUDE_CONFIG_DIR.
# C1 round: all 3 → 401.   C2 round: claude2 → healthy, others 401.
mk_mock_all_401() {
  cat > "$TMP/mock_probe.sh" <<'EOF'
#!/usr/bin/env bash
echo "{\"type\":\"error\",\"error\":{\"type\":\"authentication_error\",\"message\":\"OAuth token has been revoked. Please run /login\"}}" >&2
echo "API Error: 401" >&2
exit 1
EOF
  chmod +x "$TMP/mock_probe.sh"
}

mk_mock_healthy_for_2() {
  cat > "$TMP/mock_probe.sh" <<EOF
#!/usr/bin/env bash
case "\${CLAUDE_CONFIG_DIR:-}" in
  *.claude-claude2) echo "pong"; exit 0 ;;
  *) echo "API Error: 401 authentication_error" >&2; exit 1 ;;
esac
EOF
  chmod +x "$TMP/mock_probe.sh"
}

run_picker() {
  rm -f "$TMP/last_rc" "$TMP/last_stderr" "$TMP/last_stdout"
  set +e
  CLAUDE_SLOT_TEST_HOME="$TMP" \
  CLAUDE_SLOT_PICK_PROBE_CMD="CLAUDE_CONFIG_DIR={CONFIG_DIR} $TMP/mock_probe.sh 2>&1" \
  CLAUDE_SLOT_PICK_PROBE_TIMEOUT=3 \
  "$HEXA" run "$TOOL" --pick "$@" 2> "$TMP/last_stderr" > "$TMP/last_stdout"
  echo "__rc__=$?" > "$TMP/last_rc"
  set -e
}

assert_contains() {
  local file="$1" needle="$2" label="$3"
  if grep -F -- "$needle" "$file" > /dev/null; then
    printf 'PASS  %s\n' "$label"
  else
    printf 'FAIL  %s\n  expected: %s\n  in: %s\n' "$label" "$needle" "$file"
    cat "$file"
    exit 2
  fi
}

assert_not_contains() {
  local file="$1" needle="$2" label="$3"
  if grep -F -- "$needle" "$file" > /dev/null; then
    printf 'FAIL  %s\n  unexpected: %s\n' "$label" "$needle"
    cat "$file"
    exit 2
  fi
  printf 'PASS  %s\n' "$label"
}

# ---------- C1: all 3 revoked → exit 76, all-unhealthy ----------
rm -rf /tmp/claude_slot_health 2>/dev/null || true
mk_mock_all_401
run_picker
assert_contains "$TMP/last_rc"     "__rc__=76"                                "C1.exit-code"
assert_contains "$TMP/last_stderr" "all-slots-unhealthy-live-probe"           "C1.sentinel-trailer"
assert_contains "$TMP/last_stderr" "verdict=unhealthy"                        "C1.live-probe-emitted"
assert_contains "$TMP/last_stderr" "reason=auth-401"                          "C1.401-classification"

# ---------- C2: one healthy → exit 0, pick claude2 ----------
rm -rf /tmp/claude_slot_health 2>/dev/null || true
mk_mock_healthy_for_2
run_picker
assert_contains "$TMP/last_rc"     "__rc__=0"                                 "C2.exit-code"
assert_contains "$TMP/last_stdout" "$TMP/.claude-claude2"                     "C2.picked-config-dir"
assert_contains "$TMP/last_stderr" "PASS slot=2 reason=lru-available-live-gated" "C2.pass-sentinel"

# ---------- C3: cache hit on second pick (no fresh-probe spawn) ----------
# Same mock + same cache → second call must read cache, source=cache.
run_picker
assert_contains "$TMP/last_rc"     "__rc__=0"                                 "C3.exit-code"
assert_contains "$TMP/last_stderr" "verdict=healthy source=cache"             "C3.cache-hit"

# ---------- C4: --invalidate-cache then re-pick = fresh probe again ----------
CLAUDE_SLOT_TEST_HOME="$TMP" "$HEXA" run "$TOOL" --invalidate-cache 2> "$TMP/inv_stderr" \
  || { echo "FAIL  C4.invalidate-call"; cat "$TMP/inv_stderr"; exit 2; }
assert_contains "$TMP/inv_stderr" "live-probe-cache-invalidated"              "C4.invalidate-sentinel"
run_picker
assert_contains "$TMP/last_stderr" "source=fresh"                             "C4.refresh-after-invalidate"
assert_not_contains "$TMP/last_stderr" "verdict=healthy source=cache"         "C4.no-stale-cache"

printf '\n__SLOT_PICK_LIVE_PROBE_SELFTEST__ PASS cases=4\n'
