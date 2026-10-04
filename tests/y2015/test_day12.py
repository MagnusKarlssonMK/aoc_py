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


# The empty string is a legal JSON string, and part 1 runs with ignored set to "", so this pins the ignored != ""
# guard: without it part 1 would treat this object as holding a value to ignore and answer 0.
def test_part1_9() -> None:
    p1, _ = solve_parts("""{"a":"","b":2}""", 1)
    assert p1 == "2"


# Part 1 ignores nothing, so an object holding a red value is still walked and the red string itself contributes
# nothing. Without this, nothing in the file would catch part 1 being handed "red" instead of "".
def test_part1_10() -> None:
    p1, _ = solve_parts("""{"a":"red","b":2}""", 1)
    assert p1 == "2"


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


# The red value belongs to the inner object only. Discarding the outer one as well would answer 0, so this pins that
# the skip is scoped to the object actually holding the value.
def test_part2_5() -> None:
    _, p2 = solve_parts("""{"a":{"b":"red"},"c":1}""", 2)
    assert p2 == "1"


# Every other test here asks for one part at a time. This is the shape the runner itself uses.
def test_both_1() -> None:
    p1, p2 = solve_parts("""[1,2,3]""")
    assert p1 == "6"
    assert p2 == "6"
