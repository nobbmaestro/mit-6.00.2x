"""Midterm Exam, Problem 1.

Write a function that meets the specification below:
def solveit(test):
    ''' test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True
        In case of ties, return any one of them.
    '''
    # IMPLEMENT THIS FUNCTION

#### This test case prints 49 ####
def f1(x):
    return (x+15)**0.5 + x**0.5 == 15

#### This test case prints 0 ####
def f2(x):
    return x == 0
"""


# pylint: disable=C0103
def solve_it(test, x=0):
    """Get solution to the test func.

    Args:
        test (func): a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True

    Returns:
        int: x, with the smallest absolute value such that test(x) is True
        In case of ties, return any one of them.
    """
    if test(x):
        return x

    if test(-x):
        return -x

    return solve_it(test, x + 1)
