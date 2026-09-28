TEST_STRING = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
........
.......#..
#...#....."""

from aoc_py.y2023.day11 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "374"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "82000210"  # Answer not given by input. Just to test the real solver


# The two official part 2 examples, which use an expansion factor of 10 and 100 instead of 1000000.
def test_part2_2() -> None:
    assert InputData(TEST_STRING).get_distance_sum(10) == 1030


def test_part2_3() -> None:
    assert InputData(TEST_STRING).get_distance_sum(100) == 8410
