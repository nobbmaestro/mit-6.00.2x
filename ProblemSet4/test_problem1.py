# Problem Set 4, Problem 1

import unittest
import numpy as np

from ProblemSet4 import generate_models as func

class TestProblem1(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            0: {
                'input': [[1900, 1901, 1902, 1904, 2000], [32.0, 42.0, 31.3, 22.0, 33.0], [2]], 
                'output': [np.array([  3.51667102e-02,  -1.37199002e+02,   1.33764160e+05])]
            },
            1: {
                'input': [[1961, 1962, 1963], [4.4, 5.5, 6.6], [1, 2]], 
                'output': [
                    np.array([  1.10000000e+00,  -2.15270000e+03]), 
                    np.array([ -8.86320608e-14,   1.10000000e+00,  -2.15270000e+03])
                ]
            },
            2: {
                'input': [[1960, 1997, 1999, 2001], [-3.1, -4.1, -9.2, 10.1], [1, 2, 3]], 
                'output': [
                    np.array([  7.64961915e-02,  -1.53745049e+02]), 
                    np.array([  9.24663056e-02,  -3.66029000e+02,   3.62195201e+05]), 
                    np.array([  7.59680860e-02,  -4.52530612e+02,   8.98514989e+05,     -5.94652222e+08])
                ]
            },
            3: {
                'input': [[1960, 1997, 1999, 2001, 1998, 1995], [-3.1, -4.1, -9.2, 10.1, 9.1, 4.5], [1, 2, 3, 4]], 
                'output': [
                    np.array([  1.43651226e-01,  -2.84888692e+02]), 
                    np.array([  1.45050481e-02,  -5.72778422e+01,   5.65389304e+04]), 
                    np.array([  2.41178585e-02,  -1.43636842e+02,   2.85137445e+05,     -1.88670385e+08]), 
                    np.array([  1.14194270e-02,  -9.08068327e+01,   2.70778566e+05,     -3.58853930e+08,   1.78337425e+11])
                ]
            },
        }
    
    def test_output(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data.keys():
            arg1 = self.test_data[i]['input'][0]
            arg2 = self.test_data[i]['input'][1]
            arg3 = self.test_data[i]['input'][2]

            result = func(arg1, arg2, arg3)
            expected_output = self.test_data[i]['output']

            for j in range(len(result)):
                test = np.allclose(result[j], expected_output[j])
                self.assertEqual(test, True, msg.format(i=i, output=expected_output))