#!/usr/bin/env python3
"""
atlas_auto_promote.py — ENG-P1-1

atlas.n6 [7] 엔트리 자동 승격 파이프라인 v1.
근거 수집 → 후보 점수화 → 감사 로그 → 적용.

승격 규칙:
  [7] → [9]  : evidence_score >= 3 (domain verify + signal cross-ref + BT reference)
  [7] → [10] : evidence_score >= 5 (위 + 외부 재현 or 다중 독립 경로)
  [7] → [10*]: evidence_score >= 7 (위 + 논문 게재 or 3+ 독립 검증)

근거 소스 (각 1~2점):
  +2  domain verify.hexa 존재 + EXACT/PASS 결과
  +1  atlas.signals.n6 에 해당 도메인 신호
  +1  BT (breakthrough theorem) 참조
  +1  cross-domain 3+ 연결
  +1  논문 참조
  +1  실험 결과 (experiments/ 참조)

사용법:
  python3 scripts/atlas_auto_promote.py --dry-run     # 후보 리스트만 출력
  python3 scripts/atlas_auto_promote.py --apply        # 실제 승격 적용
  python3 scripts/atlas_auto_promote.py --report       # JSON 리포트 생성
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

# ── 경로 ──
NEXUS = Path(os.environ.get("NEXUS", Path.home() / "Dev" / "nexus"))
N6ARCH = Path(os.environ.get("N6ARCH", Path.home() / "Dev" / "n6-architecture"))

ATLAS = NEXUS / "shared" / "n6" / "atlas.n6"
SIGNALS = NEXUS / "shared" / "n6" / "atlas.signals.n6"
DOMAINS = N6ARCH / "domains"
EXPERIMENTS = N6ARCH / "experiments"
PAPERS_DIR = N6ARCH / "papers"
PRODUCTS = PAPERS_DIR / "_products.json"

AUDIT_LOG = N6ARCH / "reports" / "atlas_promote_audit.jsonl"

# ── 승격 임계값 ──
THRESHOLD_9 = 3
THRESHOLD_10 = 5
THRESHOLD_10STAR = 7


def parse_atlas_grade7(atlas_path: Path) -> list[dict]:
    """atlas.n6에서 [7] 등급 엔트리 파싱."""
    entries = []
    pattern = re.compile(r"^(@\S+)\s+(.+?)\s*=\s*(.+?)\s*::\s*(\S+)\s*\[7\]\s*$")
    with open(atlas_path, encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            m = pattern.match(line.rstrip())
            if m:
                entries.append({
                    "line": lineno,
                    "type": m.group(1),
                    "id": m.group(2).strip(),
                    "expr": m.group(3).strip(),
                    "domain": m.group(4).strip(),
                    "raw": line.rstrip(),
                })
    return entries


def check_domain_verify(domain: str) -> tuple[bool, int]:
    """도메인에 verify.hexa가 있고 EXACT/PASS가 있는지 체크. (exists, score)"""
    # 도메인 이름으로 디렉토리 탐색
    for sector in DOMAINS.iterdir():
        if not sector.is_dir() or sector.name.startswith("."):
            continue
        domain_dir = sector / domain
        if domain_dir.is_dir():
            hexa_files = list(domain_dir.glob("verify*.hexa")) + list(domain_dir.glob("*.hexa"))
            if hexa_files:
                # .hexa 파일 내 EXACT/PASS 검색
                for hf in hexa_files:
                    try:
                        content = hf.read_text(encoding="utf-8", errors="replace")
                        if "EXACT" in content or "PASS" in content:
                            return True, 2
                    except OSError:
                        pass
                return True, 1  # hexa 있지만 EXACT 없음
    return False, 0


def check_signals(domain: str) -> int:
    """atlas.signals.n6에 해당 도메인 신호가 있는지 체크."""
    if not SIGNALS.exists():
        return 0
    try:
        content = SIGNALS.read_text(encoding="utf-8", errors="replace")
        # 도메인 이름이 시그널에 등장하면 +1
        if domain in content:
            return 1
    except OSError:
        pass
    return 0


def check_bt_reference(entry_id: str, atlas_content: str) -> int:
    """BT 참조가 있는지 체크."""
    # BT- 로 시작하는 엔트리이거나, 다른 BT에서 참조되면 +1
    if entry_id.startswith("BT-") or entry_id.startswith("n6-bt-"):
        return 1
    # atlas에서 이 엔트리를 참조하는 라인 검색
    ref_pattern = re.compile(re.escape(entry_id))
    count = len(ref_pattern.findall(atlas_content))
    return 1 if count > 1 else 0  # 자기 자신 제외 1회 이상


def check_cross_domain(entry_id: str, atlas_content: str) -> int:
    """cross-domain 연결 3개 이상이면 +1."""
    # <- 또는 -> 라인에서 참조 카운트
    ref_count = atlas_content.count(entry_id)
    return 1 if ref_count >= 3 else 0


def check_paper_reference(domain: str) -> int:
    """논문에서 도메인 참조가 있는지 체크."""
    papers_json = PAPERS_DIR / "_papers.json"
    if papers_json.exists():
        try:
            data = json.loads(papers_json.read_text(encoding="utf-8"))
            for p in data if isinstance(data, list) else data.values():
                if isinstance(p, dict):
                    pdom = p.get("domain", "") or p.get("domains", "")
                    if domain in str(pdom):
                        return 1
        except (json.JSONDecodeError, OSError):
            pass
    # 파일명 검색
    for f in PAPERS_DIR.glob(f"*{domain}*"):
        if f.suffix in (".md", ".pdf"):
            return 1
    return 0


def check_experiment(domain: str) -> int:
    """experiments/에 해당 도메인 실험이 있는지."""
    for exp_dir in EXPERIMENTS.iterdir():
        if not exp_dir.is_dir():
            continue
        for f in exp_dir.iterdir():
            if domain in f.name:
                return 1
    return 0


def target_grade(score: int) -> str:
    """점수 → 타겟 등급."""
    if score >= THRESHOLD_10STAR:
        return "[10*]"
    if score >= THRESHOLD_10:
        return "[10]"
    if score >= THRESHOLD_9:
        return "[9]"
    return "[7]"  # 승격 안 함


def evaluate_candidates(entries: list[dict], atlas_content: str) -> list[dict]:
    """모든 [7] 엔트리에 대해 근거 점수 산출."""
    candidates = []
    for e in entries:
        domain = e["domain"]
        eid = e["id"]

        has_verify, verify_score = check_domain_verify(domain)
        signal_score = check_signals(domain)
        bt_score = check_bt_reference(eid, atlas_content)
        cross_score = check_cross_domain(eid, atlas_content)
        paper_score = check_paper_reference(domain)
        exp_score = check_experiment(domain)

        total = verify_score + signal_score + bt_score + cross_score + paper_score + exp_score
        tgt = target_grade(total)

        e["evidence"] = {
            "verify": verify_score,
            "signal": signal_score,
            "bt": bt_score,
            "cross_domain": cross_score,
            "paper": paper_score,
            "experiment": exp_score,
            "total": total,
        }
        e["current_grade"] = "[7]"
        e["target_grade"] = tgt
        e["promote"] = tgt != "[7]"
        candidates.append(e)

    # 점수 내림차순 정렬
    candidates.sort(key=lambda x: x["evidence"]["total"], reverse=True)
    return candidates


def apply_promotions(atlas_path: Path, candidates: list[dict]) -> int:
    """실제 atlas.n6에 승격 적용. 원자적 백업 + 치환."""
    promotes = [c for c in candidates if c["promote"]]
    if not promotes:
        return 0

    # 백업
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    backup = atlas_path.with_suffix(f".n6.bak.pre-promote-{ts}")
    shutil.copy2(atlas_path, backup)

    lines = atlas_path.read_text(encoding="utf-8").splitlines(keepends=True)

    applied = 0
    for c in promotes:
        lineno = c["line"] - 1  # 0-indexed
        if 0 <= lineno < len(lines):
            old_line = lines[lineno]
            new_line = old_line.replace("[7]", c["target_grade"])
            if new_line != old_line:
                lines[lineno] = new_line
                applied += 1

    atlas_path.write_text("".join(lines), encoding="utf-8")
    return applied


def write_audit_log(candidates: list[dict]) -> None:
    """감사 로그 JSONL 작성."""
    AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat()
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        for c in candidates:
            if c["promote"]:
                record = {
                    "timestamp": ts,
                    "id": c["id"],
                    "domain": c["domain"],
                    "line": c["line"],
                    "from": c["current_grade"],
                    "to": c["target_grade"],
                    "evidence": c["evidence"],
                    "type": c["type"],
                }
                f.write(json.dumps(record, ensure_ascii=False) + "\n")


def main():
    parser = argparse.ArgumentParser(description="atlas.n6 [7]→[9]/[10]/[10*] auto-promote")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true", help="후보만 출력, 변경 없음")
    group.add_argument("--apply", action="store_true", help="실제 승격 적용")
    group.add_argument("--report", action="store_true", help="JSON 리포트 생성")
    args = parser.parse_args()

    if not ATLAS.exists():
        print(f"error: atlas not found: {ATLAS}", file=sys.stderr)
        sys.exit(1)

    print(f"[scan] atlas: {ATLAS}")
    entries = parse_atlas_grade7(ATLAS)
    print(f"[scan] found {len(entries)} entries at [7]")

    atlas_content = ATLAS.read_text(encoding="utf-8", errors="replace")
    candidates = evaluate_candidates(entries, atlas_content)

    promotes = [c for c in candidates if c["promote"]]
    holds = [c for c in candidates if not c["promote"]]

    print(f"\n[result] promote: {len(promotes)}, hold: {len(holds)}")
    print()

    if promotes:
        print("=== PROMOTION CANDIDATES ===")
        for c in promotes:
            ev = c["evidence"]
            print(f"  {c['id']:<40} [7] → {c['target_grade']}  "
                  f"(score={ev['total']}  V={ev['verify']} S={ev['signal']} "
                  f"B={ev['bt']} X={ev['cross_domain']} P={ev['paper']} E={ev['experiment']})")

    if holds:
        print(f"\n=== HOLD (score < {THRESHOLD_9}) ===")
        for c in holds[:10]:
            ev = c["evidence"]
            print(f"  {c['id']:<40} [7] stay  "
                  f"(score={ev['total']}  V={ev['verify']} S={ev['signal']} "
                  f"B={ev['bt']} X={ev['cross_domain']} P={ev['paper']} E={ev['experiment']})")
        if len(holds) > 10:
            print(f"  ... +{len(holds) - 10} more")

    if args.apply and promotes:
        applied = apply_promotions(ATLAS, candidates)
        write_audit_log(candidates)
        print(f"\n[apply] {applied} entries promoted in atlas.n6")
        print(f"[audit] logged to {AUDIT_LOG}")

    if args.report:
        report = {
            "generated": datetime.now(timezone.utc).isoformat(),
            "atlas": str(ATLAS),
            "total_grade7": len(entries),
            "promote_count": len(promotes),
            "hold_count": len(holds),
            "thresholds": {
                "[9]": THRESHOLD_9,
                "[10]": THRESHOLD_10,
                "[10*]": THRESHOLD_10STAR,
            },
            "candidates": candidates,
        }
        report_path = N6ARCH / "reports" / "atlas_promote_report.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(
            json.dumps(report, ensure_ascii=False, indent=2, default=str),
            encoding="utf-8",
        )
        print(f"\n[report] written to {report_path}")


if __name__ == "__main__":
    main()
