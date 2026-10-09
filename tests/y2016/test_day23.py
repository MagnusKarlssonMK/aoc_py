TEST_STRING = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a"""

# Multiply loop: rewritten to a 'mul' instruction at runtime.
TEST_STRING_MUL = """cpy 0 a
cpy 3 c
cpy 4 d
inc a
dec c
jnz c -2
dec d
jnz d -5"""

# Addition loops (both orderings): rewritten to an 'add' instruction at runtime.
TEST_STRING_ADD = """cpy 0 a
cpy 5 b
inc a
dec b
jnz b -2"""

TEST_STRING_ADD_REVERSED = """cpy 0 a
cpy 5 b
dec b
inc a
jnz b -2"""

# Plain decrement, not part of any optimizable loop.
TEST_STRING_DEC = """cpy 5 a
dec a"""

# Uses the initial value of 'a' (7 in part 1, 12 in part 2).
TEST_STRING_INC = """inc a"""

from aoc_py.y2016.day23 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "3"


def test_part1_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 1) == ("3", "-1")


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "3"


def test_part2_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 2) == ("-1", "3")


# ----------- Optimizations / runtime ops ------------


def test_mul_optimization() -> None:
    assert solve_parts(TEST_STRING_MUL) == ("12", "12")


def test_add_optimization() -> None:
    assert solve_parts(TEST_STRING_ADD) == ("5", "5")


def test_add_optimization_reversed() -> None:
    assert solve_parts(TEST_STRING_ADD_REVERSED) == ("5", "5")


def test_decrement() -> None:
    assert solve_parts(TEST_STRING_DEC) == ("4", "4")


def test_initial_a_per_part() -> None:
    assert solve_parts(TEST_STRING_INC) == ("8", "13")


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("3", "3")
