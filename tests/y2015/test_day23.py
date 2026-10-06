# Custom test programs:
TEST_STRING_1 = """inc a
jio a, +2
inc a
tpl a
hlf a
inc b
jie b, +2
inc b
jmp +1"""

TEST_STRING_2 = """inc b
inc b
jie b, +3
inc a
inc a
inc b"""

TEST_STRING_3 = """jie a, +2
inc b
inc b"""

# The puzzle's own example, which the text says leaves a at 2. It never touches b, so the
# assertions below are 0 in both parts -- it is here for the program shape, not for the answer.
TEST_STRING_4 = """inc a
jio a, +2
tpl a
inc a"""

# Jumps below the start of the program. Only indices inside the list name a defined instruction,
# so this exits at once instead of indexing backwards from the end of the list.
TEST_STRING_6 = """jmp -1
inc b"""

# Halving a three leaves one, so hlf divides rather than subtracting.
TEST_STRING_7 = """inc b
inc b
inc b
hlf b"""

# Triples leave a odd here, where doubling would leave it even, so the jie below lands in a
# different place and b counts differently. Register a is never returned, which is why this
# reaches the answer through a jump.
TEST_STRING_8 = """inc a
tpl a
jie a, +2
inc b
inc b"""

# The jio taken with a equal to one: b counts the two instructions it skips over.
TEST_STRING_9 = """inc a
jio a, +2
inc b
inc b"""

# The jio not taken, with a at three rather than one. jio tests for a register holding exactly
# one, not for oddness, so a three falls through.
TEST_STRING_10 = """inc a
inc a
inc a
jio a, +2
inc b
inc b"""

from aoc_py.y2015.day23 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "2"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "3"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "1"


def test_part1_4() -> None:
    # The puzzle's example only moves register a, so b stays zero
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "0"


def test_part1_6() -> None:
    # Ends rather than wrapping to the last instruction, which would run forever
    p1, _ = solve_parts(TEST_STRING_6, 1)
    assert p1 == "0"


def test_part1_7() -> None:
    p1, _ = solve_parts(TEST_STRING_7, 1)
    assert p1 == "1"


def test_part1_8() -> None:
    # Triples leave a odd and the jump falls through, so both inc b run
    p1, _ = solve_parts(TEST_STRING_8, 1)
    assert p1 == "2"


def test_part1_9() -> None:
    # jio fires with a at one and skips the first inc b
    p1, _ = solve_parts(TEST_STRING_9, 1)
    assert p1 == "1"


def test_part1_10() -> None:
    # jio does not fire on a three, so neither inc b is skipped
    p1, _ = solve_parts(TEST_STRING_10, 1)
    assert p1 == "2"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "2"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "3"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "2"


def test_part2_4() -> None:
    # Starting a at one makes the jio fall through to the tpl, so a ends at 7 rather than 2, but
    # register b is untouched either way.
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "0"


# ----------- Both parts at once ------------


# This is the shape the runner itself uses. Both starting values have to terminate.
def test_both_6() -> None:
    p1, p2 = solve_parts(TEST_STRING_6)
    assert p1 == "0"
    assert p2 == "0"


# Part 1 leaves b at one, so part 2 only returns two if the register is cleared between runs.
def test_both_9() -> None:
    p1, p2 = solve_parts(TEST_STRING_9)
    assert p1 == "1"
    assert p2 == "2"
