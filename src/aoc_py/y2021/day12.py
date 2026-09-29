"""
2021 day 12 - Passage Pathing

Store the input as an adjacency list, and then perform a sort of modified BFS, where instead of saving a
'visited' list, the entire path is carried on the queue instead of just the previously visited caves, since
whether a cave may be entered again depends on what the path has already been through. Every path that
reaches 'end' is counted. For Part 2, just allow one small cave to be visited an extra time, and carry a
flag on the queue recording whether that extra visit is still unspent.

The search relies on the input having no edge between two big caves. Any cycle made up only of big caves
would admit infinitely many paths, so the puzzle never supplies one. The guard against stepping straight
back to the cave the path just came from covers the two-cave case, but not a longer big-cave cycle.
"""


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__adj: dict[str, list[str]] = {}
        for line in rawstr.splitlines():
            node1, node2 = line.split("-")
            self.__adj.setdefault(node1, []).append(node2)
            self.__adj.setdefault(node2, []).append(node1)

    def findallpaths(self, bonusstep: int = 0) -> int:
        """Returns number of possible paths from 'start' to 'end', where each small cave is
        visited at most once plus 'bonusstep' further times."""
        npaths = 0
        queue: list[tuple[str, list[str], int]] = [("start", [], bonusstep)]
        while queue:
            currentnode, path, cbonus = queue.pop(0)
            currentpath = [node for node in path]
            currentpath.append(currentnode)
            if currentnode == "end":
                npaths += 1
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
        return npaths


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.findallpaths())
    if part in (None, 2):
        p2 = str(p.findallpaths(1))

    return p1, p2
