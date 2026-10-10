"""
2017 day 10 - Knot Hash

Each reversal is applied to the front of the list, with the current position tracked by rotating the whole list
instead. A final right-rotation of the accumulated offset returns the list to its true order.
"""


def rotate_left(x: list[int], steps: int) -> None:
    if x:
        steps %= len(x)
        x[:] = x[steps:] + x[:steps]


def rotate_right(x: list[int], steps: int) -> None:
    rotate_left(x, -steps)


def reverse_slice(x: list[int], start: int, stop: int) -> None:
    x[start:stop] = reversed(x[start:stop])


def generate_hash(lengths: list[int], buffersize: int, rounds: int) -> list[int]:
    numbers: list[int] = list(range(buffersize))
    total_steps = 0
    skip = 0

    for _ in range(rounds):
        for length in lengths:
            steps = length + skip
            reverse_slice(numbers, 0, length)
            rotate_left(numbers, steps % buffersize)
            total_steps += steps
            skip += 1
    rotate_right(numbers, total_steps % buffersize)
    return numbers


class InputData:
    def __init__(self, s: str) -> None:
        self.__inputstr = s

    def get_p1(self, buffer_len: int) -> int:
        lengths: list[int] = (
            [] if not self.__inputstr else [int(c) for c in self.__inputstr.split(",")]
        )
        numbers = generate_hash(lengths, buffer_len, 1)
        return numbers[0] * numbers[1]

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
