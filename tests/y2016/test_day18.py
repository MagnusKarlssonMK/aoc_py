import pytest

from aoc_py.y2016.day18 import InputData, solve_parts

# ----------- Safe tile counts ------------


def test_1() -> None:
    p = InputData("..^^.")
    p1 = p.get_safetile_count(3)
    assert p1 == 6


def test_2() -> None:
    p = InputData(".^^.^.^^^^")
    p1 = p.get_safetile_count(10)
    assert p1 == 38


def test_single_row() -> None:
    assert InputData("..^^.").get_safetile_count(1) == 3


def test_all_safe() -> None:
    assert InputData(".....").get_safetile_count(4) == 20


# ----------- Part 1 ------------


def test_part1_solve_parts(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2016.day18.PART1_ROWS", 10)
    assert solve_parts(".^^.^.^^^^", 1) == ("38", "-1")


# ----------- Part 2 ------------


def test_part2_solve_parts(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2016.day18.PART2_ROWS", 10)
    assert solve_parts(".^^.^.^^^^", 2) == ("-1", "38")


# ----------- Both parts ------------


def test_both_parts(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2016.day18.PART1_ROWS", 3)
    monkeypatch.setattr("aoc_py.y2016.day18.PART2_ROWS", 10)
    assert solve_parts(".^^.^.^^^^") == ("12", "38")
