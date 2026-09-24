"""
2017 day 14 - Disk Defragmentation

Re-use the knot hasher from day 10, and use that to generate a grid of one's and zero's, which in turn is converted
to an adjacency graph of neighboring ones. The answer for part 1 is then the number of keys in that graph / dict.
For part 2, simply traverse through the graph with a simple BFS to identify the groups, similar to the solution for
day 12.
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


def get_knot_hash(s: str, buffer_len: int = 256) -> str:
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


class InputData:
    def __init__(self, s: str) -> None:
        grid = [
            bin(int(get_knot_hash(s + f"-{i}"), 16)).zfill(130)[2:] for i in range(128)
        ]
        width = len(grid[0])
        height = len(grid)
        self.__adj: dict[tuple[int, int], set[tuple[int, int]]] = {}
        for y, line in enumerate(grid):
            for x, c in enumerate(line):
                if c == "1":
                    if (x, y) not in self.__adj:
                        self.__adj[(x, y)] = set()
                    for nx, ny in [(x + dx, y + dy) for dx, dy in ((0, 1), (1, 0))]:
                        if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == "1":
                            self.__adj[(x, y)].add((nx, ny))
                            if (nx, ny) not in self.__adj:
                                self.__adj[(nx, ny)] = set()
                            self.__adj[(nx, ny)].add((x, y))

    def get_p1(self) -> int:
        return len(self.__adj)

    def get_p2(self) -> int:
        groups = 0
        squares = list(self.__adj.keys())
        while squares:
            seen: set[tuple[int, int]] = set()
            queue = [squares[0]]
            while queue:
                current = queue.pop(0)
                if current in seen:
                    continue
                seen.add(current)
                queue.extend(self.__adj[current])
                squares.remove(current)
            groups += 1
        return groups


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
