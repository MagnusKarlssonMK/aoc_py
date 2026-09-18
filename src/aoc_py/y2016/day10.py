"""
2016 day 10 - Balance Bots

Slightly confusing description and input. Split the instructions into bot connection definitions (rows starting with
'bot') and actual instructions (rows starting with 'value'). Store bots in a dict, and put the instructions on a
queue. When adding an instruction into a bot, it will spit out new instructions if it reaches two stored values,
and then add those to the instruction queue. Monitor the bot outputs to see when the 61/17 combo shows up for the
answer to Part 1. Once the queue is emptied, the answer to part 2 is found by multiplyeing the values stored in
the first three outputs.
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

    def get_comparing_bot_id(self) -> int:
        val1 = 17
        val2 = 61
        if len(self.__instructions) < 8:
            # Assume test input
            val1 = 5
            val2 = 2
        queue = list(self.__instructions)
        answer = -1
        while queue:
            newinstr = queue.pop(0)
            if newinstr.to_bot.node == Node.BOT:
                compared: list[int] = []
                for n in self.__bots[newinstr.to_bot.number].add_value(newinstr.value):
                    queue.append(n)
                    compared.append(n.value)
                if val1 in compared and val2 in compared:
                    answer = newinstr.to_bot.number
            else:
                if newinstr.to_bot.number not in self.__outputs:
                    self.__outputs[newinstr.to_bot.number] = [newinstr.value]
                else:
                    self.__outputs[newinstr.to_bot.number].append(newinstr.value)
        return answer

    def get_output_prod(self) -> int:
        return self.__outputs[0][0] * self.__outputs[1][0] * self.__outputs[2][0]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1 = p.get_comparing_bot_id()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(p.get_output_prod())

    return p1, p2
