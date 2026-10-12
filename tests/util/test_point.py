"""Unit tests for the shared Point/Directions helpers in util.point."""

import pytest

from aoc_py.util.point import Directions, Point


def test_from_str_comma() -> None:
    assert Point.from_str("3,4") == Point(3, 4)


def test_from_str_dash() -> None:
    assert Point.from_str("5-7") == Point(5, 7)


def test_from_str_invalid() -> None:
    with pytest.raises(ValueError, match="Can't parse Point"):
        _ = Point.from_str("nope")


def test_rotate_left() -> None:
    assert Point(1, 0).rotate_left() == Point(0, -1)
    assert Point(3, 4).rotate_left() == Point(4, -3)


def test_rotate_right() -> None:
    assert Point(1, 0).rotate_right() == Point(0, 1)
    assert Point(3, 4).rotate_right() == Point(-4, 3)


def test_manhattan() -> None:
    assert Point(0, 0).manhattan(Point(3, 4)) == 7
    assert Point(1, 1).manhattan(Point(1, 1)) == 0


def test_determinant() -> None:
    assert Point(1, 2).determinant(Point(3, 4)) == -2
    assert Point(0, 1).determinant(Point(1, 0)) == -1


def test_reverse() -> None:
    assert Point(1, -2).reverse() == Point(-1, 2)


def test_add() -> None:
    assert Point(1, 2) + Point(3, 4) == Point(4, 6)


def test_sub() -> None:
    assert Point(1, 2) - Point(3, 4) == Point(-2, -2)


def test_mul() -> None:
    assert Point(1, 2) * 3 == Point(3, 6)


def test_less_than_same_row() -> None:
    assert Point(1, 1) < Point(2, 1)
    assert not Point(2, 1) < Point(1, 1)


def test_less_than_different_row() -> None:
    assert Point(5, 1) < Point(0, 2)


def test_directions() -> None:
    assert Directions.ORIGIN == Point(0, 0)
    assert Directions.LEFT == Point(-1, 0)
    assert Directions.RIGHT == Point(1, 0)
    assert Directions.UP == Point(0, -1)
    assert Directions.DOWN == Point(0, 1)
    assert Directions.DIAG_R_D == Point(1, 1)
    assert Directions.DIAG_L_D == Point(-1, 1)
    assert Directions.DIAG_L_U == Point(-1, -1)
    assert Directions.DIAG_R_U == Point(1, -1)
    assert Directions.NEIGHBORS_STRAIGHT == [
        Directions.RIGHT,
        Directions.DOWN,
        Directions.LEFT,
        Directions.UP,
    ]
    assert len(Directions.NEIGHBORS_ALL) == 8
