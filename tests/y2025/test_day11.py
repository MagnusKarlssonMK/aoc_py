TEST_STRING_1 = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

TEST_STRING_2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

from aoc_py.y2025.day11 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "5"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "2"


# ----------- Both parts ------------


def test_both_parts() -> None:
    # The example uses two separate graphs (as in the Rust tests): part 1 starts at
    # "you", part 2 at "svr". The unrelated start node is absent and yields 0.
    assert solve_parts(TEST_STRING_1) == ("5", "0")
    assert solve_parts(TEST_STRING_2) == ("0", "2")
