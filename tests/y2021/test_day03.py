TEST_STRING = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

from aoc_py.y2021.day03 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "198"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "230"
