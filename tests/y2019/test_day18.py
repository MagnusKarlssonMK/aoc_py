TEST_STRING_1 = """########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################"""

TEST_STRING_2 = """#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################"""

TEST_STRING_3 = """########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################"""

TEST_STRING_4 = """#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba@#@BcIJ#
#############
#nK.L@#@G...#
#M###N#H###.#
#o#m..#i#jk.#
#############"""

TEST_STRING_5 = """#########
#b.A.@.a#
#########"""

TEST_STRING_6 = """########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################"""

TEST_STRING_7 = """#######
#a.#Cd#
##...##
##.@.##
##...##
#cB#Ab#
#######"""

TEST_STRING_8 = """#######
#@....#
#.###.#
#.#c#.#
#.###.#
#.....#
#######"""

from aoc_py.y2019.day18 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "132"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "136"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "81"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_5, 1)
    assert p1 == "8"


def test_part1_5() -> None:
    p1, _ = solve_parts(TEST_STRING_6, 1)
    assert p1 == "86"


def test_part1_6() -> None:
    p1, _ = solve_parts(TEST_STRING_7, 1)
    assert p1 == "26"


def test_part1_7() -> None:
    p1, _ = solve_parts(TEST_STRING_8, 1)
    assert p1 == "-1"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "72"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_7, 2)
    assert p2 == "8"
