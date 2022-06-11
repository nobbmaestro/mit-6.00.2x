import unittest
import random

from ProblemSet2 import Robot, RectangularRoom, Position

class TestProblem2(unittest.TestCase):
    def setUp(self):
        self.arg1 = 5
        self.arg2 = 8
        self.arg3 = 1.0
        self.test_object = Robot(RectangularRoom(self.arg1, self.arg2), self.arg3)
    
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
        self.assertRaises(NotImplementedError, self.test_object.updatePositionAndClean)