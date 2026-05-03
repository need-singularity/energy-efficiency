#!/usr/bin/env python3
# tool/own31_ast_visitor.py — own#31 Tier 2 AST visitor (host-python3 standalone)
#
# Closes A1-A5 adversarial gaps that hexa-pure substring detection cannot
# express:
#
#   A1  compile(<str-literal-with-cmp>, ...) followed by exec/eval of result
#   A2  getattr(<scope>, <split-string-concatenation>)(...) where the
#       reconstructed name is in {eval, exec, compile}
#   A3  __import__(<concat-string>) where reconstructed string is in
#       {os, sys, ctypes, importlib, builtins, subprocess}
#   A4  decorator chain with mutating decorator name in
#       {cache, memoize, transform, alias, override, force, fake, mock}
#   A5  __annotations__[<key>] = <int-literal> followed by
#       assert <key> == <same-int>  — runtime annotation hijack
#
# CLI:
#   python3 tool/own31_ast_visitor.py <block-source-file>
#
# Output: one reason per line of form `<reason-id>:line=<n>` or
#         `<reason-id>:<context>`. Exit 0 if any reason found, exit 1 if no
#         reason (clean). raw 91 C3 honest disclosure: this convention is
#         INVERTED from typical CLI norms because the hexa lint dispatcher
#         treats stdout content as the FLAG signal (presence == FLAG).
#
# Pure-stdlib (`ast`, `sys`); no third-party deps.

import ast
import sys


_CONCAT_TARGET_NAMES = {"eval", "exec", "compile"}
_DANGEROUS_IMPORTS = {
    "os", "sys", "ctypes", "importlib", "builtins", "subprocess",
}
_MUTATING_DECO_NAMES = {
    "cache", "memoize", "transform", "alias",
    "override", "force", "fake", "mock",
}

_MATH_LIB_IMPORTS = frozenset({
    "sympy", "fractions", "math.gcd", "math.lcm", "math.factorial",
    "math.comb", "math.perm", "numbers", "decimal", "statistics",
})

_PHYSICS_LIB_IMPORTS = frozenset({
    "scipy.constants", "astropy.units", "astropy.constants",
    "pint", "uncertainties", "cgs", "siconv",
})

_PHYSICS_CONSTANTS_NUMERIC = frozenset({
    1.602176634e-19,  # elementary charge e
    6.02214076e23,    # Avogadro
    2.99792458e8,     # speed of light c
    1.380649e-23,     # Boltzmann k
    6.62607015e-34,   # Planck h
    9.81,             # g earth surface
    8.314,            # R gas constant
    9.109e-31,        # electron mass
    1.673e-27,        # proton mass
})


def _flatten_str_concat(node):
    """Reconstruct a string from BinOp(Add) of string Constants."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.JoinedStr):
        parts = []
        for v in node.values:
            if isinstance(v, ast.Constant) and isinstance(v.value, str):
                parts.append(v.value)
            else:
                return None
        return "".join(parts)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = _flatten_str_concat(node.left)
        right = _flatten_str_concat(node.right)
        if left is None or right is None:
            return None
        return left + right
    return None


def _has_cmp_op(s):
    return any(op in s for op in ("==", "!=", "<=", ">=", "<", ">"))


def visit(tree):
    found = []

    ann_int_bindings = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if (isinstance(tgt, ast.Subscript)
                        and isinstance(tgt.value, ast.Name)
                        and tgt.value.id == "__annotations__"):
                    key = None
                    sl = tgt.slice
                    if isinstance(sl, ast.Constant) and isinstance(
                            sl.value, str):
                        key = sl.value
                    if (isinstance(node.value, ast.Constant)
                            and isinstance(node.value.value, int)
                            and not isinstance(node.value.value, bool)
                            and key is not None):
                        ann_int_bindings[key] = (
                            node.value.value, getattr(node, "lineno", 0))

    compile_var_lines = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            v = node.value
            if (isinstance(v, ast.Call)
                    and isinstance(v.func, ast.Name)
                    and v.func.id == "compile"
                    and v.args):
                lit = _flatten_str_concat(v.args[0])
                if isinstance(lit, str) and _has_cmp_op(lit):
                    for tgt in node.targets:
                        if isinstance(tgt, ast.Name):
                            compile_var_lines[tgt.id] = getattr(
                                node, "lineno", 0)

    for node in ast.walk(tree):
        # A1: compile() feeding exec/eval
        if (isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id in ("exec", "eval")
                and node.args):
            arg0 = node.args[0]
            if (isinstance(arg0, ast.Call)
                    and isinstance(arg0.func, ast.Name)
                    and arg0.func.id == "compile"
                    and arg0.args):
                lit = _flatten_str_concat(arg0.args[0])
                if isinstance(lit, str) and _has_cmp_op(lit):
                    found.append("compile-deferred-cmp:line={}".format(
                        getattr(node, "lineno", 0)))
            if isinstance(arg0, ast.Name) and arg0.id in compile_var_lines:
                found.append("compile-deferred-cmp:line={}".format(
                    getattr(node, "lineno", 0)))

        # A2: getattr split-string -> eval/exec/compile
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Call):
            inner = node.func
            if (isinstance(inner.func, ast.Name)
                    and inner.func.id == "getattr"
                    and len(inner.args) >= 2):
                name_lit = _flatten_str_concat(inner.args[1])
                if name_lit in _CONCAT_TARGET_NAMES:
                    found.append("getattr-split-string:{}={}".format(
                        getattr(node, "lineno", 0), name_lit))

        # A3: __import__ concat
        if (isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id == "__import__"
                and node.args):
            mod_lit = _flatten_str_concat(node.args[0])
            if isinstance(mod_lit, str) and mod_lit in _DANGEROUS_IMPORTS:
                if isinstance(node.args[0], ast.BinOp):
                    found.append("dunder-import-concat:{}={}".format(
                        getattr(node, "lineno", 0), mod_lit))

        # A4: decorator chain w/ mutating deco
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef,
                             ast.ClassDef)):
            decos = getattr(node, "decorator_list", []) or []
            if decos:
                hits = []
                for d in decos:
                    name = None
                    if isinstance(d, ast.Name):
                        name = d.id
                    elif isinstance(d, ast.Attribute):
                        name = d.attr
                    elif isinstance(d, ast.Call):
                        if isinstance(d.func, ast.Name):
                            name = d.func.id
                        elif isinstance(d.func, ast.Attribute):
                            name = d.func.attr
                    if name and name.lower() in _MUTATING_DECO_NAMES:
                        hits.append(name)
                if hits:
                    found.append("decorator-mutation:{}={}".format(
                        getattr(node, "lineno", 0), ",".join(hits)))

        # A5: __annotations__[k] = <int> + assert k == <same>
        if (isinstance(node, ast.Assert)
                and isinstance(node.test, ast.Compare)
                and len(node.test.ops) == 1
                and isinstance(node.test.ops[0], ast.Eq)
                and len(node.test.comparators) == 1):
            left = node.test.left
            right = node.test.comparators[0]
            key = None
            if isinstance(left, ast.Name):
                key = left.id
            if (key in ann_int_bindings
                    and isinstance(right, ast.Constant)
                    and isinstance(right.value, int)
                    and not isinstance(right.value, bool)
                    and right.value == ann_int_bindings[key][0]):
                found.append("annotation-hijack:{}={}={}".format(
                    getattr(node, "lineno", 0), key, right.value))

    return found


def detect_math_physics(tree):
    """Walk AST; classify block as math/physics/both/neither via imports + constants."""
    math_imports_found = []
    physics_imports_found = []
    physics_constants_found = []
    scientific_notation_count = 0

    def _check_name(name):
        if not isinstance(name, str):
            return
        if name in _MATH_LIB_IMPORTS and name not in math_imports_found:
            math_imports_found.append(name)
        if name in _PHYSICS_LIB_IMPORTS and name not in physics_imports_found:
            physics_imports_found.append(name)

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                _check_name(alias.name)
                # also check top-level package fragment (e.g. "scipy" of
                # "scipy.constants") for completeness — only if exact match
                # in either set
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            _check_name(mod)
            for alias in node.names:
                if mod:
                    _check_name(mod + "." + alias.name)
                else:
                    _check_name(alias.name)
        elif isinstance(node, ast.Constant):
            v = node.value
            if isinstance(v, bool):
                continue
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                fv = float(v)
                for const in _PHYSICS_CONSTANTS_NUMERIC:
                    if abs(fv - const) < 1e-6 * abs(const) and \
                            const not in physics_constants_found:
                        physics_constants_found.append(const)
                        break
                rep = repr(v)
                i = 0
                while i < len(rep):
                    ch = rep[i]
                    if ch == "e" or ch == "E":
                        if i + 1 < len(rep):
                            nxt = rep[i + 1]
                            if nxt.isdigit() or (
                                    nxt in ("+", "-")
                                    and i + 2 < len(rep)
                                    and rep[i + 2].isdigit()):
                                scientific_notation_count += 1
                                break
                    i += 1

    math = bool(math_imports_found)
    physics = (bool(physics_imports_found)
               or bool(physics_constants_found)
               or scientific_notation_count >= 1)
    if math and physics:
        classification = "both"
    elif math:
        classification = "math"
    elif physics:
        classification = "physics"
    else:
        classification = "neither"

    return {
        "math_imports_found": math_imports_found,
        "physics_imports_found": physics_imports_found,
        "physics_constants_found": physics_constants_found,
        "scientific_notation_count": scientific_notation_count,
        "classification": classification,
    }


def main(argv):
    if len(argv) < 2:
        sys.stderr.write("usage: own31_ast_visitor.py <source-file>\n")
        return 1
    try:
        with open(argv[1], "r") as fh:
            src = fh.read()
    except (OSError, IOError) as e:
        sys.stderr.write("read-error: {}\n".format(e))
        return 1
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return 1
    found = visit(tree)
    if found:
        for line in found:
            print(line)
        return 0
    return 1


def _classify_stdin():
    """own#6 Tier-2 fallback CLI mode.

    Read python block source from stdin, parse via ast, run
    detect_math_physics(tree), emit one-line classification marker plus
    a JSON details line. Always exits 0 (informational; gating happens
    in caller — own6_math_physics_classifier.hexa).

    Output (stdout, two lines):
      OWN6_AST_CLASSIFY: <math|physics|both|neither>
      details: {"math_imports_found": [...], "physics_imports_found": [...], ...}

    raw 91 honest caveat: parse failures emit `neither` so caller's
    Tier-1 result wins; this mirrors own#34 Tier-2 deployment status
    (informational adjunct, not authoritative).
    """
    import json
    src = sys.stdin.read()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        sys.stdout.write("OWN6_AST_CLASSIFY: neither\n")
        sys.stdout.write('details: {"error": "syntax-error"}\n')
        return 0
    info = detect_math_physics(tree)
    sys.stdout.write("OWN6_AST_CLASSIFY: {}\n".format(info["classification"]))
    try:
        sys.stdout.write("details: {}\n".format(json.dumps(info)))
    except (TypeError, ValueError):
        sys.stdout.write('details: {"error": "json-encode-failure"}\n')
    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "--classify-stdin":
        sys.exit(_classify_stdin())
    sys.exit(main(sys.argv))
