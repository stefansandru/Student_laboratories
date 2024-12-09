from colorama import Fore, Style


class Problem:

    def __init__(self, lab_nr, problem_nr, deadline, description):
        self.__lab_nr = lab_nr
        self.__problem_nr = problem_nr
        self.__deadline = deadline
        self.__description = description

    def get_lab_nr(self):
        return self.__lab_nr

    def get_problem_nr(self):
        return self.__problem_nr

    def get_description(self):
        return self.__description

    def get_deadline(self):
        return self.__deadline

    def set_lab_nr(self, new_numar_lab):
        self.__lab_nr = new_numar_lab

    def set_problem_nr(self, new_numar_problema):
        self.__problem_nr = new_numar_problema

    def set_description(self, new_descriere):
        self.__description = new_descriere

    def set_deadline(self, new_deadline):
        self.__deadline = new_deadline

    def __str__(self):
        return Fore.BLUE + f'Nr lab: {str(self.get_lab_nr())}' + Style.RESET_ALL + ' ; ' + \
            Fore.MAGENTA + f'Nr problrma: {str(self.get_problem_nr())}' + Style.RESET_ALL + ' ; ' + \
            Fore.CYAN + f'Deadline: {str(self.get_deadline())}' + Style.RESET_ALL + ' ; ' + \
            Fore.GREEN + f'Descriere: {str(self.get_description())}' + Style.RESET_ALL + ' ; '

    def __eq__(self, other):
        if isinstance(other, Problem):
            return (
                self.get_lab_nr() == other.get_lab_nr() and
                self.get_problem_nr() == other.get_problem_nr()
                )
        return False
