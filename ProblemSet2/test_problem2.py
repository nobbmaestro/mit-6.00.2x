"""Problem Set 2, Problem 2."""

import random
import unittest

from ProblemSet2 import RectangularRoom, Robot
from ProblemSet2.lib import Position


# pylint: disable=C0103
class TestProblem2(unittest.TestCase):
    """Test class for Problem 2."""

    def setUp(self):
        """Set up TestProblem2."""
        self.arg1 = 5
        self.arg2 = 8
        self.arg3 = 1.0
        self.test_object = Robot(RectangularRoom(self.arg1, self.arg2), self.arg3)

    def test_get_robot_position(self):
        """Verifies Problem 2."""
        result = self.test_object.get_robot_position()
        x = result.get_x()
        y = result.get_y()

        self.assertEqual(x <= self.arg1, True)
        self.assertEqual(y <= self.arg2, True)

    def test_get_robot_direction(self):
        """Verifies Problem 2."""
        result = self.test_object.get_robot_direction()
        self.assertEqual(result, 0)

    def test_set_robot_position(self):
        """Verifies Problem 2."""
        for _ in range(5):
            x = random.randint(0, self.arg1 * 100) / 100
            y = random.randint(0, self.arg2 * 100) / 100
            pos = Position(x, y)
            self.test_object.set_robot_position(pos)
            self.assertEqual(self.test_object.get_robot_position(), pos)

    def test_set_robot_direction(self):
        """Verifies Problem 2."""
        for _ in range(10):
            direction = random.randint(0, 360)
            self.test_object.set_robot_direction(direction)
            self.assertEqual(self.test_object.get_robot_direction(), direction)

    def test_update_position_and_clent(self):
        """Verifies Problem 2."""
        self.assertRaises(NotImplementedError, self.test_object.update_position_and_clean)
