"""Problem Set 3, Part B, Problem 4."""
import unittest

from ProblemSet3 import ResistantVirus, TreatedPatient


class TestTreatedPatient(unittest.TestCase):
    """Test class for TreatedPatient, Problem 4."""

    def test_treated_patient1(self):
        """Verifies TreatedPatient, Problem 4."""
        virus = ResistantVirus(1.0, 0.0, {}, 0.0)
        patient = TreatedPatient([virus], 100)

        res = []
        for _ in range(100):
            res.append(patient.update())

        mean = sum(res[90:]) / 10
        self.assertAlmostEqual(mean, 100, delta=5)

    def test_treated_patient2(self):
        """Verifies TreatedPatient, Problem 4."""
        virus = ResistantVirus(1.0, 1.0, {}, 0.0)
        patient = TreatedPatient([virus], 100)

        res = []
        for _ in range(100):
            res.append(patient.update())

        mean = sum(res[90:]) / 10
        self.assertAlmostEqual(mean, 0, delta=5)

    def test_add_prescription(self):
        """Verifies TreatedPatient, Problem 4."""
        patient = TreatedPatient([], 100)
        prescription_drugs = [
            'drugV', 'drugD', 'drugQ', 'drugE', 'drugA', 'drugH', 'drugC', 'drugU', 'drugB', 'drugF', 'drugV'
        ]
        for drug in prescription_drugs:
            patient.add_prescription(drug)

            # Test 1 - verify that drug exist in Patient
            self.assertEqual(drug in patient.get_prescriptions(), True)

        # Test 2 - verify that correct amount of drugs exist in Patient. Note, drugV is is the list twice
        self.assertEqual(len(patient.get_prescriptions()), len(prescription_drugs) - 1)

        # Test 3 - verify that dublicates are not listed
        for drug in prescription_drugs:
            patient.add_prescription(drug)
            self.assertEqual(len(patient.get_prescriptions()), len(prescription_drugs) - 1)

    def test_getting_resistant_pop(self):
        """Verifies TreatedPatient, Problem 4."""
        virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
        virus2 = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
        virus3 = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": True}, 0.0)
        patient = TreatedPatient([virus1, virus2, virus3], 100)

        self.assertEqual(patient.get_resist_pop(['drug1']), 2)
        self.assertEqual(patient.get_resist_pop(['drug2']), 2)
        self.assertEqual(patient.get_resist_pop(['drug1', 'drug2']), 1)
        self.assertEqual(patient.get_resist_pop(['drug3']), 0)
        self.assertEqual(patient.get_resist_pop(['drug1', 'drug3']), 0)
        self.assertEqual(patient.get_resist_pop(['drug1', 'drug2', 'drug3']), 0)

    def test_virus_populations(self):
        """Verifies TreatedPatient, Problem 4."""
        virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
        virus2 = ResistantVirus(1.0, 0.0, {"drug1": False}, 0.0)
        patient = TreatedPatient([virus1, virus2], 1000000)
        patient.add_prescription("drug1")
        for _ in range(5):
            result = patient.update()

        self.assertAlmostEqual(result, 2**5, delta=10)
