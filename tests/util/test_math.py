"""Unit tests for the shared math helpers in util.math."""

from aoc_py.util.math import signum


def test_signum_positive() -> None:
    assert signum(5) == 1


def test_signum_negative() -> None:
    assert signum(-5) == -1


def test_signum_zero() -> None:
    assert signum(0) == 0
