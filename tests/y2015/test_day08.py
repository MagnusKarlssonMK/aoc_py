# Note: need to add extra backslash in a python string, or a single backslash
# itself will be treated as an escape character
TEST_STRING = """""
"abc"
"aaa\\"aaa"
"\\x27"
"""


from aoc_py.y2015.day08 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "12"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "19"
