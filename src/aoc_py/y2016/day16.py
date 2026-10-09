"""
2016 day 16 - Dragon Checksum

Expand the data with dragon_curve until it is at least the requested size, take the prefix and repeatedly fold
adjacent pairs into a checksum until the length is odd (or one). Straightforward string solution; part 2 still
finishes in a couple of seconds.
"""

PART1_DISK_SIZE = 272
PART2_DISK_SIZE = 35651584

COMPLEMENT = str.maketrans("01", "10")


def dragon_curve(a: str) -> str:
    return a + "0" + a[::-1].translate(COMPLEMENT)


def checksum(a: str) -> str:
    while len(a) > 1 and len(a) % 2 == 0:
        a = "".join("1" if x == y else "0" for x, y in zip(a[::2], a[1::2]))
    return a


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
        p1 = str(p.get_checksum(PART1_DISK_SIZE))
    if part in (None, 2):
        p2 = str(p.get_checksum(PART2_DISK_SIZE))

    return p1, p2
