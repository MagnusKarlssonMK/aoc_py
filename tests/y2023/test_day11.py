TEST_STRING = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

from aoc_py.y2023.day11 import InputData, solve_parts

# ----------- Part 1 ------------

def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "374"

# ----------- Part 2 ------------

def test_part2_1() -> None:
    p = InputData(TEST_STRING)
    _, p2 = p.get_distance_sum(2, 100)
    assert p2 == 8410

def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "82000210" # Answer not given by input. Just to test the real solver
