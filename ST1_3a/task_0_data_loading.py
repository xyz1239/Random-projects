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

    