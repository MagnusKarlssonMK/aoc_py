TEST_STRING_1 = """abcdefgh"""

TEST_STRING_2 = """ghijklmn"""

from aoc_py.y2015.day11 import solve_parts

# ----------- Part 1 and 2 --------


def test_parts_1() -> None:
    p1, p2 = solve_parts(TEST_STRING_1)
    assert p1 == "abcdffaa"
    assert p2 == "abcdffbb"


def test_parts_2() -> None:
    p1, p2 = solve_parts(TEST_STRING_2)
    assert p1 == "ghjaabcc"
    assert p2 == "ghjbbcdd"
