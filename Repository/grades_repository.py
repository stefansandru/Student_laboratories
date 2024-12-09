from Domain.asign import Asign
from typing import List
from Exceptions.exceptions import CoruptedFileException, AssignmentAlreadyExistsException


class GradeRepo:

    def __init__(self, file_path: str):
        self.__file_path = file_path

    def __read_file(self):
        try:
            f = open(file=self.__file_path, mode='r')
        except IOError:
            raise CoruptedFileException
        grades = []
        lines = f.readlines()
        for line in lines:
            stud_id, lab, problem, grade = [token.strip() for token in line.split(";")]
            asign = Asign(int(stud_id), int(lab), int(problem), int(grade))
            grades.append(asign)
        f.close()
        return grades

    def __write_file(self, grades: List[Asign]):
        with open(self.__file_path, "w") as f:
            for grade in grades:
                grade_string = str(grade.get_student_id()) + "; " + str(grade.get_lab()) + "; " + \
                               str(grade.get_problem()) + "; " + str(grade.get_grade()) + "\n"
                f.write(grade_string)

    def find_asigment(self, student_id, lab, problem) -> Asign | None:
        """
        Searches for an assignment and if found, returns that assignment.
        :param student_id: Student ID
        :param lab: Lab number
        :param problem: Problem number
        :return: Assignment if found, None otherwise
        """
        asigns = self.__read_file()
        for asign in asigns:
            if asign.get_student_id() == student_id and asign.get_lab() == lab and asign.get_problem() == problem:
                return asign
        return None

    def find_asigns_with_specified_problem(self, lab, prob) -> List[Asign] | None:
        """
        Searches for a problem and returns a list of assignments that contain the problem.
        If not found, returns None.
        :param lab: Lab number
        :param prob: Problem number
        :return: List of assignments with the specified problem or None
        """
        asigns_with_specified_problem = []
        asigns = self.__read_file()
        for asign in asigns:
            if asign.get_lab() == lab and asign.get_problem() == prob:
                asigns_with_specified_problem.append(asign)
        return asigns_with_specified_problem

    def store(self, asign):
        """
        Creates an assignment for a specific student for a specific problem.
        :param asign: The assignment to be added to the file
        :return: None
        """
        asigns = self.__read_file()
        if self.find_asigment(asign.get_student_id(), asign.get_lab(), asign.get_problem()):
            raise AssignmentAlreadyExistsException()
        asigns.append(asign)
        self.__write_file(asigns)

    def size(self):
        """
        Returns the number of assignments.
        :return: Number of assignments
        """
        asigns = self.__read_file()
        return len(asigns)

    def remove_if_remove_student(self, student_id):
        """
        Deletes all assignments of a removed student.
        :param student_id: ID of the removed student
        :return: None
        """
        asigns = self.__read_file()
        new_assignments = []
        for asign in asigns:
            if asign.get_student_id() != student_id:
                new_assignments.append(asign)
        self.__write_file(new_assignments)

    def remove_if_remove_problem(self, lab, prob):
        """
        Deletes all assignments of a removed problem.
        :param lab: Lab number of the removed problem
        :param prob: Problem number of the removed problem
        :return: None
        """
        asigns = self.__read_file()
        new_assignments = []
        for asign in asigns:
            if asign.get_lab() != lab and asign.get_problem() != prob:
                new_assignments.append(asign)
        self.__write_file(new_assignments)

    def get_asign_list_repo(self):
        """
        Retrieves the list of all assignments.
        :return: List of assignments
        """
        return self.__read_file()