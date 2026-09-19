"""
2016 day 16 - Dragon Checksum

Basically a brute-force solution, gets part 2 done in a second or so.
There are some fancier solutions out there, I might return to check those out some rainy day...
"""


def dragon_curve(a: str) -> str:
    b = "".join(["1" if c == "0" else "0" for c in reversed(a)])
    return a + "0" + b


def checksum(a: str) -> str:
    if len(a) % 2 != 0:
        return a
    else:
        b = ""
        for i in range(0, len(a), 2):
            if a[i] == a[i + 1]:
                b += "1"
            else:
                b += "0"
        return checksum(b)


class InputData:
    def __init__(self, s: str) -> None:
        self.__startdata = s

    def get_checksum(self, disksize: int) -> str:
        data = self.__startdata
        while len(data) < disksize:
            data = dragon_curve(data)
        return checksum(data[0:disksize])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_checksum(272))
    if part in (None, 2):
        p2 = str(p.get_checksum(35651584))

    return p1, p2
