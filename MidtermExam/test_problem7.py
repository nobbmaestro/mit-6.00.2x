"""Midterm Exam, Problem 7."""

import unittest

from MidtermExam import solve_it as func


class TestProblem7(unittest.TestCase):
    """Test class for Problem 7."""

    def setUp(self):
        """Set up TestProblem7."""
        self.test_data = {
            0: {
                'input': lambda x: x == 0,
                'output': 0
            },
            1: {
                'input': lambda x: (x + 15)**0.5 + x**0.5 == 15,
                'output': 49
            },
            2: {
                'input': lambda x: x == 100,
                'output': 100
            },
            3: {
                'input': lambda x: x == 26,
                'output': 26
            },
            4: {
                'input': lambda x: x**2 == 9,
                'output': 3
            },
            5: {
                'input': lambda x: x == -4,
                'output': -4
            },
            6: {
                'input': lambda x: x**2 + x + 0 == 0,
                'output': 0
            },
            7: {
                'input': lambda x: x == -80,
                'output': -80
            },
            8: {
                'input': lambda x: x == 2,
                'output': 2
            },
            9: {
                'input': lambda x: [1, 2, 3][-x] == 1 and x != 0,
                'output': 3
            },
            10: {
                'input': lambda x: x**2 + x + 0 == 0,
                'output': 0
            },
        }

    def test_output(self):
        """Verifies Problem 7."""
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data:
            arg1 = self.test_data[i]['input']

            result = func(arg1)
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))
