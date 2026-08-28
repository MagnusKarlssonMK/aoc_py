TEST_STRING = """3   4
4   3
2   5
1   3
3   9
3   3"""

from aoc_py.y2024.day01 import solve_parts

# ----------- Part 1 ------------

def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "11"

# ----------- Part 2 ------------

def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "31"
