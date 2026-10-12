"""
2024 day 23 - LAN Party

The puzzle input is an undirected graph of computer connections. Part 1 counts the
triangles (three mutually connected computers) that contain at least one computer whose
name starts with "t". Part 2 grows a clique greedily by walking outwards from each
computer that has not already been claimed, always keeping the largest set found, and
returns its members sorted and comma-separated.
"""


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__connections: dict[str, set[str]] = {}
        for line in rawstr.splitlines():
            left, right = line.split("-")
            self.__connections.setdefault(left, set()).add(right)
            self.__connections.setdefault(right, set()).add(left)

    def get_p1(self) -> int:
        seen: set[tuple[str, ...]] = set()
        for k1, neighbors in self.__connections.items():
            if not k1.startswith("t"):
                continue
            for k2 in neighbors:
                for k3 in self.__connections[k2] & neighbors:
                    seen.add(tuple(sorted((k1, k2, k3))))
        return len(seen)

    def get_p2(self) -> str:
        # Iterating in sorted order keeps the greedy result independent of the hash order,
        # which would otherwise pick a different (possibly smaller) clique between runs.
        seen: set[str] = set()
        largest: list[str] = []
        for k1 in sorted(self.__connections):
            if k1 in seen:
                continue
            group = [k1]
            for k2 in sorted(self.__connections[k1]):
                if all(k3 in self.__connections[k2] for k3 in group):
                    seen.add(k2)
                    group.append(k2)
            if len(group) > len(largest):
                largest = group
        return ",".join(sorted(largest))


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = p.get_p2()

    return p1, p2
