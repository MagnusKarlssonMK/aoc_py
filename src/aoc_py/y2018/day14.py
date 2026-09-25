"""
2018 day 14 - Chocolate Charts

Brute force, kinda slow part 2. Not sure if there is some kind of repeating pattern in the generation that could be
exploited, couldn't really find any after some quick experimentation.
"""


class InputData:
    __START_POSITIONS = (0, 1)
    __START_RECIPES = (3, 7)

    def __init__(self, s: str) -> None:
        self.__inputnbr = s
        self.__scoreboard: list[int] = list(InputData.__START_RECIPES)
        self.__elfs = list(InputData.__START_POSITIONS)

    def __reset(self) -> None:
        self.__scoreboard = list(InputData.__START_RECIPES)
        self.__elfs = list(InputData.__START_POSITIONS)

    def __make_recipes(self) -> int:
        newcount = 1
        current_sum = sum([self.__scoreboard[e] for e in self.__elfs])
        if current_sum > 9:
            newcount = 2  # Return the number of new recipes, so we can avoid making unnecessary comparisons in part 2
            self.__scoreboard.append(1)
        self.__scoreboard.append(current_sum % 10)
        self.__elfs = [
            (e + self.__scoreboard[e] + 1) % len(self.__scoreboard) for e in self.__elfs
        ]
        return newcount

    def get_p1(self) -> int:
        limit = int(self.__inputnbr)
        while len(self.__scoreboard) < limit + 10:
            self.__make_recipes()
        result = int("".join([str(i) for i in self.__scoreboard[limit : limit + 10]]))
        self.__reset()
        return result

    def get_p2(self) -> int:
        nbrlist = [int(c) for c in self.__inputnbr]
        nbrlistlen = len(nbrlist)
        while True:
            # If two new recipes were added, we need to check also -1 from the end
            if (
                self.__make_recipes() > 1
                and self.__scoreboard[-nbrlistlen - 1 : -1] == nbrlist
            ):
                result = len(self.__scoreboard) - nbrlistlen - 1
                break
            if self.__scoreboard[-nbrlistlen:] == nbrlist:
                result = len(self.__scoreboard) - nbrlistlen
                break
        self.__reset()
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
