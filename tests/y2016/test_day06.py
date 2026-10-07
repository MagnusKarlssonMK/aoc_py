TEST_STRING = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""

from aoc_py.y2016.day06 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "easter"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "advent"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("easter", "advent")


def test_tie() -> None:
    # Column 0 has a clear winner (a:3, b:1), column 1 ties a and b two each, column 2 ties a and b at one each
    # under c's two, and columns 3/4 are distinct again. Every tie goes to the character seen first in that
    # column, so the parts are "aacdf" / "baaeg" -- and they differ, so mixing the parts up cannot pass.
    grid = """aacdf
abadf
aacdg
bbbef"""
    assert solve_parts(grid) == ("aacdf", "baaeg")
