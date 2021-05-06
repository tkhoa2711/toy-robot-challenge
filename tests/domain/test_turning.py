from toy_robot.domain.position import Direction, Position
from toy_robot.domain.robot import Robot

# NOTE: The actual logic of how turning works are tested as part of
# `test_position.py`. These tests only verify when turning the robot maintains
# its location i.e. (x, y) coordinates.


def test_turn_left__only_changes_facing_direction():
    robot = Robot()
    robot.position = Position(3, 2, Direction.SOUTH)

    robot.turn_left()

    assert robot.position == Position(3, 2, Direction.EAST)


def test_turn_right__only_changes_facing_direction():
    robot = Robot()
    robot.position = Position(3, 2, Direction.SOUTH)

    robot.turn_right()

    assert robot.position == Position(3, 2, Direction.WEST)
