#!/usr/bin/env python3
"""proposal_lint.py — own#22 + own#23 proposals/*.md HARD lint. LEGACY SHIM.

Migrated to tool/proposal_lint.hexa per raw 9 hexa-only mandate.
This shim preserves CI invocation while delegating to canonical hexa impl.

Migration date: 2026-04-29
Canonical impl: tool/proposal_lint.hexa
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
        print("[proposal_lint shim] hexa binary not found in PATH")
        return 2
    hexa_path = repo_root / "tool" / "proposal_lint.hexa"
    if not hexa_path.is_file():
        print(f"[proposal_lint shim] missing canonical impl: {hexa_path}")
        return 2
    result = subprocess.run([hexa_bin, str(hexa_path)] + sys.argv[1:])
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
