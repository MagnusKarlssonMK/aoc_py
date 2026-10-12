TEST_STRING_1 = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

TEST_STRING_2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""

# Has an invalid nearby ticket (100) plus two departure fields, so part 2 exercises both the
# filtering and the departure product.
TEST_STRING_3 = """departure location: 1-3 or 5-7
departure station: 20-22 or 24-25
class: 4-6 or 8-9
row: 10-12 or 14-15

your ticket:
2,5,11,21

nearby tickets:
2,5,11,21
100,4,12,21"""

# A single ticket with two invalid values, to check that all of them are summed.
TEST_STRING_MULTI = """class: 1-3 or 5-7

your ticket:
1

nearby tickets:
4,9"""

# Two identical fields make the mapping impossible to deduce.
TEST_STRING_AMBIGUOUS = """a: 0-5 or 10-15
b: 0-5 or 10-15

your ticket:
1,1

nearby tickets:
1,1"""

from aoc_py.y2020.day16 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "71"


def test_part1_sums_all_invalid_values() -> None:
    p1, _ = solve_parts(TEST_STRING_MULTI, 1)
    assert p1 == "13"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "1"


def test_part2_only_filters_invalid_tickets() -> None:
    # get_p2 must discard invalid nearby tickets on its own, without get_p1 running first.
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "42"


def test_part2_ambiguous() -> None:
    _, p2 = solve_parts(TEST_STRING_AMBIGUOUS, 2)
    assert p2 == "-1"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING_3) == ("100", "42")
