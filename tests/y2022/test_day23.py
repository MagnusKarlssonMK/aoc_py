TEST_STRING_1 = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#.."""

# A 2x2 block that stabilises on round 4, so the round 10 score is never recorded and get_roundscore falls back to the
# last round played.
TEST_STRING_2 = """##
##"""

# A shape where an elf's only neighbour lies to its south-east, pinning that each of the eight neighbouring cells has
# its own bit in the mask.
TEST_STRING_3 = """##.
.#.
#.."""

from aoc_py.y2022.day23 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "110"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "12"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "21"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "20"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "4"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "4"
