TEST_STRING_1 = """^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"""

TEST_STRING_2 = """^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"""

import pytest

from aoc_py.y2018.day20 import InputData, solve_parts

# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "23"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "31"


def test_part1_simple() -> None:
    # The small official problem examples (the third one exercises the empty
    # alternative); verified independently via a grid-building BFS.
    assert solve_parts("^WNE$")[0] == "3"
    assert solve_parts("^ENWWW(NEEE|SSE(EE|N))$")[0] == "10"
    assert solve_parts("^ENNWSWW(NEWS|)SSSEENWNSSS(SES|WSES)$")[0] == "15"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "0"


def test_part2_2() -> None:
    _, p2 = solve_parts(TEST_STRING_2, 2)
    assert p2 == "0"


def test_part2_threshold(monkeypatch: pytest.MonkeyPatch) -> None:
    # The threshold is a monkeypatchable class constant; a small value makes the
    # part-2 count nonzero and locks in the filter logic.
    monkeypatch.setattr(InputData, "P2_DOORS", 5)
    _, p2 = solve_parts("^ENWWW(NEEE|SSE(EE|N))$", 2)
    assert p2 == "11"


# ----------- Both parts ------------


def test_both_parts() -> None:
    assert solve_parts(TEST_STRING_1) == ("23", "0")
