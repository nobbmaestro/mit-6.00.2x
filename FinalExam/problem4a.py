"""Final Exam, Problem 4-1.

You are given the following function and class and function specifications for the two coding problems on this page
(also available in this file, die.py):

Write a function called makeHistogram(values, num_bins, x_label, y_label, title=None), with the following specification:

def makeHistogram(values, num_bins, x_label, y_label, title=None):
    '''
      - values, a list of numbers
      - num_bins, a positive int
      - x_label, y_label, title, are strings
      - Produces a histogram of values with num_bins bins and the indicated labels
        for the x and y axes
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    '''
Paste your entire function (including the definition) in the box.

Restrictions:
  - Do not paste import pylab in the box.
  - You should only be using the pylab.hist, pylab.title, pylab.x_label, pylab.y_label, pylab.show functions from the
    pylab module.
  - Do not leave any debugging print statements when you paste your code in the box.
"""

import pylab


def make_histogram(values, num_bins, x_label, y_label, title=None):
    """Make a histogram.

    - Produces a histogram of values with num_bins bins and the indicated labels for the x and y axis

    - If title is provided by caller, puts that title on the figure and otherwise does not title the figure

    Args:
        values (list): a sequence of numbers
        num_bins (int): a positive int
        x_label (str): x-axis label
        y_label (str): y-axis label
        title (str): title of the histogram
    """
    pylab.hist(values, num_bins)
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    if title:
        pylab.title(title)
    pylab.show()


def main():
    """Run Problem4a."""
    make_histogram([], 1, "A", "B", "C")
    make_histogram([1], 4, "Aa", "Bb", "Cc")
    make_histogram([1, 2], 4, "Aaa", "Bbb")
    make_histogram([1, 2, 5, 6, 9, 10], 4, "Aaaa", "Bbbb", "Cccc")
    make_histogram([21, 20, 19, 1, 2, 2, 2, 5, 6, 6, 9, 10], 5, "Aaaaa", "Bbbbb", "Ccccc")


if __name__ == '__main__':
    main()
