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
