# tests/test_train.py
"""CI test: run training and assert a minimum accuracy."""

from train import train_and_persist


def test_training_accuracy():
    """Training should produce a model with accuracy greater than 0.6 on synthetic data."""
    acc = train_and_persist()
    assert acc > 0.6, f"Training accuracy too low: {acc:.3f}"
