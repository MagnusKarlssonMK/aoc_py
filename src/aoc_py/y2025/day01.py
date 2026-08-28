class InputData:
    def __init__(self, s: str) -> None:
        self.__rotations = [
            int(line[1:]) if line[0] == "R" else -int(line[1:])
            for line in s.splitlines()
        ]

    def get_p1(self) -> int:
        zero_count = 0
        dial = 50
        for v in self.__rotations:
            dial = (dial + v) % 100
            if dial == 0:
                zero_count += 1
        return zero_count

    def get_p2(self) -> int:
        zero_count = 0
        dial = 50
        for v in self.__rotations:
            if v >= 0:
                zero_count += (dial + v) // 100
            elif dial == 0:
                zero_count += abs(v) // 100
            else:
                zero_count += (100 - dial + abs(v)) // 100
            dial = (dial + v) % 100
        return zero_count


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
