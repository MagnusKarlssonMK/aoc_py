# Custom made small input, since the problem description doesn't provide any
TEST_STRING_1 = """120"""

TEST_STRING_2 = """150"""

# The house list is bounded by elf 1 alone, so a target that does not divide evenly by the gift is
# where that rounding shows up: 11 gives an answer of 2 rather than 1, since house 1 receives only
# 10 from elf 1 and stays short.
TEST_STRING_3 = """11"""

# Same rounding in part 2, whose gift is 11: 21 is not a multiple of it either.
TEST_STRING_4 = """21"""

# Part 1 reaches 311 first at house 18, and 18 is 2 * 3**2, so it is the cheapest input covering
# both halves of the sigma rebuild: a repeated prime factor that is not two, raised above the
# first power.
TEST_STRING_5 = """311"""

# House 300 is elf 6's fiftieth stop, so house 300 collects 66 more presents under a cap of fifty
# than under a cap of forty-nine, which lifts it from 9317 to 9383. The target sits at 9318, one
# present above the first total and one below the second, so this input pins the cap from below.
TEST_STRING_6 = """9318"""

# House 6120 is elf 120's fifty-first stop, so under a cap of fifty-one it collects 1320 more and
# reaches 222123, while under a cap of fifty it stalls at 220803. This target is 220804, again one
# present past the capped total, which pins the cap from above. Dropping the cap altogether would
# instead bring the answer forward to house 5880, so this input pins the cap's existence too.
TEST_STRING_7 = """220804"""

# Degenerate target: both house bounds round down to no houses at all, so there is nothing to scan
# and the sentinel comes back rather than an answer below the real ones.
TEST_STRING_8 = """0"""

from aoc_py.y2015.day20 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "6"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "8"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "2"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "2"


def test_part1_5() -> None:
    p1, _ = solve_parts(TEST_STRING_5, 1)
    assert p1 == "18"


def test_part1_6() -> None:
    p1, _ = solve_parts(TEST_STRING_6, 1)
    assert p1 == "336"


def test_part1_7() -> None:
    p1, _ = solve_parts(TEST_STRING_7, 1)
    assert p1 == "6300"


def test_part1_8() -> None:
    p1, _ = solve_parts(TEST_STRING_8, 1)
    assert p1 == "-1"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "6"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "8"


# Part 2's answer here is house 1, where only elf 1 ever delivers, so this is the input that pins
# part 2's gift to eleven presents rather than ten.
def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "1"


def test_part2_4() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "2"


def test_part2_5() -> None:
    _, p2 = solve_parts(TEST_STRING_5, 2)
    assert p2 == "16"


def test_part2_6() -> None:
    _, p2 = solve_parts(TEST_STRING_6, 2)
    assert p2 == "300"


def test_part2_7() -> None:
    _, p2 = solve_parts(TEST_STRING_7, 2)
    assert p2 == "6240"


def test_part2_8() -> None:
    _, p2 = solve_parts(TEST_STRING_8, 2)
    assert p2 == "-1"


# ----------- Both parts at once ------------


# This is the shape the runner itself uses.
def test_both_1() -> None:
    p1, p2 = solve_parts(TEST_STRING_1)
    assert p1 == "6"
    assert p2 == "6"


def test_both_2() -> None:
    p1, p2 = solve_parts(TEST_STRING_2)
    assert p1 == "8"
    assert p2 == "8"


def test_both_7() -> None:
    p1, p2 = solve_parts(TEST_STRING_7)
    assert p1 == "6300"
    assert p2 == "6240"
