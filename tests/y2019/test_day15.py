# Hand-crafted Intcode programs for day 15 (no test program given by puzzle). Each program tracks
# the virtual droid in its own registers and answers every movement command with the status of the
# maze cell being probed, read from a baked tile array. TEST_STRING_3 is a linear transcript program
# that replays the exact probe/response sequence and then halts.
TEST_STRING_1 = """3,111,1008,111,1,119,1005,119,34,1008,111,2,120,1005,120,45,1008,111,3,121,1005,121,56,1001,112,1,114,1001,113,0,115,1105,1,67,1001,112,0,114,1001,113,-1,115,1105,1,67,1001,112,0,114,1001,113,1,115,1105,1,67,1001,112,-1,114,1001,113,0,115,1105,1,67,1001,114,1,116,1001,115,1,117,1002,117,5,117,1,116,117,116,101,125,116,88,1,88,123,118,4,118,1008,118,0,122,1005,122,108,1001,114,0,112,1001,115,0,113,1105,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,125,0,0,0,0,0,0,1,1,1,0,0,1,0,2,0,0,0,0,0,0"""

TEST_STRING_2 = """3,111,1008,111,1,119,1005,119,34,1008,111,2,120,1005,120,45,1008,111,3,121,1005,121,56,1001,112,1,114,1001,113,0,115,1105,1,67,1001,112,0,114,1001,113,-1,115,1105,1,67,1001,112,0,114,1001,113,1,115,1105,1,67,1001,112,-1,114,1001,113,0,115,1105,1,67,1001,114,1,116,1001,115,1,117,1002,117,4,117,1,116,117,116,101,125,116,88,1,88,123,118,4,118,1008,118,0,122,1005,122,108,1001,114,0,112,1001,115,0,113,1105,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,125,0,0,0,0,0,1,1,0,0,1,1,0,0,1,2,0,0,0,0,0"""

TEST_STRING_3 = """3,29,104,0,3,29,104,0,3,29,104,0,3,29,104,1,3,29,104,0,3,29,104,0,3,29,104,0,99,0"""

from aoc_py.y2019.day15 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "3"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "3"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "-1"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "4"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "3"
