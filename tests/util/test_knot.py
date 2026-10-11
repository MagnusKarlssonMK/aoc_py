"""Unit tests for the shared knot-hash helpers in util.knot."""

from aoc_py.util.knot import (
    generate_hash,
    get_knot_hash,
    reverse_slice,
    rotate_left,
    rotate_right,
)


def test_rotate_empty() -> None:
    x: list[int] = []
    rotate_left(x, 3)
    assert x == []


def test_rotate_left() -> None:
    x = [1, 2, 3, 4]
    rotate_left(x, 2)
    assert x == [3, 4, 1, 2]


def test_rotate_right() -> None:
    x = [1, 2, 3, 4]
    rotate_right(x, 1)
    assert x == [4, 1, 2, 3]


def test_reverse_slice() -> None:
    x = [1, 2, 3, 4, 5]
    reverse_slice(x, 1, 4)
    assert x == [1, 4, 3, 2, 5]


def test_generate_hash_single_round() -> None:
    assert generate_hash([3, 4, 1, 5], 5, 1) == [3, 4, 2, 1, 0]


def test_get_knot_hash_empty() -> None:
    assert get_knot_hash("") == "a2582a3a0e66e6e86e3812dcb672a272"
