
from pathlib import Path

# Create a directory for practice files
folder = Path("07_File_Handling")
folder.mkdir(exist_ok=True)

file_path = folder / "FileHandlingTest.txt"

# 1. Write to a file
with open(file_path, "w", encoding="utf-8") as file:
    file.write("Hello, Python!\n")
    file.write("Learning file handling.\n")

print("File created and written successfully.")


# 2. Read the entire file
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

print("\nFile content:")
print(content)


# 3. Read one line
with open(file_path, "r", encoding="utf-8") as file:
    first_line = file.readline()

print("First line:", first_line.strip())


# 4. Read all lines into a list
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

print("All lines:", lines)


# 5. Append new content
with open(file_path, "a", encoding="utf-8") as file:
    file.write("This line was appended.\n")

print("\nContent appended successfully.")


# 6. Check whether the file exists
if file_path.exists() and file_path.is_file():
    print("File exists:", file_path)


# 7. Read the updated content
print("\nUpdated file content:")
print(file_path.read_text(encoding="utf-8"))


# 8. Handle a missing file
missing_file = folder / "missing.txt"

try:
    with open(missing_file, "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: The requested file does not exist.")


# 9. Display the file size
print("File size:", file_path.stat().st_size, "bytes")
