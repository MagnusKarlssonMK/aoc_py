TEST_STRING_1 = """turn on 0,0 through 999,999"""

TEST_STRING_2 = """toggle 0,0 through 999,0"""

TEST_STRING_3 = """turn on 0,0 through 999,999
turn off 499,499 through 500,500"""

TEST_STRING_4 = """turn on 0,0 through 0,0"""

TEST_STRING_5 = """toggle 0,0 through 999,999"""

from aoc_py.y2015.day06 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "1000000"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "1000"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "999996"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "1"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_5, 2)
    assert p2 == "2000000"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "999996"
