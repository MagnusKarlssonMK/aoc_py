TEST_STRING = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

from aoc_py.y2020.day02 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "2"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "1"
