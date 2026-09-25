TEST_STRING_1 = """0,0,0,0
3,0,0,0
0,3,0,0
0,0,3,0
0,0,0,3
0,0,0,6
9,0,0,0
12,0,0,0"""

TEST_STRING_2 = """-1,2,2,0
0,0,2,-2
0,0,0,-2
-1,2,0,0
-2,-2,-2,2
3,0,2,-1
-1,3,2,2
-1,0,-1,0
0,2,1,-2
3,0,0,0"""

TEST_STRING_3 = """1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2"""

TEST_STRING_4 = """1,-1,-1,-2
-2,-2,0,1
0,2,1,3
-2,3,-2,1
0,2,3,-2
-1,-1,1,-2
0,-2,-1,0
-2,2,3,-1
1,2,2,0
-1,-2,0,-2"""

from aoc_py.y2018.day25 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "2"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "4"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "3"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "8"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "-"
