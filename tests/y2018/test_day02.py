TEST_STRING_1 = """abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab"""

TEST_STRING_2 = """abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz"""

from aoc_py.y2018.day02 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "12"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "fgij"
