import unittest

from Domain.student import Student
from Repository.students_repository import StudentRepo, StudentAlreadyExistsException, StudentDoesNotExistException
from utils.file_utils import copy_file, clear_file


class TestStudentRepo(unittest.TestCase):

    def setUp(self):
        clear_file("t_stud.txt")
        copy_file("def_stud.txt", "t_stud.txt")
        self.__repo = StudentRepo("t_stud.txt")

    def test_store_student(self):
        student = Student(111, "asd", 1)
        self.__repo.store(student)
        self.assertEqual(len(self.__repo.get_students_list_repo()), 9)
        existent_student = Student(345, "asd", 1)
        self.assertRaises(StudentAlreadyExistsException, self.__repo.store, existent_student)

    def test_find_student(self):
        f_student = self.__repo.find(345)
        self.assertEqual(f_student, Student(345, "Popescu", 2))
        not_f_student = self.__repo.find(111)
        self.assertEqual(not_f_student, None)

    def test_delete_student(self):
        self.__repo.delete(345)
        self.assertEqual(len(self.__repo.get_students_list_repo()), 7)
        self.assertRaises(StudentDoesNotExistException, self.__repo.delete, 111)

    def test_modify_student(self):
        self.__repo.modify(345, Student(345, "asd", 2))
        self.assertEqual(len(self.__repo.get_students_list_repo()), 8)
        self.assertEqual(self.__repo.find(345), Student(345, "asd", 2))

    def test_size(self):
        self.assertEqual(len(self.__repo.get_students_list_repo()), self.__repo.size())
