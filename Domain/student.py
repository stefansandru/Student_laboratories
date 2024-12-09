from colorama import Fore, Style


class Student:
    def __init__(self, student_id: int, name: str, group: int):
        self.__ID = student_id
        self.__name = name
        self.__group = group

    def get_ID(self):
        return self.__ID

    def get_name(self):
        return self.__name

    def get_group(self):
        return self.__group

    def set_ID(self, new_id):
        self.__ID = new_id

    def set_name(self, new_name):
        self.__name = new_name

    def set_group(self, new_group):
        self.__group = new_group

    def __str__(self):
        return Fore.BLUE + "ID: "+str(self.get_ID()) + Style.RESET_ALL + \
            " | " + Fore.GREEN + "Name: " + self.get_name() + Style.RESET_ALL + \
            " | " + Fore.MAGENTA + "Group:" + str(self.get_group()) + Style.RESET_ALL

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.__ID == other.get_ID()
        return False
