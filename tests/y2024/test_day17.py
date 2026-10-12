TEST_STRING_1 = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

TEST_STRING_2 = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""

# Exercises bst, bxl, bxc, bdv and cdv (plus a combo operand referring to register C).
TEST_STRING_3 = """Register A: 10
Register B: 0
Register C: 0

Program: 2,4,1,5,4,0,6,1,7,1,5,6"""

from aoc_py.y2024.day17 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "4,6,3,5,6,3,5,2,1,0"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "5,7,3,0"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "5"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "117440"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING_2) == ("5,7,3,0", "117440")
