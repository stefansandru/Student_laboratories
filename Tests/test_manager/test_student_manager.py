import unittest

from Manager.student_manager import StudentManager
from utils.file_utils import copy_file, clear_file

from Domain.student_validator import StudentValidator
from Repository.students_repository import StudentRepo
from Repository.grades_repository import GradeRepo
from Exceptions.exceptions import StudentDoesNotExistException, StudentAlreadyExistsException, ValidationException


class TestStudentManager(unittest.TestCase):

    def setUp(self):
        clear_file("test_students.txt")
        copy_file("default_stud.txt", "test_students.txt")

        student_repo = StudentRepo("test_students.txt")
        student_vali = StudentValidator()
        grades_repo = GradeRepo("test_grades.txt")
        self.__student_manager = StudentManager(student_vali, student_repo, grades_repo)

    def test_does_exist(self):
        self.assertTrue(self.__student_manager.does_exist_student(345))
        self.assertFalse(self.__student_manager.does_exist_student(111))

    def test_add_student(self):
        self.__student_manager.add_student(123, "Dan", 8)
        self.assertEqual(len(self.__student_manager.get_students_list_manager()), 9)
        self.assertRaises(ValidationException, self.__student_manager.add_student, 12, "n", 6)
        self.assertRaises(StudentAlreadyExistsException, self.__student_manager.add_student, 123, "Dan", 8)
        self.__student_manager.add_student(133, "Dan", 8)
        self.__student_manager.add_student(333, "Dan", 8)

    def test_remove_student(self):
        self.__student_manager.remove_student(345)
        self.assertEqual(len(self.__student_manager.get_students_list_manager()), 7)
        self.assertRaises(StudentDoesNotExistException, self.__student_manager.remove_student, 121)

    def test_modify_id(self):
        previous = self.__student_manager.get_student_manager(345)
        self.__student_manager.modify_student_id(345, 111)
        new = self.__student_manager.get_student_manager(111)
        self.assertNotEqual(previous.get_ID(), new.get_ID())
        self.assertEqual(previous.get_name(), new.get_name())
        self.assertEqual(previous.get_group(), new.get_group())
        self.assertRaises(ValidationException, self.__student_manager.modify_student_id, 567, 4444)

    def test_modify_name(self):
        previous = self.__student_manager.get_student_manager(345)  # Cu numele Popescu
        self.__student_manager.modify_student_name(345, new_name="Alex")
        new = self.__student_manager.get_student_manager(345)
        self.assertNotEqual(previous.get_name(), new.get_name())
        self.assertEqual(previous.get_ID(), new.get_ID())
        self.assertEqual(previous.get_group(), new.get_group())
        self.assertRaises(ValidationException, self.__student_manager.modify_student_name, 567, "sd")

    def test_modify_grup(self):
        previous = self.__student_manager.get_student_manager(345)  # Grupa 2
        self.__student_manager.modify_student_grup(345, 6)
        new = self.__student_manager.get_student_manager(345)
        self.assertNotEqual(previous.get_group(), new.get_group())
        self.assertEqual(previous.get_ID(), new.get_ID())
        self.assertEqual(previous.get_name(), new.get_name())
        self.assertRaises(ValidationException, self.__student_manager.modify_student_grup, 567, 34)

    def test_generate_students(self):
        previous_len = len(self.__student_manager.get_students_list_manager())
        self.__student_manager.generate_students(3)
        new_len = len(self.__student_manager.get_students_list_manager())
        difference = new_len - previous_len
        self.assertEqual(difference, 3)

    def test_recutrsive_generate_students(self):
        previous_len = len(self.__student_manager.get_students_list_manager())
        self.__student_manager.recursive_generate_students(3)
        new_len = len(self.__student_manager.get_students_list_manager())
        difference = new_len - previous_len
        self.assertEqual(difference, 3)
