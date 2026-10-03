"""
2022 day 22 - Monkey Map

The map is a cube net drawn flat, so first split it into its six square faces and work out, for every face edge,
which face and orientation you arrive at when stepping off it. Part 1 uses the flat wrap-around: keep travelling in
the same direction and wrap over the row or column, taking the first face found that way. Part 2 folds the net into a
cube: walk the flat face grid outwards from each face and connect it to the closest face in that direction, allowing
two faces to connect only once, and carrying the entry direction along so a walk can be rotated into the neighbour's
frame. With those relations in place the instructions are followed tile by tile, consulting the face relation
whenever a step would leave the current face.
"""

from dataclasses import dataclass
from typing import Final

_FaceId = tuple[int, int]
# (neighbouring face, direction to keep after the crossing)
_Neighbor = tuple[_FaceId, _FaceId]
_SearchState = tuple[_FaceId, _FaceId, _FaceId, _FaceId, set[_FaceId]]


@dataclass(frozen=True)
class Left:
    pass


@dataclass(frozen=True)
class Right:
    pass


@dataclass(frozen=True)
class Forward:
    nbr_tiles: int


Move = Left | Right | Forward


class Face:
    def __init__(
        self, rawgrid: list[str], startrow: int, endrow: int, startcol: int, endcol: int
    ) -> None:
        self.gridlines: list[str] = [
            "".join(rawgrid[row][col] for col in range(startcol, endcol))
            for row in range(startrow, endrow)
        ]
        # Flat mapping according to Part 1
        self.neighbors: dict[_FaceId, _Neighbor] = {}
        # Cube mapping according to Part 2
        self.cube_neighbors: dict[_FaceId, _Neighbor] = {}

    def add_neighbor(
        self,
        neighbor: _FaceId,
        src_direction: _FaceId,
        dest_direction: _FaceId,
        iscube: bool,
    ) -> None:
        target = self.cube_neighbors if iscube else self.neighbors
        target[src_direction] = (neighbor, dest_direction)


def parse_moves(s: str) -> list[Move]:
    """Splits a move string such as "10R5L" into alternating forward and turn moves,
    turning each distance-prefixed turn into a forward move followed by the turn."""
    result: list[Move] = []
    number: list[str] = []
    for char in s:
        if char in "RL":
            if number:
                result.append(Forward(int("".join(number))))
                number = []
            result.append(Left() if char == "L" else Right())
        else:
            number.append(char)
    if number:
        result.append(Forward(int("".join(number))))
    return result


class InputData:
    DIRECTIONS: Final = ((-1, 0), (0, 1), (1, 0), (0, -1))
    FACING: Final = {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}

    def __init__(self, s: str) -> None:
        grid, path = s.split("\n\n")
        self.__moves = parse_moves(path)
        self.__startface: _FaceId = (-1, -1)
        self.__startpos: _FaceId = (-1, -1)
        self.__direction: _FaceId = (0, 1)
        lines = grid.splitlines()
        rows = len(lines)
        cols = max(len(line) for line in lines)
        # A cube net always spans a 3x4 or 4x3 block of square faces, so the longer side has four faces.
        face_rows, face_cols = (4, 3) if rows > cols else (3, 4)
        self.__face_len = rows // face_rows
        self.__faces: dict[_FaceId, Face] = {}
        startfound = False
        for f_row in range(face_rows):
            for f_col in range(face_cols):
                r = f_row * self.__face_len
                c = f_col * self.__face_len
                if c < len(lines[r]) and lines[r][c] != " ":
                    self.__faces[(f_row, f_col)] = Face(
                        lines, r, r + self.__face_len, c, c + self.__face_len
                    )
                    if not startfound:
                        # The start tile is the first non-wall tile on the top row of the first face found.
                        self.__startface = (f_row, f_col)
                        for i, tile in enumerate(
                            self.__faces[(f_row, f_col)].gridlines[0]
                        ):
                            if tile != "#":
                                self.__startpos = (0, i)
                                startfound = True
                                break
        # Find neighbors
        # Part 1 - when reaching an edge (no neighbor face), jump to the other side and keep going in the same direction
        for face_id in self.__faces:
            row, col = face_id
            for dr, dc in self.DIRECTIONS:
                # Wrap around the face grid
                for step in range(1, max(face_rows, face_cols) + 1):
                    r = (row + dr * step) % face_rows
                    c = (col + dc * step) % face_cols
                    if (r, c) in self.__faces:
                        self.__faces[face_id].add_neighbor(
                            (r, c), (dr, dc), (dr, dc), False
                        )
                        break
        # Part 2 - BFS to find the connecting sides and relative rotations
        queue: list[_SearchState] = []
        for node in self.__faces:
            for d in self.DIRECTIONS:
                queue.append((node, d, (node[0] + d[0], node[1] + d[1]), d, {node}))
        while queue:
            originnode, outdir, currentnode, currentdir, seen = queue.pop(0)
            origin = self.__faces[originnode]
            if outdir in origin.cube_neighbors:
                # Skip if we have already found a neighbor here
                continue
            if currentnode in self.__faces:
                backdir = (-currentdir[0], -currentdir[1])
                if (
                    currentnode != originnode
                    and backdir not in self.__faces[currentnode].cube_neighbors
                    and all(
                        nbr != currentnode for nbr, _ in origin.cube_neighbors.values()
                    )
                ):
                    origin.add_neighbor(currentnode, outdir, currentdir, True)
                    self.__faces[currentnode].add_neighbor(
                        originnode, backdir, (-outdir[0], -outdir[1]), True
                    )
            else:
                seen.add(currentnode)
                for newdir in self.DIRECTIONS:
                    newnode = currentnode[0] + newdir[0], currentnode[1] + newdir[1]
                    if (
                        -1 <= newnode[0] <= face_rows
                        and -1 <= newnode[1] <= face_cols
                        and newnode not in seen
                    ):
                        queue.append((originnode, outdir, newnode, newdir, seen))

    def get_password(self, iscube: bool = False) -> int:
        direction = self.__direction
        face = self.__startface
        row, col = self.__startpos
        for move in self.__moves:
            match move:
                case Forward(value):
                    for _ in range(value):
                        newrow = row + direction[0]
                        newcol = col + direction[1]
                        if (
                            0 <= newrow < self.__face_len
                            and 0 <= newcol < self.__face_len
                        ):
                            if self.__faces[face].gridlines[newrow][newcol] == "#":
                                break
                            row = newrow
                            col = newcol
                        else:  # Move to neighbor face and rotate direction if needed
                            newface, newdir = (
                                self.__faces[face].cube_neighbors[direction]
                                if iscube
                                else self.__faces[face].neighbors[direction]
                            )
                            # Flip the coordinate to the other side
                            newrow %= self.__face_len
                            newcol %= self.__face_len
                            rotation = direction
                            while rotation != newdir:
                                # Rotate clock-wise until our direction is correct
                                rotation = self.DIRECTIONS[
                                    (self.DIRECTIONS.index(rotation) + 1)
                                    % len(self.DIRECTIONS)
                                ]
                                tmp = newrow
                                newrow = newcol
                                newcol = self.__face_len - 1 - tmp
                            if self.__faces[newface].gridlines[newrow][newcol] == "#":
                                # No need to keep the loop going if we bump into a wall
                                break
                            row = newrow
                            col = newcol
                            direction = newdir
                            face = newface
                case Left():
                    direction = self.DIRECTIONS[
                        (self.DIRECTIONS.index(direction) - 1) % len(self.DIRECTIONS)
                    ]
                case Right():
                    direction = self.DIRECTIONS[
                        (self.DIRECTIONS.index(direction) + 1) % len(self.DIRECTIONS)
                    ]
        # Convert to global coordinates for the final calculation
        row += face[0] * self.__face_len
        col += face[1] * self.__face_len
        return (1000 * (row + 1)) + (4 * (col + 1)) + self.FACING[direction]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_password())
    if part in (None, 2):
        p2 = str(p.get_password(True))

    return p1, p2
