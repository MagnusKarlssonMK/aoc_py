"""
2016 day 16 - Dragon Checksum

Expand the data with dragon_curve until it is at least the requested size, take the prefix and repeatedly fold
adjacent pairs into a checksum until the length is odd (or one). Straightforward string solution; part 2 still
finishes in a couple of seconds.
"""

from itertools import pairwise
from typing import Final

PART1_DISK_SIZE: Final = 272
PART2_DISK_SIZE: Final = 35651584


def count_ones(prefix_ones: list[int], length: int) -> int:
    # Lengths of consecutive dragon levels: initially L_0 and L_1. After the loop, `level_len` is
    # the smallest L_k >= length and `prev_len` is L_{k-1}.
    prev_len = len(prefix_ones) - 1
    level_len = 2 * prev_len + 1
    while level_len < length:
        prev_len = level_len
        level_len = 2 * prev_len + 1

    result = 0

    # Peel off one dragon level per iteration. `length` strictly decreases and the loop stops as
    # soon as the remaining prefix fits inside the input.
    while length >= len(prefix_ones):
        # Descend to the level with prev_len < length <= level_len. Halving works because
        # L_k / 2 == L_{k-1} under integer division.
        while length <= prev_len:
            prev_len //= 2
            level_len //= 2

        # `remaining = L_k - length`, and `t = L - L_{k-1} - 1` bits are taken from the flipped
        # tail, so `t == prev_len - remaining`. Those tail ones cancel the whole-level ones,
        # leaving the recursion `ones(L) = t + ones(remaining)`.
        remaining = level_len - length
        result += prev_len - remaining
        length = remaining

    return result + prefix_ones[length]


class InputData:
    def __init__(self, s: str) -> None:
        self.__prefix_ones = [0]
        for c in s:
            ones = self.__prefix_ones[-1]
            if c == "1":
                self.__prefix_ones.append(ones + 1)
            else:
                self.__prefix_ones.append(ones)

    def get_checksum(self, disk_size: int) -> str:
        # After `m` checksum halvings each output bit is the parity of a 2^m-bit block; since
        # disk_size is odd * 2^m, that block size is the lowest set bit (2^m).
        block_size = disk_size & -disk_size
        number_of_blocks = disk_size // block_size

        # `counts[i]` is the number of ones in the first `i` blocks, so the difference between
        # neighbours is the popcount of one whole block.
        counts = [
            count_ones(self.__prefix_ones, i * block_size)
            for i in range(number_of_blocks + 1)
        ]

        return "".join(
            "1" if (after - before) % 2 == 0 else "0"
            for before, after in pairwise(counts)
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_checksum(PART1_DISK_SIZE))
    if part in (None, 2):
        p2 = str(p.get_checksum(PART2_DISK_SIZE))

    return p1, p2
