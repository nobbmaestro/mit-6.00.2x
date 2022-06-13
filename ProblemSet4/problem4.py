# Problem Set 4, Problem 4
#
# READ problem4.md

import pylab, numpy as np

from ProblemSet4 import evaluate_models_on_training, Climate, generate_models, FILE_PATH, INTERVAL_1, INTERVAL_2

def main():
    raw_data = Climate(FILE_PATH)

    x1 = INTERVAL_1
    x2 = INTERVAL_2
    y = []
    for year in INTERVAL_1:
        y.append(np.mean(raw_data.get_yearly_temp('BOSTON', year)))
    models = generate_models(x1, y, [1])
    evaluate_models_on_training(x1, y, models)

if __name__ == '__main__':
    main()