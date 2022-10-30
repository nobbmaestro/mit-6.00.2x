"""Final Exam, Problem 8, Part A.

For this problem you are going to simulate growth of fox and rabbit population in a forest!

The following facts are true about the fox and rabbit population:
  - The maximum population of rabbits is determined by the amount of vegetation in the forest, which is
    relatively stable. There are never fewer than 10 rabbits; the maximum population of rabbits is 1000.

  - For each rabbit during each time step, a new rabbit will be born with a probability of
    In other words, when the current population is near the maximum, the probability of giving birth is
    very low, and when the current population is small, the probability of giving birth is very high.

  - The population of foxes is constrained by number of rabbits.
    There are never fewer than 10 foxes.

  - At each time step, after the rabbits have finished reproducing, a fox will try to hunt a rabbit with
    success rate of p_{fox eats rabbit}

               p_{fox eats rabbits} = current_rabbit_population / max_rabbit_population

    In other words, the more rabbits, the more likely a fox will eat one.

  - If a fox succeeds in hunting, it will decrease the number of rabbits by 1 immediately. Remember that
    the population of rabbits is never lower than 10. Additionally, if a fox succeeds in hunting, then it
    has a 1/3 probability of giving birth in the current time-step. If a fox fails in hunting then it has
    a 10 percent chance of dying in the current time-step.

  - If the starting population is below 10 then you should do nothing. You should not increase the population
    nor set the population to 10.

Start with 500 rabbits and 30 foxes.

At the end of each time step, record the number of foxes and rabbits.

Run the simulation for 200 time steps, and then plot the population of rabbits and the population of foxes as
a function of time step. (You do not need to paste your code for plotting for Part A of this problem).

Use the following steps, and the template file rabbits.py (click to download .py file), as guides in your
implementation of this simulation.

Step 1: Write the procedure, rabbitGrowth, that updates the number of rabbits during the first part of a
time step

Step 2: Write the procedure, foxGrowth, that updates the number of rabbits and foxes during the second part
of a time step

Step 3: Write the master procedure, runSimulation, that loops for some amount of time steps, doing the first
part and then the second part of the simulation. Record the two populations in two different lists, and return
those lists.

Paste your code for the three functions rabbitGrowth, foxGrowth, and runSimulation in the following box.

WARNING
DO NOT define the global variables MAXRABBITPOP, CURRENTRABBITPOP, or CURRENTFOXPOP in this box. We alter the
values of these variables to test your code. If you define the variables in this box, you may overwrite our
values, causing your code to be marked incorrect.

CLARIFICATIONS / HINTS
  - "See Full Output": If you are getting the line "0 10" in your output for "Test 4 foxGrowth" then for this
     particular test, your code changes the CURRENTFOXPOP (increases it if the fox population has gone below
     the minimum fox population), which is not the right behavior -- the code should not reset CURRENTFOXPOP.

  - It is not correct to assume that there is a 1/3 chance that the population increases in "Test 3 foxGrowth".
    Pay special attention to the following statement in the docstring of foxGrowth(): "Each fox, based on the
    probabilities in the problem statement, may eat one rabbit (but only if there are more than 10 rabbits)."
"""

import random

import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300


def rabbit_growth():
    """Rabbit growth function is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, a new rabbit may be born.

    Nothing is returned.
    """
    # you need this line for modifying global variables
    # pylint: disable=W0603
    global CURRENTRABBITPOP

    # TO DO
    pop = CURRENTRABBITPOP
    for _ in range(pop):
        prob = 1.0 - (CURRENTRABBITPOP/MAXRABBITPOP)
        if prob * 100 > random.randint(0, 100):
            CURRENTRABBITPOP += 1


def fox_growth():
    """Fox growth function is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP, and both may be modified by this
    procedure.

    Each fox, based on the probabilities in the problem statement, may eat one rabbit (but only if there are
    more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    # pylint: disable=W0603
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    pop = CURRENTFOXPOP
    for _ in range(pop):
        if CURRENTRABBITPOP > 10:
            prob = CURRENTRABBITPOP / MAXRABBITPOP
        else:
            prob = 0
        if prob * 100 > random.randint(0, 100) and random.randint(0, 100) < 30:
            CURRENTFOXPOP += 1
            CURRENTRABBITPOP -= 1

        elif CURRENTRABBITPOP > 10 and random.randint(0, 100) < 90:
            CURRENTFOXPOP -= 1


def run_simulation(num_steps):
    """Run the simulation for `num_steps` time steps.

    Return
        tuple: a tuple of two lists: (rabbit_populations, fox_populations)
        where rabbit_populations is a record of the rabbit population at the
        END of each time step, and fox_populations is a record of the fox population
        at the END of each time step. Both lists should be `num_steps` items long.
    """
    # TO DO
    rabbit_pop = []
    fox_pop = []
    for _ in range(num_steps):
        rabbit_growth()
        fox_growth()

        rabbit_pop.append(CURRENTRABBITPOP)
        fox_pop.append(CURRENTFOXPOP)

    return (rabbit_pop, fox_pop)


def main():
    """Run Problem8a."""
    num_steps = 200
    rabbit_pop, fox_pop = run_simulation(num_steps)

    coeff_rabbits = pylab.polyfit(range(len(rabbit_pop)), rabbit_pop, 2)
    coeff_foxes = pylab.polyfit(range(len(fox_pop)), fox_pop, 2)

    pylab.plot(range(num_steps), rabbit_pop)
    pylab.plot(range(num_steps), fox_pop)
    pylab.plot(pylab.polyval(coeff_rabbits, range(len(rabbit_pop))))
    pylab.plot(pylab.polyval(coeff_foxes, range(len(fox_pop))))
    pylab.legend(['Pop of rabbits', 'Pop of foxes', 'F: Rabbits', 'F: Foxes'])
    pylab.show()


if __name__ == '__main__':
    main()
