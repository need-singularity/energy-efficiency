# ═══════════════════════════════════════════════════════════════
# n6-architecture Makefile — test automation
# ═══════════════════════════════════════════════════════════════

CARGO   := $(HOME)/.cargo/bin/cargo
NEXUS6  := tools/nexus6
PYTHON  := python3

.PHONY: all test test-rust test-python test-quick lint build bench clean help

# ── Default ───────────────────────────────────────────────────
all: lint test build

# ── Tests ─────────────────────────────────────────────────────
test: test-rust test-python
	@echo "=== All tests passed ==="

test-rust:
	@echo "=== Rust tests (nexus6) ==="
	cd $(NEXUS6) && $(CARGO) test --quiet

test-python:
	@echo "=== Python tests ==="
	@if ls tests/test_*.py 1>/dev/null 2>&1; then \
		$(PYTHON) -m pytest tests/ -q --tb=short; \
	else \
		echo "  (no test files in tests/ — skipping)"; \
	fi

test-quick:
	@echo "=== Quick tests (Rust only, no slow) ==="
	cd $(NEXUS6) && $(CARGO) test --quiet -- --skip slow

# ── Lint ──────────────────────────────────────────────────────
lint: lint-rust lint-python
	@echo "=== Lint passed ==="

lint-rust:
	@echo "=== cargo check ==="
	cd $(NEXUS6) && $(CARGO) check --quiet

lint-python:
	@echo "=== Python syntax check ==="
	@exitcode=0; \
	for f in techniques/*.py engine/*.py; do \
		if [ -f "$$f" ]; then \
			$(PYTHON) -m py_compile "$$f" || exitcode=1; \
		fi; \
	done; \
	exit $$exitcode

# ── Build ─────────────────────────────────────────────────────
build:
	@echo "=== Building nexus6 (release) ==="
	cd $(NEXUS6) && $(CARGO) build --release

# ── Bench ─────────────────────────────────────────────────────
bench:
	@echo "=== Benchmarks ==="
	cd $(NEXUS6) && $(CARGO) bench

# ── Clean ─────────────────────────────────────────────────────
clean:
	cd $(NEXUS6) && $(CARGO) clean

# ── Help ──────────────────────────────────────────────────────
help:
	@echo "Targets:"
	@echo "  make all         — lint + test + build"
	@echo "  make test        — run ALL tests (Rust + Python)"
	@echo "  make test-rust   — cargo test for nexus6"
	@echo "  make test-python — pytest for tests/"
	@echo "  make test-quick  — fast subset (Rust, skip slow)"
	@echo "  make lint        — cargo check + Python syntax"
	@echo "  make build       — cargo build --release (nexus6)"
	@echo "  make bench       — run benchmarks"
	@echo "  make clean       — cargo clean"
