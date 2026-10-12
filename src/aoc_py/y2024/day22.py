"""
2024 day 22 - Monkey Market

Each buyer's secret number is evolved 2000 times and the ones digit of every value is its
price. The secret numbers are advanced together with numpy, and each window of four price
changes is packed into a single integer that is combined with the buyer's row; a stable
np.unique then keeps only the first occurrence of each window per buyer. Part 1 sums the
2000th secret number of every buyer, part 2 returns the most bananas any window can earn.
"""

import numpy as np

STEPS = 2000
SECRET_MASK = 0xFFFFFF
PRICE_OFFSET = 9  # changes run from -9 to 9 and are shifted into 5-bit slots
WINDOW_SHIFT = 5
WINDOW_BITS = 4 * WINDOW_SHIFT
BUYER_SHIFT = WINDOW_BITS
WINDOW_MASK = (1 << WINDOW_BITS) - 1


def advance(secrets: np.ndarray) -> None:
    """Evolve every secret number one step, in place."""
    secrets ^= secrets << 6
    secrets &= SECRET_MASK
    secrets ^= secrets >> 5
    secrets &= SECRET_MASK
    secrets ^= secrets << 11
    secrets &= SECRET_MASK


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__secret_numbers = [int(line) for line in rawstr.splitlines()]

    def get_p1(self) -> int:
        secrets = np.array(self.__secret_numbers, dtype=np.int64)
        for _ in range(STEPS):
            advance(secrets)
        return int(secrets.sum())

    def get_p2(self) -> int:
        count = len(self.__secret_numbers)
        secrets = np.array(self.__secret_numbers, dtype=np.int64)
        prices = np.empty((count, STEPS + 1), dtype=np.int8)
        prices[:, 0] = secrets % 10
        for step in range(1, STEPS + 1):
            advance(secrets)
            prices[:, step] = secrets % 10
        changes = (prices[:, 1:].astype(np.int32) - prices[:, :-1]) + PRICE_OFFSET
        windows = (
            changes[:, 0 : STEPS - 3]
            | (changes[:, 1 : STEPS - 2] << WINDOW_SHIFT)
            | (changes[:, 2 : STEPS - 1] << (2 * WINDOW_SHIFT))
            | (changes[:, 3:STEPS] << (3 * WINDOW_SHIFT))
        )
        # Combining the buyer index with the packed window turns "first occurrence per
        # buyer" into "first occurrence overall", which a stable np.unique provides.
        buyers = (np.arange(count, dtype=np.int64)[:, None] << BUYER_SHIFT) | windows
        unique, first = np.unique(buyers.ravel(), return_index=True)
        bananas = prices[:, 4 : STEPS + 1].ravel()[first]
        totals = np.bincount(
            unique & WINDOW_MASK, weights=bananas, minlength=1 << WINDOW_BITS
        )
        return int(totals.max())


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
