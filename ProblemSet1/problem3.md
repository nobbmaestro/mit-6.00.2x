# Problem Set 1, Problem 3: Comparing the Cow Transport Algorithms

POLL: ALGORITHM INTUITION
(ungraded) Before doing the task in this part, answer the following question to see your intuition for how the greedy and brute force algorithm run. In terms of time, which algorithm do you expect will run faster?

RESULTS

- Greedy Algorithm:         93%
- Brute Force Algorithm:    7%

## Problem 3: Compare the Algorithms

Implement compare_cow_transport_algorithms. Load the cow data in ps1_cow_data.txt, and then run your greedy and brute force cow transport algorithms on the data to find the minimum number of trips found by each algorithm and how long each method takes. Use the default weight limits of 10 for both algorithms. Make sure you’ve tested both your greedy and brute force algorithms before you implement this!

Hints:

- You can measure the time a block of code takes to execute using the time.time() function as follows. This prints the duration in seconds, as a float. For a very small fraction of a second, it will print 0.0.
start = time.time()

```python
start = time.time()
## code to be timed
end = time.time()
print(end - start)
```

- Using the given default weight limits of 10 and the given cow data, both algorithms should not take more than a few seconds to run.

### Problem 3-1

Now that you have run your benchmarks, which algorithm runs faster?

1. The Greedy Transport Algorithm
2. The Brute Froce Transport Algorithm
3. They take the same amount of time

#### Answer
>
> 1.

### Problem 3-2

Consider the properties of the GREEDY algorithm. Will it return the optimal solution?

1. Yes, all the time
2. No, never
3. It could, but it depends on the data, not always.

#### Answer
>
> 3.

### Problem 3-3

Consider the properties of the BRUTE FORCE algorithm. Will it return the optimal solution?

1. Yes, all the time
2. No, never
3. It could, but it depends on the data, not always.

#### Answer
>
> 1.
