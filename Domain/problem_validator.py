from Domain.problem import Problem
from Exceptions.exceptions import ValidationException


class ProblemValidator:

    def __init__(self):
        pass

    def validate_problem(self, problem: Problem):
        """
        Validates a given task
        :param problem: the problem to be validated
        :return: -
        :raises: ValueError if the problem is not valid
        """
        errors = []

        if problem.get_lab_nr() > 14 or problem.get_lab_nr() < 1:
            errors.append('Numarul laboratorului trebuie sa fie de la 1 la 14.')

        if problem.get_problem_nr() > 10 or problem.get_problem_nr() < 1:
            errors.append('Numarul prblemei trnuie sa fie de la 1 la 10')

        if len(problem.get_description()) < 3:
            errors.append("Descrierea problemei trebuie sa contina mai mult de 3 caractere.")

        if problem.get_deadline() < 1 or problem.get_deadline() > 31:
            errors.append('Deadline-ul trebuie sa fie de la 1 la 31')

        if len(errors) > 0:
            error_sting = '\n'.join(errors)
            raise ValidationException(error_sting)
