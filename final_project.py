
import random
class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = random.randint(1000, 9999)
        self.course_name = course_name
        self.course_mark = course_mark
class Student:
    total_students = 0
    def __init__(self, student_number, student_name, student_age):
        self.student_id = random.randint(10000, 99999)
        self.student_number = student_number
        self.student_name = student_name
        self.student_age = student_age
        self.courses_list = []
        Student.total_students += 1
    def enroll_course(self, course_name, course_mark):
        course = Course(course_name, course_mark)
        self.courses_list.append(course)
    def get_student_details(self):
        return self.__dict__
    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course ID: {course.course_id}, Name: {course.course_name}, Mark: {course.course_mark}")
    def get_student_average(self):
        if not self.courses_list:
            return 0
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list)
students_list = []
def save_data():
    with open("final_proj", "w") as file:
        for student in students_list:
            file.write(f"{student.student_number}||{student.student_name}||{student.student_age}\n")
            for course in student.courses_list:
                file.write(f"{course.course_name}||{course.course_mark}\n")
def load_data():
    try:
        with open("final_proj", "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 2):
                student_data = lines[i].strip().split(",")
                student = Student(student_data[0], student_data[1], int(student_data[2]))
                course_data = lines[i + 1].strip().split(",")
                student.enroll_course(course_data[0], float(course_data[1]))
                students_list.append(student)
    except FileNotFoundError:
        pass
while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit"))
    except ValueError:
        print("Invalid selection. Please enter a number.")
        continue
    if selection == 1:
        student_number = input("Enter Student Number: ")
        student_name = input("Enter Student Name: ")
        while True:
            try:
                student_age = int(input("Enter Student Age: "))
                break
            except ValueError:
                print("Invalid Age. Please enter a valid number.")

        student = Student(student_number, student_name, student_age)
        students_list.append(student)
        print("Student Added Successfully")
        save_data()
    elif selection == 2:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                students_list.remove(student)
                Student.total_students -= 1
                print("Student Deleted Successfully")
                break
        else:
            print("Student Not Exist")
        save_data()
        load_data()

    elif selection == 3:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                print(student.get_student_details())
                break
        else:
            print("Student Not Exist")
        save_data()
    elif selection == 4:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                print(f"Student Average: {student.get_student_average():.2f}")
                break
        else:
            print("Student Not Exist")
        save_data()
    elif selection == 5:
        student_number = input("Enter Student Number: ")
        for student in students_list:
            if student.student_number == student_number:
                course_name = input("Enter Course Name: ")
                course_mark = float(input("Enter Course Mark: "))
                student.enroll_course(course_name, course_mark)
                print("Course Added Successfully")
                break
        else:
            print("Student Not Exist")
        save_data()
    elif selection == 6:
        save_data()
        print("Exiting the program.")
        break
        save_data()
        load_data()
    else:
        print("Invalid selection. Please choose a valid option.")
save_data()
