class ManagementException(Exception):
    pass


class RepositoryException(ManagementException):
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return "Repository exception: " + str(self.__msg)


class StudentAlreadyExistsException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Student already exists.")


class StudentDoesNotExistException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Student does not exist.")


class ProblemAlreadyExistsException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Problem already exists.")


class ProblemDoesNotExistException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Problem does not exist.")


class AssignmentAlreadyExistsException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Assignment already exists.")


class AssignmentDoesNotExistException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Assignment does not exist.")


class ValidationException(ManagementException):
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return "Validation exception: " + str(self.__msg)


class InvalidStudentId(ValidationException):
    def __init__(self):
        ValidationException.__init__(self, "Invalid student ID.")


class InvalidStudentName(ValidationException):
    def __init__(self):
        ValidationException.__init__(self, "Invalid student name.")


class InvalidStudentGroup(ValidationException):
    def __init__(self):
        ValidationException.__init__(self, "Invalid student group.")


class InvalidProblemLab(ValidationException):
    def __init__(self):
        ValidationException.__init__(self, "Invalid problem lab.")


class InvalidProblemNumber(ValidationException):
    def __init__(self):
        ValidationException.__init__(self, "Invalid problem number.")


class InvalidProblemDeadline(ValidationException):
    def __init__(self):
        ValidationException.__init__(self, "Invalid problem deadline.")


class InvalidProblemDescription(ValidationException):
    def __init__(self):
        ValidationException.__init__(self, "Invalid problem description.")


class InvalidAsignId(ValidationException):
    def __init__(self):
        ValidationException.__init__(self, "Invalid assignment ID.")


class InvalidAsignLab(ValidationException):
    def __init__(self):
        ValidationException.__init__(self, "Invalid assignment lab.")


class InvalidAsignProblem(ValidationException):
    def __init__(self):
        ValidationException.__init__(self, "Invalid assignment problem.")


class InvalidAsignGrade(ValidationException):
    def __init__(self):
        ValidationException.__init__(self, "Invalid assignment grade.")


class CoruptedFileException(Exception):
    def __init__(self):
        pass