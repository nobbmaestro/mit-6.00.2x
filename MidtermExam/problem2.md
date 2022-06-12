# Problem 2

## Problem 2-1
Which of the following problems can be solved using dynamic programming? Check all that work.
1. Sum of elements - Given a list of integer elements, find the sum of all the elements.
2. Binary search - Given a list of elements, check if the element X is in the list.
3. Dice throws - Given n dice each with m faces, numbered from 1 to m, find the number of ways to get sum X. X is the summation of the values on each face when all the dice are thrown.

### Answer:
> 1, 2 and 3.

## Problem 2-2
What is the exact probability of rolling at least two 6's when rolling a die three times?
1. 1/12
2. 1/36
3. 2/27
4. 25/27
5. None of the above

### Answer:
> 3.

## Problem 2-3
A greedy optimization algorithm:
1. is typically efficient in time.
2. always finds an asnwer fasten than a brute force algorithm.
3. always returns the same answer as the brute force algorithm.
4. never returns the optimal solutions to the problem.

### Answer:
> 1.

## Problem 2-4:
Suppose you have a weighted directed graph and want to find a path between nodes A and B with the smallest total weight. Select the most accurate statement.
1. If some edges have negative weights, depth-first search finds a correct solution.
2. If all edges have weight 2, depth-first search guarantees that the first path found to be is the shortest path.
3. If some edges have negative weights, breadth-first search finds a correct solution.
4. If all edges have weight 2, breadth-first search guarantees that the first path found to be is the shortest path.

### Answer:
> 4.

## Problem 2-5:
Which of the following functions are deterministic?
```python
import random
        
def F():
    mylist = []
    r = 1

    if random.random() > 0.99:
        r = random.randint(1, 10)
    for i in range(r):
        random.seed(0)
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            if number not in mylist:
                mylist.append(number)
    print(mylist)

def G():  
    random.seed(0)
    mylist = []
    r = 1

    if random.random() > 0.99:
        r = random.randint(1, 10)
    for i in range(r):
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            mylist.append(number)
            print(mylist)
```

1. F
2. G
3. Both F and G
4. Neither F nor G

### Answer:
> 3.

## Problem 2-6
Consider a list of positive (there is at least one positive) and negative numbers. You are asked to find the maximum sum of a contiguous subsequence. For example,
- in the list [3, 4, -1, 5, -4], the maximum sum is 3+4-1+5 = 11
- in the list [3, 4, -8, 15, -1, 2], the maximum sum is 15-1+2 = 16
One algorithm goes through all possible subsequences and compares the sums of each contiguous subsequence with the largest sum it has seen. What is the time complexity of this algorithm in terms of the length of the list, N?

1. O(1)
2. O(log(n))
3. O(n)
4. O(n^2)
5. O(2^n)'
6. None of the above

### Answer:
> 4.