TEST_STRING_1 = """5 1 9 5
7 5 3
2 4 6 8"""

TEST_STRING_2 = """5 9 2 8
9 4 7 3
3 8 6 5"""

from aoc_py.y2017.day02 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "18"


def test_part1_solve_parts() -> None:
    assert solve_parts(TEST_STRING_1, 1) == ("18", "-1")


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "9"


def test_part2_solve_parts() -> None:
    assert solve_parts(TEST_STRING_2, 2) == ("-1", "9")


# ----------- Edge cases ------------


def test_row_without_divisible_pair() -> None:
    # Row "7 5 3" has no evenly divisible pair and must contribute 0 to part 2.
    assert solve_parts(TEST_STRING_1) == ("18", "7")


def test_non_adjacent_divisible_pair() -> None:
    # The valid pair (3, 9) is not adjacent after sorting, so combinations must find it.
    assert solve_parts("2 3 9") == ("7", "3")


def test_duplicate_values() -> None:
    assert solve_parts("5 5") == ("0", "1")


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING_2) == ("18", "9")
