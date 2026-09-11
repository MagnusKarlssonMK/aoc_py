"""
2020 day 21 - Allergen Assessment
"""


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__ingredient_list: list[list[str]] = []
        self.__allergens: dict[str, set[str]] = {}
        self.__ingredients: set[str] = set()
        self.__known: dict[str, str] = {}
        for line in rawstr.splitlines():
            left, right = line.strip(")").split("(contains ")
            self.__ingredient_list.append(left.split())
            i = set(self.__ingredient_list[-1])
            self.__ingredients.update(i)
            for a in right.split(", "):
                if a not in self.__allergens:
                    self.__allergens[a] = i
                else:
                    self.__allergens[a] = i & self.__allergens[a]

    def get_p1(self) -> int:
        changed = True
        while changed:
            changed = False
            newallergens: dict[str, set[str]] = {}
            for allergen in self.__allergens:
                if len(self.__allergens[allergen]) == 1:
                    self.__known[next(iter(self.__allergens[allergen]))] = allergen
                    changed = True
                else:
                    newallergens[allergen] = set()
                    for i in self.__allergens[allergen]:
                        if i in self.__known:
                            changed = True
                        else:
                            newallergens[allergen].add(i)
            if changed:
                self.__allergens = dict(newallergens)
        non_allergens = self.__ingredients ^ set(self.__known.keys())
        return sum([len(set(i) & non_allergens) for i in self.__ingredient_list])

    def get_p2(self) -> str:
        result = ""
        for k, _ in sorted(self.__known.items(), key=lambda x: x[1]):
            result += "," + k
        return result.strip(",")


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1 = p.get_p1()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
