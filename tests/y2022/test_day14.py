# The official test example
TEST_STRING_1 = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

# A flat floor spanning the source column, so every grain comes to rest on it and the
# source is blocked before a single grain gets below the lowest rock. Only this shape
# reaches part 1's fallback, and pinning it stops the -1 sentinel leaking out as an answer.
TEST_STRING_2 = "494,2 -> 506,2"

# An L-shaped wall that catches the sand off to one side of the source, so the answer
# depends on the source sitting at column 500 and not one to either side of it.
TEST_STRING_3 = "499,2 -> 499,4\n500,4 -> 502,4"

from aoc_py.y2022.day14 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "24"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "4"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "3"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "93"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "4"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "28"
