"""
2024 day 13 - Claw Contraption

Calculates the answer basically by solving a matrix. The same function can be
used for both parts, with an argument to input the extra scaling value for part 2.
"""

class Machine:
    def __init__(self, rawstr: str):
        lines = rawstr.splitlines()
        a = lines[0].split("+")
        self.__a = int(a[1].split(",")[0]), int(a[2])
        b = lines[1].split("+")
        self.__b = int(b[1].split(",")[0]), int(b[2])
        p = lines[2].split("=")
        self.__p = int(p[1].split(",")[0]), int(p[2])

    def get_win_tokens(self, extra: int) -> int:
        p_x = self.__p[0] + extra
        p_y = self.__p[1] + extra
        i = (self.__b[0] * p_y - self.__b[1] * p_x) // (self.__a[1] * self.__b[0] - self.__a[0] * self.__b[1])
        j = (p_x - i * self.__a[0]) // self.__b[0]
        if ((p_x - i * self.__a[0]) % self.__b[0] == 0 and
            (self.__b[0] * p_y - self.__b[1] * p_x) % (self.__a[1] * self.__b[0] - self.__a[0] * self.__b[1]) == 0):
            return 3 * i + j
        return 0


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__machines = [Machine(block) for block in rawstr.split('\n\n')]

    def get_p1(self) -> int:
        return sum([m.get_win_tokens(0) for m in self.__machines])

    def get_p2(self) -> int:
        return sum([m.get_win_tokens(10_000_000_000_000) for m in self.__machines])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
        p1, p2 = "-1"
        p = InputData(inputdata)
        if part in (None, 1):
            p1 = str(p.get_p1())
        if part in (None, 2):
            p2 = str(p.get_p2())

        return p1, p2
