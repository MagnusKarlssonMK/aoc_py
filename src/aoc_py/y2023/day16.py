"""
2023 day 16 - The Floor Will Be Lava

Store the bouncers in a dict, along with per-row and per-column dicts for faster lookups and filtering when
looking for the next possible step. Also creates an adjacency list of the bouncers coupled with the incoming direction,
i.e. every bouncer can exist in 2 / 4 entries (depending on the type of bouncer). Then, when a light source is added,
a stripped down BFS is used to traverse the bouncers and record the movement. This traversal needs to keep track of
when entering a bouncer in a direction that has already been seen and then not continue that path, since that would
otherwise likely create an endless loop.
"""

from collections import deque
from collections.abc import Callable, Generator
from enum import Enum

from aoc_py.util.point import Directions, Point


class BouncerType(Enum):
    HOR_SPLIT = "-"
    VER_SPLIT = "|"
    FWD_BOUNCE = "/"
    BCK_BOUNCE = "\\"

    def bounce_light(self, indir: Point) -> Generator[Point]:
        match self:
            case BouncerType.HOR_SPLIT:
                if indir in (Directions.LEFT, Directions.RIGHT):
                    yield indir
                else:
                    yield Directions.LEFT
                    yield Directions.RIGHT
            case BouncerType.VER_SPLIT:
                if indir in (Directions.UP, Directions.DOWN):
                    yield indir
                else:
                    yield Directions.DOWN
                    yield Directions.UP
            case BouncerType.FWD_BOUNCE:
                if indir in (Directions.UP, Directions.DOWN):
                    yield indir.rotate_right()
                else:
                    yield indir.rotate_left()
            case BouncerType.BCK_BOUNCE:
                if indir in (Directions.UP, Directions.DOWN):
                    yield indir.rotate_left()
                else:
                    yield indir.rotate_right()


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__bouncers: dict[Point, BouncerType] = {}
        self.__bouncersperrow: dict[int, list[int]] = {}
        self.__bouncerspercol: dict[int, list[int]] = {}
        lines = rawstr.splitlines()
        self.__width = len(lines[0])
        self.__height = len(lines)
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == ".":
                    continue
                # The only other characters in the grid are the four bouncers.
                self.__bouncers[Point(x, y)] = BouncerType(c)
                self.__bouncersperrow.setdefault(y, []).append(x)
                self.__bouncerspercol.setdefault(x, []).append(y)
        self.__lit_tiles: set[Point] = set()
        self.__adj: dict[tuple[Point, Point], set[tuple[Point, Point]]] = {}
        for b in self.__bouncers:
            for indir in Directions.NEIGHBORS_STRAIGHT:
                outdirs = list(self.__bouncers[b].bounce_light(indir))
                if indir in outdirs:
                    # The light carries straight on, so this is not a bouncer worth recording.
                    continue
                edges = self.__adj.setdefault((b, indir), set())
                for out in outdirs:
                    if (nextpos := self.__get_nextpos(b, out)) != b:
                        edges.add((nextpos, out))

    def __insert_light(self, pos: Point, direction: Point) -> int:
        """Inserts a light source at the given position and direction and returns the score."""
        visited: set[tuple[Point, Point]] = set()
        if pos in self.__bouncers:  # If starting on a bouncer
            head = (pos, direction)
        else:
            head = (self.__get_nextpos(pos, direction), direction)
            visited.add((pos, direction))
            self.__update_lightgrid(pos, head[0])
        lightqueue: deque[tuple[Point, Point]] = deque([head])

        while lightqueue:
            headpos, headdir = lightqueue.popleft()
            if (headpos, headdir) in visited:
                continue
            visited.add((headpos, headdir))
            for nextpos, nextdir in self.__adj.get((headpos, headdir), set()):
                lightqueue.append((nextpos, nextdir))
                self.__update_lightgrid(headpos, nextpos)
        score = len(self.__lit_tiles)
        self.__lit_tiles = set()
        return score

    def __get_nextpos(self, pos: Point, direction: Point) -> Point:
        """Returns the position the light reaches next along direction, which is the first bouncer
        that turns or splits it, or the far edge of the grid when every bouncer passes it on."""
        horizontal = direction in (Directions.LEFT, Directions.RIGHT)
        backward = direction in (Directions.LEFT, Directions.UP)
        along, line = (pos.x, pos.y) if horizontal else (pos.y, pos.x)
        perline = self.__bouncersperrow if horizontal else self.__bouncerspercol
        if line in perline:
            onside: Callable[[int], bool] = (
                (lambda c: c < along) if backward else (lambda c: c > along)
            )
            for coord in sorted(filter(onside, perline[line]), reverse=backward):
                bouncer = Point(coord, line) if horizontal else Point(line, coord)
                if direction not in self.__bouncers[bouncer].bounce_light(direction):
                    return bouncer
        if horizontal:
            return Point(0 if backward else self.__width - 1, line)
        return Point(line, 0 if backward else self.__height - 1)

    def __update_lightgrid(self, frompos: Point, topos: Point) -> None:
        startrow = min(frompos.y, topos.y)
        startcol = min(frompos.x, topos.x)
        for drow in range(abs(frompos.y - topos.y) + 1):
            for dcol in range(abs(frompos.x - topos.x) + 1):
                self.__lit_tiles.add(Point(startcol + dcol, startrow + drow))

    def get_p1(self) -> int:
        return self.__insert_light(Point(0, 0), Directions.RIGHT)

    def get_p2(self) -> int:
        width, height = self.__width, self.__height
        result = 0
        for y in range(height):
            result = max(result, self.__insert_light(Point(0, y), Directions.RIGHT))
            result = max(
                result, self.__insert_light(Point(width - 1, y), Directions.LEFT)
            )
        for x in range(width):
            result = max(result, self.__insert_light(Point(x, 0), Directions.DOWN))
            result = max(
                result, self.__insert_light(Point(x, height - 1), Directions.UP)
            )
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
