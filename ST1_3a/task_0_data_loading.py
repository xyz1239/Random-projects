import csv
import tabulate as tb

class Student: 
    def __init__(self, student_id, name, student_type):
        self.__student_id = student_id
        self.__name = name
        self.__student_type = student_type

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
    
    def __str__(self):
        return f"{self.course_name} (Code: {self.course_code}, Enrolled: 0/{self.max_capacity})"

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
   
"""
wooo
hooo
"""

if __name__ == "__main__":
    main()
