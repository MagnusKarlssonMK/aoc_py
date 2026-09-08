TEST_STRING = """Player 1 starting position: 4
Player 2 starting position: 8
"""

from aoc_py.y2021.day21 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "739785"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "444356092776315"
