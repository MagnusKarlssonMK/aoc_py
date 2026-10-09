TEST_STRING = """5-8
0-2
4-7"""

import pytest

from aoc_py.y2016.day20 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "3"


def test_part1_zero_blocked() -> None:
    assert solve_parts("0-0", 1)[0] == "1"


def test_part1_starts_late() -> None:
    assert solve_parts("4-5", 1)[0] == "0"


def test_part1_adjacent() -> None:
    assert solve_parts("0-1\n2-3", 1)[0] == "4"


def test_part1_overlapping() -> None:
    assert solve_parts("0-10\n5-6", 1)[0] == "11"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "4294967288"


def test_part2_zero_not_blocked() -> None:
    # Regression: address 0 is allowed when no range covers it.
    assert solve_parts("5-8", 2)[1] == "4294967292"
    assert solve_parts("1-1", 2)[1] == "4294967295"


def test_part2_small_address_space(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2016.day20.MAX_IP", 10)
    assert solve_parts("2-5", 2)[1] == "7"  # allows 0,1,6,7,8,9,10
    assert solve_parts("0-10", 2)[1] == "0"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("3", "4294967288")
