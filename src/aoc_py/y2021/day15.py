"""
2021 day 15 - Chiton

Part 1

Pretty much a basic Djikstra exercise.

Part 2

Expand the graph according to the updated rules and re-run the shortest-path calculation.
I chose to convert the grid to an adjacency list format, anticipating that to be beneficial for Part 2. Which it turned
out not to quite be the case, but it's actually faster than keeping it in a basic grid format and calculating neighbors
on the fly.

As a small potential optimization, both parts could be kept in the same 'expanded' object and an input parameter
to the 'get' function could set the limits on which parts of the grid can be used.
"""

from heapq import heappop, heappush


class InputData:
    def __init__(self, rawstr: str, expanded: bool = False) -> None:
        grid = rawstr.splitlines()
        self.__height = len(grid)
        self.__width = len(grid[0])
        if expanded:
            self.__height *= 5
            self.__width *= 5
        self.__adj: dict[tuple[int, int], list[tuple[int, int, int]]] = {}
        for row in range(self.__height):
            for col in range(self.__width):
                self.__adj[(row, col)] = []
                for direction in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
                    if (
                        0 <= row + direction[0] < self.__height
                        and 0 <= col + direction[1] < self.__width
                    ):
                        row_div = (row + direction[0]) // len(grid)
                        row_mod = (row + direction[0]) % len(grid)
                        col_div = (col + direction[1]) // len(grid[0])
                        col_mod = (col + direction[1]) % len(grid[0])
                        # Note - value wraps around to 1, not 0
                        value = (
                            1
                            + (int(grid[row_mod][col_mod]) - 1 + row_div + col_div) % 9
                        )
                        self.__adj[(row, col)].append(
                            (row + direction[0], col + direction[1], value)
                        )

    def get_minimum_risk(self) -> int:
        start = 0, 0
        end = self.__height - 1, self.__width - 1
        costs: dict[tuple[int, int], int] = {start: 0}
        visited: set[tuple[int, int]] = set()
        queue: list[tuple[int, tuple[int, int]]] = []
        heappush(queue, (0, start))
        while queue:
            c, node = heappop(queue)
            visited.add(node)
            if node == end:
                return c
            for n_row, n_col, n_cost in self.__adj[node]:
                if (n_row, n_col) not in visited:
                    newcost = costs[node] + n_cost
                    if (n_row, n_col) not in costs or costs[(n_row, n_col)] > newcost:
                        costs[(n_row, n_col)] = newcost
                        heappush(queue, (newcost, (n_row, n_col)))
        return -1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    if part in (None, 1):
        p = InputData(inputdata)
        p1 = str(p.get_minimum_risk())
    if part in (None, 2):
        p = InputData(inputdata, True)
        p2 = str(p.get_minimum_risk())

    return p1, p2
