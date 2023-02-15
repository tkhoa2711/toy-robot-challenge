import hypothesis.strategies as st
import pytest
from hypothesis import given

from toy_robot.domain.position import DIRECTIONS, Direction, Position
from toy_robot.domain.robot import Robot


@pytest.mark.parametrize(
    "position, want",
    [
        [Position(1, 1, Direction.WEST), True],
        [None, False],
    ],
)
def test_robot_has_been_placed(position, want):
    robot = Robot()
    robot.position = position

    got = robot.has_been_placed()

    assert got == want


@given(st.integers(), st.integers(), st.sampled_from(DIRECTIONS))
def test_robot_has_been_placed__random_position(x: int, y: int, direction: Direction):
    robot = Robot()
    robot.position = Position(x, y, direction)

    assert robot.has_been_placed()
