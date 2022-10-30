"""Final Exam, Problem 3.

You have a set of unlabeled foods to eat and you attempt to identify what each item is. The probability of
guessing each food correctly is in the list probs. You make a guess for every food and you pay cost dollars
per guess. For each food you identify correctly, you receive get dollars. Write a Monte Carlo simulation that
runs num_trials number of trials of this guessing game.

More specifically, write a function according to the specifications below (you are also given a helper function):

  # helper function
  def get_mean_and_std(X):
      mean = sum(X)/float(len(X))
      tot = 0.0
      for x in X:
          tot += (x - mean)**2
      std = (tot/len(X))**0.5
      return mean, std

  def guessfood_sim(num_trials, probs, cost, get):
      '''
      num_trials: integer, number of trials to run
      probs: list of probabilities of guessing correctly for
              the ith food, in each trial
      cost: float, how much to pay for each food guess
      get: float, how much you get for a correct guess

      Runs a Monte Carlo simulation, 'num_trials' times. In each trial
      you guess what each food is, the ith food has 'prob[i]' probability
      to get it right. For every food you guess, you pay 'cost' dollars.
      If you guess correctly, you get 'get' dollars.

      Returns: a tuple of the mean and standard deviation over
      'num_trials' trials of the net money earned
      when making len(probs) guesses
      '''

You are not allowed to import anything besides random. If you use the helper function, paste that in the code
box as well. Do not leave any debugging print stataments. Click "See full output" to see the test cases passed/failed.
Paste only the guessfood_sim function and any helper functions you made for yourself (if any).
"""

import random

from FinalExam.lib import get_mean_and_std


def weighted_choice(prob):
    """Return weighted choice.

    Args:
        prob (float): probability, a float between 0-1

    Returns:
        bool: True if prob is 1, False if prob is 0, else random
    """
    if prob == 1:
        return True

    if prob == 0:
        return False

    return prob * 100 >= random.randint(0, 100)


def guess_food_sim(num_trials, probs, cost, get):
    """Run a Monte Carlo simulation, 'num_trials' times.

    In each trial
    you guess what each food is, the ith food has 'prob[i]' probability
    to get it right. For every food you guess, you pay 'cost' dollars.
    If you guess correctly, you get 'get' dollars.

    Args:
        num_trials (int): number of trials to run
        probs (list): list of probabilities of guessing correctly for the ith food, in each trial
        cost (float): how much to pay for each food guess
        get (float): how much you get for a correct guess

    Returns:
        tuple: a tuple of the mean and standard deviation over 'num_trials' trials of the net money earned
        when making len(probs) guesses
    """
    list_of_net_money_earned = []
    for _ in range(num_trials):
        net_money_earned = 0
        for __, value in enumerate(probs):
            net_money_earned -= cost
            guess = weighted_choice(value)
            if guess:
                net_money_earned += get
        list_of_net_money_earned.append(net_money_earned)

    return get_mean_and_std(list_of_net_money_earned)
