# n6-architecture remote-dispatch cwd mapping

**status**: landed 2026-04-24 (patch in sister repo `nexus/scripts/bin/hexa_remote`)
**convergence ref**: `~/core/nexus/convergence/drill_stability.convergence` @id `N6_ARCH_REMOTE_DISPATCH_CWD_MAPPING`

## Symptom

Running `nexus drill` (or any heavy-compute subcmd: smash / free / absolute / meta-closure / hyperarithmetic) from `~/core/n6-architecture` aborts with:

```
hexa resolver: ⚠ heavy-compute (...run.hexa drill) remote dispatch failed (exit 64) — Mac 로컬 실행 시 stage0 SIGKILL 위험
NEXUS_REMOTE_DOWNGRADE {"heavy_compute":true,"cmd":"drill","hosts_tried":[],"reason":"remote_unavailable","fallback":"abort"}
NEXUS_REMOTE_ERROR {"cmd":"drill","hosts_tried":[],"reason":"all_timeout","action":"abort_to_prevent_oom","exit_code":74}
```

`hosts_tried` is empty — the resolver aborted *before* probing any host.

## Root cause

`~/core/nexus/scripts/bin/hexa_remote` at L160-215 maps local cwd → remote path. Only three sister repos were originally wired:

- `$HOME/{Dev,dev}/airgenome` → `$HOME/airgenome`
- `$HOME/{Dev,dev,core}/nexus` → `$HOME/Dev/nexus`
- `$HOME/{Dev,dev}/anima` → `$HOME/anima`

Any other cwd falls through to `*) exit 64 ;;`. The outer wrapper (`scripts/bin/hexa`) then sees exit 64 + Darwin + heavy-compute + no `HEXA_ALLOW_LOCAL_FALLBACK` → emits the abort-74. The empty `hosts_tried` is a side-effect of the early exit (no probe ever ran).

## Fix

Append a case branch for `$HOME/core/n6-architecture`:

```bash
"$HOME_LC/core/n6-architecture"|"$HOME_LC/core/n6-architecture"/*)
    for candidate in "$HOME/core/n6-architecture"; do
        [ -d "$candidate" ] && LOCAL_ROOT="$candidate" && break
    done
    REMOTE_ROOT='$HOME/core/n6-architecture'
    SYNC_EXCLUDES=(
        --exclude=.git/
        --exclude='*.log'
        --exclude=.DS_Store
        --exclude=__pycache__/
        --exclude=.claude/
        --exclude=.growth/
        --exclude=reports/history/
        --exclude=build/
    )
    ;;
```

Insertion point: between the anima case (`;;` at L213) and the fallthrough (`*)` at L214).

## Recovery procedure if reverted

The file has `uchg` (BSD user-immutable) flag set, which blocks edits even by the owner. If the patch disappears:

```bash
# verify symptom
~/.hx/bin/nexus drill --seed 'canary' 2>&1 | head -3
# expect: NEXUS_REMOTE_ERROR with hosts_tried:[] and exit 74

# verify flag + file state
ls -lO ~/core/nexus/scripts/bin/hexa_remote
# expect: ...  uchg 14756 ...  (may vary)

grep -c 'core/n6-architecture' ~/core/nexus/scripts/bin/hexa_remote
# expect: 3  (if 0: patch gone, re-apply below)

# re-apply (the Python block is idempotent — refuses to double-patch)
chflags nouchg ~/core/nexus/scripts/bin/hexa_remote
python3 <<'PY'
p = "/Users/ghost/core/nexus/scripts/bin/hexa_remote"
txt = open(p).read()
if '"$HOME_LC/core/n6-architecture"' in txt:
    print("already_patched"); exit(0)
needle = '        --exclude=.claude/\n    )\n    ;;\n  *)\n    exit 64 ;;'
insertion = '''        --exclude=.claude/
    )
    ;;
  "$HOME_LC/core/n6-architecture"|"$HOME_LC/core/n6-architecture"/*)
    for candidate in "$HOME/core/n6-architecture"; do
        [ -d "$candidate" ] && LOCAL_ROOT="$candidate" && break
    done
    REMOTE_ROOT='$HOME/core/n6-architecture'
    SYNC_EXCLUDES=(
        --exclude=.git/
        --exclude='*.log'
        --exclude=.DS_Store
        --exclude=__pycache__/
        --exclude=.claude/
        --exclude=.growth/
        --exclude=reports/history/
        --exclude=build/
    )
    ;;
  *)
    exit 64 ;;'''
assert needle in txt, "needle missing — inspect file manually"
open(p, "w").write(txt.replace(needle, insertion, 1))
print("patched")
PY
chflags uchg ~/core/nexus/scripts/bin/hexa_remote

# verify
~/.hx/bin/nexus drill --seed 'post-patch canary' 2>&1 | head -3
# expect: "hexa_remote: ubu1 에서 원격 실행 중" (no NEXUS_REMOTE_ERROR)
```

## Related upstream gaps (not fixed here)

1. **preflight SSH-alias resolution** — `~/core/hexa-lang/gate/remote_preflight.hexa` probes via `/dev/tcp/$host/22`, which does `getaddrinfo()` and fails for SSH config aliases (documented at `nexus/convergence/drill_stability.convergence:408`). Bypass: `HEXA_REMOTE_SKIP_PREFLIGHT=1`. Real fix: resolve alias → IP via `ssh -G` before the TCP probe.
2. **UserPromptSubmit hook feedback loop** — `~/core/hexa-lang/gate/claude_prompt_hook.hexa` parses prompts for `drill`+imperative marker. If an agent response echoes a drill error, the hook re-fires drill on the next prompt. Real fix: exclude response-only matches, or decay the keyword weight after consecutive failures.

## Why uchg matters

The immutable flag prevents casual overwrites — e.g., if someone re-syncs `scripts/bin/` from an upstream mirror without review. It is *not* a security boundary (owner can `chflags nouchg`), but it ensures edits require deliberate intent.

Scanners that verify the patch should check `grep -c 'core/n6-architecture' ~/core/nexus/scripts/bin/hexa_remote` equals 3 and fail loudly if not.
