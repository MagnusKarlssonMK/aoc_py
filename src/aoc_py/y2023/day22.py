"""
2023 day 22 - Sand Slabs

Sort of 3d tetris in the start to let the bricks fall down as far as possible. To speed this up, bricks are dropped in
order of original height, and the highest point for any XY coordinate is stored as a sort 'ground zero' and updated
after every dropped brick.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Point3D:
    x: int
    y: int
    z: int

    def __add__(self, other: Point3D) -> Point3D:
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)


class Brick:
    """A simple coordinate holder for a brick, as a [X,Y,Z] position plus a [dX,dY,dZ] extent."""

    def __init__(self, xyz1: Point3D, xyz2: Point3D) -> None:
        self.pos: Point3D = Point3D(
            min(xyz1.x, xyz2.x), min(xyz1.y, xyz2.y), min(xyz1.z, xyz2.z)
        )
        self.dpos: Point3D = Point3D(
            abs(xyz1.x - xyz2.x), abs(xyz1.y - xyz2.y), abs(xyz1.z - xyz2.z)
        )


class GroundZero:
    """Class used to create a 3d grid of the highest Z position for each XY tile along with the brick
    that added that tile."""

    def __init__(self, x_size: int, y_size: int) -> None:
        self.__grid: list[list[tuple[int, Brick | None]]] = [
            [(0, None) for _ in range(y_size)] for _ in range(x_size)
        ]

    def drop_newbrick(self, brick: Brick) -> set[Brick]:
        """Finds the lowest available Z-coordinate for the brick, updates the grid with the brick, and returns
        the set of bricks it comes to rest on."""
        new_z = 0
        supporters: set[Brick] = set()
        nextpos = brick.pos + brick.dpos
        for x in range(brick.pos.x, nextpos.x + 1):
            for y in range(brick.pos.y, nextpos.y + 1):
                top, supporter = self.__grid[x][y]
                if top + 1 >= new_z:
                    if top + 1 > new_z:
                        supporters.clear()
                        new_z = top + 1
                    if supporter is not None:
                        supporters.add(supporter)
        for x in range(brick.pos.x, nextpos.x + 1):
            for y in range(brick.pos.y, nextpos.y + 1):
                self.__grid[x][y] = (new_z + brick.dpos.z, brick)
        return supporters


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__moving_bricks: list[Brick] = []
        self.__resting_bricks: dict[
            Brick, tuple[set[Brick], list[Brick]]
        ] = {}  # {brick: (down-bricks, up-bricks)}
        for line in rawstr.splitlines():
            left, right = line.split("~")
            x1, y1, z1 = [int(nbr) for nbr in left.split(",")]
            x2, y2, z2 = [int(nbr) for nbr in right.split(",")]
            self.__moving_bricks.append(Brick(Point3D(x1, y1, z1), Point3D(x2, y2, z2)))

    def get_p1(self) -> int:
        """Drops the bricks to rest state and returns the number of bricks that can safely be removed from the resting
        grid without causing any other brick to fall."""
        x_max = 0
        y_max = 0
        for brick in self.__moving_bricks:
            x_max = max(x_max, brick.pos.x + brick.dpos.x + 1)
            y_max = max(y_max, brick.pos.y + brick.dpos.y + 1)
        groundzero = GroundZero(x_max, y_max)
        # Drop the bricks in order of increasing original height
        self.__moving_bricks.sort(key=lambda br: br.pos.z)
        while self.__moving_bricks:
            nextbrick: Brick = self.__moving_bricks.pop(0)
            downbricks = groundzero.drop_newbrick(nextbrick)
            self.__resting_bricks[nextbrick] = (downbricks, [])
            for downbrick in downbricks:
                self.__resting_bricks[downbrick][1].append(nextbrick)
        # A brick can be removed if every brick it upholds is held up by something else as well
        result = 0
        for upbricks in self.__resting_bricks.values():
            if all(len(self.__resting_bricks[up][0]) > 1 for up in upbricks[1]):
                result += 1
        return result

    def get_p2(self) -> int:
        """Solves the second part of calculating the total sum number of bricks that would disintegrate as chain
        reaction when disintegrating each individual brick. Assumes that get_p1 has been run first."""
        result = 0
        for brick, (_, upbricks) in self.__resting_bricks.items():
            queue: list[Brick] = list(upbricks)
            disintegrated = {brick}
            while queue:
                poof = queue.pop(0)
                if all(
                    down in disintegrated for down in self.__resting_bricks[poof][0]
                ):
                    disintegrated.add(poof)
                    queue.extend(
                        up for up in self.__resting_bricks[poof][1] if up not in queue
                    )
            result += len(disintegrated) - 1
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1 = p.get_p1()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
