# Note: need to add extra backslash in a python string, or a single backslash
# itself will be treated as an escape character
#
# The five quote characters after the equals sign look like a typo. They are not: the first two of them open the empty
# string literal that is the puzzle's own first example, so these are all four of its examples, in order.
TEST_STRING_1 = """""
"abc"
"aaa\\"aaa"
"\\x27"
"""

# The puzzle states that only three escapes ever occur, so \t here is out of spec. It should still be measured as two
# characters standing for one, saving 1 rather than the 3 that \xNN saves.
TEST_STRING_2 = '"a\\tb"'

# An escaped backslash followed by x27. The pair has to be consumed together, leaving the x27 as literal text rather
# than a hexadecimal escape, so the line saves exactly 1. Reading the second backslash as the start of a fresh escape
# would save 2 instead.
TEST_STRING_3 = '"\\\\x27"'

# A hexadecimal escape sitting directly in front of another escape. The scan has to stop right after the two hex
# digits: stepping one further lands on the backslash that begins the second escape and swallows it, which costs a
# character here. A doubled backslash instead of an escaped quote would not show this, since re-reading it still
# scores the same one.
TEST_STRING_4 = '"\\x27\\""'


from aoc_py.y2015.day08 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "12"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "3"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "3"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "6"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "19"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "5"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "6"


def test_part2_4() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "7"
