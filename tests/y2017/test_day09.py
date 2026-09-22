from aoc_py.y2017.day09 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts("{}", 1)
    assert p1 == "1"


def test_part1_2() -> None:
    p1, _ = solve_parts("{{{}}}", 1)
    assert p1 == "6"


def test_part1_3() -> None:
    p1, _ = solve_parts("{{},{}}", 1)
    assert p1 == "5"


def test_part1_4() -> None:
    p1, _ = solve_parts("{{{},{},{{}}}}", 1)
    assert p1 == "16"


def test_part1_5() -> None:
    p1, _ = solve_parts("{<a>,<a>,<a>,<a>}", 1)
    assert p1 == "1"


def test_part1_6() -> None:
    p1, _ = solve_parts("{{<ab>},{<ab>},{<ab>},{<ab>}}", 1)
    assert p1 == "9"


def test_part1_7() -> None:
    p1, _ = solve_parts("{{<!!>},{<!!>},{<!!>},{<!!>}}", 1)
    assert p1 == "9"


def test_part1_8() -> None:
    p1, _ = solve_parts("{{<a!>},{<a!>},{<a!>},{<ab>}}", 1)
    assert p1 == "3"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts("<>", 2)
    assert p2 == "0"


def test_part2_2() -> None:
    _, p2 = solve_parts("<random characters>", 2)
    assert p2 == "17"


def test_part2_3() -> None:
    _, p2 = solve_parts("<<<<>", 2)
    assert p2 == "3"


def test_part2_4() -> None:
    _, p2 = solve_parts("<{!>}>", 2)
    assert p2 == "2"


def test_part2_5() -> None:
    _, p2 = solve_parts("<!!>", 2)
    assert p2 == "0"


def test_part2_6() -> None:
    _, p2 = solve_parts("<!!!>>", 2)
    assert p2 == "0"


def test_part2_7() -> None:
    _, p2 = solve_parts('<{o"i!a,<{i<a>', 2)
    assert p2 == "10"
