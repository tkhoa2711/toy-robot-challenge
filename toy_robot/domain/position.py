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
class Facing(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()

    def get_left(self) -> Facing:
        return FACINGS[(FACINGS.index(self) + 1) % 4]

    def get_right(self) -> Facing:
        return FACINGS[FACINGS.index(self) - 1]


FACINGS = (Facing.EAST, Facing.NORTH, Facing.WEST, Facing.SOUTH)

@dataclass
class Position:
    # `x` and `y` represent the coordinates of the position on a table.
    # See `Table` class for more details.
    x: int
    y: int
    facing: Facing
