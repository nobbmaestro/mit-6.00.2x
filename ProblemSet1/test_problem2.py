import unittest

from ProblemSet1 import brute_force_cow_transport as func

class TestProblem1(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            0:  {
                    'input':  [{'Boo': 20, 'Milkshake': 40, 'Horns': 25, 'MooMoo': 50, 'Miss Bella': 25, 'Lotus': 40}, 100],
                    'output': len([['Boo', 'Lotus', 'Milkshake'], ['Horns', 'MooMoo', 'Miss Bella']])
                },
            1:  {
                    'input':  [{'Betsy': 65, 'Buttercup': 72, 'Daisy': 50}, 75],    
                    'output': len([['Daisy'], ['Betsy'], ['Buttercup']])
                },
            2:  {
                    'input':  [{'Starlight': 54, 'Betsy': 39, 'Luna': 41, 'Buttercup': 11}, 145],    
                    'output': len([['Buttercup', 'Starlight', 'Betsy', 'Luna']])
                },
        }

    def test_output(self):
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in self.test_data.keys():
            arg1 = self.test_data[i]['input'][0]
            arg2 = self.test_data[i]['input'][1]

            result = len(func(arg1, arg2))
            expected_output = self.test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))