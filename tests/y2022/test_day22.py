# Some use of \n to prevent editor from shaving off spaces
TEST_STRING_1 = """        ...#\n        .#..\n        #...\n        ....
...#.......#
........#...
..#....#....
..........#.\n        ...#....\n        .....#..\n        .#......\n        ......#.

10R5L5R10L4R5L5"""

# A tall (4x3) cube net, the same shape as the real input, with face size 2. The path exercises the vertical net
# orientation, the Part 1 wrap around a lone face in a row/column, and several cube seams.
TEST_STRING_2 = """  ....
  ....
  ..  \n  ..  \n....  \n....  \n..    \n..    \n
2R2L4R3L6R2L5R1L1L1"""

from aoc_py.y2022.day22 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "6032"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "8007"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "5031"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "8007"
