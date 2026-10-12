import pytest

from aoc_py.y2024.day18 import solve_parts

TEST_STRING_1 = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

# ----------- Part 1 ------------


def test_part1_1(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2024.day18.GRID_DIM", 7)
    monkeypatch.setattr("aoc_py.y2024.day18.PART1_BYTES", 12)
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "22"


# ----------- Part 2 ------------


def test_part2_1(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2024.day18.GRID_DIM", 7)
    monkeypatch.setattr("aoc_py.y2024.day18.PART1_BYTES", 12)
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "6,1"


# ----------- Both parts ------------


def test_both_parts(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2024.day18.GRID_DIM", 7)
    monkeypatch.setattr("aoc_py.y2024.day18.PART1_BYTES", 12)
    assert solve_parts(TEST_STRING_1) == ("22", "6,1")
