# Problem Set 3, Problem 4
## Problem 4-1
Let's try another way to get data points and see whether we can find some evidence for global warming. We surmise, due to global warming, the average temperature should increase over time. Thus, we are going to plot the results of a linear regression on the average annual temperature of Boston.

In a similar manner to Problem 3, fill in the missing piece to the following code. The code should generate your data samples. Each sample represents a year from 1961 to 2005 and the average annual temperature in Boston in that year (again, the provided helper class is helpful). Fit your data to a linear line with generate_models and plot the regression results with evaluate_models_on_training.

```python
# Problem 4: FILL IN MISSING CODE TO GENERATE y VALUES
x1 = INTERVAL_1
x2 = INTERVAL_2
y = []
# MISSING LINES
models = generate_models(x1, y, [1])    
evaluate_models_on_training(x1, y, models)
```
Which of the following is the correct missing code?

- Alternative 1
```python
for year in INTERVAL_1:
    y.append(numpy.mean(get_yearly_temp('BOSTON', year)))
```

- Alternative 2
```python
for year in INTERVAL_2:
    y.append(numpy.mean(get_yearly_temp('BOSTON', year)))
```

- Alternative 3
```python
for year in INTERVAL_1:
    y.append(numpy.mean(raw_data.get_yearly_temp('BOSTON', 1961, 2005)))
```

- Alternative 4
```python
for year in INTERVAL_1:
    y.append(numpy.mean(raw_data('BOSTON', year)))
```

- Alternative 5
```python
for year in INTERVAL_1:
    y.append(numpy.mean(raw_data.get_yearly_temp('BOSTON', year)))
```

- Alternative 6
```python
for year in INTERVAL_2:
    y.append(numpy.mean(raw_data.get_yearly_temp('BOSTON', year)))
```

### Answer:
> Alternative 5

## Problem 4-2
What is the R^2 value? (use 3 decimal places)

### Answer:
> 0.085

## [Source Code for the assigment](MIT-6.00.2x-Introduction-to-Computational-Thinking-and-Data-Science/ProblemSet3/problem4.py)