from aoc_py.y2015.day12 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts("""[1,2,3]""", 1)
    assert p1 == "6"


def test_part1_2() -> None:
    p1, _ = solve_parts("""{"a":2,"b":4}""", 1)
    assert p1 == "6"


def test_part1_3() -> None:
    p1, _ = solve_parts("""[[[3]]]""", 1)
    assert p1 == "3"


def test_part1_4() -> None:
    p1, _ = solve_parts("""{"a":{"b":4},"c":-1}""", 1)
    assert p1 == "3"


def test_part1_5() -> None:
    p1, _ = solve_parts("""{"a":[-1,1]}""", 1)
    assert p1 == "0"


def test_part1_6() -> None:
    p1, _ = solve_parts("""[-1,{"a":1}]""", 1)
    assert p1 == "0"


def test_part1_7() -> None:
    p1, _ = solve_parts("""[]""", 1)
    assert p1 == "0"


def test_part1_8() -> None:
    p1, _ = solve_parts("""{}""", 1)
    assert p1 == "0"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts("""[1,2,3]""", 2)
    assert p2 == "6"


def test_part2_2() -> None:
    _, p2 = solve_parts("""[1,{"c":"red","b":2},3]""", 2)
    assert p2 == "4"


def test_part2_3() -> None:
    _, p2 = solve_parts("""{"d":"red","e":[1,2,3,4],"f":5}""", 2)
    assert p2 == "0"


def test_part2_4() -> None:
    _, p2 = solve_parts("""[1,"red",5]""", 2)
    assert p2 == "6"
