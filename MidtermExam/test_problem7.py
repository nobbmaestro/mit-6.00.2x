# Midterm Exam, Problem 7

import unittest

from MidtermExam import solveit as func

class TestProblem7(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            0:  {'input': lambda x: x == 0,                      'output': 0},
            1:  {'input': lambda x: (x+15)**0.5 + x**0.5 == 15,  'output': 49},
            2:  {'input': lambda x: x == 100,                    'output': 100},
            3:  {'input': lambda x: x == 26,                     'output': 26},
            4:  {'input': lambda x: x**2 == 9,                   'output': 3},
            5:  {'input': lambda x: x == -4,                     'output': -4},
            6:  {'input': lambda x: x**2 + x + 0 == 0,           'output': 0},
            7:  {'input': lambda x: x == -80,                    'output': -80},
            6:  {'input': lambda x: x == 2,                      'output': 2},
            6:  {'input': lambda x: [1,2,3][-x] == 1 and x != 0, 'output': 3},
            6:  {'input': lambda x: x**2 + x + 0 == 0,           'output': 0},
        }

    def test_output(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data.keys():
            arg1 = self.test_data[i]['input']

            result = func(arg1)
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))