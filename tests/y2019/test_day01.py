TEST_STRING_1 = """12
14
1969
100756"""

TEST_STRING_2 = """14
1969
100756"""

from aoc_py.y2019.day01 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "34241"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "51314"
