TEST_STRING_1 = """1, 0, 0, 0,
2, 32, 0, 0,
2, 33, 1, 1,
2, 34, 2, 2,
1, 35, 0, 0,
1, 1, 0, 0,
1, 2, 0, 0,
99, 0, 0, 0,
0, 1000000, 10000, 7350720,
0, 0, 0, 0,
0, 0, 0, 0,
0, 0, 0, 0,
0, 0, 0, 0,
0, 0, 0, 0,
0, 0, 0, 0,
0, 0, 0, 0,
0, 0, 0, 0,
0, 0, 0, 0,
0, 0, 0, 0,
0, 0, 0, 0,
0, 0, 0, 0,
0, 0, 0, 0,
0, 0, 0, 0,
0, 0, 0, 0,
0, 0, 0, 0"""

from aoc_py.y2019.day02 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "19370720"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "1234"


def test_part2_2() -> None:
    _, p2 = solve_parts("99", 2)  # never produces the target output
    assert p2 == "-1"
