"""Test Problem Set 1, Problem 1."""

import unittest

from ProblemSet1 import greedy_cow_transport as func


class TestProblem1(unittest.TestCase):
    """Test class for Problem 1."""

    def setUp(self):
        """Set up TestProblem1."""
        self.test_data = {
            0: {
                'input': [{
                    'Lotus': 10,
                    'Muscles': 65,
                    'Louis': 45,
                    'Horns': 50,
                    'Milkshake': 75,
                    'Polaris': 20,
                    'Miss Bella': 15,
                    'MooMoo': 85,
                    'Clover': 5,
                    'Patches': 60
                }, 100],
                'output': [['MooMoo', 'Miss Bella'], ['Milkshake', 'Polaris', 'Clover'], ['Muscles', 'Lotus'],
                           ['Patches'], ['Horns', 'Louis']]
            },
            1: {
                'input': [{
                    'Coco': 10,
                    'Daisy': 50,
                    'Abby': 38,
                    'Lilly': 24,
                    'Dottie': 85,
                    'Willow': 35,
                    'Rose': 50,
                    'Buttercup': 72,
                    'Betsy': 65,
                    'Patches': 12
                }, 100],
                'output': [['Dottie', 'Patches'], ['Buttercup', 'Lilly'], ['Betsy', 'Willow'], ['Daisy', 'Rose'],
                           ['Abby', 'Coco']]
            },
            2: {
                'input': [{
                    'Coco': 59,
                    'Willow': 59,
                    'Starlight': 54,
                    'Abby': 28,
                    'Rose': 42,
                    'Buttercup': 11,
                    'Betsy': 39,
                    'Luna': 41
                }, 120],
                'output': [['Willow', 'Coco'], ['Starlight', 'Rose', 'Buttercup'], ['Luna', 'Betsy', 'Abby']]
            },
        }

    def test_output(self):
        """Verifies Problem 1."""
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data:
            arg1 = self.test_data[i]['input'][0]
            arg2 = self.test_data[i]['input'][1]

            result = func(arg1, arg2)
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))
