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

from aoc_py.y2023.day20 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "32000000"


def test_part2_1() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "11687500"


# ----------- Part 2 ------------

# No test input given for part 2.
