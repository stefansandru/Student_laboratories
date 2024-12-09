from User_interface.console import Console
from Repository.students_repository import StudentRepo
from Repository.problem_repository import ProblemRepo
from Repository.grades_repository import GradeRepo
from Manager.student_manager import StudentManager
from Manager.problem_manager import ProblemManager
from Manager.grades_manager import GradesManager
from Domain.student_validator import StudentValidator
from Domain.problem_validator import ProblemValidator
from Domain.asign_validator import GradesValidator


student_repo = StudentRepo("files/stud.txt")
problem_repo = ProblemRepo("files/problems.txt")
grades_repo = GradeRepo("files/grades.txt")

student_v = StudentValidator()
problem_v = ProblemValidator()
grades_v = GradesValidator()

student_manager = StudentManager(student_v, student_repo, grades_repo)
problem_manager = ProblemManager(problem_v, problem_repo, grades_repo)
grades_manager = GradesManager(grades_v, grades_repo, student_repo, problem_repo)

console = Console(student_manager, problem_manager, grades_manager)
console.run()

"""
Functii inpelentata recursiv: 
    recursive_calculate_average_grade - media notelor unui elev
    recursive_generate_students - genereaza un numar de studenti
    
Complexitatea recursive_generate_students 
    T(n) = n
    T(n) este de ordinul n, apartine O(n)
"""