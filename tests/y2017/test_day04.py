TEST_STRING_1 = """aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa"""

TEST_STRING_2 = """abcde fghij
abcde xyz ecdab
a ab abc abd abf abj
iiii oiii ooii oooi oooo
oiii ioii iioi iiio"""

from aoc_py.y2017.day04 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "2"


def test_part1_solve_parts() -> None:
    assert solve_parts(TEST_STRING_1, 1) == ("2", "-1")


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "3"


def test_part2_solve_parts() -> None:
    assert solve_parts(TEST_STRING_2, 2) == ("-1", "3")


# ----------- Edge cases ------------


def test_anagram_only() -> None:
    assert solve_parts("abc cba") == ("1", "0")


def test_duplicate_word() -> None:
    assert solve_parts("aa aa") == ("0", "0")


def test_empty_input() -> None:
    assert solve_parts("") == ("0", "0")


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING_2) == ("5", "3")
