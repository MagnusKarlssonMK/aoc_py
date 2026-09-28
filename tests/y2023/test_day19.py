TEST_STRING_1 = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

# A single rule on x, so part two's count is just the number of x values times 4000^3 for the
# three unconstrained parts. 9 values of x (1 to 9) are below the threshold.
TEST_STRING_2 = """in{x<10:A}

{x=5}"""

# The same shape with a ">" rule, which splits at threshold + 1 instead: 10 values of x, from
# 3991 up to 4000.
TEST_STRING_3 = """in{x>3990:A}

{x=3995}"""

# A single unconditional rule, so every rating and every part range is accepted.
TEST_STRING_4 = """in{A}

{x=5}"""

# A single unconditional rejection, so nothing is accepted at all.
TEST_STRING_5 = """in{R}

{x=5}"""

# A two-step chain through a second workflow, and a rating whose parts sum to less than four.
TEST_STRING_6 = """in{x<5:mid}
mid{A}

{x=1,m=2}"""

from aoc_py.y2023.day19 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "19114"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "5"


def test_part1_3() -> None:
    p1, _ = solve_parts(TEST_STRING_3, 1)
    assert p1 == "3995"


def test_part1_4() -> None:
    p1, _ = solve_parts(TEST_STRING_4, 1)
    assert p1 == "5"


def test_part1_5() -> None:
    p1, _ = solve_parts(TEST_STRING_5, 1)
    assert p1 == "0"


def test_part1_6() -> None:
    p1, _ = solve_parts(TEST_STRING_6, 1)
    assert p1 == "3"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "167409079868000"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "576000000000"


def test_part2_3() -> None:
    _, p2 = solve_parts(TEST_STRING_3, 2)
    assert p2 == "640000000000"


def test_part2_4() -> None:
    _, p2 = solve_parts(TEST_STRING_4, 2)
    assert p2 == "256000000000000"


def test_part2_5() -> None:
    _, p2 = solve_parts(TEST_STRING_5, 2)
    assert p2 == "0"


def test_part2_6() -> None:
    _, p2 = solve_parts(TEST_STRING_6, 2)
    assert p2 == "256000000000"
