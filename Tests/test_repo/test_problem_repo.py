import unittest
from utils.file_utils import copy_file, clear_file
from Repository.problem_repository import (ProblemRepo,
                                           Problem,
                                           ProblemDoesNotExistException,
                                           ProblemAlreadyExistsException)


class TestProblemRepo(unittest.TestCase):

    def setUp(self):
        clear_file("t_prob.txt")
        copy_file("def_prob.txt", "t_prob.txt")
        self.__repo = ProblemRepo("t_prob.txt")

    def test_store_problem(self):
        self.__repo.store(1, 1, Problem(1, 1, 11, "asd"))
        self.assertEqual(self.__repo.size(), 8)
        self.assertRaises(ProblemAlreadyExistsException, self.__repo.store, 6, 10,
                          Problem(6, 10, 7, "numere prime"))

    def test_delete_problem(self):
        self.__repo.delete(6, 10)
        self.assertEqual(self.__repo.size(), 6)
        self.assertRaises(ProblemDoesNotExistException, self.__repo.delete, 10, 10)

    def test_modify_problem(self):
        self.__repo.modify(6, 10,
                           Problem(6, 10, 7, "asd"))
        self.assertEqual(self.__repo.size(), 7)
        self.assertEqual(self.__repo.find(6, 10),
                         Problem(6, 10, 7, "asd"))

    def test_find(self):
        self.assertEqual(self.__repo.find(6, 10),
                         Problem(6, 10, 7, "numere prime"))
        self.assertEqual(self.__repo.find(10, 10), None)

    def test_size(self):
        self.assertEqual(self.__repo.size(), len(self.__repo.get_problem_list_repo()))