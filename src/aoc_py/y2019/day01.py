"""
2019 day 1 - The Tyranny of the Rocket Equation
"""


def calc_mass(mass: int, countfuel: bool = False) -> int:
    fuel_own_mass = max(0, (mass // 3) - 2)
    if fuel_own_mass == 0 or not countfuel:
        return fuel_own_mass
    return fuel_own_mass + calc_mass(fuel_own_mass, countfuel)


class InputData:
    def __init__(self, s: str) -> None:
        self.__nbrs = list(map(int, s.splitlines()))

    def get_p1(self) -> int:
        return sum([calc_mass(nbr) for nbr in self.__nbrs])

    def get_p2(self) -> int:
        return sum([calc_mass(nbr, True) for nbr in self.__nbrs])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
