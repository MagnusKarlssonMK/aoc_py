"""
2020 day 21 - Allergen Assessment

For each allergen, intersect the ingredient lists of every food that mentions it to get the set of
candidate ingredients. Repeatedly: drop already-known ingredients from the candidates, assign the
allergen of any candidate set that has shrunk to one, and remove the allergen. Ingredients left
without an allergen are the safe ones.
"""


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__ingredient_list: list[list[str]] = []
        self.__allergen_candidates: dict[str, set[str]] = {}
        self.__ingredients: set[str] = set()
        for line in rawstr.splitlines():
            left, right = line.strip(")").split("(contains ")
            ingredients = left.split()
            self.__ingredient_list.append(ingredients)
            for allergen in right.split(", "):
                candidates = set(ingredients)
                if allergen in self.__allergen_candidates:
                    candidates &= self.__allergen_candidates[allergen]
                self.__allergen_candidates[allergen] = candidates
            self.__ingredients.update(ingredients)

    def __resolve_allergens(self) -> dict[str, str]:
        candidates = {a: set(c) for a, c in self.__allergen_candidates.items()}
        known: dict[str, str] = {}
        changed = True
        while changed:
            changed = False
            resolved: list[str] = []
            for allergen, ingredients in candidates.items():
                ingredients.difference_update(known)
                if len(ingredients) == 1:
                    known[next(iter(ingredients))] = allergen
                    resolved.append(allergen)
                    changed = True
            for allergen in resolved:
                del candidates[allergen]
        return known

    def get_p1(self) -> int:
        safe = self.__ingredients - set(self.__resolve_allergens())
        return sum(len(set(food) & safe) for food in self.__ingredient_list)

    def get_p2(self) -> str:
        known = self.__resolve_allergens()
        return ",".join(sorted(known, key=known.__getitem__))


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
