TEST_STRING = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""

from aoc_py.y2020.day22 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "306"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "291"
