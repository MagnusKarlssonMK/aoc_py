def calculate(block: str) -> int:
    total = 0
    for part in block.split("mul("):
        mul = part.split(")")
        if len(mul) > 1:  # contained at least one closing parenthesis
            nbrs = mul[0].split(",")
            if len(nbrs) == 2 and nbrs[0].isdigit() and nbrs[1].isdigit():
                total += int(nbrs[0]) * int(nbrs[1])
    return total


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__program = rawstr

    def get_p1(self) -> int:
        return calculate(self.__program)

    def get_p2(self) -> int:
        return sum([calculate(block.split("don't()")[0]) for block in self.__program.split("do()")])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
