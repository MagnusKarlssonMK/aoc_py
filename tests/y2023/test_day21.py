TEST_STRING = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""

from aoc_py.y2023.day21 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p = InputData(TEST_STRING)
    p1 = p.get_p1(6)
    assert p1 == 16


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "4056"


# ----------- Part 2 ------------

# Test input doesn't have the same geometric symmetry as the real input, i.e. the assumptions made
# in the solution don't apply to the test data
# def test_part2_1() -> None:
#    _, p2 = solve_parts(TEST_STRING, 2)
#    assert p2 == "952408144115"
