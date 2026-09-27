# Intcode programs for the arcade cabinet: each output triple is (x, y, tile id). Part 2 programs are
# padded with a harmless multiply head because get_p2 overwrites memory position 0 with 2 coins.
TEST_STRING_1 = """104,1,104,2,104,0,104,3,104,4,104,1,104,5,104,6,104,2,104,7,104,8,104,3,104,9,104,10,104,4,104,11,104,12,104,2,3,0,99"""

TEST_STRING_2 = """104,0,104,1,104,2,104,2,104,3,104,4,99"""

TEST_STRING_3 = """2,0,0,999,104,5,104,1,104,4,104,3,104,2,104,3,3,0,104,-1,104,0,104,10,104,2,104,1,104,4,104,5,104,2,104,3,3,0,104,-1,104,0,104,20,104,4,104,1,104,4,104,4,104,2,104,3,3,0,104,-1,104,0,104,30,99"""

TEST_STRING_4 = """2,0,0,999,104,-1,104,0,104,123,99"""

from aoc_py.y2019.day13 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "2"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "1"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "30"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "123"
