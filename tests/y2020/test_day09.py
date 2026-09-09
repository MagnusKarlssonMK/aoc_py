TEST_STRING = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

from aoc_py.y2020.day09 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "127"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "62"
