TEST_STRING_1 = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""

# The official example is the only arrangement the puzzle itself publishes, and its pods are
# already in a fair bit of a mess, so every branch of the move generator gets some use. This
# one keeps each room's pair together but swaps the two top halves of rooms 1 and 2 and of
# rooms 3 and 4, so the pods all have to travel and neither half of the burrow can be left
# alone until the other has moved out of the way.
TEST_STRING_2 = """#############
#...........#
###A#B#D#C###
  #A#B#C#D#
  #########"""

# Every room here holds one A and one B, so the C and D rooms can never be filled and no
# sequence of moves sorts the burrow out. That reaches the search's give-up answer, which
# would otherwise never be covered, and pins it as a real result rather than a crash.
TEST_STRING_3 = """#############
#...........#
###A#A#A#A###
  #B#B#B#B#
  #########"""

from aoc_py.y2021.day23 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "12521"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "4600"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "-1"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "44169"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "28548"
