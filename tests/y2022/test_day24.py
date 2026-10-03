TEST_STRING_1 = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""

# The puzzle description's blizzard-movement illustration, with independently calculated expected answer.
# (Anwer not given in description text).
TEST_STRING_2 = """#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#"""

# A map where cheating along the top wall row would shorten a leg, and where the wrong de-duplication period would prune a
# needed state; it pins both the interior boundary and the lcm(width, height) period. The expected 9 / 29 were verified
# with an independent BFS.
TEST_STRING_3 = """##.###
#....#
#..^<#
#..^v#
####.#"""

# A 1x1 interior whose only cell is permanently occupied by a downward blizzard, so the exit can never be reached.
UNSOLVABLE = """#.#
#v#
#.#"""

# A map whose first leg is solvable but whose return leg is not, so the whole crossing is unreachable and both parts report
# -1.
PARTIAL_UNSOLVABLE = """###.#
#<^.#
#><v#
##.##"""

from aoc_py.y2022.day24 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "18"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "10"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "9"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "54"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "30"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "29"


# ----------- Unreachable ------------


def test_unreachable_exit() -> None:
    assert solve_parts(UNSOLVABLE) == ("-1", "-1")


def test_partially_unreachable_crossing() -> None:
    assert solve_parts(PARTIAL_UNSOLVABLE) == ("-1", "-1")
