TEST_STRING = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

from aoc_py.y2022.day01 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "24000"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "45000"
