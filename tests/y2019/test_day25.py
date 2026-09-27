# Day 25 is the only interactive day: the input program is a text adventure played by hand (see the module
# docstring for the walkthrough), so there is no answer to derive from data. The tests instead drive the
# solver's tiny REPL:
#
# - TEST_STRING_1 prints "hi", waits for a line, echoes its first character back, then halts. Driving it once
#   covers the whole game loop (program output -> prompt -> stdin -> echo -> halt).
# - TEST_STRING_2 halts immediately, so the part-specific calls just fall back to their untouched
#   "-" / "-1" placeholders without ever needing input.
TEST_STRING_1 = """104,104,104,105,3,1000,4,1000,99"""

TEST_STRING_2 = """99"""

import io

import pytest

from aoc_py.y2019.day25 import solve_parts

# ----------- Part 1 ------------


def test_part1_1(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("sys.stdin", io.StringIO("Z\n"))
    p1, p2 = solve_parts(TEST_STRING_1, 1)
    assert p1 == "-"
    assert p2 == "-1"


def test_part1_2() -> None:
    p1, _ = solve_parts(TEST_STRING_2, 1)
    assert p1 == "-"


# ----------- Part 2 ------------


def test_part2_1(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("sys.stdin", io.StringIO("Z\n"))
    p1, p2 = solve_parts(TEST_STRING_1, 2)
    assert p1 == "-1"
    assert p2 == "-"


def test_part2_2() -> None:
    p1, p2 = solve_parts(TEST_STRING_2)
    assert p1 == "-"
    assert p2 == "-"


def test_part2_3(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr("sys.stdin", io.StringIO("Z\n"))
    assert solve_parts(TEST_STRING_1) == ("-", "-")
    out = capsys.readouterr().out
    assert out.startswith("hi")
    assert out.endswith("Z")
