# Problem 1
#
# Write a function that meets the specification below:
# def solveit(test):
#     """ test, a function that takes an int parameter and returns a Boolean
#         Assumes there exists an int, x, such that test(x) is True
#         Returns an int, x, with the smallest absolute value such that test(x) is True 
#         In case of ties, return any one of them. 
#     """
#     # IMPLEMENT THIS FUNCTION
#
# #### This test case prints 49 ####
# def f1(x):
#     return (x+15)**0.5 + x**0.5 == 15

# #### This test case prints 0 ####
# def f2(x):
#     return x == 0

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True
        In case of ties, return any one of them.
    """
    for i in range(1000):
        if test(i):
            return i
        elif test(-i):
            return -i