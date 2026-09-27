"""
2019 day 13 - Care Package

- Step 1: Run the game program, collecting every output triple (x, y, tile id) that is sent before it
  requests input, storing the tiles in a dict keyed by coordinates.
- Step 2: Count the tiles with id 2 (blocks) for part 1; the program is given no input for this part.
- Step 3: For part 2, enable free play by overwriting memory position 0 with 2 (two coins), then run the
  program, steering the joystick (-1/0/1) at each input request to move the paddle's x-position toward
  the ball, somewhat like a game of Arkanoid (e.g. if ball < paddle, steer left). Track the score triple
  at x,y=(-1, 0) and return it when the program halts.
"""

from enum import Enum

from aoc_py.y2019.intcode import Intcode, IntResult


class TileId(Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    HORIZONTAL_PADDLE = 3
    BALL = 4


class Joystick(Enum):
    NEUTRAL = 0
    LEFT = -1
    RIGHT = 1


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__cpu = Intcode(list(map(int, rawstr.split(","))))

    def get_p1(self) -> int:
        self.__cpu.reboot()
        tiles: dict[tuple[int, int], TileId] = {}
        output_buffer: list[int] = []
        while True:
            val, res = self.__cpu.run_program()
            if res == IntResult.OUTPUT:
                output_buffer.append(val)
                if len(output_buffer) == 3:
                    x, y, t = output_buffer
                    tiles[(x, y)] = TileId(t)
                    output_buffer = []
            else:
                break
        return sum([1 for t in tiles if tiles[t] == TileId.BLOCK])

    def get_p2(self) -> int:
        self.__cpu.reboot()
        self.__cpu.override_program(0, 2)
        score = 0
        ball = 0
        paddle = 0
        output_buffer: list[int] = []
        while True:
            val, res = self.__cpu.run_program()
            if res == IntResult.WAIT_INPUT:
                if ball < paddle:
                    self.__cpu.add_input(Joystick.LEFT.value)
                elif ball > paddle:
                    self.__cpu.add_input(Joystick.RIGHT.value)
                else:
                    self.__cpu.add_input(Joystick.NEUTRAL.value)
            elif res == IntResult.OUTPUT:
                output_buffer.append(val)
                if len(output_buffer) == 3:
                    x, y, t = output_buffer
                    if (x, y) == (-1, 0):
                        score = t
                    else:
                        if TileId(t) == TileId.BALL:
                            ball = x
                        elif TileId(t) == TileId.HORIZONTAL_PADDLE:
                            paddle = x
                    output_buffer = []
            else:  # Halted
                break
        return score


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
