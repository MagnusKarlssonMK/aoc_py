TEST_STRING_1 = """3,0,4,0,99"""

TEST_STRING_2 = """3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"""

TEST_STRING_3 = """3,9,8,9,10,9,4,9,99,-1,8"""

from aoc_py.y2019.day05 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "1"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "999"


def test_part2_2() -> None:
    # Incorrect input program that doesn't output any value, just to verify decent error handling
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "-1"
