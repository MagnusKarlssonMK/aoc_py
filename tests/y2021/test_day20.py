TEST_STRING_1 = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""

# The official example's algorithm starts with a dark pixel, so its void never lights up and the boundary
# handling is never exercised with a lit void. This algorithm lights a pixel when an even number of the nine
# pixels in its 3x3 neighbourhood are lit, which makes the first entry lit and the last one dark, so the void
# alternates on every step just like it does for the real input.
TEST_STRING_2 = """#..#.##..##.#..#.##.#..##..#.##..##.#..##..#.##.#..#.##..##.#..#.##.#..##..#.##.#..#.##..##.#..##..#.##..##.#..#.##.#..##..#.##..##.#..##..#.##.#..#.##..##.#..##..#.##..##.#..#.##.#..##..#.##.#..#.##..##.#..#.##.#..##..#.##..##.#..##..#.##.#..#.##..##.#..#.##.#..##..#.##.#..#.##..##.#..##..#.##..##.#..#.##.#..##..#.##.#..#.##..##.#..#.##.#..##..#.##..##.#..##..#.##.#..#.##..##.#..##..#.##..##.#..#.##.#..##..#.##..##.#..##..#.##.#..#.##..##.#..#.##.#..##..#.##.#..#.##..##.#..##..#.##..##.#..#.##.#..##..#.##.

#.#.#.#.#.
.#.#.#.#.#
#.#.#.#.#.
.#.#.#.#.#
#.#.#.#.#.
.#.#.#.#.#
#.#.#.#.#.
.#.#.#.#.#
#.#.#.#.#.
.#.#.#.#.#"""

from aoc_py.y2021.day20 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "35"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "50"


def test_part1_3() -> None:
    p = InputData(TEST_STRING_1)
    assert p.run_steps()[0] == 35
    assert p.run_steps()[0] == 35


def test_part1_4() -> None:
    p = InputData(TEST_STRING_2)
    assert p.run_steps()[0] == 50
    assert p.run_steps()[0] == 50


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "3351"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "1250"


def test_part2_3() -> None:
    p = InputData(TEST_STRING_1)
    assert p.run_steps()[1] == 3351
    assert p.run_steps()[1] == 3351


def test_part2_4() -> None:
    p = InputData(TEST_STRING_2)
    assert p.run_steps()[1] == 1250
    assert p.run_steps()[1] == 1250
