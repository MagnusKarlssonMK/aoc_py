TEST_STRING_1 = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn"""

TEST_STRING_2 = """aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb"""

from aoc_py.y2016.day07 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "2"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "3"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING_1) == ("2", "0")
    assert solve_parts(TEST_STRING_2) == ("0", "3")


def test_near_misses() -> None:
    # None of these qualifies: "abbc" has an inner doublet but differing ends, "abca" matching ends
    # but a differing middle, "aaaa" repeated middles, "aaa[aaa]" only repeated characters, and
    # "bac" is no ABA at all, so the "aba" outside finds no BAB inside.
    near_misses = """abbc[q]r
abca[q]r
aaaa[q]r
aaa[aaa]
aba[bac]"""
    assert solve_parts(near_misses) == ("0", "0")
