TEST_STRING_1 = """deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1"""

from aoc_py.y2019.day22 import InputData, solve_parts


def apply_shuffle(deck: list[int], s: str) -> list[int]:
    """Applies every instruction in s to the deck once, by direct simulation."""
    for line in s.splitlines():
        if line.startswith("deal into new"):
            deck = deck[::-1]
        elif line.startswith("cut"):
            n = int(line.split()[-1])
            deck = deck[n:] + deck[:n]
        else:  # "deal with increment n"
            n = int(line.split()[-1])
            newdeck = [0] * len(deck)
            for i, card in enumerate(deck):
                newdeck[i * n % len(deck)] = card
            deck = newdeck
    return deck


# ----------- Part 1 ------------


def test_part1_1() -> None:
    p1, _ = solve_parts(TEST_STRING_1, 1)
    assert p1 == "1219"


# ----------- Part 2 ------------


def test_part2_1() -> None:
    _, p2 = solve_parts(TEST_STRING_1, 2)
    assert p2 == "117607927195067"


def test_part2_2() -> None:
    deck_size, passes, target = 101, 5, 37
    deck = list(range(deck_size))
    for _ in range(passes):
        deck = apply_shuffle(deck, TEST_STRING_1)
    assert deck[target] == 45  # brute force: the card that ends up at position 37
    assert (
        InputData(TEST_STRING_1).get_p2(
            deck_size=deck_size, shuffle_count=passes, target=target
        )
        == deck[target]
    )
