from dataclasses import dataclass
from typing import Optional

from toy_robot.domain.position import Position


@dataclass
class Robot:
    position: Optional[Position]

    def __init__(self):
        self.position = None

    def has_been_placed(self) -> bool:
        return self.position is None

    def turn_left(self) -> None:
        self.position.facing = self.position.facing.get_left()

    def turn_right(self) -> None:
        self.position.facing = self.position.facing.get_right()

    def report(self) -> str:
        return repr(self.position)
