"""
2023 day 20 - Pulse Propagation

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

    def send(self, inmsg: Message, pulse: Pulse) -> list[Message]:
        """One message to every output, all of them carrying the same pulse"""
        return [Message(to, inmsg.receiver, pulse) for to in self.outputs]

    def process_signal(self, inmsg: Message) -> list[Message]:
        """Broadcaster behavior as default"""
        return self.send(inmsg, Pulse.LOW)

    def reset(self) -> None:
        pass


class Flipflop(Module):
    def __init__(self, outputs: list[str]) -> None:
        super().__init__(outputs)
        self.is_on: bool = False

    @override
    def process_signal(self, inmsg: Message) -> list[Message]:
        if inmsg.pulse == Pulse.HIGH:
            return []
        self.is_on = not self.is_on
        return self.send(inmsg, Pulse.HIGH if self.is_on else Pulse.LOW)

    @override
    def reset(self) -> None:
        self.is_on = False


class Conjunction(Module):
    def __init__(self, outputs: list[str]) -> None:
        super().__init__(outputs)
        self.inputs: dict[str, Pulse] = {}

    def add_input(self, newinput: str) -> None:
        self.inputs[newinput] = Pulse.LOW

    @override
    def process_signal(self, inmsg: Message) -> list[Message]:
        self.inputs[inmsg.sender] = inmsg.pulse
        allhigh = all(state == Pulse.HIGH for state in self.inputs.values())
        return self.send(inmsg, Pulse.LOW if allhigh else Pulse.HIGH)

    @override
    def reset(self) -> None:
        for i in self.inputs:
            self.inputs[i] = Pulse.LOW


class CommunicationSystem:
    def __init__(self, rawstr: str) -> None:
        self.__modules: dict[str, Module] = {}
        rxcon = ""
        for line in rawstr.splitlines():
            name, out = line.split(" -> ")
            outputs = out.split(", ")
            module: Module
            if name[0] == "%":
                module = Flipflop(outputs)
                name = name[1:]
            elif name[0] == "&":
                module = Conjunction(outputs)
                name = name[1:]
            else:
                module = Module(outputs)
            self.__modules[name] = module
            if "rx" in outputs:
                rxcon = name

        # Initialize conjunctions. Only a conjunction can feed 'rx', so only a conjunction has
        # to know about its inputs up front, and they all start out low.
        for name, module in self.__modules.items():
            if isinstance(module, Conjunction):
                for sender, other in self.__modules.items():
                    if name in other.outputs:
                        module.add_input(sender)

        # Find the modules connecting to the module connecting to 'rx'
        self.__rxcon_inputs: list[str] = [
            name for name, module in self.__modules.items() if rxcon in module.outputs
        ]

    def __reset(self) -> None:
        for module in self.__modules.values():
            module.reset()

    def get_push_1000(self) -> int:
        pulsecount: dict[Pulse, int] = {Pulse.LOW: 0, Pulse.HIGH: 0}
        for _ in range(1000):
            msgqueue = [Message("broadcaster", "button", Pulse.LOW)]
            while msgqueue:
                newmsg = msgqueue.pop(0)
                pulsecount[newmsg.pulse] += 1
                if newmsg.receiver in self.__modules:
                    msgqueue.extend(
                        self.__modules[newmsg.receiver].process_signal(newmsg)
                    )
        # Reset module states before exiting
        self.__reset()
        return math.prod(pulsecount.values())

    def get_rx_mincount(self) -> int:
        pushcount = 0
        rxcon_inputs = {rx: 0 for rx in self.__rxcon_inputs}
        while any(count == 0 for count in rxcon_inputs.values()):
            pushcount += 1
            msgqueue = [Message("broadcaster", "button", Pulse.LOW)]
            while msgqueue:
                newmsg = msgqueue.pop(0)
                if newmsg.receiver in self.__modules:
                    for m in self.__modules[newmsg.receiver].process_signal(newmsg):
                        msgqueue.append(m)
                        if (
                            newmsg.receiver in self.__rxcon_inputs
                            and m.pulse == Pulse.HIGH
                            and rxcon_inputs[newmsg.receiver] == 0
                        ):
                            rxcon_inputs[newmsg.receiver] = pushcount
        # Reset module states before exiting
        self.__reset()
        return math.lcm(*rxcon_inputs.values())


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = CommunicationSystem(inputdata)
    if part in (None, 1):
        p1 = str(p.get_push_1000())
    if part in (None, 2):
        p2 = str(p.get_rx_mincount())

    return p1, p2
