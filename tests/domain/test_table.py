import pytest

from toy_robot.domain.exception import InvalidPositionError
from toy_robot.domain.position import Position, Facing
from toy_robot.domain.robot import Robot
from toy_robot.domain.table import Table


@pytest.fixture(scope="module", autouse=True)
def table() -> Table:
    return Table(5, 5)


@pytest.mark.parametrize("x, y, want", [
    [0, 0, True],
    [4, 0, True],
    [0, 4, True],
    [2, 2, True],
    [-1, 0, False],
    [0, -1, False],
    [0, 5, False],
    [5, 0, False],
])
def test_is_valid_position__returns_expected_result(x, y, want, table):
    position = Position(x, y, ...)

    got = table.is_valid_position(position)

    assert got == want


def test_place__sets_the_correct_position_for_the_robot(table):
    robot = Robot()
    x, y, facing = 2, 3, Facing.EAST

    table.place(robot, x, y, facing)

    assert robot.position.x == x
    assert robot.position.y == y
    assert robot.position.facing == facing


def test_place__raises_exception_when_position_is_invalid(table):
    robot = Robot()
    x, y, facing = -1, 3, Facing.SOUTH

    with pytest.raises(InvalidPositionError):
        table.place(robot, x, y, facing)
