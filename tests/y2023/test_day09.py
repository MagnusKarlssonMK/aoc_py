TEST_STRING = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

from aoc_py.y2023.day09 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "114"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "2"
