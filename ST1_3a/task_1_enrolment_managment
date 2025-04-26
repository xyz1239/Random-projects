import csv
import tabulate as tb
import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class Student: 
    def __init__(self, student_id, name, student_type):
        self.__student_id = student_id
        self.__name = name
        self.__student_type = student_type
        self.__enrolled_courses = []

#I belive this is what it asked for, could be wrong though
    @property
    def student_id(self):
        return self.__student_id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def student_type(self):
        return self.__student_type
    

    def can_enroll(self):
        return len(self.can_enroll) < 4
    
    def enroll(self, course):
        if course in self.__enrolled_courses:
            print(f"{self.name}Already enrolled in {course.course_name}.")
        elif not self.can_enroll():
            print(f"{self.name} cannot enroll in more courses.")
        else:
            self.__enrolled_courses.append(course)
            print(f"{self.name} enrolled in {course.course_name}.")
    
    def __str__(self):
        return f"{self.name} (ID: {self.student_id}, Type: {self.student_type})"

    
class Course:
    def __init__(self, course_code, course_name, max_capacity):
        self.__course_code = course_code
        self.__course_name = course_name
        self.__max_capacity = int(max_capacity)

    @property
    def course_code(self):
        return self.__course_code
    
    @property
    def course_name(self):
        return self.__course_name
    
    @property
    def max_capacity(self):
        return self.__max_capacity
    
    def addstudent(self, student):
        if len(self.__enrolled_students) >= self.max_capacity:
            print(f"{self.course_name} is full.")
        elif student in self.__enrolled_students:
            print(f"{student.name} is already enrolled in {self.course_name}.")
        elif not student.can_enroll():
            print(f"{student.name} cannot enroll in more courses.")
        else:
            self.__enrolled_students.append(student)
            print(f"{student.name} enrolled in {self.course_name}.")
    
    def __str__(self):
        return f"{self.course_name} (Code: {self.course_code}, Enrolled: 0/{self.max_capacity})"
    
def menu(students, courses):
    while True:
        print("\nMenu:")
        print("1. Enroll in a course")
        print("2. View enrolled courses")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            student_id = input("Enter student ID: ")
            course_code = input("Enter course code: ")
            
            student = next((s for s in students if s.student_id == student_id), None)
            course = next((c for c in courses if c.course_code == course_code), None)
            
            if student and course:
                student.enroll(course)
                course.addstudent(student)
            else:
                print("Invalid student ID or course code.")
        
        elif choice == "2":
            student_id = input("Enter student ID: ")
            student = next((s for s in students if s.student_id == student_id), None)
            
            if student:
                print(f"Enrolled courses for {student.name}:")
                for course in student._Student__enrolled_courses:
                    print(course.course_name)
            else:
                print("Invalid student ID.")
        
        elif choice == "3":
            wait_time = 5
            for i in range(wait_time, 0, -1):
                    print(f"Exiting in {i} seconds...", end="\r")
                    time.sleep(1)
                    clear_console()
                    print("Goodbye!")
                    time.sleep(1)
                    clear_console()
                    quit()
                    break
            else:
                print("Invalid choice. Please try again.")

def main():
    students = []
    courses = []
    
    with open("students.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for student_id, name, student_type in reader:
            students.append(Student(student_id, name, student_type))

    with open("courses.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for course_code, course_name, max_capacity in reader:
            courses.append(Course(course_code, course_name, max_capacity))

    print (f"Initialized {len(students)} students and {len(courses)} courses.")
    
    student_table = [[student.student_id, student.name, student.student_type] for student in students]
    print("Students:")
    print(tb.tabulate(student_table, headers=["Student ID", "Name", "Type"], tablefmt="grid"))
    
    course_table = [[course.course_code, course.course_name, course.max_capacity] for course in courses]
    print("Courses:")
    print(tb.tabulate(course_table, headers=["Course Code", "Course Name", "Max Capacity"], tablefmt="grid"))
   
    menu(students, courses)

if __name__ == "__main__":
    main()
