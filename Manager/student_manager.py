import random
from Domain.student import Student
from Domain.student_validator import StudentValidator
from Repository.students_repository import StudentRepo
from Repository.grades_repository import GradeRepo


class StudentManager:

    def __init__(self,
                 student_validator: StudentValidator,
                 student_repository: StudentRepo,
                 grades_repository: GradeRepo):
        self.__student_validator = student_validator
        self.__student_repo = student_repository
        self.__grades_repository = grades_repository

    def add_student(self, new_id: int, new_name: str, new_group: int) -> None:
        """
        Adds a student to the list __students_list
        :param new_id: Student ID
        :param new_name: Student name
        :param new_group: Student group
        :return: None
        """
        student = Student(new_id, new_name, new_group)
        self.__student_validator.validate_student(student)
        self.__student_repo.store(student)

    def remove_student(self, searched_id):
        """
        Removes a student from the repository and associated grades.
        :param searched_id: Student ID
        :return: None
        """
        self.__student_repo.delete(searched_id)
        self.__grades_repository.remove_if_remove_student(searched_id)

    def does_exist_student(self, searched_id):
        """
        Checks if a student with the given ID exists.
        :param searched_id: Student ID
        :return: True if found, False otherwise
        """
        if self.__student_repo.find(searched_id):
            return True
        return False

    def modify_student_id(self, searched_id, new_id):
        """
        Modifies the ID of a specific student.
        :param searched_id: Current student ID
        :param new_id: New student ID
        :return: None
        """
        students_list = self.__student_repo.get_students_list_repo()
        for i in range(len(students_list)):
            if students_list[i].get_ID() == searched_id:
                student = students_list[i]
                student.set_ID(new_id)
                self.__student_validator.validate_student(student)
                self.__student_repo.modify(searched_id, student)
                break

    def modify_student_name(self, searched_id, new_name):
        """
        Modifies the name of a specific student.
        :param searched_id: Current student ID
        :param new_name: New student name
        :return: None
        """
        students_list = self.__student_repo.get_students_list_repo()
        for i in range(len(students_list)):
            if students_list[i].get_ID() == searched_id:
                students_list[i].set_name(new_name)
                self.__student_validator.validate_student(students_list[i])
                self.__student_repo.modify(searched_id, students_list[i])
                break

    def modify_student_group(self, searched_id, new_group):
        """
        Modifies the group of a specific student.
        :param searched_id: Current student ID
        :param new_group: New student group
        :return: None
        """
        students_list = self.__student_repo.get_students_list_repo()
        for i in range(len(students_list)):
            if students_list[i].get_ID() == searched_id:
                students_list[i].set_group(new_group)
                self.__student_validator.validate_student(students_list[i])
                self.__student_repo.modify(searched_id, students_list[i])
                break

    def get_student_manager(self, student_id: int) -> Student | None:
        """
        Retrieves a specific student from the repository.
        :param student_id: Student ID
        :return: The student object or None if not found
        """
        return self.__student_repo.find(student_id)

    def get_students_list_manager(self):
        """
        Retrieves the list of all students from the repository.
        :return: List of students
        """
        return self.__student_repo.get_students_list_repo()

    def generate_students(self, count):
        """
        Generates a specified number of random students.
        :param count: Number of students to generate
        :return: None
        """
        for i in range(count):
            id_student = random.randint(100, 999)
            name = random.choice([
                'Mara', 'George', 'Stefania', 'Diana', 'Cristi', 'Georgiana', 'Sergiu', 'Horia', 'Andrei',
                'Alex', 'Bianca', 'Daniel', 'Elena', 'Florin', 'Gabriela', 'Ion', 'Laura', 'Mihai', 'Nicoleta',
                'Ovidiu', 'Paula', 'Radu', 'Simona', 'Teodor', 'Vlad'])
            group = random.randint(1, 9)
            self.add_student(id_student, name, group)

    def recursive_generate_students(self, count):
        """
        Recursively generates a specified number of random students.
        :param count: Number of students to generate
        :return: None
        """
        if count == 0:
            return
        id_student = random.randint(100, 999)
        name = random.choice([
            'Mara', 'George', 'Stefania', 'Diana', 'Cristi', 'Georgiana', 'Sergiu', 'Horia', 'Andrei',
            'Alex', 'Bianca', 'Daniel', 'Elena', 'Florin', 'Gabriela', 'Ion', 'Laura', 'Mihai', 'Nicoleta',
            'Ovidiu', 'Paula', 'Radu', 'Simona', 'Teodor', 'Vlad'])
        group = random.randint(1, 9)
        self.add_student(id_student, name, group)
        self.recursive_generate_students(count - 1)