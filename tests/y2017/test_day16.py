TEST_STRING = """s1,x3/4,pe/b"""

from aoc_py.y2017.day16 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "paedcbfghijklmno"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "ghidjklmnopabcef"
