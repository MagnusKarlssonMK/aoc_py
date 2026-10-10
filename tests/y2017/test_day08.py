TEST_STRING = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

# The condition is never true, so no register is ever modified.
TEST_STRING_NOOP = "a inc 1 if b > 0"

# Exercises the <= and != condition operators, which the official example does not use.
TEST_STRING_LE_NE = """b inc 1 if a <= 0
b inc 1 if a != 1"""

from aoc_py.y2017.day08 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "1"


def test_part1_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 1) == ("1", "-1")


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "10"


def test_part2_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 2) == ("-1", "10")


# ----------- Edge cases ------------


def test_no_instruction_executes() -> None:
    assert solve_parts(TEST_STRING_NOOP) == ("0", "0")


def test_remaining_operators() -> None:
    assert solve_parts(TEST_STRING_LE_NE) == ("2", "2")


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("1", "10")
