#!/usr/bin/env python3
"""
HEXA-WEAVE W5 Alt-2 cycle 11 fan-out 3/5 — Option C (random 500 sample).

Step 1: Re-issue RCSB Query B (rows=2000), pick deterministic random 500 IDs,
fetch FASTA for each over read-only HTTPS.

Inputs : none
Output : /tmp/cdhit_emul_cycle11_step1_data.json
Budget : ~3-5 min wall-clock; ~1.7 MB bandwidth.
Safety : urllib stdlib only; no third-party deps; no install.
"""
import json
import time
import random
import hashlib
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

QUERY_B = {
    "query": {
        "type": "group",
        "logical_operator": "and",
        "nodes": [
            {
                "type": "terminal",
                "service": "text",
                "parameters": {
                    "attribute": "rcsb_entry_info.polymer_entity_count_RNA",
                    "operator": "greater_or_equal",
                    "value": 1
                }
            },
            {
                "type": "terminal",
                "service": "text",
                "parameters": {
                    "attribute": "rcsb_entry_info.polymer_entity_count_protein",
                    "operator": "greater_or_equal",
                    "value": 1
                }
            },
            {
                "type": "terminal",
                "service": "text",
                "parameters": {
                    "attribute": "rcsb_accession_info.initial_release_date",
                    "operator": "less",
                    "value": "2024-01-01T00:00:00Z"
                }
            }
        ]
    },
    "return_type": "entry",
    "request_options": {
        "paginate": {"start": 0, "rows": 2000},
        "results_content_type": ["experimental"]
    }
}

QUERY_URL = "https://search.rcsb.org/rcsbsearch/v2/query"
FASTA_URL_TPL = "https://www.rcsb.org/fasta/entry/{}"
SEED_HEX = "0xc11abef0"  # cycle 11 seed
SAMPLE_SIZE = 500
MAX_WORKERS = 10
PER_REQ_TIMEOUT_S = 15

def query_b():
    body = json.dumps(QUERY_B).encode("utf-8")
    req = urllib.request.Request(
        QUERY_URL, data=body,
        headers={"Content-Type": "application/json", "User-Agent": "n6-hexa-weave-cycle11/1.0"}
    )
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=30) as r:
        payload = json.loads(r.read())
    dt = time.time() - t0
    total = payload.get("total_count", -1)
    ids = [hit["identifier"] for hit in payload.get("result_set", [])]
    return total, ids, dt

def deterministic_sample(ids, k, seed_hex):
    rng = random.Random(int(seed_hex, 16))
    pool = sorted(ids)  # canonical order
    rng.shuffle(pool)
    return sorted(pool[:k])  # return sorted for stable ordering

def fetch_one(pdb_id):
    url = FASTA_URL_TPL.format(pdb_id)
    req = urllib.request.Request(url, headers={"User-Agent": "n6-hexa-weave-cycle11/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=PER_REQ_TIMEOUT_S) as r:
            txt = r.read().decode("utf-8", errors="replace")
        return pdb_id, txt, None
    except urllib.error.HTTPError as e:
        return pdb_id, None, f"HTTP {e.code}"
    except Exception as e:
        return pdb_id, None, f"{type(e).__name__}: {e}"

def main():
    t_start = time.time()
    print(f"[cycle11/step1] Query B re-issue …", flush=True)
    total, ids, dt = query_b()
    print(f"[cycle11/step1] total_count={total} returned={len(ids)} t={dt:.2f}s", flush=True)
    sample = deterministic_sample(ids, SAMPLE_SIZE, SEED_HEX)
    print(f"[cycle11/step1] sample size={len(sample)} seed={SEED_HEX}", flush=True)

    fasta_records = []
    fail_count = 0
    fails = []
    t_fetch_start = time.time()
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futs = {ex.submit(fetch_one, pid): pid for pid in sample}
        done = 0
        for fut in as_completed(futs):
            pid, txt, err = fut.result()
            done += 1
            if err is None and txt:
                fasta_records.append({"pdb_id": pid, "fasta": txt})
            else:
                fail_count += 1
                fails.append({"pdb_id": pid, "error": err})
            if done % 50 == 0:
                elapsed = time.time() - t_fetch_start
                print(f"[cycle11/step1] fetched {done}/{len(sample)} elapsed={elapsed:.1f}s fails={fail_count}", flush=True)
    fetch_dt = time.time() - t_fetch_start

    out = {
        "meta": {
            "schema": "n6/hexa-weave/cycle11/cdhit_emul_step1/v1",
            "total_count": total,
            "returned": len(ids),
            "sample_size": len(sample),
            "seed": SEED_HEX,
            "query_time_s": round(dt, 3),
            "fasta_fetch_time_s": round(fetch_dt, 3),
            "fasta_fail_count": fail_count,
            "fasta_success_count": len(fasta_records),
            "wall_clock_total_s": round(time.time() - t_start, 3),
            "max_workers": MAX_WORKERS,
            "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        },
        "sample_ids": sample,
        "fasta_records": fasta_records,
        "fails": fails,
    }
    out_path = "/tmp/cdhit_emul_cycle11_step1_data.json"
    with open(out_path, "w") as f:
        json.dump(out, f)
    print(f"[cycle11/step1] DONE wall={out['meta']['wall_clock_total_s']}s wrote={out_path}", flush=True)
    print(f"[cycle11/step1] success={len(fasta_records)} fail={fail_count}", flush=True)

if __name__ == "__main__":
    main()
