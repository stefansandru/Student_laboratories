from Domain.student import Student
from Exceptions.exceptions import CoruptedFileException, StudentDoesNotExistException, StudentAlreadyExistsException

class StudentRepo:
    def __init__(self, file_path: str) -> None:
        """
        Initializes the StudentRepo with the given file path.
        :param file_path: The path to the file where student data is stored
        """
        self.__file_path = file_path

    def __load_from_file(self):
        """
        Loads the student data from the file.
        :return: A list of students from the file
        :rtype: list of Students
        """
        try:
            f = open(self.__file_path, 'r')
        except IOError:
            raise CoruptedFileException

        students = []
        lines = f.readlines()
        for line in lines:
            student_id, student_name, student_group = [token.strip() for token in line.split(';')]
            student_id = int(student_id)
            student_group = int(student_group)
            a = Student(student_id, student_name, student_group)
            students.append(a)
        f.close()
        return students

    def __save_to_file(self, students_list):
        """
        Saves the given list of students to the file.
        :param students_list: The list of students to save
        :type students_list: list of Students
        :return: None
        """
        with open(self.__file_path, 'w') as f:
            for student in students_list:
                student_string = str(student.get_ID()) + '; ' + str(student.get_name()) + '; ' + str(student.get_group()) + '\n'
                f.write(student_string)

    def store(self, student):
        """
        Saves a student to the file.
        :param student: The student to add
        :return: None
        """
        all_students = self.__load_from_file()
        if student in all_students:
            raise StudentAlreadyExistsException
        all_students.append(student)
        self.__save_to_file(all_students)

    def find(self, stud_id) -> Student | None:
        """
        Searches for a student by ID.
        :param stud_id: The ID of the student to search for
        :return: The student if found, otherwise None
        """
        all_students = self.__load_from_file()
        for student in all_students:
            if student.get_ID() == stud_id:
                return student
        return None

    def delete(self, student_id):
        """
        Deletes a student by ID.
        :param student_id: The ID of the student to delete
        :return: The deleted student
        """
        all_students = self.__load_from_file()
        student = self.find(student_id)
        if student is None:
            raise StudentDoesNotExistException
        all_students.remove(student)
        self.__save_to_file(all_students)
        return student

    def modify(self, searched_id: int, modified_stud: Student):
        """
        Modifies a student by ID.
        :param searched_id: The ID of the student to modify
        :type searched_id: int
        :param modified_stud: The student with the modifications
        :type modified_stud: Student
        :return: The modified student
        """
        all_students = self.__load_from_file()
        for index in range(self.size()):
            if all_students[index].get_ID() == searched_id:
                all_students[index] = modified_stud
        self.__save_to_file(all_students)
        return modified_stud

    def get_students_list_repo(self) -> list:
        """
        Returns the entire list of students.
        :return: The list of students
        :rtype: list of Students
        """
        return self.__load_from_file()

    def size(self):
        """
        Returns the number of students.
        :return: The number of students
        :rtype: int
        """
        return len(self.__load_from_file())