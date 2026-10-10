TEST_STRING = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

# The bad node C3 (7) is two levels below the root A: B discovers the correction,
# and A must propagate it upwards without re-evaluating its own children.
TEST_STRING_PROPAGATE = """A (10) -> B, D, E
B (20) -> C1, C2, C3
C1 (5)
C2 (5)
C3 (7)
D (35)
E (35)"""

from aoc_py.y2017.day07 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "tknk"


def test_part1_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 1) == ("tknk", "-1")


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "60"


def test_part2_solve_parts() -> None:
    assert solve_parts(TEST_STRING, 2) == ("-1", "60")


# ----------- Edge cases ------------


def test_correction_propagates() -> None:
    # C3 must weigh 5 to match its siblings; the correction is discovered at B
    # and propagates through A (which never becomes unbalanced itself).
    assert solve_parts(TEST_STRING_PROPAGATE) == ("A", "5")


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("tknk", "60")
