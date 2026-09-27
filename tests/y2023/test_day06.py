TEST_STRING_1 = """Time:      7  15   30
Distance:  9  40  200"""

# Both races have a discriminant that is a perfect square, so the roots of the quadratic are whole numbers and the
# hold times matching the distance exactly have to be excluded: time 10 beats 9 with hold times 2 to 8.
TEST_STRING_2 = """Time:      10  7
Distance:   9  9"""

from aoc_py.y2023.day06 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "288"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "28"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "71503"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "106"
