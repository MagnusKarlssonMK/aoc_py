TEST_STRING_1 = """abcdefgh"""

TEST_STRING_2 = """ghijklmn"""

TEST_STRING_3 = """zzzzz"""

TEST_STRING_4 = """zzzz"""

TEST_STRING_5 = """aabcck"""

TEST_STRING_6 = """zzzzzzzy"""

from aoc_py.y2015.day11 import solve_parts

# ----------- Part 1 and 2 --------


def test_parts_1() -> None:
    p1, p2 = solve_parts(TEST_STRING_1)
    assert p1 == "abcdffaa"
    assert p2 == "abcdffbb"


def test_parts_2() -> None:
    p1, p2 = solve_parts(TEST_STRING_2)
    assert p1 == "ghjaabcc"
    assert p2 == "ghjbbcdd"


# Five z's wrap the increment back down to the start of the alphabet, which is the only way the base case of
# get_next_password is reached: the search has to carry all the way out of the last position. Five is also exactly
# MIN_LENGTH, since aabcc is the shortest password the rules admit.
def test_parts_3() -> None:
    p1, p2 = solve_parts(TEST_STRING_3)
    assert p1 == "aabcc"
    assert p2 == "bbcdd"


# Four characters cannot hold a straight of three and two doubled pairs at once, so there is no answer to find and the
# search would otherwise wrap past the end of the space and never come back.
def test_parts_4() -> None:
    p1, p2 = solve_parts(TEST_STRING_4)
    assert p1 == "-1"
    assert p2 == "-1"


# Already a valid password, so part 1 hands the input straight back. What it really pins is part 2: the next answer is
# aabccm, which means the increment stepped over aabccl. That string satisfies every other rule, so a solver that
# stopped treating l as forbidden, or that skipped two letters instead of one when stepping over a forbidden one,
# would return it here instead.
def test_parts_5() -> None:
    p1, p2 = solve_parts(TEST_STRING_5)
    assert p1 == "aabcck"
    assert p2 == "aabccm"


# Part filters, which no other test here exercises since they all ask for both answers at once.
def test_part1_5() -> None:
    p1, _ = solve_parts(TEST_STRING_5, 1)
    assert p1 == "aabcck"


def test_part2_5() -> None:
    _, p2 = solve_parts(TEST_STRING_5, 2)
    assert p2 == "aabccm"


# Seven z's and a y, so the search has to carry out of the last position. A RANGE one too high stops the carry from
# ever happening and lets the sequence run past z into punctuation, which is how this catches that off-by-one.
def test_parts_6() -> None:
    p1, p2 = solve_parts(TEST_STRING_6)
    assert p1 == "aaaaabcc"
    assert p2 == "aaaabbcd"
