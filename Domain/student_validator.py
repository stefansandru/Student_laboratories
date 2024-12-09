from Domain.student import Student
from Exceptions.exceptions import ValidationException


class StudentValidator:
    def __init__(self):
        pass

    def validate_student(self, student: Student):
        """
        Validates a given task
        :param student: The student to be validated
        :return: -
        :raises: ValueError if the student is not valid
        """
        errors = []

        if student.get_ID() < 100 or student.get_ID() > 999:
            errors.append('ID-ul trebuie sa contina 3 cifre.')

        if len(student.get_name()) < 3:
            errors.append('Numele trebuie sa contina cel putin 3 caractere.')

        if student.get_group() < 0 or student.get_group() > 9:
            errors.append('Grupul trebuie sa contina o singura cifra.')

        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValidationException(error_string)
