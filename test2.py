import math
import numpy as np

class Student:
    def __init__(self, id, name, dob):
        self._id = id
        self._name = name
        self._dob = dob
        self._marks = {}

    def id(self):
        return self._id

    def name(self):
        return self._name

    def dob(self):
        return self._dob

    def marks(self):
        return self._marks

    def add_mark(self, course_id, mark):
        self._marks[course_id] = math.floor(mark * 10) / 10

    def get_gpa(self, courses):
        credits = []
        marks = []
        for course in courses:
            mark = self._marks.get(course.id)
            if mark is not None:
                credits.append(course.credits)
                marks.append(mark)
        if len(credits) == 0:
            return 0
        return np.average(marks, weights=credits)

class Course:
    def __init__(self, id, name, credits):
        self._id = id
        self._name = name
        self._credits = credits

    def id(self):
        return self._id

    def name(self):
        return self._name

    def credits(self):
        return self._credits

class StudentMarkManagementSystem:
    def __init__(self):
        self._students = {}
        self._courses = {}
    
    def students(self):
        return self._students

    def courses(self):
        return self._courses

    def add_student(self, student):
        self._students[student.id] = student

    def add_course(self, course):
        self._courses[course.id] = course

    def get_student_marks(self, student_id, course_id):
        student = self._students.get(student_id)
        if student is None:
            return []
        return [student.marks.get(course_id, 0)]

    def add_marks(self, course_id):
        course = self._courses.get(course_id)
        if course is None:
            return False
        for student in self._students.values():
            mark = input(f"Enter mark for {student.name}: ")
            try:
                mark = float(mark)
            except ValueError:
                return False
            student.add_mark(course_id, mark)
        return True

    def get_students_for_course(self, course_id):
        students = []
        for student in self._students.values():
            if course_id in student.marks:
                students.append(student)
        return students

    def get_student_list_sorted_by_gpa(self, courses):
        return sorted(self._students.values(), key=lambda s: s.get_gpa(courses), reverse=True)

if __name__ == "__main__":
    import curses

    def input_number_of_students(stdscr):
        stdscr.clear()
        stdscr.addstr("Enter number of students: ")
        stdscr.refresh()
        num_students = stdscr.getstr().decode()
        try:
            num_students = int(num_students)
            return num_students
        except ValueError:
            return None
        
    def input_student_info(stdscr):
        stdscr.clear()
        stdscr.addstr("Enter student information:\n")
        id = input_with_prompt(stdscr, "ID: ")
        name = input_with_prompt(stdscr, "Name: ")
        dob = input_with_prompt(stdscr, "Date of Birth (YYYY-MM-DD): ")
        return Student(id, name, dob)

    def input_number_of_courses(stdscr):
        stdscr.clear()
        stdscr.addstr("Enter number of courses: ")
        stdscr.refresh()
        num_courses = stdscr.getstr().decode()
        try:
            num_courses = int(num_courses)
            return num_courses
        except ValueError:
            return None

    def input_course_info(stdscr):
        stdscr.clear()
        stdscr.addstr("Enter course information:\n")
        id = input_with_prompt(stdscr, "ID: ")
        name = input_with_prompt(stdscr, "Name: ")
        credits = input_with_prompt(stdscr, "Credits: ")
        try:
            credits = float(credits)
            return Course(id, name, credits)
        except ValueError:
            return None

    def select_course(stdscr, courses):
        stdscr.clear()
        stdscr.addstr("Select a course:\n")
        for i, course in enumerate(courses):
            stdscr.addstr(f"{i+1}. {course.name}\n")
        stdscr.refresh()
        choice = stdscr.getstr().decode()
        try:
            choice = int(choice)
            if choice >= 1 and choice <= len(courses):
                return courses[choice-1]
            else:
                return None
        except ValueError:
            return None

    def input_with_prompt(stdscr, prompt):
        stdscr.addstr(prompt)
        stdscr.refresh()
        return stdscr.getstr().decode()

    def list_courses(stdscr, courses):
        stdscr.clear()
        stdscr.addstr("List of courses:\n")
        for course in courses:
            stdscr.addstr(f"{course.id} - {course.name} ({course.credits} credits)\n")
        stdscr.refresh()
        stdscr.getch()

    def list_students(stdscr, students):
        stdscr.clear()
        stdscr.addstr("List of students:\n")
        for student in students:
            stdscr.addstr(f"{student.id} - {student.name} ({student.dob})\n")
        stdscr.refresh()
        stdscr.getch()

    def list_student_marks(stdscr, students, course):
        stdscr.clear()
        stdscr.addstr(f"Marks for course {course.name}:\n")
        for student in students:
            mark = student.marks.get(course.id)
            stdscr.addstr(f"{student.id} - {student.name}: {mark if mark is not None else '-'}\n")
        stdscr.refresh()
        stdscr.getch()

    def list_students_sorted_by_gpa(stdscr, students):
        stdscr.clear()
        stdscr.addstr("Students sorted by GPA:\n")
        for student in students:
            stdscr.addstr(f"{student.id} - {student.name}: {student.get_gpa(smms.courses):.1f}\n")
        stdscr.refresh()
        stdscr.getch()

    def run_interface(stdscr, smms):
        stdscr.clear()
        stdscr.addstr("Hello")

    smms = StudentMarkManagementSystem()
    curses.wrapper(run_interface, smms)

    
   
        

