TEST_STRING = """p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>"""

# Three particles moving in parallel, never sharing a position.
TEST_STRING_NO_COLLISIONS = """p=<0,0,0>, v=<1,0,0>, a=<0,0,0>
p=<0,5,0>, v=<1,0,0>, a=<0,0,0>
p=<0,0,9>, v=<1,0,0>, a=<0,0,0>"""

# Two particles that meet at the origin after the first step.
TEST_STRING_ALL_COLLIDE = """p=<-1,0,0>, v=<1,0,0>, a=<0,0,0>
p=<1,0,0>, v=<-1,0,0>, a=<0,0,0>"""

# One stationary particle is wiped out by another; a third far away survives.
TEST_STRING_PARTIAL_COLLIDE = """p=<0,0,0>, v=<0,0,0>, a=<0,0,0>
p=<1,0,0>, v=<-1,0,0>, a=<0,0,0>
p=<2,0,0>, v=<0,0,0>, a=<0,0,0>"""

# Non-zero acceleration: particle 1 stays put while particle 0 comes for it.
TEST_STRING_ACCELERATION = """p=<0,0,0>, v=<0,0,0>, a=<1,0,0>
p=<10,0,0>, v=<0,0,0>, a=<0,0,0>"""

from aoc_py.y2017.day20 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "3"


def test_short_horizon() -> None:
    assert InputData(TEST_STRING).get_p1(steps=1) == 2


def test_acceleration() -> None:
    assert solve_parts(TEST_STRING_ACCELERATION) == ("1", "0")


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "1"


def test_no_collisions() -> None:
    assert solve_parts(TEST_STRING_NO_COLLISIONS) == ("0", "3")


def test_all_collide() -> None:
    assert solve_parts(TEST_STRING_ALL_COLLIDE) == ("0", "0")


def test_partial_collide() -> None:
    assert solve_parts(TEST_STRING_PARTIAL_COLLIDE) == ("0", "1")
