TEST_STRING = """..#
#..
..."""

from aoc_py.y2017 import day22
from aoc_py.y2017.day22 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "5587"


# ----------- Part 2 ------------


def test_part2_1(monkeypatch) -> None:
    # 10,000,000 bursts is too slow for the test suite; 100 is enough to exercise every NodeState branch.
    monkeypatch.setattr(day22, "PART2_BURSTS", 100)
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "26"


# ----------- Both parts ------------


def test_both_parts(monkeypatch) -> None:
    monkeypatch.setattr(day22, "PART2_BURSTS", 100)
    assert solve_parts(TEST_STRING) == ("5587", "26")
