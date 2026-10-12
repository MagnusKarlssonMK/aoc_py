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

# 40 is a pair sum within the full 25-number preamble, but not within any smaller prefix
# window, so a leaked preamble length from the example above would flag it as invalid.
LARGE_STRING = """1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
40
1000000"""

from aoc_py.y2020.day09 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "127"


def test_preamble_not_shared_between_inputs() -> None:
    # A small example must not change the preamble length used by a later larger input.
    _ = solve_parts(TEST_STRING, 1)
    p1, _ = solve_parts(LARGE_STRING, 1)
    assert p1 == "1000000"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "62"


def test_part2_2() -> None:
    # No contiguous range sums to the invalid number here.
    _, p2 = solve_parts(LARGE_STRING, 2)
    assert p2 == "-1"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("127", "62")
