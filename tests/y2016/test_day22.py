TEST_STRING = """Filesystem            Size  Used  Avail  Use%
/dev/grid/node-x0-y0   10T    8T     2T   80%
/dev/grid/node-x0-y1   11T    6T     5T   54%
/dev/grid/node-x0-y2   32T   28T     4T   87%
/dev/grid/node-x1-y0    9T    7T     2T   77%
/dev/grid/node-x1-y1    8T    0T     8T    0%
/dev/grid/node-x1-y2   11T    7T     4T   63%
/dev/grid/node-x2-y0   10T    6T     4T   60%
/dev/grid/node-x2-y1    9T    8T     1T   88%
/dev/grid/node-x2-y2    9T    6T     3T   66%"""

# 2x2 grid: 3 valid transfers (hand-checked).
TEST_STRING_SMALL = """Filesystem Size Used Avail Use%
/dev/grid/node-x0-y0   10T    8T     2T   80%
/dev/grid/node-x0-y1   11T    0T    11T    0%
/dev/grid/node-x1-y0   10T    6T     4T   60%
/dev/grid/node-x1-y1   10T    5T     5T   50%"""

# 3x3 grid with a wall at (1,1); the empty node at (0,2) must go up then right to reach G at (2,0).
TEST_STRING_WALL = """Filesystem Size Used Avail Use%
/dev/grid/node-x0-y0   10T    1T     9T   10%
/dev/grid/node-x1-y0   10T    1T     9T   10%
/dev/grid/node-x2-y0   10T    5T     5T   50%
/dev/grid/node-x0-y1   10T    1T     9T   10%
/dev/grid/node-x1-y1   10T   99T     0T  990%
/dev/grid/node-x2-y1   10T    1T     9T   10%
/dev/grid/node-x0-y2   10T    0T    10T    0%
/dev/grid/node-x1-y2   10T    1T     9T   10%
/dev/grid/node-x2-y2   10T    1T     9T   10%"""

from aoc_py.y2016.day22 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "7"


def test_part1_small_grid() -> None:
    assert InputData(TEST_STRING_SMALL).get_p1() == 3


def test_part1_wall_grid() -> None:
    assert InputData(TEST_STRING_WALL).get_p1() == 28


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "7"


def test_part2_wall_detour() -> None:
    # BFS: (0,2) -> (0,1) -> (0,0) -> (1,0) -> (2,0) = 4 steps, plus 5 * (max_x - 1) = 5.
    assert InputData(TEST_STRING_WALL).get_p2() == 9


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("7", "7")


def test_part1_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 1) == ("7", "-1")


def test_part2_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 2) == ("-1", "7")
