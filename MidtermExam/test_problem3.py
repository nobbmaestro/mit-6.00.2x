import unittest

from MidtermExam import greedySum as func

class TestProblem7(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            0:  {'input': [[], 10],                    'output': 'no solution'},
            1:  {'input': [[1], 20],                   'output': 20},
            2:  {'input': [[2], 5],                    'output': 'no solution'},
            3:  {'input': [[10, 5, 1], 14],            'output': 5},
            4:  {'input': [[10, 9, 8, 1], 20],         'output': 2},
            5:  {'input': [[10, 8, 5, 1], 13],         'output': 4},
            6:  {'input': [[15, 12, 4, 3, 1], 29],     'output': 4},
            7:  {'input': [[16, 12, 5, 3, 1], 15],     'output': 2},
            8:  {'input': [[16, 12, 5, 3, 1], 24],     'output': 3},
            9:  {'input': [[10, 8, 5, 2], 16],         'output': 'no solution'},
            10: {'input': [[10, 8, 5, 2], 16],         'output': 'no solution'},
            11: {'input': [[11, 10, 8, 5, 1], 16],     'output': 2},
            12: {'input': [[12, 10 , 8, 5, 2], 17],    'output': 2},
            13: {'input': [[20, 10, 4, 3, 1], 21],     'output': 2},
            14: {'input': [[21, 10, 8, 3, 1], 11],     'output': 2},
            15: {'input': [[30, 20, 10], 60],          'output': 2},
            16: {'input': [[50, 25, 5], 5],            'output': 1},
            17: {'input': [[101, 51, 11, 2, 1], 3000], 'output': 36},
        }

    def test_output(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data.keys():
            arg1 = self.test_data[i]['input'][0]
            arg2 = self.test_data[i]['input'][1]

            result = func(arg1, arg2)
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))