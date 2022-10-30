"""Problem Set 2, Problem 5."""

import random
import unittest

from ProblemSet2 import RandomWalkRobot, RectangularRoom
from ProblemSet2.lib import Position


# pylint: disable=C0103
class TestProblem5(unittest.TestCase):
    """Test class for Problem 5."""

    def setUp(self):
        """Set up TestProblem5."""
        self.arg1 = 5
        self.arg2 = 8
        self.arg3 = 1.0
        self.test_object = RandomWalkRobot(RectangularRoom(self.arg1, self.arg2), self.arg3)

    def test_get_robot_position(self):
        """Verifies Problem 5."""
        result = self.test_object.get_robot_position()
        x = result.get_x()
        y = result.get_y()

        self.assertEqual(x <= self.arg1, True)
        self.assertEqual(y <= self.arg2, True)

    def test_get_robot_direction(self):
        """Verifies Problem 5."""
        result = self.test_object.get_robot_direction()
        self.assertEqual(result, 0)

    def test_set_robot_position(self):
        """Verifies Problem 5."""
        for _ in range(5):
            x = random.randint(0, self.arg1 * 100) / 100
            y = random.randint(0, self.arg2 * 100) / 100
            pos = Position(x, y)
            self.test_object.set_robot_position(pos)
            self.assertEqual(self.test_object.get_robot_position(), pos)

    def test_set_robot_direction(self):
        """Verifies Problem 5."""
        for _ in range(10):
            direction = random.randint(0, 360)
            self.test_object.set_robot_direction(direction)
            self.assertEqual(self.test_object.get_robot_direction(), direction)

    def test_update_position_and_clean(self):
        """Verifies Problem 5."""
        arg1 = random.randint(5, 100)
        arg2 = random.randint(5, 100)
        arg3 = random.randint(1, 100) / 100
        test_object = RandomWalkRobot(RectangularRoom(arg1, arg2), arg3)

        for _ in range(30):
            test_object.update_position_and_clean()

        self.assertEqual(test_object.room.get_num_cleaned_tiles() > 1, True)
