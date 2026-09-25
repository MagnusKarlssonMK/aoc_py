"""
2019 day 6 - Universal Orbit Map

Store the orbits in two formats inside an orbit class - one dict to get all the objects orbiting a certain object,
and one 'reversed' variant for Part 2 to get the parent object for each object. From there it's simple recursion
to get the answer for Part 1. For Part 2, recurse through the second dict to get the paths from YOU -> COM and
SAN -> COM, then find where those two paths meet and get the answer from the remaining length of both paths.
"""


class InputData:
    def __init__(self, s: str):
        self.__orbits: dict[str, list[str]] = {}
        self.__orbiting: dict[str, str] = {}
        self.__you = ""
        self.__santa = ""
        for line in s.splitlines():
            left, right = line.split(")")
            if left not in self.__orbits:
                self.__orbits[left] = [right]
            else:
                self.__orbits[left].append(right)
            if right == "YOU":
                self.__you = left
            if right == "SAN":
                self.__santa = left
            self.__orbiting[right] = left

    def get_p1(self) -> int:
        return sum(self.__get_all_orbits(x) for x in self.__orbits)

    def __get_all_orbits(self, obj: str) -> int:
        return (
            0
            if obj not in self.__orbits
            else sum(1 + self.__get_all_orbits(x) for x in self.__orbits[obj])
        )

    def get_p2(self) -> int:
        you_path = [self.__you]
        while you_path[-1] != "COM":
            you_path.append(self.__orbiting[you_path[-1]])
        santa_path = [self.__santa]
        while santa_path[-1] != "COM":
            santa_path.append(self.__orbiting[santa_path[-1]])
        while you_path and santa_path and you_path[-1] == santa_path[-1]:
            del you_path[-1]
            del santa_path[-1]
        # Note: we chopped off also the connecting node, so it should have been this +1. But we also want the number
        # of edges, not number of nodes, so it would be number of nodes -1. So it cancels out.
        return len(you_path) + len(santa_path)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
