"""
2016 day 9 - Explosives in Cyberspace
"""


def get_decompressed_len(filedata: str, recurse: bool) -> int:
    total = 0
    fp = 0
    filesize = len(filedata)
    while fp < filesize:
        if filedata[fp] == "(":
            fp += 1
            marker = []
            while fp < filesize:
                if (d := filedata[fp]) != ")":
                    marker.append(d)
                    fp += 1
                else:
                    break
            fp += 1
            m = "".join(marker)
            a, b = m.split("x", 1)
            a = int(a)
            b = int(b)
            if recurse:
                total += b * get_decompressed_len(filedata[fp : fp + a], True)
            else:
                total += a * b
            fp += a
        else:
            fp += 1
            total += 1
    return total


class InputData:
    def __init__(self, s: str) -> None:
        self.__filedata = s

    def get_p1(self) -> int:
        return get_decompressed_len(self.__filedata, False)

    def get_p2(self) -> int:
        return get_decompressed_len(self.__filedata, True)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
