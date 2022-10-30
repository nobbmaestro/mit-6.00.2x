"""Problem Set 3, Part B, Problem 3.

We also need a representation for a patient that accounts for the use of drug treatments and manages a collection of
ResistantVirus instances. For this, we introduce the TreatedPatient class, which is a subclass of Patient.
TreatedPatient must make use of the new methods in ResistantVirus and maintain the list of drugs that are administered
to the patient.

Drugs are given to the patient using the TreatedPatient class's add_prescription() method. What happens when a drug is
introduced? The drugs we consider do not directly kill virus particles lacking resistance to the drug, but prevent those
virus particles from reproducing (much like actual drugs used to treat HIV). Virus particles with resistance to the drug
continue to reproduce normally. Implement the TreatedPatient class.

Hint: reproduce function child resistances

If you want to use numpy arrays, you should import numpy as np and use np.METHOD_NAME in your code.
"""

from ProblemSet3 import Patient
from ProblemSet3.lib import NoChildException


class TreatedPatient(Patient):
    """Representation of a patient.

    The patient is able to take drugs and his/her virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, max_pop):
        """Save the viruses and max_pop parameters as attributes.

        Also initializes the list of drugs being administered (which should initially include no drugs).

        Args:
            viruses (list): The list representing the virus population (a list of virus instances)
            max_pop (int): The  maximum virus population for this patient
        """
        Patient.__init__(self, viruses, max_pop)
        self.list_of_drugs = []

    def add_prescription(self, new_drug):
        """Administer a drug to this patient.

        After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        new_drug is already prescribed to this patient, the method has no effect.

        Args:
            new_drug (str): The name of the drug to administer to the patient
        """
        if new_drug not in self.list_of_drugs:
            self.list_of_drugs.append(new_drug)

    def get_prescriptions(self):
        """Return the drugs that are being administered to this patient.

        Returns:
            list: The list of drug names (strings) being administered to this patient.
        """
        return self.list_of_drugs

    def get_resist_pop(self, drug_resist):
        """Get the population of virus particles resistant to the drugs listed in drug_resist.

        Args:
            drug_resist (list): Which drug resistances to include in the population (a list
                of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        Returns:
            int: The population of viruses with resistances to all drugs in the drug_resist list.
        """
        res_viruses = []
        for virus in self.viruses:
            temp = []
            for drug in drug_resist:
                temp.append(virus.is_resistant_to(drug))
            if False in temp:
                res_viruses.append(False)
            else:
                res_viruses.append(True)

        return res_viruses.count(True)

    def update(self):
        """Update the state of the virus population in this patient for a single time step.

        update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        Returns:
            int: The total virus population at the end of the update
        """
        viruses = []
        for virus in self.viruses:
            if not virus.does_clear():
                res_drug_test = []
                for drug in self.get_prescriptions():
                    res_drug_test.append(virus.is_resistant_to(drug))

                if False not in res_drug_test:
                    viruses.append(virus)

        current_pop_den = len(viruses) / self.max_pop

        temp_viruses = viruses.copy()
        for virus in temp_viruses:
            try:
                reproduce = virus.reproduce(current_pop_den, self.get_prescriptions())
                if reproduce:
                    viruses.append(reproduce)
            except NoChildException:
                pass

        self.viruses = viruses
        return len(self.viruses)
