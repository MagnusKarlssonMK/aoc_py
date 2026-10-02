# The official test input, used for both parts.
TEST_STRING_1 = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

# Custom test input.
# A plateau of 'z' walls S off in both directions. From 'a' the only legal step is
# onto 'b' or lower, and walking uphill out of 'a' gains at most one letter per step,
# so neither the forward search nor the reversed one can ever reach the plateau. Both
# parts exhaust their queue and return -1, which is the only way to cover those lines.
TEST_STRING_2 = """Szz
zzz
zzE"""

from aoc_py.y2022.day12 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "31"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "-1"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "29"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "-1"
