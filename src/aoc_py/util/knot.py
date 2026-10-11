"""
Shared knot-hash helpers, used by 2017 days 10 and 14.

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


def get_knot_hash(s: str, buffer_len: int = 256) -> str:
    """Hash a string with the knot-hash algorithm: ASCII lengths, 64 rounds, xor-dense hexadecimal output."""
    lengths: list[int] = [ord(c) for c in s]
    lengths += [17, 31, 73, 47, 23]
    sparse = generate_hash(lengths, buffer_len, 64)
    dense = []

    for start in range(0, len(sparse) - len(sparse) % 16, 16):
        n = 0
        for value in sparse[start : start + 16]:
            n ^= value
        dense.append(f"{n:02x}")

    return "".join(dense)
