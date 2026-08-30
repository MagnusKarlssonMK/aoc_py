"""
2022 day 1 - Calorie Counting

Part 1

Simply parse the input a store it in a list sorted by total calories, and the largest value is the answer.

Part 2

From the same list, just take the sum of the top three.
"""

class Elf:
    def __init__(self, calories: list[int]) -> None:
        self.calories: list[int] = calories
        self.totalcalories: int = sum(calories)


class InputData:
    def __init__(self, rawstr: str) -> None:
        blocks = rawstr.split('\n\n')
        self.__elfs = sorted([Elf(list(map(int, elf.splitlines()))) for elf in blocks],
                             key=lambda tot: tot.totalcalories, reverse=True)

    def get_p1(self) -> int:
        return self.__elfs[0].totalcalories

    def get_p2(self) -> int:
        return sum([self.__elfs[num].totalcalories for num in range(3)])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
        p1, p2 = "-1"
        p = InputData(inputdata)
        if part in (None, 1):
            p1 = str(p.get_p1())
        if part in (None, 2):
            p2 = str(p.get_p2())

        return p1, p2
