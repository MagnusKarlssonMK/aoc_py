TEST_STRING_1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

TEST_STRING_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

# Edge cases: a digit word glued to the next one ('threeight' is 38), and a line without any digits at all, which
# contributes nothing to the sum.
TEST_STRING_3 = """threeight
abc"""

from aoc_py.y2023.day01 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "142"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "0"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "281"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "38"
