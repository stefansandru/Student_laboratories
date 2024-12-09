import unittest
from Domain.problem import Problem
from Domain.problem_validator import ProblemValidator
from Exceptions.exceptions import ValidationException

class ProblemTest(unittest.TestCase):

    def setUp(self):
        self.problem_validator = ProblemValidator()

    def test_create_problem(self):
        problem = Problem(4, 6, 12, "numere prime")
        self.assertEqual(problem.get_lab_nr(), 4)
        self.assertEqual(problem.get_problem_nr(), 6)
        self.assertEqual(problem.get_deadline(), 12)
        self.assertEqual(problem.get_description(), "numere prime")

    def test_set_problem(self):
        problem = Problem(4, 6, 12, "numere prime")
        problem.set_lab_nr(6)
        problem.set_problem_nr(9)
        problem.set_deadline(24)
        problem.set_description("minge")
        self.assertEqual(problem.get_lab_nr(), 6)
        self.assertEqual(problem.get_problem_nr(), 9)
        self.assertEqual(problem.get_deadline(), 24)
        self.assertEqual(problem.get_description(), "minge")

    def test_problem_eq(self):
        problem = Problem(4, 6, 12, "numere")
        problem2 = Problem(4, 6, 12, "numere")
        self.assertEqual(problem, problem2)
        problem3 = Problem(4, 2, 12, "altceva")
        self.assertNotEqual(problem, problem3)

    def test_problem_validator(self):
        problem = Problem(4, 6, 12, "numere")
        self.problem_validator.validate_problem(problem=problem)
        not_valid_problem = Problem(54, 6, 66, "")
        self.assertRaises(ValidationException, self.problem_validator.validate_problem, not_valid_problem)
