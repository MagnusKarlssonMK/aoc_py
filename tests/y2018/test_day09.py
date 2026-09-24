TEST_STRING_1 = """10 players; last marble is worth 1618 points"""
TEST_STRING_2 = """13 players; last marble is worth 7999 points"""
TEST_STRING_3 = """17 players; last marble is worth 1104 points"""
TEST_STRING_4 = """21 players; last marble is worth 6111 points"""
TEST_STRING_5 = """30 players; last marble is worth 5807 points"""

from aoc_py.y2018.day09 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "8317"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "146373"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "2764"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "54718"


def test_part1_5() -> None:
    p1, _ = solve_parts(TEST_STRING_5, 1)
    assert p1 == "37305"


# ----------- Part 2 ------------


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "74765078"
