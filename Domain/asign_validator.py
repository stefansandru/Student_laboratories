from Domain.asign import Asign
from Exceptions.exceptions import ValidationException

class GradesValidator:

    def __init__(self):
        pass

    def validate_grades(self, asign: Asign):
        errors = []

        if asign.get_student_id() < 100 or asign.get_student_id() > 999:
            errors.append("Student ID must contain 3 digits")

        if asign.get_lab() < 1 or asign.get_lab() > 14:
            errors.append("Lab number must be between 1 and 14")

        if asign.get_problem() < 1 or asign.get_problem() > 10:
            errors.append("Problem number must be between 1 and 10")

        if asign.get_grade() < 1 or asign.get_grade() > 10:
            errors.append("Grade must be between 1 and 10")

        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValidationException(error_string)