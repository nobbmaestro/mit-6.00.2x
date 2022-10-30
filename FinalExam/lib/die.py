"""Die Class."""

import random


# pylint: disable=C0103
class Die:
    """Die Class."""

    def __init__(self, valList):
        """Val list is not empty."""
        self.possibleVals = valList[:]

    def roll(self):
        """Return the outcome of roll the dice."""
        return random.choice(self.possibleVals)
