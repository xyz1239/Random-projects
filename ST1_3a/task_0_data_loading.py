import csv
import tabulate as tb

with open("students.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    data = [row for row in reader]


print(tb.tabulate(data, headers=header, tablefmt="grid"))


    

    