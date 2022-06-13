# Final Exam, Problem 4-2
#
# Write a function called getAverage(die, numRolls, numTrials), with the following specification:
#   def getAverage(die, numRolls, numTrials):
#         """
#           - die, a Die
#           - numRolls, numTrials, are positive ints
#           - Calculates the expected mean value of the longest run of a number
#             over numTrials runs of numRolls rolls.
#           - Calls makeHistogram to produce a histogram of the longest runs for all
#             the trials. There should be 10 bins in the histogram
#           - Choose appropriate labels for the x and y axes.
#           - Returns the mean calculated to 3 decimal places
#       """
# A run of numbers counts the number of times the same dice value shows up in consecutive rolls. For example:
#   - a dice roll of 1 4 3 has a longest run of 1
#   - a dice roll of 1 3 3 2 has a longest run of 2
#   - a dice roll of 5 4 4 4 5 5 2 5 has a longest run of 3
# 
# When this function is called with the test case given in the file, it will return 5.312. Your simulation 
# may give slightly different values.
#
# Paste your entire function (including the definition) in the box.
#
# Restrictions:
#   - Do not import or use functions or methods from pylab, numpy, or matplotlib.
#   - Do not leave any debugging print statements when you paste your code in the box.
#
# If you do not see the return value being printed when testing your function, close the histogram window.

from FinalExam import makeHistogram, getMeanAndStd, Die

def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    listOfMeans = []
    for trial in range(numTrials):
        rollsInTrial = []
        for roll in range(numRolls):
            rollsInTrial.append(die.roll())

        longestRunMean = 0
        for value in rollsInTrial:
            if value*rollsInTrial.count(value) / numRolls > longestRunMean:
                longestRunMean = value*rollsInTrial.count(value) / numRolls
        listOfMeans.append(longestRunMean)

    makeHistogram(listOfMeans, 10, xLabel= 'Bins', yLabel= 'Mean of Longest Rolls per Trial')
    return getMeanAndStd(listOfMeans)[0]

def main():
    getAverage(Die([1]), 10, 1000)
    getAverage(Die([1,1]), 10, 1000)
    getAverage(Die([1,2,3,4,5,6]), 50, 1000)
    getAverage(Die([1,2,3,4,5,6,6,6,7]), 50, 1000)
    getAverage(Die([1,2,3,4,5,6,6,6,7]), 1, 1000)

if __name__ == '__main__':
    main()

