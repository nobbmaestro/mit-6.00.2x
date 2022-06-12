# Problem Set 2, Problem 5: RandomWalkRobot Class
# 
# iRobot is testing out a new robot design. The proposed new robots differ in that they change direction randomly after 
# every time step, rather than just when they run into walls. You have been asked to design a simulation to determine what 
# effect, if any, this change has on room cleaning times.

# Write a new class RandomWalkRobot that inherits from Robot (like StandardRobot) but implements the new movement strategy. 
# RandomWalkRobot should have the same interface as StandardRobot.

# Test out your new class. Perform a single trial with the StandardRobot implementation and watch the visualization to make 
# sure it is doing the right thing. Once you are satisfied, you can call runSimulation again, passing RandomWalkRobot instead 
# of StandardRobot.

import random, math

from ProblemSet2 import Robot, Position
        
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.direction = random.randint(0, 360)
        self.position = self.position.getNewPosition(self.direction, self.speed)

        while not self.room.isPositionInRoom(self.position):
            self.position = self.position.getNewPosition(self.directionToCentre(self.position, self.room), self.speed)

        self.room.cleanTileAtPosition(self.position)

    def directionToCentre(self, pos, room):
        cen_pos = Position(math.sqrt(self.room.getNumTiles())/2, math.sqrt(self.room.getNumTiles())/2)
        a = cen_pos.getX() - self.position.getX()
        b = cen_pos.getY() - self.position.getY()
        try:
            alpha = math.tanh(abs(a / b)) * (180 / math.pi)
        except ZeroDivisionError:
            alpha = 90

        if a <= 0 and b <= 0:
            return  alpha + 180

        elif a <= 0 and b > 0:
            return alpha + 270

        elif a > 0 and b > 0:
            return alpha

        elif a > 0 and b <= 0:
            return alpha + 90