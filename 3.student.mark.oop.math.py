import math
import numpy as np

class Student:
    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB
        self.marks = {}

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def calculate_gpa(self, courses):
        weighted_sum = 0
        total_credits = 0
        for course in courses:
            if course.id in self.marks:
                mark = self.marks[course.id]
                weighted_sum += mark * course.credits
                total_credits += course.credits
        return weighted_sum / total_credits if total_credits > 0 else 0

class Course:
    def __init__(self, id, name, credits):
        self.id = id
        self.name = name
        self.credits = credits
        self.marks = {}

    def input_marks(self, students):
        for student in students:
            mark = float(input(f"Input mark for {student.name} in {self.name}: "))
            mark = math.floor(mark * 10) / 10
            self.marks[student.id] = mark
            student.add_mark(self.id, mark)

    def display_marks(self, students):
        print(f"Marks for course {self.name}:")
        for student in students:
            if student.id in self.marks:
                mark = self.marks[student.id]
                print(f"- {student.name}: {mark}")
            else:
                print(f"- {student.name}: Not found")

class StudentMarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_student_no(self):
        student_no = int(input("Input number of students: "))
        return student_no

    def input_student_info(self):
        id = input("Input student id: ")
        name = input("Input student name: ")
        DoB = input("Input student DoB: ")
        return Student(id, name, DoB)

    def input_course_no(self):
        course_no = int(input("Input number of courses: "))
        return course_no

    def input_course_info(self):
        id = input("Input course id: ")
        name = input("Input course name: ")
        credits = int(input("Input course credits: "))
        return Course(id, name, credits)

    def display_course(self):
        print("List of courses:")
        for course in self.courses:
            print(f"- {course.id}: {course.name}: {course.credits} credits")

    def display_student(self):
        print("List of students:")
        for student in self.students:
            print(f"- {student.id}: {student.name} : {student.DoB}")

    def display_student_by_gpa(self):
        student_gpas = [(student, student.calculate_gpa(self.courses)) for student in self.students]
        sorted_students = sorted(student_gpas, key=lambda x: x[1], reverse=True)

        print("Students ranking by GPA:")
        for student, gpa in sorted_students:
            print(f"- {student.id}: {student.name} - GPA: {gpa:.2f}")

    def run(self):
        student_no = self.input_student_no()

        for i in range(student_no):
            student = self.input_student_info()
            self.students.append(student)

        course_no = self.input_course_no()

        for i in range(course_no):
            course = self.input_course_info()
            self.courses.append(course)

        while True:
            print("Choose an action:")
            print("1. Display courses")
            print("2. Display students")
            print("3. Input marks for a course")
            print("4. Display student marks for a course")
            print("5. Display students ranking by GPA")

            action = input("Choose an action: ")
            if action == "1":
                self.display_course()
            elif action == "2":
                self.display_student()
            elif action == "3":
                self.display_course()
                course_id = input("Input course id: ")
                course = next((c for c in self.courses if c.id == course_id), None)
                if course is not None:
                    course.input_marks(self.students)
                else:
                    print("Course not available. Please try again.")
            elif action == "4":
                self.display_course()
                course_id = input("Input course id: ")
                course = next((c for c in self.courses if c.id == course_id), None)
                if course is not None:
                    course.display_marks(self.students)
                else:
                    print("Course not available. Please try again.")
            elif action == "5":
                self.display_student_by_gpa()
            else:
                print("Section not available. Please try again.")

program = StudentMarkManagementSystem()
program.run()