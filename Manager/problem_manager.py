from Domain.problem import Problem
from Domain.problem_validator import ProblemValidator, ValidationException
from Repository.problem_repository import ProblemRepo
from Repository.grades_repository import GradeRepo
import random


class ProblemManager:

    def __init__(self, problem_validator: ProblemValidator, problem_repo: ProblemRepo, grade_repo: GradeRepo):
        self.__problem_validator = problem_validator
        self.__problem_repo = problem_repo
        self.__grade_repo = grade_repo

    def does_exist_problem(self, lab_nr: int, problem_nr: int):
        """
        Searches for a problem with the given number that is part of a specific lab.
        :param lab_nr: Lab number
        :param problem_nr: Problem number
        :return: True if found, False otherwise
        """
        problems = self.__problem_repo.get_problem_list_repo()
        for problem in problems:
            if problem.get_lab_nr() == lab_nr and problem.get_problem_nr() == problem_nr:
                return True
        return False

    def add_problem(self, lab, prob, deadline, description) -> None:
        """
        Adds a new problem to the list of problems.
        :param lab: The lab number the problem belongs to
        :param prob: The problem number
        :param deadline: The last day the problem can be submitted
        :param description: The description of the problem
        :return: None
        """
        problem = Problem(lab, prob, deadline, description)
        self.__problem_validator.validate_problem(problem)
        self.__problem_repo.store(lab, prob, problem)

    def delete_problem(self, lab_nr: int, prob_nr: int):
        """
        Deletes a problem from the repository and removes associated grades.
        :param lab_nr: Lab number
        :param prob_nr: Problem number
        :return: None
        """
        self.__problem_repo.delete(lab_nr, prob_nr)
        self.__grade_repo.remove_if_remove_problem(lab_nr, prob_nr)

    def modify_lab_number(self, lab_nr, problem_nr, new_lab_nr):
        """
        Modifies the lab number of a specific problem.
        :param lab_nr: Current lab number
        :param problem_nr: Current problem number
        :param new_lab_nr: New lab number
        :return: None
        """
        problems_list = self.__problem_repo.get_problem_list_repo()
        for problem in problems_list:
            if problem.get_lab_nr() == lab_nr and problem.get_problem_nr() == problem_nr:
                problem.set_lab_nr(new_lab_nr)
                self.__problem_validator.validate_problem(problem)
                self.__problem_repo.modify(lab_nr, problem_nr, problem)
                break

    def modify_problem_number(self, lab_nr, problem_nr, new_problem_nr):
        """
        Modifies the problem number of a specific problem.
        :param lab_nr: Current lab number
        :param problem_nr: Current problem number
        :param new_problem_nr: New problem number
        :return: None
        """
        problems_list = self.__problem_repo.get_problem_list_repo()
        for problem in problems_list:
            if problem.get_lab_nr() == lab_nr and problem.get_problem_nr() == problem_nr:
                problem.set_problem_nr(new_problem_nr)
                self.__problem_validator.validate_problem(problem)
                self.__problem_repo.modify(lab_nr, problem_nr, problem)
                break

    def modify_deadline(self, lab_nr, problem_nr, new_deadline):
        """
        Modifies the deadline of a specific problem.
        :param lab_nr: Current lab number
        :param problem_nr: Current problem number
        :param new_deadline: New deadline
        :return: None
        """
        problems_list = self.__problem_repo.get_problem_list_repo()
        for problem in problems_list:
            if problem.get_lab_nr() == lab_nr and problem.get_problem_nr() == problem_nr:
                problem.set_deadline(new_deadline)
                self.__problem_validator.validate_problem(problem)
                self.__problem_repo.modify(lab_nr, problem_nr, problem)
                break

    def modify_description(self, lab_nr, problem_nr, new_description):
        """
        Modifies the description of a specific problem.
        :param lab_nr: Current lab number
        :param problem_nr: Current problem number
        :param new_description: New description
        :return: None
        """
        problems_list = self.__problem_repo.get_problem_list_repo()
        for problem in problems_list:
            if problem.get_lab_nr() == lab_nr and problem.get_problem_nr() == problem_nr:
                problem.set_description(new_description)
                self.__problem_validator.validate_problem(problem)
                self.__problem_repo.modify(lab_nr, problem_nr, problem)
                break

    def get_problem_manager(self, lab_nr: int, problem_nr: int):
        """
        Retrieves a specific problem from the repository.
        :param lab_nr: Lab number
        :param problem_nr: Problem number
        :return: The problem object
        """
        return self.__problem_repo.find(lab_nr, problem_nr)

    def get_problem_list_manager(self):
        """
        Retrieves the list of all problems from the repository.
        :return: List of problems
        """
        return self.__problem_repo.get_problem_list_repo()

    def generate_problems(self, count):
        """
        Generates a specified number of random problems.
        :param count: Number of problems to generate
        :return: None
        """
        while count:
            lab = random.randint(1, 14)
            problem = random.randint(1, 10)
            deadline = random.randint(1, 31)
            descriere = random.choice(
                ['match', 'ladder', 'analysis', 'scaling theorem', 'branches in trees',
                'wave height', 'electromagnetic waves', 'watt', 'quantum mechanics',
                'data structures', 'algorithm design', 'network protocols', 'database management',
                'operating systems', 'machine learning', 'artificial intelligence', 'cryptography',
                'software engineering', 'computer graphics', 'human-computer interaction'])
            try:
                self.add_problem(lab, problem, deadline, descriere)
                count -= 1
            except ValidationException:
                continue