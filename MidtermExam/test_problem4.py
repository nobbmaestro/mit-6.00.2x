import unittest

from MidtermExam import solve as func

class TestProblem7(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            0:  {'input': 1,   'output': [0, 0, 0, 1]},
            1:  {'input': 5,   'output': [0, 0, 1, 0]},
            2:  {'input': 10,  'output': [0, 1, 0, 0]},
            3:  {'input': 25,  'output': [1, 0, 0, 0]},
            4:  {'input': 4,   'output': [0, 0, 0, 4]},
            5:  {'input': 20,  'output': [0, 2, 0, 0]},
            6:  {'input': 50,  'output': [2, 0, 0, 0]},
            7:  {'input': 15,  'output': [0, 1, 1, 0]},
            8:  {'input': 35,  'output': [1, 1, 0, 0]},
            9:  {'input': 26,  'output': [1, 0, 0, 1]},
            10: {'input': 27,  'output': [1, 0, 0, 2]},
            11: {'input': 28,  'output': [1, 0, 0, 3]},
            12: {'input': 29,  'output': [1, 0, 0, 4]},
            13: {'input': 30,  'output': [1, 0, 1, 0]},
            14: {'input': 99,  'output': [3, 2, 0, 4]},
            15: {'input': 100, 'output': [4, 0, 0, 0]},
        }

    def test_output(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data.keys():
            arg1 = self.test_data[i]['input']

            result = func(arg1)
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))