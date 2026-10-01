TEST_STRING_1 = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

# A narrow corridor where an obstacle placed directly in front of the guard,
# or on the last cell before a wall, is what decides whether the guard loops.
TEST_STRING_2 = """..#.......
..#.......
..#.......
..#.......
..#.......
..#.......
..^.####..
##########"""

from aoc_py.y2024.day06 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "41"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "6"


def test_part2_2() -> None:
    # The blocked range must be half-open. A strict range on both
    # ends lets the guard run past an obstacle directly in front of it.
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "1"
