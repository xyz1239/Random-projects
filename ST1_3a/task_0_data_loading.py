import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
    delimiter = (",",)
    quotechar = ('"',)

    # Skip the header row
    next(reader)
    # Read the rest of the rows
