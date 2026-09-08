"""
2021 day 12 - Passage Pathing

Store the input as an adjacency list, and then perform a sort of modified BFS, where instead of saving a
'visited' list, the entire path is stored instead of just previously visited. Once the end node is found, the
path is stored and finally counted once the queue is emptied. For Part 2, just add a condition that one small cave
can be visited an extra time, and add that flag to the queue.
"""


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__adj: dict[str, list[str]] = {}
        for nodes in [
            (node[0], node[1])
            for node in [line.split("-") for line in rawstr.splitlines()]
        ]:
            for i in range(2):
                if nodes[i] in self.__adj:
                    self.__adj[nodes[i]].append(nodes[(i + 1) % 2])
                else:
                    self.__adj[nodes[i]] = [nodes[(i + 1) % 2]]

    def findallpaths(self, bonusstep: int = 0) -> int:
        """Returns number of possible paths from 'start' to 'end'."""
        foundpaths: list[list[str]] = []
        queue: list[tuple[str, list[str], int]] = [("start", [], bonusstep)]
        while queue:
            currentnode, path, cbonus = queue.pop(0)
            currentpath = [node for node in path]
            currentpath.append(currentnode)
            if currentnode == "end":
                foundpaths.append(currentpath)
            else:
                for neighbor in self.__adj[currentnode]:
                    nbonus = cbonus
                    if (
                        neighbor.isupper()
                        and currentnode.isupper()
                        and neighbor == currentpath[-2]
                    ) or neighbor == "start":
                        continue
                    elif neighbor.islower() and neighbor in currentpath:
                        if nbonus > 0:
                            nbonus -= 1
                        else:
                            continue
                    queue.append((neighbor, currentpath, nbonus))
        return len(foundpaths)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.findallpaths())
    if part in (None, 2):
        p2 = str(p.findallpaths(1))

    return p1, p2
