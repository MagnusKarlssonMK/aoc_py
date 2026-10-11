"""
2017 day 14 - Disk Defragmentation

Re-use the knot hasher from day 10 (util.knot) to generate a 128x128 grid of ones and zeroes, which is turned
into an adjacency graph of neighboring ones. Part 1 counts the "1" cells, and part 2 walks the graph to
count the connected groups.
"""

from aoc_py.util.knot import get_knot_hash


class InputData:
    def __init__(self, s: str) -> None:
        grid = [f"{int(get_knot_hash(s + f'-{i}'), 16):0128b}" for i in range(128)]
        width = len(grid[0])
        height = len(grid)
        self.__adj: dict[tuple[int, int], set[tuple[int, int]]] = {}
        for y, line in enumerate(grid):
            for x, c in enumerate(line):
                if c == "1":
                    self.__adj.setdefault((x, y), set())
                    for nx, ny in ((x, y + 1), (x + 1, y)):
                        if nx < width and ny < height and grid[ny][nx] == "1":
                            self.__adj[(x, y)].add((nx, ny))
                            self.__adj.setdefault((nx, ny), set()).add((x, y))

    def get_p1(self) -> int:
        return len(self.__adj)

    def get_p2(self) -> int:
        groups = 0
        squares = set(self.__adj)
        while squares:
            queue = [squares.pop()]
            while queue:
                for nxt in self.__adj[queue.pop()]:
                    if nxt in squares:
                        squares.remove(nxt)
                        queue.append(nxt)
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
