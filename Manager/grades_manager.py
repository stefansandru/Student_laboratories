from Domain.asign import Asign
from Domain.asign_validator import GradesValidator
from Repository.grades_repository import GradeRepo
from Repository.problem_repository import ProblemRepo
from Repository.students_repository import StudentRepo
from Exceptions.exceptions import ProblemDoesNotExistException, StudentDoesNotExistException
from Manager.sortari import selection_sort, shake_sort


class GradesManager:

    def __init__(self,
                 grades_val: GradesValidator,
                 grades_repo: GradeRepo,
                 students_repo: StudentRepo,
                 problem_repo: ProblemRepo):
        self.__grades_validator = grades_val
        self.__grades_repo = grades_repo
        self.__stud_repo = students_repo
        self.__problem_repo = problem_repo

    def add_grade(self, stud_id, lab, problem, grade):
        """
        Adds a grade for a student for a specific problem in a lab.
        :param stud_id: Student ID
        :param lab: Lab number
        :param problem: Problem number
        :param grade: Grade
        :return: None
        :raises StudentDoesNotExistException: If the student does not exist
        :raises ProblemDoesNotExistException: If the problem does not exist
        """
        asign = Asign(stud_id, lab, problem, grade)
        self.__grades_validator.validate_grades(asign)

        student = self.__stud_repo.find(stud_id)
        if student is None:
            raise StudentDoesNotExistException()

        problem = self.__problem_repo.find(lab, problem)
        if problem is None:
            raise ProblemDoesNotExistException()

        self.__grades_repo.store(asign)

    def get_grades_list_manager(self):
        """
        Retrieves the list of all grades.
        :return: List of grades
        """
        return self.__grades_repo.get_asign_list_repo()

    def for_a_problem_order_alphabetically(self, lab, problem) -> list:
        """
        Searches for the specified problem, retrieves the student names and their grades,
        and sorts the list of tuples [student name, grade] alphabetically.
        :param lab: Lab number
        :param problem: Problem number
        :return: List of tuples [student name, grade] sorted alphabetically
        :raises ProblemDoesNotExistException: If the problem does not exist
        """
        asigns_list = self.__grades_repo.find_asigns_with_specified_problem(lab, problem)
        if not asigns_list:
            raise ProblemDoesNotExistException()
        students_list = self.__stud_repo.get_students_list_repo()
        name_and_grade_list = []
        for asign in asigns_list:
            for student in students_list:
                if asign.get_student_id() == student.get_ID():
                    name_and_grade_list.append([student.get_name(), asign.get_grade()])
        sorted_list = shake_sort(name_and_grade_list, key=lambda x: x[0])
        return sorted_list

    def for_a_problem_order_by_grade(self, lab, problem) -> list:
        """
        Returns a list of all students and their average grade for a specific problem,
        sorted in ascending order by grade.
        :param lab: Lab number
        :param problem: Problem number
        :return: List of tuples (grade, student name) sorted by grade
        :raises ProblemDoesNotExistException: If the problem does not exist
        """
        asigns_list = self.__grades_repo.find_asigns_with_specified_problem(lab, problem)
        if not asigns_list:
            raise ProblemDoesNotExistException()
        students_list = self.__stud_repo.get_students_list_repo()
        name_and_grade_list = []
        for asign in asigns_list:
            for student in students_list:
                if asign.get_student_id() == student.get_ID():
                    name_and_grade_list.append([asign.get_grade(), student.get_name()])
        sorted_list = selection_sort(name_and_grade_list, key=lambda x: x[0])
        return sorted_list

    def recursive_sum(self, grades_list: list[int]) -> float:
        """
        Calculates the sum of grades in the given list.
        :param grades_list: List of grades
        :return: Sum of grades
        """
        if not grades_list:
            return 0
        return grades_list[0] + self.recursive_sum(grades_list[1:])

    def average_below_5(self) -> list:
        """
        Calculates the average grade of each student and adds them to the list
        if their average is below 5.
        :return: List of students with an average grade below 5
        """
        average_list_under_5 = []
        for student in self.__stud_repo.get_students_list_repo():
            grades_list = []
            for asign in self.__grades_repo.get_asign_list_repo():
                if student.get_ID() == asign.get_student_id():
                    grades_list.append(asign.get_grade())
            if not grades_list:
                average = 0
            else:
                average = self.recursive_sum(grades_list) / len(grades_list)
            if average < 5:
                average = "{:.2f}".format(average)
                average_list_under_5.append([average, student.get_name()])
        return average_list_under_5