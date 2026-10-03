"""
2022 day 21 - Monkey Math

Part 1

Each monkey either yells a number or applies one of +, -, * or / to two other monkeys. Evaluating a monkey is a
memoised recursive walk, since a monkey is often referenced by more than one other monkey.

Part 2

The monkey 'humn' is the unknown. Starting from root's requirement that its two children are equal, walk down the
single path that depends on 'humn'. At every step the other child is fully evaluable, so its value gives the target
the unknown child has to reach, and the operation is inverted to solve for that child's target. The walk ends at
'humn' with the answer.
"""

import operator
from collections.abc import Callable
from typing import Final, Literal, cast

_Op = Literal["+", "-", "*", "/"]
_IntOp = Callable[[int, int], int]


class InputData:
    __OPS: Final[dict[_Op, _IntOp]] = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": cast(_IntOp, operator.floordiv),
    }

    def __init__(self, rawstr: str) -> None:
        self.__numbers: dict[str, int] = {}
        self.__operations: dict[str, tuple[str, str, _Op]] = {}
        for line in rawstr.splitlines():
            name, expr = line.split(": ")
            if expr.isdigit():
                self.__numbers[name] = int(expr)
            else:
                left, op, right = expr.split()
                self.__operations[name] = (left, right, cast(_Op, op))

    def __value(self, monkey: str, memo: dict[str, int]) -> int:
        if monkey not in memo:
            left, right, op = self.__operations[monkey]
            memo[monkey] = InputData.__OPS[op](
                self.__value(left, memo), self.__value(right, memo)
            )
        return memo[monkey]

    def __depends_on_humn(self, monkey: str, memo: dict[str, bool]) -> bool:
        if monkey not in memo:
            if monkey == "humn":
                memo[monkey] = True
            elif monkey in self.__numbers:
                memo[monkey] = False
            else:
                left, right, _ = self.__operations[monkey]
                memo[monkey] = self.__depends_on_humn(
                    left, memo
                ) or self.__depends_on_humn(right, memo)
        return memo[monkey]

    def __solve_for_humn(
        self, monkey: str, target: int, values: dict[str, int], deps: dict[str, bool]
    ) -> int:
        if monkey == "humn":
            return target
        left, right, op = self.__operations[monkey]
        if self.__depends_on_humn(left, deps):
            other = self.__value(right, values)
            match op:
                case "+":
                    target -= other
                case "-":
                    target += other
                case "*":
                    target //= other
                case "/":
                    target *= other
            return self.__solve_for_humn(left, target, values, deps)
        other = self.__value(left, values)
        match op:
            case "+":
                target -= other
            case "-":
                target = other - target
            case "*":
                target //= other
            case "/":
                target = other // target
        return self.__solve_for_humn(right, target, values, deps)

    def get_yellnumber(self, monkey: str) -> int:
        return self.__value(monkey, dict(self.__numbers))

    def get_humn_number(self) -> int:
        values = dict(self.__numbers)
        del values["humn"]
        deps: dict[str, bool] = {}
        left, right, _ = self.__operations["root"]
        if self.__depends_on_humn(left, deps):
            return self.__solve_for_humn(
                left, self.__value(right, values), values, deps
            )
        return self.__solve_for_humn(right, self.__value(left, values), values, deps)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_yellnumber("root"))
    if part in (None, 2):
        p2 = str(p.get_humn_number())

    return p1, p2
