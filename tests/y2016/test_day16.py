import pytest

from aoc_py.y2016.day16 import InputData, checksum, dragon_curve, solve_parts

# ----------- Dragon curve / checksum ------------


def test_dragon_curve() -> None:
    assert dragon_curve("1") == "100"
    assert dragon_curve("0") == "001"
    assert dragon_curve("11111") == "11111000000"


def test_checksum() -> None:
    assert checksum("1") == "1"
    assert checksum("101") == "101"  # an odd length is already a checksum
    assert checksum("0000") == "1"  # two folds: 0000 -> 11 -> 1
    assert checksum("01100") == "01100"


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
