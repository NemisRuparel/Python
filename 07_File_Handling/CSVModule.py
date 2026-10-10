
import csv
from pathlib import Path

# Create a directory for practice files
folder = Path("07_File_Handling")
folder.mkdir(exist_ok=True)

file_path = folder / "students.csv"

# 1. Write data to a CSV file
students = [
    {"name": "Amit", "age": 20, "marks": 85},
    {"name": "Neha", "age": 21, "marks": 92},
    {"name": "Raj", "age": 19, "marks": 78},
]

fieldnames = ["name", "age", "marks"]

with open(file_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)

print("CSV file created successfully.")


# 2. Read rows using csv.reader()
print("\nReading rows:")

with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# 3. Read records using csv.DictReader()
print("\nReading student records:")

with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for student in reader:
        print(
            f"Name: {student['name']}, "
            f"Age: {student['age']}, "
            f"Marks: {student['marks']}"
        )


# 4. Calculate average marks
total_marks = 0
student_count = 0

with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for student in reader:
        total_marks += float(student["marks"])
        student_count += 1

if student_count > 0:
    average = total_marks / student_count
    print(f"\nAverage marks: {average:.2f}")


# 5. Append a new student
with open(file_path, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Priya", 22, 88])

print("\nNew student appended successfully.")


# 6. Display the final CSV content
print("\nFinal CSV content:")

with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for student in reader:
        print(student)


# 7. Handle a missing CSV file
try:
    with open(
        folder / "missing.csv",
        "r",
        newline="",
        encoding="utf-8"
    ) as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

except FileNotFoundError:
    print("\nError: CSV file not found.")
