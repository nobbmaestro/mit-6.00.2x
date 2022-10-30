"""Problem Set 3, Part B, Problem 3.

In this problem, we consider the effects of both administering drugs to the patient and the ability of virus particle
offsprings to inherit or mutate genetic traits that confer drug resistance. As the virus population reproduces,
mutations will occur in the virus offspring, adding genetic diversity to the virus population. Some virus particles
gain favorable mutations that confer resistance to drugs.

ResistantVirus class
In order to model this effect, we introduce a subclass of SimpleVirus called ResistantVirus. ResistantVirus maintains
the state of a virus particle's drug resistances, and accounts for the inheritance of drug resistance traits to
offspring. Implement the ResistantVirus class.

Hint: reproduce function child resistances
"""

from ProblemSet3 import SimpleVirus, get_choice
from ProblemSet3.lib import NoChildException


class ResistantVirus(SimpleVirus):
    """Representation of a virus which can have drug resistance."""

    def __init__(self, max_birth_prob, clear_prob, resistances, mut_prob):
        """Initialize a ResistantVirus instance, saves all parameters as attributes of the instance.

        Args:
            max_birth_prob (float): Maximum reproduction probability, a float between 0-1
            clear_prob (float): Maximum clearance probability, a float between 0-1
            resistances (dict): A dictionary of drug names (strings) mapping to the state of this virus particle's
                resistance (either True or False) to each drug. e.g. {'guttagonol':False, 'srinol':False}, means
                that this virus particle is resistant to neither guttagonol nor srinol.
            mut_prob (float): Mutation probability for this virus particle. This is the probability of the offspring
            acquiring or losing resistance to a drug.
        """
        SimpleVirus.__init__(self, max_birth_prob, clear_prob)
        self.resistances = resistances
        self.mut_prob = mut_prob

    def get_resistances(self):
        """Return the resistances for this virus."""
        return self.resistances

    def get_mut_prob(self):
        """Return the mutation probability for this virus."""
        return self.mut_prob

    def is_resistant_to(self, drug):
        """Get the state of this virus particle's resistance to a drug.

        This method is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.

        Args:
            drug (str): The drug

        Returns:
            bool: True if this virus instance is resistant to the drug, False otherwise.
        """
        try:
            return self.resistances[drug]
        except KeyError:
            return False

    # pylint: disable=W0221, C0103
    def reproduce(self, pop_density, active_drugs):
        """Stochastically determines whether this virus particle reproduces at a time step.

        Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the active_drugs list. For example, if there are 2 drugs in the
        active_drugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in active_drugs, then the virus reproduces with probability:

        self.max_birth_prob * (1 - pop_density).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        max_birth_prob and clear_prob values as its parent). The offspring virus
        will have the same max_birth_prob, clear_prob, and mut_prob as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mut_prob of
        inheriting that resistance trait from the parent, and probability
        mut_prob of switching that resistance trait in the offspring.

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mut_prob is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        Args:
            pop_density (float): the population density, defined as the current virus population divided by the maximum
                population

            active_drugs (list): a list of the drug names acting on this virus particle (a list of strings).

        Returns:
            ResistantVirus: a new instance of the ResistantVirus class representing the offspring of this virus
            particle. The child should have the same max_birth_prob and clear_prob values as this virus.

        Raises:
            NoChildException: if this virus particle does not reproduce.
        """
        for drug in active_drugs:
            if not self.is_resistant_to(drug):
                raise NoChildException('Virus did not reproduce')

        P = self.max_birth_prob * (1-pop_density)
        offspring_resistance = self.resistances
        if get_choice(P):
            for drug in self.resistances.keys():
                if self.is_resistant_to(drug):
                    offspring_resistance[drug] = get_choice(1 - self.mut_prob)
                else:
                    offspring_resistance[drug] = get_choice(self.mut_prob)

            return ResistantVirus(self.max_birth_prob, self.clear_prob, offspring_resistance, self.mut_prob)

        raise NoChildException('Virus did not reproduce')
