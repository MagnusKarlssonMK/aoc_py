TEST_STRING = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""

from aoc_py.y2021.day23 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "12521"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "44169"
