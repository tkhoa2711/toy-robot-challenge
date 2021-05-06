import pytest

from toy_robot.domain.position import Direction, Position
from toy_robot.domain.robot import Robot


@pytest.mark.parametrize("position, want", [
    [Position(1, 1, Direction.WEST), True],
    [None, False],
])
def test_robot_has_been_placed(position, want):
    robot = Robot()
    robot.position = position

    got = robot.has_been_placed()

    assert got == want
