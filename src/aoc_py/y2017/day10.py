"""
2017 day 10 - Knot Hash
"""

from typing import Any


def rotate_left(x: list[Any], steps: int) -> None:
    if x:
        steps %= len(x)
        x[:] = x[steps:] + x[:steps]


def rotate_right(x: list[Any], steps: int) -> None:
    rotate_left(x, -steps)


def reverse_slice(x: list[Any], start: int, stop: int) -> None:
    x[start:stop] = reversed(x[start:stop])


def generate_hash(lengths: list[int], buffersize: int, rounds: int) -> list[int]:
    nbrs: list[int] = [i for i in range(buffersize)]
    current_position = 0
    skipsize = 0

    for _ in range(rounds):
        for length in lengths:
            n = length + skipsize
            reverse_slice(nbrs, 0, length)
            rotate_left(nbrs, n % buffersize)
            current_position += n
            skipsize += 1
    rotate_right(nbrs, current_position % buffersize)
    return list(nbrs)


class InputData:
    def __init__(self, s: str) -> None:
        self.__inputstr = s

    def get_p1(self, buffer_len: int) -> int:
        lengths: list[int] = (
            [] if not self.__inputstr else [int(c) for c in self.__inputstr.split(",")]
        )
        nbrs = generate_hash(lengths, buffer_len, 1)
        return nbrs[0] * nbrs[1]

    def get_p2(self, buffer_len: int) -> str:
        lengths: list[int] = [ord(c) for c in self.__inputstr]
        lengths += [17, 31, 73, 47, 23]
        sparse = generate_hash(lengths, buffer_len, 64)
        dense = []

        for start in range(0, len(sparse) - len(sparse) % 16, 16):
            n = 0
            for value in sparse[start : start + 16]:
                n ^= value
            dense.append(f"{n:02x}")

        return "".join(dense)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1(256))
    if part in (None, 2):
        p2 = p.get_p2(256)

    return p1, p2
