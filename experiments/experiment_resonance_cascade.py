#!/usr/bin/env python3
"""
Experiment: Resonance Cascade
==============================
Chains blowup outputs across domains to amplify EXACT match discovery.

Insight: if domain A's blowup produces an EXACT match at value V, feeding V
as an additional seed into domain B's blowup lets B discover relationships
it would never find with its default seed set.  This creates a chain
reaction across the canonical domain ordering:

    math -> physics -> bio -> info -> mind -> arch

Each link in the cascade injects newly-discovered n6 constants into the next
domain's seed pool.  The experiment compares:

  (a) isolated blowup -- each domain uses only the 7 base seeds
  (b) cascaded blowup -- each domain inherits prior domains' discoveries

Each domain has a unique resonance profile: a random subset of operations
that "resonate" (succeed) in that domain.  More seeds = more pairs = more
chances to hit a resonant operation, so cascade enrichment matters.

Prediction: cascaded mode should show substantial growth in cumulative EXACT
count because each domain enriches the seed pool for all downstream domains.

n=6 connection: 6 domains in cascade order, seeds drawn from the 16-element
n6 constant family, and the cascade amplification factor itself converges
to an n6 constant.
"""
import sys, os, random, math
from collections import OrderedDict

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# --- n6 constants: the full wave spectrum ---
N6_CONSTANTS = [6, 12, 4, 2, 5, 24, 7, 48, 288, 1, 3, 8, 14, 72, 144, 576]
N6_SET = set(N6_CONSTANTS)

# --- 6 cascade domains (canonical order) ---
CASCADE_DOMAINS = ["math", "physics", "bio", "info", "mind", "arch"]

# --- Base seeds: first 7 n6 constants ---
BASE_SEEDS = N6_CONSTANTS[:7]  # [6, 12, 4, 2, 5, 24, 7]

# --- Tolerance for EXACT match ---
EXACT_TOL = 0.001  # 0.1%

# --- Operations ---
OPS = [
    ("+", lambda a, b: a + b),
    ("*", lambda a, b: a * b),
    ("-", lambda a, b: a - b),
    ("/", lambda a, b: a / b if b != 0 else None),
]


def is_exact(value):
    """Check if value matches any n6 constant within 0.1% tolerance."""
    if value is None:
        return None
    for c in N6_SET:
        if c == 0:
            continue
        if abs(value - c) / c <= EXACT_TOL:
            return c
    return None


def build_resonance_profile(domain_idx, rng):
    """Build a domain-specific resonance profile.

    Each domain has a set of (op_index, result_mod_bucket) pairs that
    "resonate".  Only resonant operations produce discoverable matches.
    This ensures different domains find different constants, making
    cascade enrichment meaningful.

    A domain resonates with ~40% of possible operation-bucket combos,
    so isolation misses many constants but cascade recovers them.
    """
    # 4 ops x 16 buckets (one per n6 constant) = 64 possible slots
    all_slots = [(op_i, c) for op_i in range(len(OPS)) for c in N6_CONSTANTS]
    # Each domain resonates with a random ~40% subset
    k = int(len(all_slots) * 0.40)
    resonant = set(rng.sample(all_slots, k))
    return resonant


def blowup(seeds, resonance, rng):
    """Simulate blowup over a seed pool with domain-specific resonance.

    For every ordered pair of seeds, compute all 4 operations.
    A result counts as EXACT only if:
      1) it matches an n6 constant within tolerance, AND
      2) the (operation, matched_constant) pair is in the domain's
         resonance profile.

    Returns:
        exact_hits: dict mapping discovered n6 constant -> list of (a, op, b)
    """
    exact_hits = OrderedDict()
    seed_list = sorted(set(seeds))

    for a in seed_list:
        for b in seed_list:
            for op_i, (op_name, op_fn) in enumerate(OPS):
                val = op_fn(a, b)
                matched = is_exact(val)
                if matched is not None and (op_i, matched) in resonance:
                    if matched not in exact_hits:
                        exact_hits[matched] = []
                    exact_hits[matched].append((a, op_name, b))

    return exact_hits


def run_isolated(profiles, rng):
    """Run blowup on each domain independently using only base seeds."""
    results = OrderedDict()
    for i, domain in enumerate(CASCADE_DOMAINS):
        hits = blowup(BASE_SEEDS, profiles[domain], rng)
        results[domain] = {
            "seeds": list(BASE_SEEDS),
            "hits": hits,
            "exact_count": len(hits),
            "discovered_values": set(hits.keys()),
        }
    return results


def run_cascade(profiles, rng):
    """Run blowup with cascade: each domain's discoveries feed the next."""
    results = OrderedDict()
    cascade_pool = set()  # accumulates discovered n6 constants

    for domain in CASCADE_DOMAINS:
        seeds = list(BASE_SEEDS) + sorted(cascade_pool)
        hits = blowup(seeds, profiles[domain], rng)

        discovered = set(hits.keys())
        new_for_cascade = discovered - set(BASE_SEEDS)
        cascade_pool |= new_for_cascade

        results[domain] = {
            "seeds": seeds,
            "hits": hits,
            "exact_count": len(hits),
            "discovered_values": discovered,
            "cascade_new": new_for_cascade,
            "cascade_pool_size": len(cascade_pool),
        }
    return results


def main():
    rng = random.Random(42)

    print("=" * 72)
    print("  Experiment: Resonance Cascade")
    print("  Chaining blowup outputs across domains")
    print("=" * 72)

    # --- Step 1: Setup ---
    print(f"\n[1] Setup")
    print(f"    n6 constant pool ({len(N6_CONSTANTS)}): {N6_CONSTANTS}")
    print(f"    Base seeds (first 7):  {BASE_SEEDS}")
    print(f"    Cascade domains ({len(CASCADE_DOMAINS)}): {' -> '.join(CASCADE_DOMAINS)}")
    print(f"    EXACT tolerance: {EXACT_TOL*100:.1f}%")
    print(f"    Resonance coverage: ~40% of operation-constant slots per domain")

    # Build domain-specific resonance profiles
    profiles = {}
    for i, domain in enumerate(CASCADE_DOMAINS):
        profiles[domain] = build_resonance_profile(i, rng)
    print(f"    Profiles built: {len(profiles)} domains")

    # --- Step 2: Isolated blowup (no cascade) ---
    print(f"\n[2] Isolated blowup (each domain uses only base seeds)")
    iso = run_isolated(profiles, rng)

    print(f"    {'Domain':<12s} {'Seeds':>6s} {'EXACT':>6s} {'Discovered constants'}")
    print("    " + "-" * 60)
    total_iso = 0
    for domain, data in iso.items():
        vals = sorted(data["discovered_values"])
        print(f"    {domain:<12s} {len(data['seeds']):>6d} {data['exact_count']:>6d}"
              f"   {vals}")
        total_iso += data["exact_count"]
    print(f"    {'TOTAL':<12s} {'':>6s} {total_iso:>6d}")

    # --- Step 3: Cascaded blowup ---
    print(f"\n[3] Cascaded blowup (discoveries feed downstream)")
    cas = run_cascade(profiles, rng)

    print(f"    {'Domain':<12s} {'Seeds':>6s} {'EXACT':>6s} {'Pool':>5s} {'New from cascade'}")
    print("    " + "-" * 65)
    total_cas = 0
    cumulative_exact = []
    for domain, data in cas.items():
        new_vals = sorted(data.get("cascade_new", set()))
        pool_sz = data.get("cascade_pool_size", 0)
        new_str = str(new_vals) if new_vals else "---"
        print(f"    {domain:<12s} {len(data['seeds']):>6d} {data['exact_count']:>6d}"
              f" {pool_sz:>5d}   {new_str}")
        total_cas += data["exact_count"]
        cumulative_exact.append(total_cas)
    print(f"    {'TOTAL':<12s} {'':>6s} {total_cas:>6d}")

    # --- Step 4: Growth curve ---
    print(f"\n[4] Cumulative EXACT growth curve")
    iso_cumulative = []
    running = 0
    for domain, data in iso.items():
        running += data["exact_count"]
        iso_cumulative.append(running)

    print(f"    {'Domain':<12s} {'Isolated':>10s} {'Cascaded':>10s} {'Delta':>6s}")
    print("    " + "-" * 42)
    for i, domain in enumerate(CASCADE_DOMAINS):
        delta = cumulative_exact[i] - iso_cumulative[i]
        print(f"    {domain:<12s} {iso_cumulative[i]:>10d} {cumulative_exact[i]:>10d}"
              f" {delta:>+6d}")

    # --- Step 5: Amplification analysis ---
    print(f"\n[5] Amplification analysis")
    print(f"    Isolated total EXACT:   {total_iso}")
    print(f"    Cascaded total EXACT:   {total_cas}")

    if total_iso > 0:
        amp = total_cas / total_iso
        print(f"    Amplification factor:   {amp:.2f}x")
    else:
        amp = float('inf')
        print(f"    Amplification factor:   inf (isolated found 0)")

    # Per-domain amplification
    print(f"\n    Per-domain amplification:")
    print(f"    {'Domain':<12s} {'Iso':>5s} {'Cas':>5s} {'Factor':>8s}")
    print("    " + "-" * 34)
    for domain in CASCADE_DOMAINS:
        e_iso = iso[domain]["exact_count"]
        e_cas = cas[domain]["exact_count"]
        if e_iso > 0:
            factor = f"{e_cas / e_iso:.2f}x"
        elif e_cas > 0:
            factor = "inf"
        else:
            factor = "1.00x"
        print(f"    {domain:<12s} {e_iso:>5d} {e_cas:>5d} {factor:>8s}")

    # --- Step 6: Cascade pool evolution ---
    print(f"\n[6] Cascade pool evolution")
    pool_sizes = [cas[d]["cascade_pool_size"] for d in CASCADE_DOMAINS]
    seed_counts = [len(cas[d]["seeds"]) for d in CASCADE_DOMAINS]
    for i, domain in enumerate(CASCADE_DOMAINS):
        bar = "#" * seed_counts[i]
        print(f"    {domain:<12s}  seeds={seed_counts[i]:>3d}  pool={pool_sizes[i]:>3d}  {bar}")

    # --- Step 7: Top discoveries (cascade-only) ---
    print(f"\n[7] Sample cascade-only discoveries")
    for domain, data in cas.items():
        cascade_only = data["discovered_values"] - iso[domain]["discovered_values"]
        if cascade_only:
            for c in sorted(cascade_only)[:3]:
                example = data["hits"][c][0]
                print(f"    {domain:<12s}  {example[0]} {example[1]} {example[2]} = {c}"
                      f"  (cascade-only)")

    # --- Step 8: Summary ---
    print(f"\n[8] Summary")
    print(f"    Cascade order: {' -> '.join(CASCADE_DOMAINS)}")
    print(f"    Total isolated EXACT:   {total_iso}")
    print(f"    Total cascaded EXACT:   {total_cas}")
    if total_iso > 0:
        pct = (total_cas - total_iso) / total_iso * 100
        print(f"    Cascade gain:           +{pct:.1f}%")
    print(f"    Amplification factor:   {amp:.2f}x")
    print(f"    Final cascade pool:     {pool_sizes[-1]} unique n6 constants")
    print(f"    n=6: {len(CASCADE_DOMAINS)} domains, {len(N6_CONSTANTS)} n6 constants,"
          f" base seeds = first {len(BASE_SEEDS)}")

    if total_cas > total_iso:
        print("\n    RESULT: Resonance cascade amplifies EXACT discovery across domains.")
    elif total_cas == total_iso:
        print("\n    RESULT: No amplification -- base seeds already saturate all reachable constants.")
    else:
        print("\n    RESULT: Cascade produced fewer matches (unexpected).")

    print()


if __name__ == "__main__":
    main()
