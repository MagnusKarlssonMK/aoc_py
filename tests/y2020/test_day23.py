import pytest

from aoc_py.y2020.day23 import InputData, solve_parts

TEST_STRING = "389125467"

# ----------- Part 1 ------------


def test_part1_1() -> None:
    assert InputData(TEST_STRING).get_p1(100) == 67384529


# ----------- Part 2 ------------
# A small circle and few moves keep the test fast; the real ten-million-move answer is
# exercised via run().


def test_part2_1(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2020.day23.CUP_COUNT", 20)
    assert InputData(TEST_STRING).get_p2(1000) == 42


# ----------- Both parts ------------


def test_both_parts(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2020.day23.PART2_MOVES", 1000)
    monkeypatch.setattr("aoc_py.y2020.day23.CUP_COUNT", 20)
    assert solve_parts(TEST_STRING) == ("67384529", "42")


def test_parts_are_order_independent(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2020.day23.CUP_COUNT", 20)
    p = InputData(TEST_STRING)
    assert p.get_p2(1000) == 42
    assert p.get_p1(100) == 67384529
