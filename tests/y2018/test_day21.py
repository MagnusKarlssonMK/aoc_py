# There is no official test vector for day 21: the problem's sample program is far too short for
# this solver, which disassembles the program by reading the base seed, multiplier, masks and shift
# from fixed instruction positions (program[6], [7], [8], [10], [11], [12] and [19]). This synthetic
# program uses the same #ip register and the same loop skeleton as a real day-21 input, with small
# constants so the hash chain (part 1) and the part-2 cycle stay short:
#   part 1: the value of register 0 after the hash loop -> 56
#   part 2: the largest register-0 seed for which the program still halts -> 3688
TEST_STRING = """#ip 4
seti 1 0 3
bani 3 255 3
eqri 3 72 3
addr 3 4 4
seti 0 0 4
seti 0 5 3
bori 3 256 2
seti 1 1 3
bani 2 255 1
addr 3 1 3
bani 3 4095 3
muli 3 7 3
bani 3 4095 3
gtir 256 2 1
addr 1 4 4
addi 4 1 4
seti 19 1 4
seti 0 7 1
addi 1 1 5
muli 5 256 5
gtrr 5 2 5
addr 5 4 4
addi 4 1 4
seti 17 3 4
addi 1 1 1
seti 10 0 4
setr 1 1 2
seti 5 7 4
eqrr 3 0 1
addr 1 4 4
seti 2 5 4"""

from aoc_py.y2018.day21 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "56"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "3688"
