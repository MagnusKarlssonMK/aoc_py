TEST_STRING = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

from aoc_py.y2025.day01 import solve_parts

# ----------- Part 1 ------------

def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "3"


# ----------- Part 2 ------------

def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "6"
