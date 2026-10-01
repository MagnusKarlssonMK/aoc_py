TEST_STRING_1 = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
TEST_STRING_2 = """bvwbjplbgvbhsrlpgdmjqwftvncz"""
TEST_STRING_3 = """nppdvjthqldpwncqszvftbrmjlhg"""
TEST_STRING_4 = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""
TEST_STRING_5 = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""
TEST_STRING_6 = "abcabcd"
TEST_STRING_7 = "abcdefghijklm\n"

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
    p1, _ = solve_parts(TEST_STRING_6, 1)
    assert p1 == "7"


def test_part1_7() -> None:
    p1, _ = solve_parts(TEST_STRING_7, 1)
    assert p1 == "4"


def test_part1_8() -> None:
    p1, _ = solve_parts("", 1)
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


def test_part2_6() -> None:
    # The only case where part 2 has no 14-character window to find.
    _, p2 = solve_parts(TEST_STRING_6, 2)
    assert p2 == "-1"


def test_part2_7() -> None:
    _, p2 = solve_parts(TEST_STRING_7, 2)
    assert p2 == "14"


def test_part2_8() -> None:
    _, p2 = solve_parts("", 2)
    assert p2 == "-1"
