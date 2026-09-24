"""
2018 day 11 - Chronal Charge

Using 'summed-area table' algorithm. (https://en.wikipedia.org/wiki/Summed-area_table)
"""


class InputData:
    __GRIDSIZE = 300

    def __init__(self, serialnbr: str) -> None:
        self.__serialnbr = int(serialnbr)
        self.__grid = [
            [0 for _ in range(InputData.__GRIDSIZE + 2)]
            for _ in range(InputData.__GRIDSIZE + 2)
        ]
        for y in range(1, InputData.__GRIDSIZE + 1):
            for x in range(1, InputData.__GRIDSIZE + 1):
                rackid = x + 10
                power = str((rackid * y + self.__serialnbr) * rackid)
                if len(power) >= 3:
                    power = int(power[-3]) - 5
                else:
                    power = -5
                self.__grid[y][x] = (
                    power
                    + self.__grid[y - 1][x]
                    + self.__grid[y][x - 1]
                    - self.__grid[y - 1][x - 1]
                )

    def __get_best_fuelcell(
        self, fuelcell_size: int
    ) -> tuple[int, int, int]:  # [x, y, power]
        max_power = 0
        max_fuelcell_x, max_fuelcell_y = 0, 0
        for y in range(1, InputData.__GRIDSIZE + 1 - fuelcell_size):
            for x in range(1, InputData.__GRIDSIZE + 1 - fuelcell_size):
                power = (
                    self.__grid[y - 1][x - 1]
                    + self.__grid[y + fuelcell_size - 1][x + fuelcell_size - 1]
                    - self.__grid[y + fuelcell_size - 1][x - 1]
                    - self.__grid[y - 1][x + fuelcell_size - 1]
                )
                if power > max_power:
                    max_power = power
                    max_fuelcell_x, max_fuelcell_y = x, y
        return max_fuelcell_x, max_fuelcell_y, max_power

    def get_p1(self) -> str:
        x, y, _ = self.__get_best_fuelcell(3)
        return f"{x},{y}"

    def get_p2(self) -> str:
        max_power = 0
        max_fuelcell_x, max_fuelcell_y, max_fuelcell_size = 0, 0, 0
        for size in range(1, InputData.__GRIDSIZE + 1):
            x, y, power = self.__get_best_fuelcell(size)
            if power > max_power:
                max_power = power
                max_fuelcell_x, max_fuelcell_y, max_fuelcell_size = x, y, size
        return f"{max_fuelcell_x},{max_fuelcell_y},{max_fuelcell_size}"


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
