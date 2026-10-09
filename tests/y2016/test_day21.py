TEST_STRING = """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d"""

TEST_ROUNDTRIP = """swap position 0 with position 7
swap letter a with letter h
rotate left 3 steps
rotate right 2 steps
rotate based on position of letter c
reverse positions 1 through 5
move position 7 to position 0"""

from aoc_py.y2016.day21 import InputData, Password, solve_parts

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


# ----------- Password operations ------------


def test_swap_pos() -> None:
    p = Password("abcdef")
    p.swap_pos(0, 5)
    assert p.pwd == "fbcdea"


def test_swap_letter() -> None:
    p = Password("abc")
    p.swap_letter("a", "c")
    assert p.pwd == "cba"


def test_rotate_wraps() -> None:
    p = Password("abcdefgh")
    p.rotate(3)
    assert p.pwd == "defghabc"
    p.rotate(-4)
    assert p.pwd == "habcdefg"


def test_rotate_pos_low_index() -> None:
    p = Password("abcdefgh")
    p.rotate_pos("a")  # index 0 -> rotate right 1
    assert p.pwd == "habcdefg"


def test_rotate_pos_high_index() -> None:
    p = Password("abcdefgh")
    p.rotate_pos("d")  # index 3 -> rotate right 4
    assert p.pwd == "efghabcd"


def test_rotate_pos_extra_turn() -> None:
    p = Password("abcdefgh")
    p.rotate_pos("e")  # index 4 -> rotate right 1+4+1 = 6
    assert p.pwd == "cdefghab"


def test_rotate_pos_reverse_roundtrip() -> None:
    for c in "abcdefgh":
        p = Password("abcdefgh")
        p.rotate_pos(c)
        p.rotate_pos_reverse(c)
        assert p.pwd == "abcdefgh"


def test_reverse_pos() -> None:
    p = Password("abcdef")
    p.reverse_pos(1, 4)
    assert p.pwd == "aedcbf"


def test_move_pos() -> None:
    p = Password("abcdef")
    p.move_pos(0, 5)
    assert p.pwd == "bcdefa"


# ----------- Instruction parsing ------------


def test_rotate_right() -> None:
    assert (
        InputData("rotate right 1 step").get_scrambled_string("abcdefgh") == "habcdefg"
    )


def test_unknown_instruction_skipped() -> None:
    p = InputData("fly to the moon\nswap position 0 with position 1")
    assert p.get_scrambled_string("ab") == "ba"


def test_roundtrip_mixed_operations() -> None:
    p = InputData(TEST_ROUNDTRIP)
    scrambled = p.get_scrambled_string("abcdefgh")
    assert scrambled == "ghedcbaf"
    assert p.get_descrambled_string(scrambled) == "abcdefgh"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts("swap position 0 with position 1") == ("bacdefgh", "bfgdceah")


def test_part1_solve_parts() -> None:
    assert solve_parts("swap position 0 with position 1", 1) == ("bacdefgh", "-1")


def test_part2_solve_parts() -> None:
    assert solve_parts("swap position 0 with position 1", 2) == ("-1", "bfgdceah")
