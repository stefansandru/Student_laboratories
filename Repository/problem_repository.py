from Domain.problem import Problem
from typing import List
from Exceptions.exceptions import CoruptedFileException, ProblemAlreadyExistsException, ProblemDoesNotExistException


class ProblemRepo:

    def __init__(self, file_path: str):
        self.__file_path = file_path

    def __read_file(self):
        """
        Reads from the file and returns a list of problems.
        :return: List of problems
        """
        try:
            f = open(self.__file_path, 'r')
        except IOError:
            raise CoruptedFileException
        all_problems = []
        lines = f.readlines()
        for line in lines:
            lab, prob, deadline, description = [token.strip() for token in line.split(';')]
            lab = int(lab)
            prob = int(prob)
            deadline = int(deadline)
            problem = Problem(lab, prob, deadline, description)
            all_problems.append(problem)
        f.close()
        return all_problems

    def __write_file(self, problems: List[Problem]):
        """
        Writes to the file.
        """
        with open(self.__file_path, 'w') as f:
            for problem in problems:
                problem_string = str(problem.get_lab_nr()) + '; ' + str(problem.get_problem_nr()) + '; ' + \
                                 str(problem.get_deadline()) + '; ' + str(problem.get_description()) + "\n"
                f.write(problem_string)

    def find(self, lab_number: int, problem_number: int) -> Problem | None:
        """
        Searches for the problem with the given number in the given lab.
        :param lab_number: Lab number
        :param problem_number: Problem number
        :return: Problem if found, None otherwise
        """
        all_problems = self.__read_file()
        for problem in all_problems:
            if lab_number == problem.get_lab_nr() and problem_number == problem.get_problem_nr():
                return problem
        return None

    def size(self):
        """
        Returns the number of problems.
        """
        return len(self.__read_file())

    def store(self, lab_nr: int, problem_nr: int, problem: Problem):
        """
        Adds a new problem if it does not already exist.
        :param lab_nr: Lab number
        :param problem_nr: Problem number
        :param problem: Problem to be added
        :return: None
        """
        problems = self.__read_file()
        if problem == self.find(lab_nr, problem_nr):
            raise ProblemAlreadyExistsException
        problems.append(problem)
        self.__write_file(problems)

    def delete(self, lab_nr: int, problem_nr: int):
        """
        Deletes the problem with the specified number from the specified lab.
        :param lab_nr: Lab number
        :param problem_nr: Problem number
        :return: Problem to be removed
        """
        problems = self.__read_file()
        problem_to_remove = self.find(lab_nr, problem_nr)
        if problem_to_remove is None:
            raise ProblemDoesNotExistException
        problems.remove(problem_to_remove)
        self.__write_file(problems)
        return problem_to_remove

    def modify(self, lab_nr: int, problem_nr: int, modified_problem: Problem):
        """
        Searches for the problem with the specified number in the specified lab
        and replaces it with the modified problem.
        :param lab_nr: Lab number
        :param problem_nr: Problem number
        :param modified_problem: Modified problem
        :return: Modified problem
        """
        problems = self.__read_file()
        for i in range(self.size()):
            if problems[i].get_lab_nr() == lab_nr and problems[i].get_problem_nr() == problem_nr:
                problems[i] = modified_problem
                break
        self.__write_file(problems)
        return modified_problem

    def get_problem_list_repo(self):
        """
        Returns the list of problems.
        """
        return self.__read_file()