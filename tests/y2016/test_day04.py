TEST_STRING_1 = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]"""

TEST_STRING_2 = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
lmprfnmjc-mzhcar-qrmpyec-548[mcrpa]"""

from aoc_py.y2016.day04 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "1514"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "548"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "-1"


def test_part2_3() -> None:
    # Same name and sector as the room in test_part2_1, but the checksum fails, so it may not answer.
    _, p2 = solve_parts("lmprfnmjc-mzhcar-qrmpyec-548[decoy]", 2)
    assert p2 == "-1"


def test_part2_4() -> None:
    # Real room with the right number of words but the wrong word lengths for the target.
    _, p2 = solve_parts("abc-def-ghij-1[abcde]", 2)
    assert p2 == "-1"


# ----------- Both parts ------------


def test_both_parts() -> None:
    # Trailing newline: the runner strips it, but splitting must not turn it into an empty room.
    p1, p2 = solve_parts(TEST_STRING_2 + "\n")
    assert (p1, p2) == ("2062", "548")
