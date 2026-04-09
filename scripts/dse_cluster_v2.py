#!/usr/bin/env python3
"""DSE 교차공명 클러스터링 v2

입력: ~/Dev/nexus/shared/dse_cross/pair_scores.jsonl (1225쌍)
      ~/Dev/nexus/shared/dse_cross/formula_cross.jsonl (59 수식→도메인)
처리: 고공명 쌍(S>0.5)을 Union-Find로 연결 컴포넌트(융합 클러스터) 도출
      각 클러스터에 공통 n=6 수식(교집합/다수결) + 대표 도메인(degree 최대) +
      잠재 BT 후보(공통 수식 수 >= 3 또는 크기 >= 5) 식별
출력: docs/dse-cluster-v2.md (클러스터 표 + ASCII 그래프)
"""
from __future__ import annotations
import json
import os
from collections import defaultdict, Counter
from pathlib import Path

SHARED = Path.home() / "Dev/nexus/shared/dse_cross"
PAIRS = SHARED / "pair_scores.jsonl"
FORMULA = SHARED / "formula_cross.jsonl"
OUT = Path(__file__).resolve().parent.parent / "docs" / "dse-cluster-v2.md"

THRESHOLD = 0.5


def load_jsonl(p: Path):
    with p.open() as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


class UF:
    def __init__(self):
        self.p = {}
    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[ra] = rb


def main():
    pairs = [p for p in load_jsonl(PAIRS) if p["score"] > THRESHOLD]
    # formula→domains 역매핑: domain→formulas
    dom_formulas: dict[str, set[str]] = defaultdict(set)
    for row in load_jsonl(FORMULA):
        formula = row.get("formula") or row.get("pattern") or row.get("label")
        doms = row.get("domains", [])
        for d in doms:
            if formula:
                dom_formulas[d].add(formula)

    uf = UF()
    degree: Counter = Counter()
    edges_by_root: dict[str, list] = defaultdict(list)
    for p in pairs:
        a, b = p["a"], p["b"]
        uf.union(a, b)
        degree[a] += 1
        degree[b] += 1

    # 클러스터 집계
    clusters: dict[str, set[str]] = defaultdict(set)
    for p in pairs:
        r = uf.find(p["a"])
        clusters[r].add(p["a"])
        clusters[r].add(p["b"])
        edges_by_root[r].append(p)

    cluster_list = []
    for root, nodes in clusters.items():
        nodes_l = sorted(nodes)
        edges = edges_by_root[root]
        # 공통 수식 (다수결: 절반 이상 도메인에서 등장)
        fcount: Counter = Counter()
        for d in nodes_l:
            for f in dom_formulas.get(d, ()):
                fcount[f] += 1
        n = len(nodes_l)
        common = [f for f, c in fcount.most_common() if c >= max(2, n // 2)]
        top_formulas = fcount.most_common(5)
        # 대표 도메인: 클러스터 내 degree 최대
        rep = max(nodes_l, key=lambda d: degree[d])
        avg_score = sum(e["score"] for e in edges) / len(edges)
        max_score = max(e["score"] for e in edges)
        is_bt = (len(common) >= 3) or (n >= 5)
        cluster_list.append({
            "rep": rep,
            "size": n,
            "edges": len(edges),
            "avg": avg_score,
            "max": max_score,
            "nodes": nodes_l,
            "common": common,
            "top_formulas": top_formulas,
            "bt": is_bt,
        })

    cluster_list.sort(key=lambda c: (-c["size"], -c["avg"]))

    n_clusters = len(cluster_list)
    max_size = max(c["size"] for c in cluster_list) if cluster_list else 0
    bt_count = sum(1 for c in cluster_list if c["bt"])

    # 마크다운 작성
    lines = []
    lines.append("# DSE 교차공명 융합 클러스터 v2")
    lines.append("")
    lines.append(f"> 생성: `scripts/dse_cluster_v2.py` | 입력: `pair_scores.jsonl` (1225쌍)")
    lines.append(f"> 임계: S > {THRESHOLD} | 알고리즘: Union-Find 연결 컴포넌트")
    lines.append("")
    lines.append("## 1. 요약")
    lines.append("")
    lines.append(f"- 입력 쌍: **1225** (전체 도메인 쌍)")
    lines.append(f"- 고공명 쌍 (S>{THRESHOLD}): **{len(pairs)}**")
    lines.append(f"- 융합 클러스터 수: **{n_clusters}**")
    lines.append(f"- 최대 컴포넌트 크기: **{max_size}** 도메인")
    lines.append(f"- 잠재 BT 후보 클러스터: **{bt_count}**")
    lines.append("")
    lines.append("## 2. 클러스터 표")
    lines.append("")
    lines.append("| # | 대표 도메인 | 크기 | 엣지 | 평균S | 최대S | 공통 n=6 수식 | BT후보 |")
    lines.append("|--:|------------|----:|----:|------:|------:|--------------|:----:|")
    for i, c in enumerate(cluster_list, 1):
        common_s = ", ".join(c["common"][:4]) if c["common"] else "(주요: " + ", ".join(f for f, _ in c["top_formulas"][:2]) + ")"
        lines.append(f"| {i} | `{c['rep']}` | {c['size']} | {c['edges']} | {c['avg']:.3f} | {c['max']:.3f} | {common_s} | {'★' if c['bt'] else '·'} |")
    lines.append("")
    lines.append("## 3. 클러스터 상세 (Top 10)")
    lines.append("")
    for i, c in enumerate(cluster_list[:10], 1):
        lines.append(f"### 클러스터 {i} — `{c['rep']}` (크기 {c['size']})")
        lines.append("")
        lines.append(f"- 도메인: {', '.join('`'+d+'`' for d in c['nodes'])}")
        tf = ", ".join(f"{f}({n})" for f, n in c["top_formulas"])
        lines.append(f"- 상위 수식 빈도: {tf if tf else '(수식 매핑 없음)'}")
        if c["common"]:
            lines.append(f"- 공통 수식(다수결): {', '.join(c['common'])}")
        lines.append(f"- 평균/최대 공명: {c['avg']:.3f} / {c['max']:.3f}")
        lines.append(f"- BT 후보: {'★ YES' if c['bt'] else '아니오'}")
        lines.append("")

    # ASCII 그래프: 클러스터 크기 막대
    lines.append("## 4. ASCII 그래프 — 클러스터 크기 분포")
    lines.append("")
    lines.append("```")
    lines.append("클러스터    대표도메인                 크기")
    max_bar = max_size if max_size else 1
    for i, c in enumerate(cluster_list, 1):
        bar_len = int(round(c["size"] * 40 / max_bar))
        bar = "█" * max(1, bar_len)
        rep = (c["rep"][:24]).ljust(24)
        mark = " ★" if c["bt"] else "  "
        lines.append(f"C{i:02d}  {rep} {bar} {c['size']}{mark}")
    lines.append("```")
    lines.append("")

    # 간이 연결 구조 (Top 클러스터별 엣지 10개)
    lines.append("## 5. ASCII 연결 구조 (Top 3 클러스터 핵심 엣지)")
    lines.append("")
    lines.append("```")
    for i, c in enumerate(cluster_list[:3], 1):
        lines.append(f"[C{i:02d}] {c['rep']}  (n={c['size']})")
        top_edges = sorted(edges_by_root[uf.find(c['rep'])], key=lambda e: -e["score"])[:8]
        for e in top_edges:
            lines.append(f"   {e['a']:<32} ──{e['score']:.2f}── {e['b']}")
        lines.append("")
    lines.append("```")
    lines.append("")
    lines.append("## 6. 결론")
    lines.append("")
    lines.append(f"- **{n_clusters}개** 융합 클러스터 도출, 최대 **{max_size}** 도메인 컴포넌트")
    lines.append(f"- **{bt_count}개** 잠재 BT 후보 (공통 수식 ≥3 또는 크기 ≥5)")
    lines.append("- 각 BT 후보는 동일 n=6 수식을 다수 도메인이 공유 → 교차 BT 승격 검토 대상")
    lines.append("")

    OUT.write_text("\n".join(lines))
    print(f"clusters={n_clusters} max_size={max_size} bt_candidates={bt_count}")
    print(f"wrote: {OUT}")


if __name__ == "__main__":
    main()
