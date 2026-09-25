"""
2018 day 21 - Chronal Conversion

Like day 19, we now need to disassemble the program even further. Again, trying
to extract the data from the input file, but there is no guarantee that it will
work without modifications for other inputs too if there are shifts in the
program lines.
"""


class InputData:
    def __init__(self, s: str) -> None:
        lines = s.splitlines()
        self.__program = [
            (op, int(a), int(b), int(c))
            for op, a, b, c in [line.split() for line in lines[1:]]
        ]
        self.__ipreg = int(lines[0].split()[1])

    def get_p1(self, startval: int = 0) -> int:
        v1 = self.__program[7][1]
        v2 = self.__program[11][2]
        v3 = startval | self.__program[6][2]
        result = v1
        while v3 != 0:
            result += v3 & self.__program[8][2]
            result &= self.__program[10][2]
            result *= v2
            result &= self.__program[12][2]
            v3 //= self.__program[19][2]
        return result

    def get_p2(self) -> int:
        startval = 0
        count = 0
        result: dict[int, int] = {}
        while True:
            count += (startval << 8) + (startval << 16)
            startval = self.get_p1(startval)
            if startval in result:
                return max(result, key=lambda seed: result[seed])
            result[startval] = count


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
