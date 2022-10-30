"""Problem Set 2, Problem 2: Robot Class.

In ps2.py we provided you with the Robot class, which stores the position and direction of a robot. For this class,
decide what fields you will use and decide how the following operations are to be performed:
  - Initializing the object
  - Accessing the robot's position
  - Accessing the robot's direction
  - Setting the robot's position
  - Setting the robot's direction
  - Complete the Robot class by implementing its methods in ps2.py.

Note: When a Robot is initialized, it should clean the first tile it is initialized on. Generally the model these
Robots will follow is that after a robot lands on a given tile, we will mark the entire tile as clean. This might not
make sense if you're thinking about really large tiles, but as we make the size of the tiles smaller and smaller, this
does actually become a pretty good approximation.

Although this problem has many parts, it should not take long once you have chosen how you wish to represent your data.
For reasonable representations, a majority of the methods will require only a couple of lines of code.

Note: The Robot class is an abstract class, which means that we will never make an instance of it. Read up on the
Python docs on abstract classes at this link and if you want more examples on abstract classes, follow this link.

In the final implementation of Robot, not all methods will be implemented. Not to worry -- its subclass(es) will
implement the method updatePositionAndClean()

Enter your code for classes RectangularRoom (from the previous problem) and Robot below.
"""


class Robot:
    """Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """

    def __init__(self, room, speed):
        """Initialize a Robot with the given speed in the specified room.

        The robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        Args:
            room (RengularRoom): a RectangularRoom object.
            speed (float): a float (speed > 0)
        """
        self.room = room
        self.speed = speed

        self.position = room.get_random_position()
        self.direction = 0

    def get_robot_position(self):
        """Return the position of the robot.

        Returns:
            Position: a Position object giving the robot's position.
        """
        return self.position

    def get_robot_direction(self):
        """Return the direction of the robot.

        Returns:
            int: an integer d giving the direction of the robot as an angle in degrees, 0 <= d < 360.
        """
        return self.direction

    def set_robot_position(self, position):
        """Set the position of the robot to POSITION.

        Args:
            position (Position): a Position object.
        """
        self.position = position

    def set_robot_direction(self, direction):
        """Set the direction of the robot to DIRECTION.

        Args:
            direction (int): integer representing an angle in degrees
        """
        self.direction = direction

    def update_position_and_clean(self):
        """Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError  # don't change this!
