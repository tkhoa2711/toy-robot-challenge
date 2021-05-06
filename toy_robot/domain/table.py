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
        current_facing = robot.position.facing
        new_position = robot.position

        if current_facing == Facing.EAST:
            new_position.x += 1
        elif current_facing == Facing.WEST:
            new_position.x -= 1
        elif current_facing == Facing.NORTH:
            new_position.y += 1
        elif current_facing == Facing.SOUTH:
            new_position.y -= 1

        if not self.is_valid_position(new_position):
            raise InvalidPositionError

        robot.position = new_position

    @staticmethod
    def turn_left(robot: Robot) -> None:
        robot.position.facing = robot.position.facing.get_left()

    @staticmethod
    def turn_right(robot: Robot) -> None:
        robot.position.facing = robot.position.facing.get_right()
