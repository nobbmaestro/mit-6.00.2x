"""Get Mean and Standard deviation."""


# pylint: disable=C0103
def get_mean_and_std(X):
    """Return mean and standard deviation."""
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot / len(X))**0.5
    return mean, std
