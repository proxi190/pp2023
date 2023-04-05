import math
import numpy as np
import curses

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def get_mark(self, course):
        return self.marks[course]

    def set_mark(self, course, mark):
        self.marks[course] = mark

    def calculate_gpa(self, courses):
        total_credits = 0
        total_marks = 0
        for course in courses:
            if course.get_id() in self.marks:
                total_credits += course.get_credit()
                total_marks += course.get_credit() * self.get_mark(course.get_id())
        if total_credits > 0:
            self.gpa = math.floor((total_marks / total_credits) * 10) / 10
        else:
            self.gpa = 0

    def get_gpa(self):
        return self.gpa


class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_credit(self):
        return self.credit


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_number_of_students(self):
        while True:
            try:
                num_students = int(input("Enter the number of students: "))
                if num_students > 0:
                    return num_students
                else:
                    print("Invalid input. Please enter a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

    def input_student_information(self, num_students):
        for i in range(num_students):
            print(f"Enter information for student #{i + 1}:")
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth (dd/mm/yyyy): ")
            student = Student(id, name, dob)
            self.students.append(student)

    def input_number_of_courses(self):
        while True:
            try:
                num_courses = int(input("Enter the number of courses: "))
                if num_courses > 0:
                    return num_courses
                else:
                    print("Invalid input. Please enter a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

    def input_course_information(self, num_courses):
        for i in range(num_courses):
            print(f"Enter information for course #{i + 1}:")
            id = input("Enter course ID: ")
            name = input("Enter course name: ")
            while True:
                try:
                    credit = int(input("Enter course credit: "))
                    if credit > 0:
                        break
                    else:
                        print("Invalid input. Please enter a positive integer.")
                except ValueError:
                    print("Invalid input. Please enter a positive integer.")
            course = Course(id, name, credit)
            self.courses.append(course)

    def select_course_and_input_marks(self):
        while True:
            selected_course_id = input("Enter the ID of the selected course: ")
            selected_course = None
            for course in self.courses:
                if course.get_id() == selected_course_id:
                    selected_course = course
                    break
            if selected_course is not None:
                break
            else:
                print("Invalid course ID. Please try again.")
        
        for student in self.students:
            while True:
                try:
                    mark = float(input(f"Enter mark for student {student.get_name()}: "))
                    if mark >= 0 and mark <= 100:
                        mark = math.floor(mark * 10) / 10
                        student.set_mark(selected_course.get_id(), mark)
                        break
                    else:
                        print("Invalid input. Please enter a number between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 100.")

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(f"ID: {course.get_id()}, Name: {course.get_name()}, Credit: {course.get_credit()}")

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(f"ID: {student.get_id()}, Name: {student.get_name()}, DoB: {student.get_dob()}")

    def show_student_marks_for_course(self, course_id):
        print(f"Student marks for course {course_id}:")
        for student in self.students:
            mark = student.get_mark(course_id)
            print(f"Student ID: {student.get_id()}, Name: {student.get_name()}, Mark: {mark}")

    def calculate_gpa_for_all_students(self):
        for student in self.students:
            student.calculate_gpa(self.courses)

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: student.get_gpa(), reverse=True)

    def show_students_sorted_by_gpa(self):
        print("Students sorted by GPA (descending):")
        for student in self.students:
            print(f"Student ID: {student.get_id()}, Name: {student.get_name()}, GPA: {student.get_gpa()}")


def main():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

    try:
        sms = StudentManagementSystem()

        num_students = sms.input_number_of_students()
        sms.input_student_information(num_students)

        num_courses = sms.input_number_of_courses()
        sms.input_course_information(num_courses)

        while True:
            sms.list_courses()
            sms.select_course_and_input_marks()

            choice = input("Do you want to input marks for another course? (y/n): ")
            if choice.lower() != 'y':
                break

        sms.calculate_gpa_for_all_students()
        sms.sort_students_by_gpa()
        sms.show_students_sorted_by_gpa()

    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()


if __name__ == '__main__':
    main()

    