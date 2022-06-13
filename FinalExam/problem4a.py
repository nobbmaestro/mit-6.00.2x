# Final Exam, Problem 4-1
#
# You are given the following function and class and function specifications for the two coding problems on this page (also available in this file, die.py):
#
# Write a function called makeHistogram(values, numBins, xLabel, yLabel, title=None), with the following specification:
#
# def makeHistogram(values, numBins, xLabel, yLabel, title=None):
#     """
#       - values, a list of numbers
#       - numBins, a positive int
#       - xLabel, yLabel, title, are strings
#       - Produces a histogram of values with numBins bins and the indicated labels
#         for the x and y axes
#       - If title is provided by caller, puts that title on the figure and otherwise
#         does not title the figure
#     """
# Paste your entire function (including the definition) in the box.
#
# Restrictions:
#   - Do not paste import pylab in the box.
#   - You should only be using the pylab.hist, pylab.title, pylab.xlabel, pylab.ylabel, pylab.show functions from the pylab module.
#   - Do not leave any debugging print statements when you paste your code in the box.

import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    std = (tot / len(X)) ** 0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]

    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title:
        pylab.title(title)
    pylab.show()

def main():
    makeHistogram([], 1, "A", "B", "C")
    makeHistogram([1], 4, "Aa", "Bb", "Cc")
    makeHistogram([1,2], 4, "Aaa", "Bbb")
    makeHistogram([1,2,5,6,9,10], 4,"Aaaa", "Bbbb", "Cccc")
    makeHistogram([21,20,19,1,2,2,2,5,6,6,9,10], 5, "Aaaaa", "Bbbbb", "Ccccc")

if __name__ == '__main__':
    main()