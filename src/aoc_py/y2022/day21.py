"""
2022 day 21 - Monkey Math

Part 1

Parse the input and store in a dict, use recursion to extrtact the root value.

Part 2

Remove 'humn' from the known dict, and update root operation to '-': root = lhs-rhs = 0
Then extract all the monkeys not dependent on 'humn' through recursion similar to Part 1 and add those to known dict.
Finally, add root=0 as a known value, then 'reverse' the remaining operations (all dict keys should now have one
known value on the 'items' side of the dict), then one final round of recursion to calculate the remaining values.

Note: The implementation for Part 2 is really messy and can likely be cleaned up significantly / add a bit of structure.
"""

import operator
from collections.abc import Callable
from typing import Final, cast

_IntOp = Callable[[int, int], int]


class InputData:
    __OPS: Final[dict[str, Callable[[int, int], int]]] = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": cast(_IntOp, operator.floordiv),
    }
    __REV_OPS: Final = {"+": "-", "-": "+", "*": "/", "/": "*"}

    def __init__(self, rawstr: str) -> None:
        self.__inputdata: dict[str, str] = {
            left: right
            for left, right in [line.split(": ") for line in rawstr.splitlines()]
        }
        self.__known: dict[str, int] = {}
        self.__unknown: dict[str, tuple[str, str, str]] = {}
        for m in self.__inputdata:
            if self.__inputdata[m].isdigit():
                self.__known[m] = int(self.__inputdata[m])
            else:
                left, op, right = self.__inputdata[m].split()
                self.__unknown[m] = (left, right, op)

    def get_yellnumber(self, monkey: str) -> int:
        known = dict(self.__known)
        unknown = dict(self.__unknown)

        def __extractvalue(m1: str, m2: str, operation: str) -> int:
            nbrs: list[int] = []
            for n in (m1, m2):
                if n not in known:
                    known[n] = __extractvalue(*unknown[n])
                nbrs.append(known[n])
            return InputData.__OPS[operation](*nbrs)

        queue = list(unknown.keys())
        while queue:
            next_m = queue.pop(0)
            if next_m not in known:
                known[next_m] = __extractvalue(*unknown[next_m])
        return known[monkey]

    def get_humn_number(self) -> int:
        known = dict(self.__known)
        unknown = dict(self.__unknown)
        _ = known.pop("humn")
        unknown["root"] = unknown["root"][0], unknown["root"][1], "-"

        def __extractnonhuman(m1: str, m2: str, operation: str) -> tuple[bool, int]:
            nbrs: list[int] = []
            for n in (m1, m2):
                if n == "humn":
                    return False, -1
                if n not in known:
                    f, v = __extractnonhuman(*unknown[n])
                    if f:
                        known[n] = v
                    else:
                        return False, -1
                nbrs.append(known[n])
            return True, InputData.__OPS[operation](*nbrs)

        # Evaluate the monkeys not dependent on 'humn'
        queue = list(unknown.keys())
        while queue:
            next_m = queue.pop(0)
            if next_m not in known:
                found, val = __extractnonhuman(*unknown[next_m])
                if found:
                    known[next_m] = val
                    _ = unknown.pop(next_m)

        # Add the root to known and extract the remaining values from the reversed list
        known["root"] = 0
        reverse_unknown: dict[str, tuple[str, str, str]] = {}
        for k, v in unknown.items():
            l, r, o = v
            if l not in known:
                reverse_unknown[l] = k, r, InputData.__REV_OPS[o]
            if r not in known:
                match o:
                    case "+":
                        reverse_unknown[r] = k, l, "-"
                    case "-":
                        reverse_unknown[r] = l, k, "-"
                    case "*":
                        reverse_unknown[r] = k, l, "/"
                    case "/":
                        reverse_unknown[r] = l, k, "/"
                    case _:
                        pass

        def __extractvalue(m1: str, m2: str, operation: str) -> int:
            nbrs: list[int] = []
            for n in (m1, m2):
                if n not in known:
                    known[n] = __extractvalue(*reverse_unknown[n])
                nbrs.append(known[n])
            return InputData.__OPS[operation](*nbrs)

        queue = list(reverse_unknown.keys())
        while queue:
            next_m = queue.pop(0)
            if next_m not in known:
                known[next_m] = __extractvalue(*reverse_unknown[next_m])
        return known["humn"]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_yellnumber("root"))
    if part in (None, 2):
        p2 = str(p.get_humn_number())

    return p1, p2
