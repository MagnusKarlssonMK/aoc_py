TEST_STRING = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

# The only integer solution is i = -1, j = 4 (negative presses), so the machine
# cannot be won and must score 0.
TEST_STRING_2 = """Button A: X+1, Y+2
Button B: X+2, Y+1
Prize: X=7, Y=2"""

from aoc_py.y2024.day13 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "480"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "875318608908"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("480", "875318608908")


def test_negative_presses() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "0"
