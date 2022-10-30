"""Problem Set 3, Part B, Problem 5.

In this problem, we will use the implementation you filled in for Problem 4 to run a simulation. You will
create a TreatedPatient instance with the following parameters, then run the simulation:
  - viruses, a list of 100 ResistantVirus instances
  - max_pop, maximum sustainable virus population = 1000
  - Each ResistantVirus instance in the viruses list should be initialized with the following parameters:
  - max_birth_prob, maximum reproduction probability for a virus particle = 0.1
  - clear_prob, maximum clearance probability for a virus particle = 0.05
  - resistances, The virus's genetic resistance to drugs in the experiment = {'guttagonol': False}
  - mut_prob, probability of a mutation in a virus particle's offspring = 0.005

Run a simulation that consists of 150 time steps, followed by the addition of the drug, guttagonol, followed
by another 150 time steps. You should make use of the function simulationWithDrug(num_viruses, max_pop, max_birth_prob,
clear_prob, resistances, mut_prob, num_trials). As with problem 3, perform up to 100 trials and make sure that your
results are repeatable and representative.

Create one plot that records both the average total virus population and the average population of guttagonol-
resistant virus particles over time.

A few good questions to consider as you look at your plots are: What trends do you observe? Are the trends
consistent with your intuition? Feel free to discuss the answers to these questions in the forum, to fully
cement your understanding of this problem set, processing and interpreting data.

Again, as in Problem 2, you can use the provided .pyc file to check that your implementation of the TreatedPatient
and ResistantVirus classes work as expected.

If you want to use numpy arrays, you should import numpy as np and use np.METHOD_NAME in your code.
"""

import pylab

from ProblemSet3 import ResistantVirus, TreatedPatient


def simulation_with_drug(num_viruses, max_pop, max_birth_prob, clear_prob, resistances, mut_prob, num_trials):
    """Run simulations and plots graphs for problem 5.

    For each of num_trials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    Args:
        num_viruses (int): number of ResistantVirus to create for patient
        max_pop (int): maximum virus population for patient
        max_birth_prob (float): Maximum reproduction probability, a float between 0-1
        clear_prob (float): maximum clearance probability, a float between 0-1
        resistances (dict): a dictionary of drugs that each ResistantVirus is resistant to, e.g., {'guttagonol': False}
        mut_prob (float): mutation probability for each ResistantVirus particle, a float between 0-1
        num_trials (int): number of simulation runs to execute
    """
    avg_vpop = [0] * 300
    avg_rvpop = [0] * 300

    for trail in range(num_trials):
        virus = [ResistantVirus(max_birth_prob, clear_prob, resistances, mut_prob)] * num_viruses
        patient = TreatedPatient(virus, max_pop)

        for i in range(300):
            patient.update()
            avg_vpop[i] = avg_vpop[i] + patient.get_total_pop()
            avg_rvpop[i] = avg_rvpop[i] + patient.get_resist_pop(['guttagonol'])

            if i + 1 == 150:
                patient.add_prescription('guttagonol')

            if trail + 1 == num_trials:
                avg_vpop[i] = avg_vpop[i] / num_trials
                avg_rvpop[i] = avg_rvpop[i] / num_trials

    pylab.plot(avg_vpop, label="ResistantVirus")
    pylab.plot(avg_rvpop, label="Guttagonol ResistantVirus")
    pylab.title("Resistant Virus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc="best")
    pylab.show()


def main():
    """Run Problem5."""
    simulation_with_drug(1, 10, 1.0, 0.0, {}, 1.0, 5)
    simulation_with_drug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)
    simulation_with_drug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)


if __name__ == '__main__':
    main()
