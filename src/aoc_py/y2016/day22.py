"""
2016 day 22 - Grid Computing

Part 1

Parse the data into a dict of nodes keyed by (x, y). Then count the ordered pairs where a non-empty node's data would
fit in another node's available space.

Part 2

The empty node (used == 0) is the only node that can move data around, so the plan is:
1. BFS the empty node up to the goal node G at the top-right corner, treating nodes whose used is larger than the empty
   node's capacity as walls.
2. Once it is there, shifting G one column to the left takes 5 moves (the empty node has to loop around it), so add
   5 * (max_x - 1) for walking G to the top-left.
"""

import re
from collections import deque
from dataclasses import dataclass
from itertools import combinations


@dataclass
class Node:
    size: int
    used: int
    avail: int
    use: int


class InputData:
    def __init__(self, s: str) -> None:
        self.__nodes: dict[tuple[int, int], Node] = {}
        self.__max_x = 0
        self.__max_y = 0
        self.__zeronode: tuple[int, int] = -1, -1
        for line in s.splitlines():
            nbrs = list(map(int, re.findall(r"\d+", line)))
            if len(nbrs) == 6:
                self.__nodes[(nbrs[0], nbrs[1])] = Node(*nbrs[2:])
                self.__max_x = max(self.__max_x, nbrs[0])
                self.__max_y = max(self.__max_y, nbrs[1])
                if (self.__zeronode == (-1, -1)) and nbrs[3] == 0:
                    self.__zeronode = nbrs[0], nbrs[1]

    def get_p1(self) -> int:
        count = 0
        for a, b in combinations(self.__nodes, 2):
            if (0 < self.__nodes[a].used <= self.__nodes[b].avail) or (
                0 < self.__nodes[b].used <= self.__nodes[a].avail
            ):
                count += 1
        return count

    def get_p2(self) -> int:
        # Step 1 - BFS the empty node to G, avoiding nodes too full for it to absorb.
        node_g = self.__max_x, 0
        hole_size = self.__nodes[self.__zeronode].size
        seen = {self.__zeronode}
        queue = deque([(self.__zeronode, 0)])
        g_steps = 0
        while queue:
            nextnode, steps = queue.popleft()
            if nextnode == node_g:
                g_steps = steps
                break
            for d in ((-1, 0), (1, 0), (0, -1)):  # No reason to ever go +1 in y
                n = nextnode[0] + d[0], nextnode[1] + d[1]
                if (
                    n in self.__nodes
                    and n not in seen
                    and self.__nodes[n].used <= hole_size
                ):
                    seen.add(n)
                    queue.append((n, steps + 1))

        # Step 2 - add the cost for moving G to the top left (one tile costs 5 moves).
        return g_steps + (5 * (self.__max_x - 1))


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
