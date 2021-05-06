from toy_robot.domain.robot import Robot
from toy_robot.domain.table import Table


class State:
    def __init__(self):
        self.table = Table(5, 5)
        self.robot = Robot()
