TEST_STRING = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

# Passwords shorter than the requested positions must not count out-of-range positions.
SHORT_PASSWORDS = """1-5 a: ab
3-4 a: ab"""

from aoc_py.y2020.day02 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "2"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "1"


def test_part2_2() -> None:
    _, p2 = solve_parts(SHORT_PASSWORDS, 2)
    assert p2 == "1"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("2", "1")
