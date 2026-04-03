#!/usr/bin/env bash
# Run NEXUS-6 performance benchmarks and save baseline
cd "$(dirname "$0")/.."
mkdir -p ~/.nexus6
~/.cargo/bin/cargo test bench_ -- --nocapture 2>&1 | tee ~/.nexus6/benchmark-baseline.txt
