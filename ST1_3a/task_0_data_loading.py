import csv
import tabulate as tb

"cd . \ST1_3a\ "

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



#These might need to be chnaged to protected rather than private, need to check task requirements
class students: 
    def __init__(self, student_id,name,student_type):
        self.name = name
        self.student_id = student_id
        self.student_type = student_type

    def __str__(self):
        return f"{self.name} {self.student_id} {self.student_type}"
    
class courses:
    def __init__(self,course_code,course_name,max_capacity):
        self.course_code = course_code
        self.course_name = course_name
        self.max_capacity = max_capacity
    def __str__(self):
        return f"{self.course_code} {self.course_name} {self.max_capacity}"
    