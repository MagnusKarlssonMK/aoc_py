"""
Part 1

The optimal distance will be on the median value, so simply calculate this using the median function
from statistics module, and then determine the total fuel cost at that value.

Part 2

The optimal distance will rather be on the mean value, so similar approach to part 1, but also check
the surrounding values to be safe against rounding errors.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__crabs = list(map(int, s.split(",")))

    def __get_median(self) -> int:
        crabs = sorted(self.__crabs)
        middle = len(crabs) // 2
        return (
            (crabs[middle - 1] + crabs[middle]) // 2
            if len(crabs) % 2 == 0
            else crabs[middle]
        )

    def get_mean(self) -> int:
        return sum(self.__crabs) // len(self.__crabs)

    def get_p1(self) -> int:
        calnbr = self.__get_median()
        return sum([abs(crab - calnbr) for crab in self.__crabs])

    def get_p2(self) -> int:
        distance = self.get_mean()
        cost = min(
            self.__scaling_cost(distance),
            self.__scaling_cost(distance - 1),
            self.__scaling_cost(distance + 1),
        )
        return cost

    def __scaling_cost(self, calnbr: int) -> int:
        return sum(
            [d * (d + 1) // 2 for d in [abs(crab - calnbr) for crab in self.__crabs]]
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
