# Custom made test vector

TEST_STRING = """Before: [3, 0, 2, 1]
0 2 0 0
After:  [1, 0, 2, 1]

Before: [3, 1, 0, 2]
1 3 0 0
After:  [1, 1, 0, 2]

Before: [0, 2, 3, 1]
2 2 3 0
After:  [0, 2, 3, 1]

Before: [0, 0, 1, 2]
3 3 2 0
After:  [0, 0, 1, 2]

Before: [1, 2, 3, 0]
4 2 3 0
After:  [0, 2, 3, 0]

Before: [1, 2, 3, 0]
5 1 3 0
After:  [0, 2, 3, 0]

Before: [3, 1, 0, 2]
6 1 2 0
After:  [0, 1, 0, 2]

Before: [0, 1, 2, 3]
7 1 0 0
After:  [0, 1, 2, 3]

Before: [2, 2, 1, 1]
8 3 0 0
After:  [0, 2, 1, 1]

Before: [1, 2, 3, 0]
9 3 1 0
After:  [0, 2, 3, 0]

Before: [2, 3, 0, 1]
10 3 1 0
After:  [1, 3, 0, 1]

Before: [1, 2, 3, 0]
11 3 0 0
After:  [0, 2, 3, 0]

Before: [2, 0, 1, 3]
12 1 0 0
After:  [0, 0, 1, 3]

Before: [0, 1, 2, 3]
13 0 1 0
After:  [0, 1, 2, 3]

Before: [0, 1, 2, 3]
14 1 1 0
After:  [1, 1, 2, 3]

Before: [0, 0, 0, 0]
15 0 0 0
After:  [0, 0, 0, 0]


13 9 0 0
11 0 7 0
7 0 3 0
15 0 0 1
4 1 0 2
0 2 1 1
6 1 63 1
10 0 5 3
14 3 1 2
1 53 2 1
2 0 3 1
12 999 0 1
8 0 1 1
5 0 48 1
9 2 0 3
7 1 40000 0
11 0 2 0
15 3 0 0
"""

from aoc_py.y2018.day16 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "14"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "40055"
