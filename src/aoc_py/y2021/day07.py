"""
2021 day 7 - The Treachery of Whales

Each crab sits at a horizontal position and spends one unit of fuel per step towards a
chosen target. Part 1 spends one unit per step however far it walks, so the total cost is
the sum of absolute distances, which is minimised at the median; that is taken straight from
the sorted crabs, averaging the two middle values when the count is even and taking the
single middle one when it is odd. Part 2 instead spends the step number, one unit for the
first step, two for the second, and so on, so a crab at distance d costs d * (d + 1) / 2.
That cost is minimised at the mean, which need not be a whole number, so the floored mean
and the positions either side of it are each costed and the cheapest of the three taken.
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

    def __get_mean(self) -> int:
        return sum(self.__crabs) // len(self.__crabs)

    def get_p1(self) -> int:
        target = self.__get_median()
        return sum([abs(crab - target) for crab in self.__crabs])

    def get_p2(self) -> int:
        target = self.__get_mean()
        return min(
            self.__scaling_cost(target),
            self.__scaling_cost(target - 1),
            self.__scaling_cost(target + 1),
        )

    def __scaling_cost(self, target: int) -> int:
        cost = 0
        for crab in self.__crabs:
            distance = abs(crab - target)
            cost += distance * (distance + 1) // 2
        return cost


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
