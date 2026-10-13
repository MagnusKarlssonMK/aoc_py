EXAMPLE = """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#"""

import pytest

from aoc_py.y2017 import day21
from aoc_py.y2017.day21 import solve_parts

# ----------- Example ------------


def test_example() -> None:
    # After 2 iterations the start pattern has 12 pixels on.
    assert day21.InputData(EXAMPLE).get_pixel_count(2) == 12


# ----------- Part 1 ------------


def test_part1_1(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(day21, "PART1_ITERATIONS", 2)
    monkeypatch.setattr(day21, "PART2_ITERATIONS", 1)
    p1, _ = solve_parts(EXAMPLE, 1)
    assert p1 == "12"


# ----------- Part 2 ------------


def test_part2_1(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(day21, "PART1_ITERATIONS", 2)
    monkeypatch.setattr(day21, "PART2_ITERATIONS", 1)
    _, p2 = solve_parts(EXAMPLE, 2)
    assert p2 == "4"


# ----------- Both parts ------------


def test_both_parts(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(day21, "PART1_ITERATIONS", 2)
    monkeypatch.setattr(day21, "PART2_ITERATIONS", 1)
    assert solve_parts(EXAMPLE) == ("12", "4")
