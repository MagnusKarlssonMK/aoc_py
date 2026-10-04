TEST_STRING_1 = """turn on 0,0 through 999,999"""

TEST_STRING_2 = """toggle 0,0 through 999,0"""

TEST_STRING_3 = """turn on 0,0 through 999,999
turn off 499,499 through 500,500"""

TEST_STRING_4 = """turn on 0,0 through 0,0"""

TEST_STRING_5 = """toggle 0,0 through 999,999"""

# Part 1 assigns the whole region when turning on rather than adding to it, so toggling a region first and turning
# it on afterwards must still leave it fully lit. Adding to whatever was there would count twice as many lights.
TEST_STRING_6 = """toggle 0,0 through 999,999
turn on 0,0 through 999,999"""

# Turning off a region that was never lit has to leave it at zero, and not run into negative brightness, which is
# what the clip after the decrement is there to stop.
TEST_STRING_7 = """turn off 0,0 through 999,999"""

# Toggling the same region twice has to return it to unlit, which is what the modulo after the increment is for.
# Letting the count run free instead would report a million lights on, and taking the remainder three would too.
TEST_STRING_8 = """toggle 0,0 through 999,999
toggle 0,0 through 999,999"""

# Brightness can go past one, so this tells a decrement of one apart from a decrement of two: each light here is
# turned on twice, to brightness two, and turning it off must leave it at one.
TEST_STRING_9 = """turn on 0,0 through 999,999
turn on 0,0 through 999,999
turn off 0,0 through 999,999"""

# A single row away from the diagonal. Every other input here is square, or offset equally in both directions, so
# none of them can tell the two coordinates of the far corner apart once they are read the wrong way round.
TEST_STRING_10 = """turn on 0,5 through 999,5"""

from aoc_py.y2015.day06 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "1000000"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "1000"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "999996"


def test_part1_6() -> None:
    p1, _ = solve_parts(TEST_STRING_6, 1)
    assert p1 == "1000000"


def test_part1_8() -> None:
    p1, _ = solve_parts(TEST_STRING_8, 1)
    assert p1 == "0"


def test_part1_10() -> None:
    p1, _ = solve_parts(TEST_STRING_10, 1)
    assert p1 == "1000"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "1"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_5, 2)
    assert p2 == "2000000"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "999996"


def test_part2_6() -> None:
    _, p2 = solve_parts(TEST_STRING_6, 2)
    assert p2 == "3000000"


def test_part2_7() -> None:
    _, p2 = solve_parts(TEST_STRING_7, 2)
    assert p2 == "0"


def test_part2_8() -> None:
    _, p2 = solve_parts(TEST_STRING_8, 2)
    assert p2 == "4000000"


def test_part2_9() -> None:
    _, p2 = solve_parts(TEST_STRING_9, 2)
    assert p2 == "1000000"


# ----------- Both parts ------------

# Passing no part computes both, which is the documented default but is otherwise never exercised. This input makes
# the two models visible side by side: the same toggle leaves 1000 lights lit but 2000 total brightness.


def test_both_2() -> None:
    assert solve_parts(TEST_STRING_2) == ("1000", "2000")
