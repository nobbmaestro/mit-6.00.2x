"""Problem Set 3, Part B, Problem 1.

We start with a trivial model of the virus population - the patient does not take any drugs and the viruses do not
acquire resistance to drugs. We simply model the virus population inside a patient as if it were left untreated.

SimpleVirus class
To implement this model, you will need to fill in the SimpleVirus class, which maintains the state of a single
virus particle. You will implement the methods __init__, getmax_birth_prob, getclear_prob,doesClear, and reproduce
according to the specifications. Use random.random() for generating random numbers to ensure that your results are
consistent with ours.

Hint: random seed

The reproduce method in SimpleVirus should produce an offspring by returning a new instance of SimpleVirus with
probability: self.max_birth_prob * (1 - popDensity). This method raises a NoChildException if the virus particle does
not reproduce. For a reminder on raising execptions, review the Python docs.

self.max_birth_prob is the birth rate under optimal conditions (the virus population is negligible relative to the
available host cells so there is ample nourishment available). popDensity is defined as the ratio of the current
virus population to the maximum virus population for a patient and should be calculated in the update method of
the Patient class.

Patient class
You will also need to implement the Patient class, which maintains the state of a virus population associated with
a patient.

The update method in the Patient class is the inner loop of the simulation. It modifies the state of the virus
population for a single time step and returns the total virus population at the end of the time step. At every time
step of the simulation, each virus particle has a fixed probability of being cleared (eliminated from the patient's
body). If the virus particle is not cleared, it is considered for reproduction. If you utilize the population density
correctly, you shouldn't need to provide an explicit check that the virus population exceeds maxPop when you are
calculating how many offspring are added to the population -- you just calculate the new population density and use
that for the next call to update.

Unlike the clearance probability, which is constant, the probability of a virus particle reproducing is a function of
the virus population. With a larger virus population, there are fewer resources in the patient's body to facilitate
reproduction, and the probability of reproduction will be lower. One way to think of this limitation is to consider
that virus particles need to make use of a patient's cells to reproduce; they cannot reproduce on their own. As the
virus population increases, there will be fewer available host cells for viruses to utilize for reproduction.

To summarize, update should first decide which virus particles are cleared and which survive by making use of the
doesClear method of each SimpleVirus instance, then update the collection of SimpleVirus instances accordingly. With
the surviving SimpleVirus instances, update should then call the reproduce method for each virus particle. Based on the
population density of the surviving SimpleVirus instances, reproduce should either return a new instance of SimpleVirus
representing the offspring of the virus particle, or raise a NoChildException indicating that the virus particle does
not reproduce during the current time step. The update method should update the attributes of the patient appropriately
under either of these conditions. After iterating through all the virus particles, the update method returns the number
of virus particles in the patient at the end of the time step.

Hint: mutating objects

Note that the mapping between time steps and actual time will vary depending on the type of virus being considered, but
for this problem set, think of a time step as a simulated hour of time.

About the grader: When defining a Patient class member variable to store the viruses list representing the virus
population, please use the name self.viruses in order for your code to be compatible with the grader and to pass one
of the tests.

Note: If you want to use numpy arrays, you should add the following lines at the beginning of your code for the grader:
  import os
  os.environ["OPENBLAS_NUM_THREADS"] = "1"

Then, do import numpy as np and use np.METHOD_NAME in your code.
"""

import random

from ProblemSet3.lib import NoChildException


# pylint: disable=C0103
def get_choice(P):
    """Return True or False randomly depending on the probability P.

    Args:
        P (float): Probability, float between 0 and 1

    Returns:
        bool: True if random.randint < P * 100, else False:
    """
    return random.randint(0, 100) <= (P * 100)


class SimpleVirus:
    """Representation of a simple virus (does not model drug effects/resistance)."""

    def __init__(self, max_birth_prob, clear_prob):
        """Save all parameters as attributes of the instance.

        Args:
            max_birth_prob (float): Maximum reproduction probability,a float between 0-1
            clear_prob (float): Maximum clearance probability, a float between 0-1
        """
        self.max_birth_prob = max_birth_prob
        self.clear_prob = clear_prob

    def get_max_birth_prob(self):
        """Return the max birth probability."""
        return self.max_birth_prob

    def get_clear_prob(self):
        """Return the clear probability."""
        return self.clear_prob

    def does_clear(self):
        """Stochastically determines whether this virus particle is cleared from the patient's body at a time step.

        Returns:
            bool: True with probability self.getclear_prob and otherwise returns False.
        """
        return get_choice(self.get_clear_prob())

    def reproduce(self, pop_density):
        """Stochastically determines whether this virus particle reproduces at a time step.

        Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.max_birth_prob * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        max_birth_prob and clear_prob values as its parent).

        Args:
            pop_density (float): the population density, defined as the current virus population divided by
            the maximum population.

        Returns:
            SimpleVirus: a new instance of the SimpleVirus class representing the offspring of this virus particle.
            The child should have the same max_birth_prob and clear_prob values as this virus.

        Raises:
            NoChildException: if this virus particle does not reproduce.
        """
        P = self.max_birth_prob * (1-pop_density)
        if get_choice(P):
            return SimpleVirus(self.max_birth_prob, self.clear_prob)

        raise NoChildException('Virus did not reproduce')


class Patient:
    """Representation of a simplified patient.

    The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, max_pop):
        """Save the viruses and maxPop parameters as attributes.

        Args:
            viruses (list): the list representing the virus population (a list of SimpleVirus instances)
            max_pop (int): the maximum virus population for this patient
        """
        self.viruses = viruses
        self.max_pop = max_pop

    def get_viruses(self):
        """Return the viruses in this Patient."""
        return self.viruses

    def get_max_pop(self):
        """Return the max population."""
        return self.max_pop

    def get_total_pop(self):
        """Get the size of the current total virus population.

        Returns:
            int: The total virus population
        """
        return len(self.viruses)

    def update(self):
        """Update the state of the virus population in this patient for a single time step.

        update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update()

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.

        Returns:
            int: The total virus population at the end of the update
        """
        viruses = []
        for virus in self.viruses:
            if not virus.does_clear():
                viruses.append(virus)

        current_pop_den = len(viruses) / self.max_pop

        temp_viruses = viruses.copy()
        for virus in temp_viruses:
            try:
                reproduce = virus.reproduce(current_pop_den)
                if reproduce:
                    viruses.append(reproduce)
            except NoChildException:
                pass

        self.viruses = viruses
        return len(self.viruses)
