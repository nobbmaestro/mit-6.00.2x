# Final Exam, Problem 3

import unittest

from FinalExam import guessfood_sim as func

class TestProblem3(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            0:  {'input': [100,  [1, 1, 1], 1, 0],              'output': (-3.0, 0.0)},
            1:  {'input': [100,  [1, 1, 1], 1, 1],              'output': (0.0, 0.0)},
            2:  {'input': [100,  [1, 1, 1], 0, 1],              'output': (3.0, 0.0)},
            3:  {'input': [100,  [1, 1, 1], 0, 0],              'output': (0.0, 0.0)},
            4:  {'input': [100,  [0, 1, 1], 0, 1],              'output': (2.0, 0.0)},
            5:  {'input': [100,  [0, 1, 0], 1, 0],              'output': (-3.0, 0.0)},
            6:  {'input': [100,  [0, 1, 1], 0.5, 1],            'output': (0.5, 0.0)},
            7:  {'input': [100,  [0, 1, 0], 1, 0.5],            'output': (-2.5, 0.0)},
            8:  {'input': [100,  [0, 1, 0], 1, 0.5],            'output': (-2.5, 0.0)},
            9:  {'input': [3000, [0.5, 0.5, 0.5], 1, 1],        'output': (-1.4856666666666667, 0.8546702418021968)},
            10: {'input': [3000, [0.5, 0.5, 0.5], 2, 3.5],      'output': (-0.673, 3.0502575301112116)},
            11: {'input': [3000, [0.25, 0.5, 0.75], 1.5, 2.5],  'output': (-0.7208333333333333, 1.9903892346863998)},
            12: {'input': [3000, [0.5, 0.4, 0.9], 2.2, 10.3],   'output': (12.097933333333357, 7.910897698463439)},
            13: {'input': [3000, [0.1, 0.1, 0.7], 0.5, 0.8],    'output': (-0.763466666666678, 0.5066214716684908)},
            14: {'input': [3000, [0.5, 0.1, 0.5], 1, 1],        'output': (-1.879, 0.7679142747294933)},
            15: {'input': [3000, [0.11, 0.2, 0.5], 2, 2.5],     'output': (-3.910833333333333, 1.8359736669014488)},
            16: {'input': [3000, [0.25, 0.3, 0.7], 1.2, 2.1],   'output': (-0.9057000000000098, 1.6759407835600957)},
            17: {'input': [3000, [0.3, 0.001, 0.1], 3, 3],      'output': (-7.779, 1.6468633823119228)},
            18: {'input': [3000, [0.1, 0.99, 0.4], 1, 1],       'output': (-1.4993333333333334, 0.5893495472882623)},
        }

    def test_output(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data.keys():
            arg1 = self.test_data[i]['input'][0]
            arg2 = self.test_data[i]['input'][1]
            arg3 = self.test_data[i]['input'][2]
            arg4 = self.test_data[i]['input'][3]

            result = func(arg1, arg2, arg3, arg4)
            expected_output = self.test_data[i]['output']

            for j in range(len(result)):
                self.assertAlmostEqual(result[j], expected_output[j], delta=0.5, msg=msg.format(i=i, output=expected_output))