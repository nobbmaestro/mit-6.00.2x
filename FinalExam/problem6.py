# Final Exam, Problem 6
#
# Write a function that meets the specifications below. You do not have to use dynamic programming.
#
# Hint: You might want to use bin() on an int to get a string, get rid of the first two characters, add leading 0's as needed, and then convert it to a numpy array of ints. Type help(bin) in the console.
#
# For example,
#   - If choices = [1,2,2,3] and total = 4 you should return either [0 1 1 0] or [1 0 0 1]
#   - If choices = [1,1,3,5,3] and total = 5 you should return [0 0 0 1 0]
#   - If choices = [1,1,1,9] and total = 4 you should return [1 1 1 0]
#
# More specifically, write a function that meets the specifications below:
#
# def find_combination(choices, total):
#     """
#     choices: a non-empty list of ints
#     total: a positive int
#
#     Returns result, a numpy.array of length len(choices) 
#     such that
#         * each element of result is 0 or 1
#         * sum(result*choices) == total
#         * sum(result) is as small as possible
#     In case of ties, returns any result that works.
#     If there is no result that gives the exact total, 
#     pick the one that gives sum(result*choices) closest 
#     to total without going over.
#     """
# Paste your entire function (including the definition) in the box.
#
# Note: If you want to use numpy arrays, you should add the following 3 lines before your code:
#   >>> import os
#   >>> os.environ["OPENBLAS_NUM_THREADS"] = "1"
#   >>> import numpy as np
#
# And use np.METHOD_NAME in your code. Unfortunately, pylab does not work with the grader.

import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    dict_results = {}
    for i in range(2 ** len(choices)):
        binList = [int(x) for x in bin(i)[2:]]
        tmp = [0 for x in range(len(choices) - len(binList))]
        combination = tmp + binList

        result = np.dot(choices, combination)
        if result == total:
            return np.array(combination)

        dict_results[result] = np.array(combination)

    for key in reversed(sorted(list(dict_results.keys()))):
        if key < total:
            return dict_results[key]