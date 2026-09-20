"""
2016 day 22 - Grid Computing

Part 1

Just parse the data into a dict representing the nodes keyed with (x, y) of each node. Then go through the
possible pair combinations of the nodes and count how many are fulfilling the conditions for transfer.

Part 2

Uhhhh.... So.... I guess this is kind of the equivalent of getting Rick-rolled in AoC...

All pairs in part 1 contain the same empty node (x=15, y=29 in my case). So for part 2 we first need to move that empty
node to the top right corner, and the path is partially blocked by a line of full nodes. Once there we can move the
'G' node to the left by stepping around it, so moving it one tile costs 5 steps. This is easiest done by simply printing
the grid and then calculate the answer by hand, but to keep it at least a little bit as a programming exercise:
1. Find the closest path from the empty node to G with a quick BFS, just to get a generic solution to handle the full
nodes.
2. Add the row length multiplied by 5 for the cost of moving G to the top left.
"""

import re
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
        # Step 1 - find nbr of steps to move zero-node to G
        g_steps = 0
        node_g = self.__max_x, 0
        seen: set[tuple[int, int]] = set()
        queue = [(self.__zeronode, 0)]
        while queue:
            nextnode, steps = queue.pop(0)
            if nextnode == node_g:
                g_steps = steps
                break
            if nextnode in seen:
                continue
            seen.add(nextnode)
            for d in ((-1, 0), (1, 0), (0, -1)):  # No reason to ever go +1 in y
                n = nextnode[0] + d[0], nextnode[1] + d[1]
                if (
                    n in self.__nodes
                    and self.__nodes[n].used < self.__nodes[self.__zeronode].size
                ):
                    queue.append((n, steps + 1))

        # Step 2 - add the cost for moving G to top left
        return g_steps + (5 * (self.__max_x - 1))


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
