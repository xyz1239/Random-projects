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


class students: 
    def __init__(self, student_id,name,student_type):
        self.name = name
        self.student_id = student_id
        self.student_type = student_type

    def __str__(self):
        return f"{self.name} {self.student_id} {self.student_type}"