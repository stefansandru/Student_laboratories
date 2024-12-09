import unittest
from Domain.asign_validator import GradesValidator
from Manager.grades_manager import GradesManager
from Repository.grades_repository import GradeRepo
from Repository.problem_repository import ProblemRepo
from Repository.students_repository import StudentRepo
from Exceptions.exceptions import ProblemDoesNotExistException, StudentDoesNotExistException, ValidationException
from utils.file_utils import clear_file, copy_file


class TestGradesManager(unittest.TestCase):

    def setUp(self):
        clear_file("test_grades.txt")
        copy_file("default_grades.txt", "test_grades.txt")

        validator = GradesValidator()
        grades_repo = GradeRepo("test_grades.txt")
        students_repo = StudentRepo("default_stud.txt")
        problems_repo = ProblemRepo("default_problems.txt")
        self.__grades_manager = GradesManager(validator, grades_repo, students_repo, problems_repo)

    def test_grades_manager(self):
        self.__grades_manager.add_grade(205, 8, 4, 6)
        self.assertEqual(len(self.__grades_manager.get_grades_list_manager()), 13)
        self.assertRaises(StudentDoesNotExistException, self.__grades_manager.add_grade, 111, 8, 6, 3)
        self.assertRaises(ProblemDoesNotExistException, self.__grades_manager.add_grade, 205, 1, 1, 3)
        self.assertRaises(ValidationException, self.__grades_manager.add_grade, 345, 8, 6, 11)

    def test_for_a_problem_order_alphabetically(self):
        ordered_by_algorithm = self.__grades_manager.for_a_problem_order_alphabetically(6, 10)
        ordered = [['Ana', 9], ['Andrei Mihail', 3], ['Elena', 4], ['Popescu', 6]]
        self.assertEqual(ordered_by_algorithm, ordered)
        self.assertRaises(ProblemDoesNotExistException, self.__grades_manager.for_a_problem_order_alphabetically, 1, 1)

    def test_for_a_problem_order_by_grade(self):
        ordered_by_algorithm = self.__grades_manager.for_a_problem_order_by_grade(6, 10)
        corect = [[3, 'Andrei Mihail'], [4, 'Elena'], [6, 'Popescu'], [9, 'Ana']]
        self.assertEqual(ordered_by_algorithm, corect)
        self.assertRaises(ProblemDoesNotExistException, self.__grades_manager.for_a_problem_order_by_grade, 1, 1)

    def test_recursive_sum(self):
        self.assertEqual(self.__grades_manager.recursive_sum([1, 2, 3, 3]), 9)
        self.assertEqual(self.__grades_manager.recursive_sum([]), 0)
        self.assertEqual(self.__grades_manager.recursive_sum([5]), 5)

    def test_average_below_5(self):
        made_by_algorithm = self.__grades_manager.average_below_5()
        self.assertEqual(made_by_algorithm, [
            ['3.00', 'Andrei Mihail'],
            ['4.33', 'George'],
            ['0.00', 'Alex'],
            ['2.00', 'Andrei']])
