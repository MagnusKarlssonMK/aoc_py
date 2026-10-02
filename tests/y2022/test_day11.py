# The official test input, used for both parts.
TEST_STRING_1 = """Monkey 0:
Starting items: 79, 98
Operation: new = old * 19
Test: divisible by 23
If true: throw to monkey 2
If false: throw to monkey 3

Monkey 1:
Starting items: 54, 65, 75, 74
Operation: new = old + 6
Test: divisible by 19
If true: throw to monkey 2
If false: throw to monkey 0

Monkey 2:
Starting items: 79, 60, 97
Operation: new = old * old
Test: divisible by 13
If true: throw to monkey 1
If false: throw to monkey 3

Monkey 3:
Starting items: 74
Operation: new = old + 3
Test: divisible by 17
If true: throw to monkey 0
If false: throw to monkey 1"""

# Custom test input.
# Monkey 0 throws to itself on the false branch: 5 becomes 6, which fails the test
# and comes straight back, and 6 becomes 7, which passes and leaves for monkey 1.
# That is the deferral the puzzle asks for - an item thrown to a monkey that has
# already had its turn waits for that monkey's next turn. Monkey 1 never throws to
# itself and sends both its branches back to monkey 0, so the run always ends.
# The expected values come from an independent reference implementation that first
# reproduces all four known answers: 10605, 2713310158, 58056 and 15048718170.
TEST_STRING_2 = """Monkey 0:
Starting items: 5
Operation: new = old + 1
Test: divisible by 7
If true: throw to monkey 1
If false: throw to monkey 0

Monkey 1:
Starting items: 100
Operation: new = old + 1
Test: divisible by 3
If true: throw to monkey 0
If false: throw to monkey 0"""

from aoc_py.y2022.day11 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "10605"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "1365"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "2713310158"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "66676666"
