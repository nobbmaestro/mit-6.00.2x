"""Final Exam, Problem 4-2.

Write a function called get_average(die, num_rolls, num_trials), with the following specification:
  def get_average(die, num_rolls, num_trials):
        '''
          - die, a Die
          - num_rolls, num_trials, are positive ints
          - Calculates the expected mean value of the longest run of a number
            over num_trials runs of num_rolls rolls.
          - Calls make_histogram to produce a histogram of the longest runs for all
            the trials. There should be 10 bins in the histogram
          - Choose appropriate labels for the x and y axes.
          - Returns the mean calculated to 3 decimal places
      '''
A run of numbers counts the number of times the same dice value shows up in consecutive rolls. For example:
  - a dice roll of 1 4 3 has a longest run of 1
  - a dice roll of 1 3 3 2 has a longest run of 2
  - a dice roll of 5 4 4 4 5 5 2 5 has a longest run of 3

When this function is called with the test case given in the file, it will return 5.312. Your simulation
may give slightly different values.

Paste your entire function (including the definition) in the box.

Restrictions:
  - Do not import or use functions or methods from pylab, numpy, or matplotlib.
  - Do not leave any debugging print statements when you paste your code in the box.

If you do not see the return value being printed when testing your function, close the histogram window.
"""

from FinalExam import make_histogram
from FinalExam.lib import Die, get_mean_and_std


def get_average(die, num_rolls, num_trials):
    """Calculate the expected mean value of the longest run of a number over num_trials runs of num_rolls rolls.

    Args:
      die (Die): a Die object
      num_rolls (int): number of rolls per trial
      num_trials (int): number of trials

      Returns:
        int: the mean calculated
    """
    list_of_means = []
    for _ in range(num_trials):
        rolls_in_trial = []
        for __ in range(num_rolls):
            rolls_in_trial.append(die.roll())

        longest_run_mean = 0
        for value in rolls_in_trial:
            if value * rolls_in_trial.count(value) / num_rolls > longest_run_mean:
                longest_run_mean = value * rolls_in_trial.count(value) / num_rolls
        list_of_means.append(longest_run_mean)

    make_histogram(list_of_means, 10, x_label='Bins', y_label='Mean of Longest Rolls per Trial')
    return get_mean_and_std(list_of_means)[0]


def main():
    """Run Problem4b."""
    get_average(Die([1]), 10, 1000)
    get_average(Die([1, 1]), 10, 1000)
    get_average(Die([1, 2, 3, 4, 5, 6]), 50, 1000)
    get_average(Die([1, 2, 3, 4, 5, 6, 6, 6, 7]), 50, 1000)
    get_average(Die([1, 2, 3, 4, 5, 6, 6, 6, 7]), 1, 1000)


if __name__ == '__main__':
    main()
