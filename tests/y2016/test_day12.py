TEST_STRING = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""

# Programs to exercise the optimization blocks and runtime MUL/ADD execution.
MUL_OPT = """cpy 2 b
cpy 3 c
inc a
dec b
jnz b -2
dec c
jnz c -5"""

ADD_INC_DEC = """cpy 5 b
inc a
dec b
jnz b -2"""

ADD_DEC_INC = """cpy 3 b
dec b
inc a
jnz b -2"""

NO_MATCH_JNZ_OFF = """cpy 2 b
inc a
dec b
jnz b -3"""

NO_MATCH_ARG_MISMATCH = """cpy 2 b
cpy 1 c
inc a
dec b
jnz c -2
dec c
jnz c -5"""

from aoc_py.y2016.day12 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "42"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "42"


# ----------- Optimization coverage ------------


def test_mul_optimization() -> None:
    # 2*b + 3*c added to a: 2*2+3*3=13, with initial c unused? Wait: in our test, c starts at 0,
    # but the pattern is dec c then jnz c -5; better to set c appropriately.
    # Let's write: cpy 2 c then run the standard mul pattern with b=3, c=2: inc a; dec b; jnz b -2 (adds b to a, clears b); dec c; jnz c -5 (repeats)
    s = """cpy 2 c
cpy 3 b
inc a
dec b
jnz b -2
dec c
jnz c -5"""
    p1, _ = solve_parts(s, 1)
    assert p1 == "6"


def test_add_inc_dec() -> None:
    # inc a; dec b; jnz b -2 with b=5 -> adds 5
    s = ADD_INC_DEC
    p1, _ = solve_parts(s, 1)
    assert p1 == "5"


def test_add_dec_inc() -> None:
    # dec b; inc a; jnz b -2 with b=3 -> adds 3
    s = ADD_DEC_INC
    p1, _ = solve_parts(s, 1)
    assert p1 == "3"


def test_no_match_jnz_offset() -> None:
    # jnz offset is -1, not -2; no optimization.
    s = """cpy 2 b
inc a
dec b
jnz b -1"""
    p1, _ = solve_parts(s, 1)
    assert p1 == "1"


def test_add_dec_inc_variant() -> None:
    # dec b; inc a; jnz b -2 with b=4 -> adds 4
    s = """cpy 4 b
dec b
inc a
jnz b -2"""
    p1, _ = solve_parts(s, 1)
    assert p1 == "4"


def test_mul_and_add_combined() -> None:
    # Run a program that produces MUL optimization and then ADD optimization
    s = """cpy 2 c
cpy 3 b
inc a
dec b
jnz b -2
dec c
jnz c -5
cpy 5 d
dec d
inc a
jnz d -2"""
    p1, _ = solve_parts(s, 1)
    assert p1 == "11"
