import csv
import tabulate as tb

class students: 
    def __init__(self, student_id, name, student_type):
        self.__student_id = student_id
        self.__name = name
        self.__student_type = student_type

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

    
class courses:
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

def read_csv():
    with open("students.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader]
        
        print(tb.tabulate(data, headers=header, tablefmt="grid"))


    with open("courses.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader]
        
        print(tb.tabulate(data, headers=header, tablefmt="grid"))


def main():
    