TEST_STRING = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

# Swapping the first nop/jmp completes the program, so the repair must start from a clean
# accumulator rather than reusing the value left over from part 1.
RESET_STRING = """jmp +1
acc +5
acc +6"""

# No nop/jmp to swap, so the program can never be repaired.
NO_SOLUTION_STRING = """acc +1
acc +2"""

from aoc_py.y2020.day08 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "5"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "8"


def test_part2_2() -> None:
    _, p2 = solve_parts(NO_SOLUTION_STRING, 2)
    assert p2 == "-1"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(RESET_STRING) == ("11", "11")
