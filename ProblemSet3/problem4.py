# Problem Set 3, Part B, Problem 3
#
# We also need a representation for a patient that accounts for the use of drug treatments and manages a collection of 
# ResistantVirus instances. For this, we introduce the TreatedPatient class, which is a subclass of Patient. TreatedPatient 
# must make use of the new methods in ResistantVirus and maintain the list of drugs that are administered to the patient.
#
# Drugs are given to the patient using the TreatedPatient class's addPrescription() method. What happens when a drug is 
# introduced? The drugs we consider do not directly kill virus particles lacking resistance to the drug, but prevent those 
# virus particles from reproducing (much like actual drugs used to treat HIV). Virus particles with resistance to the drug 
# continue to reproduce normally. Implement the TreatedPatient class.
#
# Hint: reproduce function child resistances
#
# If you want to use numpy arrays, you should import numpy as np and use np.METHOD_NAME in your code.

from ProblemSet3 import Patient, NoChildException

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        Patient.__init__(self, viruses, maxPop)
        self.listOfDrugs = []


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if newDrug not in self.listOfDrugs:
            self.listOfDrugs.append(newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.listOfDrugs


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        resViruses = []
        for virus in self.viruses:
            temp = []
            for drug in drugResist:
                temp.append(virus.isResistantTo(drug))
            if False in temp:
                resViruses.append(False)
            else:
                resViruses.append(True)

        return resViruses.count(True)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        viruses = []
        for virus in self.viruses:
            if not virus.doesClear():
                res_drug_test = []
                for drug in self.getPrescriptions():
                    res_drug_test.append(virus.isResistantTo(drug))

                if False not in res_drug_test:
                    viruses.append(virus)

        currentPopDen = len(viruses) / self.maxPop

        temp_viruses = viruses.copy()
        for virus in temp_viruses:
            try:
                repr = virus.reproduce(currentPopDen, self.getPrescriptions())
                if repr:
                    viruses.append(repr)
            except NoChildException:
                pass

        self.viruses = viruses
        return len(self.viruses)

def main():
    from ProblemSet3 import ResistantVirus

    test_data = {
        0: {'input': [1.0, 0.0, {}, 0.0]},
        1: {'input': [1.0, 1.0, {}, 0.0]},
    }
    virus = ResistantVirus(1.0, 1.0, {}, 0.0)
    patient = TreatedPatient([virus], 100)

    tmp = []
    for i in range(100):
        tmp.append(patient.update())
        print(sum(tmp)/len(tmp))
    
if __name__ == '__main__':
    main()