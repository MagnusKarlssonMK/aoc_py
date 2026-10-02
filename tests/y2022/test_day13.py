TEST_STRING_1 = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

# Pairs 1 and 4 compare equal, and the spec says an equal pair is neither left nor right, so
# only pair 2 counts toward part 1. Pair 3 also hands part 2 a packet, [2], that is equal to the
# first divider, so the sort has to keep the two apart for the divider positions to come out right.
TEST_STRING_2 = """[1,2]
[1,2]

[1,1]
[1,2]

[2]
[1,1]

[]
[]"""

from aoc_py.y2022.day13 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "13"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "2"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "140"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "90"
