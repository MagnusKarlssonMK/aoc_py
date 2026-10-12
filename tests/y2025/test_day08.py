import pytest

from aoc_py.y2025.day08 import solve_parts

TEST_STRING = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

# ----------- Part 1 ------------


def test_part1_1(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2025.day08.MAX_CONNECTIONS_PART1", 10)
    p1, _ = solve_parts(TEST_STRING, 1)
    assert p1 == "40"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING, 2)
    assert p2 == "25272"


# ----------- Both parts ------------


def test_both_parts(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2025.day08.MAX_CONNECTIONS_PART1", 10)
    assert solve_parts(TEST_STRING) == ("40", "25272")
