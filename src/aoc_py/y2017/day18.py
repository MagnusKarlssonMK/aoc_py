"""
2017 day 18 - Duet

Another assembly simulator of sorts. Nothing special about part 1, but a bit more tricky with part 2 since we now have
two programs running in parallel and communcicating with messages. Mostly just a matter of having two instances of
everything, keeping track of the progam states and toggling the 'running' program.
"""

from dataclasses import dataclass
from enum import Enum


class Operation(Enum):
    SND = "snd"
    SET = "set"
    ADD = "add"
    MUL = "mul"
    MOD = "mod"
    RCV = "rcv"
    JGZ = "jgz"


@dataclass(frozen=True)
class Instr:
    op: Operation
    attr1: str = ""
    attr2: str = ""


class State(Enum):
    IDLE = 1
    RECEIVING = 2
    DONE = 3


class Register:
    def __init__(self, regs: set[str], pval: int) -> None:
        self.__regs: dict[str, int] = {r: 0 for r in regs}
        self.__regs["p"] = pval

    def get_value(self, attr: str) -> int:
        if attr in self.__regs:
            return self.__regs[attr]
        return int(attr)

    def set_value(self, reg: str, val: int) -> None:
        self.__regs[reg] = val

    def add_value(self, reg: str, val: int) -> None:
        self.__regs[reg] += val

    def mul_value(self, reg: str, val: int) -> None:
        self.__regs[reg] *= val

    def mod_value(self, reg: str, val: int) -> None:
        self.__regs[reg] %= val


class InputData:
    def __init__(self, s: str) -> None:
        self.__registers: set[str] = set()
        self.__instr: list[Instr] = []
        for line in s.splitlines():
            t = line.split()
            self.__instr.append(Instr(Operation(t[0]), *t[1:]))
            for w in t[1:]:
                if not w[-1].isdigit():
                    self.__registers.add(w)

    def get_p1(self) -> int:
        sp = 0
        regs = Register(self.__registers, 0)
        sound = None
        while 0 <= sp < len(self.__instr):
            i = self.__instr[sp]
            match i.op:
                case Operation.SND:
                    sound = regs.get_value(i.attr1)
                case Operation.SET:
                    regs.set_value(i.attr1, regs.get_value(i.attr2))
                case Operation.ADD:
                    regs.add_value(i.attr1, regs.get_value(i.attr2))
                case Operation.MUL:
                    regs.mul_value(i.attr1, regs.get_value(i.attr2))
                case Operation.MOD:
                    regs.mod_value(i.attr1, regs.get_value(i.attr2))
                case Operation.RCV:
                    if regs.get_value(i.attr1) != 0 and sound:
                        return sound
                case Operation.JGZ:
                    if regs.get_value(i.attr1) > 0:
                        sp += regs.get_value(i.attr2)
                        continue
            sp += 1
        return -1

    def get_p2(self) -> int:
        sp = [0, 0]
        regs = [Register(self.__registers, 0), Register(self.__registers, 1)]
        states = [State.IDLE, State.IDLE]
        inbox: list[list[int]] = [[], []]
        running = 0
        send_count = 0
        while states[running] == State.IDLE or (
            states[running] == State.RECEIVING and inbox[running]
        ):
            i = self.__instr[sp[running]]
            match i.op:
                case Operation.SND:
                    inbox[(running + 1) % 2].append(regs[running].get_value(i.attr1))
                    sp[running] += 1
                    if running == 1:
                        send_count += 1
                case Operation.SET:
                    regs[running].set_value(i.attr1, regs[running].get_value(i.attr2))
                    sp[running] += 1
                case Operation.ADD:
                    regs[running].add_value(i.attr1, regs[running].get_value(i.attr2))
                    sp[running] += 1
                case Operation.MUL:
                    regs[running].mul_value(i.attr1, regs[running].get_value(i.attr2))
                    sp[running] += 1
                case Operation.MOD:
                    regs[running].mod_value(i.attr1, regs[running].get_value(i.attr2))
                    sp[running] += 1
                case Operation.RCV:
                    if inbox[running]:
                        regs[running].set_value(
                            i.attr1, regs[running].get_value(str(inbox[running].pop(0)))
                        )
                        states[running] = State.IDLE
                        sp[running] += 1
                    else:
                        states[running] = State.RECEIVING
                        running = (running + 1) % 2
                case Operation.JGZ:
                    if regs[running].get_value(i.attr1) > 0:
                        sp[running] += regs[running].get_value(i.attr2)
                    else:
                        sp[running] += 1
            if not 0 <= sp[running] < len(self.__instr):
                states[running] = State.DONE
                running = (running + 1) % 2
        return send_count


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
