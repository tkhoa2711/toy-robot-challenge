from dataclasses import dataclass

from toy_robot.domain.exception import InvalidPositionError
from toy_robot.domain.position import Position, Facing
from toy_robot.domain.robot import Robot


@dataclass
class Table:
    # `x` and `y` represent the size of a table, similar to X and Y axes.
    #
    # Y
    # ^
    # |
    # |
    # + -- --> X
    x: int
    y: int

    def is_valid_position(self, position: Position) -> bool:
        return 0 <= position.x < self.x and 0 <= position.y < self.y

    def place(self, robot: Robot, x: int, y: int, facing: Facing) -> None:
        position = Position(x, y, facing)
        if not self.is_valid_position(position):
            raise InvalidPositionError

        robot.position = position

    def move_forward(self, robot: Robot) -> None:
        pass

    def turn_left(self, robot: Robot) -> None:
        pass

    def turn_right(self, robot: Robot) -> None:
        pass
