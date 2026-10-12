import pytest

TEST_STRING = """5764801
17807724"""

from aoc_py.y2020.day25 import discrete_log, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "14897079"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "-"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("14897079", "-")


# ----------- Discrete log ------------


def test_discrete_log() -> None:
    assert discrete_log(5764801, 7, 20201227) == 8
    with pytest.raises(ValueError):
        _ = discrete_log(3, 2, 7)
