"""
Uses classes and inheritance to implement the different module types, and an overall system class to hold them all
and provide an interface for pushing the button.
"""
import math
from dataclasses import dataclass
from enum import Enum
from typing import override


class Pulse(Enum):
    LOW = 0
    HIGH = 1


@dataclass(frozen=True)
class Message:
    receiver: str
    sender: str
    pulse: Pulse


class Module:
    def __init__(self, outputs: list[str]) -> None:
        self.outputs: set[str] = set(outputs)

    def process_signal(self, inmsg: Message) -> list[Message]:
        """Broadcaster behavior as default"""
        return [Message(to, inmsg.receiver, Pulse.LOW) for to in self.outputs]

    def reset(self) -> None:
        pass

    def add_input(self, _newinput: str) -> None:
        pass


class Flipflop(Module):
    def __init__(self, outputs: list[str]) -> None:
        super().__init__(outputs)
        self.is_on: bool = False

    @override
    def process_signal(self, inmsg: Message) -> list[Message]:
        if inmsg.pulse == Pulse.HIGH:
            return []
        else:
            if self.is_on:
                self.is_on = False
                return [Message(to, inmsg.receiver, Pulse.LOW) for to in self.outputs]
            else:
                self.is_on = True
                return [Message(to, inmsg.receiver, Pulse.HIGH) for to in self.outputs]

    @override
    def reset(self) -> None:
        self.is_on = False


class Conjunction(Module):
    def __init__(self, outputs: list[str]) -> None:
        super().__init__(outputs)
        self.inputs: dict[str, Pulse] = {}

    @override
    def add_input(self, newinput: str) -> None:
        self.inputs[newinput] = Pulse.LOW

    @override
    def process_signal(self, inmsg: Message) -> list[Message]:
        self.inputs[inmsg.sender] = inmsg.pulse
        if any(instate != Pulse.HIGH for instate in list(self.inputs.values())):
            return [Message(to, inmsg.receiver, Pulse.HIGH) for to in self.outputs]
        else:
            return [Message(to, inmsg.receiver, Pulse.LOW) for to in self.outputs]

    @override
    def reset(self) -> None:
        for i in self.inputs:
            self.inputs[i] = Pulse.LOW


class CommunicationSystem:
    def __init__(self, rawstr: str) -> None:
        self.__modules: dict[str, Module] = {}
        conjunction_ids: list[str] = []
        rxcon = ""
        for line in rawstr.splitlines():
            name, out = line.split(' -> ')
            out = out.split(', ')
            if name[0] == '%':
                self.__modules[name[1:]] = Flipflop(out)
            elif name[0] == '&':
                self.__modules[name[1:]] = Conjunction(out)
                conjunction_ids.append(name[1:])
            else:
                self.__modules[name[0:]] = Module(out)  # Broadcaster
            if "rx" in out:
                rxcon = name[1:]

        # Initialize conjunctions
        for cid in conjunction_ids:
            for m in self.__modules:
                if cid in self.__modules[m].outputs:
                    self.__modules[cid].add_input(m)

        # Find the modules connecting to the module connecting to 'rx'
        self.__rxcon_inputs: list[str] = [m for m in self.__modules if rxcon in self.__modules[m].outputs]

    def get_push_1000(self) -> int:
        pulsecount: dict[Pulse, int] = {Pulse.LOW: 0, Pulse.HIGH: 0}
        for _ in range(1000):
            msgqueue = [Message("broadcaster", "button", Pulse.LOW)]
            while msgqueue:
                newmsg = msgqueue.pop(0)
                pulsecount[newmsg.pulse] += 1
                if newmsg.receiver in self.__modules:
                    outmsgs = self.__modules[newmsg.receiver].process_signal(newmsg)
                    [msgqueue.append(m) for m in outmsgs]
        # Reset module states before exiting
        for m in self.__modules:
            self.__modules[m].reset()
        return math.prod(pulsecount.values())

    def get_rx_mincount(self) -> int:
        pushcount = 0
        rxcon_inputs = {rx: 0 for rx in self.__rxcon_inputs}
        while any(count == 0 for count in list(rxcon_inputs.values())):
            pushcount += 1
            msgqueue = [Message("broadcaster", "button", Pulse.LOW)]
            while msgqueue:
                newmsg = msgqueue.pop(0)
                if newmsg.receiver in self.__modules:
                    for m in self.__modules[newmsg.receiver].process_signal(newmsg):
                        msgqueue.append(m)
                        if (newmsg.receiver in self.__rxcon_inputs and m.pulse == Pulse.HIGH and
                                rxcon_inputs[newmsg.receiver] == 0):
                            rxcon_inputs[newmsg.receiver] = pushcount
        # Reset module states before exiting
        for m in self.__modules:
            self.__modules[m].reset()
        return math.lcm(*list(rxcon_inputs.values()))


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
        p1, p2 = "-1"
        p = CommunicationSystem(inputdata)
        if part in (None, 1):
            p1 = str(p.get_push_1000())
        if part in (None, 2):
            p2 = str(p.get_rx_mincount())

        return p1, p2
