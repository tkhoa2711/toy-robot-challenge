from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


#         N
#         |
#         |
# W -- -- + -- -- E
#         |
#         |
#         S
class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()

    def get_left(self) -> Direction:
        return DIRECTIONS[(DIRECTIONS.index(self) + 1) % 4]

    def get_right(self) -> Direction:
        return DIRECTIONS[DIRECTIONS.index(self) - 1]


DIRECTIONS = (Direction.EAST, Direction.NORTH, Direction.WEST, Direction.SOUTH)

@dataclass
class Position:
    # `x` and `y` represent the coordinates of the position on a table.
    # See `Table` class for more details.
    x: int
    y: int
    facing: Direction
