TEST_STRING = """3"""

from aoc_py.y2017.day17 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "638"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "1222153"


# ----------- Edge cases ------------


def test_part2_small_target_matches_naive() -> None:
    # Cross-check the ceil-div skip against a plain step-by-step loop.
    steps, target = 3, 5_000
    expected = -1
    current_pos = 0
    for nbr in range(1, target + 1):
        current_pos = 1 + (current_pos + steps) % nbr
        if current_pos == 1:
            expected = nbr
    assert InputData(TEST_STRING).get_p2(target=target) == expected


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("638", "1222153")
