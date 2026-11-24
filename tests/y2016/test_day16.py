import pytest

from aoc_py.y2016.day16 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p = InputData("110010110100")
    p1 = p.get_checksum(12)
    assert p1 == "100"


def test_part1_solve_parts(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2016.day16.PART1_DISK_SIZE", 12)
    assert solve_parts("10000", 1) == ("011", "-1")


# ----------- Part 2 ------------


def test_part2_1() -> None:
    p = InputData("10000")
    p1 = p.get_checksum(20)
    assert p1 == "01100"


def test_part2_solve_parts(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2016.day16.PART2_DISK_SIZE", 20)
    assert solve_parts("10000", 2) == ("-1", "01100")


# ----------- Both parts ------------


def test_both_parts(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2016.day16.PART1_DISK_SIZE", 12)
    monkeypatch.setattr("aoc_py.y2016.day16.PART2_DISK_SIZE", 20)
    assert solve_parts("10000") == ("011", "01100")
