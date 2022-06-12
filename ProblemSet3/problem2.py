# Problem Set 3, Part B, Problem 2
# 
# You should start by understanding the population dynamics before introducing any drug.
#
# Fill in the function simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials) that instantiates 
# a Patient, simulates changes to the virus population for 300 time steps (i.e., 300 calls to update), and plots the 
# average size of the virus population as a function of time; that is, the x-axis should correspond to the number of 
# elapsed time steps, and the y-axis should correspond to the average size of the virus population in the patient. 
# The population at time=0 is the population after the first call to update.
#
# Run the simulation for numTrials trials, where numTrials in this case can be up to 100 trials. Use pylab to produce 
# a plot (with a single curve) that displays the average result of running the simulation for many trials. Make sure 
# you run enough trials so that the resulting plot does not change much in terms of shape and time steps taken for the 
# average size of the virus population to become stable. Don't forget to include axes labels, a legend for the curve, 
# and a title on your plot.
#
# You should call simulationWithoutDrug with the following parameters:
#   - numViruses = 100
#   - maxPop (maximum sustainable virus population) = 1000
#   - maxBirthProb (maximum reproduction probability for a virus particle) = 0.1
#   - clearProb (maximum clearance probability for a virus particle) = 0.05
#
# Thus, your simulation should be instantiatating one Patient with a list of 100 SimpleVirus instances. Each SimpleVirus 
# instance in the viruses list should be initialized with the proper values for maxBirthProb and clearProb.
#
# Hint: graphing
#
# Consult reference documentation on pylab as reference. Scroll down on the page to find a list of all the plotting 
# commands in pylab.
#
# Hint: testing your simulation
#
# For further testing, we have provided the .pyc (compiled Python) files for the completed Patient and SimpleVirus 
# classes (and for Problem 5, the ResistantVirus and TreatedPatient classes) that you can use to confirm that your 
# code is generating the correct results during simulation.
#
# If you comment out your versions of these classes in ps3b.py, and add the following import statements to the top 
# of your file, you can run the simulation using our pre-compiled implementation of these classes to make sure you 
# are obtaining the correct results. This is a good way to test if you've implemented these classes correctly. Make 
# sure to comment out the import statement and uncomment your implementations before moving to Problem 4.
#
# If you want to use numpy arrays, you should import numpy as np and use np.METHOD_NAME in your code.

import pylab

from ProblemSet3 import SimpleVirus, Patient

def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    viruses = [SimpleVirus(maxBirthProb, clearProb) for i in range(numViruses)]
    timesteps = 300

    listOfPopList = []
    for trial in range(numTrials):
        popList = []
        patient = Patient(viruses, maxPop)
        for timestep in range(timesteps):
            popList.append(patient.update())
        listOfPopList.append(popList)

    avgPopList = []
    for timestep in range(timesteps):
        popList = []
        for trial in range(numTrials):
            popList.append(listOfPopList[trial][timestep])
        avgPopList.append(sum(popList) / numTrials)

    pylab.plot(range(timesteps), avgPopList)
    pylab.ylabel('Virus Population')
    pylab.xlabel('Timesteps')
    pylab.legend('P')
    pylab.title('Average Virus Population for %i Simulations' % numTrials)
    pylab.show()

def main():
    simulationWithoutDrug(1, 10, 1.0, 0.0, 1)
    simulationWithoutDrug(100, 200, 0.2, 0.8, 1)
    simulationWithoutDrug(1, 90, 0.8, 0.1, 1)

if __name__ == '__main__':
    main()