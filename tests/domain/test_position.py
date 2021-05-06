import pytest

from toy_robot.domain.position import Facing


@pytest.mark.parametrize("current_facing, want", [
    [Facing.EAST, Facing.NORTH],
    [Facing.NORTH, Facing.WEST],
    [Facing.WEST, Facing.SOUTH],
    [Facing.SOUTH, Facing.EAST],
])
def test_to_left(current_facing: Facing, want: Facing):
    got = current_facing.get_left()

    assert got == want


@pytest.mark.parametrize("current_facing, want", [
    [Facing.EAST, Facing.SOUTH],
    [Facing.SOUTH, Facing.WEST],
    [Facing.WEST, Facing.NORTH],
    [Facing.NORTH, Facing.EAST],
])
def test_to_left(current_facing: Facing, want: Facing):
    got = current_facing.get_right()

    assert got == want
