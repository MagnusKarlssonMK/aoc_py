TEST_STRING_1 = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""

TEST_STRING_2 = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""

# Exercises every part-2 opcode (set/add/mul/mod), both jgz branches and the DONE transition.
TEST_STRING_3 = """set a 4
add a 3
mul a 2
mod a 5
jgz a 2
snd 9
snd a
set z 0
jgz z 2
snd 8
rcv b"""

from aoc_py.y2017.day18 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "4"


def test_part1_no_sound() -> None:
    p1, _ = solve_parts("set a 1", 1)
    assert p1 == "-1"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "3"


def test_part2_all_opcodes() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "2"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING_1) == ("4", "1")
