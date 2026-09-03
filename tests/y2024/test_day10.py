TEST_STRING_1 = """0123
1234
8765
9876"""

TEST_STRING_2 = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

from aoc_py.y2024.day10 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "1"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    p1, p2 = solve_parts(TEST_STRING_2)
    assert p1 == "36"
    assert p2 == "81"
