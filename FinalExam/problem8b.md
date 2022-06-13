# Final Exam, Problem 8, Part B
Follow the next steps of the simulation to answer the remaining questions.

Step 4: Assume MAXRABBITPOP = 1000, CURRENTRABBITPOP = 500, CURRENTFOXPOP = 30, numSteps = 200. Plot two curves, one for the rabbit population and one for the fox population. You won't be submitting the plots. They are for your own understanding.

Step 5: Use polyfit to find the coefficients of a 2nd degree polynomial for the rabbit curve and the same for the fox curve. Then use polyval to evaluation the 2nd degree polynomial and plot it, e.g.
```python
coeff = polyfit(range(len(rabbitPopulationOverTime)), rabbitPopulationOverTime, 2)

plot(polyval(coeff, range(len(rabbitPopulationOverTime))))
```
Of course your variables and plotting commands may not look identical to the above code; the above code is shown just to give you an idea of what we mean.

Once you have finished Steps 4 and 5, continue on to answer the following questions.

# Problem 8-2
At some point in time, there are more foxes than rabbits.

True or False?

## Answer:
> True

# Problem 8-3
The polyfit curve for the rabbit population is:
1. A straight line
2. A concave up curve (looks like a U shape)
3. A concave down curve (looks like a ∩ shape)
4. An exponentially decreasing curve
5. An exponentially increasing curve
6. None of the above

## Answer:
> Alternative 2

# Problem 8-4
The polyfit curve for the fox population is:
1. A straight line
2. A concave up curve (looks like a U shape)
3. A concave down curve (looks like a ∩ shape)
4. An exponentially decreasing curve
5. An exponentially increasing curve
6. None of the above

## Answer:
> Alternative 3

# Problem 8-5
Changing the initial conditions from 500 rabbits and 30 foxes to 50 rabbits and 300 foxes changes the general shapes of both the polyfit curves for the rabbit population and fox population.

True or False?

## Answer:
> False

# Problem 8-6
Let's say we make a change in the original simulation. That is, we are going to change one detail in the original simulation, but everything else will remain the same as it was explained in Problem 8 - Part A.

Now, if a fox fails in hunting, it has a 90 percent chance of dying (instead of a 10 percent chance, as in the original simulation).

Changing the probability of an unsuccessful fox dying from 10% to 90% changes the general shapes of both the polyfit curves for the rabbit population and fox population.

True or False?
## Answer:
> True