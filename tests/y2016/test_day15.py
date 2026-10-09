TEST_STRING = """Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1."""

SINGLE_DISC = """Disc #1 has 5 positions; at time=0, it is at position 4."""

THREE_DISCS = """Disc #1 has 2 positions; at time=0, it is at position 1.
Disc #2 has 3 positions; at time=0, it is at position 0.
Disc #3 has 5 positions; at time=0, it is at position 2."""

from aoc_py.y2016.day15 import InputData, chinese_remainder, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "5"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "85"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("5", "85")


# ----------- Chinese remainder ------------


def test_chinese_remainder() -> None:
    assert chinese_remainder([3, 5, 7], [2, 3, 2]) == 23
    assert chinese_remainder([5, 11], [0, 9]) == 20
    assert chinese_remainder([4], [3]) == 3


# ----------- Edge cases ------------


def test_single_disc_zero_remainder() -> None:
    # (4 + t + 1) % 5 == 0 first holds at t == 0, so the remainder is exactly the modulus.
    assert solve_parts(SINGLE_DISC) == ("0", "20")


def test_three_discs() -> None:
    assert solve_parts(THREE_DISCS) == ("10", "40")


def test_extra_disc_is_idempotent() -> None:
    # Adding the extra disc must not mutate the stored discs: a second call must agree with the first,
    # and the plain search must be unaffected.
    p = InputData(TEST_STRING)
    assert p.get_buttonpress_time(True) == 85
    assert p.get_buttonpress_time(True) == 85
    assert p.get_buttonpress_time() == 5
