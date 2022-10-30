"""Problem Set 3, Part B, Problem 1."""

import random
import unittest

from ProblemSet3 import Patient, SimpleVirus
from ProblemSet3.lib import NoChildException


class TestSimpleVirus(unittest.TestCase):
    """Test class for SimpleVirus, Problem 1."""

    def setUp(self):
        """Set up TestSimpleVirus."""
        self.test_data = {
            # Initialize a SimpleVirus that is never cleared and always reproduces
            0: {
                'input': [1.00, 0.00, 0.00],
                'output': [False, False]
            },

            # Initialize a SimpleVirus that is never cleared and never reproduces
            1: {
                'input': [0.00, 0.00, 0.00],
                'output': [False, True]
            },

            # Initialize a SimpleVirus that is always cleared and always reproduces
            2: {
                'input': [1.00, 1.00, 0.00],
                'output': [True, False]
            },

            # Initialize a SimpleVirus that is always cleared and never reproduces
            3: {
                'input': [0.00, 1.00, 0.00],
                'output': [True, True]
            },
        }

    def test_init(self):
        """Verifies SimpleVirus, Problem 1."""
        arg1 = random.randint(0, 100) / 100
        arg2 = random.randint(0, 100) / 100
        test_object = SimpleVirus(arg1, arg2)
        self.assertEqual(test_object.max_birth_prob, arg1)
        self.assertEqual(test_object.clear_prob, arg2)

    def test_simple_virus(self):
        """Verifies SimpleVirus, Problem 1."""
        msg = 'Failed at {i}:{j}. Expected: {exp}, Got: {res}'
        for i in self.test_data:
            arg1 = self.test_data[i]['input'][0]
            arg2 = self.test_data[i]['input'][1]
            arg3 = self.test_data[i]['input'][2]

            expected_result = self.test_data[i]['output'][0]
            shall_raise = self.test_data[i]['output'][1]

            test_object = SimpleVirus(arg1, arg2)
            for j in range(10):
                if shall_raise:
                    self.assertRaises(NoChildException, test_object.reproduce, arg3)
                    result = test_object.does_clear()
                    self.assertEqual(result, expected_result, msg.format(i=i, j=j, exp=expected_result, res=result))

                else:
                    test_object.reproduce(arg3)
                    result = test_object.does_clear()
                    self.assertEqual(result, expected_result, msg.format(i=i, j=j, exp=expected_result, res=result))


class TestPatient(unittest.TestCase):
    """Test class for Patient, Problem 1."""

    def setUp(self):
        """Set up TestPatient."""
        self.test_data = {
            0: {
                'input': [1.00, 0.00]
            },
            1: {
                'input': [1.00, 1.00]
            },
        }

    def test_init(self):
        """Verifies Patient, Problem 1."""
        viruses = []
        for _ in range(random.randint(1, 5)):
            arg1 = random.randint(0, 100) / 100
            arg2 = random.randint(0, 100) / 100
            viruses.append(SimpleVirus(arg1, arg2))

        test_object = Patient(viruses, 9)
        self.assertEqual(test_object.get_total_pop(), len(viruses))

    def test_patient1(self):
        """Verifies Patient, Problem 1."""
        arg1 = self.test_data[0]['input'][0]
        arg2 = self.test_data[0]['input'][1]

        virus = SimpleVirus(arg1, arg2)
        patient = Patient([virus], 100)

        for _ in range(100):
            patient.update()

        self.assertEqual(patient.get_total_pop() >= 100, True)

    def test_patient2(self):
        """Verifies Patient, Problem 1."""
        arg1 = self.test_data[1]['input'][0]
        arg2 = self.test_data[1]['input'][1]

        virus = SimpleVirus(arg1, arg2)
        patient = Patient([virus], 100)

        for _ in range(100):
            patient.update()

        self.assertEqual(patient.get_total_pop() == 0, True)

    def test_patient_random(self):
        """Verifies Patient, Problem 1."""
        viruses = []
        for _ in range(random.randint(1, 5)):
            arg1 = random.randint(0, 100) / 100
            arg2 = random.randint(0, 100) / 100
            viruses.append(SimpleVirus(arg1, arg2))

        patient = Patient(viruses, 6)
        self.assertEqual(patient.get_total_pop(), len(viruses))

        for _ in range(10):
            self.assertEqual(len(patient.viruses) < patient.max_pop, True)
