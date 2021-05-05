from dataclasses import dataclass
from enum import Enum, auto


class Facing(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


@dataclass
class Position:
    # `x` and `y` represent the coordinates of the position on a table.
    # See `Table` class for more details.
    x: int
    y: int
    facing: Facing
