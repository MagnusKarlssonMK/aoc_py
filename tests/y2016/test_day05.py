# The puzzle example cannot be scaled down: part 1 needs eight hashes with five leading zeroes (about one in a
# million each) and part 2 needs tens of millions of hashes for every door id there is, so real hashing costs
# seconds per call and would dominate every suite run. The tests script hashlib.md5 instead (the approach of
# y2019 day 25): each solver call gets a finite queue of digests, which pins the password rules exactly, records
# the data the solver asked to hash, and cannot hang -- a loop that failed to advance would exhaust its queue
# and fail the test. The real md5 path is exercised once, outside the suite, against the real input's answers.

TEST_STRING_1 = """doorid"""

import pytest

from aoc_py.y2016.day05 import solve_parts


def qualify(char6: str, char7: str) -> str:
    """A digest the solver keeps: five leading zeroes, then its sixth and seventh characters."""
    return "00000" + char6 + char7 + "0" * 25


# Misses carry four leading zeroes rather than none: they still fail the five-zero rule, but a solver that
# loosened the rule to four would start filling from them and give itself away.
def miss() -> str:
    """A digest with four leading zeroes: the fifth character turns GOOD away, the sixth would be a position."""
    return "0000" + "e5" + "0" * 26


class FakeDigest:
    def __init__(self, digest: str) -> None:
        self.__digest = digest

    def hexdigest(self) -> str:
        return self.__digest


class FakeMd5:
    """Stands in for hashlib.md5: records every input and hands back the next queued digest."""

    def __init__(self, digests: list[str]) -> None:
        self.__digests = iter(digests)
        self.inputs: list[bytes] = []

    def __call__(self, data: bytes) -> FakeDigest:
        self.inputs.append(data)
        return FakeDigest(next(self.__digests))


# Part 1: two misses interleaved with eight hits; the sixth characters spell "abcdef09", reached in ten
# iterations hashing doorid0 through doorid9.
TEST_DIGESTS_1 = [
    miss(),
    qualify("a", "x"),
    qualify("b", "x"),
    miss(),
    qualify("c", "x"),
    qualify("d", "x"),
    qualify("e", "x"),
    qualify("f", "x"),
    qualify("0", "x"),
    qualify("9", "x"),
]

# Part 2: a plain miss, a four-zero digest that only a loosened four-zero check would read (position 5, filler
# q), a non-digit position, an out-of-range position, repeats of filled positions, then eight fills in scrambled
# order -> "adfjhgec". Reaching them takes fourteen iterations, doorid0 through doorid13.
TEST_DIGESTS_2 = [
    miss(),
    "000035q" + "0" * 25,
    qualify("a", "x"),
    qualify("8", "x"),
    qualify("3", "j"),
    qualify("0", "a"),
    qualify("3", "k"),
    qualify("0", "b"),
    qualify("7", "c"),
    qualify("1", "d"),
    qualify("6", "e"),
    qualify("2", "f"),
    qualify("5", "g"),
    qualify("4", "h"),
]

# ----------- Part 1 ------------


def test_part1_1(monkeypatch: pytest.MonkeyPatch) -> None:
    fake = FakeMd5(TEST_DIGESTS_1)
    monkeypatch.setattr("hashlib.md5", fake)
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "abcdef09"
    # The hash input is the door id with the index appended, one call per iteration from zero.
    assert fake.inputs == [("doorid" + str(i)).encode() for i in range(10)]


# ----------- Part 2 ------------


def test_part2_1(monkeypatch: pytest.MonkeyPatch) -> None:
    fake = FakeMd5(TEST_DIGESTS_2)
    monkeypatch.setattr("hashlib.md5", fake)
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "adfjhgec"
    assert fake.inputs == [("doorid" + str(i)).encode() for i in range(14)]


def test_part2_2(monkeypatch: pytest.MonkeyPatch) -> None:
    # An empty door id is a door id like any other: the hash input is just the index, and each digest's sixth
    # character picks the position that its seventh character then fills.
    digests = [qualify(str(i), str(i)) for i in range(8)]
    fake = FakeMd5(digests)
    monkeypatch.setattr("hashlib.md5", fake)
    _, p2 = solve_parts("", 2)
    assert p2 == "01234567"
    assert fake.inputs == [str(i).encode() for i in range(8)]


# ----------- Both parts ------------


def test_both_parts(monkeypatch: pytest.MonkeyPatch) -> None:
    # get_p1 drains the first ten digests, then get_p2 continues with the next fourteen; the passwords differ,
    # so a solver mixing the parts up cannot pass.
    fake = FakeMd5(TEST_DIGESTS_1 + TEST_DIGESTS_2)
    monkeypatch.setattr("hashlib.md5", fake)
    assert solve_parts(TEST_STRING_1) == ("abcdef09", "adfjhgec")
