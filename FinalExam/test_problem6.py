"""Final Exam, Problem 6."""

import unittest

import numpy as np

from FinalExam import find_combination as func


class TestProblem6(unittest.TestCase):
    """Test class for Problem 6."""

    def setUp(self):
        """Set up TestProblem6."""
        self.test_data = {
            0: {
                'input': [[3, 10, 2, 1, 5], 12],
                'output': np.array([0, 1, 1, 0, 0])
            },
            1: {
                'input': [[10, 100, 1000, 3, 8, 12, 38], 1171],
                'output': np.array([1, 1, 1, 1, 1, 1, 1])
            },
            2: {
                'input': [[21, 15, 100, 19, 12], 12],
                'output': np.array([0, 0, 0, 0, 1])
            },
            3: {
                'input': [[10, 10, 11, 11, 11], 20],
                'output': np.array([1, 1, 0, 0, 0])
            },
            4: {
                'input': [[4, 6, 3, 5, 2], 10],
                'output': np.array([0, 0, 1, 1, 1])
            },
            5: {
                'input': [[1, 3, 4, 2, 5], 16],
                'output': np.array([1, 1, 1, 1, 1])
            },
            6: {
                'input': [[4, 10, 3, 5, 8], 1],
                'output': np.array([0, 0, 0, 0, 0])
            },
            7: {
                'input': [[1, 81, 3, 102, 450, 10], 9],
                'output': np.array([1, 0, 1, 0, 0, 0])
            },
            8: {
                'input': [[105, 10, 9, 6, 4], 120],
                'output': np.array([1, 0, 1, 1, 0])
            },
            9: {
                'input': [[1], 10],
                'output': np.array([1])
            },
        }

    def test_output(self):
        """Verifies Problem 6."""
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data:
            arg1 = self.test_data[i]['input'][0]
            arg2 = self.test_data[i]['input'][1]

            result = func(arg1, arg2)
            expected_output = self.test_data[i]['output']

            for j, value in enumerate(result):
                self.assertEqual(value, expected_output[j], msg=msg.format(i=i, output=expected_output))
