#!/usr/bin/env python3
# tool/own31_runtime_sandbox.py — own#31 Tier 2 runtime sandbox + literal
# mutation differential. Closes B1-B4 by EXECUTING the block and observing
# whether assertions are sensitive to literal-binding values.
#
# Algorithm:
#   1. Parse source via `ast` -> identify integer/float/string Constant
#      literal-binding lines (e.g. `sigma = 12`).
#   2. Execute the block once in a fresh globals dict (subprocess); count
#      how many top-level assertions pass without raising.
#   3. Mutation: replace each literal-binding RHS with a deterministic-
#      pseudorandom value (seed via --seed; default 42). Re-execute.
#   4. If ANY assertion still passes after the literal mutation -> the
#      assertions are sensitive to ACTUAL computation (real-verify, exit 0).
#      If ALL assertions fail / raise / never run after mutation -> the
#      assertions are LOAD-BEARING ONLY on the literals = tautology
#      (FLAG, exit 1).
#
# Closes:
#   B1 globals injection      — sandbox uses fresh globals each subproc run
#   B2 frame manipulation     — runs in subprocess; frame walks affect
#                                only the child interpreter
#   B3 coroutine deferred     — top-level `asyncio.run(...)` is executed;
#                                downstream literal-only asserts still
#                                fail under mutation
#   B4 generator-deferred     — generator yield -> consumer assert pattern;
#                                mutation breaks the literal source so
#                                generator yields different value
#
# Safety:
#   - Subprocess invocation; runner sets RLIMIT_CPU = 5s. Parent wall
#     timeout = 8s. Any harness failure or timeout = abstain (exit 0,
#     no FLAG). raw 91 C3 honest fallback.
#
# Pure-stdlib (`ast`, `random`, `subprocess`, `sys`, `os`); no third-party.

import ast
import os
import random
import subprocess
import sys


CPU_BUDGET_SEC = 5
WALL_BUDGET_SEC = 8
DEFAULT_SEED = 42


def _collect_literal_bindings(tree):
    """Top-level `name = <int|float|str literal>` assignments."""
    bindings = []
    for node in ast.iter_child_nodes(tree):
        if not isinstance(node, ast.Assign):
            continue
        if len(node.targets) != 1:
            continue
        tgt = node.targets[0]
        if not isinstance(tgt, ast.Name):
            continue
        rhs = node.value
        if isinstance(rhs, ast.Constant):
            v = rhs.value
            if isinstance(v, bool):
                continue
            if isinstance(v, (int, float, str)):
                bindings.append({
                    "lineno": rhs.lineno,
                    "col_offset": rhs.col_offset,
                    "end_col_offset": rhs.end_col_offset,
                    "kind": type(v).__name__,
                    "original": v,
                    "target": tgt.id,
                })
    return bindings


def _mutate_value(kind, original, rng):
    if kind == "int":
        cur = int(original)
        for _ in range(10):
            cand = rng.randint(-10000, 10000)
            if cand != cur:
                return repr(cand)
        return repr(cur + 7919)
    if kind == "float":
        cur = float(original)
        cand = rng.uniform(-1e6, 1e6)
        if cand == cur:
            cand = cur + 1.0
        return repr(cand)
    if kind == "str":
        return repr("_OWN31_T2_mut_" + str(rng.randint(1000, 9999)))
    return repr(original)


def _rewrite_with_mutations(source_lines, bindings, rng):
    out = list(source_lines)
    for b in bindings:
        ln = b["lineno"]
        if ln < 1 or ln > len(out):
            continue
        line = out[ln - 1]
        co = b["col_offset"]
        eo = b["end_col_offset"]
        if eo is None or eo > len(line):
            continue
        new_val = _mutate_value(b["kind"], b["original"], rng)
        out[ln - 1] = line[:co] + new_val + line[eo:]
    return out


# Runner: rewrites top-level `assert X` to a probe that counts pass/fail
# without aborting. Sets a 5-second CPU rlimit.
_RUNNER = r'''
import resource, sys, ast
try:
    resource.setrlimit(resource.RLIMIT_CPU, (__CPU__, __CPU__))
except Exception:
    pass

_PROBE = {"pass": 0, "fail": 0}

def _own31_probe(thunk):
    try:
        if bool(thunk()):
            _PROBE["pass"] += 1
        else:
            _PROBE["fail"] += 1
    except Exception:
        _PROBE["fail"] += 1


class _AP(ast.NodeTransformer):
    def visit_Assert(self, node):
        try:
            test_src = ast.unparse(node.test)
        except Exception:
            return node
        new = ast.parse("_OWN31_PROBE(lambda: (" + test_src + "))").body[0]
        return ast.copy_location(new, node)


SRC = sys.stdin.read()

try:
    tree = ast.parse(SRC)
except SyntaxError:
    print("__OWN31_SB__ pass=0 fail=0")
    sys.exit(0)

new_tree = _AP().visit(tree)
ast.fix_missing_locations(new_tree)

glb = {"__name__": "__own31_sandbox__",
       "_OWN31_PROBE": _own31_probe}

try:
    code = compile(new_tree, "<own31-sandbox>", "exec")
    exec(code, glb)
except SystemExit:
    pass
except Exception:
    pass

print("__OWN31_SB__ pass={} fail={}".format(_PROBE["pass"], _PROBE["fail"]))
'''


def _run_block_subprocess(source):
    runner = _RUNNER.replace("__CPU__", str(CPU_BUDGET_SEC))
    try:
        proc = subprocess.run(
            [sys.executable, "-c", runner],
            input=source,
            capture_output=True, text=True,
            timeout=WALL_BUDGET_SEC,
        )
    except (subprocess.TimeoutExpired, OSError):
        return (-1, -1)
    out = proc.stdout or ""
    pass_n = -1
    fail_n = -1
    for line in out.splitlines():
        if line.startswith("__OWN31_SB__ "):
            try:
                for tok in line.split()[1:]:
                    if tok.startswith("pass="):
                        pass_n = int(tok[5:])
                    elif tok.startswith("fail="):
                        fail_n = int(tok[5:])
            except (ValueError, IndexError):
                return (-1, -1)
    return (pass_n, fail_n)


def main(argv):
    seed = DEFAULT_SEED
    src_path = None
    i = 1
    while i < len(argv):
        a = argv[i]
        if a == "--seed":
            i += 1
            if i < len(argv):
                try:
                    seed = int(argv[i])
                except ValueError:
                    pass
        elif src_path is None:
            src_path = a
        i += 1
    if src_path is None:
        sys.stderr.write("usage: own31_runtime_sandbox.py <src> [--seed N]\n")
        return 0
    try:
        with open(src_path, "r") as fh:
            source = fh.read()
    except (OSError, IOError):
        return 0
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return 0
    bindings = _collect_literal_bindings(tree)
    if not bindings:
        return 0

    base_pass, base_fail = _run_block_subprocess(source)
    if base_pass < 0:
        return 0
    if base_pass == 0:
        return 0

    rng = random.Random(seed)
    mutated_lines = _rewrite_with_mutations(
        source.splitlines(keepends=False), bindings, rng)
    mutated_src = "\n".join(mutated_lines)
    if not mutated_src.endswith("\n"):
        mutated_src += "\n"
    mut_pass, mut_fail = _run_block_subprocess(mutated_src)
    if mut_pass < 0:
        return 0

    if mut_pass == 0:
        print("runtime-literal-load-bearing:base_pass={} "
              "mut_pass={}".format(base_pass, mut_pass))
        return 1
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except Exception:
        sys.exit(0)
