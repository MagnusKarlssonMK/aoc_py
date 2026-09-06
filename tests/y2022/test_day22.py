# Some use of \n to prevent editor from shaving off spaces
TEST_STRING = """        ...#\n        .#..\n        #...\n        ....
...#.......#
........#...
..#....#....
..........#.\n        ...#....\n        .....#..\n        .#......\n        ......#.

10R5L5R10L4R5L5"""

from aoc_py.y2022.day22 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "6032"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "5031"
