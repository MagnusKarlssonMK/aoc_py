TEST_STRING = """s1,x3/4,pe/b"""

# This dance has an orbit length of 140 rounds, so the 100-round target is always
# reached before a cycle can be detected (fallback path in get_p2, no repeats seen).
TEST_STRING_LONG_NO_CYCLE = "s7,x0/1,x2/15"

import pytest

from aoc_py.y2017.day16 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "paedcbfghijklmno"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "ghidjklmnopabcef"


# ----------- Edge cases ------------


def test_part2_reaches_target_without_cycle() -> None:
    p = InputData(TEST_STRING_LONG_NO_CYCLE)
    _ = p.get_p1()
    assert (
        p.get_p2(rounds=100) == "dbcfehgkijmlonap"
    )  # arrangement after exactly 100 rounds


def test_unknown_move_op_loudly_rejected() -> None:
    with pytest.raises(ValueError):
        _ = InputData("q1")


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("paedcbfghijklmno", "ghidjklmnopabcef")
