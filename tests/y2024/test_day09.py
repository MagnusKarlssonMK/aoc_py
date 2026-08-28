TEST_STRING = """2333133121414131402"""

from aoc_py.y2024.day09 import solve_parts

# ----------- Part 1 ------------

def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "1928"


# ----------- Part 2 ------------

def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "2858"
