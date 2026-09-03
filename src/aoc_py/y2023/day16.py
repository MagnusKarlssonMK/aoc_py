"""
2023 day 16 - The Floor Will Be Lava

Store the bouncers in a Grid class, along with per-row and per-column dicts for faster lookups and filtering when
looking for the next possible step. Also creates an adjacency list of the bouncers coupled with the incoming direction,
i.e. every bouncer can exist in 2 / 4 entries (depending on the type of bouncer). Then, when a light source is added,
a stripped down BFS is used to traverse the bouncers and record the movement. This traversal needs to keep track of
when entering a bouncer in a direction that has already been seen and then not continue that path, since that would
otherwise likely create an endless loop.
"""

from collections.abc import Generator
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
        grid: list[str] = []
        for y, line in enumerate(rawstr.splitlines()):
            grid.append(line)
            for x, c in enumerate(line):
                if c == ".":  # not in ['-', '|', '/', '\\']: #BouncerType:
                    continue
                self.__bouncers[Point(x, y)] = BouncerType(c)
                if y in self.__bouncersperrow:
                    self.__bouncersperrow[y].append(x)
                else:
                    self.__bouncersperrow[y] = [x]
                if x in self.__bouncerspercol:
                    self.__bouncerspercol[x].append(y)
                else:
                    self.__bouncerspercol[x] = [y]
        self.__width = len(grid[0])
        self.__height = len(grid)
        self.__lit_tiles: set[Point] = set()
        self.__adj: dict[tuple[Point, Point], set[tuple[Point, Point]]] = {}
        for b in self.__bouncers:
            for indir in Directions.NEIGHBORS_STRAIGHT:
                outdir = [d for d in self.__bouncers[b].bounce_light(indir)]
                if indir not in outdir:
                    if (b, indir) not in self.__adj:
                        self.__adj[(b, indir)] = set()
                    for out in outdir:
                        if (nextpos := self.__get_nextpos(b, out)) != b:
                            self.__adj[(b, indir)].add((nextpos, out))

    def __insert_light(self, pos: Point, direction: Point) -> int:
        """Inserts a light source at the given position and direction and returns the score."""
        visited: set[tuple[Point, Point]] = set()
        if pos in self.__bouncers:  # If starting on a bouncer
            lightqueue = [(pos, direction)]
        else:
            nextpos = self.__get_nextpos(pos, direction)
            lightqueue = [(nextpos, direction)]
            visited.add((pos, direction))
            self.__update_lightgrid(pos, nextpos)

        while lightqueue:
            headpos, headdir = lightqueue.pop(0)
            if (headpos, headdir) not in visited:
                if (headpos, headdir) in self.__adj:
                    for n_p, n_d in self.__adj[(headpos, headdir)]:
                        lightqueue.append((n_p, n_d))
                        self.__update_lightgrid(headpos, n_p)
                visited.add((headpos, headdir))
        score = self.__get_lightscore()
        self.__reset_lightgrid()
        return score

    def __get_nextpos(self, pos: Point, direction: Point) -> Point:
        if direction == Directions.RIGHT:
            if pos.y in self.__bouncersperrow:
                cols = sorted(filter(lambda x: x > pos.x, self.__bouncersperrow[pos.y]))
                for i in cols:
                    bounced = [
                        d
                        for d in self.__bouncers[Point(i, pos.y)].bounce_light(
                            direction
                        )
                    ]
                    if direction not in bounced:
                        return Point(i, pos.y)
            return Point(self.__width - 1, pos.y)
        elif direction == Directions.LEFT:
            if pos.y in self.__bouncersperrow:
                cols = sorted(
                    filter(lambda x: x < pos.x, self.__bouncersperrow[pos.y]),
                    reverse=True,
                )
                for i in cols:
                    bounced = [
                        d
                        for d in self.__bouncers[Point(i, pos.y)].bounce_light(
                            direction
                        )
                    ]
                    if direction not in bounced:
                        return Point(i, pos.y)
            return Point(0, pos.y)
        elif direction == Directions.UP:
            if pos.x in self.__bouncerspercol:
                rows = sorted(
                    filter(lambda x: x < pos.y, self.__bouncerspercol[pos.x]),
                    reverse=True,
                )
                for i in rows:
                    bounced = [
                        d
                        for d in self.__bouncers[Point(pos.x, i)].bounce_light(
                            direction
                        )
                    ]
                    if direction not in bounced:
                        return Point(pos.x, i)
            return Point(pos.x, 0)
        else:  # Directions.DOWN:
            if pos.x in self.__bouncerspercol:
                rows = sorted(filter(lambda x: x > pos.y, self.__bouncerspercol[pos.x]))
                for i in rows:
                    bounced = [
                        d
                        for d in self.__bouncers[Point(pos.x, i)].bounce_light(
                            direction
                        )
                    ]
                    if direction not in bounced:
                        return Point(pos.x, i)
            return Point(pos.x, self.__height - 1)

    def __update_lightgrid(self, frompos: Point, topos: Point) -> None:
        startrow = min(frompos.y, topos.y)
        startcol = min(frompos.x, topos.x)
        for drow in range(abs(frompos.y - topos.y) + 1):
            for dcol in range(abs(frompos.x - topos.x) + 1):
                self.__lit_tiles.add(Point(startcol + dcol, startrow + drow))

    def __get_lightscore(self) -> int:
        return len(self.__lit_tiles)

    def __reset_lightgrid(self) -> None:
        self.__lit_tiles = set()

    def get_p1(self) -> int:
        return self.__insert_light(Point(0, 0), Directions.RIGHT)

    def get_p2(self) -> int:
        result = 0
        for y in range(self.__height):
            result = max(result, self.__insert_light(Point(0, y), Directions.RIGHT))
            result = max(
                result, self.__insert_light(Point(self.__width - 1, y), Directions.LEFT)
            )
        for x in range(self.__width):
            result = max(result, self.__insert_light(Point(x, 0), Directions.DOWN))
            result = max(
                result, self.__insert_light(Point(x, self.__height - 1), Directions.UP)
            )
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
