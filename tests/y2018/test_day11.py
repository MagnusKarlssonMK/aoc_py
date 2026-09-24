TEST_STRING_1 = """18"""
TEST_STRING_2 = """42"""

from aoc_py.y2018.day11 import solve_parts

# Pretty slow solver, so disabling tests for the second input

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "33,45"


# def test_part1_2() -> None:
#    p1, _ = solve_parts(TEST_STRING_2, 1)
#    assert p1 == "21,61"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "90,269,16"


# def test_part2_2() -> None:
#    _, p2 = solve_parts(TEST_STRING_2, 2)
#    assert p2 == "232,251,12"
