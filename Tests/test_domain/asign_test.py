import unittest
from Domain.asign import Asign
from Domain.asign_validator import GradesValidator
from Exceptions.exceptions import ValidationException


class AsignTest(unittest.TestCase):

    def setUp(self):
        self.asign_validator = GradesValidator()

    def test_create_asign(self):
        asign = Asign(345, 5, 6, 7)
        self.assertEqual(asign.get_student_id(), 345)
        self.assertEqual(asign.get_lab(), 5)
        self.assertEqual(asign.get_problem(), 6)
        self.assertEqual(asign.get_grade(), 7)

    def test_set_asign(self):
        asign = Asign(345, 5, 6, 7)
        asign.set_studnet_id(123)
        asign.set_lab(9)
        asign.set_problem(8)
        asign.set_grade(2)
        self.assertEqual(asign.get_student_id(), 123)
        self.assertEqual(asign.get_lab(), 9)
        self.assertEqual(asign.get_problem(), 8)
        self.assertEqual(asign.get_grade(), 2)

    def test_equal_asign(self):
        asign = Asign(345, 5, 6, 7)
        asign2 = Asign(345, 5, 6, 7)
        self.assertEqual(asign, asign2)
        asign3 = Asign(345, 5, 7, 6)
        self.assertNotEqual(asign, asign3)

    def test_asign_validator(self):
        asign = Asign(345, 5, 6, 7)
        self.asign_validator.validate_grades(asign)
        not_valid_asign = Asign(12, 44, 34, 12)
        self.assertRaises(ValidationException, self.asign_validator.validate_grades, not_valid_asign)
