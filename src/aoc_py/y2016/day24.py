"""
2016 day 24 - Air Duct Spelunking

Travelling salesman sort of. Doing this in multiple steps:

First set up the grid as an adj list, and find the numbers in the grid while doing that.
Then find the edges and path lengths between all numbers, giving us a graph of numbers with all the edges, and we can
throw away the grid after that.
Based on this we can then do BFS with keeping a sorted list of the visited numbers in the state.

For part 2, simply modify the stop condition of the BFS to also require the current point to be 0.
"""


class InputData:
    def __init__(self, rawstr: str) -> None:
        adj_list: dict[tuple[int, int], set[tuple[int, int]]] = {}
        nbrs: dict[tuple[int, int], int] = {}
        grid = rawstr.splitlines()
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col != "#":
                    if col.isdigit():
                        nbrs[(r, c)] = int(col)
                    if (r, c) not in adj_list:
                        adj_list[(r, c)] = set()
                    for dr, dc in ((1, 0), (0, 1)):
                        if grid[r + dr][c + dc] != "#":
                            adj_list[(r, c)].add((r + dr, c + dc))
                            if (r + dr, c + dc) not in adj_list:
                                adj_list[(r + dr, c + dc)] = set()
                            adj_list[(r + dr, c + dc)].add((r, c))
        self.__nbrs: dict[int, set[tuple[int, int]]] = {}  # nbr -> {(nbr, steps), ...}
        nbrs_seen: dict[tuple[int, int], tuple[int, bool]] = {}
        for nbr, value in nbrs.items():
            points_seen: set[tuple[int, int]] = set()
            queue: list[tuple[tuple[int, int], int, bool]] = [(nbr, 0, False)]
            while queue:
                point, steps, stepover = queue.pop(0)
                # Stepover to keep track of when we have already seen at least one number on this path, to avoid
                # adding direct edges later when it's really an indirect path through another number
                if point in points_seen:
                    continue
                points_seen.add(point)
                if point in nbrs and point != nbr:
                    if (value, nbrs[point]) not in nbrs_seen or steps < nbrs_seen[
                        (value, nbrs[point])
                    ][0]:
                        nbrs_seen[(value, nbrs[point])] = steps, stepover
                    stepover = True
                for n in adj_list[point]:
                    queue.append((n, steps + 1, stepover))
        for (n_from, n_to), (steps, stepover) in nbrs_seen.items():
            if not stepover:
                if n_from not in self.__nbrs:
                    self.__nbrs[n_from] = set()
                self.__nbrs[n_from].add((n_to, steps))

    def get_shortest_path(self, returntozero: bool = False) -> int:
        seen_states = {}
        shortest_path = None
        queue: list[tuple[int, int, tuple[int, ...]]] = [
            (0, 0, (0,))
        ]  # point, steps, seenpoints(sorted)
        while queue:
            currentpoint, steps, currentseen = queue.pop(0)
            if (
                (currentpoint, currentseen) in seen_states
                and steps >= seen_states[(currentpoint, currentseen)]
            ) or (shortest_path and steps > shortest_path):
                continue
            seen_states[(currentpoint, currentseen)] = steps
            if len(currentseen) >= len(self.__nbrs) and (
                currentpoint == 0 or not returntozero
            ):
                if shortest_path:
                    shortest_path = min(shortest_path, steps)
                else:
                    shortest_path = steps
            for p, n in self.__nbrs[currentpoint]:
                cs = set(currentseen)
                cs.add(p)
                cs = tuple(sorted(cs))
                queue.append((p, steps + n, cs))
        if not shortest_path:
            shortest_path = -1  # Should never happen, just to keep linter happy
        return shortest_path


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_shortest_path())
    if part in (None, 2):
        p2 = str(p.get_shortest_path(True))

    return p1, p2
