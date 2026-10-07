TEST_STRING = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1"""

from aoc_py.y2016.day08 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "6"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "\n #  # #\n# #    \n #     \n"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("6", "\n #  # #\n# #    \n #     \n")


def test_screen_size() -> None:
    # Five instructions cross the heuristic's threshold: this runs on the real 50x6 screen, so the
    # rect lights 9x4 = 36 pixels (rotation preserves the count) and the art is 6 rows of 50.
    screen = """rect 9x4
rotate column x=0 by 1
rotate row y=0 by 0
rotate column x=8 by 1
rotate row y=3 by 0"""
    p1, p2 = solve_parts(screen)
    assert p1 == "36"
    assert p2 == (
        "\n #######                                          \n"
        "#########                                         \n"
        "#########                                         \n"
        "#########                                         \n"
        "#       #                                         \n"
        "                                                  \n"
    )
