import pytest

from aoc_py.y2024.day20 import solve_parts

TEST_STRING_1 = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

# The published example reports the distribution of cheats by saved time rather than a
# threshold-100 answer, so the gain is lowered to values that reproduce the official counts.

# ----------- Part 1 ------------


def test_part1_1(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2024.day20.GAIN", 2)
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "44"


def test_part1_2(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2024.day20.GAIN", 12)
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "8"


# ----------- Part 2 ------------


def test_part2_1(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2024.day20.GAIN", 50)
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "285"


# ----------- Both parts ------------


def test_both_parts(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2024.day20.GAIN", 50)
    assert solve_parts(TEST_STRING_1) == ("1", "285")
