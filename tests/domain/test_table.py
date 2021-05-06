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


@pytest.mark.parametrize("current_position, new_position", [
    [Position(0, 0, Facing.EAST), Position(1, 0, Facing.EAST)],
    [Position(0, 0, Facing.NORTH), Position(0, 1, Facing.NORTH)],
    [Position(4, 0, Facing.WEST), Position(3, 0, Facing.WEST)],
    [Position(4, 0, Facing.NORTH), Position(4, 1, Facing.NORTH)],
    [Position(0, 4, Facing.EAST), Position(1, 4, Facing.EAST)],
    [Position(0, 4, Facing.SOUTH), Position(0, 3, Facing.SOUTH)],
    [Position(4, 4, Facing.WEST), Position(3, 4, Facing.WEST)],
    [Position(4, 4, Facing.SOUTH), Position(4, 3, Facing.SOUTH)],
])
def test_move_forward__moves_the_robot_in_its_facing_direction(current_position, new_position, table):
    robot = Robot()
    robot.position = current_position

    table.move_forward(robot)

    assert robot.position == new_position


@pytest.mark.parametrize("current_position", [
    Position(0, 0, Facing.WEST),
    Position(0, 0, Facing.SOUTH),
    Position(4, 0, Facing.EAST),
    Position(4, 0, Facing.SOUTH),
    Position(0, 4, Facing.WEST),
    Position(0, 4, Facing.NORTH),
    Position(4, 4, Facing.EAST),
    Position(4, 4, Facing.NORTH),
])
def test_move_forward__raises_exception_when_the_next_position_is_off_the_table(current_position, table):
    robot = Robot()
    robot.position = current_position

    with pytest.raises(InvalidPositionError):
        table.move_forward(robot)


def test_turn_left__only_changes_facing_direction(table):
    robot = Robot()
    robot.position = Position(3, 2, Facing.SOUTH)

    table.turn_left(robot)

    assert robot.position == Position(3, 2, Facing.EAST)


def test_turn_right__only_changes_facing_direction(table):
    robot = Robot()
    robot.position = Position(3, 2, Facing.SOUTH)

    table.turn_right(robot)

    assert robot.position == Position(3, 2, Facing.WEST)
