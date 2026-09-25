"""
2019 day 4 - Secure Container

Valid passwords are generated with an iter function, minimizing the number of numbers to loop though by first finding
the lowest valid password and then for each increment, adjust to follow the rules if necessary before completing
the loop.
"""

from collections.abc import Generator


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__lower, self.__upper = list(map(int, rawstr.split("-")))

    def __generate_pwds(self, exactlytwo: bool) -> Generator[int]:
        v_list = [int(c) for c in str(self.__lower)]
        # Find the first valid initial value starting from 'lower' - the value never decreases
        tmp = 0
        for i in range(1, len(v_list)):
            if tmp > 0:
                v_list[i] = tmp
            elif v_list[i] < v_list[i - 1]:
                v_list[i] = v_list[i - 1]
                tmp = v_list[i]
        value = int("".join(map(str, v_list)))

        while value <= self.__upper:
            # valid pwd if two adjacent digits are the same
            tmp = v_list[0]
            counts = [1]
            for i in range(1, len(v_list)):
                if v_list[i] == tmp:
                    counts[-1] += 1
                else:
                    counts.append(1)
                    tmp = v_list[i]

            if not exactlytwo:
                if any(c > 1 for c in counts):
                    yield value
            else:
                if any(c == 2 for c in counts):
                    yield value

            # step the value, make sure to follow the 'never decreases' rule
            for i in reversed(range(len(v_list))):
                v_list[i] += 1
                if v_list[i] <= 9:
                    for j in range(i + 1, len(v_list)):
                        v_list[j] = v_list[i]
                    break
            value = int("".join(map(str, v_list)))

    def get_password_count(self, exactlytwo: bool = False) -> int:
        return sum([1 for _ in self.__generate_pwds(exactlytwo)])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_password_count())
    if part in (None, 2):
        p2 = str(p.get_password_count(True))

    return p1, p2
