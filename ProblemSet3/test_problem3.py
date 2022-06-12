# Problem Set 3, Part B, Problem 3

import unittest

from ProblemSet3 import ResistantVirus, NoChildException

class TestSimpleVirus(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            # Create a ResistantVirus that is never cleared and always reproduces.
            0: {'input': [1.00, 0.00, {}, 0.00], 'output': [False, False]},

            # Create a ResistantVirus that is never cleared and never reproduces.
            1: {'input': [0.00, 0.00, {}, 0.00], 'output': [True, False]},

            # Create a ResistantVirus that is always cleared and always reproduces.
            2: {'input': [1.00, 1.00, {}, 0.00], 'output': [False, True]},

            # Create a ResistantVirus that is always cleared and never reproduces.
            3: {'input': [0.00, 1.00, {}, 0.00], 'output': [True, True]},

        }

    def test_resistiveVirus(self):
        for i in self.test_data.keys():
            arg1 = self.test_data[i]['input'][0]
            arg2 = self.test_data[i]['input'][1]
            arg3 = self.test_data[i]['input'][2]
            arg4 = self.test_data[i]['input'][3]
            virus = ResistantVirus(arg1, arg2, arg3, arg4)

            shall_raise     = self.test_data[i]['output'][0]
            expected_result = self.test_data[i]['output'][1]

            if shall_raise:
                self.assertRaises(NoChildException, virus.reproduce, 0, [])
            else:
                self.assertEqual(type(virus.reproduce(0, [])) , type(virus))                

            self.assertEqual(virus.doesClear(), expected_result)

    def test_virus_resistances(self):
        arg1 = 1.0
        arg2 = 0.0
        arg3 = {"drug1": True, "drug2": False}
        arg4 = 0.0
        virus = ResistantVirus(arg1, arg2, arg3, arg4)

        self.assertRaises(NoChildException, virus.reproduce, 0, ['drug2'])
        self.assertEqual(type(virus.reproduce(0, ["drug1"])) == type(virus), True)
                  
    def test_virus_mutProb(self):
        arg1 = 1.0
        arg2 = 0.0
        arg3 = {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}
        arg4 = 0.5
        virus = ResistantVirus(arg1, arg2, arg3, arg4)

        for i in range(10):
           child = virus.reproduce(0, [])
           for drug in arg3.keys():
               self.assertEqual(child.isResistantTo(drug), arg3[drug])

    def test_positive_mutability(self):
        arg1 = 1.0
        arg2 = 0.0
        arg3 = {'drug2': True}
        arg4 = 1.0
        virus = ResistantVirus(arg1, arg2, arg3, arg4)

        for i in range(100):
           child = virus.reproduce(0, [])
           for drug in arg3.keys():
               self.assertEqual(child.isResistantTo(drug), arg3[drug])

    def test_negative_mutability(self):
        arg1 = 1.0
        arg2 = 0.0
        arg3 = {'drug2': True}
        arg4 = 0.0
        virus = ResistantVirus(arg1, arg2, arg3, arg4)

        for i in range(100):
            child = virus.reproduce(0, [])
            for drug in arg3.keys():
                self.assertEqual(child.isResistantTo(drug), arg3[drug])

    def test_virus_reproduction_with_drugs_applied(self):
        arg1 = 0.0
        arg2 = 0.0
        arg3 = {"drug1":True, "drug2":False}
        arg4 = 0.0
        virus = ResistantVirus(arg1, arg2, arg3, arg4)

        self.assertRaises(NoChildException, virus.reproduce, 0, ['drug2'])
        self.assertRaises(NoChildException, virus.reproduce, 0, ['drug1'])