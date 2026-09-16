TEST_STRING = """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""

from aoc_py.y2015.day18 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "4"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    # Note: only run 4 steps like in part 1 to keep it simple
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "14"
