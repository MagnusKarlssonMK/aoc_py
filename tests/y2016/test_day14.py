# A real Part 2 run stretches every candidate hash 2017 times and takes around ten seconds, so the solver is not
# suitable for a per-run unit test. The scan itself is therefore tested with a stubbed get_md5 that returns crafted
# digests (the approach of y2016 day 5): the tests pin the triple/quintuple rules, the 1000-index validation window and
# the scan order, and cannot hang because any unspecified index returns a run-free neutral digest. The real md5 path is
# covered by direct get_md5 checks and by the Part 1 example; Part 2's real hashing is verified against the real input
# outside the suite.

TEST_STRING_1 = """abc"""

import hashlib
from collections.abc import Callable

import pytest

from aoc_py.y2016.day14 import get_md5, solve_parts

# A 32-character digest with no run of three identical characters.
NEUTRAL = "0123456789abcdef" * 2
FILL = "~"


def triple(c: str) -> str:
    """A digest whose first three-in-a-row is c (the tilde tail is never a pending triple)."""
    return c * 3 + FILL * 29


def quint(c: str) -> str:
    """A digest whose five-in-a-row is c."""
    return c * 5 + FILL * 27


def make_fake(
    mapping: dict[str, str], calls: list[tuple[str, int]] | None = None
) -> Callable[..., str]:
    def fake(inputstr: str, stretch: int = 0) -> str:
        if calls is not None:
            calls.append((inputstr, stretch))
        return mapping.get(inputstr, NEUTRAL)

    return fake


def build_mapping() -> dict[str, str]:
    """Digests for salt 'x' that exercise every branch and yield 64 keys, the 64th at index 1220."""
    mapping = {
        "x0": triple("q"),
        "x1": triple("q"),  # a second pending 'q': exercises the set-add branch
        "x2": quint("q"),  # validates both pending 'q' triples
        "x3": quint("w"),  # a quintuple with no pending triple
        "x4": triple("e"),
        "x1005": quint("e"),  # 1001 away: outside the window, discarded
        "x6": triple("r"),
        "x1006": quint("r"),  # exactly 1000 away: inside the window
    }
    pool = [
        c
        for c in (chr(i) for i in range(0x21, 0x7F))
        if c not in ("q", "w", "e", "r", FILL)
    ]
    for k in range(62):
        mapping[f"x{1100 + 2 * k}"] = triple(pool[k])
        mapping[f"x{1101 + 2 * k}"] = quint(pool[k])
    return mapping


# ----------- md5 / stretching ------------


def test_get_md5_single_hash() -> None:
    assert get_md5("md5-single") == hashlib.md5(b"md5-single").hexdigest()


def test_get_md5_stretched() -> None:
    expected = hashlib.md5(b"md5-stretched").hexdigest()
    for _ in range(3):
        expected = hashlib.md5(expected.encode()).hexdigest()
    assert get_md5("md5-stretched", 3) == expected


# ----------- Part 1 (real hashing) ------------


def test_part1_example() -> None:
    assert solve_parts(TEST_STRING_1, 1) == ("22728", "-1")


# ----------- Scan rules (stubbed hashing) ------------


def test_scan_rules(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("aoc_py.y2016.day14.get_md5", make_fake(build_mapping()))
    p1, _ = solve_parts("x", 1)
    assert p1 == "1220"


def test_scan_inputs_and_stretch(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[str, int]] = []
    monkeypatch.setattr("aoc_py.y2016.day14.get_md5", make_fake(build_mapping(), calls))
    _, p2 = solve_parts("x", 2)
    assert p2 == "1220"
    # The salt is prefixed and the stretch forwarded; indices are scanned in order from zero.
    assert calls[:3] == [("x0", 2016), ("x1", 2016), ("x2", 2016)]


# ----------- Both parts ------------


def test_both_parts(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[str, int]] = []
    monkeypatch.setattr("aoc_py.y2016.day14.get_md5", make_fake(build_mapping(), calls))
    assert solve_parts("x") == ("1220", "1220")
    assert ("x0", 0) in calls
    assert ("x0", 2016) in calls
