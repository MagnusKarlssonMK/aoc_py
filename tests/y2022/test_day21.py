TEST_STRING_1 = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""

# A chain ending under root's right child that exercises the four inversions the example does not reach:
# left-dependent + and *, and right-dependent - and /.
TEST_STRING_2 = """root: c5 + n4
n4: n3 + c4
n3: c3 - n2
n2: c2 / n1
n1: humn * c1
c1: 2
c2: 36
c3: 50
c4: 10
c5: 57
humn: 999"""

from aoc_py.y2022.day21 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "152"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "117"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "301"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "6"
