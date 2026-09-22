"""
2017 day 9 - Stream Processing
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__s = s

    def get_score_and_garbage(self) -> tuple[int, int]:
        i = 0
        garbage_count = 0
        score = 0
        level = 1
        while i < len(self.__s):
            match self.__s[i]:
                case "<":
                    i += 1
                    while i < len(self.__s):
                        match self.__s[i]:
                            case "!":
                                i += 1
                            case ">":
                                break
                            case _:
                                garbage_count += 1
                        i += 1
                case "{":
                    score += level
                    level += 1
                case "}":
                    level -= 1
                case _:
                    pass
            i += 1
        return score, garbage_count


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_score_and_garbage()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
