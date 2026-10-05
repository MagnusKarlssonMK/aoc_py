TEST_STRING_1 = """H => HO
H => OH
O => HH

HOH"""

TEST_STRING_2 = """H => HO
H => OH
O => HH

HOHOHO"""

# Part 2 needs rules shaped like the real input's, which the two examples above are not. Their "e"
# rules are e => H and e => O, a single atom each, so they do not carry the second unit that the
# final subtraction accounts for. These six rules are a subset of the real input and do carry it:
# every "e" rule raises the measure by two and every other rule by one, which is what makes the
# count independent of the order the reductions happen in.
TEST_STRING_3 = """e => HF
F => CaF
Ca => CaCa
H => CRnMgYFAr
Ca => SiRnMgAr
Mg => TiMg

CRnMgYCaFArSiRnMgArCaCaF"""

# Same rules, a molecule with Rn and Ar but no Y.
TEST_STRING_4 = """e => HF
F => CaF
Ca => CaCa
H => CRnMgYFAr
Ca => SiRnMgAr
Mg => TiMg

HCaSiRnTiMgArCaF"""

# Same rules again, a molecule with no markers at all, so the three corrections all come out as zero
# and the answer is just the measure minus one.
TEST_STRING_5 = """e => HF
F => CaF
Ca => CaCa
H => CRnMgYFAr
Ca => SiRnMgAr
Mg => TiMg

HCaCaCaCaF"""

from aoc_py.y2015.day19 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "4"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "7"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "7"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "6"


def test_part1_5() -> None:
    p1, _ = solve_parts(TEST_STRING_5, 1)
    assert p1 == "6"


# ----------- Part 2 ------------


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "7"


def test_part2_4() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "6"


def test_part2_5() -> None:
    _, p2 = solve_parts(TEST_STRING_5, 2)
    assert p2 == "5"


# ----------- Both parts at once ------------


# This is the shape the runner itself uses.
def test_both_1() -> None:
    p1, p2 = solve_parts(TEST_STRING_1)
    assert p1 == "4"
    assert p2 == "2"


def test_both_2() -> None:
    p1, p2 = solve_parts(TEST_STRING_3)
    assert p1 == "7"
    assert p2 == "7"
