TEST_STRING = """ULL
RRDDD
LURDL
UUUUD"""

# Each line walks to one key and presses one of its edges, so together they press every edge of
# the corresponding keypad exactly once.
TOUR_SMALL = """ULD
UR
D
UL
RR
D
UL
LDD
UR
LU
RDD
UL
RR
LU
RDD
UL
RU
LLDDR
LU
RDL
RR
LU
RDL
RU"""

TOUR_ADVANCED = """RURUD
LD
UR
D
UL
RR
LU
DRD
UL
LDLR
D
UL
RR
LU
RDD
UL
RR
LU
RDD
UL
RR
LU
DRL
LLDR
LU
RDD
UL
RR
LU
RDL
RU
LDDU"""

from aoc_py.y2016.day02 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "1985"


def test_part1_2() -> None:
    p1, _ = solve_parts("", 1)
    assert p1 == "-1"


def test_part1_3() -> None:
    p1, _ = solve_parts(TOUR_SMALL, 1)
    assert p1 == "425136275184629538479586"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "5DB3"


def test_part2_2() -> None:
    _, p2 = solve_parts(TOUR_ADVANCED, 2)
    assert p2 == "3637241836A572B683C7948B6DAC7B8B"


# ----------- Both parts ------------


def test_both_parts() -> None:
    p1, p2 = solve_parts(TEST_STRING)
    assert (p1, p2) == ("1985", "5DB3")
