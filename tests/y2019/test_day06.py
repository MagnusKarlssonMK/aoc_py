TEST_STRING_1 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""

TEST_STRING_2 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""

# The next three examples cover theoretical cases for part 2, just to ensure robust error handling
# TEST_STRING_3 - YOU's object (B) is an ancestor of SAN's object (A)
TEST_STRING_3 = """COM)A
A)B
B)YOU
A)SAN"""

# TEST_STRING_4 - YOU and SAN are siblings, both attached to B
TEST_STRING_4 = """COM)A
A)B
B)YOU
B)SAN"""

# TEST_STRING_5 - YOU and SAN both attach directly to COM
TEST_STRING_5 = """COM)YOU
COM)SAN"""

from aoc_py.y2019.day06 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "42"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "8"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "9"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_5, 1)
    assert p1 == "2"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "4"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "1"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "0"


def test_part2_4() -> None:
    _, p2 = solve_parts(TEST_STRING_5, 2)
    assert p2 == "0"
