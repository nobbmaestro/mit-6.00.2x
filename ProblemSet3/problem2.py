"""Problem Set 3, Part B, Problem 2.

You should start by understanding the population dynamics before introducing any drug.

Fill in the function simulationWithoutDrug(num_viruses, max_pop, max_birth_prob, clear_prob, num_trials) that
instantiates a Patient, simulates changes to the virus population for 300 time steps (i.e., 300 calls to update),
and plots the average size of the virus population as a function of time; that is, the x-axis should correspond to the
number of elapsed time steps, and the y-axis should correspond to the average size of the virus population in the
patient. The population at time=0 is the population after the first call to update.

Run the simulation for num_trials trials, where num_trials in this case can be up to 100 trials. Use pylab to produce
a plot (with a single curve) that displays the average result of running the simulation for many trials. Make sure
you run enough trials so that the resulting plot does not change much in terms of shape and time steps taken for the
average size of the virus population to become stable. Don't forget to include axes labels, a legend for the curve,
and a title on your plot.

You should call simulationWithoutDrug with the following parameters:
  - num_viruses = 100
  - max_pop (maximum sustainable virus population) = 1000
  - max_birth_prob (maximum reproduction probability for a virus particle) = 0.1
  - clear_prob (maximum clearance probability for a virus particle) = 0.05

Thus, your simulation should be instantiatating one Patient with a list of 100 SimpleVirus instances. Each SimpleVirus
instance in the viruses list should be initialized with the proper values for max_birth_prob and clear_prob.

Hint: graphing

Consult reference documentation on pylab as reference. Scroll down on the page to find a list of all the plotting
commands in pylab.

Hint: testing your simulation

For further testing, we have provided the .pyc (compiled Python) files for the completed Patient and SimpleVirus
classes (and for Problem 5, the ResistantVirus and TreatedPatient classes) that you can use to confirm that your
code is generating the correct results during simulation.

If you comment out your versions of these classes in ps3b.py, and add the following import statements to the top
of your file, you can run the simulation using our pre-compiled implementation of these classes to make sure you
are obtaining the correct results. This is a good way to test if you've implemented these classes correctly. Make
sure to comment out the import statement and uncomment your implementations before moving to Problem 4.

If you want to use numpy arrays, you should import numpy as np and use np.METHOD_NAME in your code.
"""

import pylab

from ProblemSet3 import Patient, SimpleVirus


def simulation_without_drug(num_viruses, max_pop, max_birth_prob, clear_prob, num_trials):
    """Run the simulation and plot the graph for problem 3.

    No drugs are used, viruses do not have any drug resistance.
    For each of num_trails trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    Args:
        num_viruses (int): number of SimpleVirus to create for patient
        max_pop (int): maximum virus population for patient
        max_birth_prob (float): Maximum reproduction probability, a float between 0-1
        clear_prob (float): Maximum clearance probability, a float between 0-1
        num_trials (int): number of simulation runs to execute
    """
    viruses = [SimpleVirus(max_birth_prob, clear_prob) for i in range(num_viruses)]
    timesteps = 300

    list_of_pop_list = []
    for trial in range(num_trials):
        pop_list = []
        patient = Patient(viruses, max_pop)
        for timestep in range(timesteps):
            pop_list.append(patient.update())
        list_of_pop_list.append(pop_list)

    avg_pop_list = []
    for timestep in range(timesteps):
        pop_list = []
        for trial in range(num_trials):
            pop_list.append(list_of_pop_list[trial][timestep])
        avg_pop_list.append(sum(pop_list) / num_trials)

    pylab.plot(range(timesteps), avg_pop_list)
    pylab.ylabel('Virus Population')
    pylab.xlabel('Timesteps')
    pylab.legend('P')
    pylab.title('Average Virus Population for %i Simulations' % num_trials)
    pylab.show()


def main():
    """Run Problem2."""
    simulation_without_drug(1, 10, 1.0, 0.0, 1)
    simulation_without_drug(100, 200, 0.2, 0.8, 1)
    simulation_without_drug(1, 90, 0.8, 0.1, 1)


if __name__ == '__main__':
    main()
