TEST_STRING_1 = """/->-\\        \n|   |  /----\\\n| /-+--+-\\  |\n| | |  | v  |\n\\-+-/  \\-+--/\n  \\------/   \n"""

TEST_STRING_2 = """/>-<\\  \n|   |  \n| /<+-\\\n| | | v\n\\>+</ |\n  |   ^\n  \\<->/"""

from aoc_py.y2018.day13 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "7,3"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "6,4"


# ----------- Both parts ------------


def test_vertical_slash_turn() -> None:
    # A cart moving vertically onto "/" takes the rotate_right branch; the
    # "<" and ">" collide at 1,0 on tick 1, leaving the "v"/"^" cart alone.
    assert solve_parts(">-<-\n---/\n---^") == ("1,0", "3,1")


def test_rear_end_collision() -> None:
    # Cart 0 rear-ends cart 1 by moving into its pre-move position, so cart 1
    # is skipped mid-tick via the dead-cart `continue`; cart 3 survives.
    assert solve_parts(">>->-") == ("1,0", "4,0")
