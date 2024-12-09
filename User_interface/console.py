from colorama import Fore, Style
from User_interface.menus import main_menu, menu_gestioneaza, menu_statistici
from Manager.student_manager import StudentManager
from Manager.problem_manager import ProblemManager
from Manager.grades_manager import GradesManager
from Exceptions.exceptions import RepositoryException, ValidationException, ManagementException


class Console:

    def __init__(self,
                 student_manager: StudentManager,
                 problem_manager: ProblemManager,
                 grades_manager: GradesManager):
        """
        Initializes the Console class with managers for students, problems, and grades.
        :param student_manager: Manager for student operations
        :param problem_manager: Manager for problem operations
        :param grades_manager: Manager for grades operations
        """
        self.__student_manager = student_manager
        self.__problem_manager = problem_manager
        self.__grades_manager = grades_manager

    @staticmethod
    def create_int(message):
        """
        Requests an input and checks if it can be converted to int.
        :param message: The message to display when requesting input
        :return: The input converted to int
        """
        while True:
            user_input = input(message)
            user_input.strip()
            try:
                user_input = int(user_input)
            except ValueError as e:
                print(Fore.RED + 'ERROR:' + str(e) + Style.RESET_ALL)
            if isinstance(user_input, int):
                return user_input

    @staticmethod
    def create_str(message):
        """
        Requests an input and returns it as a string.
        :param message: The message to display when requesting input
        :return: The input as a string
        """
        user_input = input(message)
        user_input.strip()
        return user_input

    @staticmethod
    def successful_operation():
        """
        Prints a success message.
        :return: None
        """
        print(Fore.GREEN + 'Action was executed!' + Style.RESET_ALL)

    @staticmethod
    def print_error(error):
        """
        Prints an error message.
        :param error: The error message to print
        :return: None
        """
        print(Fore.RED + 'ERROR: ' + str(error) + Style.RESET_ALL)

    # ______________________________________________________________STUDENT

    def add_default_students(self):
        """
        Adds a list of default students.
        :return: None
        """
        students_to_add = [
            (345, 'Popescu', 2),
            (427, 'Andrei Mihail', 6),
            (632, 'Elena', 3),
            (543, 'George', 6),
            (943, 'Ana', 9),
            (628, 'Karina', 4)]
        try:
            for student_data in students_to_add:
                self.__student_manager.add_student(*student_data)
        except RepositoryException as e:
            self.print_error(e)

    def add_student_ui(self):
        """
        Adds a student with user input.
        :return: None
        """
        new_id = Console.create_int('ID: ')
        new_name = Console.create_str('Name: ')
        new_grup = Console.create_int('Group: ')
        try:
            self.__student_manager.add_student(new_id, new_name, new_grup)
            self.successful_operation()
        except ManagementException as e:
            self.print_error(e)

    def remove_student_ui(self):
        """
        Removes a student with user input.
        :return: None
        """
        searched_id = Console.create_int('ID: ')
        try:
            self.__student_manager.remove_student(searched_id)
            self.successful_operation()
        except ManagementException as e:
            self.print_error(e)

    def modify_student_ui(self):
        """
        Modifies a student with user input.
        :return: None
        """
        searched_id = self.create_int('ID of the student you want to modify: ')
        if not self.__student_manager.does_exist_student(searched_id):
            print(Fore.RED + 'The entered ID does not exist!' + Style.RESET_ALL)
            return
        print('What do you want to modify?')
        print('1) ID \n2) Name \n3) Group')
        what_to_modify = self.create_int('Enter the number: ')
        try:
            if what_to_modify == 1:
                new_id = self.create_int('New ID: ')
                if self.__student_manager.does_exist_student(new_id):
                    print(Fore.RED + 'The entered ID already exists!' + Style.RESET_ALL)
                    return
                self.__student_manager.modify_student_id(searched_id, new_id)
            elif what_to_modify == 2:
                new_name = self.create_str('New name: ')
                self.__student_manager.modify_student_name(searched_id, new_name)
            elif what_to_modify == 3:
                new_grup = self.create_int('New group:')
                self.__student_manager.modify_student_grup(searched_id, new_grup)
        except (ValidationException, RepositoryException) as e:
            self.print_error(e)

    def search_student_ui(self):
        """
        Searches for a student with user input.
        :return: None
        """
        searched_id = self.create_int('Student ID: ')
        if not self.__student_manager.does_exist_student(searched_id):
            print(Fore.RED + 'The entered ID does not exist!' + Style.RESET_ALL)
            return
        student = self.__student_manager.get_student_manager(searched_id)
        print(student)

    @staticmethod
    def print_all_students_ui(students_list):
        """
        Displays the list of students.
        :param students_list: List of students
        :return: None
        """
        for student in students_list:
            print(student)

    def generate_student_ui(self):
        """
        Generates a specified number of students.
        :return: None
        """
        try:
            count = self.create_int("How many students? \n-->")
            self.__student_manager.recursive_generate_students(count)
        except ManagementException as e:
            self.print_error(e)


    # ___________________________________________________________PROBLEM

    def add_default_problems(self):
        """
        Adds a list of default problems.
        :return: None
        """
        problems_to_add = [
            (3, 5, 23, 'calculators'),
            (5, 8, 14, 'store'),
            (6, 10, 7, 'prime numbers'),
            (6, 3, 9, 'complex numbers'),
            (7, 1, 18, 'football team'),
            (8, 7, 28, 'boxes'),
            (8, 4, 23, 'web page')]
        try:
            for problem_data in problems_to_add:
                self.__problem_manager.add_problem(*problem_data)
        except ManagementException as e:
            self.print_error("Problems already added.")

    def add_problem_ui(self):
        """
        Adds a problem with user input.
        :return: None
        """
        lab_nr = self.create_int("Lab number: ")
        prob_nr = self.create_int("Problem number: ")
        deadline = self.create_int("Deadline: ")
        description = self.create_str("Description: ")
        try:
            self.__problem_manager.add_problem(lab_nr, prob_nr, deadline, description)
            self.successful_operation()
        except (RepositoryException, ValidationException) as e:
            self.print_error(e)

    def delete_problem_ui(self):
        """
        Deletes a problem with user input.
        :return: None
        """
        lab_nr_del = self.create_int("Lab number: ")
        prob_nr_del = self.create_int("Problem number: ")
        try:
            self.__problem_manager.delete_problem(lab_nr_del, prob_nr_del)
            self.successful_operation()
        except ManagementException as e:
            self.print_error(e)

    def modify_problem_ui(self):
        """
        Modifies a problem with user input.
        :return: None
        """
        searched_lab_nr = self.create_int('Lab number: ')
        searched_prob_nr = self.create_int("Problem number: ")
        if not self.__problem_manager.does_exist_problem(searched_lab_nr, searched_prob_nr):
            print(Fore.RED + 'The problem does not exist!' + Style.RESET_ALL)
            return
        print('What do you want to modify?')
        print('1) Lab number \n2) Problem number \n3) Deadline \n4) Description')
        what_to_modify = self.create_int('Enter the number: ')
        try:
            if what_to_modify == 1:
                new_lab_nr = self.create_int('New lab number: ')
                if self.__student_manager.does_exist_student(new_lab_nr):
                    print(Fore.RED + 'The entered lab number already exists!' + Style.RESET_ALL)
                    return
                self.__problem_manager.modify_lab_number(searched_lab_nr, searched_prob_nr, new_lab_nr)
            elif what_to_modify == 2:
                new_problem_nr = self.create_int('New problem number: ')
                self.__problem_manager.modify_problem_number(searched_lab_nr, searched_prob_nr, new_problem_nr)
            elif what_to_modify == 3:
                new_deadline = self.create_int('New deadline:')
                self.__problem_manager.modify_deadline(searched_lab_nr, searched_prob_nr, new_deadline)
            elif what_to_modify == 4:
                new_description = self.create_str("New description: ")
                self.__problem_manager.modify_description(searched_lab_nr, searched_prob_nr, new_description)
        except ManagementException as e:
            self.print_error(e)

    def search_problem_ui(self):
        """
        Searches for a problem with user input.
        :return: None
        """
        searched_lab_nr = self.create_int('Lab number: ')
        searched_problem_nr = self.create_int("Problem number: ")
        if not self.__problem_manager.does_exist_problem(searched_lab_nr, searched_problem_nr):
            print(Fore.RED + 'The entered problem does not exist!' + Style.RESET_ALL)
            return
        student = self.__problem_manager.get_problem_manager(searched_lab_nr, searched_problem_nr)
        print(student)

    @staticmethod
    def print_all_problms_ui(problems_list: list):
        """
        Displays the entire list of problems.
        :param problems_list: List of problems
        :return: None
        """
        for probl in problems_list:
            print(probl)

    def generate_problems_ui(self):
        """
        Generates a specified number of problems.
        :return: None
        """
        try:
            count = self.create_int("How many problems? \n-> ")
            self.__problem_manager.generate_problems(count)
        except ManagementException as e:
            self.print_error(e)

    # ___________________________________________________________________ASIGN AND STATS

    def add_default_assigments(self):
        """
        Adds a list of default assignments.
        :return: None
        """
        assigments_to_add = [
            (345, 5, 8, 7),
            (632, 3, 5, 7),
            (632, 6, 10, 4),
            (543, 3, 5, 4),
            (543, 7, 1, 3),
            (345, 6, 10, 6),
            (427, 6, 10, 3),
            (943, 6, 10, 9),
            (543, 8, 7, 6),
            (345, 6, 3, 2)]
        try:
            for assigments_data in assigments_to_add:
                self.__grades_manager.add_grade(*assigments_data)
        except ManagementException as e:
            self.print_error(e)

    def asign_ui(self):
        """
        Assigns a grade with user input.
        :return: None
        """
        student_id = self.create_int("Student ID: ")
        lab_nr = self.create_int("Lab number: ")
        problema = self.create_int("Problem number: ")
        grade = self.create_int("Grade: ")
        try:
            self.__grades_manager.add_grade(student_id, lab_nr, problema, grade)
            self.successful_operation()
        except ManagementException as e:
            self.print_error(e)

    def order_for_problem_ui(self):
        """
        Orders students for a problem based on user input.
        :return: None
        """
        lab = self.create_int("Lab: ")
        problem = self.create_int("Problem: ")
        print("In what order should they appear?")
        print("  1) Alphabetically by name")
        print("  2) Ascending by grade")
        order = self.create_int("-> ")
        try:
            if order == 1:
                name_and_grade_list = self.__grades_manager.for_a_problem_order_alphabetically(lab, problem)
                for i in name_and_grade_list:
                    print(
                        Fore.CYAN + "Name: " + str(i[0]) +
                        Fore.BLACK + " | " +
                        Fore.RED + "Grade: " + str(i[1]) +
                        Style.RESET_ALL)
            elif order == 2:
                name_and_grade_list = self.__grades_manager.for_a_problem_order_by_grade(lab, problem)
                for i in name_and_grade_list:
                    print(
                        Fore.RED + "Grade: " + str(i[0]) +
                        Fore.BLACK + " | " +
                        Fore.CYAN + "Name: " + str(i[1]) +
                        Style.RESET_ALL)
        except ManagementException as e:
            self.print_error(e)

    def average_below_5_ui(self):
        """
        Displays students with an average grade below 5.
        :return: None
        """
        average_below_5_list = self.__grades_manager.average_below_5()
        if len(average_below_5_list) == 0:
            print(Fore.GREEN + "All have an average above 5." + Style.RESET_ALL)
        for i in average_below_5_list:
            print(
                Fore.RED + "Average:" + str(i[0]) +
                Fore.BLACK + " | " +
                Fore.CYAN + "Name: " + str(i[1]) +
                Style.RESET_ALL)

    @staticmethod
    def print_all_grades_ui(grades_list: list):
        """
        Displays the entire list of grades.
        :param grades_list: List of grades
        :return: None
        """
        for asign in grades_list:
            print(asign)

    # ___________________________________________________________________________RUN

    def run(self):
        """
        Runs the main menu and handles user input.
        :return: None
        """
        while True:
            main_menu()
            option = self.create_str('Option: ')

            # Manage student list
            if option == "1":
                menu_gestioneaza()
                second_option = self.create_int('Option: ')
                if second_option == 1:
                    self.add_student_ui()
                elif second_option == 2:
                    self.remove_student_ui()
                elif second_option == 3:
                    self.modify_student_ui()

            # Manage problem list
            elif option == "2":
                menu_gestioneaza()
                second_option = self.create_int('Option: ')
                if second_option == 1:
                    self.add_problem_ui()
                if second_option == 2:
                    self.delete_problem_ui()
                if second_option == 3:
                    self.modify_problem_ui()

            # Search student
            elif option == "3":
                self.search_student_ui()

            # Search problem
            elif option == "4":
                self.search_problem_ui()

            # Assign a grade
            elif option == "5":
                self.asign_ui()

            # Statistics
            elif option == "6":
                menu_statistici()
                second_option = self.create_int("Option: ")
                if second_option == 1:
                    self.order_for_problem_ui()
                elif second_option == 2:
                    self.average_below_5_ui()

            # Show all students
            elif option == "7":
                self.print_all_students_ui(self.__student_manager.get_students_list_manager())

            # Show all problems
            elif option == "8":
                self.print_all_problms_ui(self.__problem_manager.get_problem_list_manager())

            # Show all grades
            elif option == "9":
                self.print_all_grades_ui(self.__grades_manager.get_grades_list_manager())

            # Generate random students
            elif option == 'gs':
                self.generate_student_ui()

            # Generate random problems
            elif option == 'gp':
                self.generate_problems_ui()

            elif option == 's':
                self.add_default_students()

            elif option == 'p':
                self.add_default_problems()

            elif option == 'g':
                self.add_default_assigments()

            # Done
            elif option == "x":
                break

            else:
                print(Fore.RED + 'Invalid option!' + Style.RESET_ALL)