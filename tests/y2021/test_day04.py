TEST_STRING_1 = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

# The first board completes its top row exactly when 0 is drawn, so it scores 0 * unmarked = 0. Part 1 must
# still report that zero as the first bingo, and part 2 must still pick up the second board.
TEST_STRING_2 = """1,2,3,4,0,5,6,7,8,9

 1  2  3  4  0
20 21 22 23 24
30 31 32 33 34
40 41 42 43 44
50 51 52 53 54

 5  6  7  8  9
40 41 42 43 44
50 51 52 53 54
60 61 62 63 64
70 71 72 73 74"""

# The drawn numbers run out before the second board gets a bingo, so only one board ever wins. Part 2 must
# still report that board, rather than falling back to zero because two boards were left on the table.
TEST_STRING_3 = """1,2,3,4,5,6,7,8,9,0

 1  2  3  4  5
30 31 32 33 34
35 36 37 38 39
40 41 42 43 44
45 46 47 48 49

20 21 22 23 24
25 26 27 28 29
50 51 52 53 54
55 56 57 58 59
60 61 62 63 64"""

from aoc_py.y2021.day04 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "4512"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "0"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "3950"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "1924"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "10260"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "3950"
