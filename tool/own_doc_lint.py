#!/usr/bin/env python3
"""own_doc_lint.py — own#1..29 main lint dispatcher. LEGACY SHIM.

Migrated to tool/own_doc_lint.hexa (dispatcher) per raw 9 hexa-only mandate.
Per-rule logic remains in tool/own_doc_lint_legacy.py for now — hexa
dispatcher delegates to legacy for not-yet-ported rules. Migration follow-up
will land own<N>_lint.hexa per-rule modular ports over 30d.

Migration date: 2026-04-29
Canonical impl: tool/own_doc_lint.hexa
Legacy impl   : tool/own_doc_lint_legacy.py (per-rule check functions)
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    hexa_bin = shutil.which("hexa")
    if hexa_bin is None:
        print("[own_doc_lint shim] hexa binary not found in PATH")
        return 2
    hexa_path = repo_root / "tool" / "own_doc_lint.hexa"
    if not hexa_path.is_file():
        print(f"[own_doc_lint shim] missing canonical impl: {hexa_path}")
        return 2
    result = subprocess.run([hexa_bin, str(hexa_path)] + sys.argv[1:])
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
