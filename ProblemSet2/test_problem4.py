import unittest
import random

from ProblemSet2 import runSimulation, StandardRobot

class TestProblem4(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            0: {'input': [1, 1.0, 5,  5,  0.78], 'output': 34.6},
            1: {'input': [1, 1.0, 10, 12, 0.96], 'output': 382.82},
            2: {'input': [1, 2.0, 12, 12, 0.96], 'output': 442.84},
            3: {'input': [2, 1.0, 8,  8,  0.80], 'output': 50.08},
            4: {'input': [2, 3.0, 15, 13, 0.98], 'output': 397.58},
        }
    
    def test_runSimulation(self):
        random.seed(0)

        for i in self.test_data.keys():
            arg1 = self.test_data[i]['input'][0]
            arg2 = self.test_data[i]['input'][1]
            arg3 = self.test_data[i]['input'][2]
            arg4 = self.test_data[i]['input'][3]
            arg5 = self.test_data[i]['input'][4]

            result = runSimulation(arg1, arg2, arg3, arg4, arg5, 100, StandardRobot)
            expected_result = self.test_data[i]['output']

            self.assertEqual(result, expected_result)