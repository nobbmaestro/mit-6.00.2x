# Final Exam, Problem 2

Consider the following code:

```python
import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals
```

For each of the following questions, select the best answer from the set of choices.

---

## Problem 2-1

The values in tVals are most closely:

1. Uniformly distributed
2. Distributed with a Gaussian distribution
3. Exponentially distributed

### Answer

> Alternative 2

---

## Problem 2-2

The values in xVals are most closely:

1. Uniformly distributed
2. Distributed with a Gaussian distribution
3. Exponentially distributed

### Answer

> Alternative 1

For each of the following expressions using the code above, match the following calls to pylab.plot with one of the graphs shown below.

You can click on the following images to view a larger size.

---

## Problem 2-3

pylab.plot(xVals, zVals)

### Answer

> Graph 5

---

## Problem 2-4

pylab.plot(xVals, yVals)

### Answer

> Graph 4

---

## Problem 2-5

pylab.plot(xVals, sorted(yVals))

### Answer

> Graph 3

---

## Problem 2-6

pylab.plot(sorted(xVals), yVals)

### Answer

> Graph 2

---

## Problem 2-7

pylab.plot(sorted(xVals), sorted(yVals))

### Answer

> Graph 1
