"""
2017 day 9 - Stream Processing
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__s = s

    def get_score_and_garbage(self) -> tuple[int, int]:
        score = 0
        level = 0
        garbage_count = 0
        it = iter(self.__s)
        for c in it:
            match c:
                case "<":
                    for c in it:
                        if c == "!":
                            next(it)
                        elif c == ">":
                            break
                        else:
                            garbage_count += 1
                case "{":
                    level += 1
                    score += level
                case "}":
                    level -= 1
                case _:
                    pass
        return score, garbage_count


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    r1, r2 = InputData(inputdata).get_score_and_garbage()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
