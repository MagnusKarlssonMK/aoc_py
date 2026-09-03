TEST_STRING_1 = """AAAA
BBCD
BBCC
EEEC"""

TEST_STRING_2 = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""

TEST_STRING_3 = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

TEST_STRING_4 = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""

TEST_STRING_5 = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""

from aoc_py.y2024.day12 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "140"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "772"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "1930"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "80"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "236"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_5, 2)
    assert p2 == "368"
