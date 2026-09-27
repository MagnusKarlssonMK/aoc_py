# Day 21 puzzle description gives no test input, so these are hand-crafted intcode programs that act as the
# springdroid's computer. The solver feeds the springdroid instruction program to them as ASCII bytes and keeps
# the last output value, so the tests observe exactly which bytes were sent:
#
# - TEST_STRING_1 echoes the first byte it reads back: part 1 receives the WALK program (first byte 'O' = 79)
#   and part 2 the RUN program (first byte 'N' = 78), so the two feeds are distinguishable.
# - TEST_STRING_2 halts without producing any output, so both parts fall back to -1.
# - TEST_STRING_3 and TEST_STRING_4 read exactly as many bytes as the WALK / RUN program has, sum their ASCII
#   values and output the total (2468 resp. 3284). Because the expected read count is built into the program,
#   any change to the instruction strings - in content or length - breaks the sum, pinning down the exact bytes.
TEST_STRING_1 = """3,1298,4,1298,99"""

TEST_STRING_2 = """99"""

TEST_STRING_3 = """1101,44,0,1300,3,1298,1,1299,1298,1299,1001,1300,-1,1300,107,0,1300,1301,1005,1301,4,4,1299,99"""

TEST_STRING_4 = """1101,58,0,1300,3,1298,1,1299,1298,1299,1001,1300,-1,1300,107,0,1300,1301,1005,1301,4,4,1299,99"""

from aoc_py.y2019.day21 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "79"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "-1"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "2468"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "78"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "3284"


def test_part2_3() -> None:
    p1, p2 = solve_parts(TEST_STRING_1)
    assert p1 == "79"
    assert p2 == "78"
