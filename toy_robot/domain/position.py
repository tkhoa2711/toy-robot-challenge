from dataclasses import dataclass
from enum import Enum, auto


class Facing(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


@dataclass
class Position:
    x: int
    y: int
    facing: Facing
