"""
2019 day 23 - Category Six

- Step 1: Boot 50 copies of the network interface controller program, each with its own address as initial
  input, and process them round-robin. Three consecutive outputs form a packet (destination, X, Y) that is
  queued for that node, and a node that runs out of input gets -1. The Y value of the first packet addressed
  to 255 is the answer to part 1.
- Step 2: The computer at address 255 is the NAT: it stores the last packet it received. Once a whole lap
  produces no new traffic the network is idle and the NAT sends its stored packet to node 0, waking the
  network up. The answer to part 2 is the first delivered Y that repeats the previous delivery, i.e. the
  network has stabilised.
"""

from dataclasses import dataclass

from aoc_py.y2019.intcode import Intcode, IntResult


@dataclass
class Computer:
    cpu: Intcode
    output_buffer: list[int]
    input_buffer: list[tuple[int, int]]


class InputData:
    def __init__(self, rawstr: str) -> None:
        nic = list(map(int, rawstr.split(",")))
        self.__computers = {i: Computer(Intcode(nic), [], []) for i in range(50)}

    def get_first_packets_y_value(self) -> tuple[int, int]:
        [self.__computers[i].cpu.add_input(i) for i, _ in enumerate(self.__computers)]
        i = -1
        p1 = p2 = None
        nat = None
        nat_previous_y = -1
        network_idle = True
        while not p1 or not p2:
            i = (i + 1) % len(self.__computers)
            if i == 0:
                if network_idle and nat:
                    x = nat.pop(0)
                    y = nat.pop(0)
                    self.__computers[0].cpu.add_input(x)
                    self.__computers[0].cpu.add_input(y)
                    network_idle = False
                    if y == nat_previous_y:
                        p2 = y
                        break
                    else:
                        nat_previous_y = y
                else:
                    network_idle = True
            while True:
                val, res = self.__computers[i].cpu.run_program()
                if res == IntResult.OUTPUT:
                    self.__computers[i].output_buffer.append(val)
                    if len(self.__computers[i].output_buffer) == 3:
                        dest = self.__computers[i].output_buffer.pop(0)
                        x = self.__computers[i].output_buffer.pop(0)
                        y = self.__computers[i].output_buffer.pop(0)
                        if dest == 255:
                            if not p1:
                                p1 = y
                            nat = [x, y]
                        else:
                            self.__computers[dest].input_buffer.append((x, y))
                            network_idle = False
                elif res == IntResult.WAIT_INPUT:
                    if self.__computers[i].input_buffer:
                        x, y = self.__computers[i].input_buffer.pop(0)
                        self.__computers[i].cpu.add_input(x)
                        self.__computers[i].cpu.add_input(y)
                        network_idle = False
                    else:
                        self.__computers[i].cpu.add_input(-1)
                    break
                else:
                    break
        # The loop can only exit once `p2` is set, and `p1` is set before any NAT delivery, so the
        # fallback is not reachable - it just narrows `p1` to int for the type checker.
        return p1 if p1 is not None else -1, p2


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_first_packets_y_value()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
