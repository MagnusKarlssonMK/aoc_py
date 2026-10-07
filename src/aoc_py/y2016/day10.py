"""
2016 day 10 - Balance Bots

'value' lines feed a starting chip to a bot, 'bot' lines wire each bot's low and high destinations
(another bot or an output). Draining that instruction queue as a FIFO, a bot holding two chips emits
its low and high give-instructions and clears its slots; receiving bots enqueue theirs in turn. Part 1
is the bot that compares the target pair -- 17/61 for real input, 5/2 for the statement example,
which the value-line count tells apart. Part 2 multiplies the first chip landed in outputs 0, 1 and 2
once the queue runs dry.
"""

from collections.abc import Generator
from dataclasses import dataclass
from enum import Enum


class Node(Enum):
    BOT = 0
    OUTPUT = 1


@dataclass(frozen=True)
class Connection:
    node: Node
    number: int


class Bot:
    def __init__(self, low: Connection, high: Connection) -> None:
        self.low: Connection = low
        self.high: Connection = high
        self.values: list[int] = []

    def add_value(self, newvalue: int) -> Generator[Instruction]:
        self.values.append(newvalue)
        if len(self.values) >= 2:
            self.values.sort()
            yield Instruction(self.values[0], self.low)
            yield Instruction(self.values[1], self.high)
            self.values.clear()


@dataclass(frozen=True)
class Instruction:
    value: int
    to_bot: Connection


class InputData:
    def __init__(self, s: str) -> None:
        self.__instructions: list[Instruction] = []
        self.__bots: dict[int, Bot] = {}
        self.__outputs: dict[int, list[int]] = {}
        self.__answer: int = -1
        for line in s.splitlines():
            tokens = line.split()
            if tokens[0] == "value":
                self.__instructions.append(
                    Instruction(int(tokens[1]), Connection(Node.BOT, int(tokens[5])))
                )
            else:
                self.__bots[int(tokens[1])] = Bot(
                    Connection(
                        Node.BOT if tokens[5] == "bot" else Node.OUTPUT, int(tokens[6])
                    ),
                    Connection(
                        Node.BOT if tokens[10] == "bot" else Node.OUTPUT,
                        int(tokens[11]),
                    ),
                )
        self._simulate()

    def _simulate(self) -> None:
        val1 = 17
        val2 = 61
        if len(self.__instructions) < 8:
            # The statement example compares 5 and 2 instead.
            val1 = 5
            val2 = 2
        queue = list(self.__instructions)
        while queue:
            newinstr = queue.pop(0)
            if newinstr.to_bot.node == Node.BOT:
                compared: list[int] = []
                for n in self.__bots[newinstr.to_bot.number].add_value(newinstr.value):
                    queue.append(n)
                    compared.append(n.value)
                if val1 in compared and val2 in compared:
                    self.__answer = newinstr.to_bot.number
            else:
                if newinstr.to_bot.number not in self.__outputs:
                    self.__outputs[newinstr.to_bot.number] = [newinstr.value]
                else:
                    self.__outputs[newinstr.to_bot.number].append(newinstr.value)

    def get_p1(self) -> int:
        return self.__answer

    def get_p2(self) -> int:
        return self.__outputs[0][0] * self.__outputs[1][0] * self.__outputs[2][0]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
