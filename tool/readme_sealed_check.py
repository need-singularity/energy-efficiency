#!/usr/bin/env python3
"""readme_sealed_check.py — own#14 readme-sealed-required enforcement. LEGACY SHIM.

Migrated to tool/readme_sealed_check.hexa per raw 9 hexa-only mandate
(commit chain post 04f85f01). This shim preserves the existing CI invocation
path while delegating to the canonical hexa implementation.

Migration date: 2026-04-29
Canonical impl: tool/readme_sealed_check.hexa
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
        print("[sealed-check shim] hexa binary not found in PATH — fallback impossible")
        return 2
    hexa_path = repo_root / "tool" / "readme_sealed_check.hexa"
    if not hexa_path.is_file():
        print(f"[sealed-check shim] missing canonical impl: {hexa_path}")
        return 2
    result = subprocess.run([hexa_bin, str(hexa_path)] + sys.argv[1:])
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
