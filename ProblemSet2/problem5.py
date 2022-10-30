"""Problem Set 2, Problem 5: RandomWalkRobot Class.

iRobot is testing out a new robot design. The proposed new robots differ in that they change direction randomly after
every time step, rather than just when they run into walls. You have been asked to design a simulation to determine
what effect, if any, this change has on room cleaning times.

Write a new class RandomWalkRobot that inherits from Robot (like StandardRobot) but implements the new movement
strategy. RandomWalkRobot should have the same interface as StandardRobot.

Test out your new class. Perform a single trial with the StandardRobot implementation and watch the visualization to
make sure it is doing the right thing. Once you are satisfied, you can call runSimulation again, passing
RandomWalkRobot instead of StandardRobot.
"""

import math
import random

from ProblemSet2 import Robot
from ProblemSet2.lib import Position


# pylint: disable=I1101
class RandomWalkRobot(Robot):
    """RandomWalkRobot Class.

    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """

    def update_position_and_clean(self):
        """Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.direction = random.randint(0, 360)
        self.position = self.position.get_new_position(self.direction, self.speed)

        while not self.room.is_position_in_room(self.position):
            self.position = self.position.get_new_position(self._direction_to_centre(), self.speed)

        self.room.clean_tile_at_position(self.position)

    def _direction_to_centre(self):
        """Get direction to the centre of the room.

        Args:
            pos (Position): a Position object
            room (): a Room object

        Returns:
            int: angle to the centre
        """
        centre = Position(math.sqrt(self.room.get_num_tiles()) / 2, math.sqrt(self.room.get_num_tiles()) / 2)
        delta_x = centre.get_x() - self.position.get_x()
        delta_y = centre.get_y() - self.position.get_y()
        try:
            alpha = math.tanh(abs(delta_x / delta_y)) * (180 / math.pi)

        except ZeroDivisionError:
            alpha = 90

        if delta_x and delta_y <= 0:
            return alpha + 180

        if delta_x <= 0 < delta_y:
            return alpha + 270

        if delta_x and delta_y > 0:
            return alpha

        if delta_y <= 0 < delta_x:
            return alpha + 90

        return None
