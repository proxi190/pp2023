import numpy as np
import curses
import math

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}
        
    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark
        
    def get_mark(self, course_id):
        return self.marks.get(course_id, None)
        
    def get_average_gpa(self, course_list):
        credits = [course.credit for course in course_list]
        marks = [self.get_mark(course.id) for course in course_list]
        gpa = np.average(marks, weights=credits)
        return round(gpa, 1)

class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit
        
class MarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.stdscr = curses.initscr()

    def input_num_students(self):
        self.num_students = int(input("Enter the number of students in the class: "))
        
    def input_student_info(self):
        for i in range(self.num_students):
            id = input(f"Enter the ID of student {i+1}: ")
            name = input(f"Enter the name of student {i+1}: ")
            dob = input(f"Enter the date of birth of student {i+1} (YYYY-MM-DD): ")
            self.students.append(Student(id, name, dob))
            
    def input_num_courses(self):
        self.num_courses = int(input("Enter the number of courses: "))
        
    def input_course_info(self):
        for i in range(self.num_courses):
            id = input(f"Enter the ID of course {i+1}: ")
            name = input(f"Enter the name of course {i+1}: ")
            credit = float(input(f"Enter the credit of course {i+1}: "))
            self.courses.append(Course(id, name, credit))
            
    def select_course(self):
        self.stdscr.addstr("Select a course:\n")
        for i, course in enumerate(self.courses):
            self.stdscr.addstr(f"{i+1}. {course.name}\n")
        course_index = int(input("Enter the course number: ")) - 1
        selected_course = self.courses[course_index]
        for student in self.students:
            mark = float(input(f"Enter the mark for student {student.name}: "))
            mark = math.floor(mark * 10) / 10  # round down to 1-digit decimal
            student.add_mark(selected_course.id, mark)
            
    def list_courses(self):
        self.stdscr.addstr("List of courses:\n")
        for i, course in enumerate(self.courses):
            self.stdscr.addstr(f"{i+1}. {course.name} ({course.credit} credits)\n")
            
    def list_students(self):
        self.stdscr.addstr("List of students:\n")
        for i, student in enumerate(self.students):
            self.stdscr.addstr(f"{i+1}. {student.name} ({student.id})\n")
            
    def show_student_marks(self):
        self.list_students()
        student_index = int(input("Enter the student number: ")) - 1
        selected_student = self.students[student_index]
        self.stdscr.addstr(f"Marks for {selected_student.name} {selected_student.id}")
        self.stdscr.addstr("Select a course:\n")
        for i, course in enumerate(self.courses):
            self.stdscr.addstr(f"{i+1}. {course.name}\n")
        course_index = int(input("Enter the course number: ")) - 1
        selected_course = self.courses[course_index]
        mark = selected_student.get_mark(selected_course.id)
        if mark is None:
            self.stdscr.addstr(f"{selected_student.name} has not taken {selected_course.name}.\n")
        else:
            self.stdscr.addstr(f"{selected_student.name} got {mark} in {selected_course.name}.\n")
            
    def sort_students_by_gpa(self):
        gpas = [student.get_average_gpa(self.courses) for student in self.students]
        sorted_indices = np.argsort(gpas)[::-1]  # sort in descending order
        self.stdscr.addstr("Students sorted by GPA:\n")
        for i, index in enumerate(sorted_indices):
            student = self.students[index]
            gpa = gpas[index]
            self.stdscr.addstr(f"{i+1}. {student.name} ({student.id}) - GPA: {gpa}\n")
            
    def run(self):
        self.input_num_students()
        self.input_student_info()
        self.input_num_courses()
        self.input_course_info()
        self.select_course()
        self.list_courses()
        self.list_students()
        self.show_student_marks()
        self.sort_students_by_gpa()
        curses.endwin()

if __name__ == "__main__":
    mms = MarkManagementSystem()
    mms.run()

