"""Problem Set 2, Problem 1: RectanggularRoom.

You will need to design two classes to keep track of which parts of the room have been cleaned as well as the position
and direction of each robot.

In ps2.py, we've provided skeletons for the following two classes, which you will fill in in Problem 1:
  - RectangularRoom: Represents the space to be cleaned and keeps track of which tiles have been cleaned.
  - Position: We've also provided a complete implementation of this class. It stores the x- and y-coordinates of a
    robot in a room.

Read ps2.py carefully before starting, so that you understand the provided code and its capabilities.

The problem:
  In this problem you will implement the RectangularRoom class. For this class, decide what fields you will use and
  decide how the following operations are to be performed:
      - Initializing the object
      - Marking an appropriate tile as cleaned when a robot moves to a given position (casting floats to ints - and/or
        the function math.floor - may be useful to you here)
      - Determining if a given tile has been cleaned
      - Determining how many tiles there are in the room
      - Determining how many cleaned tiles there are in the room
      - Getting a random position in the room
      - Determining if a given position is in the room

Complete the RectangularRoom class by implementing its methods in ps2.py.

Although this problem has many parts, it should not take long once you have chosen how you wish to represent your data.
For reasonable representations, a majority of the methods will require only a couple of lines of code.

Hint: During debugging, you might want to use random.seed(0) so that your results are reproducible.
"""

import random

from ProblemSet2.lib import Position


class RectangularRoom:
    """A RectangularRoom represents a rectangular region containing clean or dirty tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """

    def __init__(self, width, height):
        """Initialize a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        Args:
            width (int): an integer > 0
            height (int): an integer > 0
        """
        self.width = width
        self.heigth = height
        self.is_cleaned = [[False for w in range(self.width)] for h in range(self.heigth)]

    def clean_tile_at_position(self, pos):
        """Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        Args:
            pos (Position): a Position
        """
        try:
            self.is_cleaned[int(pos.get_y())][int(pos.get_x())] = True
        except IndexError:
            self.is_cleaned[int(pos.get_x())] = True

    # pylint: disable=C0103
    def is_tile_cleaned(self, m, n):
        """Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        Args:
            m (int): an integer
            n (int): an integer

        Returns:
            bool: True if (m, n) is cleaned, False otherwise
        """
        try:
            return self.is_cleaned[n][m]

        except IndexError:
            return self.is_cleaned[m]

    def get_num_tiles(self):
        """Return the total number of tiles in the room.

        Returns:
            int: an integer
        """
        return len(self.is_cleaned) * len(self.is_cleaned[0])

    def get_num_cleaned_tiles(self):
        """Return the total number of clean tiles in the room.

        Returns:
            int: an integer
        """
        clean_tiles = 0
        for h in range(self.heigth):
            for w in range(self.width):
                if self.is_cleaned[h][w]:
                    clean_tiles += 1

        return clean_tiles

    def get_random_position(self):
        """Return a random position inside the room.

        Returns
            Position: a Position object.
        """
        return Position(random.uniform(0, self.width), random.uniform(0, self.heigth))

    def is_position_in_room(self, pos):
        """Return True if pos is inside the room.

        Args:
            pos (Position): a Position object.

        Returns:
            bool: True if pos is in the room, False otherwise.
        """
        return pos.get_x() >= 0 and pos.get_x() < self.width and pos.get_y() >= 0 and pos.get_y() < self.heigth
