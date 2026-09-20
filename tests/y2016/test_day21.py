TEST_STRING = """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d"""

from aoc_py.y2016.day21 import InputData

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p = InputData(TEST_STRING)
    p1 = p.get_scrambled_string("abcde")
    assert p1 == "decab"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    p = InputData(TEST_STRING)
    p2 = p.get_descrambled_string("decab")
    assert p2 == "abcde"
