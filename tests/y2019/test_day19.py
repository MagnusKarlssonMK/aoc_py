# Day 19 puzzle description gives no test program, so these are hand-crafted intcode programs that act as the
# drone's beam-response computer. Every query feeds in x and y; TEST_STRING_1 answers 1 when the point lies
# inside a synthetic beam cone (y between 2*x+30 and 3*x+60) and 0 outside it, then jumps back to read the next pair.
# The solver probes all 2500 coordinates of the 50 x 50 grid (part 1 = number of affected points) and then
# walks a 100 x 100 square down the beam, so part 2 = x * 10000 + y of the fitted square.
# The computer is rebooted after every query; a second program that halts without answering (TEST_STRING_2)
# therefore reports -1 for every coordinate, which part 1 sums to -2500. Part 2 is never run against it,
# since a beam that never responds would make the square scan run forever.
TEST_STRING_1 = """3,50,3,51,1,50,50,52,1,52,41,53,1,50,52,54,1,54,42,55,7,51,53,56,7,55,51,57,1,56,57,58,7,58,43,59,4,59,1105,1,0,30,60,1"""

TEST_STRING_2 = """99"""

from aoc_py.y2019.day19 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "110"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "-2500"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "2670762"
