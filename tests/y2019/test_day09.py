TEST_STRING_1 = """109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"""

TEST_STRING_2 = """104,1125899906842624,99"""

TEST_STRING_3 = """1102,34915192,34915192,7,4,7,99,0"""

from aoc_py.y2019.day09 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "99"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "1125899906842624"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "1219070632396864"


def test_both_parts() -> None:
    # Both parts run on the same InputData; make sure solver reboots so the second call works.
    p1, p2 = solve_parts("3,0,4,0,99")
    assert p1 == "1"
    assert p2 == "2"
