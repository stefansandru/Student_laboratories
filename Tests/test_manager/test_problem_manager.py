import unittest
from Manager.problem_manager import ProblemManager
from utils.file_utils import clear_file, copy_file
from Domain.problem_validator import ProblemValidator
from Repository.problem_repository import ProblemRepo
from Repository.grades_repository import GradeRepo
from Exceptions.exceptions import ValidationException, ProblemAlreadyExistsException, ProblemDoesNotExistException


class TestProblemManager(unittest.TestCase):
    def setUp(self):
        clear_file("test_problems.txt")
        copy_file("default_problems.txt", "test_problems.txt")

        validator = ProblemValidator()
        problem_repo = ProblemRepo("test_problems.txt")
        grade_repo = GradeRepo("test_grades.txt")
        self.__problem_manager = ProblemManager(validator, problem_repo, grade_repo)

    def test_does_exist(self):
        self.assertTrue(self.__problem_manager.does_exist_problem(7, 1))
        self.assertFalse(self.__problem_manager.does_exist_problem(1, 1))

    def test_add_problem(self):
        self.__problem_manager.add_problem(1, 1, 11, "test_problem")
        self.assertEqual(len(self.__problem_manager.get_problem_list_manager()), 8)
        self.assertRaises(ValidationException, self.__problem_manager.add_problem, 15, 2, 11, "test_problem")
        self.assertRaises(ValidationException, self.__problem_manager.add_problem, 1, 11, 11, "test_problem")
        self.assertRaises(ValidationException, self.__problem_manager.add_problem, 2, 3, 32, "test_problem")
        self.assertRaises(ValidationException, self.__problem_manager.add_problem, 2, 2, 31, "sa")
        self.assertRaises(ProblemAlreadyExistsException, self.__problem_manager.add_problem, 8, 7, 28, "cutii")

    def test_delete_problem(self):
        self.__problem_manager.delete_problem(8, 7)
        self.assertEqual(len(self.__problem_manager.get_problem_list_manager()), 6)
        self.assertRaises(ProblemDoesNotExistException, self.__problem_manager.delete_problem, 2, 2)

    def test_modify_problem_lab(self):
        previous = self.__problem_manager.get_problem_manager(8, 7)
        self.__problem_manager.modify_lab_number(8, 7, 1)
        new = self.__problem_manager.get_problem_manager(1, 7)
        self.assertNotEqual(previous.get_lab_nr(), new.get_lab_nr())
        self.assertEqual(previous.get_problem_nr(), new.get_problem_nr())
        self.assertEqual(previous.get_deadline(), new.get_deadline())
        self.assertEqual(previous.get_description(), new.get_description())
        self.assertRaises(ValidationException, self.__problem_manager.modify_lab_number, 6, 10, 15)

    def test_mofdify_problem_number(self):
        previous = self.__problem_manager.get_problem_manager(8, 7)
        self.__problem_manager.modify_problem_number(8, 7, 2)
        new = self.__problem_manager.get_problem_manager(8, 2)
        self.assertEqual(previous.get_lab_nr(), new.get_lab_nr())
        self.assertNotEqual(previous.get_problem_nr(), new.get_problem_nr())
        self.assertEqual(previous.get_deadline(), new.get_deadline())
        self.assertEqual(previous.get_description(), new.get_description())
        self.assertRaises(ValidationException, self.__problem_manager.modify_problem_number, 6, 10, 11)

    def test_modify_deadline(self):
        previous = self.__problem_manager.get_problem_manager(8, 7)
        self.__problem_manager.modify_deadline(8, 7, 11)
        new = self.__problem_manager.get_problem_manager(8, 7)
        self.assertEqual(previous, new)
        self.assertNotEqual(previous.get_deadline(), new.get_deadline())
        self.assertEqual(previous.get_description(), new.get_description())
        self.assertRaises(ValidationException, self.__problem_manager.modify_deadline, 6, 10, 32)

    def test_modify_descriere(self):
        previous = self.__problem_manager.get_problem_manager(8, 7)
        self.__problem_manager.modify_description(8, 7, "Test Description")
        new = self.__problem_manager.get_problem_manager(8, 7)
        self.assertEqual(previous, new)
        self.assertEqual(previous.get_deadline(), new.get_deadline())
        self.assertNotEqual(previous.get_description(), new.get_description())
        self.assertRaises(ValidationException, self.__problem_manager.modify_description, 6, 10, "nu")

    def test_generate_problems(self):
        previous_len = len(self.__problem_manager.get_problem_list_manager())
        self.__problem_manager.generate_problems(4)
        new_len = len(self.__problem_manager.get_problem_list_manager())
        difference = new_len - previous_len
        self.assertEqual(difference, 4)
