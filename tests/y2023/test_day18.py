TEST_STRING_1 = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

# A single square, whose trench is 2x2 lattice points. The colour encodes the same step and
# direction as the rest of the line, so both parts dig out the same trench.
TEST_STRING_2 = """R 1 (#000010)
D 1 (#000011)
L 1 (#000012)
U 1 (#000013)"""

# A 3x3 square, whose trench is 4x4 lattice points.
TEST_STRING_3 = """R 3 (#000030)
D 3 (#000031)
L 3 (#000032)
U 3 (#000033)"""

# A 1x5 bar, whose trench is 2x6 lattice points.
TEST_STRING_4 = """R 5 (#000050)
D 1 (#000011)
L 5 (#000052)
U 1 (#000013)"""

from aoc_py.y2023.day18 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "62"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "4"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "16"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "12"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "952408144115"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "4"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "16"


def test_part2_4() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "12"
