# Dictionary

# Creating a Dictionary
student = {
    "name": "Nemis",
    "age": 20,
    "marks": 85.5
}

print("Student:", student)

# Accessing Values
print("Name:", student["name"])
print("Age:", student.get("age"))

# Adding an Item
student["city"] = "Ahmedabad"
print("After adding:", student)

# Changing a Value
student["age"] = 21
print("After changing:", student)

# Checking a Key
print("name" in student)
print("grade" in student)

# Dictionary Methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Updating Dictionary
student.update({"grade": "A"})
print("After update:", student)

# Iterating Through Dictionary
for key, value in student.items():
    print(key, ":", value)

# Removing an Item
student.pop("city")
print("After removing:", student)