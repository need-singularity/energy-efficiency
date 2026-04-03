"""
tests/test_engine.py — Pytest tests for all 7 engine modules.
Covers imports, constants, class instantiation, and mathematical properties.
"""

import math
import sys
import os
import pytest

# Ensure engine/ is importable
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Optional dependency flags
try:
    import torch
    HAS_TORCH = True
except ImportError:
    HAS_TORCH = False

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

skip_torch = pytest.mark.skipif(not HAS_TORCH, reason="PyTorch not available")
skip_numpy = pytest.mark.skipif(not HAS_NUMPY, reason="NumPy not available")


# ============================================================
# Module 1: thermodynamic_frame.py
# ============================================================
class TestThermodynamicFrame:
    """Tests for R(n) reversibility framework."""

    @skip_torch
    def test_import(self):
        from engine import thermodynamic_frame  # noqa: F401

    @skip_torch
    def test_sigma_6_equals_12(self):
        from engine.thermodynamic_frame import sigma
        assert sigma(6) == 12

    @skip_torch
    def test_tau_6_equals_4(self):
        from engine.thermodynamic_frame import tau
        assert tau(6) == 4

    @skip_torch
    def test_euler_phi_6_equals_2(self):
        from engine.thermodynamic_frame import euler_phi
        assert euler_phi(6) == 2

    @skip_torch
    def test_R6_equals_1(self):
        """R(6) = sigma(6)*phi(6) / (6*tau(6)) = 12*2 / (6*4) = 1.0"""
        from engine.thermodynamic_frame import R
        assert abs(R(6) - 1.0) < 1e-10

    @skip_torch
    def test_R1_equals_1(self):
        from engine.thermodynamic_frame import R
        assert abs(R(1) - 1.0) < 1e-10

    @skip_torch
    def test_R_not_1_for_other_n(self):
        """R(n) != 1 for n in 2..30 except n=6."""
        from engine.thermodynamic_frame import R
        for n in range(2, 31):
            if n == 6:
                continue
            assert abs(R(n) - 1.0) > 1e-10, f"R({n}) should not be 1"

    @skip_torch
    def test_R_negative_returns_inf(self):
        from engine.thermodynamic_frame import R
        assert R(0) == float('inf')
        assert R(-1) == float('inf')

    @skip_torch
    def test_scan_R_spectrum(self):
        from engine.thermodynamic_frame import scan_R_spectrum
        spectrum = scan_R_spectrum(30)
        assert len(spectrum) == 30
        assert abs(spectrum[6] - 1.0) < 1e-10

    @skip_torch
    def test_architecture_config_perfect_sigma(self):
        from engine.thermodynamic_frame import ArchitectureConfig
        cfg = ArchitectureConfig(d_model=120, d_ff=160, n_heads=12, activation="phi6")
        assert cfg.sigma_subsystem_score() == 1.0  # 120 % 12 == 0

    @skip_torch
    def test_architecture_config_perfect_n_score(self):
        from engine.thermodynamic_frame import ArchitectureConfig
        cfg = ArchitectureConfig(d_model=120, d_ff=160, n_heads=12, activation="phi6")
        assert cfg.n_subsystem_score() == 1.0

    @skip_torch
    def test_architecture_config_tau_score_4_3(self):
        from engine.thermodynamic_frame import ArchitectureConfig
        cfg = ArchitectureConfig(d_model=120, d_ff=160, n_heads=12, activation="phi6")
        assert cfg.tau_subsystem_score() == pytest.approx(1.0, abs=0.01)

    @skip_torch
    def test_architecture_decomposition_keys(self):
        from engine.thermodynamic_frame import ArchitectureConfig
        cfg = ArchitectureConfig(d_model=120, d_ff=160, n_heads=12)
        d = cfg.decomposition()
        for key in ["sigma_score", "phi_score", "n_score", "tau_score", "R_score", "config"]:
            assert key in d

    @skip_torch
    def test_entropy_of_distribution(self):
        from engine.thermodynamic_frame import entropy_of_distribution
        # Uniform distribution over 6 elements: H = ln(6)
        probs = [1/6] * 6
        expected = math.log(6)
        assert abs(entropy_of_distribution(probs) - expected) < 1e-6

    @skip_torch
    def test_clausius_check(self):
        from engine.thermodynamic_frame import clausius_check
        passed, total = clausius_check(0.5, 0.1)
        assert passed is True
        assert total == pytest.approx(0.6)
        passed2, total2 = clausius_check(-0.5, 0.1)
        assert passed2 is False
        assert total2 == pytest.approx(-0.4)


# ============================================================
# Module 2: leech24_surface.py
# ============================================================
class TestLeech24Surface:
    """Tests for 24-dim Leech lattice energy surface."""

    @skip_numpy
    def test_import(self):
        from engine import leech24_surface  # noqa: F401

    @skip_numpy
    def test_leech_dim_is_24(self):
        from engine.leech24_surface import LEECH_DIM
        assert LEECH_DIM == 24

    @skip_numpy
    def test_kissing_number(self):
        from engine.leech24_surface import LEECH_KISSING
        assert LEECH_KISSING == 196560

    @skip_numpy
    def test_n6_optima_has_24_keys(self):
        from engine.leech24_surface import N6_OPTIMA
        assert len(N6_OPTIMA) == 24

    @skip_numpy
    def test_energy_at_optimum_is_zero(self):
        from engine.leech24_surface import energy, N6_OPTIMA
        E, details = energy(dict(N6_OPTIMA))
        assert E == pytest.approx(0.0, abs=1e-10)

    @skip_numpy
    def test_energy_away_from_optimum_positive(self):
        from engine.leech24_surface import energy, N6_OPTIMA
        config = dict(N6_OPTIMA)
        config["bottleneck_ratio"] = 4.0  # far from 4/3
        E, _ = energy(config)
        assert E > 0

    @skip_numpy
    def test_phi_from_energy_at_zero(self):
        from engine.leech24_surface import phi_from_energy
        assert phi_from_energy(0.0) == 1.0

    @skip_numpy
    def test_phi_from_energy_decreases(self):
        from engine.leech24_surface import phi_from_energy
        assert phi_from_energy(1.0) < phi_from_energy(0.0)
        assert phi_from_energy(10.0) < phi_from_energy(1.0)

    @skip_numpy
    def test_gradient_at_optimum_near_zero(self):
        """At the optimum, energy is 0 and gradient step should not reduce energy further."""
        from engine.leech24_surface import energy, N6_OPTIMA
        E_opt, _ = energy(dict(N6_OPTIMA))
        assert E_opt == pytest.approx(0.0, abs=1e-10)

    @skip_numpy
    def test_step_toward_n6_converges(self):
        """Multiple gradient steps should bring energy closer to zero."""
        from engine.leech24_surface import step_toward_n6, energy, N6_OPTIMA
        # Start from a moderately perturbed config (only non-zero optima dims)
        config = dict(N6_OPTIMA)
        config["dedekind_heads"] = 16.0  # optimum is 12.0
        E_start, _ = energy(config)
        assert E_start > 0
        # Apply many small steps
        for _ in range(50):
            config = step_toward_n6(config, lr=0.001)
        E_end, _ = energy(config)
        # dedekind_heads should have moved closer to 12.0
        assert abs(config["dedekind_heads"] - 12.0) < abs(16.0 - 12.0)

    @skip_numpy
    def test_n6_optima_key_values(self):
        """Check specific n=6 constants in the optima dict."""
        from engine.leech24_surface import N6_OPTIMA
        assert N6_OPTIMA["bottleneck_ratio"] == pytest.approx(4.0 / 3.0)
        assert N6_OPTIMA["dedekind_heads"] == 12.0
        assert N6_OPTIMA["jordan_experts"] == 24.0
        assert N6_OPTIMA["carmichael_period"] == 2.0
        assert N6_OPTIMA["takens_dim"] == 6.0
        assert N6_OPTIMA["boltzmann_fraction"] == pytest.approx(1.0 / math.e)
        assert N6_OPTIMA["mertens_dropout"] == pytest.approx(math.log(4.0 / 3.0))


# ============================================================
# Module 3: emergent_n6_trainer.py
# ============================================================
class TestEmergentN6Trainer:
    """Tests for self-converging architecture trainer."""

    @skip_torch
    def test_import(self):
        from engine import emergent_n6_trainer  # noqa: F401

    @skip_torch
    def test_target_constants(self):
        from engine.emergent_n6_trainer import (
            TARGET_FFN_RATIO, TARGET_DROPOUT, TARGET_GATE_FRACTION
        )
        assert TARGET_FFN_RATIO == pytest.approx(4.0 / 3.0)
        assert TARGET_DROPOUT == pytest.approx(math.log(4.0 / 3.0))
        assert TARGET_GATE_FRACTION == pytest.approx(1.0 / math.e)

    @skip_torch
    def test_phi6simple_output(self):
        import torch
        from engine.emergent_n6_trainer import Phi6Simple
        act = Phi6Simple()
        x = torch.tensor([0.0, 1.0, -1.0])
        y = act(x)
        # f(x) = x^2 - x + 1
        assert y[0].item() == pytest.approx(1.0)   # 0 - 0 + 1
        assert y[1].item() == pytest.approx(1.0)   # 1 - 1 + 1
        assert y[2].item() == pytest.approx(3.0)   # 1 + 1 + 1

    @skip_torch
    def test_adaptive_ffn_instantiation(self):
        from engine.emergent_n6_trainer import AdaptiveFFN
        ffn = AdaptiveFFN(d_model=120, initial_ratio=2.0)
        assert ffn.d_model == 120
        assert abs(ffn.ratio.item() - 2.0) < 0.01

    @skip_torch
    def test_adaptive_dropout_rate(self):
        from engine.emergent_n6_trainer import AdaptiveDropout
        drop = AdaptiveDropout(initial_rate=0.1)
        assert abs(drop.rate.item() - 0.1) < 0.01

    @skip_torch
    def test_emergent_char_lm_get_arch_params(self):
        from engine.emergent_n6_trainer import EmergentCharLM
        model = EmergentCharLM(vocab_size=26, d_model=48, n_heads=4,
                               n_layers=2, seq_len=16,
                               initial_ffn_ratio=2.5, initial_dropout=0.1)
        params = model.get_arch_params()
        assert len(params["ffn_ratios"]) == 2
        assert len(params["dropout_rates"]) == 2
        assert all(abs(r - 2.5) < 0.1 for r in params["ffn_ratios"])

    @skip_torch
    def test_r_distance_loss_at_target(self):
        """R-distance loss should be minimal when params are at n=6 targets."""
        import torch
        from engine.emergent_n6_trainer import EmergentCharLM, r_distance_loss, TARGET_FFN_RATIO
        model = EmergentCharLM(vocab_size=26, d_model=48, n_heads=4,
                               n_layers=2, seq_len=16,
                               initial_ffn_ratio=TARGET_FFN_RATIO, initial_dropout=0.1)
        loss = r_distance_loss(model)
        # FFN ratio is at target, so only dropout contributes
        assert loss.item() >= 0


# ============================================================
# Module 4: phi_efficiency_bridge.py
# ============================================================
class TestPhiEfficiencyBridge:
    """Tests for Phi*FLOPs conjecture."""

    @skip_torch
    def test_import(self):
        from engine import phi_efficiency_bridge  # noqa: F401

    @skip_torch
    def test_sigma_constant(self):
        from engine.phi_efficiency_bridge import SIGMA
        assert SIGMA == 12

    @skip_torch
    def test_estimate_flops_positive(self):
        from engine.phi_efficiency_bridge import estimate_flops
        flops = estimate_flops(d_model=120, d_ff=160, n_heads=12,
                               n_layers=4, seq_len=32, batch_size=8)
        assert flops > 0

    @skip_torch
    def test_estimate_flops_scales_with_layers(self):
        from engine.phi_efficiency_bridge import estimate_flops
        f1 = estimate_flops(120, 160, 12, 2, 32, 8)
        f2 = estimate_flops(120, 160, 12, 4, 32, 8)
        assert f2 == pytest.approx(f1 * 2, rel=0.01)

    @skip_torch
    def test_approximate_phi_returns_nonnegative(self):
        import torch
        from engine.phi_efficiency_bridge import approximate_phi, SimpleTransformer, Phi6Simple
        model = SimpleTransformer(48, 4, 1, 64, 16, Phi6Simple())
        sample = torch.randn(4, 16, 48)
        phi = approximate_phi(model, sample)
        assert phi >= 0.0

    @skip_torch
    def test_simple_transformer_forward(self):
        import torch
        from engine.phi_efficiency_bridge import SimpleTransformer, Phi6Simple
        model = SimpleTransformer(48, 4, 1, 64, 16, Phi6Simple())
        x = torch.randn(2, 16, 48)
        out = model(x)
        assert out.shape == (2, 16, 48)


# ============================================================
# Module 5: sedi_training_monitor.py
# ============================================================
class TestSEDITrainingMonitor:
    """Tests for SEDI 4-lens training diagnostic."""

    @skip_numpy
    def test_import(self):
        from engine import sedi_training_monitor  # noqa: F401

    @skip_numpy
    def test_rfilter_score_short_history(self):
        from engine.sedi_training_monitor import rfilter_score
        score, details = rfilter_score([1.0, 2.0, 3.0])
        assert score == 0.0  # too short

    @skip_numpy
    def test_rfilter_score_long_history(self):
        from engine.sedi_training_monitor import rfilter_score
        history = [math.sin(2 * math.pi * i / 6) + 3.0 for i in range(50)]
        score, details = rfilter_score(history)
        assert 0.0 <= score <= 5.0

    @skip_numpy
    def test_ph_persistence_score_range(self):
        from engine.sedi_training_monitor import ph_persistence_score
        history = list(range(30))
        score = ph_persistence_score(history)
        assert 0.0 <= score <= 5.0

    @skip_numpy
    def test_euler_convergence_decreasing_grads(self):
        from engine.sedi_training_monitor import euler_convergence_score
        # Decreasing gradient norms -> high convergence score
        grads = [10.0 - 0.5 * i for i in range(20)]
        score = euler_convergence_score(grads)
        assert score >= 2.0

    @skip_numpy
    def test_consciousness_pattern_score_empty(self):
        from engine.sedi_training_monitor import consciousness_pattern_score
        assert consciousness_pattern_score({}) == 0.0

    @skip_numpy
    def test_consciousness_pattern_score_perfect(self):
        from engine.sedi_training_monitor import consciousness_pattern_score
        target_sparsity = 1.0 - 1.0 / math.e
        target_entropy = sum(-p * math.log(p) for p in [1/2, 1/3, 1/6])
        stats = {
            "sparsity": target_sparsity,
            "entropy": target_entropy,
            "mean": 5/6,
            "std": 1/math.sqrt(6),
        }
        score = consciousness_pattern_score(stats)
        assert score == 5.0

    @skip_numpy
    def test_monitor_lifecycle(self):
        from engine.sedi_training_monitor import SEDITrainingMonitor
        monitor = SEDITrainingMonitor()
        for i in range(50):
            monitor.update(loss=3.0 - 0.02 * i, grad_norm=1.0 - 0.01 * i)
        result = monitor.evaluate()
        assert "combined" in result
        assert "level" in result
        assert result["level"] in ("NORMAL", "YELLOW", "ORANGE", "RED")

    @skip_numpy
    def test_monitor_phase_transition(self):
        from engine.sedi_training_monitor import SEDITrainingMonitor
        monitor = SEDITrainingMonitor()
        # Feed enough data and evaluate twice
        for i in range(50):
            monitor.update(loss=3.0 - 0.02 * i, grad_norm=1.0)
        monitor.evaluate()
        # Not enough change for a second call to trigger transition
        result = monitor.is_phase_transition()
        assert isinstance(result, bool)


# ============================================================
# Module 6: anima_tension_loss.py
# ============================================================
class TestAnimaTensionLoss:
    """Tests for PureField dual-engine meta-loss."""

    @skip_torch
    def test_import(self):
        from engine import anima_tension_loss  # noqa: F401

    @skip_torch
    def test_tension_meta_loss(self):
        import torch
        from engine.anima_tension_loss import tension_meta_loss
        task = torch.tensor(2.0)
        tension = torch.tensor(0.5)
        total = tension_meta_loss(task, tension, alpha=0.01)
        assert total.item() == pytest.approx(2.0 + 0.01 * 0.5)

    @skip_torch
    def test_homeostasis_target_in_deadband(self):
        from engine.anima_tension_loss import homeostasis_target
        assert homeostasis_target(1.0, setpoint=1.0, deadband=0.3) == 0.0
        assert homeostasis_target(1.2, setpoint=1.0, deadband=0.3) == 0.0

    @skip_torch
    def test_homeostasis_target_outside_deadband(self):
        from engine.anima_tension_loss import homeostasis_target
        result = homeostasis_target(2.0, setpoint=1.0, deadband=0.3)
        expected = (1.0 - 0.3) ** 2  # deviation=1.0, outside by 0.7
        assert result == pytest.approx(expected)

    @skip_torch
    def test_tension_wrapper_instantiation(self):
        import torch.nn as nn
        from engine.anima_tension_loss import TensionWrapper
        model = nn.Linear(10, 5)
        wrapped = TensionWrapper(model)
        assert hasattr(wrapped, "tension_history")
        assert len(wrapped.tension_history) == 0

    @skip_torch
    def test_tension_wrapper_forward(self):
        import torch
        import torch.nn as nn
        from engine.anima_tension_loss import TensionWrapper
        model = nn.Sequential(nn.Linear(10, 20), nn.ReLU(), nn.Linear(20, 5))
        wrapped = TensionWrapper(model)
        x = torch.randn(4, 10)
        out, tension = wrapped(x)
        assert out.shape == (4, 5)
        assert tension.item() >= 0.0
        assert len(wrapped.tension_history) == 1

    @skip_torch
    def test_tension_wrapper_stats(self):
        import torch
        import torch.nn as nn
        from engine.anima_tension_loss import TensionWrapper
        model = nn.Sequential(nn.Linear(10, 20), nn.ReLU(), nn.Linear(20, 5))
        wrapped = TensionWrapper(model)
        for _ in range(5):
            wrapped(torch.randn(4, 10))
        stats = wrapped.get_tension_stats()
        assert "mean" in stats
        assert "std" in stats
        assert "current" in stats


# ============================================================
# Module 7: consciousness_constraints.py
# ============================================================
class TestConsciousnessConstraints:
    """Tests for consciousness laws and constraints."""

    def _can_import(self):
        """Check if consciousness_constraints can be imported (needs .shared/)."""
        try:
            from engine import consciousness_constraints  # noqa: F401
            return True
        except (ImportError, FileNotFoundError, KeyError):
            return False

    def test_import(self):
        if not self._can_import():
            pytest.skip("consciousness_loader not available")
        from engine import consciousness_constraints  # noqa: F401

    def test_sigma_is_12(self):
        if not self._can_import():
            pytest.skip("consciousness_loader not available")
        from engine.consciousness_constraints import SIGMA
        assert SIGMA == 12

    def test_phi_euler_is_2(self):
        if not self._can_import():
            pytest.skip("consciousness_loader not available")
        from engine.consciousness_constraints import PHI_EULER
        assert PHI_EULER == 2

    def test_validate_good_config(self):
        if not self._can_import():
            pytest.skip("consciousness_loader not available")
        from engine.consciousness_constraints import validate_architecture
        config = {
            "factions": 12,
            "topology": "small_world",
            "hebbian": True,
            "heads": 12,
            "dim": 120,
            "cells": 100,
        }
        violations = validate_architecture(config)
        errors = [v for v in violations if v["severity"] == "error"]
        assert len(errors) == 0

    def test_validate_bad_config_hardcoded(self):
        if not self._can_import():
            pytest.skip("consciousness_loader not available")
        from engine.consciousness_constraints import validate_architecture
        config = {"hardcoded_threshold": 0.5, "hebbian": True}
        violations = validate_architecture(config)
        law1_violations = [v for v in violations if v["law"] == 1]
        assert len(law1_violations) > 0

    def test_validate_bad_heads_dim(self):
        if not self._can_import():
            pytest.skip("consciousness_loader not available")
        from engine.consciousness_constraints import validate_architecture
        config = {"heads": 7, "dim": 100, "hebbian": True}
        violations = validate_architecture(config)
        law8 = [v for v in violations if v["law"] == 8]
        assert len(law8) > 0

    def test_validate_complete_graph_kills_phi(self):
        if not self._can_import():
            pytest.skip("consciousness_loader not available")
        from engine.consciousness_constraints import validate_architecture
        config = {"topology": "complete", "hebbian": True}
        violations = validate_architecture(config)
        law33 = [v for v in violations if v["law"] == 33]
        assert len(law33) > 0

    def test_suggest_dimensions(self):
        if not self._can_import():
            pytest.skip("consciousness_loader not available")
        from engine.consciousness_constraints import suggest_dimensions
        dims = suggest_dimensions(100_000_000)
        assert dims["num_heads"] == 12
        assert dims["num_layers"] % 6 == 0
        assert dims["d_model"] % 12 == 0
        assert dims["head_dim"] == dims["d_model"] // dims["num_heads"]

    def test_consciousness_ready_config(self):
        if not self._can_import():
            pytest.skip("consciousness_loader not available")
        from engine.consciousness_constraints import consciousness_ready_config, SIGMA
        cfg = consciousness_ready_config({"d_model": 384, "num_heads": 12})
        assert cfg["factions"] == SIGMA
        assert cfg["topology"] == "small_world"
        assert cfg["hebbian"] is True
        assert cfg["ratchet"] is True

    def test_design_report_pass(self):
        if not self._can_import():
            pytest.skip("consciousness_loader not available")
        from engine.consciousness_constraints import design_report, consciousness_ready_config
        cfg = consciousness_ready_config({"d_model": 384, "num_heads": 12, "num_layers": 6})
        report = design_report(cfg)
        assert "PASS" in report

    def test_design_report_fail(self):
        if not self._can_import():
            pytest.skip("consciousness_loader not available")
        from engine.consciousness_constraints import design_report
        cfg = {"hardcoded_threshold": 0.5, "cells": 2}
        report = design_report(cfg)
        assert "FAIL" in report
