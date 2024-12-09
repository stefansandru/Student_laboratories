from colorama import Fore, Style


class Asign:

    def __init__(self, student_id, lab, problem, grade):
        self.__student_id = student_id
        self.__lab = lab
        self.__problem = problem
        self.__grade = grade

    def get_student_id(self):
        return self.__student_id

    def get_lab(self):
        return self.__lab

    def get_problem(self):
        return self.__problem

    def get_grade(self):
        return self.__grade

    def set_studnet_id(self, new):
        self.__student_id = new

    def set_lab(self, new):
        self.__lab = new

    def set_problem(self, new):
        self.__problem = new

    def set_grade(self, new):
        self.__grade = new

    def __str__(self):
        return Fore.BLUE + "Student ID: " + str(self.get_student_id()) + Style.RESET_ALL + \
            " | " + Fore.GREEN + "Laborator: " + str(self.get_lab()) + Style.RESET_ALL + \
            " | " + Fore.MAGENTA + "Problem:" + str(self.get_problem()) + Style.RESET_ALL + \
            " | " + Fore.RED + "Nota: " + str(self.get_grade()) + Style.RESET_ALL

    def __eq__(self, other):
        if isinstance(other, Asign):
            return (self.__student_id == self.get_student_id() and
                    self.__lab == other.get_lab() and
                    self.__problem == other.get_problem()
                    )
        return False
