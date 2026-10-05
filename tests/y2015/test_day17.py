TEST_STRING_1 = """20
15
10
5
5"""

# Nothing here comes to the target of 25, so neither part has an answer to give. The containers are
# kept small on purpose: an input summing to 150 or more is solved for the real target of 150.
TEST_STRING_2 = """1
2"""

# Exactly one combination reaches the target, so part 1 and part 2 both answer 1. That distinguishes
# "counted the one match" from "counted every combination of any size" and from counting the sizes
# rather than the combinations.
TEST_STRING_3 = """10
10
5"""

TEST_STRING_4 = ""

# One container that is itself the target, and the only test input whose containers sum to exactly
# 150. That makes it the only one that reaches the real target rather than the fallback of 25, and
# the sum sitting on the boundary is the point: it is what distinguishes "at least 150" from
# "more than 150". It is also the only input where a single container is a combination in its own
# right, so it is what catches a scan that skips the smallest size.
TEST_STRING_5 = "150"

from aoc_py.y2015.day17 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "4"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "-1"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "1"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_5, 1)
    assert p1 == "1"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "3"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "-1"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "1"


def test_part2_4() -> None:
    _, p2 = solve_parts(TEST_STRING_5, 2)
    assert p2 == "1"


# ----------- Both parts at once ------------


# Every other test here asks for one part at a time. This is the shape the runner itself uses.
def test_both_1() -> None:
    p1, p2 = solve_parts(TEST_STRING_1)
    assert p1 == "4"
    assert p2 == "3"


# No containers at all, so there is nothing to combine.
def test_both_2() -> None:
    p1, p2 = solve_parts(TEST_STRING_4)
    assert p1 == "-1"
    assert p2 == "-1"


# ----------- Part 2 standing on its own -----------


# Part 2 must not depend on part 1 having run first. solve_parts hides that dependency by asking for
# part 1 up front, so only reaching for the class directly can show whether it is really gone. This
# is the one test here that fails against the order-dependent version, which answered 0.
def test_p2_without_part1() -> None:
    assert InputData(TEST_STRING_1).get_p2() == 3
