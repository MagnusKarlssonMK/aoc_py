TEST_STRING = """987654321111111
811111111111119
234234234234278
818181911112111"""

from aoc_py.y2025.day03 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "357"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "3121910778619"
