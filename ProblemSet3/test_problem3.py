"""Problem Set 3, Part B, Problem 3."""

import unittest

from ProblemSet3 import ResistantVirus
from ProblemSet3.lib import NoChildException


class TestResistantVirus(unittest.TestCase):
    """Test class for ResistantVirus, Problem 3."""

    def setUp(self):
        """Set up TestResistantVirus."""
        self.test_data = {
            # Create a ResistantVirus that is never cleared and always reproduces.
            0: {
                'input': [1.00, 0.00, {}, 0.00],
                'output': [False, False]
            },

            # Create a ResistantVirus that is never cleared and never reproduces.
            1: {
                'input': [0.00, 0.00, {}, 0.00],
                'output': [True, False]
            },

            # Create a ResistantVirus that is always cleared and always reproduces.
            2: {
                'input': [1.00, 1.00, {}, 0.00],
                'output': [False, True]
            },

            # Create a ResistantVirus that is always cleared and never reproduces.
            3: {
                'input': [0.00, 1.00, {}, 0.00],
                'output': [True, True]
            },
        }

    def test_resistive_virus(self):
        """Verifies ResistantVirus, Problem 3."""
        for i in self.test_data:
            arg1 = self.test_data[i]['input'][0]
            arg2 = self.test_data[i]['input'][1]
            arg3 = self.test_data[i]['input'][2]
            arg4 = self.test_data[i]['input'][3]
            virus = ResistantVirus(arg1, arg2, arg3, arg4)

            shall_raise = self.test_data[i]['output'][0]
            expected_result = self.test_data[i]['output'][1]

            if shall_raise:
                self.assertRaises(NoChildException, virus.reproduce, 0, [])
            else:
                self.assertEqual(type(virus.reproduce(0, [])), type(virus))

            self.assertEqual(virus.does_clear(), expected_result)

    def test_virus_resistances(self):
        """Verifies ResistantVirus, Problem 3."""
        arg1 = 1.0
        arg2 = 0.0
        arg3 = {"drug1": True, "drug2": False}
        arg4 = 0.0
        virus = ResistantVirus(arg1, arg2, arg3, arg4)

        self.assertRaises(NoChildException, virus.reproduce, 0, ['drug2'])
        self.assertIsInstance(virus.reproduce(0, ["drug1"]), type(virus))

    def test_virus_mut_prob(self):
        """Verifies ResistantVirus, Problem 3."""
        arg1 = 1.0
        arg2 = 0.0
        arg3 = {'drug1': True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}
        arg4 = 0.5
        virus = ResistantVirus(arg1, arg2, arg3, arg4)

        for _ in range(10):
            child = virus.reproduce(0, [])
            for drug in arg3:
                self.assertEqual(child.is_resistant_to(drug), arg3[drug])

    def test_positive_mutability(self):
        """Verifies ResistantVirus, Problem 3."""
        arg1 = 1.0
        arg2 = 0.0
        arg3 = {'drug2': True}
        arg4 = 1.0
        virus = ResistantVirus(arg1, arg2, arg3, arg4)

        for _ in range(100):
            child = virus.reproduce(0, [])
            for drug in arg3:
                self.assertEqual(child.is_resistant_to(drug), arg3[drug])

    def test_negative_mutability(self):
        """Verifies ResistantVirus, Problem 3."""
        arg1 = 1.0
        arg2 = 0.0
        arg3 = {'drug2': True}
        arg4 = 0.0
        virus = ResistantVirus(arg1, arg2, arg3, arg4)

        for _ in range(100):
            child = virus.reproduce(0, [])
            for drug in arg3:
                self.assertEqual(child.is_resistant_to(drug), arg3[drug])

    def test_virus_reproduction_with_drugs_applied(self):
        """Verifies ResistantVirus, Problem 3."""
        arg1 = 0.0
        arg2 = 0.0
        arg3 = {"drug1": True, "drug2": False}
        arg4 = 0.0
        virus = ResistantVirus(arg1, arg2, arg3, arg4)

        self.assertRaises(NoChildException, virus.reproduce, 0, ['drug2'])
        self.assertRaises(NoChildException, virus.reproduce, 0, ['drug1'])
