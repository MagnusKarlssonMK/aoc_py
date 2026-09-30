TEST_STRING_1 = """Player 1 starting position: 4
Player 2 starting position: 8
"""

# The official example has Player 1 win both parts. This is the only pair of starting positions, out of all
# hundred possible ones, where Player 2 wins both, so it is what pins down that part 1 reports the loser's
# score and part 2 reports the winner's total number of universes.
TEST_STRING_2 = """Player 1 starting position: 7
Player 2 starting position: 1
"""

from aoc_py.y2021.day21 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "739785"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "684495"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "444356092776315"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "152587196649184"
