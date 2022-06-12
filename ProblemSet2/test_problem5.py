# Problem Set 2, Problem 5

import unittest
import random

from ProblemSet2 import RandomWalkRobot, RectangularRoom, Position

class TestProblem5(unittest.TestCase):
    def setUp(self):
        self.arg1 = 5
        self.arg2 = 8
        self.arg3 = 1.0
        self.test_object = RandomWalkRobot(RectangularRoom(self.arg1, self.arg2), self.arg3)
    
    def test_getRobotPosition(self):
        result = self.test_object.getRobotPosition()
        x = result.getX()
        y = result.getY()

        self.assertEqual(x <= self.arg1, True)
        self.assertEqual(y <= self.arg2, True)

    def test_getRobotDirection(self):
        result = self.test_object.getRobotDirection()
        self.assertEqual(result, 0)

    def test_setRobotPosition(self):
        for i in range(5):
            x = random.randint(0, self.arg1*100)/100
            y = random.randint(0, self.arg2*100)/100
            pos = Position(x, y)
            self.test_object.setRobotPosition(pos)
            self.assertEqual(self.test_object.getRobotPosition(), pos)

    def test_setRobotDirection(self):
        for i in range(10):
            direction = random.randint(0, 360)
            self.test_object.setRobotDirection(direction)
            self.assertEqual(self.test_object.getRobotDirection(), direction)

    def test_updatePositionAndClean(self):
        arg1 = random.randint(5, 100)
        arg2 = random.randint(5, 100)
        arg3 = random.randint(1, 100)/100
        test_object = RandomWalkRobot(RectangularRoom(arg1, arg2), arg3)

        for i in range(30):
            test_object.updatePositionAndClean()
            
        self.assertEqual(test_object.room.getNumCleanedTiles() > 1, True)