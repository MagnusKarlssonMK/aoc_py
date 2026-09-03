TEST_STRING = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

from aoc_py.y2025.day05 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "3"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "14"
