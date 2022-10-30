"""Problem Set 4, Problem 4.

READ problem4.md
"""

import numpy as np

from ProblemSet4 import evaluate_models_on_training, generate_models
from ProblemSet4.lib import FILE_PATH, INTERVAL_1, Climate


# pylint: disable=C0103
def main():
    """Run Problem4."""
    raw_data = Climate(FILE_PATH)

    x1 = INTERVAL_1
    y = []
    for year in INTERVAL_1:
        y.append(np.mean(raw_data.get_yearly_temp('BOSTON', year)))
    models = generate_models(x1, y, [1])

    evaluate_models_on_training(x1, y, models)


if __name__ == '__main__':
    main()
