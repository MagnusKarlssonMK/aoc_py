TEST_STRING = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

# Home made test to cover items in the rightmost column
TEST_STRING_CUSTOM = """.23+..4.
.......*
11.....7
*.5..+..
3..2..*6"""

from aoc_py.y2023.day03 import solve_parts

# ----------- Part 1 ------------

def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "4361"

def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_CUSTOM, 1)
    assert p1 == "54"


# ----------- Part 2 ------------

def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "467835"

def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_CUSTOM, 2)
    assert p2 == "61"
