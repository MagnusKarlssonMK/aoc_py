TEST_STRING = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""

from aoc_py.y2018.day04 import solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "240"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "4455"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING) == ("240", "4455")


def test_cross_year_month_order() -> None:
    # Guards sleep the same 20 minutes, but across different months and years, to
    # exercise the chronological ordering (year, then month comparisons).
    logs = """[1518-02-01 00:00] Guard #1 begins shift
[1518-02-01 00:05] falls asleep
[1518-02-01 00:25] wakes up
[1518-03-01 00:00] Guard #2 begins shift
[1518-03-01 00:05] falls asleep
[1518-03-01 00:25] wakes up
[1519-02-01 00:00] Guard #3 begins shift
[1519-02-01 00:05] falls asleep
[1519-02-01 00:25] wakes up"""
    assert solve_parts(logs) == ("5", "5")
