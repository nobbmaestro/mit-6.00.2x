"""Position."""

import math


# pylint: disable=C0103, I1101
class Position:
    """A Position represents a location in a two-dimensional room."""

    def __init__(self, x, y):
        """Initialize a position with coordinates (x, y)."""
        self.x = x
        self.y = y

    def get_x(self):
        """Return X coordinate."""
        return self.x

    def get_y(self):
        """Return Y coordinate."""
        return self.y

    def get_new_position(self, angle, speed):
        """Return new position.

        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        Args:
            angle (int): number representing angle in degrees, 0 <= angle < 360
            speed (float): positive float representing speed

        Returns
            Position: a Position object representing the new position.
        """
        old_x, old_y = self.get_x(), self.get_y()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):
        """Representation."""
        return "(%0.2f, %0.2f)" % (self.x, self.y)
