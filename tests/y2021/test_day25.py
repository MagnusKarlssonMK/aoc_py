TEST_STRING = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""

from aoc_py.y2021.day25 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "58"


# ----------- Part 2 ------------


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING, 2)
    assert p1 == "-"
