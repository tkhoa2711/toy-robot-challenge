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

    def report(self) -> None:
        pass
