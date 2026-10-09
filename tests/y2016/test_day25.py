TEST_STRING = """cpy a d
cpy 2 c
cpy 3 b
inc d
dec b
jnz b -2
dec c
jnz c -5
cpy 5 b
inc d
dec b
jnz b -2
cpy d a
jnz 0 0
cpy a b
cpy 0 a
cpy 2 c
jnz b 2
jnz 1 6
dec b
dec c
jnz c -4
inc a
jnz 1 -7
cpy 2 b
jnz c 2
jnz 1 4
dec b
dec c
jnz 1 -4
jnz 0 0
out b
jnz a -19
jnz 1 -21"""

# Executes INC, DEC and TGL instructions at runtime (none get optimized away),
# transmitting 0,1,0 repeating, so a loop detection returns immediately.
TEST_STRING_RUNTIME = """tgl 10
cpy 0 c
out c
inc c
out c
cpy 0 c
inc c
dec d
inc d
jnz 1 -8
inc a"""

# Contains a reversed add pattern (DEC; INC; JNZ -2) that triggers the second ADD
# optimizer variant, then transmits 0,1,0 repeating, so a loop detection returns.
TEST_STRING_ADD = """cpy 0 c
cpy 5 b
dec b
inc c
jnz b -2
cpy 0 c
out c
inc c
out c
cpy 0 c
jnz 1 -5"""

from aoc_py.y2016.day25 import InputData, Instruction, Operation, Registers, solve_parts

# ----------- Part 1 ------------

# The program transmits the LSB-first bits of a + 11 repeatedly. The smallest a for
# which that stream is an endless 0,1,0,1,... is a = 42 - 11 = 31 (42 = 0b101010).


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "31"


def test_part1_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 1) == ("31", "-1")


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "-"


def test_part2_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 2) == ("-1", "-")


# ----------- Registers ------------


def test_registers() -> None:
    regs = Registers()
    regs.set_reg("a", 5)
    regs.inc_reg("a")
    regs.dec_reg("a")
    assert regs.get_reg("a") == 5
    regs.inc_reg("zz")  # unknown register is ignored
    regs.dec_reg("zz")
    assert regs.get_reg("zz") == 0
    assert regs.get_val("a") == 5
    assert regs.get_val("7") == 7


# ----------- Instruction toggle ------------


def test_toggle_op() -> None:
    assert Instruction(Operation.INC, "a").get_toggled_op() == Operation.DEC
    assert Instruction(Operation.DEC, "a").get_toggled_op() == Operation.INC
    assert Instruction(Operation.JNZ, "1", "2").get_toggled_op() == Operation.CPY
    assert Instruction(Operation.CPY, "1", "2").get_toggled_op() == Operation.JNZ


# ----------- Runtime op coverage ------------


def test_runtime_inc_dec_tgl() -> None:
    assert InputData(TEST_STRING_RUNTIME).get_a_register() == 0


def test_add_reversed_optimization() -> None:
    assert InputData(TEST_STRING_ADD).get_a_register() == 0


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("31", "-")
