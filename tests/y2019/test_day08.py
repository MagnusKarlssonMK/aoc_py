TEST_STRING = """0222112222120000"""

from aoc_py.y2019.day08 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "24"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    p = InputData(TEST_STRING, 2, 2)
    p2 = p.get_p2()
    assert p2 == "\n #\n# "
