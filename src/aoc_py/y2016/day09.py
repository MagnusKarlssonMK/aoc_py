"""
2016 day 9 - Explosives in Cyberspace

A marker (AxB) consumes the next A characters as payload and repeats them B times: part 1 counts the
payload raw as A*B without looking inside it, part 2 decompresses it first -- recursing into any
markers in the payload -- and counts the result B times. Everything else counts as one literal
character. Walk the string with a file pointer, using find() to locate each marker's closing paren.
"""


def get_decompressed_len(filedata: str, recurse: bool) -> int:
    total = 0
    fp = 0
    filesize = len(filedata)
    while fp < filesize:
        if filedata[fp] == "(":
            fp += 1
            end = filedata.find(")", fp)
            if end == -1:
                end = filesize
            m = filedata[fp:end]
            fp = end + 1
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
