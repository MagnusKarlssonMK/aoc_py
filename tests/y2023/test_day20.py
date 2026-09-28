TEST_STRING_1 = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

TEST_STRING_2 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

# The module feeding 'rx' is a conjunction with two inputs, and the two first fire on different
# button presses, so part two is the lcm of 1 and 2.
TEST_STRING_3 = """broadcaster -> a, b
%a -> inv
&inv -> con
%b -> con
&con -> rx"""

# Four subgraphs, each ending in a conjunction, all of them merging into a single conjunction that
# feeds 'rx'. This is the shape of the real input, and it gives part two four counts to take the
# lcm of.
TEST_STRING_4 = """broadcaster -> a, b, c, d
%a -> inv
&inv -> ca
%b -> b1
&b1 -> cb
%c -> c1
&c1 -> cc
%d -> d1
&d1 -> cd
&ca -> final
&cb -> final
&cc -> final
&cd -> final
&final -> rx"""

from aoc_py.y2023.day20 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "32000000"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "11687500"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "15001999"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "109250000"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "2"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "1"
