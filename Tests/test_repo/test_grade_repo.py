import unittest
from utils.file_utils import copy_file, clear_file
from Repository.grades_repository import GradeRepo, Asign, AssignmentAlreadyExistsException


class TestGradeRepo(unittest.TestCase):

    def setUp(self):
        clear_file('t_grades.txt')
        copy_file("def_grades.txt", "t_grades.txt")
        self.__repo = GradeRepo("t_grades.txt")

    def test_add_grade(self):
        self.__repo.store(Asign(205, 6, 10, 9))
        self.assertEqual(self.__repo.size(), 13)
        self.assertRaises(AssignmentAlreadyExistsException, self.__repo.store,
                          Asign(345, 6, 10, 3))

    def test_size(self):
        self.assertEqual(self.__repo.size(), len(self.__repo.get_asign_list_repo()))

    def test_find_grade(self):
        self.assertEqual(self.__repo.find_asigment(345, 6, 10),
                         Asign(345, 6, 10, 6))
        self.assertEqual(self.__repo.find_asigment(111, 1, 1), None)
