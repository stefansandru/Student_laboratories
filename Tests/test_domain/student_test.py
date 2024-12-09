import unittest
from Domain.student import Student
from Domain.student_validator import StudentValidator
from Exceptions.exceptions import ValidationException

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.stundent_validator = StudentValidator()

    def test_crete_stundet(self):
        student = Student(678, "Andrei", 4)
        self.assertEqual(student.get_ID(), 678)
        self.assertEqual(student.get_name(), "Andrei")
        self.assertEqual(student.get_group(), 4)

    def test_set_student(self):
        student = Student(678, "Andrei", 4)
        student.set_ID(123)
        student.set_name("Ion")
        student.set_group(1)
        self.assertEqual(student.get_ID(), 123)
        self.assertEqual(student.get_name(), "Ion")
        self.assertEqual(student.get_group(), 1)

    def test_equal_students(self):
        student = Student(678, "Andrei", 4)
        student2 = Student(678, "Andrei", 4)
        self.assertEqual(student, student2)

        student3 = Student(671, "Andrei", 7)
        self.assertNotEqual(student, student3)

    def test_student_validator(self):
        student = Student(648, "Andrei", 5)
        student_not_valid = Student(324, "sf", 3346)
        self.stundent_validator.validate_student(student)
        self.assertRaises(ValidationException, self.stundent_validator.validate_student, student_not_valid)
