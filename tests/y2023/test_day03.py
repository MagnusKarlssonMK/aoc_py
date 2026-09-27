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

# A part that ends in the rightmost column of a row, to cover the end-of-row branch of the parser.
TEST_STRING_2 = """.23+..4.
.......*
11.....7
*.5..+..
3..2..*6"""

# Both stars touch the one and only part 123, so neither of them is a gear, and the part itself is counted once
# even though it touches two symbols.
TEST_STRING_3 = """.*.
123
.*."""

from aoc_py.y2023.day03 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "4361"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "54"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "123"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "467835"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "61"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "0"
