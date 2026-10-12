"""
2018 day 25 - Four-Dimensional Adventure

Any two points within manhattan distance 3 of each other belong to the same
constellation, so the constellations are just the connected components of that graph.
Union-find counts them directly: start with one constellation per point, and decrement
the count every time two distinct constellations get joined.
"""


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__points = [
            tuple(map(int, line.split(","))) for line in rawstr.splitlines()
        ]

    def get_p1(self) -> int:
        points = self.__points
        constellations = len(points)
        parent = list(range(constellations))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i in range(len(points) - 1):
            a0, a1, a2, a3 = points[i]
            for j in range(i + 1, len(points)):
                b0, b1, b2, b3 = points[j]
                if abs(a0 - b0) + abs(a1 - b1) + abs(a2 - b2) + abs(a3 - b3) <= 3:
                    rooti, rootj = find(i), find(j)
                    if rooti != rootj:
                        parent[rooti] = rootj
                        constellations -= 1
        return constellations


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = "-"

    return p1, p2
