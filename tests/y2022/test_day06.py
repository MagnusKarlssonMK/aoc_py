TEST_STRING_1 = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
TEST_STRING_2 = """bvwbjplbgvbhsrlpgdmjqwftvncz"""
TEST_STRING_3 = """nppdvjthqldpwncqszvftbrmjlhg"""
TEST_STRING_4 = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""
TEST_STRING_5 = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""

from aoc_py.y2022.day06 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "7"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "5"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "6"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "10"


def test_part1_5() -> None:
    p1, _ = solve_parts(TEST_STRING_5, 1)
    assert p1 == "11"


def test_part1_6() -> None:
    p1, _ = solve_parts("", 1)
    # Just for code coverage for when no solution exists
    assert p1 == "-1"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "19"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "23"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "23"


def test_part2_4() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "29"


def test_part2_5() -> None:
    _, p2 = solve_parts(TEST_STRING_5, 2)
    assert p2 == "26"
