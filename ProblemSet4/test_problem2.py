"""Problem Set 4, Problem 2."""

import unittest

from ProblemSet4 import r_squared as func


class TestProblem2(unittest.TestCase):
    """Test class for Problem 2."""

    def setUp(self):
        """Set up function for Problem 2."""
        self.test_data = {
            0: {
                'input': [[32.0, 42.0, 31.3, 22.0, 33.0], [32.3, 42.1, 31.2, 22.1, 34.0]],
                'output': [0.9944]
            },
            1: {
                'input': [[4.4, 5.5, 6.6], [4.4, 5.5, 6.6]],
                'output': [1.0000]
            },
            2: {
                'input': [[-3.1, -4.1, -9.2, 10.1], [-2.1, -6.1, 9.2, 20.1]],
                'output': [-1.1834]
            },
            3: {
                'input': [[-3.1, -4.1, -9.2, 10.1, 9.1, 4.5], [-1.1, -2.1, -7.2, 11.1, 11.1, 5.5]],
                'output': [0.9414]
            },
        }

    def test_output(self):
        """Verifies Problem 2."""
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data:
            arg1 = self.test_data[i]['input'][0]
            arg2 = self.test_data[i]['input'][1]

            result = func(arg1, arg2)
            expected_output = self.test_data[i]['output']

            self.assertAlmostEqual(result, expected_output, delta=0.01, msg=msg.format(i=i, output=expected_output))
